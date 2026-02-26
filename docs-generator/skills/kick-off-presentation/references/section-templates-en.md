# Section Templates — English

Writing patterns, word budgets, and style guidance for each slide's content in the kick-off presentation.

---

## General Writing Principles

1. **Presentation slides, not paragraphs** — Every bullet should be scannable in 2-3 seconds
2. **Active voice** — "Analyze incoming data" not "Incoming data is analyzed"
3. **Client vocabulary** — Use their terminology (their product names, not generic labels)
4. **Specific over generic** — "4 sprints over 16 weeks" not "several development phases"
5. **No filler** — Cut "In order to", "It is important to note that", "As mentioned above"
6. **Parallel structure** — If first bullet starts with a verb, all bullets start with verbs
7. **Em-dashes for structured content** — Format as "Title — description" in risks, phases, and sprint goals
8. **Metrics from source material only** — No invented numbers; use `[To be confirmed]` if uncertain
9. **Honest but constructive** — Acknowledge risks without defeatism
10. **Audience-focused** — Every slide answers: "Why should I care?" for kick-off attendees

---

## Power Verbs List

Use these action verbs to start sprint goals, phase descriptions, and deliverable bullets. They convey energy and clarity:

**Data & Analysis:**
- Analyze, Parse, Extract, Ingest, Capture, Import, Profile, Assess

**Design & Build:**
- Design, Build, Prototype, Develop, Implement, Configure, Deploy, Architect

**Validation & Quality:**
- Validate, Verify, Test, Review, Audit, Confirm, Benchmark, Evaluate

**Process & Delivery:**
- Execute, Deliver, Release, Ship, Launch, Roll out, Hand off, Publish

**Collaboration & Communication:**
- Align, Coordinate, Facilitate, Present, Document, Train, Onboard, Brief

**Optimization & Iteration:**
- Optimize, Refine, Enhance, Improve, Iterate, Expand, Scale, Tune

**Integration & Connection:**
- Integrate, Connect, Sync, Migrate, Link, Bridge, Interface, Embed

**Examples:**
- "Analyze existing data pipelines" (not "Look at data")
- "Prototype the core matching engine" (not "Build a first version")
- "Validate output accuracy against historical records" (not "Check if it works")
- "Deploy MVP to staging environment" (not "Put it somewhere for testing")

---

## Parallel Structure Rules

**Rule**: If the first element in a list starts with a verb, ALL must start with verbs. Same for nouns, adjectives, or prepositional phrases.

**Bad example (mixed):**
```
- Analyze incoming customer requests
- Build matching algorithm
- The system generates draft proposals
```

**Good example (parallel verbs):**
```
- Analyze incoming customer requests
- Build matching algorithm
- Generate draft proposals
```

**Bad example (mixed sprint titles):**
```
Sprint 1: Data Foundation
Sprint 2: Building the Core Engine
Sprint 3: Integration Phase
Sprint 4: User Testing and Feedback
```

**Good example (parallel noun phrases):**
```
Sprint 1: Data Foundation
Sprint 2: Core Engine
Sprint 3: System Integration
Sprint 4: User Validation
```

---

## 1. Cover Slide

**Word budget:** 20 words
**Tone:** Bold, branded
**Placement:** First slide

### Template Pattern

```
{TAGLINE}

{USE_CASE_TITLE}

Project Kick-Off | DD.MM.YYYY
```

### Tagline Pattern

```
STRENGTHENING {CLIENT_NAME} WITH AI
```

### Example

```
STRENGTHENING HABA WITH AI

Product Advisor — Intelligent Recommendation Engine

Project Kick-Off | 15.03.2026
```

### Key Rules

- Tagline is ALWAYS uppercase
- Use the pattern "STRENGTHENING {CLIENT} WITH AI" — consistent across all kick-offs
- Use case title follows tagline; can include an em-dash subtitle
- Date format: `Project Kick-Off | DD.MM.YYYY`
- No logos or imagery instructions — those come from the design system
- Keep total text under 20 words

---

## 2. Check-In Questions

**Word budget:** 30 words total (2-3 questions)
**Tone:** Conversational, icebreaker
**Placement:** Early slide (slide 2-3)

### Standard Questions (Recommended)

```
Who am I?
When is this kick-off a success?
```

### Alternative Questions

```
What excites me most about this project?
What does a successful collaboration look like to me?
What would I automate first at {client_name}?
```

### Example

```
Who am I?
When is this kick-off a success?
What comes to my mind when I think of {client_name} and AI?
```

### Key Rules

- Maximum 3 questions; 2 is preferred for kick-offs (shorter than hackathons)
- First question is always a personal introduction prompt
- Second question anchors success criteria for the session
- Questions must be open-ended (no yes/no)
- Do NOT make questions too long or formal
- Do NOT ask technical questions — this is an icebreaker
- Do NOT pre-answer the questions
- Tone should feel warm and inviting, setting the collaborative mood for the project

---

## 3. Pain x Data Slide

**Word budget:** 120 words total (40 pain, 40 data, 40 solution)
**Tone:** Problem-focused but constructive; data-grounded
**Placement:** Mid-early slide (context-setting section)

### Layout: Three Columns

```
PAIN                     DATA                     SOLUTION
(3-5 bullets)            (3-5 bullets)            (2-3 bullets)
```

### Pain Column — Template Patterns

**Volume/Capacity Pattern:**
```
~{number} {tasks} per {time_period} handled manually, consuming {team} capacity.
```
Example: `~200 product inquiries per week handled manually, consuming sales team capacity.`

**Time Waste Pattern:**
```
Too much time spent on {activity}: {specific_details}.
```
Example: `Too much time spent on product lookup: matching customer descriptions to catalog items.`

**Error/Quality Pattern:**
```
High error rate in {process} due to {cause}.
```
Example: `High error rate in product recommendations due to incomplete customer requirements.`

**Format/Channel Pattern:**
```
{Items} arrive in varied formats ({list}), requiring manual interpretation.
```
Example: `Customer requests arrive in varied formats (email, phone, chat), requiring manual interpretation.`

**Bottleneck Pattern:**
```
{Activity} is a bottleneck: {reason}, causing {consequence}.
```
Example: `Product matching is a bottleneck: no automated lookup, causing 20-minute delays per inquiry.`

### Pain Column — Key Rules

- Start with the most impactful or quantifiable pain point
- Include at least one metric/number if available from source material
- Use the client's own words and terminology
- Each bullet should be independently understandable
- Do NOT invent metrics — use `[To be confirmed]` if numbers are not in source
- 3-5 bullets, each 8-15 words

### Data Column — Template Patterns

**Structured Data Pattern:**
```
{System} contains {data_type}: {specifics about volume, format, or coverage}.
```
Example: `ERP system contains product master data: 5,000+ SKUs with specifications and pricing.`

**Unstructured Data Pattern:**
```
{Source} provides {data_type} in {format}: {volume or coverage detail}.
```
Example: `Email archive provides historical inquiries in free-text: 3 years of customer correspondence.`

**External Data Pattern:**
```
{External source} offers {data_type}: {relevance to use case}.
```
Example: `Product catalogs offer category hierarchies: structured taxonomy for recommendation logic.`

### Data Column — Key Rules

- Only list data that actually exists and is accessible
- Mention specific formats (PDF, Excel, email, API, database)
- Include approximate volume if known
- If data availability is uncertain, mark with `[To be confirmed]`
- Focus on data that supports the specific use case
- 3-5 bullets, each 8-15 words

### Solution Column — Template Patterns

**Outcome Pattern:**
```
{Verb} {desired_outcome} to {benefit}.
```
Example: `Generate personalized product recommendations to accelerate sales cycles.`

**Automation Pattern:**
```
Automate {process} — reducing {metric} from {current} to {target}.
```
Example: `Automate product matching — reducing lookup time from 20 minutes to seconds.`

**Capability Pattern:**
```
Enable {team} to {new_capability} with AI-assisted {tool/process}.
```
Example: `Enable sales team to serve more customers with AI-assisted product advisory.`

### Solution Column — Key Rules

- 2-3 bullets that directly address the pain points
- Each solution should map to at least one pain point
- Focus on desired outcomes, not technical implementation
- Use active verbs (Generate, Automate, Enable, Reduce, Accelerate)
- Keep aspirational but grounded — no promises the project cannot deliver

### Full Example

```
PAIN:
- ~200 product inquiries per week handled manually, consuming sales capacity
- Too much time spent matching customer descriptions to catalog products
- Inconsistent recommendations depending on which advisor handles the inquiry
- No systematic way to cross-sell or upsell related products
- Customer wait times averaging 2+ days for complex product questions

DATA:
- Product master data: 5,000+ SKUs with specs, pricing, and availability
- 3 years of historical inquiry-response pairs in email archive
- Customer purchase history in CRM: order patterns and preferences
- Product catalog with category hierarchies and compatibility rules

SOLUTION:
- Generate personalized product recommendations in real-time
- Automate product matching — reducing response time from days to minutes
- Enable consistent, data-driven advisory across the entire sales team
```

---

## 4. Step-by-Step Phases

**Word budget:** 60 words total, 4 items, 1 sentence each
**Tone:** Sequential, clear, forward-moving
**Placement:** Project overview section

### Phase Structure

```
Phase 1: MVP — {Description of prototype/hackathon outcome}
Phase 2: Data Deep Dive — {Description of data validation and enrichment}
Phase 3: Expansion — {Description of feature extension and integration}
Phase 4: User Feedback — {Description of testing and iteration}
```

### Template Pattern

```
{Phase number}: {Phase name} — {One sentence describing the key activity and deliverable}.
```

### Standard Phase Names (EN)

| Phase | Name | Focus |
|-------|------|-------|
| 1 | MVP | Prototype from hackathon; validate core functionality |
| 2 | Data Deep Dive | Clean, enrich, and validate data pipelines |
| 3 | Expansion | Extend features, integrate with production systems |
| 4 | User Feedback | End-user testing, iteration, and handover preparation |

### Example

```
Phase 1: MVP — Deliver working prototype from hackathon covering core matching logic and basic UI.
Phase 2: Data Deep Dive — Validate data quality, enrich pipelines, and benchmark accuracy against real cases.
Phase 3: Expansion — Integrate with production ERP/CRM, add advanced features and edge-case handling.
Phase 4: User Feedback — Conduct user acceptance testing, gather feedback, and iterate before release.
```

### Key Rules

- Exactly 4 phases — this is the standard kick-off structure
- Each phase is 1 sentence, 12-18 words
- Phase 1 always references the hackathon/prototype outcome
- Phase 4 always involves end-user validation
- Use em-dash (—) to separate phase name from description
- Maintain parallel structure across all 4 descriptions
- Phase names should be short (2-3 words maximum)
- Do NOT include dates here — dates go in the Timeline/Gantt slide

---

## 5. Sprint Goals

**Word budget:** 200 words total, ~50 per sprint (for 4 sprints)
**Tone:** Deliverable-focused, specific
**Placement:** Detailed planning section
**Source:** Sprint design plan

### Template Pattern — Single Use Case

```
**Sprint {N}: {Sprint Title}**
- {Deliverable verb} {specific deliverable}
- {Deliverable verb} {specific deliverable}
- {Deliverable verb} {specific deliverable}
- {Deliverable verb} {specific deliverable} [optional 4th]
- {Deliverable verb} {specific deliverable} [optional 5th]
```

### Template Pattern — Multi Use Case

```
**Sprint {N}: {Sprint Title}**
UC1 ({use_case_name}):
- {Deliverable verb} {specific deliverable}
- {Deliverable verb} {specific deliverable}

UC2 ({use_case_name}):
- {Deliverable verb} {specific deliverable}
- {Deliverable verb} {specific deliverable}
```

### Standard Sprint Progression

| Sprint | Typical Title | Focus |
|--------|--------------|-------|
| 1 | Foundation & Data | Data pipelines, environment setup, initial model |
| 2 | Core Logic | Main algorithm/model, primary integrations |
| 3 | Integration & Polish | End-to-end flow, UI, system connections |
| 4 | Testing & Handover | UAT, documentation, deployment preparation |

### Example — Single Use Case

```
**Sprint 1: Foundation & Data**
- Set up development and staging environments
- Build data ingestion pipeline for product master data
- Profile and cleanse historical inquiry data
- Establish accuracy baselines with test dataset

**Sprint 2: Core Matching Engine**
- Develop product matching algorithm using catalog taxonomy
- Integrate customer context from CRM records
- Build recommendation ranking and scoring logic

**Sprint 3: Integration & UI**
- Connect to production ERP via API for live product data
- Build advisor-facing interface with recommendation display
- Implement feedback loop for recommendation quality tracking
- Add cross-sell and upsell suggestion logic

**Sprint 4: Testing & Handover**
- Conduct user acceptance testing with 3-5 sales advisors
- Document system architecture and operational runbook
- Prepare deployment package and monitoring dashboards
- Deliver final presentation and knowledge transfer session
```

### Example — Multi Use Case

```
**Sprint 1: Foundation & Data**
UC1 (Product Advisor):
- Build data ingestion pipeline for product catalog
- Profile historical inquiry-response pairs

UC2 (Order Automation):
- Extract order templates from email archive
- Map order fields to ERP data model

**Sprint 2: Core Logic**
UC1 (Product Advisor):
- Develop matching algorithm with category taxonomy
- Build recommendation scoring engine

UC2 (Order Automation):
- Build order parsing and field extraction pipeline
- Implement validation rules against product master
```

### Key Rules

- Each sprint gets a **bold title** followed by 3-5 deliverable bullets
- Bullets start with action verbs (Build, Develop, Integrate, Test, Deploy, Document, etc.)
- Maintain parallel structure within each sprint
- Sprints should build on each other (no standalone sprints)
- For multi-UC: clearly label which deliverables belong to which use case
- Total across all 4 sprints: ~200 words
- Each bullet: 8-15 words, one specific deliverable
- Do NOT include dates — dates go in the Timeline/Gantt slide
- Source all deliverables from the sprint design plan; do NOT invent features

---

## 6. Timeline / Gantt

**Word budget:** Minimal text — this is a visual/structural slide
**Tone:** Factual, calendar-based
**Placement:** Planning section, after Sprint Goals

### Structure Pattern

```
           | {MON1} | {MON2} | {MON3} | {MON4} | {MON5} | {MON6} |
           | CW{nn} | CW{nn} | CW{nn} | CW{nn} | CW{nn} | CW{nn} |
-----------+--------+--------+--------+--------+--------+--------+
Kick-Off   |   X    |        |        |        |        |        |
{Task 1}   |  ████  |  ████  |        |        |        |        |
{Task 2}   |        |  ████  |  ████  |  ████  |        |        |
{Task 3}   |        |        |        |  ████  |  ████  |        |
Release    |        |        |        |        |        |   X    |
-----------+--------+--------+--------+--------+--------+--------+
Sprint 1   |  ████  |  ████  |        |        |        |        |
Sprint 2   |        |  ████  |  ████  |        |        |        |
Sprint 3   |        |        |  ████  |  ████  |        |        |
Sprint 4   |        |        |        |  ████  |  ████  |        |
```

### Header Row — Month Names (EN)

```
JAN | FEB | MAR | APR | MAY | JUN | JUL | AUG | SEP | OCT | NOV | DEC
```

### Week Numbers

```
CW01 | CW02 | CW03 | ... | CW52
```
Use "CW" (Calendar Week) prefix in English version.

### Standard Task Rows

| Row | Description |
|-----|-------------|
| Kick-Off | Single marker (X) at project start date |
| {Project-specific tasks} | Bars spanning relevant weeks; derived from sprint goals |
| Release Party | Single marker (X) at project end date |

### Sprint Bar Positioning

- Each sprint typically spans 3-4 weeks
- Sprints should be contiguous (no gaps between sprints)
- Sprint bars appear below the task rows
- Color-code or label sprints distinctly

### Legend

```
Legend:
████ {CLIENT_NAME}    (client-responsible tasks)
████ 1000             (One Thousand-responsible tasks)
```

### Example

```
           | MAR    | APR    | MAY    | JUN    | JUL    |
           | CW10   | CW14   | CW18   | CW22   | CW27   |
-----------+--------+--------+--------+--------+--------+
Kick-Off   |   X    |        |        |        |        |
Data Prep  |  ████  |  ████  |        |        |        |
Model Dev  |        |  ████  |  ████  |        |        |
Integration|        |        |  ████  |  ████  |        |
UAT & QA   |        |        |        |  ████  |  ████  |
Release    |        |        |        |        |   X    |
-----------+--------+--------+--------+--------+--------+
Sprint 1   |  ████  |  ████  |        |        |        |
Sprint 2   |        |  ████  |  ████  |        |        |
Sprint 3   |        |        |  ████  |  ████  |        |
Sprint 4   |        |        |        |  ████  |  ████  |

Legend:
████ HABA       ████ 1000
```

### Key Rules

- Months header row uses standard 3-letter English abbreviations
- Week numbers use "CW" prefix (Calendar Week)
- First row is always "Kick-Off"; last row before sprints is always "Release Party" or "Release"
- Project-specific task rows between Kick-Off and Release are derived from sprint goals
- Sprint bars align with the task rows they cover
- Legend distinguishes client tasks from One Thousand tasks
- Keep task names short (1-3 words)
- Do NOT overload the chart — 4-6 task rows maximum plus the sprint bars

---

## 7. Risks

**Word budget:** 80 words total
**Tone:** Honest, proactive, solution-oriented
**Placement:** Planning section

### Layout: Two Columns

```
WHAT ALREADY HAPPENED              WHAT RISKS DO WE SEE
(2-4 bullets)                      (2-4 bullets)
```

### Left Column — "What Already Happened"

Template patterns for known issues or past events:

**Timeline Pattern:**
```
{Event} during {phase} caused {consequence}.
```
Example: `Data access delays during hackathon caused reduced testing coverage.`

**Scope Pattern:**
```
{Feature/scope item} was {deferred/reduced} due to {reason}.
```
Example: `CRM integration was deferred due to API availability constraints.`

**Quality Pattern:**
```
{Data/system} quality issues discovered: {specific detail}.
```
Example: `Product data quality issues discovered: 15% of SKUs missing category labels.`

### Right Column — "What Risks Do We See"

Template patterns for anticipated risks:

**Data Risk Pattern:**
```
{Data source} may have {quality/availability issue} — mitigation: {action}.
```
Example: `Historical email data may have inconsistent formatting — mitigation: build flexible parser.`

**Integration Risk Pattern:**
```
{System} integration could be delayed by {dependency} — mitigation: {action}.
```
Example: `ERP integration could be delayed by IT resource availability — mitigation: parallel workstreams.`

**Adoption Risk Pattern:**
```
User adoption may be slower than expected — mitigation: {action}.
```
Example: `User adoption may be slower than expected — mitigation: involve end-users from Sprint 2.`

**Scope Risk Pattern:**
```
Scope creep from {source} — mitigation: {action}.
```
Example: `Scope creep from additional use cases — mitigation: strict sprint backlog governance.`

### Standard Risk Patterns for AI Projects

These risks apply to most AI kick-off projects:

```
- Data quality gaps may require additional cleansing effort
- Model accuracy may not meet expectations on first iteration — plan for tuning sprints
- Integration with legacy systems may surface undocumented constraints
- End-user trust in AI recommendations requires gradual onboarding
- Resource availability on client side may fluctuate during project
```

### Example

```
WHAT ALREADY HAPPENED:
- Data access took 2 weeks longer than planned during hackathon
- Product catalog had 15% missing category labels — required manual enrichment
- CRM API rate limits discovered during initial testing

WHAT RISKS DO WE SEE:
- Historical data quality may require additional cleansing before Sprint 2
- ERP integration could surface undocumented business rules — mitigation: early IT alignment
- User adoption may need extra onboarding effort — mitigation: co-design sessions in Sprint 3
```

### Key Rules

- Be honest about what happened — this builds trust with the client
- Every risk in the right column should have a mitigation action
- Use em-dash (—) to separate risk from mitigation
- 2-4 bullets per column; keep each bullet under 20 words
- Avoid catastrophizing — frame risks as manageable with proper planning
- Include at least one non-technical risk (adoption, resources, scope)
- Do NOT list risks that are already fully resolved — those belong in "What Already Happened"
- Risks should be specific to THIS project, not generic AI risks

---

## 8. Participants / Meetings

**Word budget:** Varies — structured content
**Tone:** Organized, clear, action-oriented
**Placement:** Collaboration section

### Participant Types

| Meeting Type | Frequency | Typical Participants |
|-------------|-----------|---------------------|
| Jour Fixe | WEEKLY | Project leads, developers, client PO |
| IT Alignment | BIWEEKLY | IT architects, system admins, security |
| Steering Committee | MONTHLY | Sponsors, department heads, project leads |
| Testing / UAT | AS NEEDED | End-users, QA, product owner |

### Meeting Card Format

```
┌──────────────────────────────┐
│  {MEETING_TYPE}              │
│  DAY: {Weekday}              │
│  TIME: {HH:MM} - {HH:MM}    │
│  FREQUENCY: {WEEKLY/etc.}    │
│  PARTICIPANTS: {List}        │
└──────────────────────────────┘
```

### Frequency Labels (EN)

| Label | Meaning |
|-------|---------|
| WEEKLY | Every week |
| BIWEEKLY | Every two weeks |
| FORTNIGHTLY | Every two weeks (alternative) |
| MONTHLY | Once per month |
| AS NEEDED | On demand |

### Example

```
┌──────────────────────────────┐     ┌──────────────────────────────┐
│  JOUR FIXE                   │     │  IT ALIGNMENT                │
│  DAY: Tuesday                │     │  DAY: Thursday               │
│  TIME: 10:00 - 10:30         │     │  TIME: 14:00 - 15:00         │
│  FREQUENCY: WEEKLY           │     │  FREQUENCY: BIWEEKLY         │
│  PARTICIPANTS:               │     │  PARTICIPANTS:               │
│  - Project Lead (1000)       │     │  - IT Architect (Client)     │
│  - Product Owner (Client)    │     │  - DevOps Lead (1000)        │
│  - Developer (1000)          │     │  - Security Officer (Client) │
└──────────────────────────────┘     └──────────────────────────────┘

┌──────────────────────────────┐     ┌──────────────────────────────┐
│  STEERING COMMITTEE          │     │  TESTING / UAT               │
│  DAY: First Wednesday/month  │     │  DAY: As scheduled           │
│  TIME: 15:00 - 16:00         │     │  TIME: Varies                │
│  FREQUENCY: MONTHLY          │     │  FREQUENCY: AS NEEDED        │
│  PARTICIPANTS:               │     │  PARTICIPANTS:               │
│  - Project Sponsor (Client)  │     │  - End-users (Client)        │
│  - Department Head (Client)  │     │  - QA Lead (1000)            │
│  - Project Lead (1000)       │     │  - Product Owner (Client)    │
└──────────────────────────────┘     └──────────────────────────────┘
```

### Key Rules

- Each meeting type gets its own card
- All cards use the same format: DAY / TIME / FREQUENCY / PARTICIPANTS
- Frequency labels are UPPERCASE
- Participant names use role format: "Role (Organization)"
- Include both client-side and 1000-side participants
- Jour Fixe is always included — it is the primary sync meeting
- Steering Committee is always included for sponsor visibility
- IT Alignment is included when technical integration is involved
- Testing/UAT is included when end-user validation is planned
- Do NOT overload cards with too many participants (3-5 per meeting)

---

## 9. Discussion

**Word budget:** 10-15 words (static content)
**Tone:** Open, inviting
**Placement:** Near-end slide

### Template

```
OTHER TOPICS / DISCUSSION

What other questions, concerns, or ideas should we address today?
```

### Key Rules

- This is a mostly static slide — minimal text
- Title is always "OTHER TOPICS / DISCUSSION"
- Include one open-ended prompt to invite conversation
- Do NOT pre-populate with specific discussion topics
- This slide exists to create space for unplanned conversation
- Keep the prompt short and open-ended

---

## 10. Check-Out / Thank You

**Word budget:** 20-30 words
**Tone:** Warm, appreciative, forward-looking
**Placement:** Final slide

### Template

```
THANK YOU!!

How do you feel after the kick-off?
```

### Alternative Check-Out Patterns

```
THANK YOU!!
What is your key takeaway from today?
```

```
THANK YOU!!
On a scale of 1-5, how confident do you feel about this project?
```

```
THANK YOU!!
What is one thing you are looking forward to in this project?
```

### Key Rules

- "THANK YOU!!" is always uppercase with double exclamation
- Include exactly one feedback/check-out question
- The question should be reflective and forward-looking
- Do NOT make it too formal — this is a closing moment
- Do NOT add next steps here — those belong in the Timeline or Sprint Goals slides
- Keep it brief and positive

---

## Em-Dash Pattern Summary

Use em-dashes (---) to separate titles from descriptions in structured content. This creates clarity and visual rhythm.

**Where to use em-dashes:**
- Phase descriptions: "MVP — Deliver working prototype from hackathon"
- Sprint titles: "Foundation & Data — Build pipelines and establish baselines"
- Risk items: "Data quality gaps — mitigation: additional cleansing sprint"
- Pain points: "Manual matching — 20 minutes per inquiry with no automation"

**Em-dash examples:**
```
OK  Phase 1: MVP — Deliver working prototype covering core matching logic.
OK  Data quality gaps may require cleansing — mitigation: dedicated Sprint 1 task.
OK  User adoption may be slower than expected — mitigation: co-design sessions.

BAD Phase 1: MVP. Deliver working prototype covering core matching logic.
BAD Phase 1: MVP: Deliver working prototype covering core matching logic.
```

**Em-dash formatting in Markdown:**
```
- Title — description text continues here
- Another — description text here
```

---

## Confidence Scoring & `[To be confirmed]` Markers

Every section should have confidence scores calculated. Use `[To be confirmed]` for borderline (60-74%) or low (<60%) confidence items.

**When to use `[To be confirmed]`:**
- A metric is mentioned in source material but not exact
- A system or API is mentioned but not confirmed
- A timeline or deliverable depends on external factors
- Data availability is assumed but not verified
- Meeting schedules or participants are tentative

**Example:**
```
High confidence (85%+):
Sprint 1 delivers data pipeline and accuracy baseline.

Medium confidence (60-74%):
ERP API endpoint for live product data [To be confirmed: requires IT alignment]

Low confidence (<60%):
Release date target: July 2026 [To be confirmed: depends on integration complexity]
```

**In the presentation:**
- High confidence items: Include without caveat
- Medium confidence items: Include with `[To be confirmed]` marker; resolve during Sprint 1
- Low confidence items: Mark and ask the user to verify during kick-off discussion

---

## Checklist: Content Quality

Before generating any slide, check:

- [ ] Every metric traces to source material
- [ ] Parallel structure enforced (all bullets start same way)
- [ ] Power verbs used for action items and deliverables
- [ ] Em-dashes used for structured descriptions
- [ ] Client terminology used (not generic terms)
- [ ] No invented details or aspirational claims
- [ ] Word budget respected
- [ ] Tone appropriate for kick-off audience (collaborative, not sales-pitch)
- [ ] Confidence score calculated
- [ ] Actionable and specific (not vague)
- [ ] Sprint goals traceable to sprint design plan
- [ ] Risks include mitigations
- [ ] Timeline aligns with sprint goals
