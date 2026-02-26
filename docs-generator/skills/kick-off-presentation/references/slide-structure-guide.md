# Slide Structure Guide

This document maps each slide in the kick-off presentation to its template layout and describes exactly what content goes where.

## Presentation Structure Overview

The kick-off presentation follows a fixed 6-section structure with ~20 slides. All sections are connected by agenda divider slides that highlight the active section in the table of contents.

```
[Section 0: Cover]
  Slide 0: Cover

[Section 1: Check In]
  Slide 1: Full Agenda (ToC)
  Slide 2: Agenda Divider 01 (Check In highlighted)
  Slide 3: Check-In

[Section 2: Use-Case]
  Slide 4: Agenda Divider 02 (Use-Case highlighted)
  Slide 5: Pain x Data
  Slide 6: Hackathon Validation
  Slide 7: Step by Step
  Slide 8: Architecture

[Section 3: Timeline]
  Slide 9: Agenda Divider 03 (Timeline highlighted)
  Slide 10: Sprint Goals
  Slide 11: Timeline / Gantt
  Slide 12: Progress / Risks

[Section 4: Collaboration]
  Slide 13: Agenda Divider 04 (Collaboration highlighted)
  Slide 14: Participants
  Slide 15: Meetings

[Section 5: Other Topics]
  Slide 16: Agenda Divider 05 (Other Topics highlighted)
  Slide 17: Discussion

[Section 6: Check Out]
  Slide 18: Agenda Divider 06 (Check Out highlighted)
  Slide 19: Thank You
```

---

## Slide-by-Slide Specification

### Slide 0: Cover

**Layout:** `Title Lime + one Logo` (layout index 40)
**Purpose:** Opening slide shown as participants arrive; sets project context and branding
**Content Type:** System-generated (logo is user-supplied)

| Element | Content | Example |
|---------|---------|---------|
| Date | `{kick_off_date}` | `25.02.2026` |
| Title | `{project_title}` | `AI-Powered Quotation Assistant` |
| Subtitle | `{use_case_subtitle}` | `Kick-Off \| Automated Quotation Creation` |
| Client Logo | `[IMAGE: Add client logo here]` | Gray placeholder box (user fills in) |

**Placeholder indices:** Logo area is user-fills-image
**Content source:** variables.json (project_title, use_case_subtitle, kick_off_date, client_logo)

**Notes:**
- Title should use title case
- The subtitle typically follows the pattern: `Kick-Off | {use_case_name}`
- Client logo placeholder is a gray box (top-right area)
- Date format: DD.MM.YYYY
- For German variant, subtitle becomes: `Kick-Off | {use_case_name_de}`

---

### Slide 1: Full Agenda

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Overview of all 6 sections with page references; shown once at the start
**Content Type:** System-generated (static structure, dynamic page numbers)

| Placeholder Index | Content | Example |
|-------------------|---------|---------|
| 13 | Section 1 name | `Check In` |
| 14 | Section 1 number | `01` |
| 15 | Section 2 name | `Use-Case` |
| 16 | Section 2 number | `02` |
| 17 | Section 1 page ref | `03` |
| 18 | Section 2 page ref | `05` |
| 19 | Section 3 name | `Timeline` |
| 20 | Section 3 number | `03` |
| 21 | Section 3 page ref | `10` |
| 25 | Section 4 name | `Collaboration` |
| 26 | Section 4 number | `04` |
| 27 | Section 5 name | `Other Topics` |
| 28 | Section 5 number | `05` |
| 29 | Section 4 page ref | `14` |
| 30 | Section 5 page ref | `17` |
| 31 | Section 6 name | `Check Out` |
| 32 | Section 6 number | `06` |
| 33 | Section 6 page ref | `19` |

**Content source:** Computed from slide count; section names from variables.json or defaults
**Placeholder indices:** 13-21, 25-33 (see table above)

**Notes:**
- On the full agenda slide, ALL sections are displayed in the same color (no highlighting)
- Page references are zero-indexed slide numbers formatted as two-digit strings
- Section names are the canonical English defaults unless overridden for German or rollout variants
- Standard English section names: Check In, Use-Case, Timeline, Collaboration, Other Topics, Check Out
- Standard German section names: Check In, Die Anwendung, Projektablauf, Zusammenarbeit, Weitere Punkte, Check Out

---

### Slide 2: Agenda Divider 01 (Check In)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Check In" as the active section
**Content Type:** System-generated (identical structure to Slide 1, with highlighting)

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 1 ("Check In") text is rendered in Sharp Green (#18A05A) to indicate it is active
- All other section names are rendered in a grayed-out color
- The structure and page references are identical to Slide 1
- This pattern repeats for all 6 agenda divider slides (Slides 2, 4, 9, 13, 16, 18)

---

### Slide 3: Check-In

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Interactive opening slide with icebreaker questions; optionally includes a GIF
**Content Type:** Semi-auto (text generated, GIF is user-supplied)

| Element | Content | Example |
|---------|---------|---------|
| Title | `CHECK IN` | `CHECK IN` |
| Question 1 | Icebreaker question | `Who am I?` |
| Question 2 | Context question | `What is my role in this project?` |
| Question 3 | Expectation question | `When is this kick-off a success?` |
| GIF (optional) | `[IMAGE: Add icebreaker GIF]` | Animated GIF or illustration |

**Content source:** content.json -> check_in -> questions (array of strings)
**Placeholder indices:** Text body placeholder + optional image placeholder for GIF

**Content Guidelines:**
- Questions should be conversational and warm, not formal
- Standard set: identity, role/context, success criteria
- The {client_name} or {project_name} can be substituted into questions for personalization
- GIF is optional but recommended for setting a relaxed tone
- 3 questions is the standard count; can be 2-4

**Notes:**
- Lime background with dark text
- GIF is placed to the right or bottom-right of the questions
- If no GIF is provided, the text expands to fill the slide

---

### Slide 4: Agenda Divider 02 (Use-Case)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Use-Case" as the active section
**Content Type:** System-generated

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 2 ("Use-Case") text is rendered in Sharp Green (#18A05A)
- All other section names are grayed out
- For rollout variant, this section is named "THE APPLICATION" (English) or "Die Anwendung" (German)

---

### Slide 5: Pain x Data

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Present the P x D (Pain times Data) formula -- the core justification for the use case
**Content Type:** System-generated text (from source enrichment); optional GIF is user-supplied

| Element | Content | Example |
|---------|---------|---------|
| Title | `PAIN x DATA` or use-case name | `PAIN x DATA` |
| Pain Bullets | 3-5 pain points | `~50 quotations per day created manually, tying up sales capacity.` |
| Data Bullets | 2-4 data source descriptions | `Inquiry emails and PDFs in multiple languages and formats.` |
| Solution Bullets | 2-3 solution outcome statements | `AI-assisted quotation drafts reduce turnaround from days to hours.` |
| GIF (optional) | `[IMAGE: Add P x D GIF]` | Illustration or animated GIF |

**Content source:** content.json -> use_case -> pain_points (array), data_sources (array), solution_outcomes (array)
**Placeholder indices:** Text body placeholder + optional image placeholder for GIF

**Content Guidelines:**
- Pain section: Each bullet is 1 sentence, 10-20 words. Start with the most impactful pain point. Include numbers/metrics when available. Use client's own terminology.
- Data section: Each bullet describes a concrete, available data source. Specify format, volume, and relevance. Only list data that exists and is accessible.
- Solution section: Each bullet describes an expected outcome of applying AI to the pain + data combination. Action-oriented, starting with a verb or AI capability.
- The P x D formula should feel like a logical argument: pain exists, data exists, therefore this solution is viable.

**Example (Montanstahl):**
```
Pain:
- ~50 quotations per day created manually, tying up sales capacity.
- Enquiries in varied formats (emails, PDFs, portals) requiring manual interpretation.
- High error rate in manual transcription to ERP system.

Data:
- Inquiry emails and PDFs: Real customer inquiries in multiple languages with varying formats.
- Product master data: Product list with SP numbers, measurements, materials.

Solution:
- AI-assisted quotation drafts reduce turnaround from days to hours.
- Automated product matching increases accuracy and consistency.
```

**Notes:**
- GIF is placed to the right or bottom-right of the content
- If no GIF is provided, the text expands to fill the slide
- For multi use-case variant: duplicate this slide for each use case, adjusting content per UC

---

### Slide 6: Hackathon Validation

**Layout:** `DEFAULT` (layout index 79)
**Purpose:** Show evidence from the hackathon that validated this use case; Miro board screenshots and co-creation highlights
**Content Type:** Manual/Image (user-supplied images, optional auto-generated captions)

| Element | Content | Example |
|---------|---------|---------|
| Title | `HACKATHON VALIDATION` or `CO-CREATION HIGHLIGHTS` | `HACKATHON VALIDATION` |
| Images | 1-3 Miro board screenshots or co-creation artifacts | Exported Miro frames |
| Captions (optional) | Brief descriptions of what each image shows | `Day 1 brainstorming results` |

**Content source:** content.json -> hackathon -> validation_images (array of image refs), validation_captions (array of strings)
**Placeholder indices:** Image placeholders (user-supplied or auto-extracted from Miro)

**Content Guidelines:**
- Images should be actual artifacts from the hackathon: Miro boards, whiteboard photos, prototype screenshots
- Captions are optional but recommended for context
- If no hackathon occurred (e.g., rollout kick-off), this slide may be replaced with solution screenshots

**Notes:**
- DEFAULT layout provides maximum flexibility for image placement
- For rollout variant: replace with solution/application screenshots instead of hackathon artifacts
- If hackathon validation is not available, this slide can be skipped or replaced with a solution overview

---

### Slide 7: Step by Step

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Present the 4-phase progression of the project from MVP to full feedback loop
**Content Type:** System-generated text; optional screenshots are user-supplied

| Element | Content | Example |
|---------|---------|---------|
| Title | `STEP BY STEP` | `STEP BY STEP` |
| Phase 1 | MVP description | `MVP: Core quotation parsing and draft generation` |
| Phase 2 | Data deep dive description | `Data Deep Dive: Integrate product catalog and pricing engine` |
| Phase 3 | Expansion description | `Expansion: Multi-language support and portal integration` |
| Phase 4 | Feedback description | `Feedback: User testing, accuracy tuning, and workflow refinement` |
| Screenshots (optional) | `[IMAGE: Add step screenshots]` | UI mockups or architecture sketches per phase |

**Content source:** content.json -> use_case -> phases (array of objects: {name, description})
**Placeholder indices:** Text body placeholder + optional image placeholders

**Content Guidelines:**
- Exactly 4 phases in the standard structure
- Each phase: short name + 1-2 sentence description
- Progression should feel logical: build -> deepen -> expand -> refine
- Phase names can be customized but the 4-phase pattern is standard
- Screenshots are optional but help make the progression tangible

**Example:**
```
MVP: Build core AI pipeline for parsing inquiries and generating draft quotations.
Data Deep Dive: Connect to product catalog, pricing rules, and customer history.
Expansion: Support multi-language inquiries, portal integrations, and bulk processing.
Feedback: Conduct user acceptance testing, tune accuracy, and refine approval workflow.
```

**Notes:**
- Lime background with dark text
- The 4-phase model is OT's standard project progression
- For multi use-case variant, phases may be shared or UC-specific

---

### Slide 8: Architecture

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Show the technical architecture diagram and describe key capabilities
**Content Type:** Semi-auto (architecture diagram is auto-extracted or user-supplied; capabilities text is generated)

| Element | Content | Example |
|---------|---------|---------|
| Title | `ARCHITECTURE` | `ARCHITECTURE` |
| Image | Architecture diagram | System diagram showing components, APIs, data flow |
| Capabilities | 3-5 bullet points describing technical capabilities | `Real-time inquiry parsing via NLP pipeline` |

**Content source:** content.json -> use_case -> architecture (object: {diagram_ref, capabilities array})
**Placeholder indices:** Image placeholder for diagram + text body for capabilities

**Content Guidelines:**
- Architecture diagram should show: data sources, AI components, integrations, outputs
- Capabilities text: 3-5 bullets describing what the system does technically
- Each capability: 1 sentence, action-oriented
- Use technical but accessible language (stakeholders will read this)
- Diagram can be auto-extracted from scope document or sprint design document

**Example:**
```
Capabilities:
- Real-time inquiry parsing via NLP pipeline (emails, PDFs, portal submissions).
- Product matching against master data using fuzzy search and ML classification.
- Draft quotation generation with pricing lookup and configurable approval rules.
- Integration with SAP via OData API for master data and order lifecycle.
- Monitoring dashboard for accuracy tracking and exception handling.
```

**Notes:**
- The architecture diagram is the primary visual element; capabilities text is secondary
- Diagram is typically auto-extracted from the scope document or sprint design
- If no diagram is available, a placeholder box is shown with "[IMAGE: Add architecture diagram]"
- This is one of the most important slides for technical stakeholders

---

### Slide 9: Agenda Divider 03 (Timeline)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Timeline" as the active section
**Content Type:** System-generated

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 3 ("Timeline") text is rendered in Sharp Green (#18A05A)
- All other section names are grayed out
- For rollout variant, this section may be named "ROLLOUT SCOPE" instead of "Timeline"
- For German variant: "Projektablauf"

---

### Slide 10: Sprint Goals

**Layout:** `1_Bullet Points Lime` (layout index 69)
**Purpose:** Present sprint-by-sprint goals in a columnar card format
**Content Type:** System-generated text (from project plan)

| Element | Content | Example |
|---------|---------|---------|
| Title | `SPRINT GOALS` | `SPRINT GOALS` |
| Sprint 1 Card | Title + deliverables | `Sprint 1: Foundation` + bullet list |
| Sprint 2 Card | Title + deliverables | `Sprint 2: Core Pipeline` + bullet list |
| Sprint 3 Card | Title + deliverables | `Sprint 3: Integration` + bullet list |
| Sprint 4 Card | Title + deliverables | `Sprint 4: Testing & Handover` + bullet list |

**Content source:** content.json -> timeline -> sprints (array of objects: {number, title, deliverables array})
**Placeholder indices:** 4 columnar text regions (card layout)

**Content Guidelines:**
- Standard project has 4 sprints (2 weeks each = 8 weeks total)
- Each card: sprint number + title (bold) + 3-5 deliverable bullets
- Deliverables should be concrete and verifiable (not vague)
- Sprint titles should reflect the progression: setup -> build -> integrate -> validate
- For rollout variant: may have only 2 sprints

**Example:**
```
Sprint 1: Foundation
- Environment setup and data access
- Initial data pipeline for inquiry parsing
- Baseline accuracy measurement

Sprint 2: Core Pipeline
- Product matching algorithm
- Pricing lookup integration
- Draft quotation template engine

Sprint 3: Integration
- SAP OData API connection
- End-to-end workflow testing
- Error handling and edge cases

Sprint 4: Testing & Handover
- User acceptance testing with sales team
- Accuracy tuning and threshold calibration
- Documentation and knowledge transfer
```

**Notes:**
- The `1_Bullet Points Lime` layout (index 69) supports columnar card arrangement
- 4 columns is standard; 2 columns for rollout variant with fewer sprints
- For multi use-case variant: sprint goals become multi-track (one track per UC)
- Each card should fit 3-5 bullet points to avoid overflow

---

### Slide 11: Timeline / Gantt

**Layout:** `Calendar Lime w/o lines` (layout index 22)
**Purpose:** Visual Gantt-style timeline showing months, calendar weeks, task rows, sprint bars, and milestones
**Content Type:** System-generated table (from project plan)

| Element | Content | Example |
|---------|---------|---------|
| Title | `TIMELINE` | `TIMELINE` |
| Month Headers | Month names spanning calendar weeks | `March`, `April`, `May`, `June` |
| CW Headers | Calendar week numbers | `CW 10`, `CW 11`, ..., `CW 22` |
| Task Rows | Named work streams with sprint bars | `AI Development`, `Integration`, `Testing` |
| Sprint Bars | Colored bars spanning CW ranges | Green bars for active sprint periods |
| Milestones | Diamond or marker icons at key dates | `MVP Demo`, `Go-Live` |

**Content source:** content.json -> timeline -> gantt (object: {months, calendar_weeks, tasks, milestones})
**Placeholder indices:** Table/calendar placeholder in the Calendar Lime layout

**Content Guidelines:**
- Months are displayed as column group headers
- Calendar weeks (CW) are individual columns under each month
- Task rows represent work streams, not individual tasks
- Sprint bars are colored blocks spanning the relevant CW range
- Milestones are marked with icons or labels at specific CWs
- For German variant: use "KW" instead of "CW"; month names in German (Marz, April, Mai, Juni)
- Standard timeline: 8-12 weeks (4 sprints x 2 weeks + buffer)

**Example structure:**
```
           |  March          |  April          |  May            |  June     |
           | CW10 | CW11 | CW12 | CW13 | CW14 | CW15 | CW16 | CW17 | CW18 |
-----------+------+------+------+------+------+------+------+------+------+
Sprint 1   | ████ | ████ |      |      |      |      |      |      |      |
Sprint 2   |      |      | ████ | ████ |      |      |      |      |      |
Sprint 3   |      |      |      |      | ████ | ████ |      |      |      |
Sprint 4   |      |      |      |      |      |      | ████ | ████ |      |
-----------+------+------+------+------+------+------+------+------+------+
Milestones |      |      |  MVP |      |      |      |      |  UAT | Live |
```

**Notes:**
- The Calendar Lime layout (index 22) is specifically designed for Gantt-style tables
- Sprint bars should align with the sprint dates defined in sprint goals
- Milestones should correspond to key deliverables or decision points
- For multi use-case variant: task rows become multi-track (one row per UC plus shared rows)
- For rollout variant: fewer sprints (2 vs 4), possibly shorter overall timeline
- This is a complex layout; content generation must precisely map CW ranges to table cells

---

### Slide 12: Progress / Risks

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Two-column view showing what has already been accomplished and what risks are anticipated
**Content Type:** System-generated text (from project status)

| Element | Content | Example |
|---------|---------|---------|
| Title | `PROGRESS / RISKS` | `PROGRESS / RISKS` |
| Left Column Title | `What already happened` | `What already happened` |
| Left Column Bullets | 3-5 completed items | `Hackathon completed with 88% accuracy on test set` |
| Right Column Title | `Which risks do we see` | `Which risks do we see` |
| Right Column Bullets | 3-5 identified risks | `Data quality varies across customer segments` |

**Content source:** content.json -> timeline -> progress (array of strings), risks (array of strings)
**Placeholder indices:** Two-column text body placeholder

**Content Guidelines:**
- Progress bullets: past tense, concrete accomplishments with metrics where possible
- Risk bullets: present tense, specific and actionable (not vague fears)
- Each bullet: 1 sentence, 10-20 words
- Progress should reference hackathon results, data access confirmations, stakeholder alignment
- Risks should cover: data quality, integration complexity, resource availability, timeline pressure, adoption
- Balance: roughly equal number of bullets in both columns

**Example:**
```
What already happened:
- Hackathon completed with 88% first-pass accuracy on 50 test quotations.
- SAP OData API access confirmed and tested in sandbox.
- Key stakeholders aligned on MVP scope and success criteria.
- Development environment provisioned on AWS.

Which risks do we see:
- Data quality varies across customer segments; new customers lack complete specs.
- SAP pricing data may be stale during peak load hours.
- Sales team availability for UAT limited to 2 hours/week.
- Timeline assumes no scope changes after Sprint 2.
```

**Notes:**
- The two-column layout is achieved within the Bullet Points Lime layout using text formatting
- Columns should be visually balanced (same approximate height)
- For German variant: "Was ist bereits passiert" / "Welche Risiken sehen wir"

---

### Slide 13: Agenda Divider 04 (Collaboration)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Collaboration" as the active section
**Content Type:** System-generated

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 4 ("Collaboration") text is rendered in Sharp Green (#18A05A)
- All other section names are grayed out
- For German variant: "Zusammenarbeit"

---

### Slide 14: Participants

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Show the collaboration structure as a circular/hub diagram with recurring meeting types and participant groups
**Content Type:** System-generated text (from project plan); diagram is auto-composed

| Element | Content | Example |
|---------|---------|---------|
| Title | `PARTICIPANTS` | `PARTICIPANTS` |
| Diagram | Circular diagram showing meeting types | Hub-and-spoke with 4 meeting categories |
| Jour Fixe | Regular sync meeting | `Jour Fixe: Weekly, 30 min, OT + Client PM` |
| IT Alignments | Technical sync | `IT Alignments: Bi-weekly, 60 min, OT Dev + Client IT` |
| Steering Committee | Executive oversight | `Steering Committee: Monthly, 60 min, OT Lead + Client Exec` |
| Testing | UAT coordination | `Testing: Sprint-end, 90 min, OT QA + Client Users` |

**Content source:** content.json -> collaboration -> participant_groups (array of objects: {name, frequency, duration, participants})
**Placeholder indices:** Text body placeholder (diagram is composed from text/shapes)

**Content Guidelines:**
- 4 meeting categories is standard: Jour Fixe, IT Alignments, Steering Committee, Testing
- Each category: name, frequency, duration, and participant list
- The circular diagram visually shows how these groups interconnect
- Participant names or roles should be specific (not just "client team")
- For multi use-case variant: may have additional Jour Fixe per UC

**Notes:**
- The circular/hub diagram is a visual convention, not a template-level feature; it is composed using shapes or a pre-placed image
- For German variant: meeting names remain the same (Jour Fixe is already French/international; Steering Committee may stay English or become "Lenkungsausschuss")

---

### Slide 15: Meetings

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Detail each recurring meeting with day, time, frequency, and participant list
**Content Type:** System-generated text (from project plan)

| Element | Content | Example |
|---------|---------|---------|
| Title | `MEETINGS` | `MEETINGS` |
| Meeting Card 1 | Jour Fixe details | `Jour Fixe: Tuesday, 10:00, Weekly, OT PM + Client PM` |
| Meeting Card 2 | IT Alignment details | `IT Alignment: Thursday, 14:00, Bi-weekly, OT Dev + Client IT` |
| Meeting Card 3 | Steering Committee details | `Steering: 1st Monday/month, 11:00, Monthly, OT Lead + Client Exec` |
| Meeting Card 4 | Testing details | `Testing: Friday (sprint-end), 09:00, Bi-weekly, OT QA + Client Users` |

**Content source:** content.json -> collaboration -> meetings (array of objects: {name, day, time, frequency, participants})
**Placeholder indices:** Text body placeholder (card-style formatting)

**Content Guidelines:**
- Each meeting card: name (bold) + day + time + frequency + participant list
- Be specific about day and time (not just "weekly")
- Participant list should name roles or specific people
- Order: most frequent first (Jour Fixe) to least frequent (Steering Committee)
- For multi use-case variant: may have separate Jour Fixe entries per UC

**Example:**
```
Jour Fixe
  Day: Tuesday | Time: 10:00 | Frequency: Weekly
  Participants: OT Project Manager, Client Project Manager, Use-Case Lead

IT Alignment
  Day: Thursday | Time: 14:00 | Frequency: Bi-weekly
  Participants: OT Tech Lead, Client IT Manager, Data Engineer

Steering Committee
  Day: 1st Monday of month | Time: 11:00 | Frequency: Monthly
  Participants: OT Partner, Client VP Operations, Client CTO

Testing / UAT
  Day: Friday (sprint-end) | Time: 09:00 | Frequency: Bi-weekly
  Participants: OT QA Lead, Client Power Users (2-3 from sales team)
```

**Notes:**
- Meeting cards are formatted as structured text blocks within the Bullet Points Lime layout
- Visual separation between cards is achieved through spacing and bold titles
- Times should include timezone if participants are in different zones

---

### Slide 16: Agenda Divider 05 (Other Topics)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Other Topics" as the active section
**Content Type:** System-generated

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 5 ("Other Topics") text is rendered in Sharp Green (#18A05A)
- All other section names are grayed out
- For German variant: "Weitere Punkte"

---

### Slide 17: Discussion

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Open discussion slide for any topics not covered in the structured sections
**Content Type:** Static text with optional icon

| Element | Content | Example |
|---------|---------|---------|
| Title | `OTHER TOPICS` | `OTHER TOPICS` |
| Subtitle | `DISCUSSION` | `DISCUSSION` |
| Icon | Projector or discussion icon | Projector/presentation icon (decorative) |

**Content source:** Static (no content.json dependency)
**Placeholder indices:** Text body placeholder + optional image placeholder for icon

**Notes:**
- This is a mostly static slide; the content is fixed
- The projector icon is decorative and placed center or right
- No bullets or generated content -- this slide is a prompt for live discussion
- Facilitator uses this slide to open the floor for questions, concerns, and additional topics
- For German variant: "WEITERE PUNKTE" / "DISKUSSION"

---

### Slide 18: Agenda Divider 06 (Check Out)

**Layout:** `ToC middle w/o lines` (layout index 78)
**Purpose:** Section divider highlighting "Check Out" as the active section
**Content Type:** System-generated

**Placeholder indices:** Same as Slide 1 (indices 13-21, 25-33)
**Content source:** Same as Slide 1

**Notes:**
- Section 6 ("Check Out") text is rendered in Sharp Green (#18A05A)
- All other section names are grayed out
- For German variant: section name remains "Check Out" (English loan word used in German context)

---

### Slide 19: Thank You

**Layout:** `Bullet Points Lime` (layout index 0)
**Purpose:** Closing slide with gratitude message and feedback prompt
**Content Type:** System-generated text (static with optional customization)

| Element | Content | Example |
|---------|---------|---------|
| Title | `THANK YOU!!` | `THANK YOU!!` |
| Feedback Question | Closing reflection question | `What is one thing you are taking away from today?` |
| Icons | Thumbs-up icons | Decorative thumbs-up icons (left and right) |

**Content source:** content.json -> check_out -> feedback_question (string, optional); defaults to standard question
**Placeholder indices:** Text body placeholder + optional image placeholders for icons

**Content Guidelines:**
- The "THANK YOU!!" title is standard (with double exclamation)
- Feedback question should be open-ended and positive
- Standard question: "What is one thing you are taking away from today?"
- Alternative: "On a scale of 1-5, how confident are you in this project's direction?"
- Thumbs-up icons are decorative and placed symmetrically

**Notes:**
- Lime background with dark text
- Icons are decorative; they do not need to be user-supplied (embedded in template)
- For German variant: "VIELEN DANK!!" with German feedback question

---

## Image Placeholder Summary

| Slide # | Slide Title | Placeholder Description | Source | Required? | When to Add |
|---------|-------------|------------------------|--------|-----------|------------|
| 0 | Cover | Client logo | User upload | Optional | Before kick-off |
| 3 | Check-In | Icebreaker GIF | User upload | Optional | Before kick-off |
| 5 | Pain x Data | P x D illustration GIF | User upload | Optional | Before kick-off |
| 6 | Hackathon Validation | Miro board images | Auto from Miro export | Optional | After hackathon |
| 7 | Step by Step | Phase screenshots | User upload | Optional | During preparation |
| 8 | Architecture | Architecture diagram | Auto-extracted from scope doc / sprint design | Auto | During preparation |

---

## Agenda / ToC Placeholder Index Map

All agenda divider slides (Slides 1, 2, 4, 9, 13, 16, 18) use layout index 78 (`ToC middle w/o lines`). The placeholder indices are mapped as follows:

```
Section 1:  name=13  number=14  page=17
Section 2:  name=15  number=16  page=18
Section 3:  name=19  number=20  page=21
Section 4:  name=25  number=26  page=29
Section 5:  name=27  number=28  page=30
Section 6:  name=31  number=32  page=33
```

**Highlighting rules:**
- Slide 1 (Full Agenda): No highlighting; all sections in default color
- Slide 2: Section 1 highlighted (green), rest grayed
- Slide 4: Section 2 highlighted (green), rest grayed
- Slide 9: Section 3 highlighted (green), rest grayed
- Slide 13: Section 4 highlighted (green), rest grayed
- Slide 16: Section 5 highlighted (green), rest grayed
- Slide 18: Section 6 highlighted (green), rest grayed

**Green highlight color:** Sharp Green #18A05A (or Accent Green #19A960 depending on scheme)
**Gray inactive color:** Light gray, ~60% opacity

---

## Available Template Layouts

The OT kick-off template contains branded slide layouts. The most commonly used for kick-off presentations:

| Layout Name | Index | Usage | Background | Content Style |
|-------------|-------|-------|------------|---------------|
| Bullet Points Lime | 0 | Check-In, P x D, Step by Step, Architecture, Progress/Risks, Participants, Meetings, Discussion, Thank You | Lime (#D5F89E) | Title + bullet list / two-column |
| Calendar Lime w/o lines | 22 | Timeline / Gantt | Lime | Table with month/CW headers and task bars |
| Title Lime + one Logo | 40 | Cover | Lime / Green | Date, title, subtitle, client logo |
| 1_Bullet Points Lime | 69 | Sprint Goals | Lime | Columnar card layout (4 columns) |
| ToC middle w/o lines | 78 | Full Agenda + all 6 Agenda Dividers | White | 6-section numbered list with page refs |
| DEFAULT | 79 | Hackathon Validation | White | Flexible: images, text, cards |

---

## Brand Guidelines

| Element | Value |
|---------|-------|
| Sharp Green | #18A05A (cover, highlights) |
| Accent Green | #19A960 (scheme accent2) |
| Lime | #D5F89E (scheme lt2/bg2, slide backgrounds) |
| Ash | #2F2F2F (body text) |
| Dark | #242424 (ash backgrounds) |
| Body Font | Akkurat LL |
| Decorative Font | Wavetable (timeline title, special headings) |
| Footer | `(c) 2019-2026 ONE THOUSAND` + slide number |
| Format | 16:9 widescreen (13.333" x 7.5") |

---

## Variations

### Multi Use-Case Variant

When a project covers multiple use cases, the following changes apply:

- **Slide 5 (Pain x Data):** Duplicated for each use case. Each UC gets its own P x D slide with UC-specific pain, data, and solution bullets. Agenda section 2 name may become plural ("Use-Cases").
- **Slide 10 (Sprint Goals):** Sprint cards become multi-track. Each sprint may list deliverables per UC, or sprints may be UC-specific.
- **Slide 11 (Timeline / Gantt):** Task rows become multi-track. Each UC gets its own row(s) plus shared infrastructure rows.
- **Slide 15 (Meetings):** May include additional Jour Fixe entries, one per UC, with UC-specific participants.
- **Slide count:** Increases by 1 per additional use case (additional P x D slide).

### Rollout Kick-Off Variant

When the kick-off is for a rollout (post-PoC deployment), the following changes apply:

- **Agenda section names change:**
  - Section 2: "THE APPLICATION" (English) or "Die Anwendung" (German) instead of "Use-Case"
  - Section 3: "ROLLOUT SCOPE" (English) or "Rollout-Umfang" (German) instead of "Timeline"
- **Slide 6 (Hackathon Validation):** May be skipped entirely or replaced with solution screenshots showing the production application.
- **Slide 10 (Sprint Goals):** Fewer sprints (typically 2 instead of 4), focused on deployment, training, and go-live.
- **Slide 11 (Timeline / Gantt):** Shorter timeline, focused on rollout phases rather than development sprints.
- **Overall tone:** More operational, less exploratory. Emphasizes deployment logistics, training, and change management.

### German Language Variant

When the presentation is in German, the following translations apply:

| English | German |
|---------|--------|
| Check In | Check In |
| Use-Case | Die Anwendung |
| Timeline | Projektablauf |
| Collaboration | Zusammenarbeit |
| Other Topics | Weitere Punkte |
| Check Out | Check Out |
| CW (Calendar Week) | KW (Kalenderwoche) |
| Sprint Goals | Sprint-Ziele |
| Progress / Risks | Fortschritt / Risiken |
| What already happened | Was ist bereits passiert |
| Which risks do we see | Welche Risiken sehen wir |
| Participants | Teilnehmer |
| Meetings | Termine |
| Discussion | Diskussion |
| Thank You | Vielen Dank |
| Month names | Januar, Februar, Marz, April, Mai, Juni, Juli, August, September, Oktober, November, Dezember |

**Notes:**
- "Check In" and "Check Out" remain in English (common loan words in German business context)
- Jour Fixe remains unchanged (French, used internationally)
- Steering Committee may become "Lenkungsausschuss" or remain English depending on client preference

---

## Content Generation Rules

1. **No Inventions**: Every fact, metric, or detail must trace to source material. Use `[To be confirmed]` for unknowns.
2. **Parallel Structure**: If one bullet starts with a verb, all bullets in that section should start with verbs. If one bullet starts with a noun, all should.
3. **Client Terminology**: Use the client's own words and abbreviations (SP numbers, not product codes).
4. **Word Budgets**: Respect per-slide limits -- pain bullets 10-20 words each, sprint deliverables 5-15 words each, risk bullets 10-20 words each.
5. **Consistent Tense**: Progress bullets in past tense ("Completed..."), risk bullets in present tense ("Data quality varies..."), sprint goals in future/imperative ("Build...", "Integrate...").
6. **Confidence Scoring**: Every generated section has a confidence score; borderline sections get `[To be confirmed]` markers.
7. **Formatting Consistency**: Titles in UPPER CASE on slides. Section names in Title Case in the ToC. Body text in sentence case.

---

## Checklist for Slide Generation

- [ ] All 20 slides accounted for (1 cover + 1 full agenda + 6 agenda dividers + 12 content slides = 20)
- [ ] All client names, dates, and project titles filled from variables.json
- [ ] All content sourced from content.json
- [ ] Image placeholders clearly marked as user-fills-image where applicable
- [ ] Architecture diagram auto-extracted or placeholder inserted
- [ ] No invented metrics or details -- all `[To be confirmed]` markers in place for unknowns
- [ ] Agenda divider highlighting matches the correct section per slide
- [ ] ToC page references match actual slide positions (especially after multi-UC duplication)
- [ ] Sprint goals align with timeline/Gantt dates
- [ ] Meeting details are complete (day, time, frequency, participants)
- [ ] Word budgets respected per slide
- [ ] Parallel structure checked across bullet groups
- [ ] Language variant applied consistently (EN vs DE) across all slides
- [ ] Footer present on all slides: "(c) 2019-2026 ONE THOUSAND" + slide number
- [ ] Presentation format: 16:9 (13.333" x 7.5")
