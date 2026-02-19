---
name: hackathon-debrief
description: >
  Generate professional One Thousand branded hackathon debrief documents (DOCX).
  Triggers on: "hackathon debrief", "debrief document", "generate debrief",
  "hackathon report", "create debrief", "write debrief", "debrief for this",
  "hackathon summary document", "hackathon writeup", "post-hackathon document",
  "debrief doc", "debrief docx".
  Transforms hackathon notes, PDFs, meeting transcripts, and images into
  professional debrief documents with branded cover page, table of contents,
  confidence-scored content generation, and anti-hallucination verification.
  Supports English and German. Produces DOCX output with green branded
  title page, One Thousand logo, professional typography, and structured sections.
license: Proprietary
triggers:
  - "hackathon debrief"
  - "debrief document"
  - "generate debrief"
  - "hackathon report"
  - "create debrief"
  - "write debrief"
  - "debrief for this"
  - "hackathon summary"
  - "hackathon writeup"
  - "post-hackathon document"
  - "debrief doc"
  - "debrief docx"
  - "hackathon document"
  - "write a debrief"
  - "make a debrief"
---

# Hackathon Debrief Generator Skill

## Overview

This skill generates **professional One Thousand branded hackathon debrief documents** (DOCX format) from raw source material. It takes hackathon notes, PDFs, meeting transcripts, and optional images, then produces a publication-ready document with:

- Green branded cover page with One Thousand logo
- Table of contents with dotted leaders
- Structured sections with branded headings
- Confidence-scored content generation
- Anti-hallucination verification
- Support for both German and English

The workflow: Collect inputs (source material + language) -> Extract information -> Generate content with confidence scoring -> Iteratively review weak sections -> Run anti-hallucination verification -> Assemble branded DOCX -> Deliver.

**Output:** A branded DOCX file with green cover page (#19A960), "hackathon" / "debrief" display text, One Thousand logo, participant listing, professional headings in green, table of contents, and structured content sections.

---

## When to Use This Skill

**ALWAYS invoke this skill when the user's request matches ANY of these patterns:**

- User says "hackathon debrief", "debrief document", or "hackathon report"
- User says "create/generate/write a debrief" for some hackathon
- User has hackathon notes/PDFs and wants a "professional document" or "client deliverable"
- User wants to write up hackathon findings as a formal document
- User says "hackathon writeup" or "post-hackathon document"
- User needs a debrief document for a completed hackathon

**Do NOT invoke for:** scope documents (use scope-document-generator), slide decks (use hackathon-presentation), spreadsheets, or non-debrief deliverables.

---

## Inputs

### Source Material (Required)
- Hackathon notes, PDFs, DOCX files, or text pasted in conversation
- Meeting transcripts or recordings
- Can include multiple files — extract and combine content from all sources
- This is the **primary source of truth** for all content

### Optional Enrichment
- Post-hackathon decisions, scope changes, follow-up meeting notes
- Screenshots or images from the hackathon (embedded as base64 in sections)
- Architecture diagrams or process flows
- Canvas data (AI Breakthrough Canvas)

---

## Workflow

### Phase 1: Input Collection

Ask the user using AskUserQuestion:

1. **Language:** English or German?
2. **Source Material:** Hackathon notes, PDFs, transcripts, or text
3. **Additional Context:** Post-hackathon decisions, follow-up notes (optional)
4. **Images:** Any screenshots, diagrams, or photos to include? (optional)

**Note:** Python dependencies (`python-docx`, `Pillow`) are installed automatically by the plugin's SessionStart hook. No manual `pip install` is needed.

---

### Phase 2: Content Extraction

#### Parallel Reference File Loading

Before generating, Claude **MUST** read these reference files. **Read ALL FOUR files in parallel** (use multiple Read tool calls in a single message):

- `references/section-templates-en.md` OR `references/section-templates-de.md` — prompt templates for the chosen language
- `references/style-patterns.md` — the 5 mandatory style patterns
- `references/anti-hallucination-rules.md` — verification framework
- `references/sample-excerpts-en.md` OR `references/sample-excerpts-de.md` — tone/structure examples

**Important:** These are data-loading calls, not generation steps. Reading them in parallel produces the exact same context as reading them sequentially.

#### Extract from Source Material

From the provided hackathon documents, extract:

1. **Company info:** Name, industry, background, AI opportunity
2. **Participants:** Customer team (names + roles), One Thousand team (names + roles)
3. **Metadata:** Hackathon title, dates, location, format
4. **Use cases:** Title, challenge description, pain points, current process
5. **Goals:** Primary goal, secondary goals, expected benefits, success criteria
6. **Data sources:** Name, type, volume, quality for each source
7. **Approach:** Proposed solution, technical details, architecture, technologies
8. **Results:** Quantitative metrics (before/after), qualitative outcomes, live demo results
9. **Canvas data:** Pain, Data, Value, Users, Compliance, Security (if available)
10. **User flow:** Input sources, processing steps, output integration (if available)
11. **Recommendations:** Short/medium/long-term recommendations
12. **Next steps:** Action items with owners and deadlines

Build a structured data object from the extracted information.

---

### Phase 3: Section Generation with Confidence Scoring

Generate each section using the prompt templates from the reference files.

#### Confidence Scoring System

After generating each section, self-assess a **confidence score (0-100)** based on five dimensions (each 0-20 points):

1. **Source Grounding (0-20):** Is every claim traceable to the source document?
2. **Specificity (0-20):** Are names, tools, integrations specific rather than generic?
3. **Completeness (0-20):** Does the section cover its full purpose?
4. **Actionability (0-20):** Can someone act on this content?
5. **Anti-Hallucination (0-20):** Is the section free of invented details?

#### Section-Specific Thresholds

| Section | Threshold | Rationale |
|---------|-----------|-----------|
| Participants | 90 | Just data extraction — should be nearly perfect |
| Background | 75 | Some framing language is generic by nature |
| Hackathon Structure | 70 | Structural description with some standard elements |
| Challenge | 80 | Core problem statement — must be precise |
| Goal | 75 | Derived from challenge — allows some synthesis |
| Data | 75 | Data listing must be accurate |
| Approach | 80 | Technical solution — must be precise |
| Results | 80 | Metrics must be exact |
| Canvas (optional) | 65 | Structured framework allows some synthesis |
| User Flow (optional) | 65 | Process description allows some synthesis |
| Conclusion | 75 | Summary with forward-looking — some synthesis allowed |

#### Iterative Review Loop

After scoring all sections, if ANY section falls below its threshold:

1. **Show the user a summary table:**
   ```
   Section                  Score   Status
   ─────────────────────────────────────────
   1. Participants            95     Pass
   2. Background              82     Pass
   3. Hackathon Structure     78     Pass
   4. Challenge               62     Needs input
   5. Goal                    74     Needs input (below 75)
   ...
   ```

2. **For each failing section, ask specific questions using AskUserQuestion.** Do NOT ask vague questions. Ask precisely what's missing:
   - "Challenge scored 62/100. The source mentions 'manual process issues' but doesn't specify concrete metrics. Can you clarify: (a) how many hours per month are spent manually? (b) what is the current error rate?"

3. **Re-generate the failing sections** with the new input.
4. **Re-score** and repeat until all sections pass OR the user says to proceed anyway.

**The user can always override** by saying "proceed anyway", "good enough", or similar — in which case, proceed with `[To be confirmed]` / `[Noch zu bestätigen]` markers.

---

### Phase 4: Anti-Hallucination Verification

Run the 4-check verification framework from `references/anti-hallucination-rules.md`:

1. **Metrics Check (20%):** Every number traces to source
2. **Terminology Check (20%):** Domain terms match source, not sample excerpts
3. **Style Patterns (30%):** All 5 patterns correctly applied
4. **Completeness (30%):** All sections present, all pain points covered

Flag any section that fails. Ask the user for corrections.

---

### Phase 5: Document Assembly

#### Step 5.1: Write Content JSON

Write the structured content to a JSON file at `/tmp/debrief_content.json`:

```json
{
  "language": "de",
  "company": {
    "name": "Company GmbH",
    "industry": "Manufacturing"
  },
  "metadata": {
    "title": "AI-Powered Invoice Processing",
    "dates": {
      "start": "25. Juni 2025",
      "end": "26. Juni 2025"
    },
    "date": "25.-26. Juni 2025",
    "location": "Frankfurt"
  },
  "participants": {
    "customer": [
      { "name": "Dr. Michael Weber", "role": "Leiter Finanzen" },
      { "name": "Sandra Mueller", "role": "Teamleiterin" }
    ],
    "oneThousand": [
      { "name": "David Chen", "role": "AI Solutions Architect" },
      { "name": "Anna Kowalski", "role": "Data Engineer" }
    ]
  },
  "useCases": [
    { "title": "Automated Document Bundling" }
  ],
  "sections": [
    {
      "id": "background",
      "title": "Hintergrund",
      "content": "## Hintergrund\n\nMarkdown content here..."
    },
    {
      "id": "hackathon_structure",
      "title": "Hackathon",
      "content": "..."
    },
    {
      "id": "challenge",
      "title": "Herausforderung",
      "content": "..."
    },
    {
      "id": "goal",
      "title": "Ziel",
      "content": "..."
    },
    {
      "id": "data",
      "title": "Daten",
      "content": "..."
    },
    {
      "id": "approach",
      "title": "Ansatz",
      "content": "..."
    },
    {
      "id": "results",
      "title": "Ergebnisse",
      "content": "..."
    },
    {
      "id": "conclusion",
      "title": "Fazit und Ausblick",
      "content": "..."
    }
  ]
}
```

**Content JSON Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `language` | string | "de" or "en" |
| `company.name` | string | Client company name |
| `company.industry` | string | Client industry |
| `metadata.title` | string | Hackathon/use case title |
| `metadata.dates.start` | string | Start date |
| `metadata.dates.end` | string | End date |
| `metadata.date` | string | Formatted date string (fallback if dates not split) |
| `metadata.location` | string | Hackathon location |
| `participants.customer` | array | Customer participants with name and optional role |
| `participants.oneThousand` | array | OT participants with name and optional role |
| `useCases` | array | Use cases with title (first used for cover page subtitle) |
| `sections` | array | Generated sections with id, title, and markdown content |

**Section IDs (in order):** `background`, `hackathon_structure`, `challenge`, `goal`, `data`, `approach`, `results`, `canvas` (optional), `user_flow` (optional), `conclusion`

**Section Content Format:** Each section's `content` field contains markdown text. The Python script converts markdown to DOCX formatting:
- `## Heading` -> H2 (14pt, green, Amsi Pro Narw Black)
- `### Heading` -> H3 (12pt, green, Amsi Pro Narw Black)
- `**bold**` -> Bold text
- `*italic*` -> Italic text
- `- item` -> Bullet list
- `1. item` -> Numbered list
- Markdown tables -> Formatted DOCX tables
- `![alt](data:image/png;base64,...)` -> Embedded images

#### Step 5.2: Run Python Script

```bash
SKILL_DIR="<path_to_hackathon-debrief_skill>"

python "$SKILL_DIR/scripts/generate_debrief_doc.py" \
  --content /tmp/debrief_content.json \
  --logo-dir "$SKILL_DIR/assets/logos/" \
  --output /path/to/output/hackathon_debrief.docx
```

The script generates a branded DOCX with:
- Full-page green (#19A960) title page with logo, display text, participants
- Table of contents with dotted leaders and bookmarked links
- Content sections with branded green H1 headings
- Markdown-to-DOCX conversion (headings, lists, tables, images, inline formatting)
- Page numbers in bottom-right footer
- A4 page size with 1-inch margins

#### Step 5.3: Deliver

After generation:
1. Validate the DOCX by checking it has the expected section count
2. Report the final confidence scores
3. Flag any sections with `[To be confirmed]` markers
4. Provide the file path to the user

---

## Style Pattern Rules

The 5 mandatory style patterns MUST be applied in every debrief document. See `references/style-patterns.md` for full details.

| Pattern | Where Applied | Requirement |
|---------|--------------|-------------|
| Three Pillars | Conclusion | MUST start with "Während des Hackathons haben wir uns intensiv mit den drei Hauptpfeilern beschäftigt" (DE) / "During the hackathon, we focused intensively on the three main pillars" (EN) |
| Forward-Looking | Conclusion | MUST end with "Wir würden uns sehr freuen, diese Erfolgsgeschichte gemeinsam mit Ihnen schreiben zu dürfen!" (DE) / "We would be delighted to write this success story together with you!" (EN) |
| AI Journey | Background | Must use "KI-Reise"/"AI journey" and "Transformation" terminology |
| Collaborative Tone | All sections | Use "wir"/"we" over "sie"/"they" — emphasize partnership |
| Evidence-Based | Challenge, Data, Results | All metrics must trace to source data — never invent numbers |

---

## Domain Adaptation Rule

**CRITICAL:** The sample excerpts in `references/sample-excerpts-*.md` show STRUCTURE and TONE only. ALL domain-specific content must come EXCLUSIVELY from the provided source data:

- Company names: Use ACTUAL client name, never "LOGEX" or "TechFlow"
- Industry terminology: Use client's domain terms, never sample domain terms
- Process names: Use client's actual processes
- Technical systems: Use client's actual tech stack
- Metrics: Use client's actual numbers

**Example of WRONG behavior:** Source is about healthcare, but output uses "Dokumentenbündelung" (from LOGEX sample) instead of the client's actual process.

---

## Content Quality Standards

### Tone & Voice
- Professional, partnership-focused, results-oriented
- First person plural ("we") when describing joint work
- Confident but not arrogant
- Technical precision without jargon overload

### Formatting Rules
- Format lists with one item per line; never combine numbering like "1. 2." on a single line
- Do NOT use checkbox markdown (- [ ]) or nested list markers (* *, * -)
- Do NOT use markdown tables in sections that specify "Do NOT use markdown tables"
- Only include dates or commitments if explicitly present in source data
- Keep sections concise and report-grade
- Target 2,200-3,200 words for core sections

### Anti-Hallucination Rules
1. NEVER invent metrics, KPIs, or statistics
2. NEVER fabricate company details
3. NEVER add technologies not mentioned in source
4. NEVER invent participant names
5. NEVER copy domain terms from sample excerpts
6. NEVER assume timelines unless explicitly stated
7. Use "[Noch zu bestätigen]" (DE) or "[To be confirmed]" (EN) for unknowns
8. Every claim in Results must align with Challenge/Goal/Approach
9. Prefer omission over invention

---

## Section Order

Sections appear in the document in this fixed order:

1. **Background** (Hintergrund) — Company context, AI journey, partnership
2. **Hackathon** (Hackathon) — Event details, dates, agenda
3. **Challenge** (Herausforderung) — Pain points, current process issues
4. **Goal** (Ziel) — Primary/secondary goals, success criteria
5. **Data** (Daten) — Data sources, quality, privacy
6. **Approach** (Ansatz) — Technical solution, architecture, technologies
7. **Results** (Ergebnisse) — Quantitative/qualitative outcomes
8. **AI Breakthrough Canvas** (optional) — Canvas analysis
9. **User Flow** (optional) — Process flow mapping
10. **Conclusion** (Fazit und Ausblick) — Summary, recommendations, next steps

**Note:** Participants are shown on the title page only, NOT as a separate content section.

---

## File Paths (Relative to Skill Directory)

```
hackathon-debrief/
├── SKILL.md                              # This file
├── scripts/
│   └── generate_debrief_doc.py           # Python DOCX generator
├── assets/
│   └── logos/
│       └── onethousand-icon-limeonblack-rounded.png  # Cover page logo
├── references/
│   ├── section-templates-de.md           # German section prompts
│   ├── section-templates-en.md           # English section prompts
│   ├── style-patterns.md                 # 5 mandatory style patterns (DE/EN)
│   ├── sample-excerpts-de.md             # German sample document (LOGEX)
│   ├── sample-excerpts-en.md             # English sample document (TechFlow)
│   └── anti-hallucination-rules.md       # Verification framework
```

---

## Brand Guidelines

| Element | Font | Size | Color |
|---------|------|------|-------|
| Title page "hackathon" / "debrief" | Amsi Pro Narw Black | 48pt | White on #19A960 |
| Use case subtitle | Amsi Pro Narw Black | 24pt | White |
| H1 section headings | Amsi Pro Narw Black | 16pt | #19A960 |
| H2 subsection headings | Amsi Pro Narw Black | 14pt | #19A960 |
| H3 sub-subsection | Amsi Pro Narw Black | 12pt | #19A960 |
| Body text | Akkurat LL | 11pt | #2F2F2F |
| TOC title | Amsi Pro Narw Black | 28pt | #19A960 |
| Footer page numbers | Akkurat LL | 10pt | #2F2F2F |
| Cover page background | — | — | #19A960 (Sharp Green) |
