---
name: kick-off-presentation
description: >
  Generate One Thousand branded project kick-off presentation decks (.pptx) from
  scope documents, sprint design plans (Confluence), and Miro boards. Triggers on:
  "kick-off presentation", "kick-off slides", "kick-off deck", "projekt kick-off",
  "project kick-off", "kickoff slides", "kickoff deck", "create kick-off",
  "generate kick-off", "kick-off pptx", "rollout kick-off". Transforms scope
  documents, Confluence sprint design plans, and Miro hackathon boards into
  professional 6-section kick-off presentations with branded OT slide layouts,
  client-specific content, Gantt timelines, and image placeholders for the user
  to fill in. Includes rich input collection with optional image uploads,
  multi-source enrichment, confidence scoring with iterative review, and visual
  QA via soffice + pdftoppm inspection. Use this skill whenever someone mentions
  creating or generating a kick-off presentation, kick-off slides, or kick-off deck.
license: Proprietary
---

# Kick-Off Presentation Generator

Generates professional One Thousand branded project kick-off presentation decks from scope documents, sprint design plans (Confluence), and Miro hackathon boards. Includes multi-source enrichment, anti-hallucination validation, confidence scoring with iterative review, and visual QA inspection.

The presentation follows OT's standard 6-section kick-off format:
1. **Check In** — Cover, icebreaker with GIF
2. **Use-Case** — Pain × Data, hackathon validation, step-by-step, architecture
3. **Timeline** — Sprint goals, Gantt chart, risks
4. **Collaboration** — Participants, meeting schedule
5. **Other Topics** — Discussion / pending decisions
6. **Check Out** — Thank you, feedback

The skill generates ALL text content with confidence scoring. Images are handled as follows:
- **Architecture diagram**: Automatically extracted from the scope document or sprint design plan
- **Miro board images**: Automatically fetched from the project's Miro board via the cowork connector
- **Other images** (GIFs, client logo, screenshots): User provides them upfront or adds them later — clearly marked placeholders are created for anything not provided

---

## Phase 1: Input Collection

### Step 1.1 — Ask the user for primary information

Collect the following information upfront:

1. **Language**: English (en) or German (de)? Default: en

2. **Kick-off type**: Project kick-off (standard) or rollout kick-off?
   - **Project kick-off**: Full deck with hackathon validation, step-by-step, architecture
   - **Rollout kick-off**: Abbreviated — may skip hackathon, fewer sprints, focuses on rollout scope

3. **Source documents** (required — at least one):
   - **Scope document**: PDF or DOCX file path/upload
   - **Sprint design plan**: Confluence page (search automatically, or user provides space/page name)

4. **Client Core Details** (if not extractable from source documents):
   - **Client name** (e.g., "HABA", "MOSCA", "DMV")
   - **Project name / use-case title** (e.g., "Intelligent Sales Assistant")
   - **Kick-off date** (DD.MM.YYYY format)

### Step 1.2 — Ask for optional images

Present this as "add now or add later":

> "I'll generate the full deck with all text content. You can provide images now, or add them to the generated deck later — I'll create clearly marked placeholders for anything not provided."
>
> **Optional images you can provide now:**
> - Client logo (PNG/SVG) — for the cover slide
> - Check-in GIF — icebreaker animation for the intro
> - Pain × Data GIF — animated GIF for the P×D formula visual
> - Step-by-step screenshots — UI mockup or prototype images
> - Hackathon screenshots — photos from the hackathon (if not using Miro)

### Step 1.3 — Validate completeness

Before moving to Phase 2, confirm you have:
- Client name, project name, kick-off date
- At least one of: scope document or sprint design plan
- Language and kick-off type

If critical pieces are missing, ask for them. **Never invent missing details.**

---

## Phase 2: Source Enrichment & Data Gathering

### Step 2.1 — Read reference files

Before generating, Claude **MUST** read these reference files. **Read ALL files in parallel** (use multiple Read tool calls in a single message) to save time — they have no dependencies on each other.

**Important:** These are data-loading calls, not generation steps. Reading them in parallel produces the exact same context as reading them sequentially.

```
Read references/anti-hallucination-rules.md
Read references/section-templates-en.md   # or section-templates-de.md based on language
Read references/slide-structure-guide.md
```

### Step 2.2 — Extract content from scope document

If the user provided a scope document (PDF/DOCX):

**From the scope document, extract:**
- Client name and project name (from cover page)
- Partnership line (e.g., "ClientName x One Thousand")
- Initial context / project summary (Section 1)
- In-scope features with descriptions (Section 2)
- Out-of-scope features (Section 3)
- Architecture diagram — extract the embedded image directly from the PDF/DOCX:
  - For PDF: use `pdfplumber` to extract images from the architecture section
  - For DOCX: use `python-docx` to extract embedded images
  - Save the extracted image to the working directory for embedding in the PPTX
- Architecture description text and bullet points (Section 4)
- Prerequisites from client (Section 5)
- Sprint design plan with deliverables (Section 6)

**Store findings** in a structured extraction document.

### Step 2.3 — Search Confluence for sprint design plan

Search Confluence for the sprint design plan:
- Search for pages matching: "{client_name} design plan", "Project Design Plan", "Sprint Design"
- Look under the client's Confluence space hierarchy: `[Use Case] → Project Management → Project Design Plan`

**From the sprint design plan, extract:**
- Overview (project summary)
- Key requirements
- Architecture section (diagram + notes — if scope doc didn't have one)
- Sprint plan overview (one-line per sprint)
- Timeline & Design table: sprint names, calendar week ranges, goals, epics
- Design decisions (if any)
- Effort estimation (if any)

### Step 2.4 — Fetch Miro board automatically

Use the Miro connector to automatically find the project's hackathon board:
- Use `context_explore` to search for boards matching the client name and "hackathon" / "kick-off" / "discovery"
- Identify the correct board from the search results
- Extract frames and content: AI canvas, validation notes, sticky-note clusters, process flows
- Use `context_get` to fetch board images/frame screenshots
- Save the relevant images for embedding in the hackathon validation slide

**If no Miro board is found:** Skip the hackathon validation slide content and leave it as a placeholder.

### Step 2.5 — Map extracted data to slide content

Create a consolidated **Content Mapping Document**:

| Slide | Content Needed | Source | Available? | Confidence |
|-------|---------------|--------|------------|------------|
| Cover | Client name, project title, date | Scope doc cover + user input | Yes/No | High/Med/Low |
| Pain × Data | Pain points, data sources, solution | Scope doc Sec 1-2 + Miro AI canvas | Yes/No | High/Med/Low |
| Architecture | Diagram image | Scope doc Sec 4 or Confluence | Yes/No | High/Med/Low |
| Sprint Goals | Sprint titles + deliverables | Scope doc Sec 6 or Confluence timeline | Yes/No | High/Med/Low |
| Timeline/Gantt | Calendar weeks, tasks, phases | Confluence timeline table | Yes/No | High/Med/Low |
| Risks | Risk items | User input or scope doc | Yes/No | High/Med/Low |
| Meetings | Day/time/frequency/participants | User input or Confluence | Yes/No | High/Med/Low |

**For any missing content**: Mark as `[To be confirmed]` — do NOT invent details.

---

## Phase 3: Content Extraction & Anti-Hallucination Prep

### Step 3.1 — Apply anti-hallucination rules

**CRITICAL**: Every claim in the presentation must trace to source material. No invented metrics, feature names, technical details, or client-specific processes without documentation.

Before writing ANY content, review:
- What data did we gather from source material (scope doc, Confluence, Miro)?
- What details are MISSING or unclear?
- Where should we place `[To be confirmed]` markers?

### Step 3.2 — Derive Pain × Data content from source

The Pain × Data slide requires three categories of bullets:

**PAIN** (from scope doc Section 1 + in-scope features):
- What business problems does the client face?
- What manual processes are slow/error-prone?
- What inefficiencies exist?

**DATA** (from scope doc Section 2 + architecture):
- What data sources are available?
- What systems/APIs can be accessed?
- What formats does the data come in?

**SOLUTION** (from scope doc Section 2 summary):
- What will the AI solution do?
- What outcomes does it deliver?

### Step 3.3 — Derive sprint content

**From the scope doc's sprint design (Section 6):**
- Extract sprint numbers, titles/goals, and deliverable bullets
- Map to the sprint goals slide format (4 columnar cards)

**From the Confluence timeline table:**
- Extract calendar week ranges per sprint
- Extract task names and durations for the Gantt chart
- Identify milestones (Kick-Off, Release Party)

### Step 3.4 — Extract architecture diagram

The architecture diagram should be extracted AS-IS from the source document:

**From PDF scope document:**
```python
import pdfplumber

with pdfplumber.open(scope_doc_path) as pdf:
    for page in pdf.pages:
        images = page.images
        # Look for the largest image (likely the architecture diagram)
        # Extract and save it
```

**From Confluence sprint design plan:**
- If the Confluence page has an architecture image attachment, download it
- If it has an embedded Graphviz diagram, extract the rendered PNG

**Save the diagram** to the working directory as `architecture_diagram.png` for embedding.

---

## Phase 4: Content Generation with Confidence Scoring

### Step 4.1 — Generate variables.json

Create the metadata file:

```json
{
  "client_name": "ClientName",
  "project_title": "Use Case Title",
  "tagline": "STRENGTHENING CLIENTNAME WITH AI",
  "date": "DD.MM.YYYY",
  "language": "en",
  "kickoff_type": "project",
  "use_cases": [
    {"id": "UC1", "title": "Use Case Title"}
  ],
  "copyright_year": "2019-2026",
  "images": {
    "client_logo": "/path/to/logo.png",
    "checkin_gif": "/path/to/gif.gif",
    "pxd_gif": "/path/to/gif.gif",
    "architecture_diagram": "/path/to/architecture_diagram.png",
    "hackathon_images": ["/path/to/miro_board_1.png"],
    "step_screenshots": []
  }
}
```

**Note on tagline:**
- English: `"STRENGTHENING {CLIENT_NAME} WITH AI"`
- German: `"{CLIENT_NAME} MIT KI STÄRKEN"`

**Note on images:** Only include paths for images that were actually provided or extracted. Omit keys for missing images — the generator will create placeholders automatically.

### Step 4.2 — Generate content.json

Create the content file with ALL slide text. Refer to `references/section-templates-en.md` (or `-de.md`) for writing patterns, word budgets, and style guidance for each section.

**Complete content.json schema:**

```json
{
  "agenda": {
    "sections": [
      {"name": "Check In", "number": "01"},
      {"name": "Use-case", "number": "02"},
      {"name": "Timeline", "number": "03"},
      {"name": "Collaboration", "number": "04"},
      {"name": "Other Topics", "number": "05"},
      {"name": "Check Out", "number": "06"}
    ]
  },
  "check_in": {
    "title": "Before we start",
    "questions": [
      "Who am I?",
      "When is this kick-off a success?"
    ]
  },
  "use_cases": [
    {
      "title": "USE CASE 1: FEATURE TITLE",
      "pain_points": [
        "~50 quotations per day created manually, tying up sales capacity.",
        "Enquiries in varied formats (emails, PDFs) requiring manual interpretation.",
        "High error rate in manual transcription to ERP system."
      ],
      "data_sources": [
        "Inquiry emails and PDFs: Real customer inquiries in multiple formats.",
        "Product master data: Product list with SP numbers, measurements, materials.",
        "Order lifecycle data: Historical examples from inquiry through confirmation."
      ],
      "solution": [
        "AI-powered quotation creation service that automates the end-to-end process.",
        "Intelligent extraction, matching, and draft generation."
      ]
    }
  ],
  "hackathon": {
    "title": "In the hackathon, we validated the usecase together",
    "highlights": [
      "Co-creation is key",
      "Knowledge from similar use-cases",
      "Available prototype"
    ]
  },
  "step_by_step": {
    "title": "Step by step, we'll have a fully working service",
    "phases": [
      {"name": "MVP", "description": "Starting with the hackathon prototype"},
      {"name": "Data deep dive", "description": "Deep exploration of data and processes"},
      {"name": "Expansion", "description": "Expansion of the range of function"},
      {"name": "Feedback", "description": "Regular feedback through testing sessions"}
    ]
  },
  "architecture": {
    "title": "WE ARE BUILDING ON AN EFFICIENT ARCHITECTURE",
    "capabilities": [
      "Web interface for configuration and monitoring",
      "Automated data enrichment pipeline"
    ]
  },
  "sprints": [
    {
      "number": 1,
      "title": "Sprint 1",
      "description": "Service runs search on data sources, checks for duplicates, generates initial reports."
    },
    {
      "number": 2,
      "title": "Sprint 2",
      "description": "Data enrichment, integration with client systems, expanded functionality."
    },
    {
      "number": 3,
      "title": "Sprint 3",
      "description": "Contact information for direct outreach, advanced matching."
    },
    {
      "number": 4,
      "title": "Sprint 4",
      "description": "Lead updates, analytics dashboard, production hardening."
    }
  ],
  "timeline": {
    "title": "timeline",
    "year_quarter": "2025 Q1, 2",
    "legend": {"client": "CLIENTNAME", "ot": "1000"},
    "months": [
      {"name": "MAR 2025", "span": 3},
      {"name": "APR 2025", "span": 4},
      {"name": "MAI 2025", "span": 3}
    ],
    "weeks": ["KW11", "KW12", "KW13", "KW14", "KW15", "KW16", "KW17", "KW18", "KW19", "KW20", "KW21"],
    "tasks": [
      {"name": "Kick-Off", "cells": []},
      {"name": "Replicating prototype", "cells": [1, 2, 3]},
      {"name": "Upload results", "cells": [3, 4, 5]},
      {"name": "Data Enrichment", "cells": [5, 6, 7, 8]},
      {"name": "Integration", "cells": [7, 8, 9]},
      {"name": "User training", "cells": [8, 9, 10]},
      {"name": "Release Party", "cells": []}
    ]
  },
  "risks": {
    "title": "We already started making progress",
    "what_happened": ["Activity 1", "Activity 2"],
    "risks": ["Risk 1: Description", "Risk 2: Description"]
  },
  "collaboration": {
    "participants_title": "Our project has different participants",
    "meeting_types": ["Jour Fixe", "IT Alignments", "Steering Committee", "Testing"],
    "meetings_title": "We meet regularly to accompany the project together",
    "meetings": [
      {
        "name": "Projekt Team Jour Fixe",
        "day": "Wednesday",
        "time": "9:30 AM",
        "frequency": "WEEKLY",
        "participants": ["Person A", "Person B", "Person C"]
      },
      {
        "name": "Steering Committee",
        "day": "Friday",
        "time": "2:00 PM",
        "frequency": "BIWEEKLY",
        "participants": ["Person D", "Person E"]
      }
    ]
  },
  "discussion": {
    "title": "OTHER Topics",
    "subtitle": "DISCUSSION"
  },
  "checkout": {
    "title": "THANK YOU!!",
    "question": "How do you feel after the kick-off?"
  }
}
```

### Step 4.3 — Confidence Scoring Process

Score each content section using five dimensions, each on a 0-20 scale:

| Dimension | 0-5 | 6-10 | 11-15 | 16-20 |
|-----------|-----|------|-------|-------|
| **Source Grounding** | No source | Vague reference | Tied to specific doc | Every claim traced |
| **Specificity** | Generic | Some detail | Mostly specific | Concrete, client-specific |
| **Completeness** | <50% items | ~50-70% | ~80% | All required present |
| **Actionability** | Unclear | Partially clear | Mostly clear | Crystal clear |
| **Anti-Hallucination** | Multiple invented | Some invented | 1-2 invented | Zero invented |

**Combined Score** = Average of five dimensions (0-100)

**Section-Specific Minimum Thresholds:**

| Section | Minimum Threshold |
|---------|-------------------|
| Pain × Data | 75 |
| Sprint Goals | 75 |
| Timeline/Gantt | 70 |
| Architecture | 65 |
| Risks | 60 |
| Meetings | 55 |

### Step 4.4 — Iterative Review Loop

**After scoring all sections:**

1. **Create a summary table** showing all scores
2. **For each FAILING or BORDERLINE section**, ask the user specific questions (NOT vague "tell me more" — ask exactly what data point is needed)
3. **Regenerate failing sections** with the new information
4. **Re-score** regenerated sections
5. **Repeat until** all sections pass their thresholds, OR user says "proceed anyway"

### Step 4.5 — Final content.json validation

Before generating the PPTX:
- Confirm no invented metrics or feature names
- Ensure all `[To be confirmed]` markers are documented
- Verify word counts stay within budgets (see section templates)
- Check parallel structure in bullet points

---

## Phase 5: Presentation Assembly

### Step 5.1 — Save JSON files

Save `variables.json` and `content.json` to the working directory.

### Step 5.2 — Run the generation script

```bash
python scripts/generate_kickoff_pptx.py \
  --template assets/templates/ot-kickoff-template.pptx \
  --variables variables.json \
  --content content.json \
  --output {client_name}_Kick_Off_Presentation.pptx \
  --verbose
```

The script creates a **20-slide** presentation (base case, single use-case) from OT's branded template:

| # | Slide | Layout | Content |
|---|-------|--------|---------|
| 1 | Cover | Title Lime + one Logo | Date, tagline, UC subtitle, client logo |
| 2 | Full Agenda | ToC middle w/o lines | 6 sections with page references |
| 3 | Agenda → Check In | ToC middle w/o lines | Section 01 highlighted |
| 4 | Check-In | Bullet Points Lime | Icebreaker questions + GIF |
| 5 | Agenda → Use-case | ToC middle w/o lines | Section 02 highlighted |
| 6 | Pain × Data | Bullet Points Lime | Pain/Data/Solution bullets + GIF |
| 7 | Hackathon | DEFAULT | Miro board images / co-creation highlights |
| 8 | Step by Step | Bullet Points Lime | 4-phase progression + screenshots |
| 9 | Architecture | Bullet Points Lime | Diagram image + capabilities |
| 10 | Agenda → Timeline | ToC middle w/o lines | Section 03 highlighted |
| 11 | Sprint Goals | 1_Bullet Points Lime | Columnar sprint cards |
| 12 | Timeline/Gantt | Calendar Lime w/o lines | Table with months, weeks, tasks, sprints |
| 13 | Progress/Risks | Bullet Points Lime | What happened + risks |
| 14 | Agenda → Collaboration | ToC middle w/o lines | Section 04 highlighted |
| 15 | Participants | Bullet Points Lime | Circular diagram |
| 16 | Meetings | Bullet Points Lime | Meeting cards |
| 17 | Agenda → Other Topics | ToC middle w/o lines | Section 05 highlighted |
| 18 | Discussion | Bullet Points Lime | Open discussion prompt |
| 19 | Agenda → Check Out | ToC middle w/o lines | Section 06 highlighted |
| 20 | Thank You | Bullet Points Lime | Feedback question + icons |

### Step 5.3 — Verify slide generation

Extract slide count and text from the generated PPTX:

```bash
python -c "
from pptx import Presentation
prs = Presentation('{client_name}_Kick_Off_Presentation.pptx')
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

Expected output: **20 slides** (single UC) or **20 + N-1 slides** (N use-cases).

### Step 5.4 — Create image placeholder inventory

List all placeholders the user must fill:

**Required (auto-extracted or provided):**
- Slide 9: Architecture diagram (auto-extracted from scope doc)
- Slide 7: Hackathon Miro board images (auto-fetched from Miro)

**Optional (user adds later if not provided):**
- Slide 1: Client logo
- Slide 4: Check-in icebreaker GIF
- Slide 6: Pain × Data animated GIF
- Slide 8: Step-by-step UI screenshots

---

## Phase 6: Visual QA & Delivery

### Step 6.1 — Convert PPTX to PDF and inspect visually

```bash
soffice --headless --convert-to pdf {client_name}_Kick_Off_Presentation.pptx
pdftoppm -jpeg -r 150 {client_name}_Kick_Off_Presentation.pdf slide
```

### Step 6.2 — Visual inspection checklist

For each generated slide, verify:

1. **Layout integrity**: Text not cut off, placeholders clearly labeled
2. **Content accuracy**: Client name consistent, dates correct, no stale `[To be confirmed]`
3. **Brand compliance**: OT green/lime on covers and dividers, footer on every slide
4. **Agenda accuracy**: Page numbers match actual slide positions
5. **Table formatting**: Gantt chart has correct week numbers and task labels
6. **Readability**: Font sizes readable, bullet points not overflowing

### Step 6.3 — Fix issues found during QA

If visual inspection finds problems:
1. **Layout issues**: Reduce content length in content.json, re-run generator
2. **Content errors**: Update content.json, re-run generator
3. **Page numbers wrong**: Re-run generator (it auto-calculates)

Re-run soffice conversion after each fix.

---

## Phase 7: Delivery

### Step 7.1 — Prepare delivery package

1. **PPTX file**: `{ClientName}_Kick_Off_Presentation.pptx` (ready to use)
2. **Image placeholder inventory** (list of slides still needing images)
3. **Confidence scores document** (if any borderline or `[To be confirmed]` items)

### Step 7.2 — Final handoff to user

1. Display the confidence scores table
2. List any `[To be confirmed]` items that need follow-up
3. Provide the image placeholder inventory
4. Ask: "Any final edits before I save?"
5. Copy the final PPTX to the user's workspace

---

## Writing Quality Standards

### Word & Bullet Budgets

| Slide | Max Words | Max Bullets | Notes |
|-------|-----------|-------------|-------|
| Cover | 20 | — | Tagline + use-case subtitle |
| Check-in questions | 30 | 2-3 | One question per line |
| Pain points | 40 | 3-5 | Specific, quantified where possible |
| Data sources | 40 | 3-5 | Actual available data |
| Solution | 40 | 2-3 | Desired outcomes |
| Step-by-step phases | 60 | 4 | One sentence per phase |
| Sprint descriptions | 50 each | 3-5 bullets | Per sprint card |
| Risk items | 80 | 2-4 per column | Concise |
| Meeting details | — | — | Structured card format |

### Style & Tone Guidelines

1. **Collaborative and forward-looking** — kick-off, not a report
2. **Active voice** — "We will build" not "The system will be built"
3. **Client vocabulary** — use their terminology from source documents
4. **Specific over generic** — "~50 quotations per day" not "many quotations"
5. **No filler words** — every word must earn its place on the slide
6. **Parallel structure** — all bullets in a list use the same grammatical form
7. **Present tense for goals** — "Sprint 1 delivers X" not "Sprint 1 will deliver X"

### Avoiding Hallucination

**RED FLAGS — Never write these without source material:**
- Client company metrics not in source documents
- Specific feature names not in scope document
- Timeline claims not backed by sprint design plan
- Team member names not provided by user
- Meeting schedules not confirmed
- Architecture components not in scope doc or sprint design

**When in doubt**: Use `[To be confirmed]` and ask the user.

---

## Brand Guidelines

- **Cover color**: OT Sharp Green (#18A05A)
- **Accent green**: #19A960 (for active agenda items, highlights)
- **Lime green**: #D5F89E (background accents)
- **Ash**: #2F2F2F (body text)
- **Dark**: #242424 (dark backgrounds)
- **Footer**: "(c) 2019-2026 ONE THOUSAND" center-aligned at bottom
- **Format**: Widescreen 16:9 (13.333" x 7.5")
- **Fonts**: Akkurat LL (body), Wavetable (decorative headings)
- **Logo**: One Thousand logo on template (preserved automatically)

---

## File Paths (relative to skill directory)

```
kick-off-presentation/
├── SKILL.md                                    # This file
├── scripts/
│   └── generate_kickoff_pptx.py                # PPTX generation script
├── assets/
│   └── templates/
│       └── ot-kickoff-template.pptx            # OT branded template (20 slides)
└── references/
    ├── anti-hallucination-rules.md             # 17 binding rules
    ├── section-templates-en.md                 # English writing patterns
    ├── section-templates-de.md                 # German writing patterns
    └── slide-structure-guide.md                # Slide-by-slide specification
```

---

## Dependencies & Setup

### Python packages

**Note:** Python dependencies (`python-pptx`, `Pillow`, `lxml`, `pdfplumber`, `python-docx`, `graphviz`) are installed automatically by the plugin's SessionStart hook. No manual `pip install` is needed.

### External tools (for visual QA)

- **soffice** (LibreOffice): For headless PPTX to PDF conversion
- **pdftoppm** (Poppler): For PDF to JPEG conversion for visual inspection

### MCP tools used for enrichment

- **Confluence search** — Search for sprint design plan pages
- **`context_explore` / `context_get`** — Automatically find and fetch Miro board content for the hackathon validation slide
- **Close CRM** — Lookup client metadata (name, contacts) if needed

---

## Skill Triggers

The skill is invoked when a user mentions:

- "kick-off presentation"
- "kick-off slides"
- "kick-off deck"
- "kick-off pptx"
- "project kick-off"
- "projekt kick-off"
- "create kick-off"
- "generate kick-off"
- "rollout kick-off"
- Similar variations

---

## Multi Use-Case Handling

When the scope document or sprint design plan covers multiple use-cases:

1. **Pain × Data slides**: One slide per use-case (duplicated from template)
2. **Sprint goals**: Multi-track layout (one row per use-case with separator line)
3. **Timeline/Gantt**: Multi-track with separate sprint bars per use-case
4. **Meetings**: Additional Jour Fixe per use-case (UC1 JF + UC2 JF + Steering)
5. **Agenda**: Section 2 label changes to "Use-cases" (plural)
6. **Page numbers**: Automatically recalculated based on extra slides

---

## Rollout Variant

For rollout kick-offs (existing product being rolled out to new region/team):

1. **Section 2** changes to "THE APPLICATION" (or "DIE ANWENDUNG" in DE)
2. **Section 3** changes to "ROLLOUT SCOPE" (or "ROLLOUT UMFANG" in DE)
3. **Hackathon slide**: Replaced with solution screenshots
4. **Fewer sprints**: Typically 2 (Improvements + Rollout) instead of 4
5. **Step-by-step**: May be simplified or omitted
6. **Architecture**: Shows existing architecture (not new)

---

## Troubleshooting

**Issue**: PPTX generator fails with "template file not found"
**Solution**: Verify `assets/templates/ot-kickoff-template.pptx` exists and is readable

**Issue**: Slides are missing content after generation
**Solution**: Check that `content.json` is valid JSON; run `python -m json.tool content.json`

**Issue**: Agenda page numbers are wrong
**Solution**: Re-run the generator — it auto-calculates page numbers based on slide count

**Issue**: Architecture diagram not appearing
**Solution**: Verify the image was extracted from the scope doc and the path in variables.json is correct

**Issue**: Miro board images not found
**Solution**: Check that the Miro connector is available and the board exists; fall back to user-provided images

**Issue**: `[To be confirmed]` markers remain
**Solution**: Expected for items the user approved; document in delivery handoff

---

## Example Workflow

### User Input

> "Generate a kick-off presentation for HABA. The scope document is at ~/scope.pdf and the sprint design is on Confluence. Kick-off date is March 21, 2025. Use case is Intelligent Sales Assistant."

### Skill Workflow

1. **Phase 1** — Confirm: language=EN, type=project, client=HABA, date=21.03.2025. Ask for optional images.
2. **Phase 2** — Read scope doc → extract features, architecture diagram, sprint plan. Search Confluence → get timeline details. Auto-search Miro → fetch hackathon board.
3. **Phase 3** — Map content to slides, verify no hallucinations, flag gaps.
4. **Phase 4** — Generate variables.json and content.json; score each section.
5. **Phase 5** — Run `generate_kickoff_pptx.py`; verify 20 slides generated.
6. **Phase 6** — Convert to PDF and JPEG; visually inspect all slides.
7. **Phase 7** — Deliver PPTX + image placeholder list + confidence scores.

### Handoff to User

```
Presentation generated: HABA_Kick_Off_Presentation.pptx (20 slides)

Confidence Scores:
  Pain × Data        82/100  (threshold: 75)  PASS
  Sprint Goals       88/100  (threshold: 75)  PASS
  Timeline/Gantt     79/100  (threshold: 70)  PASS
  Architecture       90/100  (threshold: 65)  PASS
  Risks              65/100  (threshold: 60)  PASS
  Meetings           58/100  (threshold: 55)  PASS

Images Embedded:
  ✓ Architecture diagram (extracted from scope doc)
  ✓ Miro hackathon board (2 frames)

Image Placeholders to Add:
  - Slide 1: Client logo
  - Slide 4: Check-in GIF
  - Slide 6: Pain × Data GIF
  - Slide 8: Step-by-step screenshots

Ready to download!
```
