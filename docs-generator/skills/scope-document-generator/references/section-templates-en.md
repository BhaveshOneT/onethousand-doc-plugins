# Scope Document Section Templates - English

Professional reference guide for writing each section of a scope document in English. Based on RVT scope document style: partnership-focused, evidence-based, and professional tone.

---

## 1. Initial Context

**Purpose**: Establish the business problem, justify the PoC approach, and demonstrate what was validated during the hackathon.

### Template Patterns

#### Pattern A (Discovery-focused)
"During the hackathon conducted on {{DATE}}, {{CLIENT}} and One Thousand explored {{TOPIC}}. The exploration revealed {{HACKATHON_FINDING}}. This PoC builds on those validated assumptions to deliver a production-ready {{USE_CASE}} solution."

#### Pattern B (Challenge-focused)
"{{CLIENT}} currently faces a significant challenge with {{BUSINESS_PROBLEM}}. This results in {{IMPACT_OF_PROBLEM}}. During the hackathon on {{DATE}}, we demonstrated that {{HACKATHON_FINDING}} can address this gap. This PoC scope outlines how to develop a complete solution for {{USE_CASE}}."

#### Pattern C (Opportunity-focused)
"The hackathon on {{DATE}} with {{CLIENT}} identified an opportunity to {{OPPORTUNITY}}. Our exploration showed that {{HACKATHON_FINDING}}. This PoC will transform that proof-of-concept into a scalable, integrated solution for {{USE_CASE}}."

### Key Phrases to Use
- "During the hackathon, we validated..."
- "The exploration revealed..."
- "This demonstrates the feasibility of..."
- "Building on this foundation, this PoC will..."
- "One Thousand and {{CLIENT}} explored the intersection of..."

### Key Phrases to Avoid
- "We will explore whether..." (suggests uncertainty, not validation)
- "We hope to demonstrate..." (passive, not confident)
- "Allegedly, the system could..." (informal for professional documents)
- Vague references to "requirements" without context

### Structure
1. Opening sentence: What was explored during the hackathon
2. Middle sentences: Key finding from the hackathon, why it matters
3. Closing sentence: How this PoC builds on that foundation

### Variable Placeholders
- `{{CLIENT}}`: Client company name
- `{{DATE}}`: Hackathon date (e.g., "March 15-16, 2024")
- `{{TOPIC}}`: What the hackathon explored (e.g., "AI-powered document classification")
- `{{USE_CASE}}`: The specific use case (e.g., "invoice processing automation")
- `{{HACKATHON_FINDING}}`: Key validated finding (e.g., "a rule-based classifier can accurately categorize documents with 85% accuracy using only the invoice header")
- `{{BUSINESS_PROBLEM}}`: The challenge {{CLIENT}} faces
- `{{IMPACT_OF_PROBLEM}}`: How it affects them (time, cost, quality)

### Length Guidelines (CRITICAL)
- 4–5 sentences maximum across 2 short paragraphs
- 80–120 words total — no more
- Extra source data should make sentences more specific, NOT add more sentences

---

## 2. In-Scope Features

**Purpose**: Describe exactly what will be built, with sufficient detail to be binding.

### Template Patterns

#### Section Header Format
"### 2.1 [Feature Name]"

#### Paragraph Introduction Pattern
"[Feature Name] encompasses the ability to {{ACTION}} by {{METHOD}}. This feature will {{BENEFIT}}. The implementation includes [specific components or integrations]."

#### Multi-part Feature Pattern
"2.1 [Feature Name] will deliver three core capabilities:
- [Capability A]: [one-sentence description]
- [Capability B]: [one-sentence description]
- [Capability C]: [one-sentence description]

The feature includes [additional context]. {{CLIENT}} will be able to [tangible outcome]."

### IMPORTANT: No Deliverables Sub-lists

Do NOT include "Deliverables:" bullet lists under each feature. The 2–3 sentence description is sufficient. Deliverables sub-lists bloat the document and push it beyond the 4–5 page limit.

### Concise Feature Writing Patterns (2–3 sentences each)

#### Data Extraction Feature
"The system extracts text from [document type] using [extraction method] and ingests it into [target]. Custom parsing handles [specific challenge] with minimal information loss."

#### Classification Feature
"[Feature name] automatically categorizes [document type] into [number] categories using [method]. This enables {{CLIENT}} to [workflow improvement]."

#### Chatbot/Conversational Feature
"When a [user role] asks a question, the system identifies the most relevant [information source] via [search method], then generates a natural-language answer using [AI service]. It handles [query types]."

#### Integration Feature
"The [system name] is deployed as a [platform] app using [integration method]. Users [interaction pattern] to ensure focused responses."

### Key Phrases to Use
- "The feature will enable {{CLIENT}} to..."
- "This implementation includes..."
- "Deliverables for this feature are..."
- "The system will automatically..."
- "{{CLIENT}} users can..."

### Key Phrases to Avoid
- "We will try to..." (uncertain)
- "The feature might..." (hedge language)
- "Best effort to..." (non-binding)
- Overly technical jargon without explanation

### Structure Per Feature
1. Opening sentence: What the feature does (what + how)
2. Technical sentence: Key technology, method, or integration
3. Optional third sentence: User benefit or specific detail

### Variable Placeholders
- `{{ACTION}}`: What users can do (e.g., "extract vendor information from invoices")
- `{{METHOD}}`: How it works (e.g., "a machine learning model trained on historical data")
- `{{BENEFIT}}`: Why it matters (e.g., "reducing processing time from 2 hours to 5 minutes per document")

### Length Guidelines (CRITICAL)
- **2–3 sentences per feature subsection** — this is a hard limit
- No deliverables sub-lists
- Total In-Scope section: 250–350 words maximum
- More source data = more specific sentences, NOT more sentences

---

## 3. Out-of-Scope Features

**Purpose**: Explicitly state what is NOT included to prevent scope creep.

### Template Pattern

Use a simple dash-separated list format with **single-line items only**:

```
## 3. Out-of-Scope Features

- Image processing from PDFs or other documents
- Customer-facing interactions (internal users only)
- Spoken language processing (written text only)
- Additional data sources beyond the four defined sources
- Production deployment hardening (load testing, disaster recovery)
```

### CRITICAL: Single-Line Items Only

Each out-of-scope bullet must be a **single concise phrase** (5–15 words). Do NOT include:
- Bold feature names with colon-separated explanations
- Multi-sentence descriptions per item
- Reasons why items are excluded
- Suggestions for when items might be addressed

**Good examples (single-line):**
- "Image processing from PDFs or other documents"
- "Customer-facing interactions (internal technicians only)"
- "Comprehensive multi-language support beyond German and English"
- "Production deployment hardening (load testing, disaster recovery)"
- "CRM integration if it does not add sufficient value during Sprint 4"

**Bad examples (too verbose):**
- "**Production Environment Deployment**: While the PoC will be fully functional, deployment to the client's production infrastructure is outside this scope."
- "**Historical Data Migration**: Migration of existing historical data from the legacy system is not included."

### Key Phrases to Use
- Parenthetical clarifiers: "(internal users only)", "(written text only)"
- Brief conditional notes: "if it does not add sufficient value"

### Length Guidelines (CRITICAL)
- **5–15 words per item** — single line only
- 5–8 items typical
- Total section: 80–120 words maximum
- No bold formatting, no colons, no multi-sentence items

---

## 4. Architecture Diagram

**Purpose**: Provide visual representation of the proposed system design with brief explanatory context.

### Template Pattern (Concise)

The architecture text should be **1–2 sentences + 3 short bullets**. The diagram image does the heavy lifting — text is supplementary only.

#### Pattern
"This is an initial architecture diagram constructed based on our hackathon conversations and project design. We will use this as the blueprint for project implementation.

Hosting Setup: [Cloud provider] within [Client] subscription:
- [Infrastructure point 1]
- [Infrastructure point 2]
- [Infrastructure point 3]"

#### Example
"This is an initial architecture diagram constructed based on our hackathon conversations and project design. We will use this as the blueprint for project implementation.

Hosting Setup: Azure cloud within SW subscription:
- Data sources stored on SW premises with backup in Azure Blob Storage
- AI services hosted in SW's Azure environment (West Germany / France Central)
- Teams integration via Power Virtual Agents and Power Automate"

### What NOT to Include
- Lengthy component-by-component descriptions (the diagram shows this)
- Data flow narratives (arrows in diagram show this)
- Implementation details or library choices
- Code snippets or pseudocode

### Length Guidelines (CRITICAL)
- **1–2 sentences** introductory text
- **3 short bullets** for hosting/infrastructure highlights
- Total: 60–100 words maximum (excluding diagram image)
- The diagram image provides the detail — keep text minimal

---

## 5. Prerequisites from {{CLIENT}}

**Purpose**: Clearly state what the client must provide for the PoC to succeed.

### Template Pattern (Concise)

Use **simple single-line bullets** — no status indicators, no owners, no timelines, no bold formatting.

```
## 5. Prerequisites from {{CLIENT}}

- Access to {{CLIENT}} [system/platform] subscription
- API access to [System A], [System B], and [System C] data sources
- Access to [file server/storage] and [specific documents/data]
- Access to {{CLIENT}} [communication platform] for deployment
- [Cloud/AI service] access within {{CLIENT}}'s subscription
- [Number] sample questions and answers per data source for validation
- Regular availability of domain experts for testing and feedback ([names])
```

### CRITICAL: Single-Line Bullets Only

Each prerequisite is one line (~10–20 words). Do NOT include:
- Bold feature names with descriptions
- Status indicators (✓, ⏳, ⚠, ❌)
- Owner assignments
- Timelines or effort estimates
- Multi-line nested sub-items

**Good examples:**
- "Access to SW Azure subscription and Power Platform (Copilot Studio, Power Automate)"
- "API access to Academy System, AuthorIT, and CRM data sources"
- "20 sample questions and answers per data source for validation"

**Bad examples:**
- "**API Access to Academy System**: Read and write access to SW's Academy System API, with credentials to authenticate as integration user. Required for data extraction. Status: ⏳ In Progress"

### Length Guidelines (CRITICAL)
- **Single line per item** (~10–20 words)
- 6–8 items typical
- Total section: 80–120 words maximum
- No bold, no status, no nested items

---

## 6. High-Level Sprint Design

**Purpose**: Outline the development timeline, deliverables per sprint, and key milestones.

### Template Pattern (Concise — Deliverables Only)

Each sprint has: **bold title line** + **"Deliverables:" label** + **4–5 short bullet deliverables**. No Objectives, Key Activities, or Success Criteria sub-sections.

```
## 6. High-Level Sprint Design

We suggest to implement this solution over [N] sprints. Please find below the sprint goals and deliverables. We will finalize this together with you before our project kickoff.

Exemplary development sprints plan

Sprint 0: Preparation (1 week — before project kickoff)
Deliverables:
- Confirm [infrastructure] prerequisites
- Align on [scope items] and data source APIs
- Finalize architecture design and tech stack decisions
- Define sample Q&A sets for each data source

Sprint 1: [Goal description] (X weeks)
Deliverables:
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]
- [Deliverable 4]

Sprint 2: [Goal description] (X weeks)
Deliverables:
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]
- [Deliverable 4]
```

### CRITICAL: Deliverables Only

Do NOT include per-sprint:
- **Objective** sub-sections
- **Key Activities** sub-sections
- **Success Criteria** sub-sections
- Multi-sentence deliverable descriptions

Each deliverable bullet is one concise line (~5–15 words).

**Good examples:**
- "Deploy Qdrant vector database on Azure"
- "Build initial data extraction pipeline for error codes"
- "Parse and ingest Academy training documents"
- "Final testing and fine-tuning of answers"

**Bad examples:**
- "Development environment fully operational and documented with all dependencies configured"
- "Working feature accessible via REST API with comprehensive error handling and retry logic"

### Structure Per Sprint
1. Bold sprint label with title and duration
2. "Deliverables:" label
3. 4–5 short bullet deliverables (one line each)

### Length Guidelines (CRITICAL)
- 1–2 sentence intro for the whole section
- Sprint 0 + 3–4 implementation sprints
- **4–5 bullet deliverables per sprint** (one concise line each)
- Total section: 200–300 words maximum
- No Objectives, Key Activities, or Success Criteria

---

## 7. Conclusion (OPTIONAL — Not included by default)

**IMPORTANT:** Do NOT include a Conclusion section by default. The standard scope document ends at Section 6 (Sprint Design). Only add a Conclusion if the user explicitly requests it.

Including a Conclusion section adds ~150–250 words and risks pushing the document beyond the 4–5 page limit.

If explicitly requested, keep it to 3–4 sentences maximum.

---

## Writing Style Guidelines for All Sections

### Document Length (CRITICAL)
- **The entire document must be 4–5 pages maximum (800–1200 words)**
- More source data = more specific content, NOT more content
- Every sentence must earn its place — cut anything generic or filler
- When in doubt, shorter is better

### Tone
- Professional but not stuffy
- Confident and capability-focused
- Partnership-oriented (use "we" and "our")
- Benefit-focused (emphasize {{CLIENT}} outcomes)
- Evidence-based (everything traces to the hackathon or stated requirements)

### Structure
- Clear section headers with numbering
- Topic sentences at the start of paragraphs
- Bullet points for lists of related items
- Short paragraphs (2–3 sentences typical)
- Single-line bullets in list sections (Out-of-Scope, Prerequisites)

### Language
- Active voice preferred: "The system will extract..." not "Extraction will be performed..."
- Specific and concrete language
- Define technical terms on first use
- Use consistent terminology throughout (don't vary between "extract," "parse," "identify" for the same concept)
- Avoid marketing jargon or unsupported superlatives

### What Makes a Good Scope Document Section
- ✓ Every claim traces to the hackathon documentation or user notes
- ✓ Features are described with enough detail to be binding
- ✓ Content is concise — no filler, no padding, no redundancy
- ✓ Prerequisites are clear, actionable, and single-line
- ✓ Timeline and deliverables are specific
- ✓ Out-of-scope items are single-line phrases
- ✓ No unexplained jargon or technical acronyms
- ✓ Document fits within 4–5 pages

### Common Errors to Avoid
- ✗ **Document too long:** Exceeding 5 pages — this is the #1 error to prevent
- ✗ Verbose out-of-scope items with multi-sentence explanations
- ✗ Deliverables sub-lists under each in-scope feature
- ✗ Objectives/Key Activities/Success Criteria sub-sections per sprint
- ✗ Adding a Conclusion section when not requested
- ✗ Vague language: "We'll do our best," "hopefully," "we'll try"
- ✗ Unsubstantiated claims: "This will save 50% time" (without evidence)
- ✗ Invented details: features not in the hackathon, made-up timeline, fictional metrics
- ✗ Inconsistent terminology: switching between "user," "operator," "administrator"
