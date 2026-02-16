# Section Templates — English

Writing patterns, word budgets, and style guidance for each slide's content in the hackathon presentation.

---

## General Writing Principles

1. **Presentation slides, not paragraphs** — Every bullet should be scannable in 2-3 seconds
2. **Active voice** — "Parse incoming inquiries" not "Incoming inquiries are parsed"
3. **Client vocabulary** — Use their terminology (SP numbers, not "product codes")
4. **Specific over generic** — "~50 quotations per day" not "many quotations"
5. **No filler** — Cut "In order to", "It is important to note that", "As mentioned above"
6. **Parallel structure** — If first bullet starts with a verb, all bullets start with verbs
7. **Em-dashes for technical content** — Format as "Title — description" in challenges, approach, and system landscape
8. **Metrics from source material only** — No invented numbers; use `[To be confirmed]` if uncertain
9. **Honest but constructive** — Acknowledge challenges without defeatism
10. **Audience-focused** — Every slide answers: "Why should I care?"

---

## Power Verbs List

Use these action verbs to start approach steps, lessons learned, and next steps. They convey energy and clarity:

**Data & Parsing:**
- Parse, Extract, Ingest, Capture, Import, Read, Scan, Recognize

**Matching & Classification:**
- Map, Match, Classify, Categorize, Link, Associate, Route, Assign

**Generation & Creation:**
- Generate, Create, Build, Synthesize, Compose, Produce, Construct, Draft

**Validation & Quality:**
- Validate, Verify, Audit, Review, Check, Confirm, Reconcile, Test

**Process & Flow:**
- Execute, Process, Transform, Route, Escalate, Submit, Approve, Publish

**Learning & Optimization:**
- Optimize, Refine, Enhance, Improve, Iterate, Adjust, Tune, Calibrate

**Integration & Communication:**
- Integrate, Connect, Sync, Communicate, Notify, Alert, Deliver, Transmit

**Examples:**
- "Parse incoming emails" (not "Read emails")
- "Map customer IDs to CRM records" (not "Associate customer IDs")
- "Generate draft quotations" (not "Create quotations")
- "Validate pricing against regional policies" (not "Check pricing")

---

## Parallel Structure Rules

**Rule**: If the first element in a list starts with a verb, ALL must start with verbs. Same for nouns, adjectives, or prepositional phrases.

**Bad example (mixed):**
```
- Parse incoming emails
- Extract product requirements
- System maps products to catalog
```

**Good example (parallel verbs):**
```
- Parse incoming emails
- Extract product requirements
- Map products to catalog
```

**Bad example (mixed):**
```
01: Faster Turnaround
02: Strategic Time Use
03: Building AI Skills
```

**Good example (parallel nouns):**
```
01: Faster Turnaround
02: Strategic Time Use
03: Enhanced AI Capability
```

---

## Check-in Questions

**Word budget:** 30 words total (3 questions)
**Tone:** Conversational, inviting
**Placement:** Slide 2 (Bullet Points Ash)

### Standard Questions (Recommended)

```
Who am I?
What comes to my mind when I think of {client_name} and AI?
When is this AI Hackathon a success?
```

### Alternative Questions

```
What excites me most about AI?
What would I automate first at {client_name}?
What does a successful hackathon look like to me?
```

**Do NOT:**
- Make questions too long or formal
- Ask technical questions (this is an icebreaker)
- Use more than 3 questions
- Pre-answer the questions

---

## Pain Points (Slide 5)

**Word budget:** 100 words total, 5-6 bullets
**Each bullet:** 10-20 words, one sentence
**Tone:** Problem-focused but not negative
**Placement:** Slide 5 (Chapter Divider Ash + Text)

### Template Patterns

**Volume/Capacity Pattern:**
```
~{number} {tasks} per {time_period} created manually, tying up {team} capacity.
```
Example: `~50 quotations per day created manually, tying up sales capacity.`

**Format/Channel Pattern:**
```
{Items} in varied formats ({list formats}) requiring manual interpretation.
```
Example: `Enquiries in varied formats (emails, PDFs, portals) requiring manual interpretation.`

**Time Waste Pattern:**
```
Too much time spent on {activity}: {specific_details}.
```
Example: `Too much time spent on data lookup: SP numbers, measurements, materials, stock…`

**Data Quality Pattern:**
```
Incomplete {data_type}, especially for {condition} ({specific_gap}).
```
Example: `Incomplete customer data, especially for new accounts (missing SP numbers).`

**Error/Quality Pattern:**
```
High error rate in {process} to {system}.
```
Example: `High error rate in manual transcription to ERP system.`

**Bottleneck/Constraint Pattern:**
```
{Activity} is a bottleneck: {reason}, causing {consequence}.
```
Example: `Data enrichment is a bottleneck: no automated lookup available, causing 30-minute delays per quote.`

### Key Rules

- Start with the most impactful/quantifiable pain point
- Include at least one metric/number if available from source material
- Use the client's own words and terminology where possible
- Each bullet should be independently understandable
- Do NOT invent metrics — use `[To be confirmed]` if numbers aren't in source
- Mix metric-based and process-based pain points (don't make it all numbers)

---

## Data Sources (Slide 6)

**Word budget:** 80 words total, 3-4 items
**Each item:** Icon + Title + Description (1-2 sentences)
**Tone:** Factual, descriptive
**Placement:** Slide 6 (Chapter Divider Ash + Text)

### Template Pattern

```
{emoji} {Category Title}: {Description of what data is available, format, volume, relevance}
```

### Recommended Icons & Categories

| Data Type | Icon | Examples |
|-----------|------|----------|
| Emails/Messages | 📧 | Customer inquiries, support tickets, newsletters |
| Documents/PDFs | 📄 | Contracts, proposals, specifications, manuals |
| Databases/Tables | 📊 | CRM records, ERP data, product master, historical logs |
| APIs/Systems | 🔗 | REST APIs, SOAP services, middleware connectors |
| Images/Media | 🖼️ | Product photos, diagrams, screenshots, brand assets |
| Customer/People Data | 👥 | Contact lists, employee records, user profiles |
| Product Data | 📦 | Catalog, inventory, SKU data, part numbers |
| Historical Records | 📁 | Archives, past transactions, audit trails |

### Example (Montanstahl)

```
📧 Inquiry emails and PDFs: Real customer inquiries in multiple languages with varying formats and attachments.
📋 Order lifecycle data: Examples from inquiry through order confirmation for 5 suppliers (FIM INOX, INOX CENTER, KORO, PROFILINOX, SIDERTUBI).
📊 Product master data: Product list with SP numbers, measurements, materials, and the standard order process documentation.
```

### Key Rules

- Only list data that actually exists and is accessible
- Mention specific formats (PDF, Excel, email, API, database) and approximate volume (if known)
- If data availability is uncertain, mark with `[To be confirmed]`
- Include supplier/system names if mentioned in source material
- Focus on what data supports the PoC, not all available data

---

## Data Screenshots (Slide 7)

**Word budget:** 0 words (images only)
**Tone:** Visual demonstration
**Placement:** Slide 7 (Title Ash + small Image)

### Content Guidelines

- This is an IMAGE-ONLY slide
- User adds 3-7 screenshots of actual data files, emails, documents
- No text content needed — the images speak for themselves
- Gray placeholder boxes indicate where images go
- Critical for proving data actually exists and is available

### What to Capture

1. **Sample inquiry email** — Show the format, language variation, attachments
2. **Product master data** — Screenshot of the ERP or database with product information
3. **Customer database record** — Show customer contact data, purchase history, order examples
4. **Process document** — Workflow diagram, ordering process, specification template
5. **Output example** — Current quotation format or order confirmation template
6-7. **Additional context** — Any other relevant data format (forms, spreadsheets, API responses)

### Key Rules

- Use real, anonymized data (not mock data)
- Avoid sensitive information (financial data, personal IDs)
- High enough quality to read text (screenshots, not photos)
- Represent the actual variety in data (multiple formats, languages if applicable)

---

## System Landscape (Slide 8)

**Word budget:** 100-150 words total
**Tone:** Technical, factual
**Placement:** Slide 8 (DEFAULT layout with card-based content)
**NEW slide** in expanded structure

### Template Pattern: Card-Based Layout

```
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│   ERP SYSTEM        │  │   CRM SYSTEM        │  │   CLOUD INFRA       │
│   {System Name}     │  │   {System Name}     │  │   {Provider} ({svcs}│
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│   KEY APIs & INTEGRATIONS                                               │
│   - {API/System} → {Purpose}                                            │
│   - {API/System} → {Purpose}                                            │
│   - {Integration Pattern} (real-time/batch)                             │
│   - {Constraints or Special Requirements}                               │
└─────────────────────────────────────────────────────────────────────────┘
```

### Content Guidelines by Card

**ERP (Enterprise Resource Planning):**
- Name the actual system (SAP S/4HANA, Oracle EBS, NetSuite, etc.) or "[To be confirmed]"
- Include key modules if relevant (Finance, Procurement, Manufacturing, etc.)
- Version/release if known (e.g., "SAP S/4HANA 2023")

**CRM (Customer Relationship Management):**
- Name the actual system (Salesforce Sales Cloud, Microsoft Dynamics 365, Pipedrive, etc.) or "[To be confirmed]"
- Include modules if relevant (Opportunities, Accounts, Leads, etc.)
- Note if custom or out-of-box

**Cloud Infrastructure:**
- Cloud provider (AWS, Microsoft Azure, Google Cloud, on-premise) or "[To be confirmed]"
- Key services (EC2, Lambda, RDS for AWS; App Service, CosmosDB for Azure, etc.)
- Data residency or compliance notes if relevant (e.g., "GDPR-compliant EU region")

**Key APIs & Integrations:**
- List 2-4 critical integration points
- Include direction and purpose (e.g., "SAP OData API → fetch quotation master data")
- Mention specific endpoints if known (e.g., "/api/quotations/v2")
- Note if APIs are RESTful, SOAP, GraphQL, or proprietary
- Describe integration pattern: real-time sync, batch ingestion, webhooks, message queue, etc.

**Constraints or Technical Notes:**
- Legacy system attachments or limitations
- Latency requirements (e.g., "real-time sync required for <1min turnaround")
- Security/compliance constraints (authentication, encryption, audit logging)
- Known performance issues or data quality concerns
- Any third-party middleware or integration platform (e.g., MuleSoft, Zapier)

### Example (Montanstahl)

```
ERP: SAP S/4HANA (Finance & Procurement)
CRM: Salesforce Sales Cloud
Cloud Infrastructure: AWS (EC2, Lambda, RDS)
Key APIs:
- SAP OData API → quotation master data, product catalogs, pricing rules
- Salesforce REST API → opportunities, accounts, leads
- Custom REST API → document upload and processing
- Integration pattern: Real-time sync via API Gateway + Lambda; batch ingestion for historical data
Constraints: Legacy mainframe attachment for historical data; real-time sync required for <1min turnaround; GDPR compliance for EU customers
```

### Key Rules

- Be specific with system names and versions (not "we use SAP")
- Only list systems/APIs that are actually used or planned for the PoC
- If a system is unknown, use "[To be confirmed]" — do NOT guess
- Order: input → processing → output (follow data flow)
- Include constraints that affect the approach or challenges (latency, compliance, legacy systems)

---

## Approach Steps (Slide 9)

**Word budget:** 80 words total, 4-5 steps
**Each step:** Verb-led title + brief description
**Tone:** Action-oriented, capability-focused
**Placement:** Slide 9 (Chapter Divider Ash + Text)

### Template Pattern

```
{Action verb}ing: {What the system does} from/to/using {specifics}.
```

### Common Approach Patterns

**Data Ingestion Step:**
```
{Input} parsing: Extract structured data from {sources}...
```
Example: `Inquiry parsing: Extract structured data from emails, PDFs, and web forms…`

**Enrichment/Lookup Step:**
```
{Entity} enrichment: Lookup and add {missing_context} from {data_source}.
```
Example: `Customer enrichment: Lookup customer ID and account history from CRM.`

**Matching/Classification Step:**
```
{Entity} mapping: Match {input} to {catalog/database} using {identifiers}.
```
Example: `Product mapping: Match requested products to our catalog using SP numbers and measurements.`

**Generation/Output Step:**
```
{Output} generation: Create standardized {output_type} with {key_fields}.
```
Example: `Quotation generation: Create standardized quotations with pricing, lead times, and terms.`

**Validation/Clarification Step:**
```
Clarification automation: {Detect/Request} missing information and {action}.
```
Example: `Clarification automation: Detect missing customer info and request via email template.`

**Approval/Delivery Step:**
```
{Output} delivery: Route to {destination} with {approval_condition}.
```
Example: `Quote delivery: Send to sales team for 1-click approval or manual editing.`

### Example (Montanstahl)

```
Inquiry parsing: Extract structured data from emails, PDFs, and web forms…
Product mapping: Match requested products to our catalog using SP numbers and measurements.
Quotation generation: Create standardized quotations with pricing and lead times.
Clarification automation: Request missing information and guide customers through the sales process.

Optional clarification question:
Do we need customer data validation? Verify customer information and match with lifecycle examples.
```

### Key Rules

- Order from data input → processing → output → validation
- Use the client's process terminology (not generic "data processing")
- Keep each step focused on one capability
- Don't describe implementation details (no "using Azure OpenAI" or "via REST API")
- The approach should directly address pain points — map each pain to at least one approach step
- Use power verbs from the list above
- Maintain parallel structure (all steps start with verb-ing)
- Optional: Add ONE clarification question at the end to engage audience

---

## Challenges (Slide 10)

**Word budget:** 120 words total, 4-5 challenges
**Each challenge:** Title + em dash + description (15-25 words)
**Tone:** Honest, constructive
**Placement:** Slide 10 (Chapter Divider Ash + Text)

### Template Pattern

```
{Challenge title} — {Specific description of why this is challenging for this use case}.
```

### Common Challenge Categories

**Data Quality:**
```
Unstructured data formats — {specifics about format variety and parsing difficulty}.
```
Example: `Unstructured data formats — Emails, PDFs, and web forms vary widely in structure and content density.`

**Data Completeness:**
```
Incomplete or inconsistent {data_type} — Especially for {condition}, {details} can be {problem}.
```
Example: `Incomplete or inconsistent customer data — Especially for new customers, SP numbers and specifications can be missing or use non-standard naming conventions.`

**Accuracy Requirements:**
```
{Domain} matching accuracy — {Matching/classifying} {items} to the correct {target} demands high precision.
```
Example: `Product catalog matching accuracy — Mapping customer requests to the correct standard profile in the catalog demands high precision.`

**Integration Complexity:**
```
System integration timing — {System/API} has {issue}, causing {consequence}.
```
Example: `System integration timing — SAP OData queries return stale pricing data during peak hours, causing quotation inaccuracy.`

**Edge Cases:**
```
Edge cases and exceptions — Not every {item} fits the "{standard}" pattern; the system needs to detect when human intervention is required.
```
Example: `Edge cases and exceptions — Not every inquiry fits the "standard product" pattern; system must reliably detect when human intervention is required.`

**Adoption/Trust:**
```
User adoption and trust — {Team} needs to trust AI-generated {outputs} enough to use them.
```
Example: `User adoption and trust — Sales teams need to trust AI-generated quotation drafts enough to use them without extensive review.`

**Regulatory/Compliance:**
```
Regulatory requirements — {Outputs} must comply with {policy/regulation}, which {constraint}.
```
Example: `Regulatory requirements — Quotation pricing must comply with regional discount policies, which limits AI flexibility.`

### Example (Montanstahl)

```
Unstructured data formats — Emails, PDFs, portals, and web forms vary widely in structure.
Incomplete or inconsistent customer data — Especially for new customers, SP numbers and specifications can be missing, incorrect, or use non-standard naming conventions.
Product catalog matching accuracy — Mapping customer requirements to the correct standard profile in the catalog demands high precision.
Edge cases and exceptions — Not every inquiry fits the "standard product" pattern; the system needs to reliably detect when human intervention is required.
User adoption and trust — Sales teams need to trust AI-generated quotation drafts enough to use them.
```

### Key Rules

- Be honest about real challenges, not hypothetical ones
- Every challenge should be addressable (not show-stoppers)
- Include at least one non-technical challenge (adoption, trust, change management)
- Use em-dash (—) not hyphen (-) between title and description
- These set realistic expectations for what the hackathon may or may not solve
- Frame challenges as learning opportunities, not failures
- Maintain parallel structure in descriptions

---

## Business Value (Slide 17)

**Word budget:** 90 words total, exactly 3 items
**Each item:** Number + Title + Description (1-2 sentences)
**Tone:** Strategic, outcome-focused
**Placement:** Slide 17 (Table of Contents small)

### Template Pattern

```
{Number}: {Value Driver Title}
{Concrete description} — {impact metric or qualitative benefit}.
```

### Common Value Drivers

**Efficiency/Speed:**
```
Faster {Process} Turnaround
Reduce average {metric} from {current} to {target} — {business impact}.
```
Example: `Faster Quotation Turnaround. Reduce average response time from days to hours – winning more competitive deals.`

**Capacity/FTE:**
```
Strategic Use of Time
~{number} FTE freed from {manual_work} to focus on {high-value_tasks} — {strategic benefit}.
```
Example: `Strategic Use of Time. ~1 FTE freed from manual quotation work to focus on complex projects and key account management – Strengthening customer relationships.`

**Capability/Skill Development:**
```
AI Skill Development
Enhancing AI competency across {client_name} — {teams affected}.
```
Example: `AI Skill Development. Enhancing AI competency across Montanstahl – operations and IT teams gain hands-on experience with AI-driven automation.`

**Revenue/Market Impact:**
```
Revenue Opportunity
{Enabler} unlocks {opportunity} — {financial or strategic outcome}.
```
Example: `Revenue Opportunity. Faster quotations enable entry into high-volume, low-margin markets – expanding total addressable market.`

**Quality/Compliance:**
```
Accuracy & Compliance
{Improvement} aligns with {standard} — {consequence}.
```
Example: `Accuracy & Compliance. AI-generated quotes align with regional policies 100% of the time – eliminates discount overrides and compliance violations.`

### Example (Montanstahl)

```
01: Faster Quotation Turnaround
Reduce average response time from days to hours – winning more competitive deals and faster sales cycles.

02: Strategic Use of Time
~1 FTE freed from manual quotation work to focus on complex projects and key accounts – Strengthening customer focus and relationships.

03: AI Skill Development
Enhancing AI competency across Montanstahl – operations and IT teams gain hands-on experience with AI-driven automation and AI-guided decision-making.
```

### Key Rules

- Use ONLY metrics from source material
- If no specific metrics available, describe qualitative benefits
- Exactly 3 items (OT standard format)
- Each should address a different stakeholder concern (CFO cares about cost, operations cares about time, CEO cares about capability)
- Avoid generic phrases like "improved efficiency" — be specific
- Use em-dash (—) to connect impact to outcome
- Numbers should be from the Approach/PoC scope (not invented)

---

## Key Metrics (Slide 18)

**Word budget:** 120 words total
**Tone:** Data-driven, factual
**Placement:** Slide 18 (DEFAULT card-based layout)
**NEW slide** in expanded structure

### Template Pattern: Three Card Sections

```
┌─────────────────────────────────────────┐
│   PoC Test Results                      │
│   {X} {items} tested                    │
│   {Y}/{X} passed without manual rework  │
│   {Z}% first-pass accuracy              │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│   Time to Production                    │
│   Phase 1 ({focus}): {weeks} weeks      │
│   Phase 2 ({focus}): {weeks} weeks      │
│   Phase 3 ({focus}): {weeks} weeks      │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│   Estimated ROI                         │
│   Annual {metric}: ~{number} hours      │
│   Value: ${amount}/year @ ${rate}/hr    │
│   Payback period: {months} months       │
└─────────────────────────────────────────┘
```

### Card 1: PoC Test Results

**What was tested?**
- Number of samples: "50 historical quotations", "100 customer inquiries", etc.
- Accuracy metric: "88% first-pass accuracy", "44/50 passed without rework", etc.
- Scope note: "Tested with product category A and B only; category C to follow"

**Key Rules:**
- Use ONLY numbers from actual test data
- Include caveat: "Tested with {sample_size}; production may vary"
- Focus on the most impressive metric (highest accuracy, fastest processing time, etc.)

**Example:**
```
PoC Test Results
50 historical quotations tested
44/50 passed without manual rework
88% first-pass accuracy
(Tested with standard product profiles; custom products to be retested)
```

### Card 2: Time to Production (Phased Roadmap)

**Phases:**
- **Phase 1 (Validation & Refinement):** 4 weeks — Test with live data, iterate based on feedback
- **Phase 2 (Integration & Testing):** 6 weeks — Full ERP integration, end-to-end testing
- **Phase 3 (Rollout & Support):** 2-4 weeks — Phased rollout to sales team, monitoring, optimization

**Key Rules:**
- Be realistic with timelines (not overly optimistic)
- Each phase should have a clear deliverable/gate
- Total timeline: typically 3-4 months from PoC to production
- Include dependency notes if any (e.g., "Phase 1 requires SAP team availability")

**Example:**
```
Time to Production
Phase 1 (Data Refinement): 4 weeks
Phase 2 (ERP Integration): 6 weeks
Phase 3 (Sales Rollout): 2 weeks
Total: 12 weeks to production
```

### Card 3: Estimated ROI

**FTE Savings:**
- Current state: "~200 minutes per day on manual quotation creation"
- PoC state: "~20 minutes per day (85% time savings)"
- Annual: "~1,200 hours @ $75/hr = $90k/year"

**Cost Avoidance:**
- Pricing errors: "~$50k/year in missed margin from manual errors"
- Compliance violations: "~$200k/year in discount overrides"

**Revenue Enablement:**
- Faster response enables higher deal volume
- Market expansion (new customer segments)
- Competitive advantage (shorter quote turnaround)

**Payback Period:**
- PoC investment + Phase 1-2 development costs ÷ annual benefit = payback
- Example: "$200k investment ÷ $90k/year benefit = 2.2 year payback"

**Key Rules:**
- Use realistic hourly rates (industry or provided by client)
- Include one caveat: "Assumes current manual process continues; actual savings depends on adoption"
- Frame in terms the business cares about (cost, time, revenue)
- Be conservative rather than optimistic

**Example:**
```
Estimated ROI
Annual FTE savings: ~1,200 hours @ $75/hr = $90k/year
Payback period: 4-6 months post-go-live (assuming Phase 1-2 investment of $300k)
Ongoing benefit: $90k+/year with minimal maintenance overhead
Assumption: Assumes sales team achieves 80%+ adoption in first 6 months
```

### Key Rules

- All numbers must be from test results, not estimates
- Include disclaimer for all projections (Phase timeline, ROI)
- Focus on metrics the client cares about (not technical metrics like "API response time")
- Use realistic numbers, even if less impressive
- If a metric is uncertain, mark with `[To be confirmed]`

---

## PoC Summary (Slide 19)

**Word budget:** 60 words total
**Intro:** 1 sentence (10-15 words)
**Features:** 4-6 bullet points (5-10 words each)
**Tone:** Achievement-focused, concrete
**Placement:** Slide 19 (DEFAULT text-focused)

### Template

```
Intro: "We have built a proof of concept (PoC) that enables us to:"
Features:
- {Verb} incoming {items}
- {Verb} {data type}
- {Verb} them to {target}
- {Verb} draft {outputs}
- {Verb} the {output} to {destination}
- [And more...]
```

### Example (Montanstahl)

```
We have built a proof of concept (PoC) that enables us to:
- Parse incoming customer inquiries from multiple formats
- Extract product requirements and customer information
- Map them to the product catalog automatically
- Generate draft quotations with pricing and lead times
- Send the offer to the customer with approval tracking
- And more...
```

### Key Rules

- Only list capabilities that were actually demonstrated in the hackathon
- Use simple, clear verbs (Parse, Extract, Map, Generate, Send, Validate, etc.)
- Order follows the data flow (input → process → output)
- "And more..." is optional but shows there's additional potential
- 4-6 features is the sweet spot (enough to show scope, not overwhelming)
- Each bullet should be one action, not compound (not "Extract and validate")

---

## Demo Walkthrough (Slide 21)

**Word budget:** 50 words total
**Tone:** Engaging, step-by-step
**Placement:** Slide 21 (DEFAULT with image + description)
**NEW slide** in expanded structure

### Template

```
{Demonstration intro}: {First action} → {Processing} → {Output} in {time metric}.
{Details about what the AI shows}: {How it explains or proves the capability}.
{User action}: {What happens next in the workflow}.
```

### Example (Montanstahl)

```
Live walkthrough: An incoming customer email is transformed into a formatted quote ready for send in under 90 seconds. Watch how the AI extracts product specifications, maps to our catalog, and calculates pricing based on customer history. Sales team can accept, edit, or request a revised quote with one click.
```

### Key Rules

- 2-3 sentences maximum
- Walk through the main flow: input → processing → output
- Highlight the most impressive or surprising result
- Include timing if applicable (e.g., "under 90 seconds")
- Focus on what the user sees and does, not backend processing
- Be concrete ("click the email" not "interact with the system")
- Emphasize the time savings or capability gain

---

## Lessons Learned (Slide 23)

**Word budget:** 100 words total, 3-5 lessons
**Each lesson:** 1-2 sentences, focused on a single insight
**Tone:** Honest, constructive, forward-looking
**Placement:** Slide 23 (DEFAULT text-focused)
**NEW slide** in expanded structure

### Template Pattern

```
{Area}: {What surprised/challenged you} — {How this will inform Phase 1}.
```

### Common Lesson Categories

**Technical Discoveries:**
```
{System/technology} is harder/easier than expected — {Specific finding about performance, integration, or capability}.
Implication for Phase 1: {How this will change approach or prioritization}.
```
Example: `Email parsing is harder than expected — SAP OData queries return stale pricing data during peak hours. Implication: Phase 1 will include caching layer for master data.`

**Team Process Insights:**
```
{Activity} engagement is critical — {What worked well or what surprised you about collaboration}.
Implication for Phase 1: {How this will shape team structure or communication}.
```
Example: `Sales team engagement early is critical — We showed draft UI to 3 sales managers and got invaluable feedback on approval workflow. Implication: Phase 1 will include user co-design sessions weekly.`

**Data Quality Discoveries:**
```
Data quality varies more than expected — {Specific gaps or patterns found during testing}.
Implication for Phase 1: {How this will change data preparation or validation strategy}.
```
Example: `Data quality varies more than expected — New customers often lack complete product specifications; error rate ~15%. Implication: Phase 1 will add data cleansing rules and customer education.`

**Regulatory/Compliance Discoveries:**
```
Regulatory review should happen in parallel — {What compliance issue was discovered too late}.
Implication for Phase 1: {How Phase 1 will prevent this}.
```
Example: `Regulatory review should happen in parallel — Discount policy conflicts discovered late in development. Implication: Phase 1 will include compliance review gates at weeks 2 and 6.`

**Scope/Timeline Discoveries:**
```
{Feature} will take longer than expected — {Reason discovered during PoC}.
Implication for Phase 1: {How timeline or scope will adjust}.
```
Example: `Customer data enrichment will take longer than expected — CRM lookups are inconsistent and require manual validation. Implication: Phase 1 will prioritize core quotation features; customer enrichment moved to Phase 2.`

### Key Rules

- Be honest: what surprised you? What was harder than expected?
- Include both technical and process learnings (not just tech)
- Frame as forward-looking: "What did we learn that will make Phase 1 better?"
- Avoid blaming or negative tone — frame as learning, not failure
- Each lesson should be specific and actionable (not generic like "communication is important")
- Include implication or recommendation for Phase 1
- Use em-dash (—) to separate lesson from implication

### Example (Montanstahl)

```
Email parsing is harder than expected — SAP OData queries return stale pricing data during peak hours. Phase 1 will include caching layer.

Sales team engagement early is critical — Showed draft UI to 3 sales managers, got valuable feedback on approval workflow. Phase 1 will include weekly user co-design.

Regulatory review should happen in parallel — Discount policy conflicts discovered late in development. Phase 1 includes compliance gates at weeks 2 and 6.

Data quality varies more than expected — New customers often lack complete product specifications. Phase 1 will add data cleansing rules.
```

---

## What's Next (Slide 24)

**Word budget:** 80 words total, 2-4 next steps
**Tone:** Forward-looking, action-oriented
**Placement:** Slide 24 (Chapter Divider Ash + Text)

### Template Pattern

```
1. {Action verb} {deliverable} — {Specific detail/timeline}.
2. {Action verb} {activity} with {stakeholder} — {Specific detail/timeline}.
3. [Optional] {Specific refinement} based on {PoC finding}.
4. [Optional] {Governance/enablement activity}.
```

### Standard Next Steps (Always Include)

**Step 1: Debrief Document**
```
Publish hackathon debrief document summarizing PoC scope, test results, and refinement roadmap.
```

**Step 2: Phase 1 Kickoff**
```
Schedule Phase 1 kickoff meeting with {client_name} technical team (target: {date}, {duration}).
```

### Optional Additional Steps (Choose Based on PoC Results)

**Data Quality Refinement:**
```
Refine data quality rules based on test results; establish SLA for quote turnaround (target: <60 minutes).
```

**Governance Setup:**
```
Define governance: who approves AI pricing? What is the escalation policy for edge cases?
```

**Team Enablement:**
```
Prepare user training materials and test script for sales team pilot (Phase 1 week 2).
```

**Technical Preparation:**
```
Document API integration requirements and begin SAP/CRM sandbox environment setup.
```

**Business Alignment:**
```
Secure budget approval for Phase 1 development and Phase 2 production deployment.
```

**Phased Rollout Plan:**
```
Define rollout phases: pilot with 1 sales region, then expand to full team by {target_date}.
```

### Example (Montanstahl)

```
Publish hackathon debrief document summarizing PoC scope, test results, and Phase 1 roadmap.
Schedule Phase 1 kickoff meeting with Montanstahl technical team (target: February 24, 2025; 2 hours).
Refine data quality rules based on test results; establish SLA for quote turnaround (target: <60 minutes).
Define governance: who approves AI-generated pricing? escalation policy for edge cases?
```

### Phased Roadmap Pattern (Alternative)

If the team wants to show a longer-term roadmap, use this pattern:

```
Phase 1 (Validation, 4 weeks): Data refinement, live testing, UX iteration
Phase 2 (Integration, 6 weeks): Full ERP connection, approval workflow, API hardening
Phase 3 (Rollout, 2-4 weeks): Sales team training, pilot with 1 region, monitoring and optimization

Launch target: {Month/Year}
```

### Key Rules

- Always include the debrief document as the first next step
- Always include a follow-up meeting with a specific date
- Keep it to 2-4 items maximum — this is a closing slide, not a project plan
- Be specific with dates, stakeholders, and deliverables
- Each should be a concrete task, not aspirational
- Link to PoC findings (e.g., "Based on data quality issues found, Phase 1 will include…")
- Use action verbs (Publish, Schedule, Refine, Define, Prepare, Secure, etc.)

---

## Thanks (Slide 25)

**Word budget:** 40 words total
**Format:** Two columns: OT Team and Client Team
**Tone:** Appreciative, collaborative
**Placement:** Slide 25 (Bullet Points Ash)

### Template

```
{Client Name} Team:
- Name (Title)
- Name (Title)
- Name (Title)

One Thousand Team:
- Name (Role)
- Name (Role)
- Name (Role)
```

### Example (Montanstahl)

```
Montanstahl Team:
- Florian Rösch (Head of Operations)
- Daniela Meier (Sales Director)
- Stefan Keller (IT Manager)

One Thousand Team:
- Alice Chen (AI Architect)
- Bob Mueller (Solutions Engineer)
- Carol Zhang (Product Lead)
```

### Key Rules

- Client Team: List titles (Head of Operations, Sales Director, IT Manager, etc.)
- OT Team: List roles (AI Architect, Solutions Engineer, Product Lead, Project Manager, etc.)
- Include 3-5 people per side (top contributors or decision-makers)
- Use formal names + title format ("Name (Title)")
- Format as simple bullet lists under each heading
- Optional: Add client logo or team photos at the bottom (user-supplied images)

---

## Em-Dash Pattern Summary

Use em-dashes (—) to separate titles from descriptions in technical content. This creates clarity and visual rhythm.

**Where to use em-dashes:**
- Challenges: "Challenge Title — Description"
- Approach steps: "Step Title — What it does and how"
- System Landscape constraints: "Constraint Title — Why this matters"
- Lessons Learned: "Learning — Implication for Phase 1"

**Em-dash examples:**
```
✓ Unstructured data formats — Emails, PDFs, portals vary widely in structure.
✓ Email parsing is harder than expected — SAP OData queries return stale pricing data during peak hours.
✓ User adoption and trust — Sales teams need to trust AI-generated quotations.

✗ Unstructured data formats. Emails, PDFs, and portals vary widely.
✗ Unstructured data formats: emails, PDFs, portals vary widely.
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
- A metric is mentioned in source material but not exact (e.g., "~50 quotations")
- A system or API is mentioned but not confirmed
- A number or timeline is estimated, not tested
- Data availability is assumed but not verified

**Example:**
```
High confidence (85%+):
~50 quotations per day created manually, tying up sales capacity.

Medium confidence (60-74%):
SAP OData API for quotation master data [To be confirmed: is this the right endpoint?]

Low confidence (<60%):
Phase 1 development will take ~4 weeks [To be confirmed: depends on SAP integration complexity]
```

**In the presentation:**
- High confidence items: Include without caveat
- Medium confidence items: Include with `[To be confirmed]` marker; resolve during Phase 2 content enrichment
- Low confidence items: Mark and ask the user to verify during review phase

---

## Checklist: Content Quality

Before generating any slide, check:

- [ ] Every metric traces to source material
- [ ] Parallel structure enforced (all bullets start same way)
- [ ] Power verbs used for action items
- [ ] Em-dashes used for technical descriptions
- [ ] Client terminology used (not generic terms)
- [ ] No invented details or aspirational claims
- [ ] Word budget respected
- [ ] Tone appropriate for audience (not too casual, not too formal)
- [ ] Confidence score calculated
- [ ] Actionable and specific (not vague)

