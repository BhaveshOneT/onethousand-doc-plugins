# Design Plan Structure Reference

This document defines the standard structure for One Thousand Project Design Plan pages in Confluence. The structure is derived from analysis of real design plan pages across multiple projects.

---

## Standard Sections

### 1. Overview

**Purpose:** Provide a concise project description that orients the reader.

**Content pattern:**
- Paragraph 1: What the project is + what problem it solves (2-3 sentences)
- Paragraph 2: Technical approach — what technologies/methods are used (2-3 sentences)
- Paragraph 3 (optional): Delivery model, hosting, external collaborations (1-2 sentences)

**Length:** 100-200 words (2-3 short paragraphs)

**Example patterns:**

Pattern A (Product-focused):
"**[PROJECT_NAME]** is an AI-powered [product type] for [target users]. The [system/game/tool] [key capability] based on [input/method], and delivers [output] to [target platform/users]. The project leverages [technology stack] for [core function] and integrates [external service] to produce [output type]."

Pattern B (Solution-focused):
"This project develops a **minimum viable product** tailored for [use case]. Within [timeline], structured into [N] sprints, the primary focus is on [core objective]. This integration will empower users with [key benefit], enhancing [business outcome]."

**Bolding:** Project name should be bold on first mention.

---

### 2. Key Requirements

**Purpose:** List the functional and non-functional requirements that drive sprint planning.

**Format:** Bullet list with 1-2 sentence items.

**Content pattern:**
```markdown
## Key Requirements

- [Functional requirement 1 with specific detail]
- [Functional requirement 2 with specific detail]
- [Non-functional requirement: performance/scale/budget]
- [Integration requirement with specific systems]
- [Quality/testing requirement]
```

**Important notes box:** If requirements include assumptions, add:
```markdown
**Important note:** The numbers mentioned above can be assumptions, and not exact numbers (for instance: [example]).
```

**Length:** 5-10 bullet items, each 1-2 sentences.

---

### 3. Notes & Dependencies (Optional)

**Purpose:** Highlight external dependencies, collaboration requirements, and important considerations.

**When to include:** Only when there are significant external dependencies or collaboration notes that don't fit elsewhere.

**Format:** Bullet list or short paragraphs.

**Example:**
```markdown
## Notes & Dependencies

- **[Partner name]** deliverables: [specific items they must provide]
- **Important collaboration:** [collaboration cadence/format]
- [Other dependency or note]
```

---

### 4. Architecture

**Purpose:** Visual and textual representation of the system architecture.

**Structure options:**

Option A (Single architecture):
```markdown
## Architecture

[1-2 sentence description of the architecture basis]

![Architecture Diagram](attachment)

**Notes:**
- [Infrastructure note 1]
- [Infrastructure note 2]
```

Option B (Evolving architecture):
```markdown
## Initial Architecture

[1 sentence about when/how this was designed]

![Initial Architecture](attachment)

## Updated Architecture

[1 sentence about what changed and why]

![Updated Architecture](attachment)
```

**Architecture diagram generation:** Use the Graphviz-based `generate_architecture_diagram.py` script with the standard JSON description format (zones, components, flows).

---

### 5. Sprint Plan Overview

**Purpose:** High-level summary of all sprints — the "elevator pitch" version.

**Format:** Numbered or bulleted list with one line per sprint.

**Content pattern:**
```markdown
## Sprint Plan Overview

- **Sprint 1:** [One-line goal description]
- **Sprint 2:** [One-line goal description]
- **Sprint 3:** [One-line goal description]
- ...
```

**Optional:** Can include two versions:
1. "What was communicated to [Client]" — original plan
2. "Updated overview" — revised plan after feedback

**Length:** One line per sprint, max ~100 words total.

---

### 6. Timeline & Design (CORE SECTION)

**Purpose:** Detailed sprint breakdown with timeline, goals, and epics.

**This is the most important and detailed section.** It maps directly to project execution.

**Format:** Markdown table with the following columns:

| Column | Required | Content |
|--------|----------|---------|
| Sprint / Phase | Yes | Sprint number and name |
| Timeline (CW) | Yes | Calendar week range (e.g., CW 32–33) |
| Goal | Yes | 1-2 sentence sprint goal |
| Epics (High-Level Features) | Yes | Detailed breakdown of work items |
| Estimated Client Effort | Optional | Person-days from client team |

**Epic formatting within table cells:**

Use category prefixes to organize epics:
- **Data:** [data-related tasks]
- **AI:** [AI/ML-related tasks]
- **Pipeline:** [infrastructure/pipeline tasks]
- **Integration:** [integration tasks]
- **Testing:** [testing/QA tasks]
- **Documentation:** [docs/handover tasks]

**Status markers** (only if confirmed in source):
- `→ Done` or `[DONE]` for completed items
- `→ WIP` for work in progress
- No marker for planned items

**Table template:**
```markdown
## Timeline & Design

| Sprint / Phase | Timeline (CW) | Goal | Epics (High-Level Features) |
|---|---|---|---|
| **Sprint 0 - Alignment / Preparation** | CW XX & YY | Align on data + integration | **Data:** [items] **Integration:** [items] |
| **Sprint 1** | CW XX & YY | [Goal] | **Data:** [items] **AI:** [items] **Pipeline:** [items] |
| **Sprint 2** | CW XX & YY | [Goal] | **AI:** [items] **Integration:** [items] **Testing:** [items] |
| **Sprint N (Final)** | CW XX & YY | Testing + deployment | **Testing:** [items] **Documentation:** [items] |
| **Release event** | CW XX | | 🎉 |
```

**Length:** One row per sprint. Epic descriptions can be multi-line within cells (use `<br>` or `+` for line breaks in Confluence markdown).

---

### 7. Design Decisions (Optional)

**Purpose:** Document key technical decisions made during planning.

**When to include:** Only when specific design decisions were discussed in source material.

**Format:** Bullet list or short descriptions.

**Example:**
```markdown
## Design Decisions

- Send the board configuration with each story request
- Store ID-to-asset-name mapping in the relational database:
  - IDs are machine-level identifiers (6 bytes)
  - Name mappings are human-readable strings understood by the backend
```

---

### 8. Effort Estimation (Optional)

**Purpose:** Outline expected effort from the client team per sprint.

**When to include:** Only when effort data was discussed with the client.

**Format:** Grouped by sprint and team.

**Example:**
```markdown
## Effort Estimation

**Sprint 0: Application team**
- Define the 20 cities for processing (1 person day)
- Export document samples (1 person day)

**Sprints 0+1: IT**
- Define data exchange process (5 person days)
- Setup Azure subscription and resource groups (1 person day)

**Sprint 3: Application team**
- Suggest validation rules (2 person days)

**Sprints 2–5: IT and application team**
- Testing sessions and feedback (1 person day each team each sprint)
```

**Notes:**
- Differentiate between IT team and application/business team
- Specify that estimates exclude meeting time (kick-off, jour fixes)
- Use person-days as the unit

---

## Confluence-Specific Formatting

### Page Title
- Standard: "Project Design Plan"
- With project name: "[PROJECT_NAME] - Design Plan"
- With version: "Project Design Plan v2"

### Page Hierarchy
```
[Space Root]
  └── [Use Case / Project Name]
       └── Project Management
            └── Project Design Plan  ← THIS PAGE
```

### Markdown Compatibility
Confluence markdown supports:
- `## Headings` (h2-h6)
- `**bold**` and `*italic*`
- `- bullet lists` and `1. numbered lists`
- `| table | syntax |`
- `![alt](url)` for images
- `> blockquotes`
- `` `inline code` `` and code blocks

### Table Tips
- Keep table cells concise
- Use `+` or manual line breaks for multi-line cells
- Bold category prefixes: `**Data:** items`
- Use consistent column widths
