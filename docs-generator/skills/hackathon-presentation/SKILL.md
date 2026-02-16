---
name: hackathon-presentation
description: "Generate One Thousand branded hackathon presentation decks (.pptx) from sales context, Confluence pages, Miro boards, and project briefs. Triggers on: 'hackathon presentation', 'hackathon deck', 'hackathon slides', 'hackathon pptx', 'create presentation for hackathon', 'generate hackathon slides', 'presentation for [client]', 'hackathon pitch deck'. Transforms sales context emails, Slack messages, Confluence pages, Miro boards, and Close CRM data into professional 2-day hackathon presentations with branded OT slide layouts, client-specific use case content, and image placeholders for the user to fill in. Includes rich input collection, multi-source enrichment, confidence scoring with iterative review, and visual QA via soffice + pdftoppm inspection. Use this skill whenever someone mentions creating or generating a hackathon presentation or slides."
---

# Hackathon Presentation Generator

Generates professional One Thousand branded hackathon presentation decks from sales context, project briefs, Confluence documentation, Miro boards, and hackathon summaries. Includes multi-source enrichment, anti-hallucination validation, confidence scoring with iterative review, and visual QA inspection.

The presentation follows OT's standard 2-day hackathon format with three content blocks:
1. **Day 1 Pre-Intro** — Cover, Check-in, Agenda (before the generic AI education section)
2. **Use Case Section** — Pain, Data, Approach, Challenges, System Landscape (client-specific, after AI intro)
3. **Day 2 Results** — Cover, Team photos, Business value, PoC summary, Demo, Key Metrics, Lessons Learned, Next steps, Thanks

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

5. **System Landscape** (if known):
   - Primary ERP system (SAP, Oracle, NetSuite, etc.) or "Unknown"
   - CRM system (Salesforce, Dynamics, Pipedrive, etc.) or "Unknown"
   - Cloud infrastructure (AWS, Azure, GCP) or "Unknown"
   - Key APIs or data sources
   - Any tech stack notes relevant to the PoC

6. **Team & Stakeholders**:
   - OT team members who will be named in the presentation
   - Key client contacts / stakeholders
   - Any roles to highlight (e.g., "Product Manager", "Data Architect")

7. **Hackathon Goals & Success Criteria** (optional but valuable):
   - What does success look like? (e.g., "Prove we can automate 80% of quotations")
   - Any specific metrics or KPIs?
   - Expected business impact (time savings, cost reduction, FTE capacity, etc.)

8. **Branding Notes** (optional):
   - Client's primary brand colors (hex codes if available)
   - Font preferences or accessibility constraints
   - Logo placement preferences
   - Any styling guidelines

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
- Client name, location, dates ✓
- Use case title ✓
- At least one source of information ✓

If critical pieces are missing, ask for them. **Never invent missing details.**

---

## Phase 2: Source Enrichment & Data Gathering

### Step 2.1 — Search Confluence for client documentation

If the user provided Confluence URLs or space names, search for:
- **Hackathon planning pages** (look for "Hackathon {ClientName}", "2-day discovery", etc.)
- **Technical documentation** (system landscape, data sources, API docs, ERPs)
- **Scope documents** or discovery debrief documents
- **Client background** pages (industry context, company profile, strategic goals)

**MCP Tool**: Use `sharepoint_search` to find:
- File names containing the client name + "hackathon"
- Pages containing "system landscape", "ERP", "CRM", "API"
- Technical architecture or integration docs

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

Use `outlook_email_search` or `mcp__11679210-8cb4-4219-9fe0-7b8f107a576b__chat_message_search` to find:
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
- Em-dash patterns for challenges/approach (Bold title — description)

### Step 3.3 — Extract and structure content from all sources

Create a consolidated **Content Extraction Document** with:

| Category | Source | Extracted Details | Confidence |
|----------|--------|-------------------|------------|
| **Client & Project** | Confluence + CRM | Company name, size, industry, HQ, strategic goals | High/Med/Low |
| **Pain Points** | Email + Confluence + user input | Specific problems, manual processes, metrics | High/Med/Low |
| **Data Sources** | Miro + Confluence tech docs | Systems, APIs, databases, data formats, volume | High/Med/Low |
| **System Landscape** | Confluence tech docs | ERP, CRM, cloud infra, APIs, integrations | High/Med/Low |
| **Approach** | Miro AI canvas + scope doc | PoC capabilities, steps, features | High/Med/Low |
| **Challenges** | Miro + Confluence + Email | Data quality, integration, adoption, technical blockers | High/Med/Low |
| **Business Value** | Confluence planning + Email | Time savings, FTE freed, revenue impact, strategic benefits | High/Med/Low |
| **Team** | Close CRM + Email | OT team members, client stakeholders, roles | High/Med/Low |
| **Hackathon Goals** | Confluence + Email | Success criteria, expected metrics, go-live plans | High/Med/Low |

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
  "industry": "Manufacturing",
  "company_size": "Enterprise",
  "location": "City, Country",
  "hackathon_dates": {
    "day1": "DD.MM.YYYY",
    "day2": "DD.MM.YYYY"
  },
  "use_case_title": "Short Use Case Name",
  "presentation_title": "Strengthening {client_name} With AI",
  "language": "en",
  "team_members": {
    "ot_team": ["Name1 (Role)", "Name2 (Role)"],
    "client_contacts": ["Name1 (Title)", "Name2 (Title)"]
  },
  "hackathon_goals": [
    "Prove we can automate 80% of quotations",
    "Achieve <1 minute processing time per quote"
  ],
  "branding_notes": {
    "primary_color": "#18A05A or client color",
    "logo_style": "full logo on cover, icon elsewhere"
  }
}
```

### Step 4.2 — Generate content.json with enhanced schema

Create the content file with ALL slide text:

```json
{
  "check_in": {
    "questions": [
      "Who am I?",
      "What comes to my mind when I think of {client_name} and AI?",
      "When is this AI Hackathon a success?"
    ]
  },
  "agenda": {
    "day1": [
      {"time": "09:00", "activity": "Opening & Discovery"},
      {"time": "10:00", "activity": "Deep Dive: {use_case_title}"},
      {"time": "12:00", "activity": "Lunch"},
      {"time": "13:00", "activity": "Building the PoC"},
      {"time": "17:00", "activity": "Day 1 Retrospective"}
    ],
    "day2": [
      {"time": "09:00", "activity": "Day 2 Stand-up"},
      {"time": "10:00", "activity": "PoC Refinement & Testing"},
      {"time": "12:00", "activity": "Lunch"},
      {"time": "13:00", "activity": "Final Demo Preparation"},
      {"time": "14:00", "activity": "Presentation to Stakeholders"}
    ]
  },
  "use_case": {
    "pain_points": [
      "Pain point 1 — specific, with metric or quote from source",
      "Pain point 2 — quantified impact (time, cost, error rate)",
      "Pain point 3 — current bottleneck or manual process",
      "Pain point 4 — strategic or competitive disadvantage",
      "Pain point 5 — adoption or scaling constraint"
    ],
    "data_sources": [
      {
        "icon": "📧",
        "title": "Data Category (e.g., Incoming Quotation Requests)",
        "description": "Specific description: source system, format (email, API, document), volume, key fields"
      },
      {
        "icon": "💾",
        "title": "Another Data Source",
        "description": "System name, data format, approximate records/day, relevant schema"
      }
    ],
    "system_landscape": {
      "erp": "SAP S/4HANA (or actual system name, or '[To be confirmed]')",
      "crm": "Salesforce Sales Cloud",
      "cloud_infra": "AWS (EC2, Lambda, RDS)",
      "key_apis": [
        "SAP OData API for quotation master data",
        "Salesforce REST API for opportunities",
        "Custom REST API for document processing"
      ],
      "integrations": "Real-time sync via middleware; batch ingestion for historical data",
      "constraints_or_notes": "Legacy mainframe attachment; real-time sync required for <1min turnaround"
    },
    "approach_steps": [
      "Step 1: Ingest quotation requests — parse email, extract key fields (product, quantity, customer)",
      "Step 2: Enrich data — lookup customer info from CRM, product master from ERP",
      "Step 3: Generate pricing — apply rules engine + AI for market-based adjustments",
      "Step 4: Validate & deliver — quality check, format response, send via email + CRM"
    ],
    "approach_question": "Optional: How would we handle edge cases (new products, special pricing)?",
    "challenges": [
      "Challenge 1 — Data quality issue: email subjects lack structured product codes [To be confirmed: error rate?]",
      "Challenge 2 — Integration complexity: SAP API has slow response times during peak hours",
      "Challenge 3 — Adoption risk: sales team may distrust AI pricing without audit trail",
      "Challenge 4 — Regulatory: pricing must comply with regional discount policies",
      "Challenge 5 — Scalability: current design tested with ~100 quotations/day; need to scale to 500+"
    ]
  },
  "results": {
    "business_value": [
      {
        "number": "01",
        "title": "Time Savings",
        "description": "Reduces quotation creation time from 15 minutes to 2 minutes per request; frees ~30 FTE hours per week"
      },
      {
        "number": "02",
        "title": "Accuracy & Compliance",
        "description": "AI-generated quotes align with regional policies 100% of the time; eliminates discount overrides and compliance violations"
      },
      {
        "number": "03",
        "title": "Faster Go-to-Market",
        "description": "Average quotation turnaround drops from 2-3 days to <1 hour; enables faster sales cycles and competitive response"
      }
    ],
    "poc_summary": {
      "intro": "We have built a proof of concept (PoC) that enables us to:",
      "features": [
        "Parse and extract quotation requests from multiple email formats",
        "Enrich request context using live CRM and ERP lookups",
        "Generate AI-backed pricing with explainability audit trail",
        "Route quotes through approval workflow with 1-click sign-off"
      ],
      "demo_description": "Live walkthrough: watch as an incoming customer email is transformed into a formatted quote ready for send in under 90 seconds. See how the AI explains its pricing logic."
    },
    "key_metrics": {
      "poc_scope": "Tested with 50 historical quotations; 44/50 generated without manual rework (88% first-pass accuracy)",
      "timeline_to_live": "Phase 1 (validation & refinement): 4 weeks; Phase 2 (production integration): 6 weeks; Phase 3 (rollout to sales): 2 weeks",
      "estimated_roi": "Annual FTE savings: ~1,200 hours @ $75/hr = $90k/year; payback period: 4-6 months post-go-live"
    },
    "lessons_learned": [
      "Email parsing is harder than expected — SAP OData queries return stale pricing data during peak load hours",
      "Sales team engagement early is critical — showed draft UI to 3 sales managers, got valuable feedback on approval workflow",
      "Regulatory review should happen in parallel, not after development — discount policy conflicts discovered late"
    ],
    "next_steps": [
      "Publish hackathon debrief document summarizing PoC scope, test results, and refinement roadmap",
      "Schedule Phase 1 kickoff meeting with {client_name} technical team (target: 2 weeks post-hackathon)",
      "Refine data quality rules based on test results; establish SLA for quote turnaround (target: <60 minutes)",
      "Define governance: who approves AI pricing? escalation policy for edge cases?"
    ]
  },
  "confidence_scores": {
    "pain_points": {
      "score": 85,
      "source_grounding": 18,
      "specificity": 17,
      "completeness": 18,
      "actionability": 18,
      "anti_hallucination": 18,
      "threshold": 75,
      "status": "PASS"
    },
    "data_sources": {
      "score": 72,
      "source_grounding": 16,
      "specificity": 15,
      "completeness": 14,
      "actionability": 16,
      "anti_hallucination": 17,
      "threshold": 70,
      "status": "BORDERLINE — ask user to confirm data formats and volume"
    },
    "approach": {
      "score": 78,
      "source_grounding": 16,
      "specificity": 17,
      "completeness": 16,
      "actionability": 17,
      "anti_hallucination": 16,
      "threshold": 75,
      "status": "PASS"
    },
    "challenges": {
      "score": 68,
      "source_grounding": 14,
      "specificity": 14,
      "completeness": 13,
      "actionability": 14,
      "anti_hallucination": 13,
      "threshold": 65,
      "status": "BORDERLINE — ask user about data quality error rates and SAP integration details"
    },
    "business_value": {
      "score": 74,
      "source_grounding": 15,
      "specificity": 16,
      "completeness": 15,
      "actionability": 16,
      "anti_hallucination": 16,
      "threshold": 70,
      "status": "PASS"
    },
    "poc_summary": {
      "score": 82,
      "source_grounding": 17,
      "specificity": 17,
      "completeness": 16,
      "actionability": 17,
      "anti_hallucination": 18,
      "threshold": 60,
      "status": "PASS"
    },
    "next_steps": {
      "score": 75,
      "source_grounding": 15,
      "specificity": 15,
      "completeness": 15,
      "actionability": 17,
      "anti_hallucination": 16,
      "threshold": 55,
      "status": "PASS"
    }
  }
}
```

### Step 4.3 — Confidence Scoring Process

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

**Section-Specific Minimum Thresholds** (lower than scope docs since presentations are less detailed):

| Section | Minimum Threshold |
|---------|-------------------|
| Pain Points | 75 |
| Data Sources | 70 |
| Approach | 75 |
| Challenges | 65 |
| Business Value | 70 |
| PoC Summary | 60 |
| Next Steps | 55 |

### Step 4.4 — Iterative Review Loop

**After scoring all sections:**

1. **Create a summary table** showing all scores:
   ```
   ┌─────────────────┬───────┬───────────┬────────────┐
   │ Section         │ Score │ Threshold │ Status     │
   ├─────────────────┼───────┼───────────┼────────────┤
   │ Pain Points     │  85   │    75     │ ✓ PASS     │
   │ Data Sources    │  72   │    70     │ ⚠ BORDER   │
   │ Approach        │  78   │    75     │ ✓ PASS     │
   │ Challenges      │  68   │    65     │ ⚠ BORDER   │
   │ Business Value  │  74   │    70     │ ⚠ BORDER   │
   │ PoC Summary     │  82   │    60     │ ✓ PASS     │
   │ Next Steps      │  75   │    55     │ ✓ PASS     │
   └─────────────────┴───────┴───────────┴────────────┘
   ```

2. **For each FAILING or BORDERLINE section**, ask the user specific questions:

   **Example for Data Sources (score 72):**
   > "Data Sources scored 72/100 (just above threshold of 70). The content is mostly specific, but we're missing details on data volumes and integration formats.
   >
   > Can you clarify:
   > 1. How many quotation requests arrive per day? (you said '~200', but need to confirm actual range)
   > 2. What format are they in? (email body, attachment, API call, all three?)
   > 3. Do quotation details come from CRM, ERP, or a separate system?"

3. **Regenerate failing sections** with the new information

4. **Re-score** regenerated sections

5. **Repeat until**:
   - All sections pass their thresholds, OR
   - User says "proceed anyway" (sections marked with `[To be confirmed]`)

### Step 4.5 — Final content.json validation

Before generating the PPTX:
- Confirm no invented metrics or feature names
- Ensure all `[To be confirmed]` markers are documented
- Verify word counts stay within budgets (see Content Constraints section below)
- Check parallel structure in bullet points (e.g., all challenges start with the same grammatical structure)

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

The script creates slides from OT's branded template layouts:

| Slide | Layout | Content |
|-------|--------|---------|
| Cover (Day 1) | Cover Lime + Logo | Client name, location, date, use case |
| Check-in | Bullet Points Ash | 3 interactive questions with speaker notes |
| Agenda | Dayline Lime | Customizable 2-day schedule from content.json |
| Table of Contents | Table of Contents large | Pain / Data / Approach / Challenges |
| Pain (01) | Chapter Divider Ash + Text | Pain point bullets with metrics |
| Data (02) | Chapter Divider Ash + Text | Data source descriptions with icons |
| Data Screenshots | Title Ash + Image | `[IMAGE placeholder]` for sample data |
| System Landscape | DEFAULT (card layout) | ERP, CRM, cloud infra, APIs, integrations |
| Approach (03) | Chapter Divider Ash + Text | Step-by-step approach bullets |
| Challenges (04) | Chapter Divider Ash + Text | Challenge descriptions (em-dash pattern) |
| Breakthrough! | Chapter Divider Lime | Motivational call-to-action |
| Cover (Day 2) | Cover Lime + Logo | Day 2 date, results title |
| Team Photos | DEFAULT | `[IMAGE placeholder]` for team |
| What we've done | Chapter Divider Lime | Section divider with speaker notes |
| Process Flow | DEFAULT | `[IMAGE placeholder]` for whiteboard/Miro flow |
| Architecture | DEFAULT | `[IMAGE placeholder]` for system architecture |
| Business Value | Table of Contents small | 3 numbered outcomes with metrics |
| Key Metrics | DEFAULT | PoC test results, timeline to live, estimated ROI |
| PoC Summary | DEFAULT | Feature list + demo description |
| DEMO | Chapter Divider Lime | Section divider with demo walkthrough notes |
| Demo Walkthrough | DEFAULT | `[IMAGE placeholder]` or video embed |
| Expectations Check | Chapter Divider Lime | Section divider with reflection prompt |
| Lessons Learned | DEFAULT | Key insights from the hackathon |
| What's Next | Chapter Divider Ash + Text | Phased roadmap and next-step actions |
| Thanks | Bullet Points Ash | Team names, roles, logos |

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
            text_preview = shape.text[:50].replace('\n', ' ')
            if text_preview.strip():
                print(f'  > {text_preview}...')
"
```

### Step 5.4 — Create image placeholder inventory

List all placeholders the user must fill:

**Before the Hackathon (Day 1):**
- Slide 1: Client logo (recommend 1200×400px)
- Slide 7 (Data Screenshots): 2-3 sample data files, emails, or screenshots

**After the Hackathon (Day 2):**
- Slide 12: Team photos from Day 1 (recommend group photo 1920×1080px)
- Slide 14: Process flow diagram (from whiteboard photo, Miro, or Lucidchart export)
- Slide 15: Architecture diagram (system landscape, API flows, integrations)
- Slide 21 (Demo): Demo screenshot or embedded video link
- Slide 24: Lessons learned visuals (optional: team retro board photo)
- Slide 25: Team photos and client logos for thanks slide

---

## Phase 6: Visual QA & Inspection

### Step 6.1 — Convert PPTX to PDF and inspect visually

Run the soffice conversion and PDF-to-image pipeline:

```bash
# Convert PPTX to PDF
python /sessions/trusting-optimistic-thompson/mnt/.skills/skills/pptx/scripts/office/soffice.py \
  --headless \
  --convert-to pdf \
  {client_name}_Hackathon_Presentation.pptx

# Convert PDF to JPEG images (150 DPI for readable inspection)
pdftoppm -jpeg -r 150 {client_name}_Hackathon_Presentation.pdf slide

# Output: slide-1.jpg, slide-2.jpg, ... slide-N.jpg
```

### Step 6.2 — Visual inspection checklist

For each generated slide, verify:

1. **Layout integrity**:
   - Text is not cut off at slide edges
   - Placeholder boxes are clearly labeled `[IMAGE: ...]`
   - Font sizes are readable (body text ≥20pt, headers ≥32pt)

2. **Content accuracy**:
   - No `[To be confirmed]` markers remain (unless explicitly approved)
   - Client name is consistent throughout
   - Dates, numbers, and metrics are correct

3. **Brand compliance**:
   - OT green (#18A05A) used on cover and dividers
   - Footer shows "© 2019-2026 ONE THOUSAND" + slide number
   - 16:9 widescreen aspect ratio maintained

4. **Readability**:
   - Bullet points have appropriate line breaks (max 2 lines per bullet)
   - Headers max 6 words
   - No orphaned text (single word on a line)

5. **Consistency**:
   - Parallel bullet structure (e.g., all challenges use em-dash pattern)
   - Power verbs and active voice throughout
   - Client terminology used consistently

### Step 6.3 — Fix issues found during QA

If visual inspection finds problems:

1. **Layout issues** (text cut off, misaligned): Adjust `--fontsize` or re-run generator with shorter content
2. **Content errors**: Update `content.json`, re-run generator, re-inspect
3. **Brand/formatting**: Verify template file and regenerate

Re-run soffice conversion after each fix to re-inspect.

### Step 6.4 — Generate final QA report

Document findings:

```
Visual QA Report: {client_name}_Hackathon_Presentation.pptx
Generated: {timestamp}

✓ Passed Checks:
  - All 25 slides render correctly
  - Text is readable (font sizes 20pt+)
  - OT branding consistent (green covers, ash dividers, white body)
  - No text cut-off detected
  - Placeholder images clearly labeled

⚠ Warnings:
  - Slide 5 (Challenges): line break needed on bullet 3 (currently 3 lines)
  - Slide 12: placeholder "[IMAGE: Team Photos]" needs 1920×1080px team photo
  - Slide 19: "Key Metrics" slide uses smaller font (18pt); ensure readability on projector

Status: READY FOR DELIVERY
```

---

## Phase 7: Delivery

### Step 7.1 — Prepare delivery package

1. **PPTX file**: `{ClientName}_Hackathon_Presentation.pptx` (ready to use)
2. **Image placeholder inventory** (CSV or list):
   ```
   Slide | Placeholder | Recommended Size | Notes
   1     | Client Logo | 1200×400         | Place on cover
   7     | Data Example 1 | 1024×768      | Email or system screenshot
   12    | Team Photo  | 1920×1080        | Group photo from Day 1
   14    | Process Flow | 1400×900        | Miro board or whiteboard
   ...
   ```
3. **Confidence scores document** (if any borderline or `[To be confirmed]` items)
4. **Visual QA report**

### Step 7.2 — AI intro section instruction

Provide the user with this critical note:

> **IMPORTANT: How to Complete Your Hackathon Deck**
>
> The generated presentation contains your **client-specific slides only** (Pain, Data, Approach, Challenges, System Landscape, Business Value, Results, Next Steps, etc.).
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
> - Copy slides 5-54 (the AI intro slides) from the master deck
> - Paste them into your generated deck after Slide 4 (Agenda)
> - Update the Table of Contents slide numbers if needed
> - Save as final version

### Step 7.3 — Final handoff to user

1. Display the confidence scores table
2. List any `[To be confirmed]` items that need follow-up post-hackathon
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
| Pain points | 100 | 5-6 | Include metrics where possible |
| Data sources | 80 | 3-4 | Describe system + format + volume |
| System landscape | 120 | Variable | Structured as ERP/CRM/Cloud/APIs |
| Approach steps | 80 | 4-5 | Sequential numbered steps |
| Challenges | 120 | 4-5 | Em-dash pattern (Bold — description) |
| Business value | 90 | 3 items | Numbered outcomes with metrics |
| PoC summary | 60 | 4-6 | Feature list; simple, concrete |
| Key metrics | 100 | 3-5 | Test results, timeline, ROI |
| Lessons learned | 100 | 3-5 | Retrospective insights |
| Next steps | 60 | 3-4 | Actionable, phased roadmap |
| Thanks | 30 | Team names + roles | Names, roles, logos |

### Style & Tone Guidelines

1. **Concise and impactful** — presentation slides, not a detailed report
2. **Active voice** — "Parse incoming quotations" not "Incoming quotations are parsed"
3. **Specific over generic** — "~200 quotations per day" not "many quotations"; "SAP S/4HANA" not "ERP"
4. **Client vocabulary** — use their terminology (SP numbers, not "product codes"; "Material Master", not "product database")
5. **No filler words** — every word must earn its place on the slide
6. **Power verbs** — Transform, Automate, Accelerate, Unlock, Drive, Enable, Streamline (not: "help", "improve", "do")
7. **Parallel structure** — if using em-dash pattern for challenges, apply it consistently to all challenges
8. **Em-dash pattern** (for challenges and complex points):
   ```
   Bold Title — one-line description explaining the challenge or approach
   ```
   Example:
   ```
   Data Quality Issues — email subjects lack standardized product codes; 40% require manual correction
   Legacy System Integration — SAP OData API has 5-second query latency during peak load
   Adoption Risk — sales team may distrust AI-generated pricing without transparent audit trail
   ```

### Avoiding Hallucination

**RED FLAGS — Never write these without source material:**

- Client company metrics not mentioned in source docs (e.g., "annual revenue of $500M" — ask for confirmation)
- Specific feature names not agreed upon during discovery (e.g., "QuoteGPT" without user saying so)
- Technical specifications not confirmed (e.g., "processing 1000 quotations/minute" — verify with data sources)
- Timeline claims not backed by project scope (e.g., "go-live in 3 months" — ask the user)
- ROI numbers without clear calculation (e.g., "save $2M annually" — show the math)
- Regulatory or compliance claims without documentation (e.g., "GDPR-compliant by design" — verify)

**When in doubt**: Use `[To be confirmed]` marker and ask the user for confirmation before finalizing.

---

## Brand Guidelines

- **Cover color**: `#18A05A` (OT Sharp Green)
- **Dark/Ash background**: `#323232` (for chapter dividers and text backgrounds)
- **Body text**: Dark ash text on white background
- **Accent colors**: OT lime for Day 1/opening, ash for use case, lime for results/breakthrough
- **Footer**: "© 2019-2026 ONE THOUSAND" + slide number (white on dark background)
- **Format**: Widescreen 16:9 (13.333" × 7.5")
- **Template**: One Thousand branded layouts with green/ash/white color scheme
- **Logo placement**: Client logo on cover (right side, 1200×400px); OT logo on thanks slide

---

## Content Constraints & Validation

### Before generating content.json

1. **Source traceability**: Every fact must trace to an extracted source (Confluence, Miro, Email, CRM, user input)
2. **No invented details**: If a detail is missing, mark it `[To be confirmed]`; ask the user rather than guessing
3. **Metric verification**: All numbers (time savings, accuracy rates, costs) must come from source material or be explicitly marked as estimates
4. **Team name accuracy**: Verify all team member names against CRM or email; spell correctly
5. **Dates and timelines**: Confirm hackathon dates, project timelines, and go-live estimates with the user

### After generating content.json

1. **Confidence scoring**: Run all seven dimensions; ensure all sections meet or exceed thresholds
2. **Word count check**: Verify each section stays within budgets
3. **Parallel structure**: All bullet points in a list should use the same grammatical form
4. **No jargon without explanation**: Client-specific acronyms should be spelled out on first mention
5. **Visual mockup**: Ask user to review `content.json` before running the PPTX generator

---

## Dependencies & Setup

### Python packages

```bash
pip install python-pptx --break-system-packages
pip install markitdown --break-system-packages
pip install pdf2image --break-system-packages
```

### External tools

- **soffice** (LibreOffice): For headless PPTX→PDF conversion
  ```bash
  sudo apt-get install libreoffice
  ```
- **pdftoppm** (Poppler): For PDF→JPEG conversion for visual inspection
  ```bash
  sudo apt-get install poppler-utils
  ```

### Template files

- **OT Hackathon template**: `assets/templates/ot-hackathon-template.pptx`
- **OT Master hackathon deck** (for AI intro slides): `assets/templates/ot-master-hackathon.pptx`
- **Section templates** (writing guidance): `references/section-templates-en.md` or `references/section-templates-de.md`
- **Slide structure guide**: `references/slide-structure-guide.md`
- **Anti-hallucination rules**: `references/anti-hallucination-rules.md`

### MCP tools required

- `sharepoint_search` — Search Confluence for client documentation
- `context_explore` — Explore Miro board structure
- `context_get` — Extract content from Miro documents/diagrams
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
- "presentation for {client} hackathon"
- Similar variations

---

## Troubleshooting

**Issue**: PPTX generator fails with "template file not found"
**Solution**: Verify `assets/templates/ot-hackathon-template.pptx` exists and is readable

**Issue**: Slides are missing content after regeneration
**Solution**: Check that `content.json` is valid JSON; run `python -m json.tool content.json` to validate

**Issue**: `[To be confirmed]` markers remain after final review
**Solution**: This is expected for items the user approved; document them in the delivery handoff

**Issue**: Placeholder images don't show in visual QA
**Solution**: Placeholders are gray boxes with text labels; they are intentional (user will add images)

**Issue**: Font sizes too small or text cut off
**Solution**: Reduce word count per bullet or increase font size in generator script parameters

**Issue**: pdftoppm fails to convert PDF
**Solution**: Verify Poppler is installed; check PDF file is not corrupted by running `pdfinfo {filename}.pdf`

---

## Example Workflow

### User Input

> "Generate a hackathon presentation for Acme Manufacturing. They're in automotive parts production, based in Stuttgart. Hackathon is Jan 18-19, 2024. Use case is automating quotation creation. Here's the Confluence space: https://confluence.acme.com/display/HACKATHONS/2024-Q1-Automotive"

### Skill Workflow

1. **Phase 1** — Ask for branding notes, team names, hackathon goals, system landscape (SAP? cloud?)
2. **Phase 2** — Search Confluence space for planning docs; extract pain points, data sources, tech stack
3. **Phase 3** — Create Content Extraction Document; identify gaps (e.g., "Need to confirm email volume")
4. **Phase 4** — Generate variables.json and content.json; score each section
5. **Phase 5** — Run `generate_hackathon_pptx.py`; generate the PPTX
6. **Phase 6** — Convert to PDF and JPEG; visually inspect all slides
7. **Phase 7** — Deliver PPTX + image placeholder list + confidence scores + instructions for AI intro insertion

### Handoff to User

```
✓ Presentation generated: Acme_Manufacturing_Hackathon_Presentation.pptx (25 slides)

Confidence Scores:
┌──────────────────┬────┬────────────┬─────────┐
│ Section          │ Sc │ Threshold  │ Status  │
├──────────────────┼────┼────────────┼─────────┤
│ Pain Points      │ 82 │ 75         │ ✓ PASS  │
│ Data Sources     │ 76 │ 70         │ ✓ PASS  │
│ Approach         │ 80 │ 75         │ ✓ PASS  │
│ Challenges       │ 71 │ 65         │ ✓ PASS  │
│ Business Value   │ 75 │ 70         │ ✓ PASS  │
│ PoC Summary      │ 81 │ 60         │ ✓ PASS  │
│ Next Steps       │ 73 │ 55         │ ✓ PASS  │
└──────────────────┴────┴────────────┴─────────┘

Image Placeholders to Add (8 total):
- Slide 1: Client logo (1200×400px)
- Slide 7: 2× data screenshots (1024×768px each)
- Slide 12: Team photo from Day 1 (1920×1080px)
- Slide 14: Process flow diagram
- Slide 15: System architecture diagram
- Slide 21: Demo walkthrough screenshot
- Slide 25: Team + client logos

Next: Insert OT's AI intro slides (50 slides) between Slide 4 and Slide 5, then add images above.

Ready to download!
```

