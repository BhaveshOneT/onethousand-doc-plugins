# docs-generator

Claude Cowork plugin by **One Thousand GmbH** for generating professional, branded PoC scope documents from hackathon summaries, project briefs, or meeting notes.

## What This Plugin Does

Transforms unstructured project input (PDFs, DOCX files, text notes) into client-ready scope documents with:

- One Thousand branded cover page, headers, and formatting
- Numbered sections with green Heading1 / dark Heading2 styles
- Graphviz-rendered architecture diagrams (Pillow fallback if Graphviz unavailable)
- Confidence-scored content with iterative review for weak sections
- Anti-hallucination verification (never invents metrics, features, or timelines)
- English and German language support

**Output:** A `.docx` file ready for client delivery.

## Installation

This plugin is distributed via the `onethousand-doc-plugins` private marketplace.

```
/plugin marketplace add BhaveshOneT/onethousand-doc-plugins
/plugin install docs-generator@onethousand-doc-plugins
```

## Usage

Invoke the skill by saying any of these trigger phrases:

```
/scope-document
```

Or naturally in conversation: "create a scope document", "generate scope for this project", "convert hackathon to scope", "client deliverable", "project definition document".

## Plugin Structure

```
docs-generator/
├── .claude-plugin/
│   └── plugin.json                      # Plugin manifest (name, version, keywords)
├── package.json                         # Node package metadata
├── skills/
│   └── scope-document-generator/
│       ├── SKILL.md                     # Full skill instructions (start here)
│       ├── scripts/
│       │   ├── generate_scope_doc.py    # DOCX assembly from JSON content + template
│       │   ├── generate_architecture_diagram.py  # Graphviz/Pillow diagram renderer
│       │   └── extract_architecture_diagram.py   # Extract diagram from source PDF/DOCX
│       ├── assets/
│       │   ├── templates/scope-template/ # Unpacked DOCX template (OT branding baked in)
│       │   ├── logos/                    # logo-stack-black.png, logo-stack-neural-lime.png
│       │   └── fonts/                    # Akkurat LL Regular/Bold (.otf + .ttf)
│       └── references/
│           ├── anti-hallucination-rules.md   # CRITICAL: read before content generation
│           ├── content-extraction-guide.md   # Patterns for extracting info from source docs
│           ├── section-templates-en.md       # English section writing patterns
│           └── section-templates-de.md       # German section writing patterns
└── README.md
```

## How It Works (Agent Workflow)

The skill runs in 6 phases. Full details are in `skills/scope-document-generator/SKILL.md`.

### Phase 1 — Input Collection
Ask the user for: language (EN/DE), source document, cover details (project name, subtitle, client name), and whether to extract or generate the architecture diagram.

### Phase 2 — Content Extraction
Read `references/content-extraction-guide.md` and `references/anti-hallucination-rules.md`, then extract structured information from the source document using pandoc or Python tools.

### Phase 3 — Content Generation with Confidence Scoring
Generate `variables.json` (cover metadata) and `content.json` (all sections). Each section is scored 0-100 across five dimensions: source grounding, specificity, completeness, actionability, anti-hallucination. Sections below their threshold trigger targeted follow-up questions to the user. The loop repeats until all sections pass or the user overrides.

### Phase 4 — Architecture Diagram
Generate or extract the architecture diagram. The generation script accepts a JSON description with zones, typed components, and data flows, and renders via Graphviz `dot`.

```bash
python scripts/generate_architecture_diagram.py \
  --description /tmp/arch_desc.json \
  --output /tmp/arch_diagram.png \
  --style detailed
```

### Phase 5 — Document Assembly
Assemble the final DOCX from the template, variables, content, and diagram:

```bash
python scripts/generate_scope_doc.py \
  --template-dir assets/templates/scope-template \
  --variables /tmp/scope_variables.json \
  --content /tmp/scope_content.json \
  --output /path/to/output.docx \
  --arch-diagram /tmp/arch_diagram.png
```

### Phase 6 — Verification
Validate the DOCX opens correctly, display final confidence scores, flag any `[To be confirmed]` markers.

## Standard Document Sections

| # | English | German |
|---|---------|--------|
| 1 | Initial Context | Ausgangslage |
| 2 | In-Scope Features | In-Scope Funktionen |
| 3 | Out-of-Scope Features | Out-of-Scope Funktionen |
| 4 | Architecture Diagram | Architekturdiagramm |
| 5 | Prerequisites from [Client] | Voraussetzungen von [Kunde] |
| 6 | High Level Sprint Design | Sprint Design & Zeitplan |

## Content JSON Schema

Two JSON files drive document generation:

**`variables.json`** — Cover page metadata:
```json
{
  "cover_title": "PROJECT NAME",
  "cover_subtitle": "Project Scope Document",
  "cover_client_x_ot": "ClientName x One Thousand",
  "language": "en"
}
```

**`content.json`** — Section content (see SKILL.md for full schema):
```json
{
  "sections": [
    {
      "number": "1",
      "title": "Initial Context",
      "content": "Paragraph text. Use \\n\\n for breaks.",
      "subsections": [],
      "bullet_points": [],
      "bullet_style": "normal"
    }
  ]
}
```

Key fields: `is_sprint_section` (bool) for sprint layout, `bullet_style` (`"normal"` or `"dash"`), subsections for Heading2-level content.

## Requirements

- Python 3.10+
- `python-docx` (DOCX generation)
- `graphviz` system package (architecture diagrams; falls back to Pillow if missing)
- `Pillow` (fallback diagram renderer)

## Brand Reference

| Element | Value |
|---------|-------|
| Cover color | `#18A05A` (Sharp Green) |
| Heading1 | `#19A960`, bold, 15pt |
| Heading2 | `#323232`, bold, 13pt |
| Body font | Akkurat LL, ~11pt |
| Logo | One Thousand circle logo on every page |

All branding is embedded in the DOCX template — agents only provide content.

## License

Proprietary — One Thousand GmbH
