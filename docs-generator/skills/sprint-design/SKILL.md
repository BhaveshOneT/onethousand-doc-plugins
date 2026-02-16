---
name: sprint-design
description: >
  Generate detailed Project Design Plan pages directly in Confluence.
  Triggers on: "design plan", "sprint design", "project design plan",
  "sprint plan", "create design plan", "generate sprints",
  "project timeline", "sprint breakdown", "design plan for this".
  Transforms hackathon summaries and customer conversation inputs into
  structured Confluence pages with overview, key requirements, architecture
  diagram, sprint timeline table, and effort estimation — placed under the
  correct use-case → project management → project design plan hierarchy.
  Supports English and German. Includes confidence scoring and smart
  Confluence lookup for missing data.
license: Proprietary
triggers:
  - "design plan"
  - "sprint design"
  - "project design plan"
  - "sprint plan"
  - "create design plan"
  - "generate sprints"
  - "project timeline"
  - "sprint breakdown"
  - "design plan for this"
  - "sprint design for this"
  - "create sprints"
  - "timeline and sprints"
---

# Sprint Design (Project Design Plan) Skill

## Overview

This skill generates **Project Design Plan** pages directly in Confluence, following the established One Thousand structure. It takes two inputs — a hackathon summary document and additional customer conversation context — and produces a comprehensive design plan with architecture diagrams, sprint timelines, and effort estimations.

The workflow: Collect inputs → Extract content → Score confidence → Smart-fill gaps from Confluence → Ask user for remaining gaps → Generate architecture diagram → Publish to Confluence → Verify.

**Output:** A Confluence page published under `[Use Case Space] → Project Management → Project Design Plan` with markdown-formatted content, architecture diagram image, and structured sprint table.

---

## When to Use This Skill

**ALWAYS invoke this skill when the user's request matches ANY of these patterns:**

- User says "design plan", "sprint design", "project design plan", or "sprint plan"
- User wants to create sprints/timeline from a hackathon summary
- User wants to generate a "project design plan" in Confluence
- User has hackathon output and customer feedback and wants to plan sprints
- User says "create design plan for [project]" or similar

**Do NOT invoke for:** scope documents (use scope-document-generator), general Word docs, slide decks, or non-Confluence deliverables.

---

## CRITICAL: Safety Rules

### No Modification or Deletion of Existing Data

1. **NEVER modify** existing Confluence pages unless explicitly told to update a specific page
2. **NEVER delete** any Confluence pages, comments, or content
3. When publishing, **always create a NEW page** under the correct parent
4. If a "Project Design Plan" page already exists under the target parent, **ASK the user** before proceeding:
   - Option A: Create with a different title (e.g., "Project Design Plan v2" or "Project Design Plan - Updated")
   - Option B: Update the existing page (only with explicit user confirmation)
5. Before publishing, **always show the user a preview** of what will be created and where

### No Hallucination

All anti-hallucination rules from `references/anti-hallucination-rules.md` apply. Key summary:
- NEVER invent metrics, KPIs, timelines, or technical details
- EVERY claim must trace to the hackathon document or customer conversation
- Use `[To be confirmed]` / `[Noch zu bestätigen]` for unknowns
- NEVER add features, components, or sprints not discussed in source material
- NEVER assume sprint durations, team sizes, or effort estimates

---

## Inputs

This skill requires **two inputs**:

### Input 1: Hackathon Summary Document
- Can be a PDF, DOCX, or text pasted in conversation
- If uploaded as a file, extract text using appropriate tools
- This is the **primary source of truth** for technical content

### Input 2: Customer Conversation / Additional Context
- Notes from post-hackathon discussions with the customer
- Can be provided as text in the conversation, meeting notes, or email excerpts
- May contain updated requirements, scope changes, timeline preferences
- **Priority:** Customer conversation input overrides hackathon doc when there are conflicts (flag the conflict)

---

## Workflow

### Phase 1: Input Collection + Background Setup

Ask the user using AskUserQuestion:

1. **Language:** English or German?
2. **Confluence Space:** Which space should the design plan be created in? (Provide space key or name)
3. **Project/Use Case Name:** Name of the project (used for page title)
4. **Hackathon Document:** Source file (PDF, DOCX, or text)
5. **Customer Notes:** Additional context from customer conversations
6. **Architecture Diagram:** Extract from source, generate new, or skip?

#### Background: Pre-warm Dependencies

**While waiting for user responses**, launch a background agent to install dependencies:

```bash
pip install pdfplumber python-docx Pillow graphviz --break-system-packages --quiet 2>/dev/null
which dot || echo "Graphviz not installed — will use Pillow fallback for diagrams"
```

---

### Phase 2: Confluence Navigation + Content Extraction

#### Step 2a: Find the Correct Parent Page

The design plan MUST be created under the correct hierarchy:
```
[Space Root]
  └── [Use Case / Project Name]
       └── Project Management
            └── Project Design Plan  ← CREATE HERE
```

**To find the parent:**

1. Use the Confluence MCP tools to search for "Project Management" pages in the target space:
   ```
   searchConfluenceUsingCql: title = "Project Management" AND space = "[SPACE_KEY]" AND type = page
   ```

2. If found, use that page's ID as the parent for the new design plan page.

3. If NOT found, ask the user:
   - "I couldn't find a 'Project Management' page in space [SPACE_KEY]. Should I create the page hierarchy, or place it somewhere else?"

4. Before creating, check if a "Project Design Plan" page already exists under that parent:
   ```
   getConfluencePageDescendants: pageId = [PROJECT_MANAGEMENT_PAGE_ID]
   ```
   If one exists, ask user whether to create a new version or update.

#### Step 2b: Smart Confluence Lookup for Missing Data

Before asking the user for missing information, **search Confluence** for data that might already exist:

1. **Search for scope documents** in the same space:
   ```
   searchConfluenceUsingCql: title ~ "scope" AND space = "[SPACE_KEY]" AND type = page
   ```

2. **Search for hackathon pages**:
   ```
   searchConfluenceUsingCql: title ~ "hackathon" AND space = "[SPACE_KEY]" AND type = page
   ```

3. **Search for architecture pages**:
   ```
   searchConfluenceUsingCql: title ~ "architecture" AND space = "[SPACE_KEY]" AND type = page
   ```

4. **Search for requirements pages**:
   ```
   searchConfluenceUsingCql: title ~ "requirements" AND space = "[SPACE_KEY]" AND type = page
   ```

If relevant pages are found, read their content and use it to fill gaps — but **always attribute the source** and maintain traceability.

#### Step 2c: Content Extraction

**Read reference files in parallel** (use multiple Read tool calls in a single message):

- `references/anti-hallucination-rules.md` — what NOT to invent
- `references/design-plan-structure.md` — structure templates based on real examples

**From the hackathon document, extract:**

1. Project overview / description
2. Key requirements (functional and non-functional)
3. Technical approach / technologies used
4. Architecture components and data flows
5. Timeline discussions or sprint suggestions
6. Dependencies and external collaborations
7. Data sources and infrastructure details
8. Effort estimations (if mentioned)

**From customer conversation, extract:**

1. Updated/refined requirements
2. Timeline preferences or constraints
3. Sprint structure preferences
4. Client effort expectations
5. Priority changes
6. New dependencies or prerequisites

---

### Phase 3: Content Generation with Confidence Scoring

#### CRITICAL: Confidence Scoring System

After generating each section, Claude MUST self-assess a **confidence score (0–100)** based on five dimensions. This score is used internally to decide whether to ask the user for more input.

**Scoring Criteria per Section (each 0–20 points):**

1. **Source grounding (0–20):** Is every claim traceable to source? (20 = every sentence backed, 0 = entirely invented)
2. **Specificity (0–20):** Are names, tools, integrations specific? (20 = "GCP Firestore via REST API", 0 = "the database")
3. **Completeness (0–20):** Does the section cover its purpose fully? (20 = nothing missing, 0 = skeletal)
4. **Actionability (0–20):** Can someone act on this content? (20 = clear deliverables, 0 = hand-wavy)
5. **Anti-hallucination (0–20):** Is the section free of invented details? (20 = nothing fabricated, 0 = multiple fabrications)

**Section-specific minimum thresholds:**

| Section | Minimum Score | Rationale |
|---------|--------------|-----------|
| Overview | 70 | Framing can be somewhat generic |
| Key Requirements | 80 | Core input — must be precise |
| Architecture | 65 | Can be supplemented by diagram |
| Sprint Plan Overview | 70 | High-level summary can be broader |
| Timeline & Design Table | 80 | Core deliverable — must be precise |
| Design Decisions | 65 | Can contain open items |
| Effort Estimation | 70 | Client needs to act on these |

#### Iterative Review Loop

After scoring all sections, if ANY section falls below its threshold:

1. **First: Smart Confluence Lookup** — Search for missing data in Confluence (see Step 2b). If found, integrate and re-score.

2. **Then: Show the user a summary table:**
   ```
   Section                    Score   Status
   ──────────────────────────────────────────
   Overview                    85     ✓ Pass
   Key Requirements            62     ✗ Needs input
   Architecture                55     ✗ Needs input
   Sprint Plan Overview        78     ✓ Pass
   Timeline & Design           72     ✗ Needs input (below 80)
   Design Decisions            68     ✓ Pass
   Effort Estimation           45     ✗ Needs input
   ```

3. **For each failing section, ask specific questions.** Do NOT ask vague questions:
   - "Key Requirements scored 62/100. The hackathon doc mentions 'product recommendations' but doesn't specify the number of supported product categories or data source format. Can you clarify: (a) how many product categories, (b) what format does the product data come in?"
   - "Effort Estimation scored 45/100. I found no mention of client-side effort in the source. What effort should we estimate for the client team per sprint? (e.g., person-days for IT, application team)"

4. **Re-generate failing sections** with new input.
5. **Re-score** and repeat until all pass OR user says to proceed anyway.

**The user can always override** by saying "proceed anyway" — use `[To be confirmed]` markers on weak sections.

---

### Phase 4: Architecture Diagram Generation

Every design plan SHOULD include an architecture diagram. Use the **same Graphviz-based approach** as the scope-document-generator skill.

#### Diagram Generation

The diagram generation script is shared with the scope skill. Reference it at:
```
../scope-document-generator/scripts/generate_architecture_diagram.py
```

Or use the local copy at:
```
scripts/generate_architecture_diagram.py
```

**Usage:**
```bash
SKILL_DIR="[path-to-sprint-design-skill]"

python "$SKILL_DIR/scripts/generate_architecture_diagram.py" \
  --description /tmp/arch_desc.json \
  --output /tmp/arch_diagram.png \
  --style detailed
```

**Description JSON format:**
```json
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "Client Infrastructure",
      "components": ["PXM System", "SAP", "Web Portal"]
    },
    {
      "name": "Azure / GCP Environment",
      "color": "#0078D4",
      "components": ["AI Service", "Vector DB", "API Gateway", "Chat Interface"]
    }
  ],
  "components": [
    {"name": "PXM System", "type": "external"},
    {"name": "SAP", "type": "database"},
    {"name": "Web Portal", "type": "client"},
    {"name": "AI Service", "type": "ai"},
    {"name": "Vector DB", "type": "database"},
    {"name": "API Gateway", "type": "gateway"},
    {"name": "Chat Interface", "type": "client"}
  ],
  "flows": [
    {"from": "PXM System", "to": "AI Service", "label": "Product data"},
    {"from": "AI Service", "to": "Vector DB", "label": "Embeddings"},
    {"from": "Chat Interface", "to": "API Gateway", "label": "User queries"},
    {"from": "API Gateway", "to": "AI Service", "label": "Recommendation request"}
  ]
}
```

**Component types → shapes:** `client` (rounded box), `service` (rounded box), `database` (cylinder), `external` (component), `gateway` (3D box), `ai` (double octagon), `queue`, `cache`, `message`

**Rendering pipeline (automatic fallback):**
1. **Graphviz `dot`** — primary renderer
2. **Pillow PNG** — basic grid fallback

#### Uploading Diagram to Confluence

After generating the diagram PNG, embed it in the Confluence page using this priority order:

1. **Primary: Two-step publish** (recommended)
   - First create the page with a placeholder: `[Architecture diagram — see below]`
   - Then use the Confluence attachment upload API (if available) to attach the PNG
   - Update the page body to reference the attachment: `![Architecture Diagram](attachment:arch_diagram.png)`

2. **Fallback: Textual description + manual upload note**
   - Include a detailed text description of the architecture in the page
   - Add a clear note: `**[Architecture diagram to be added — PNG file provided separately]**`
   - Provide the generated PNG file to the user via the workspace folder for manual upload
   - Link: `[View diagram](computer:///sessions/.../arch_diagram.png)`

3. **Last resort: ASCII/text diagram**
   - If Graphviz and Pillow both fail, describe the architecture as a structured text block with components and data flows listed

**Important:** Always inform the user which method was used and whether manual steps are needed.

---

### Phase 5: Confluence Page Generation

#### Design Plan Structure

Based on analysis of real One Thousand design plan pages, the structure follows this pattern:

```markdown
## Overview

[2-3 paragraphs: Project description, tech stack, external collaborations]

## Key Requirements

[Bullet list of functional and non-functional requirements]

## Notes & Dependencies

[Optional: External dependencies, collaboration notes, important considerations]

## Architecture

[1-2 sentence description + diagram image]

### Initial Architecture
[If applicable: first version of the architecture]

### Updated Architecture
[If applicable: revised version after feedback]

## Sprint Plan Overview

[High-level bullet list of sprints with one-line goals]

## Timeline & Design

| Sprint / Phase | Timeline (CW) | Goal | Epics (High-Level Features) |
|---|---|---|---|
| Sprint 1 | CW XX–YY | [Goal] | [Detailed epics with bullet sub-items] |
| Sprint 2 | CW XX–YY | [Goal] | [Detailed epics] |
| ... | ... | ... | ... |

## Design Decisions

[Optional: Key technical decisions made during planning]

## Effort Estimation

[Optional: Table or description of estimated effort from client side]
```

#### Content Format

Generate the page content as **markdown** (Confluence API supports markdown format). Use:
- `##` for main section headings
- `###` for sub-headings
- `|` pipe tables for the timeline
- `*` or `-` for bullet lists
- `**bold**` for emphasis

#### Publishing to Confluence

Use the Confluence MCP tool to create the page:

```
createConfluencePage:
  cloudId: [from getAccessibleAtlassianResources]
  spaceId: [target space ID]
  parentId: [Project Management page ID]
  title: "Project Design Plan"  (or "[Project Name] - Design Plan")
  body: [generated markdown content]
  contentFormat: "markdown"
```

**IMPORTANT:** Always show the user the content preview BEFORE publishing. Ask for explicit confirmation:
- "Here's the design plan I've prepared. Should I publish it to Confluence under [Space] → Project Management → Project Design Plan?"

#### Retrieving the Page URL

After successful creation, the `createConfluencePage` MCP tool returns the page ID. Construct the URL:
```
https://leadmachinelearning.atlassian.net/wiki/spaces/{SPACE_KEY}/pages/{PAGE_ID}
```

Or use the `webUrl` field from the response if available. Always provide this URL to the user.

---

### Phase 6: Verification & Delivery

After publishing:

1. **Verify the page was created** by fetching it back:
   ```
   getConfluencePage: pageId = [newly created page ID]
   ```

2. **Check content integrity:**
   - All sections present
   - Table formatting renders correctly
   - No broken markdown

3. **Final confidence summary:** Display the final confidence scores for all sections

4. **Flag gaps:** Note sections that still have `[To be confirmed]` markers

5. **Provide the Confluence page URL** to the user

---

## Content Quality Standards

### Design Plan Structure: Section Details

Each section has specific content expectations based on analysis of real One Thousand design plans:

#### Overview Section
- 2-3 short paragraphs
- What the project is (one sentence)
- What technology/approach it uses (one sentence)
- How it will be delivered/deployed (one sentence)
- External collaborations if any
- **Max ~150 words**

#### Key Requirements Section
- Bullet list format
- Each requirement is 1-2 sentences
- Include both functional and non-functional requirements
- Note which are assumptions vs. confirmed requirements
- **Source:** Primarily from hackathon doc + customer refinements

#### Architecture Section
- Brief text description (1-2 sentences)
- Architecture diagram (generated via Graphviz)
- Can have "Initial" and "Updated" sub-sections if architecture evolved
- **Source:** Architecture discussions from hackathon + customer feedback

#### Sprint Plan Overview Section
- High-level bullet list
- One bullet per sprint with a brief goal
- **Format:** `Sprint N: [Goal description]`
- This is the "what was communicated to the client" summary

#### Timeline & Design Table Section
- **This is the core deliverable** — must be the most detailed section
- Markdown table with columns: Sprint/Phase | Timeline (CW) | Goal | Epics
- Each sprint row has detailed epics with sub-items
- Use calendar weeks (CW) for timeline when available
- Include status markers like `→ Done`, `→ WIP` if provided in source
- **Effort column** is optional (include if client effort data is available)

#### Design Decisions Section (Optional)
- Key technical decisions with brief rationale
- Only include if design decisions were discussed in source material

#### Effort Estimation Section (Optional)
- Breakdown of client-side effort per sprint
- Differentiate between IT team and application/business team
- Only include if effort data was discussed

### Tone & Voice
- Professional, partnership-focused, results-oriented
- First person plural ("we") when describing joint work
- Confident but not arrogant
- Technical precision without jargon overload
- Use client's exact domain terminology

### Evidence-Based Writing
- Every claim traces to hackathon document or customer conversation
- Use exact terminology from source material
- Never invent metrics, KPIs, or performance numbers
- Never add features or sprints not discussed in source
- Never assume timelines unless explicitly discussed

---

## Anti-Hallucination Rules (Critical)

Read the full rules at `references/anti-hallucination-rules.md`. Key rules for design plans:

1. **Sprint durations:** ONLY use durations explicitly discussed. Don't assume 2-week sprints.
2. **Calendar weeks:** ONLY use specific CW numbers if provided. Otherwise use relative timing.
3. **Effort estimates:** ONLY include if mentioned in source. Don't invent person-day estimates.
4. **Architecture components:** ONLY include components mentioned in hackathon or discussions.
5. **Technology choices:** Use exact technology names from source (e.g., "Firestore" not "NoSQL database").
6. **Feature names:** Preserve exact terminology — don't rename or rebrand features.
7. **Status markers:** Only mark items as "Done" if explicitly confirmed in source.
8. **Client names and roles:** Use exact names from source. Don't invent stakeholder roles.
9. **Dependencies:** Only list dependencies mentioned in source.
10. **Timeline conflicts:** If hackathon and customer say different things, flag BOTH — don't pick one.

**Decision tree for uncertain content:**
```
I want to include [claim/timeline/component] because [reason]

Is it in the hackathon doc?
├─ YES → Include with source reference
└─ NO  → Is it in customer conversation?
    ├─ YES → Include with source reference
    └─ NO  → Is it in Confluence (found via smart lookup)?
        ├─ YES → Include with Confluence source reference
        └─ NO  → Does the client need to decide?
            ├─ YES → Include as [To be confirmed]
            └─ NO  → DO NOT INCLUDE
```

---

## File Paths (Relative to Skill Directory)

```
sprint-design/
├── assets/                                # Shared assets
├── scripts/
│   └── generate_architecture_diagram.py   # Graphviz diagram generator (same as scope skill)
├── references/
│   ├── anti-hallucination-rules.md        # Anti-hallucination rules
│   └── design-plan-structure.md           # Structure templates from real examples
└── SKILL.md                               # This file
```

**Shared with scope-document-generator:**
- `generate_architecture_diagram.py` — Same script, same JSON format, same rendering pipeline
- `anti-hallucination-rules.md` — Same rules apply to design plans

---

## Example: Minimal Design Plan

For a project called "ACME Produktberater" in space "AC":

```markdown
## Overview

**ACME Produktberater** is an AI-based product advisor that provides accurate furniture
recommendations based on user requirements (age, room type, space, usage). The project
leverages Large Language Models for recommendation generation and integrates with ACME's
PXM and SAP data systems.

The backend provides REST APIs to the ACME Pro website for features such as product search,
recommendation generation, and conversation history. The system is hosted on Azure within
ACME's subscription.

## Key Requirements

- Develop an AI-based product advisor with accurate recommendations based on user input
- Support at least 10 reference room types, extendable in the future
- Establish recommendation rules that influence the LLM's behavior
- Build chat interface and API endpoints for website integration
- Ensure integration with PXM, SAP data systems and Azure environment

## Architecture

The following diagram shows the initial architecture based on hackathon conversations
and project design discussions.

[Architecture diagram image]

## Sprint Plan Overview

- **Sprint 1:** Knowledge Foundation & First Prototype
- **Sprint 2:** Enhanced Recommendation & Website Integration
- **Sprint 3:** Production Readiness & Final Testing

## Timeline & Design

| Sprint / Phase | Timeline | Goal | Epics (High-Level Features) |
|---|---|---|---|
| **Sprint 1** | CW 41–42 | Knowledge foundation + first prototype | **Data:** Connect to PXM/SAP; ingest reference rooms and catalog. **AI:** Basic recommendation prototype. **Integration:** Chat API skeleton + UI mockup. |
| **Sprint 2** | CW 43–44 | Enhanced recommendation + website integration | **AI:** Develop recommendation rules. **Integration:** Web integration with HABA Pro developer team. **Testing:** Internal user tests for 10 room types. |
| **Sprint 3** | CW 45–46 | Production readiness | **Data:** Final data sync with PXM/SAP. **AI:** Optimize recommendation precision. **Testing:** End-to-end UAT; load/performance checks. |
```

---

## Reference Examples in Confluence

This skill's structure is derived from analysis of these real One Thousand design plan pages. Use them as the gold standard for formatting and content depth:

1. **MICUBO - Design Plan** (Yellow Satellite space)
   - URL: `https://leadmachinelearning.atlassian.net/wiki/spaces/YS/pages/1085309264/MICUBO+-+Design+plan`
   - Page ID: `1085309264`
   - **Characteristics:** Most detailed example. Has Overview, Initial + Updated Architecture, Sprint Plan Overview (original + updated), detailed Timeline & Design table with epics and status markers, Design Decisions section.

2. **Project Design Plan** (Blue Homes space)
   - URL: `https://leadmachinelearning.atlassian.net/wiki/spaces/BH/pages/776896513/Project+Design+Plan`
   - Page ID: `776896513`
   - **Characteristics:** Includes Key Requirements with assumption notes, Architecture with notes, Timeline & Design table with client effort estimation column, separate Effort Estimation section grouped by sprint and team.

3. **Project Design Plan** (Colorful-Toys Produktberater space)
   - URL: `https://leadmachinelearning.atlassian.net/wiki/spaces/CH/pages/1444479015/Project+design+plan`
   - Page ID: `1444479015`
   - **Characteristics:** Most concise example. Key Requirements, Notes & Dependencies, Architecture, Timeline & Sprints table. Good model for smaller/simpler projects.

**When generating new design plans**, the level of detail should scale with project complexity:
- **Simple projects (3 sprints):** Follow Colorful-Toys pattern
- **Medium projects (5-6 sprints):** Follow Blue Homes pattern
- **Complex projects (7+ sprints):** Follow MICUBO pattern

---

## Language Support

### English (Default)
All section headings, templates, and examples in this skill are in English.

### German
When generating German design plans:
- Use German section headings: "Überblick", "Kernanforderungen", "Architektur", "Sprint-Übersicht", "Zeitplan & Design", "Designentscheidungen", "Aufwandsschätzung"
- Use `[Noch zu bestätigen]` instead of `[To be confirmed]`
- Preserve client's domain terminology in original language (do NOT translate domain terms)
- For mixed teams, section headings can remain in English while content is in German — ask user preference
- Anti-hallucination markers: see `references/anti-hallucination-rules.md` language section
