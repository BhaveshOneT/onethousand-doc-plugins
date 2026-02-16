#!/usr/bin/env python3
"""
Hackathon Presentation Generator for One Thousand GmbH

Generates a branded, high-quality hackathon presentation from JSON content files
using a pre-designed PPTX template with 43 slide layouts.

Supports:
- Rich text formatting with mixed bold/normal text
- Card-based layouts for structured content
- Colored accent bars and visual separators
- Speaker notes on key slides
- Customizable agendas from JSON
- System landscape, key metrics, and lessons learned slides

Usage:
    python generate_hackathon_pptx.py \\
        --template ../assets/templates/ot-hackathon-template.pptx \\
        --variables variables.json \\
        --content content.json \\
        --output hackathon_presentation.pptx \\
        [--verbose]

Author: One Thousand GmbH
License: Proprietary
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from pptx import Presentation
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls


# One Thousand Brand Colors
OT_GREEN = RGBColor(0x18, 0xA0, 0x5A)
OT_DARK_GREEN = RGBColor(0x14, 0x7A, 0x46)
OT_ASH = RGBColor(0x32, 0x32, 0x32)
OT_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
OT_LIGHT_GRAY = RGBColor(0xE8, 0xE8, 0xE8)
OT_MINT_BG = RGBColor(0xF0, 0xF8, 0xF3)
OT_VERY_LIGHT_GRAY = RGBColor(0xF5, 0xF5, 0xF5)
OT_CARD_BG = RGBColor(0x3E, 0x3E, 0x3E)  # Slightly lighter than ash, for cards on dark bg
OT_MID_GRAY = RGBColor(0xBB, 0xBB, 0xBB)  # Subtle text on dark bg

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> Dict[str, Any]:
    """Load JSON file from path."""
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_layout(prs: Presentation, name: str):
    """Find a slide layout by name."""
    for layout in prs.slide_layouts:
        if layout.name == name:
            return layout
    logger.warning(f"Layout not found: {name}")
    return None


def ph_by_idx(slide, idx: int):
    """Return placeholder by idx, or None."""
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            return ph
    return None


def set_ph_text(ph, text: str, size: int = None, bold: bool = False, color: RGBColor = None):
    """Set text on a placeholder, preserving its existing formatting where possible."""
    if ph is None or not ph.has_text_frame:
        return
    tf = ph.text_frame
    tf.clear()
    p = tf.paragraphs[0]
    p.text = text
    if size:
        p.font.size = Pt(size)
    if bold:
        p.font.bold = True
    if color:
        p.font.color.rgb = color


def add_textbox(slide, left, top, width, height, text,
                font_size=14, bg_color=None, text_color=OT_ASH,
                alignment=PP_ALIGN.CENTER, bold=False, word_wrap=True,
                vertical_anchor=MSO_ANCHOR.MIDDLE):
    """Add a text box with optional background to a slide."""
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = word_wrap
    tf.vertical_anchor = vertical_anchor
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = text_color
    p.font.bold = bold
    p.alignment = alignment
    if bg_color:
        tb.fill.solid()
        tb.fill.fore_color.rgb = bg_color
    return tb


def add_bullets_textbox(slide, left, top, width, height, bullets,
                        font_size=14, text_color=OT_ASH, spacing=6):
    """Add a text box with bullet points as separate paragraphs."""
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = True
    for i, bullet in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = bullet
        p.font.size = Pt(font_size)
        p.font.color.rgb = text_color
        p.space_before = Pt(spacing)
        p.space_after = Pt(spacing)
    return tb


def slide_count(prs):
    """Return the current slide count."""
    return len(prs.slides)


# ---------------------------------------------------------------------------
# New helper functions for better formatting
# ---------------------------------------------------------------------------

def add_rich_textbox(slide, left, top, width, height, parts: List[Tuple[str, bool, int, RGBColor]],
                     alignment=PP_ALIGN.LEFT, word_wrap=True):
    """
    Add a text box with mixed formatting.

    Args:
        parts: List of (text, bold, font_size, color) tuples
        Example: [("Bold Title", True, 16, OT_ASH), (" — Normal", False, 16, OT_ASH)]
    """
    tb = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    tf = tb.text_frame
    tf.word_wrap = word_wrap

    p = tf.paragraphs[0]
    p.alignment = alignment

    for text, bold, size, color in parts:
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = color

    return tb


def add_card(slide, left, top, width, height, title, body,
             accent_color=OT_GREEN, dark_bg=True):
    """
    Add a card-style content block with colored left border, title, and body.

    Uses text boxes to create a card layout with:
    - Subtle card background (slightly lighter on dark slides)
    - Thin colored left border (accent line)
    - Bold title at top
    - Body text below
    """
    title_color = OT_WHITE if dark_bg else OT_ASH
    body_color = OT_LIGHT_GRAY if dark_bg else OT_ASH
    bg = OT_CARD_BG if dark_bg else OT_VERY_LIGHT_GRAY

    # Card background
    add_textbox(slide, left, top, width, height, "",
                font_size=1, bg_color=bg)

    # Add accent line on the left
    add_accent_line(slide, left, top, height, accent_color, thickness=Pt(4))

    # Add title
    add_textbox(slide, left + 0.2, top + 0.1, width - 0.3, 0.5, title,
                font_size=14, bold=True, text_color=title_color, alignment=PP_ALIGN.LEFT)

    # Add body text
    add_textbox(slide, left + 0.2, top + 0.6, width - 0.3, height - 0.7, body,
                font_size=12, text_color=body_color, alignment=PP_ALIGN.LEFT)

    return slide


def add_accent_line(slide, left, top, height, color=OT_GREEN, thickness=Pt(3)):
    """Add a thin colored accent line (vertical)."""
    line = slide.shapes.add_shape(
        1,  # Line shape type
        Inches(left), Inches(top), Inches(0.05), Inches(height)
    )
    line.line.color.rgb = color
    line.line.width = thickness
    line.fill.background()
    return line


def add_numbered_card(slide, left, top, width, height, number, title, description):
    """
    Add a numbered card with a colored badge, title, and description.
    Useful for business value, metrics, outcomes.
    """
    # Number badge
    add_textbox(slide, left, top, 0.7, 0.7, number,
                font_size=22, bold=True, text_color=OT_WHITE,
                bg_color=OT_GREEN, alignment=PP_ALIGN.CENTER)

    # Title
    add_textbox(slide, left + 0.85, top, width - 0.85, 0.4, title,
                font_size=14, bold=True, text_color=OT_ASH,
                alignment=PP_ALIGN.LEFT)

    # Description
    add_textbox(slide, left + 0.85, top + 0.45, width - 0.85, height - 0.55, description,
                font_size=12, text_color=OT_ASH,
                alignment=PP_ALIGN.LEFT)

    return slide


def add_icon_row(slide, left, top, width, icon, title, description,
                 font_size=12, spacing=0.1):
    """
    Add a row with icon (emoji), title, and description.
    Useful for data sources, integrations, etc.
    """
    # Icon
    add_textbox(slide, left, top, 0.3, 0.4, icon,
                font_size=20, alignment=PP_ALIGN.CENTER)

    # Title + description on one line
    text = f"{title}: {description}"
    add_textbox(slide, left + 0.5, top, width - 0.5, 0.4, text,
                font_size=font_size, text_color=OT_ASH, alignment=PP_ALIGN.LEFT)

    return slide


def add_bullet_paragraph(text_frame, text, bold_prefix=None, font_size=14, color=OT_ASH):
    """
    Add a properly formatted bullet point with optional bold prefix.

    Example: add_bullet_paragraph(tf, "Description", bold_prefix="Title")
    Creates: "Title — Description" where Title is bold.
    """
    p = text_frame.add_paragraph()
    p.font.size = Pt(font_size)
    p.font.color.rgb = color

    if bold_prefix:
        r = p.add_run()
        r.text = f"{bold_prefix} — "
        r.font.bold = True
        r.font.size = Pt(font_size)
        r.font.color.rgb = color

        r = p.add_run()
        r.text = text
        r.font.bold = False
        r.font.size = Pt(font_size)
        r.font.color.rgb = color
    else:
        p.text = text

    p.space_before = Pt(6)
    p.space_after = Pt(6)
    return p


def add_speaker_notes(slide, text):
    """Add speaker notes to a slide."""
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = text


def add_footer(slide, slide_num: int, copyright_text="© 2019-2026 ONE THOUSAND",
               dark_bg=True):
    """Add OT footer with copyright + slide number."""
    color = OT_MID_GRAY if dark_bg else OT_ASH
    add_textbox(slide, 0.3, 7.0, 4.0, 0.35,
                copyright_text,
                font_size=9, text_color=color, alignment=PP_ALIGN.LEFT)
    add_textbox(slide, 11.5, 7.0, 1.5, 0.35,
                str(slide_num),
                font_size=9, text_color=color, alignment=PP_ALIGN.RIGHT)


def set_footer(slide, slide_num, copyright_text="© 2019-2026 ONE THOUSAND",
               dark_bg=True):
    """Set footer using template placeholders if available, fall back to textboxes.

    Also covers any inherited layout footer text (like 'CONFIDENTIAL') that
    shows through from the layout but can't be edited via placeholders.
    """
    color = OT_MID_GRAY if dark_bg else OT_ASH
    footer_ph = ph_by_idx(slide, 11)
    num_ph = ph_by_idx(slide, 12)
    if footer_ph and num_ph:
        set_ph_text(footer_ph, copyright_text, size=9, color=color)
        set_ph_text(num_ph, str(slide_num), size=9, color=color)
    else:
        # Textbox footer — also covers inherited layout footer text
        # Place a wide enough box to cover any inherited "CONFIDENTIAL" etc.
        add_textbox(slide, 0.3, 7.0, 10.0, 0.35, copyright_text,
                    font_size=9, text_color=color, alignment=PP_ALIGN.LEFT)
        add_textbox(slide, 11.0, 7.0, 2.0, 0.35, str(slide_num),
                    font_size=9, text_color=color, alignment=PP_ALIGN.RIGHT)


def image_placeholder(slide, left, top, width, height, description):
    """Add a gray box with [IMAGE: ...] text as a placeholder for user images."""
    add_textbox(slide, left, top, width, height,
                f"[IMAGE: {description}]",
                font_size=14, bg_color=OT_LIGHT_GRAY, text_color=OT_ASH,
                alignment=PP_ALIGN.CENTER)


# ---------------------------------------------------------------------------
# Slide creation functions
# ---------------------------------------------------------------------------

def make_cover(prs, client_name, location, date, use_case_title, day=1, verbose=False):
    """
    Cover slide using 'Cover Lime + one Logo' layout.

    Layout has:
      idx=10  Date placeholder
      idx=11  Picture/logo placeholder (unused, we add image placeholder as text box)
    Title and subtitle are added as text boxes.
    """
    layout = find_layout(prs, "Cover Lime + one Logo")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Hide the built-in logo picture placeholder (idx=11) by removing it
    # It renders the OT logo at full size which is too large
    logo_ph = ph_by_idx(slide, 11)
    if logo_ph is not None:
        sp = logo_ph._element
        sp.getparent().remove(sp)

    # Date placeholder
    date_ph = ph_by_idx(slide, 10)
    date_text = f"{location}  |  {date}"
    if day == 2:
        date_text += "  |  Day 2"
    set_ph_text(date_ph, date_text, size=14, color=OT_WHITE)

    # Title as text box (large, white, positioned in lower-center area)
    title_text = f"Strengthening {client_name} With AI"
    add_textbox(slide, 0.8, 3.5, 11.5, 1.5, title_text,
                font_size=44, text_color=OT_WHITE, bold=True,
                alignment=PP_ALIGN.LEFT)

    # Subtitle as text box
    subtitle_text = f"AI Hackathon | {use_case_title}"
    add_textbox(slide, 0.8, 5.2, 11.5, 0.8, subtitle_text,
                font_size=20, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Client logo placeholder (top-right, smaller)
    image_placeholder(slide, 9.5, 0.5, 3.3, 1.8, "Add client logo here")

    if verbose:
        logger.info(f"Created Day {day} cover slide")


def make_checkin(prs, questions, client_name, verbose=False):
    """
    Check-in slide using 'Bullet Points Ash' layout.

    Layout placeholders:
      idx=0   Title ("CHECK-IN")
      idx=1   Subtitle
      idx=27  Emoji left (🧠)
      idx=36  Headline left
      idx=42  Text left
      idx=46  Emoji right
      idx=44  Headline right
      idx=45  Text right
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Bullet Points Ash")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    questions = [q.replace("{client_name}", client_name) for q in questions]

    # Title
    set_ph_text(ph_by_idx(slide, 0), "CHECK-IN", size=44, bold=True)

    # Clear subtitle
    set_ph_text(ph_by_idx(slide, 1), "")

    # Left column: brain emoji + first question
    set_ph_text(ph_by_idx(slide, 27), "🧠")
    if len(questions) > 0:
        set_ph_text(ph_by_idx(slide, 36), questions[0])
    set_ph_text(ph_by_idx(slide, 42), "")

    # Right column: thinking emoji + second/third questions
    set_ph_text(ph_by_idx(slide, 46), "💭")
    if len(questions) > 1:
        set_ph_text(ph_by_idx(slide, 44), questions[1])
    if len(questions) > 2:
        set_ph_text(ph_by_idx(slide, 45), questions[2])
    else:
        set_ph_text(ph_by_idx(slide, 45), "")

    # Clear idx=47 if it exists (overlapping placeholder)
    set_ph_text(ph_by_idx(slide, 47), "")

    set_footer(slide, slide_count(prs))

    # Add speaker notes
    notes_text = "Engage the team with check-in questions. Listen to their concerns and expectations."
    add_speaker_notes(slide, notes_text)

    if verbose:
        logger.info("Created Check-in slide")


def make_agenda(prs, agenda_data, verbose=False):
    """
    Agenda slide — uses 'Dayline Lime' layout with grid placeholders.

    Reads from agenda_data which can have custom_items or day1/day2 arrays.
    If no custom items, generates a default schedule by filling grid placeholders.
    """
    layout = find_layout(prs, "Dayline Lime")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), "AI Hackathon – Agenda", size=36, bold=True)

    # Subtitle (idx=1)
    set_ph_text(ph_by_idx(slide, 1), "")

    # Day headers
    set_ph_text(ph_by_idx(slide, 21), "Day 1")
    set_ph_text(ph_by_idx(slide, 121), "Day 2")

    # Get schedules — support both day1/day2 arrays and custom_items format
    day1_schedule = agenda_data.get("day1", [])
    day2_schedule = agenda_data.get("day2", [])

    # Parse custom_items if day1/day2 not provided
    if not day1_schedule and not day2_schedule:
        custom_items = agenda_data.get("custom_items", [])
        for item in custom_items:
            day_label = item.get("day", "").lower()
            entry = {"time": item.get("time", ""), "activity": item.get("activity", "")}
            if "1" in day_label:
                day1_schedule.append(entry)
            elif "2" in day_label:
                day2_schedule.append(entry)

    # Default Day 1 schedule (time, activity pairs)
    if not day1_schedule:
        day1_schedule = [
            {"time": "08:00", "activity": "Check-In + Introduction"},
            {"time": "09:00", "activity": "Process Flow + Framing"},
            {"time": "10:00", "activity": "Workstream: AI Modelling"},
            {"time": "12:00", "activity": "Lunch Break"},
            {"time": "13:00", "activity": "Workstream: Application"},
            {"time": "17:00", "activity": "Check Out"},
        ]

    # Default Day 2 schedule
    if not day2_schedule:
        day2_schedule = [
            {"time": "08:00", "activity": "Check-in + Feedback"},
            {"time": "09:00", "activity": "Workstreams"},
            {"time": "12:00", "activity": "Working Lunch"},
            {"time": "13:00", "activity": "Final Prep"},
            {"time": "14:00", "activity": "Presentations"},
            {"time": "16:00", "activity": "Wrap-up"},
        ]

    # Fill Day 1 grid (limit to first 3 time slots to avoid overflow)
    day1_grid_indices = [
        (97, 107, 108),   # Row 1: time, activity1, activity2
        (66, 115, 116),   # Row 2
        (66, 117, 118),   # Row 3 (reuse time)
    ]
    for row_idx, (time_idx, act1_idx, act2_idx) in enumerate(day1_grid_indices):
        if row_idx < len(day1_schedule):
            item = day1_schedule[row_idx]
            time = item.get("time", "")
            activity = item.get("activity", "")
            set_ph_text(ph_by_idx(slide, time_idx), time)
            set_ph_text(ph_by_idx(slide, act1_idx), activity)
            set_ph_text(ph_by_idx(slide, act2_idx), "")
        else:
            set_ph_text(ph_by_idx(slide, time_idx), "")
            set_ph_text(ph_by_idx(slide, act1_idx), "")
            set_ph_text(ph_by_idx(slide, act2_idx), "")

    # Clear remaining Day 1 cells to avoid template text showing
    remaining_day1_indices = [109, 110, 111, 112, 113, 114, 119, 120]
    for idx in remaining_day1_indices:
        set_ph_text(ph_by_idx(slide, idx), "")

    # Fill Day 2 grid
    day2_grid_indices = [
        (122, 124, 125),  # Row 1
        (123, 132, 138),  # Row 2
    ]
    for row_idx, (time_idx, act1_idx, act2_idx) in enumerate(day2_grid_indices):
        if row_idx < len(day2_schedule):
            item = day2_schedule[row_idx]
            time = item.get("time", "")
            activity = item.get("activity", "")
            set_ph_text(ph_by_idx(slide, time_idx), time)
            set_ph_text(ph_by_idx(slide, act1_idx), activity)
            set_ph_text(ph_by_idx(slide, act2_idx), "")
        else:
            set_ph_text(ph_by_idx(slide, time_idx), "")
            set_ph_text(ph_by_idx(slide, act1_idx), "")
            set_ph_text(ph_by_idx(slide, act2_idx), "")

    # Clear remaining Day 2 cells
    remaining_day2_indices = [126, 129, 130, 131, 134, 135, 136]
    for idx in remaining_day2_indices:
        set_ph_text(ph_by_idx(slide, idx), "")

    # Clear source text (idx=22)
    set_ph_text(ph_by_idx(slide, 22), "")

    set_footer(slide, slide_count(prs), dark_bg=False)
    if verbose:
        logger.info("Created Agenda slide")


def make_toc(prs, num_items=5, verbose=False):
    """
    Table of Contents slide with 4 main items using template placeholders.

    Uses 'Table of Contents large' layout:
      Row 1 Left:  idx=37 (number), idx=36 (headline), idx=38 (arrow)
      Row 1 Right: idx=40 (number), idx=39 (headline), idx=41 (arrow)
      Row 2 Left:  idx=20 (number), idx=19 (headline), idx=21 (arrow)
      Row 2 Right: idx=32 (number), idx=31 (headline), idx=33 (arrow)
      Descriptions: idx=42, 43, 34, 35 (cleared)
      Title: idx=0
      Footer: idx=11, Slide number: idx=12
    """
    layout = find_layout(prs, "Table of Contents large")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Clear title
    set_ph_text(ph_by_idx(slide, 0), "")

    items = [
        ("01", "Pain"),
        ("02", "Data"),
        ("03", "Approach"),
        ("04", "Challenges"),
    ]

    # Fill the 4 main number/headline/arrow slots
    slot_mapping = [
        (37, 36, 38),  # Row 1 Left
        (40, 39, 41),  # Row 1 Right
        (20, 19, 21),  # Row 2 Left
        (32, 31, 33),  # Row 2 Right
    ]

    for i, (num, title) in enumerate(items):
        if i < len(slot_mapping):
            num_idx, headline_idx, arrow_idx = slot_mapping[i]
            set_ph_text(ph_by_idx(slide, num_idx), num)
            set_ph_text(ph_by_idx(slide, headline_idx), title)
            set_ph_text(ph_by_idx(slide, arrow_idx), "→")

    # Clear description boxes
    for idx in [42, 43, 34, 35]:
        set_ph_text(ph_by_idx(slide, idx), "")

    set_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Table of Contents slide")


def make_chapter(prs, number, title, bullets, verbose=False):
    """
    Chapter Divider slide (Pain/Data/Approach/Challenges/Next Steps).

    Uses 'Chapter Divider Ash + Text' layout:
      idx=0   Title
      idx=14  Number area
      idx=15  Content text
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Chapter Divider Ash + Text")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), title, size=40, bold=True)

    # Number (idx=14)
    if number:
        set_ph_text(ph_by_idx(slide, 14), number, size=72, bold=True, color=OT_GREEN)

    # Content bullets (idx=15) — scale font if many bullets
    content_ph = ph_by_idx(slide, 15)
    if content_ph and content_ph.has_text_frame:
        tf = content_ph.text_frame
        tf.clear()
        # Reduce font size for many/long bullets to prevent overflow
        total_chars = sum(len(b) for b in bullets)
        if total_chars > 400 or len(bullets) > 4:
            font_sz = 11
            spacing = 5
        else:
            font_sz = 13
            spacing = 8
        for i, bullet in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = bullet
            p.font.size = Pt(font_sz)
            p.font.color.rgb = OT_WHITE
            p.space_before = Pt(spacing)
            p.space_after = Pt(spacing)

    # Footer + slide number via placeholders
    set_ph_text(ph_by_idx(slide, 11), "© 2019-2026 ONE THOUSAND", size=9)
    set_ph_text(ph_by_idx(slide, 12), str(slide_count(prs)), size=9)

    if verbose:
        logger.info(f"Created chapter: {number} — {title}")


def make_data_screenshots(prs, verbose=False):
    """
    Data screenshots slide — uses 'Title Ash + small Image' layout.

    Layout:
      idx=0   Title
      idx=15  Picture placeholder
      idx=31  Text (Client Name)
      idx=32  Small text
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Title Ash + small Image")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), "Data Screenshots")

    # Small text (idx=32) — describe what to add
    set_ph_text(ph_by_idx(slide, 32), "Sample data files: emails, PDFs, spreadsheets")

    # Clear client name (idx=31)
    set_ph_text(ph_by_idx(slide, 31), "")

    # Picture placeholder (idx=15) — user will replace with actual screenshot
    # (No action needed, it's a built-in picture placeholder)

    set_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Data Screenshots slide")


def make_system_landscape(prs, landscape_data, verbose=False):
    """
    NEW: System Landscape slide showing ERP, CRM, Cloud, APIs.

    Uses DEFAULT layout (no placeholders) with card-based layout.
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    add_textbox(slide, 0.5, 0.3, 12.0, 0.7, "SYSTEM LANDSCAPE",
                font_size=24, bold=True, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Accent line
    add_accent_line(slide, 0.5, 1.1, 0.08, OT_GREEN, thickness=Pt(3))

    # Extract data from landscape_data
    erp = landscape_data.get("erp", "ERP System")
    crm = landscape_data.get("crm", "CRM System")
    cloud = landscape_data.get("cloud_infra", "Cloud Infrastructure")
    key_apis = landscape_data.get("key_apis", [])
    integrations = landscape_data.get("integrations", "")
    constraints = landscape_data.get("constraints_or_notes", "")

    # Create 2x2 card layout for ERP, CRM, Cloud, and Integrations
    # Row 1: ERP (left), CRM (right)
    add_card(slide, 0.5, 1.5, 5.8, 1.5, "ERP System", erp, OT_GREEN, dark_bg=True)
    add_card(slide, 6.8, 1.5, 5.8, 1.5, "CRM System", crm, OT_GREEN, dark_bg=True)

    # Row 2: Cloud (left), APIs/Integrations (right)
    add_card(slide, 0.5, 3.3, 5.8, 1.5, "Cloud Infrastructure", cloud, OT_GREEN, dark_bg=True)

    # APIs list
    apis_text = "\n".join([f"• {api}" for api in key_apis[:5]])
    add_card(slide, 6.8, 3.3, 5.8, 1.5, "Key APIs", apis_text, OT_GREEN, dark_bg=True)

    # Integrations and constraints at bottom
    integration_info = f"Integrations: {integrations}\n\nConstraints: {constraints}"
    add_textbox(slide, 0.5, 5.1, 12.0, 1.5, integration_info,
                font_size=11, text_color=OT_ASH, alignment=PP_ALIGN.LEFT,
                bg_color=OT_VERY_LIGHT_GRAY)

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created System Landscape slide")


def make_key_metrics(prs, metrics_data, verbose=False):
    """
    NEW: Key Metrics slide showing PoC Scope, Timeline to Live, Estimated ROI.

    Uses DEFAULT layout with large stat callouts.
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    add_textbox(slide, 0.5, 0.3, 12.0, 0.7, "KEY METRICS",
                font_size=24, bold=True, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Accent line
    add_accent_line(slide, 0.5, 1.1, 0.08, OT_GREEN, thickness=Pt(3))

    # Extract metric data
    poc_scope = metrics_data.get("poc_scope", "")
    timeline = metrics_data.get("timeline_to_live", "")
    roi = metrics_data.get("estimated_roi", "")

    # Create 3-column layout for metrics
    add_card(slide, 0.5, 1.5, 3.8, 4.5, "PoC Scope", poc_scope, OT_GREEN, dark_bg=True)
    add_card(slide, 4.6, 1.5, 3.8, 4.5, "Timeline to Live", timeline, OT_GREEN, dark_bg=True)
    add_card(slide, 8.7, 1.5, 3.8, 4.5, "Estimated ROI", roi, OT_GREEN, dark_bg=True)

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Key Metrics slide")


def make_lessons_learned(prs, lessons, verbose=False):
    """
    NEW: Lessons Learned slide with structured insights.

    Uses DEFAULT layout.
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    add_textbox(slide, 0.5, 0.3, 12.0, 0.7, "LESSONS LEARNED",
                font_size=24, bold=True, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Accent line
    add_accent_line(slide, 0.5, 1.1, 0.08, OT_GREEN, thickness=Pt(3))

    # Create text box for lessons with bullet points
    lessons_text = "\n\n".join([f"• {lesson}" for lesson in lessons[:8]])  # Limit to 8 lessons
    add_textbox(slide, 0.8, 1.5, 11.5, 5.0, lessons_text,
                font_size=13, text_color=OT_LIGHT_GRAY, alignment=PP_ALIGN.LEFT,
                vertical_anchor=MSO_ANCHOR.TOP)

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Lessons Learned slide")


def make_divider(prs, title, verbose=False):
    """
    Green chapter divider (Breakthrough, Demo, etc.).

    Uses 'Chapter Divider Lime' layout:
      idx=0   Title
      idx=14  Number text (clear)
      idx=32  Small text (clear)
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Chapter Divider Lime")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), title, size=44, bold=True)

    # Clear number text (idx=14)
    set_ph_text(ph_by_idx(slide, 14), "")

    # Clear small text (idx=32)
    set_ph_text(ph_by_idx(slide, 32), "")

    set_footer(slide, slide_count(prs), dark_bg=False)
    if verbose:
        logger.info(f"Created divider: {title}")


def make_business_value(prs, values, verbose=False):
    """
    Business value slide with 3 numbered outcomes.

    Uses 'Table of Contents small' layout:
      idx=0   Title
      Row 1:  idx=14 (number), idx=13 (headline), idx=17 (arrow)
      Row 2:  idx=16 (number), idx=15 (headline), idx=18 (arrow)
      Row 3:  idx=20 (number), idx=19 (headline), idx=21 (arrow)
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Table of Contents small")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), "THE OVERALL GOAL IS TO CREATE BUSINESS VALUE", size=20, bold=True)

    # 3 rows: number / headline / arrow
    slot_mapping = [
        (14, 13, 17),  # Row 1
        (16, 15, 18),  # Row 2
        (20, 19, 21),  # Row 3
    ]

    for i, item in enumerate(values[:3]):
        if i < len(slot_mapping):
            num_idx, headline_idx, arrow_idx = slot_mapping[i]
            num = item.get("number", f"{i+1:02d}")
            title = item.get("title", "")
            desc = item.get("description", "")

            set_ph_text(ph_by_idx(slide, num_idx), num)
            # Use title only in headline (short), put description below via text frame
            headline_ph = ph_by_idx(slide, headline_idx)
            if headline_ph and headline_ph.has_text_frame:
                tf = headline_ph.text_frame
                tf.clear()
                # Title line (bold)
                p = tf.paragraphs[0]
                r = p.add_run()
                r.text = title
                r.font.bold = True
                r.font.size = Pt(14)
                # Description line (normal, smaller)
                if desc:
                    p2 = tf.add_paragraph()
                    p2.text = desc
                    p2.font.size = Pt(11)
                    p2.space_before = Pt(4)
            set_ph_text(ph_by_idx(slide, arrow_idx), "")

    set_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Business Value slide")


def make_poc_summary(prs, intro, features, demo_description="",
                     title_text="WE HAVE FOCUSED ON THE CORE PAIN POINTS", verbose=False):
    """
    PoC summary slide — DEFAULT layout with text boxes.
    Includes features list and optional demo description.
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    add_textbox(slide, 0.5, 0.3, 12.0, 0.9, title_text,
                font_size=20, bold=True, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Intro text
    add_textbox(slide, 0.8, 1.3, 11.0, 0.5, intro,
                font_size=14, text_color=OT_LIGHT_GRAY, alignment=PP_ALIGN.LEFT)

    # Features in a card-style box
    feature_bullets = [f"• {f}" for f in features]
    feature_text = "\n".join(feature_bullets)
    add_textbox(slide, 0.8, 2.0, 11.0, 3.0, feature_text,
                font_size=13, text_color=OT_ASH, alignment=PP_ALIGN.LEFT,
                bg_color=OT_VERY_LIGHT_GRAY)

    # Demo description if provided
    if demo_description:
        add_textbox(slide, 0.8, 5.2, 11.0, 1.3, f"Demo: {demo_description}",
                    font_size=11, text_color=OT_ASH, alignment=PP_ALIGN.LEFT,
                    bg_color=OT_LIGHT_GRAY)

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created PoC Summary slide")


def make_demo_walkthrough(prs, demo_description="", verbose=False):
    """
    NEW: Demo Walkthrough slide with title + demo description + image placeholder.

    Uses DEFAULT layout.
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    add_textbox(slide, 0.5, 0.3, 12.0, 0.7, "DEMO WALKTHROUGH",
                font_size=24, bold=True, text_color=OT_WHITE,
                alignment=PP_ALIGN.LEFT)

    # Demo description
    if demo_description:
        add_textbox(slide, 0.8, 1.2, 11.0, 0.6, demo_description,
                    font_size=13, text_color=OT_LIGHT_GRAY, alignment=PP_ALIGN.LEFT)

    # Large image placeholder
    image_placeholder(slide, 0.5, 2.0, 12.0, 4.5, "Add demo screenshots here")

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Demo Walkthrough slide")


def make_image_slide(prs, title, image_desc, verbose=False):
    """
    Generic content slide with title + image placeholder.

    Uses DEFAULT layout (no placeholders).
    """
    layout = find_layout(prs, "DEFAULT")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title
    if title:
        add_textbox(slide, 0.5, 0.3, 12.0, 0.9, title,
                    font_size=24, bold=True, text_color=OT_WHITE,
                    alignment=PP_ALIGN.LEFT)
        image_top = 1.5
    else:
        image_top = 0.5

    # Image placeholder
    image_placeholder(slide, 0.5, image_top, 12.0, 5.0, image_desc)

    add_footer(slide, slide_count(prs))
    if verbose:
        logger.info(f"Created image slide: {title}")


def make_thanks(prs, ot_team, client_contacts, client_name, verbose=False):
    """
    Closing thanks slide — Bullet Points Ash layout.

    Layout:
      idx=0   Title ("Many thanks!")
      idx=1   Subtitle
      idx=27  Emoji left
      idx=36  Headline left
      idx=42  Text left (OT team members)
      idx=46  Emoji right
      idx=44  Headline right
      idx=45  Text right (client contacts)
      idx=11  Footer
      idx=12  Slide number
    """
    layout = find_layout(prs, "Bullet Points Ash")
    if not layout:
        return
    slide = prs.slides.add_slide(layout)

    # Title (idx=0)
    set_ph_text(ph_by_idx(slide, 0), "Many thanks!", size=44, bold=True)

    # Clear subtitle (idx=1)
    set_ph_text(ph_by_idx(slide, 1), "")

    # Left column: OT team
    set_ph_text(ph_by_idx(slide, 27), "🙏")
    set_ph_text(ph_by_idx(slide, 36), "ONE THOUSAND Team")

    # All team members (OT + client) in left text placeholder
    all_members = ot_team.copy()
    if client_contacts:
        all_members.append("")  # blank line separator
        all_members.append(f"{client_name}:")
        all_members.extend(client_contacts)

    ot_text = ph_by_idx(slide, 42)
    if ot_text and ot_text.has_text_frame:
        tf = ot_text.text_frame
        tf.clear()
        for i, member in enumerate(all_members):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = member
            p.font.size = Pt(14)
            p.space_before = Pt(4)
            p.space_after = Pt(4)

    # Clear right column placeholders (we use that area for images)
    set_ph_text(ph_by_idx(slide, 46), "")
    set_ph_text(ph_by_idx(slide, 44), "")
    set_ph_text(ph_by_idx(slide, 45), "")
    set_ph_text(ph_by_idx(slide, 47), "")

    # Image placeholders in right column area
    image_placeholder(slide, 7.0, 1.8, 5.5, 2.0, "Add team group photo")
    image_placeholder(slide, 7.0, 4.2, 2.5, 1.8, "Client logos")
    image_placeholder(slide, 9.8, 4.2, 2.7, 1.8, "OT + partner logos")

    set_footer(slide, slide_count(prs))
    if verbose:
        logger.info("Created Thanks slide")


# ---------------------------------------------------------------------------
# Main generation function
# ---------------------------------------------------------------------------

def generate_presentation(template_path, variables_path, content_path, output_path, verbose=False):
    """Generate the complete hackathon presentation."""
    variables = load_json(variables_path)
    content = load_json(content_path)
    prs = Presentation(str(template_path))

    client = variables.get("client_name", "Client")
    location = variables.get("location", "Location")
    d1 = variables.get("hackathon_dates", {}).get("day1", "DD.MM.YYYY")
    d2 = variables.get("hackathon_dates", {}).get("day2", "DD.MM.YYYY")
    use_case = variables.get("use_case_title", "Use Case")
    ot_team = variables.get("team_members", {}).get("ot_team", [])
    client_contacts = variables.get("team_members", {}).get("client_contacts", [])

    logger.info(f"Generating presentation for {client}")

    # === DAY 1 PRE-INTRO ===
    make_cover(prs, client, location, d1, use_case, day=1, verbose=verbose)
    make_checkin(prs, content.get("check_in", {}).get("questions", []), client, verbose=verbose)
    make_agenda(prs, content.get("agenda", {}), verbose=verbose)

    # === USE CASE SECTION ===
    make_toc(prs, num_items=5, verbose=verbose)

    uc = content.get("use_case", {})
    make_chapter(prs, "01", "Pain", uc.get("pain_points", []), verbose=verbose)

    # Data slide — format data sources into bullets
    data_sources = uc.get("data_sources", [])
    data_bullets = [
        f"{src.get('icon', '')} {src.get('title', '')}: {src.get('description', '')}"
        for src in data_sources
    ]
    make_chapter(prs, "02", "Data", data_bullets, verbose=verbose)

    make_data_screenshots(prs, verbose=verbose)

    # NEW: System Landscape slide
    landscape = uc.get("system_landscape", {})
    if landscape:
        make_system_landscape(prs, landscape, verbose=verbose)

    approach = uc.get("approach_steps", [])
    q = uc.get("approach_question", "")
    if q:
        approach = approach + [q]
    make_chapter(prs, "03", "Approach", approach, verbose=verbose)

    make_chapter(prs, "04", "Challenges", uc.get("challenges", []), verbose=verbose)

    make_divider(prs, "Let's create A BREAKTHROUGH!", verbose=verbose)

    # === DAY 2 ===
    make_cover(prs, client, location, d2, use_case, day=2, verbose=verbose)

    make_image_slide(prs, "", "Add team photos from Day 1 here", verbose=verbose)

    make_divider(prs, "What have we done in the past 30h?", verbose=verbose)

    make_image_slide(prs, "WE DISCUSSED THE PROCESS FLOW",
                     "Add process flow diagram (from whiteboard / Miro)", verbose=verbose)
    make_image_slide(prs, "WE'VE SET UP AN INITIAL ARCHITECTURE",
                     "Add architecture diagram (from Miro / whiteboard)", verbose=verbose)

    res = content.get("results", {})
    make_business_value(prs, res.get("business_value", []), verbose=verbose)

    # NEW: Key Metrics slide
    metrics = res.get("key_metrics", {})
    if metrics:
        make_key_metrics(prs, metrics, verbose=verbose)

    poc = res.get("poc_summary", {})
    make_poc_summary(prs,
                     poc.get("intro", "We have built a proof of concept (PoC):"),
                     poc.get("features", []),
                     poc.get("demo_description", ""),
                     verbose=verbose)

    make_divider(prs, "DEMO", verbose=verbose)

    # NEW: Demo Walkthrough slide
    if poc.get("demo_description"):
        make_demo_walkthrough(prs, poc.get("demo_description"), verbose=verbose)

    make_divider(prs, "Expectations check", verbose=verbose)

    # NEW: Lessons Learned slide
    lessons = res.get("lessons_learned", [])
    if lessons:
        make_lessons_learned(prs, lessons, verbose=verbose)

    make_chapter(prs, "", "WHAT'S NEXT?", res.get("next_steps", []), verbose=verbose)

    make_thanks(prs, ot_team, client_contacts, client, verbose=verbose)

    # Save
    prs.save(str(output_path))
    logger.info(f"Saved {slide_count(prs)} slides → {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate OT hackathon presentation")
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--variables", type=Path, required=True)
    parser.add_argument("--content", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        generate_presentation(args.template, args.variables, args.content, args.output, args.verbose)
    except Exception as e:
        logger.error(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
