---
name: scope-document-generator
description: >
  Generate professional One Thousand branded PoC scope documents.
  Triggers on: "scope document", "scope doc", "project scope", "PoC scope",
  "create scope", "generate scope", "scope for this", "formal document from hackathon",
  "client deliverable", "project definition document", "convert hackathon to scope".
  Transforms hackathon debrief documents and additional user context into
  formal scope documents with cover page, numbered sections, architecture
  diagrams, sprint design, and anti-hallucination verification.
  Project name and client name are extracted from the hackathon debrief —
  not asked separately.
  Supports English and German.
license: Proprietary
triggers:
  - "scope document"
  - "scope doc"
  - "project scope"
  - "PoC scope"
  - "create scope"
  - "generate scope"
  - "scope for this"
  - "formal document"
  - "client deliverable"
  - "project definition"
  - "convert hackathon"
  - "hackathon to scope"
  - "make a scope"
  - "write a scope"
  - "scope document for this input"
---

# Scope Document Generator Skill

## Overview

This skill transforms hackathon debrief documents and additional user context into **professional One Thousand branded PoC scope documents**. It takes two inputs — a hackathon debrief document (primary source of truth) and additional user context (post-hackathon decisions, scope changes, conversation notes) — and uses a template-based approach for pixel-perfect formatting consistency.

The workflow: Collect inputs (hackathon debrief + user notes) → Extract information (including project name and client name from the debrief) → Generate content with confidence scoring → Iteratively review weak sections with the user → Assemble branded DOCX → Deliver client-ready document.

**Output:** A branded DOCX file with green cover page, One Thousand logo on every page, numbered headings in green, properly formatted subsections, bullet lists, sprint design, and architecture diagram.

---

## When to Use This Skill

**ALWAYS invoke this skill when the user's request matches ANY of these patterns:**

- User says "scope document", "scope doc", "project scope", or "PoC scope"
- User says "create/generate/write a scope" for some input
- User has a hackathon PDF/DOCX and wants a "formal document", "client deliverable", or "proposal"
- User wants to convert hackathon findings into a One Thousand document
- User needs a "project definition" document
- User is preparing handoff materials from a sprint/workshop
- User says "scope document for this input" or similar

**Do NOT invoke for:** general Word documents, slide decks, spreadsheets, or non-scope deliverables.

---

## Inputs

This skill requires **two inputs**:

### Input 1: Hackathon Debrief Document
- Can be a PDF, DOCX, or text pasted in conversation
- If uploaded as a file, extract text using appropriate tools
- This is the **primary source of truth** for all technical content
- **Project name and client name are extracted from this document** — do NOT ask for them separately. The cover page values (`cover_title`, `cover_client_x_ot`) are derived from the hackathon debrief content.

### Input 2: Additional User Context
- Post-hackathon decisions, scope changes, customer conversation notes, meeting notes, or email excerpts
- Can be provided as text in the conversation
- May contain updated requirements, scope refinements, or timeline preferences
- **Priority:** User-provided context overrides hackathon doc when there are conflicts (flag the conflict)

---

## Workflow

### Phase 1: Input Collection + Background Setup

Ask the user using AskUserQuestion:

1. **Language:** English or German?
2. **Hackathon Debrief Document:** Source file (PDF, DOCX, or text)
3. **Additional Context:** Post-hackathon decisions, scope changes, customer conversation notes
4. **Architecture Diagram:** Extract from source or generate new one? (Always included)

**Do NOT ask for project name, client name, or cover details** — these are extracted from the hackathon debrief document during Phase 2. The cover page values (`cover_title`, `cover_subtitle`, `cover_client_x_ot`) are populated automatically from extracted content.

**Note:** Python dependencies (`pdfplumber`, `python-docx`, `Pillow`, `graphviz`) are installed automatically by the plugin's SessionStart hook. No manual `pip install` is needed.

---

### Phase 2: Content Extraction

#### Parallel Reference File Loading

Before generating, Claude **MUST** read these reference files. **Read ALL THREE files in parallel** (use multiple Read tool calls in a single message) to save time — they have no dependencies on each other and the content generation that follows needs all of them loaded in context:

- `references/content-extraction-guide.md` — extraction patterns
- `references/anti-hallucination-rules.md` — what NOT to invent
- `references/section-templates-en.md` OR `references/section-templates-de.md` — writing patterns for the chosen language

**Important:** These are data-loading calls, not generation steps. Reading them in parallel produces the exact same context as reading them sequentially — the order they are loaded does not matter. All three files will be fully available in context before any content generation begins.

**From the hackathon document:**

1. Use pandoc or python tools to extract text from PDF/DOCX
2. Extract:
   - Use case descriptions (exact terminology from source)
   - Problem statement / business objectives
   - Technical approach demonstrated
   - Data sources and integrations
   - Features demonstrated (distinguish confirmed vs. aspirational)
   - Architecture decisions
   - Timeline/sprint discussion (if any)
   - Known constraints or limitations
   - Out-of-scope items explicitly mentioned

3. **Architecture diagram extraction** (if choosing "extract"):
   ```bash
   python scripts/extract_architecture_diagram.py \
     --input /path/to/hackathon_doc \
     --output /tmp/arch_diagram.png
   ```

---

### Phase 3: Content Generation with Confidence Scoring

Generate two JSON files that feed the document assembly script.

#### CRITICAL: Confidence Scoring System

After generating each section, Claude MUST self-assess a **confidence score (0–100)** based on the following criteria. This score is NOT added to the document — it is used internally to decide whether to ask the user for more input.

**Scoring Criteria per Section:**

| Score Range | Meaning | Action |
|-------------|---------|--------|
| 90–100 | Strong: fully backed by source, specific, complete | Proceed |
| 70–89 | Adequate: mostly backed, minor gaps or generic phrasing | Proceed with note |
| 50–69 | Weak: significant gaps, vague language, thin content | **ASK USER** |
| 0–49 | Insufficient: mostly invented or missing | **ASK USER** |

**How to calculate the score:**

For each section, evaluate these five dimensions (each 0–20 points):

1. **Source grounding (0–20):** Is every claim traceable to the source document? (20 = every sentence backed by source, 0 = entirely invented)
2. **Specificity (0–20):** Are names, tools, integrations specific? (20 = "SAP CRM via RFC", 0 = "the system")
3. **Completeness (0–20):** Does the section cover its purpose fully? (20 = nothing missing, 0 = skeletal)
4. **Actionability (0–20):** Can someone act on this content? (20 = clear deliverables/requirements, 0 = hand-wavy)
5. **Anti-hallucination (0–20):** Is the section free of invented details? (20 = nothing fabricated, 0 = multiple fabrications)

**Section-specific minimum thresholds:**

| Section | Minimum Score | Rationale |
|---------|--------------|-----------|
| Initial Context | 70 | Framing can be somewhat generic |
| In-Scope Features | 80 | Core deliverable — must be precise |
| Out-of-Scope | 75 | Manages client expectations — must be specific |
| Architecture Diagram | 65 | Text description can be supplemented by image |
| Prerequisites | 80 | Client needs to act on these — must be precise |
| Sprint Design | 75 | Guides project planning — must be realistic |

#### Iterative Review Loop

After scoring all sections, if ANY section falls below its threshold:

1. **Show the user a summary table:**
   ```
   Section                  Score   Status
   ─────────────────────────────────────────
   1. Initial Context        85     ✓ Pass
   2. In-Scope Features      62     ✗ Needs input
   3. Out-of-Scope           78     ✓ Pass
   4. Architecture Diagram   55     ✗ Needs input
   5. Prerequisites          45     ✗ Needs input
   6. Sprint Design          72     ✗ Needs input (below 75)
   ```

2. **For each failing section, ask specific questions using AskUserQuestion.** Do NOT ask vague questions. Ask precisely what's missing:
   - "In-Scope Features scored 62/100. The source document mentions 'email classification' but doesn't specify the classification categories or the ML approach. Can you clarify: (a) what email categories exist, (b) what model/approach was discussed?"
   - "Prerequisites scored 45/100. I found no mention of data access or credentials in the source. What does the client need to provide for: (a) database access, (b) API credentials, (c) sample data?"

3. **Re-generate the failing sections** with the new input.
4. **Re-score** and repeat until all sections pass their thresholds OR the user explicitly says to proceed anyway.

**The user can always override** by saying "proceed anyway", "good enough", or similar — in which case, proceed with `[To be confirmed]` markers on weak sections.

---

#### variables.json

```json
{
  "cover_title": "SMART QUOTATION\nCREATION",
  "cover_subtitle": "Project Scope Document",
  "cover_client_x_ot": "ClientName x One Thousand",
  "language": "en"
}
```

Fields:
- `cover_title`: Project name in UPPERCASE. Use `\n` for line breaks on cover.
- `cover_subtitle`: Document type. "Project Scope Document" (EN) or "Projekt Scope Dokument" (DE)
- `cover_client_x_ot`: Client × One Thousand attribution
- `language`: "en" or "de"

#### content.json

The content.json defines all document sections. Each section maps to a numbered heading in the output.

```json
{
  "sections": [
    {
      "number": "1",
      "title": "Initial Context",
      "content": "Paragraph text here. Use \\n\\n for paragraph breaks.",
      "subsections": [],
      "bullet_points": []
    },
    {
      "number": "2",
      "title": "In-Scope Features",
      "content": "Optional intro text before subsections.",
      "subsections": [
        {
          "number": "2.1",
          "title": "Feature name",
          "content": "Feature description paragraph(s).",
          "bullet_points": []
        }
      ],
      "bullet_points": []
    },
    {
      "number": "3",
      "title": "Out-of-Scope Features",
      "content": "",
      "subsections": [],
      "bullet_points": [
        "Item excluded from scope",
        "Another excluded item"
      ],
      "bullet_style": "dash"
    },
    {
      "number": "4",
      "title": "Architecture Diagram",
      "content": "Description of the architecture. The diagram image is injected separately via --arch-diagram.",
      "subsections": [],
      "bullet_points": []
    },
    {
      "number": "5",
      "title": "Prerequisites from ClientName",
      "content": "",
      "subsections": [],
      "bullet_points": [
        "Prerequisite item 1",
        "Prerequisite item 2"
      ],
      "bullet_style": "normal"
    },
    {
      "number": "6",
      "title": "High Level Sprint Design",
      "content": "Intro paragraph about sprint methodology.",
      "is_sprint_section": true,
      "subsections": [
        {
          "number": "Sprint 0",
          "title": "Preparation (1 week – before project kickoff)",
          "content": "",
          "bullet_points": [
            "Deliverable 1",
            "Deliverable 2"
          ]
        },
        {
          "number": "Sprint 1",
          "title": "Sprint goal description",
          "content": "Deliverables:",
          "bullet_points": [
            "Deliverable 1",
            "Deliverable 2"
          ]
        }
      ],
      "bullet_points": []
    }
  ]
}
```

**Key fields:**

| Field | Type | Description |
|-------|------|-------------|
| `number` | string | Section number ("1", "2", etc.) or sprint label ("Sprint 0") |
| `title` | string | Section heading text |
| `content` | string | Body text. Use `\n\n` for paragraph breaks |
| `subsections` | array | Child subsections (Heading2 style) |
| `bullet_points` | array | Bullet list items at section level |
| `bullet_style` | string | `"normal"` (round bullets) or `"dash"` (hyphen prefix) |
| `is_sprint_section` | bool | If true, subsections render as bold sprint labels with deliverable bullets |

**Formatting rules the script applies automatically:**

- **Heading1** (green, bold): `"1.  Initial Context"` format
- **Heading2** (dark, bold): `"2.1    Feature name"` with auto-numbering disabled
- **Normal bullets**: Round bullet character via ListParagraph + numPr
- **Dash bullets**: Hyphen prefix `"-  text"` via ListParagraph without numPr
- **Sprint labels**: Bold Normal paragraph `"Sprint 0: Title text"`
- **Deliverables label**: Auto-bold when content ends with `":"` (e.g., "Deliverables:")
- **Cover title line breaks**: `\n` in cover_title converts to `<w:br/>`

---

### Phase 4: Architecture Diagram (Required) + Overlapped Execution

Every scope document MUST include an architecture diagram. Either extract it from the source document or generate a new one based on the technical components discussed.

#### Overlapped Diagram Generation

**Performance optimization:** The architecture diagram depends only on the architecture data extracted in Phase 2 — it does NOT depend on the sprint design (Section 6) or other late-stage content. Therefore, when generating a new diagram, **launch diagram generation via the Task tool as a background agent** while continuing to write remaining sections (especially Section 6 — Sprint Design).

**How to overlap:**
1. After writing Sections 1–5 and preparing the architecture description JSON, launch the diagram generation script in a background Task agent
2. Continue writing Section 6 (Sprint Design) in the main agent
3. Collect the diagram result before proceeding to Phase 5 (Document Assembly)

**Important:** This overlap is safe because the diagram generation is a standalone Python script that takes a JSON description as input and produces a PNG image. It has no dependency on Section 6 content, and Section 6 has no dependency on the diagram output. The final document assembly in Phase 5 needs both to be complete, which they will be.

**If NOT overlapping** (e.g., extracting diagram from source document), run it sequentially as before — extraction is typically fast enough that overlapping provides minimal benefit.

#### Diagram Generation

```bash
python scripts/generate_architecture_diagram.py \
  --description /tmp/arch_desc.json \
  --output /tmp/arch_diagram.png \
  --style detailed
```

Description JSON format (with zones for grouped layout):
```json
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "On Premise",
      "components": ["SQL Database", "Email Inboxes", "SAP Endpoint"]
    },
    {
      "name": "Azure Virtual Network",
      "color": "#0078D4",
      "components": ["VPN Gateway", "Pipeline", "LLM Endpoint", "Webapp", "Draft DB"]
    }
  ],
  "components": [
    {"name": "SQL Database",  "type": "database"},
    {"name": "Email Inboxes", "type": "client"},
    {"name": "SAP Endpoint",  "type": "external"},
    {"name": "VPN Gateway",   "type": "gateway"},
    {"name": "Pipeline",      "type": "service",  "label": "Quotation\nCreation\nPipeline"},
    {"name": "LLM Endpoint",  "type": "ai",       "label": "Private\nOpenAI\nEndpoint"},
    {"name": "Webapp",        "type": "client",    "label": "Webapp\nto Finalize\nQuotations"},
    {"name": "Draft DB",      "type": "database",  "label": "Database\nwith Quotation\nDrafts"}
  ],
  "flows": [
    {"from": "SQL Database",  "to": "VPN Gateway",  "label": "Load relevant\ndata"},
    {"from": "Email Inboxes", "to": "VPN Gateway",  "label": "Read\nemails"},
    {"from": "VPN Gateway",   "to": "Pipeline"},
    {"from": "Pipeline",      "to": "LLM Endpoint", "label": "LLM extraction"},
    {"from": "Pipeline",      "to": "Draft DB",     "label": "Store quotations"},
    {"from": "Webapp",        "to": "Draft DB",     "label": "Fetch quotations", "dir": "both"},
    {"from": "Webapp",        "to": "SAP Endpoint", "label": "Save confirmed\nquotations"}
  ]
}
```

**Component types → shapes:** `client` (rounded box), `service` (rounded box), `database` (cylinder), `external` (component), `gateway` (3D box), `ai` (double octagon), `queue`, `cache`, `message`

**Zone properties:** `name` (label), `color` (border hex, optional), `bgcolor` (fill hex, auto-calculated if omitted), `components` (list of component names to group)

**Rendering pipeline (automatic fallback):**
1. **Graphviz `dot`** — primary renderer; produces professional diagrams with zones, typed shapes, automatic arrow routing, and colour-coded nodes
2. **Pillow PNG** — basic grid fallback if Graphviz is not installed

**Image embedding:** The `--arch-diagram` flag on `generate_scope_doc.py` uses python-docx's `new_pic_inline()` to embed the image (max 6" wide, centered). Do NOT use raw OOXML injection — Word rejects it.

---

### Phase 5: Document Assembly

Run the generation script:

```bash
SKILL_DIR="/path/to/scope-document-generator"

python "$SKILL_DIR/scripts/generate_scope_doc.py" \
  --template-dir "$SKILL_DIR/assets/templates/scope-template" \
  --variables /tmp/scope_variables.json \
  --content /tmp/scope_content.json \
  --output /path/to/output/scope_document.docx \
  --arch-diagram /tmp/arch_diagram.png
```

The `--arch-diagram` flag is required for every scope document. Always generate or extract a diagram before assembly.

---

### Phase 6: Verification & Delivery

After generation:

1. **Validate the DOCX** opens correctly:
   ```python
   from docx import Document
   doc = Document("/path/to/output.docx")
   print(f"Paragraphs: {len(doc.paragraphs)}")
   ```
2. **Final confidence summary:** Display the final confidence scores for all sections to the user
3. **Flag gaps:** Note sections that still have `[To be confirmed]` markers
4. **Copy to workspace folder** and provide download link

---

## Document Length Constraints (CRITICAL)

**The final scope document MUST be 4–5 pages maximum.** This is a hard constraint that applies regardless of how much source material or additional context is provided. Extra data should make the content smarter and more specific — NOT longer.

### Rules:
- **Total word count:** 800–1200 words across all sections (excluding cover page)
- **Never exceed 5 pages** in the final DOCX output
- **More source data = better quality, NOT more length.** When you have rich source material, use it to choose more precise wording and specific details — do not expand section lengths
- **No Conclusion section by default.** Only add if the user explicitly requests it
- **Brevity is a feature.** Clients value concise, scannable documents. Every sentence must earn its place

### Per-Section Word Budget (approximate):

| Section | Max Words | Format |
|---------|-----------|--------|
| 1. Initial Context | ~80–120 | 2 short paragraphs (4–5 sentences total) |
| 2. In-Scope Features | ~250–350 | 2–3 sentences per subsection, NO deliverables sub-lists |
| 3. Out-of-Scope | ~80–120 | Single-line dash bullets only, no explanations |
| 4. Architecture Diagram | ~60–100 | 1–2 sentences + 3 short bullets + diagram image |
| 5. Prerequisites | ~80–120 | Single-line round bullets, 6–8 items |
| 6. Sprint Design | ~200–300 | Sprint 0 + 3–4 sprints, ~4–5 short bullet deliverables each |

---

## Content Quality Standards

### Tone & Voice
- Professional, partnership-focused, results-oriented
- First person plural ("we") when describing joint work
- Confident but not arrogant
- Technical precision without jargon overload

### Evidence-Based Writing
- Every claim traces to the source document
- Use the client's exact domain terminology
- Never invent metrics, KPIs, benchmarks, or performance numbers
- Never add features the hackathon didn't demonstrate
- Never assume timelines unless explicitly discussed

### Section-Specific Guidelines

**Initial Context (Section 1):**
- Maximum 2 short paragraphs (4–5 sentences total)
- First paragraph: what was explored and key finding
- Second paragraph: what this PoC will deliver and its significance
- Do NOT pad with generic AI/partnership filler text

**In-Scope Features (Section 2):**
- One Heading2 subsection per use case / feature
- **2–3 sentences per subsection maximum** — what it does, how it works, what value it adds
- Use specific terminology from the hackathon (e.g., "SAP CRM via RFC" not "the CRM system")
- **Do NOT include deliverables sub-lists under each feature** — the description sentences are sufficient
- If a feature has options/alternatives, present them in a single sentence

**Out-of-Scope (Section 3):**
- Use `bullet_style: "dash"` (hyphen prefix, matching One Thousand format)
- **Single-line items only** — each bullet is one concise phrase (5–15 words)
- Do NOT add explanations, reasons, or multi-sentence descriptions per item
- Example good: `"Image processing from PDFs or other documents"`
- Example bad: `"Image processing — While the hackathon explored image extraction, this requires additional ML and is deferred."`

**Architecture Diagram (Section 4):**
- **1–2 sentences** describing the architecture + hosting setup
- **3 short bullets** for key infrastructure points
- The diagram image provides the rest of the detail — keep text minimal

**Prerequisites (Section 5):**
- Use `bullet_style: "normal"` (round bullets)
- **Single-line bullets only** (one sentence each, ~10–20 words)
- 6–8 items typical
- Be specific: "Access to SAP CRM API" not "System access"
- Do NOT include status indicators, owners, or timelines in each bullet

**Sprint Design (Section 6):**
- Set `is_sprint_section: true`
- Sprint 0 is always preparation/setup (before kickoff)
- Each sprint: bold title line + "Deliverables:" label + **4–5 short bullet deliverables**
- Each deliverable bullet is one concise line (~5–15 words)
- **Do NOT include Objectives, Key Activities, or Success Criteria sub-sections** — just deliverables
- Don't invent sprint durations unless discussed

### Anti-Hallucination Rules (Critical)

Read the full rules at `references/anti-hallucination-rules.md`. Summary:

1. NEVER invent metrics, KPIs, or statistics
2. NEVER fabricate third-party tool names or version numbers
3. NEVER assume budget, timeline, or team size
4. NEVER add features not demonstrated or discussed
5. Use "[To be confirmed]" / "[Noch zu bestätigen]" for unknowns
6. Cross-check: every in-scope feature should have architecture support
7. If source is ambiguous, note it rather than guessing

---

## Standard Section Structure

For English documents, the standard 6-section structure is:

1. Initial Context
2. In-Scope Features (with subsections per use case)
3. Out-of-Scope Features (dash bullets)
4. Architecture Diagram (with image)
5. Prerequisites from [Client] (round bullets)
6. High Level Sprint Design (sprint labels + deliverable bullets)

For German documents:

1. Ausgangslage
2. In-Scope Funktionen (mit Unterabschnitten pro Use Case)
3. Out-of-Scope Funktionen (Strich-Aufzählung)
4. Architekturdiagramm (mit Bild)
5. Voraussetzungen von [Kunde] (Punkt-Aufzählung)
6. Sprint Design & Zeitplan (Sprint-Labels + Lieferergebnisse)

**Important:** Do NOT add a Conclusion section by default. The 6-section structure above is the standard. Only add extra sections (e.g., "Next Steps", "Open Questions") if the user explicitly requests them. Adding sections increases page count — always respect the 4–5 page limit.

---

## Brand Guidelines

- **Cover color:** Sharp Green #18A05A
- **Heading1 color:** Green #19A960, bold, 15pt
- **Heading2:** Dark #323232, bold, 13pt
- **Body font:** Akkurat LL, ~11pt
- **Cover font:** Wavetable Bold, white on green
- **Logo:** One Thousand circle logo (logo-stack-black.png) on every page via header
- **Company:** One Thousand GmbH

All brand elements are embedded in the template—Claude only provides content.

---

## File Paths (Relative to Skill Directory)

```
scope-document-generator/
├── assets/
│   ├── templates/scope-template/      # Unpacked DOCX template
│   ├── fonts/                          # Akkurat LL, Wavetable
│   └── logos/                          # logo-stack-black.png, etc.
├── scripts/
│   ├── extract_architecture_diagram.py # Extract diagram from PDF/DOCX
│   ├── generate_architecture_diagram.py # Generate diagram (Graphviz → Pillow fallback)
│   └── generate_scope_doc.py           # Main DOCX generation script
├── references/
│   ├── content-extraction-guide.md     # Read in parallel at Phase 2 start
│   ├── section-templates-en.md         # Read in parallel at Phase 2 start
│   ├── section-templates-de.md         # Read in parallel at Phase 2 start (if German)
│   └── anti-hallucination-rules.md     # Read in parallel at Phase 2 start
└── SKILL.md                             # This file
```
