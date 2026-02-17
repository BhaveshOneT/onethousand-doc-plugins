---
name: hackathon-presentation
description: "Generate One Thousand branded hackathon presentation decks (.pptx) from sales context, Confluence pages, Miro boards, and project briefs. Triggers on: 'hackathon presentation', 'hackathon deck', 'hackathon slides', 'hackathon pptx', 'create presentation for hackathon', 'generate hackathon slides', 'presentation for [client]', 'hackathon pitch deck'. Transforms sales context emails, Slack messages, Confluence pages, Miro boards, and Close CRM data into professional 2-day hackathon presentations with branded OT slide layouts, client-specific use case content, and image placeholders for the user to fill in. Includes rich input collection, multi-source enrichment, confidence scoring with iterative review, and visual QA via soffice + pdftoppm inspection. Use this skill whenever someone mentions creating or generating a hackathon presentation or slides."
---

# Hackathon Presentation Generator

Generates professional One Thousand branded hackathon presentation decks from sales context, project briefs, Confluence documentation, Miro boards, and hackathon summaries. Includes multi-source enrichment, anti-hallucination validation, confidence scoring with iterative review, and visual QA inspection.

The presentation follows OT's standard 2-day hackathon format with three content blocks:
1. **Day 1 Pre-Intro** — Cover, Check-in, Agenda (before the generic AI education section)
2. **Use Case Section** — Pain, Data, Approach, Challenges (client-specific, after AI intro)
3. **Day 2 Results** — Cover, Team photos, Process Flow, Architecture, Business Value, PoC Summary, Demo, Next Steps, Thanks

The skill generates ALL text content with confidence scoring. Images are left as clearly marked placeholders — the user adds screenshots, diagrams, team photos, and client logos manually.

---

## Phase 1: Input Collection

### Step 1.1 — Ask the user for primary information

Collect the following information upfront:

1. **Language**: English (en) or German (de)? Default: en

2. **Source material type**: Where is the primary context?
   - Sales email / Slack message describing the client and use case
   - Confluence page URL(s) with hackathon planning docs or technical briefs
   - Miro board URL with AI canvas and discovery notes
   - Close CRM lead/opportunity record
   - Previous hackathon debrief or scope document
   - Direct text input from the user
   - Email thread or Teams conversation

3. **Client Core Details** (if not in source material):
   - **Client name** and company size (startup, SMB, enterprise)
   - **Industry/sector** (manufacturing, finance, healthcare, retail, logistics, etc.)
   - **Headquarters location** (city, country)
   - **Hackathon dates**: Day 1 date and Day 2 date (DD.MM.YYYY format)

4. **Use Case Specifics**:
   - **Use case title**: Short name (e.g., "Quotation creation", "Customer chatbot", "Invoice automation")
   - **Business problem summary**: 1-2 sentences on what we're solving

5. **Team & Stakeholders**:
   - OT team members who will be named in the presentation
   - Key client contacts / stakeholders (optional)

6. **Hackathon Goals & Success Criteria** (optional but valuable):
   - What does success look like? (e.g., "Prove we can automate 80% of quotations")
   - Any specific metrics or KPIs?
   - Expected business impact (time savings, cost reduction, FTE capacity, etc.)

### Step 1.2 — Ask for Confluence/connected-source URLs

Before proceeding to Phase 2, explicitly ask:

> "Do you have Confluence pages, Miro boards, or Email threads about this hackathon that I should review? Please provide URLs or descriptions."

If the user provides Confluence URLs:
- Store them for Phase 2 (Source Enrichment)
- Ask: "Any specific Confluence spaces I should search for related pages (e.g., 'Client-{ClientName}', 'Hackathons', 'Technical Docs')?"

If the user provides Miro board URLs:
- Note them for Phase 2
- Ask: "Should I extract the AI canvas (pain/data/approach) from this board?"

### Step 1.3 — Validate completeness

Before moving to Phase 2, confirm you have:
- Client name, location, dates
- Use case title
- At least one source of information

If critical pieces are missing, ask for them. **Never invent missing details.**

---

## Phase 2: Source Enrichment & Data Gathering

### Step 2.1 — Search Confluence for client documentation

If the user provided Confluence URLs or space names, search for:
- **Hackathon planning pages** (look for "Hackathon {ClientName}", "2-day discovery", etc.)
- **Technical documentation** (system landscape, data sources, API docs, ERPs)
- **Scope documents** or discovery debrief documents
- **Client background** pages (industry context, company profile, strategic goals)

**Extraction**: From Confluence, extract:
- Specific pain points with numbers (e.g., "~200 manual quotations per day")
- Data source details (which systems, APIs, databases are available)
- Existing tech stack and integration constraints
- Business goals or success metrics mentioned in planning docs
- Team member names or roles

**Store findings** in a "Confluence Extraction" document for Phase 3.

### Step 2.2 — Explore Miro board if provided

If a Miro board URL was provided:
- Use `context_explore` to list all items on the board
- Look for frames or sections labeled "Pain", "Data", "Approach", "Challenges"
- Extract the AI canvas or discovery mapping if present
- Check for diagrams (process flows, system architecture)

**Store findings** in the Miro Extraction document.

### Step 2.3 — Search Close CRM for lead/opportunity context

If a Close CRM lead or opportunity was mentioned:
- Use `lead_search` or `fetch_lead` to retrieve client details
- Extract: Company size, industry, location, contact names, deal stage, any notes
- Look for related opportunities or tasks mentioning hackathon

**Store findings** in the CRM Extraction document.

### Step 2.4 — Search Email/Teams for hackathon communications

Use `outlook_email_search` or `chat_message_search` to find:
- Emails with subject containing "hackathon" + client name
- Recent emails discussing use case, pain points, or team
- Messages mentioning success criteria or business metrics

**Extract**: Specific quotes, metrics, team names, stakeholder concerns.

**Store findings** in the Email Extraction document.

---

## Phase 3: Content Extraction & Anti-Hallucination Prep

### Step 3.1 — Read the anti-hallucination rules

```
Read references/anti-hallucination-rules.md
```

**CRITICAL**: Every claim in the presentation must trace to source material. No invented metrics, feature names, technical details, or client-specific processes without documentation.

Before writing ANY content, review:
- What data did we gather from source material (Confluence, Miro, CRM, Email)?
- What details are MISSING or unclear?
- Where should we place `[To be confirmed]` markers?

### Step 3.2 — Read section writing templates and standards

```
Read references/section-templates-en.md   # or section-templates-de.md
Read references/slide-structure-guide.md
```

These contain:
- Writing patterns and style guidance for each slide
- Word budgets and bullet point limits
- Power words and active verb recommendations
- Parallel structure enforcement rules

### Step 3.3 — Extract and structure content from all sources

Create a consolidated **Content Extraction Document** with:

| Category | Source | Extracted Details | Confidence |
|----------|--------|-------------------|------------|
| **Client & Project** | Confluence + CRM | Company name, size, industry, HQ, strategic goals | High/Med/Low |
| **Pain Points** | Email + Confluence + user input | Specific problems, manual processes, metrics | High/Med/Low |
| **Data Sources** | Miro + Confluence tech docs | Systems, APIs, databases, data formats, volume | High/Med/Low |
| **Approach** | Miro AI canvas + scope doc | PoC capabilities, steps, features | High/Med/Low |
| **Challenges** | Miro + Confluence + Email | Data quality, integration, adoption, technical blockers | High/Med/Low |
| **Business Value** | Confluence planning + Email | Time savings, FTE freed, revenue impact, strategic benefits | High/Med/Low |
| **Team** | Close CRM + Email | OT team members, client stakeholders, roles | High/Med/Low |

**For any missing category**: Mark as `[To be confirmed]` — do NOT invent details.

### Step 3.4 — Map content to slide sections

For each slide section, list:
- What content is available?
- What sources back it?
- What's missing?

Example:
```
PAIN POINTS:
- "Manual quotation entry takes ~200 minutes per day" (Source: Email from sales lead)
- "Error rate: ~5% of quotes contain pricing mistakes" (Source: Confluence discovery doc)
- "Quotation turnaround: 2-3 business days" (Source: scope doc)
- [To be confirmed]: Market pressure or competitive disadvantage if quotation is slow?
```

---

## Phase 4: Content Generation with Confidence Scoring

### Step 4.1 — Generate variables.json

Create the metadata file:

```json
{
  "client_name": "ClientName",
  "location": "City, Country",
  "use_case_title": "Short Use Case Name",
  "hackathon_dates": {
    "day1": "DD.MM.YYYY",
    "day2": "DD.MM.YYYY"
  },
  "team_members": {
    "ot_team": ["Name1", "Name2", "Name3", "Name4"],
    "client_contacts": ["Name1 (Title)", "Name2 (Title)"]
  }
}
```

**Note**: The variables.json is intentionally minimal. The generator constructs slide titles like "Strengthening {client_name} With AI" and "AI Hackathon | {use_case_title}" automatically from these values.

### Step 4.2 — Generate content.json with rich text markup

Create the content file with ALL slide text. The content.json supports **rich text markup**:

- `**bold text**` — Rendered as bold. On Data/Approach/Challenges slides, bold text uses theme scheme color ACCENT_2 (green). On What's Next, bold keywords also use ACCENT_2.
- `<<highlighted text>>` — Rendered with green highlight color (#00B050). On Business Value title, `<<text>>` uses scheme color TEXT_1. On Business Value item descriptions, `<<text>>` uses scheme color BACKGROUND_2 (lime).

**Complete content.json schema:**

```json
{
  "check_in": {
    "questions": [
      "Question 1 for the group",
      "Question 2 — can use {client_name} placeholder",
      "Question 3 about hackathon expectations"
    ]
  },
  "agenda": {
    "day1": [
      {"time": "08:00", "activity": "Check-In + Introduction"},
      {"time": "09:00", "activity": "Process Flow + Framing"},
      {"time": "10:00", "activity": "Workstream: AI Modelling"}
    ],
    "day2": [
      {"time": "08:00", "activity": "Check-in + Feedback"},
      {"time": "09:00", "activity": "Workstreams"}
    ]
  },
  "use_case": {
    "pain_points": [
      "Pain point with <<highlighted keywords>> for emphasis",
      "Another pain point with <<green highlighted>> metrics"
    ],
    "data_sources": [
      {
        "title": "**Bold Category Title:**",
        "description": "Description of data source, format, volume"
      }
    ],
    "approach_steps": [
      "**Bold Step Name:** Description of what this step does",
      "**Next Step:** Description with details"
    ],
    "approach_question": "Optional closing question — rendered in BACKGROUND_2 color",
    "challenges": [
      "**Challenge Title** — Description with details about the challenge",
      "**Another Challenge** — More details using em-dash pattern"
    ]
  },
  "results": {
    "business_value": {
      "title": "THE OVERALL GOAL IS TO <<CREATE BUSINESS VALUE>>",
      "items": [
        {
          "number": "01",
          "title": "Short Benefit Title",
          "description": "Description ending with <<green highlighted outcome>>"
        },
        {
          "number": "02",
          "title": "Another Benefit",
          "description": "Description with <<highlighted result>>"
        },
        {
          "number": "03",
          "title": "Third Benefit",
          "description": "Description with <<highlighted impact>>"
        }
      ]
    },
    "poc_summary": {
      "intro": "We have built a proof of concept (PoC) that demonstrates:",
      "features": [
        "Feature 1 description — concrete capability",
        "Feature 2 description — concrete capability",
        "Feature 3 description — concrete capability"
      ]
    },
    "next_steps": [
      "**Bold keyword** followed by description of next step action",
      "**Another keyword** followed by what needs to happen"
    ]
  }
}
```

### Step 4.3 — Rich Text Markup Reference

The generator's `_parse_rich_segments()` function parses `**bold**` and `<<green>>` markup into styled runs. Here is how each slide uses them:

| Slide | Markup | Rendering |
|-------|--------|-----------|
| Pain | `<<text>>` | #00B050 green highlight, white base text (explicit) |
| Data | `**text**` | Bold + scheme ACCENT_2 (green), leading space before first segment |
| Approach | `**text**` | Bold + scheme ACCENT_2 (green); last bullet question uses BACKGROUND_2 |
| Challenges | `**text**` | Bold + scheme ACCENT_2 (green), em-dash pattern |
| Business Value title | `<<text>>` | Scheme TEXT_1 (dark), normal text #FFFFFF |
| Business Value items | `<<text>>` | Scheme BACKGROUND_2 (lime green highlight) |
| What's Next | `**text**` | Bold + scheme ACCENT_2, normal text #FFFFFF, font: Akkurat LL 28pt |

### Step 4.4 — Confidence Scoring Process

Score each content section using five dimensions, each on a 0-20 scale:

| Dimension | 0-5 | 6-10 | 11-15 | 16-20 |
|-----------|-----|------|-------|-------|
| **Source Grounding** | No source or invented | Vague source reference | Tied to specific doc/quote | Every claim directly traced to source |
| **Specificity** | Generic, could apply to any client | Some client detail | Mostly specific, few generic phrases | Concrete details, numbers, client terminology |
| **Completeness** | <50% of required items | ~50-70% present | ~80% present | All required items present; no major gaps |
| **Actionability** | Unclear what to do | Partially clear | Mostly clear; 1-2 ambiguities | Crystal clear; audience understands next step |
| **Anti-Hallucination** | Multiple invented details | Some invented metrics/names | 1-2 invented details | Zero invented details; all verifiable |

**Combined Score** = Average of the five dimension scores (0-100)

**Scoring Guide by Combined Score:**

| Range | Meaning | Action |
|-------|---------|--------|
| 90-100 | Strong | Proceed without modification |
| 75-89 | Adequate | Proceed; note any minor gaps in final review |
| 50-74 | Weak | Ask user for clarification; regenerate with new info |
| 0-49 | Insufficient | Ask user; mark content `[To be confirmed]` before proceeding |

**Section-Specific Minimum Thresholds:**

| Section | Minimum Threshold |
|---------|-------------------|
| Pain Points | 75 |
| Data Sources | 70 |
| Approach | 75 |
| Challenges | 65 |
| Business Value | 70 |
| PoC Summary | 60 |
| Next Steps | 55 |

### Step 4.5 — Iterative Review Loop

**After scoring all sections:**

1. **Create a summary table** showing all scores
2. **For each FAILING or BORDERLINE section**, ask the user specific questions
3. **Regenerate failing sections** with the new information
4. **Re-score** regenerated sections
5. **Repeat until** all sections pass their thresholds, OR user says "proceed anyway"

### Step 4.6 — Final content.json validation

Before generating the PPTX:
- Confirm no invented metrics or feature names
- Ensure all `[To be confirmed]` markers are documented
- Verify word counts stay within budgets (see Writing Quality Standards below)
- Check parallel structure in bullet points
- Verify rich text markup is valid (`**` and `<<`/`>>` must be properly paired)

---

## Phase 5: Presentation Assembly

### Step 5.1 — Save JSON files

Save `variables.json` and `content.json` to the working directory.

### Step 5.2 — Run the generation script

```bash
python scripts/generate_hackathon_pptx.py \
  --template assets/templates/ot-hackathon-template.pptx \
  --variables variables.json \
  --content content.json \
  --output {client_name}_Hackathon_Presentation.pptx \
  --verbose
```

The script creates **21 slides** from OT's branded template layouts:

| # | Slide | Layout | Content |
|---|-------|--------|---------|
| 1 | Cover (Day 1) | Title Lime + one Logo | Client name, location, Day 1 date, use case title |
| 2 | Check-in | Bullet Points Ash | 3 questions (32pt white), "Check-in" title (66pt Wavetable) at bottom |
| 3 | Agenda | Dayline Lime | Customizable 2-day schedule grid |
| 4 | Table of Contents | Table of Contents large | Pain / Data / Approach / Challenges with 01-04 numbers |
| 5 | Pain (01) | Chapter Divider Ash + Text | Pain points with `<<green>>` highlights in manual TEXT_BOX |
| 6 | Data (02) | Chapter Divider Ash + Text | Data sources with `**bold**` ACCENT_2 titles in resized PH 15 |
| 7 | Data Screenshots | Title Ash + small Image | `[IMAGE placeholder]` for sample data files |
| 8 | Approach (03) | Chapter Divider Ash + Text | Approach steps with `**bold**` ACCENT_2, question in BACKGROUND_2 |
| 9 | Challenges (04) | Chapter Divider Ash + Text | Challenges with `**bold**` ACCENT_2 em-dash pattern (14pt) |
| 10 | Breakthrough! | Chapter Divider Lime | "Let's create A BREAKTHROUGH!" divider |
| 11 | Cover (Day 2) | Title Lime + one Logo | Day 2 date, results title |
| 12 | Team Photos | DEFAULT | `[IMAGE placeholder]` for team group photos |
| 13 | What we've done | Chapter Divider Lime | "What have we done in the past 30h?" divider |
| 14 | Process Flow | DEFAULT | Title 40pt white + `[IMAGE placeholder]` for whiteboard/Miro flow |
| 15 | Architecture | DEFAULT | Title 50pt white + `[IMAGE placeholder]` for system architecture |
| 16 | Business Value | Table of Contents small | Title with `<<green>>` TEXT_1 highlight + 3 numbered items with BACKGROUND_2 |
| 17 | PoC Summary | DEFAULT | Title 40pt white + lime rectangle (bg2 fill) with features (line_spacing=1.5) |
| 18 | DEMO | Chapter Divider Lime | "DEMO" section divider |
| 19 | Expectations Check | Chapter Divider Lime | "Expectations check" section divider |
| 20 | What's Next | Chapter Divider Ash + Text | `**bold**` keywords in ACCENT_2, normal in #FFFFFF, 28pt Akkurat LL |
| 21 | Thanks | Bullet Points Ash | "Many thanks!" (Wavetable), team names (Akkurat LL), photo + logos placeholders |

### Step 5.3 — Verify slide generation

Extract slide count and text from the generated PPTX:

```bash
python -c "
from pptx import Presentation
prs = Presentation('{client_name}_Hackathon_Presentation.pptx')
print(f'Total slides: {len(prs.slides)}')
for i, slide in enumerate(prs.slides):
    print(f'Slide {i+1}: {slide.slide_layout.name}')
    for shape in slide.shapes:
        if hasattr(shape, 'text'):
            text_preview = shape.text[:50].replace(chr(10), ' ')
            if text_preview.strip():
                print(f'  > {text_preview}...')
"
```

Expected output: **21 slides** total.

### Step 5.4 — Create image placeholder inventory

List all placeholders the user must fill:

**Before the Hackathon (Day 1):**
- Slide 1: Client logo (recommend 1200x400px, right side)
- Slide 7 (Data Screenshots): 2-3 sample data files, emails, or screenshots

**After the Hackathon (Day 2):**
- Slide 12: Team photos from Day 1 (recommend group photo 1920x1080px)
- Slide 14: Process flow diagram (from whiteboard photo, Miro, or Lucidchart export)
- Slide 15: Architecture diagram (system landscape, API flows, integrations)
- Slide 21: Team group photo (left side, full-bleed 5.39x5.99"), client + OT logos (bottom bar)

---

## Phase 6: Visual QA & Inspection

### Step 6.1 — Convert PPTX to PDF and inspect visually

Run the soffice conversion and PDF-to-image pipeline:

```bash
# Convert PPTX to PDF
soffice --headless --convert-to pdf {client_name}_Hackathon_Presentation.pptx

# Convert PDF to JPEG images (150 DPI for readable inspection)
pdftoppm -jpeg -r 150 {client_name}_Hackathon_Presentation.pdf slide

# Output: slide-1.jpg, slide-2.jpg, ... slide-21.jpg
```

### Step 6.2 — Visual inspection checklist

For each generated slide, verify:

1. **Layout integrity**:
   - Text is not cut off at slide edges
   - Placeholder boxes are clearly labeled `[IMAGE: ...]`
   - Font sizes are readable (body text >= 14pt, headers >= 32pt)

2. **Content accuracy**:
   - No `[To be confirmed]` markers remain (unless explicitly approved)
   - Client name is consistent throughout
   - Dates, numbers, and metrics are correct

3. **Brand compliance**:
   - OT green/lime used on covers and dividers
   - Dark ash (#323232) backgrounds on chapter dividers
   - Footer shows "© 2019-2026 ONE THOUSAND" + slide number
   - 16:9 widescreen aspect ratio maintained (13.333" x 7.5")

4. **Formatting accuracy** (theme colors):
   - Bold titles on Data/Approach/Challenges use ACCENT_2 scheme color (green)
   - Business Value `<<green>>` text uses TEXT_1 on title, BACKGROUND_2 on items
   - PoC Summary lime rectangle uses bg2 scheme fill
   - What's Next bold keywords use ACCENT_2, normal text is #FFFFFF
   - Fonts: Wavetable for Check-in/Thanks titles, Akkurat LL for What's Next/Thanks names

5. **Readability**:
   - Bullet points have appropriate line breaks (max 2 lines per bullet)
   - Headers max 6 words
   - No orphaned text (single word on a line)

### Step 6.3 — Fix issues found during QA

If visual inspection finds problems:

1. **Layout issues** (text cut off, misaligned): Reduce content length in content.json, re-run generator
2. **Content errors**: Update `content.json`, re-run generator, re-inspect
3. **Brand/formatting**: Verify template file and regenerate

Re-run soffice conversion after each fix to re-inspect.

---

## Phase 7: Delivery

### Step 7.1 — Prepare delivery package

1. **PPTX file**: `{ClientName}_Hackathon_Presentation.pptx` (ready to use)
2. **Image placeholder inventory** (list of slides needing images)
3. **Confidence scores document** (if any borderline or `[To be confirmed]` items)

### Step 7.2 — AI intro section instruction

Provide the user with this critical note:

> **IMPORTANT: How to Complete Your Hackathon Deck**
>
> The generated presentation contains your **client-specific slides only** (21 slides covering Pain, Data, Approach, Challenges, Business Value, Results, Next Steps, etc.).
>
> To create the **complete hackathon presentation**, you must insert OT's standard **AI education slides** in between:
>
> 1. Keep slides 1-4 (Cover, Check-in, Agenda, Table of Contents)
> 2. **INSERT here:** OT's standard AI intro section (~50 slides):
>    - What is AI?
>    - Machine Learning fundamentals
>    - Deep Learning and LLMs
>    - OT's ABC+DEF framework
>    - Agentic AI patterns
>    - (See master hackathon deck at: `assets/templates/ot-master-hackathon.pptx`)
> 3. Continue with Slide 5+ (Pain section) from your generated deck
>
> **How to insert:**
> - Open your generated PPTX in PowerPoint
> - Open the master hackathon deck
> - Copy the AI intro slides from the master deck
> - Paste them into your generated deck after Slide 4 (Agenda)
> - Save as final version

### Step 7.3 — Final handoff to user

1. Display the confidence scores table
2. List any `[To be confirmed]` items that need follow-up
3. Provide the image placeholder inventory
4. Explain the AI intro insertion process
5. Ask: "Any final edits before I save the PPTX to your downloads folder?"
6. Copy the final PPTX to the user's workspace

---

## Writing Quality Standards

### Word & Bullet Budgets

| Slide | Max Words | Max Bullets | Notes |
|-------|-----------|-------------|-------|
| Check-in questions | 30 | 3 | One question per line |
| Pain points | 100 | 4-6 | Include `<<green>>` metrics where possible |
| Data sources | 80 | 3-4 | Use `**bold title:**` + description format |
| Approach steps | 80 | 4-5 | Use `**Bold Step:** description` pattern |
| Challenges | 120 | 4-5 | Use `**Bold Title** — description` em-dash pattern |
| Business value | 90 | 3 items | Use `<<green>>` on key outcome phrases in description |
| PoC summary | 60 | 4-6 | Feature list; simple, concrete |
| Next steps | 60 | 2-4 | Use `**bold keyword** rest of sentence` pattern |
| Thanks | 30 | Team names | Names listed vertically |

### Style & Tone Guidelines

1. **Concise and impactful** — presentation slides, not a detailed report
2. **Active voice** — "Parse incoming quotations" not "Incoming quotations are parsed"
3. **Specific over generic** — "~200 quotations per day" not "many quotations"
4. **Client vocabulary** — use their terminology
5. **No filler words** — every word must earn its place on the slide
6. **Power verbs** — Transform, Automate, Accelerate, Unlock, Drive, Enable, Streamline
7. **Parallel structure** — all bullets in a list should use the same grammatical form
8. **Rich text markup** — use `**bold**` and `<<green>>` consistently per slide type

### Avoiding Hallucination

**RED FLAGS — Never write these without source material:**

- Client company metrics not mentioned in source docs
- Specific feature names not agreed upon during discovery
- Technical specifications not confirmed
- Timeline claims not backed by project scope
- ROI numbers without clear calculation
- Regulatory or compliance claims without documentation

**When in doubt**: Use `[To be confirmed]` marker and ask the user for confirmation.

---

## Formatting Reference

### Theme Color Mapping

The OT hackathon template uses these theme colors:

| Theme Key | Value | Usage |
|-----------|-------|-------|
| dk1 (TEXT_1/tx1) | #000000 | Dark text — used on Business Value title `<<green>>` |
| lt1 | #FFFFFF | White |
| dk2 | #242424 | Ash dark background |
| lt2 (BACKGROUND_2/bg2) | #D5F89E | Lime green — PoC Summary box fill, Business Value `<<green>>` items |
| accent2 | #19A960 | Green accent — bold titles on Data/Approach/Challenges/What's Next |

### Font Usage

| Font | Usage |
|------|-------|
| Wavetable | Check-in slide title (66pt), Thanks "Many thanks!" (24pt) |
| Akkurat LL | What's Next content (28pt), Thanks team names (20pt) |
| (Theme default) | All other text — inherits from slide master |

### Color Inheritance Rules

- **Placeholder text** on dark backgrounds: Inherits white from theme (no explicit RGB needed)
- **TextBox text** on dark backgrounds: Must set explicit `#FFFFFF` (textboxes don't inherit theme)
- **Green highlights**: `#00B050` explicit RGB for Pain slide `<<green>>` markup
- **Scheme colors**: Used via XML `schemeClr` for ACCENT_2, BACKGROUND_2, TEXT_1

---

## Brand Guidelines

- **Cover color**: OT Sharp Green (#18A05A)
- **Dark/Ash background**: #323232 (for chapter dividers and text backgrounds)
- **Lime green**: #D5F89E (scheme lt2/bg2 — for PoC summary box, business value highlights)
- **Accent green**: #19A960 (scheme accent2 — for bold titles in content slides)
- **Footer**: "© 2019-2026 ONE THOUSAND" center-aligned at bottom
- **Format**: Widescreen 16:9 (13.333" x 7.5")
- **Template**: One Thousand branded layouts with green/ash/white color scheme
- **Logo placement**: Client logo on cover (right side); client + OT logos on Thanks slide bottom bar

---

## Dependencies & Setup

### Python packages

```bash
pip install python-pptx --break-system-packages
pip install lxml --break-system-packages
```

### External tools (for visual QA)

- **soffice** (LibreOffice): For headless PPTX to PDF conversion
- **pdftoppm** (Poppler): For PDF to JPEG conversion for visual inspection

### Template files

- **OT Hackathon template**: `assets/templates/ot-hackathon-template.pptx`
- **OT Master hackathon deck** (for AI intro slides): `assets/templates/ot-master-hackathon.pptx`
- **Section templates** (writing guidance): `references/section-templates-en.md` or `references/section-templates-de.md`
- **Anti-hallucination rules**: `references/anti-hallucination-rules.md`

### MCP tools used for enrichment

- Confluence search — Search for client documentation
- `context_explore` / `context_get` — Explore Miro board structure and content
- `lead_search`, `fetch_lead` — Query Close CRM for client context
- `outlook_email_search` — Search email history for hackathon communications
- `chat_message_search` — Search Teams messages if applicable

---

## Skill Triggers

The skill is invoked when a user mentions:

- "hackathon presentation"
- "hackathon deck"
- "hackathon slides"
- "hackathon pptx"
- "create presentation for hackathon"
- "generate hackathon slides"
- "presentation for [client name]"
- "hackathon pitch deck"
- Similar variations

---

## Troubleshooting

**Issue**: PPTX generator fails with "template file not found"
**Solution**: Verify `assets/templates/ot-hackathon-template.pptx` exists and is readable

**Issue**: Slides are missing content after regeneration
**Solution**: Check that `content.json` is valid JSON; run `python -m json.tool content.json` to validate

**Issue**: Rich text markup not rendering
**Solution**: Ensure `**` and `<<`/`>>` markers are properly paired and not nested

**Issue**: `[To be confirmed]` markers remain after final review
**Solution**: This is expected for items the user approved; document them in the delivery handoff

**Issue**: Font sizes too small or text cut off
**Solution**: Reduce word count per bullet; the generator uses `_enable_autofit()` for auto-shrink on most content areas

**Issue**: Theme colors not applying correctly
**Solution**: The generator uses XML-level `schemeClr` manipulation; ensure the template's theme.xml defines dk1, lt2, accent2 correctly

---

## Example Workflow

### User Input

> "Generate a hackathon presentation for Acme Manufacturing. They're in automotive parts, based in Stuttgart. Hackathon is Jan 18-19, 2024. Use case is automating quotation creation."

### Skill Workflow

1. **Phase 1** — Ask for team names, hackathon goals, data source details
2. **Phase 2** — Search Confluence/Miro/CRM/Email for planning docs; extract pain points, data sources, tech stack
3. **Phase 3** — Create Content Extraction Document; identify gaps
4. **Phase 4** — Generate variables.json and content.json with rich text markup; score each section
5. **Phase 5** — Run `generate_hackathon_pptx.py`; verify 21 slides generated
6. **Phase 6** — Convert to PDF and JPEG; visually inspect all slides
7. **Phase 7** — Deliver PPTX + image placeholder list + confidence scores + AI intro insertion instructions

### Handoff to User

```
Presentation generated: Acme_Manufacturing_Hackathon_Presentation.pptx (21 slides)

Confidence Scores:
  Pain Points      85/100  (threshold: 75)  PASS
  Data Sources     76/100  (threshold: 70)  PASS
  Approach         80/100  (threshold: 75)  PASS
  Challenges       71/100  (threshold: 65)  PASS
  Business Value   75/100  (threshold: 70)  PASS
  PoC Summary      81/100  (threshold: 60)  PASS
  Next Steps       73/100  (threshold: 55)  PASS

Image Placeholders to Add (6 total):
- Slide 1: Client logo (1200x400px)
- Slide 7: 2x data screenshots (1024x768px each)
- Slide 12: Team photo from Day 1 (1920x1080px)
- Slide 14: Process flow diagram
- Slide 15: System architecture diagram
- Slide 21: Team photo + client/OT logos

Next: Insert OT's AI intro slides between Slide 4 and Slide 5, then add images above.

Ready to download!
```
