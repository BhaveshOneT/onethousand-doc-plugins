# Anti-Hallucination Rules for Scope Document Generator

Strict operational rules to prevent AI hallucination and maintain factual accuracy in generated scope documents. These rules are binding and override all other instructions when conflicts arise.

---

## Core Principle

**EVERY claim, metric, feature, or technical detail in the generated scope document must trace directly to source data (hackathon documentation or user-provided notes). No invented content under any circumstances.**

---

## Rule 1: Traceability Requirement

**Binding Rule**: Every factual statement must have a documented source.

### What requires a source:
- Any metric or number (accuracy rates, processing times, volumes)
- Feature names and descriptions
- Technical approaches and architecture components
- Timeline durations
- Team member roles or names
- Client information (company name, industry, location)
- Business problems and objectives
- Prerequisites and dependencies

### What constitutes a valid source:
- Direct quote from hackathon document
- Paraphrase of content from hackathon document with page/section reference
- User note or clarification provided in supplementary input
- Extraction from structured data (spreadsheet, JSON provided by user)

### What is NOT a valid source:
- General knowledge about similar projects
- Assumptions about how the industry typically works
- Inference from partial information
- "Seems like this should be included"
- Common best practices not mentioned in source
- What the AI thinks would be helpful

### Implementation:
```
Before including any claim in the scope document:
1. Find the source material
2. Record the source: "per hackathon document page 5"
3. If source cannot be found: DO NOT INCLUDE the claim
4. If source is ambiguous: Flag with "[To be confirmed with client]"

Example correct: "The hackathon demonstrated 85% accuracy with Form Recognizer on sample invoices."
Example hallucination: "The system is expected to achieve 90% accuracy" (no source for 90%)
Example flagged: "Accuracy target: [To be confirmed - hackathon showed 85% with Form Recognizer]"
```

---

## Rule 2: No Invented Metrics

**Binding Rule**: Performance numbers, accuracy rates, processing times, and ROI figures must come directly from source or be marked as estimates needing validation.

### Prohibited Inventions:
- Cost savings not in source: "This will save $50,000/year" (make up number)
- Performance improvements without evidence: "Reduce processing time by 75%" (guess)
- Accuracy rates not tested: "Model will achieve 92% accuracy" (never validated)
- ROI or payback period without analysis: "3-month payback" (invented)
- Capacity metrics without basis: "System handles 1000 concurrent users" (assumed)

### Correct practices:
- If hackathon tested something: use the exact result → "Testing showed 85% accuracy"
- If user provided target: use their target → "Client target is 90% accuracy"
- If nothing is quantified: flag for validation → "Accuracy target: [To be confirmed with client]"
- If range is uncertain: use range from source → "Between 80-90% accuracy based on testing"

### Examples:

**Hallucination**:
```
"The system will reduce invoice processing time by 60%, enabling the client to save
15 FTE annually, resulting in an estimated $750,000 annual savings."
```
(None of these numbers were in the source)

**Correct**:
```
"The hackathon demonstrated that the proposed approach can reduce manual data entry
time per invoice from 45 minutes to approximately 10 minutes. The exact FTE savings
and financial impact will depend on actual deployment volume and are to be confirmed
with the client during the PoC."
```

---

## Rule 3: No Invented Feature Names

**Binding Rule**: Features must use exact terminology from the hackathon documents. Do not rename, rebrand, or create variations.

### Prohibited:
- Hackathon says "Data Extraction" → Scope document says "Smart Data Harvesting" (invented variation)
- Hackathon mentions "Invoice Classifier" → Scope document says "Intelligent Invoice Categorizer" (rebranded)
- Hackathon discusses "API Integration" → Scope document says "Advanced System Bridge" (marketing rename)

### Correct:
- Preserve exact feature names from source
- If feature is described but unnamed, assign a simple descriptive name
- If you must clarify a name, use parenthetical: "Data Extraction (also called parsing in the hackathon document)"

### Example:

**Hallucination**:
```
2.1 Intelligent Invoice Analysis Engine
The Advanced Document Intelligence System uses proprietary deep learning...
```
(Document just said "Extract data from invoices")

**Correct**:
```
2.1 Invoice Data Extraction
Based on the hackathon exploration, the system will extract key fields from invoices using...
```

---

## Rule 4: No Invented Quotes or Attributions

**Binding Rule**: Do not create fake quotes or attribute statements to stakeholders who didn't say them.

### Prohibited:
- Adding quotes from "the client said..." when they didn't say it in documented form
- Inventing stakeholder enthusiasm: "The client was excited about..." (not documented)
- Creating supporting statements: "The team agreed that..." (no record of this)

### Correct:
- Use only documented quotes from meeting notes, emails, or presentations
- If paraphrasing: don't use quotation marks
- Report what was actually said in source material

### Example:

**Hallucination**:
```
"One Thousand and Acme agreed that automation would revolutionize their operations,"
said Acme CFO John Smith.
```
(This exact quote doesn't exist in source)

**Correct**:
```
The hackathon confirmed that invoice automation can reduce processing time and error rates,
addressing Acme's primary business challenge with invoice handling.
```

---

## Rule 5: Preserve Exact Technical Terminology

**Binding Rule**: Do not paraphrase or standardize technical terms. Use exact terminology from source documents.

### Why this matters:
- "API integration" and "File-based integration" are different approaches
- "Machine learning model" and "Rule-based extraction" have different properties
- "Real-time processing" and "Batch processing" have different architectural implications
- If terms vary in source, preserve the variations and clarify in architecture section

### Prohibited:
- Source: "Form Recognizer" → Scope: "Optical character recognition technology" (different implications)
- Source: "Rule-based extraction" → Scope: "Machine learning extraction" (contradictory)
- Source: "Webhook integration" → Scope: "API connection" (loses important detail)

### Correct:
- Copy exact terminology from source
- If source is vague, research and match to documentation available
- If must clarify: add parenthetical → "Form Recognizer (Microsoft's document analysis service)"

### Example:

**Hallucination**:
```
The system will use advanced machine learning models to extract invoice data,
leveraging neural networks trained on historical documents.
```
(Hackathon actually tested Form Recognizer, which uses pre-trained models, not custom neural networks)

**Correct**:
```
The system will use Azure Form Recognizer to extract invoice data. During the hackathon,
this service was tested and demonstrated 85% accuracy on sample invoices.
```

---

## Rule 6: Flag Gaps with [To be confirmed]

**Binding Rule**: When information is missing, incomplete, or ambiguous, use explicit gap markers rather than inventing details.

### Gap markers:
- `[To be confirmed]` - Information needed but not yet determined
- `[To be confirmed with client]` - Requires client input
- `[Noch zu bestätigen]` (German) - German equivalent

### When to use:
- Missing data: "Timeline: [To be confirmed with client]"
- Incomplete specification: "Success criteria: Accuracy above [To be confirmed] percent"
- Unresolved conflicts: "Deployment timeline: [To be confirmed - hackathon suggested 4 weeks, client notes mention 3 weeks]"
- Unknown prerequisites: "Client will provide: [To be confirmed]"

### What NOT to do:
- Leave blank fields (use [To be confirmed] instead)
- Use placeholder syntax like [X], [Company], [N days]
- Assume reasonable defaults
- Fill in standard practice values

### Examples:

**Hallucination** (invents a number):
```
"The project will take approximately 4 weeks to complete."
```
(Source says "4-5 weeks" but it's ambiguous)

**Correct**:
```
"The project timeline is estimated at [To be confirmed] weeks, with preliminary
suggestions ranging from 4-5 weeks pending confirmation of prerequisites and data access."
```

**Hallucination** (uses placeholder):
```
"Client will provide [X] sample records for model training."
```

**Correct**:
```
"Client will provide [To be confirmed - estimated 50-100] sample records for model training."
```

---

## Rule 7: No Placeholder Values

**Binding Rule**: Do not use unfilled placeholder syntax in the final document.

### Prohibited placeholder patterns:
- `[X]`, `[Y]`, `[N]` - unfilled variables
- `[Company Name]`, `[Project Name]` - unpopulated fields
- `[N days]`, `[X weeks]` - undefined quantities
- `[TBD]`, `[TK]` - journalism shorthand
- `{...}` - template syntax in final output

### Correct alternatives:
- If value is known: use the actual value
- If value is missing: use `[To be confirmed]`
- If it's a template/instruction: clearly mark as such (e.g., "Section template for {{CLIENT_NAME}}")

### Example:

**Hallucination** (unfilled placeholders):
```
"2.1 [Feature Name]
One Thousand will build [number] capabilities for [system name], enabling [company]
to [achieve outcome] in [timeframe]."
```

**Correct**:
```
"2.1 Invoice Data Extraction
One Thousand will build automated field extraction for invoices, enabling Acme Financial
to reduce processing time from 45 minutes to approximately 10 minutes per document."
```

---

## Rule 8: No Timeline Assumptions

**Binding Rule**: Never assume or invent timeline values. Use only documented durations or mark as uncertain.

### Prohibited assumptions:
- "The PoC will take 4 weeks" (assumed industry standard)
- "Sprint 1 will be 2 weeks" (default sprint length)
- "Deployment will happen in Q3" (assumed based on current date)
- "We'll start March 15" (assumed next available date)
- "Testing will take 2 weeks" (standard testing duration)

### Correct practices:
- Use documented timeline: "Hackathon recommended 4-week PoC"
- Use client input: "Client requires completion by [date]"
- If no timeline: flag as missing: "Proposed timeline: [To be confirmed with client]"
- If multiple suggestions: present all: "Timeline suggestions ranged from 3-5 weeks depending on data availability"

### Examples:

**Hallucination**:
```
"Sprint 0: 1 week (Foundation & Setup)
Sprint 1: 2 weeks (Feature Development)
Sprint 2: 1 week (Testing & Refinement)
Total: 4 weeks"
```
(Standard assumption, not documented)

**Correct**:
```
"The hackathon recommended a 4-week timeline. The detailed sprint breakdown is
subject to confirmation of prerequisites from the client (see Section 5)."
```

---

## Rule 9: No Team/Resource Assumptions

**Binding Rule**: Do not assume or invent team size, resource allocation, or skill requirements.

### Prohibited:
- "The PoC will require 2 developers and 1 QA engineer" (assumed)
- "Development time is estimated at 8 person-weeks" (inferred)
- "A senior architect will be assigned to oversee design" (assumed)
- "We'll need a data scientist for model training" (inferred from use case)

### Correct:
- If documented: use it → "The hackathon team consisted of 3 developers and 1 architect"
- If not documented: flag → "Resource allocation: [To be confirmed by One Thousand leadership]"
- If mentioned tangentially: note it → "The hackathon suggested consideration of data science expertise for advanced use cases"

### Example:

**Hallucination**:
```
"Estimated effort: 10 person-weeks
Team composition: 1 Senior Developer, 2 Full-Stack Developers, 1 QA Engineer, 1 Data Scientist"
```

**Correct**:
```
"Detailed resource allocation and team composition will be determined by One Thousand
leadership based on finalized scope. Preliminary assessment suggests significant engineering
effort for the features in Sections 2.1 and 2.2."
```

---

## Rule 10: Architecture Components Must Match Source

**Binding Rule**: Architecture diagrams and component descriptions must reflect what was actually proposed/validated, not what you think should be there.

### Prohibited:
- Adding components that weren't mentioned: "Add a caching layer for performance" (not in source)
- Removing components that were discussed: (even if they seem minor or incomplete)
- Rearranging architecture without source: changing data flow paths not documented
- Assuming scalability components: "Add load balancer and auto-scaling" (not mentioned)

### Correct:
- Use exact components from hackathon architecture
- If component has unclear purpose: add `[To be confirmed]`
- If implementation method unclear: flag it → "Integration approach: [To be confirmed - options: REST API or direct database connection]"
- If component seems unnecessary: ask in documentation, don't remove

### Example:

**Hallucination**:
```
Architecture components:
1. REST API Gateway
2. Load Balancer
3. ML Service
4. Database
5. Cache Layer
6. Message Queue
```
(Source only mentioned API, service, and database)

**Correct**:
```
Architecture components (per hackathon exploration):
1. REST API Gateway - for client system integration
2. Document Processing Service - for validation and routing
3. Extraction Service - using Azure Form Recognizer
4. Database - for storing extracted data
5. Additional scalability components [To be confirmed during implementation planning]
```

---

## Rule 11: Don't Add Unmentioned Features

**Binding Rule**: Do not include features that were not discussed in the hackathon, even if they logically belong.

### Prohibited:
- Hackathon focused on extraction → Scope adds classification feature (not mentioned)
- Document covers invoice automation → Scope adds PO automation (different use case, not explored)
- Requirements specify basic dashboard → Scope includes advanced analytics (not discussed)

### Correct:
- List only features validated or discussed in hackathon
- If you think a feature is missing: add to "Recommendations for Phase 2"
- If a feature seems obvious: discuss with client before including

### Example:

**Hallucination**:
```
2.1 Invoice Data Extraction
2.2 Invoice Categorization
2.3 Automatic Approval Workflow
2.4 Exception Handling and Escalation
```
(Hackathon only covered extraction; others inferred)

**Correct**:
```
2.1 Invoice Data Extraction
2.2 Human-in-the-Loop Review Interface

Out of Scope:
— Automatic Approval Workflow: Not discussed in hackathon; recommended for Phase 2
— Exception Handling: Covered by manual review function; more complex automation deferred
```

---

## Rule 12: Don't Remove Mentioned Features

**Binding Rule**: Do not omit features that were explicitly discussed in the hackathon, even if they seem:
- Minor or incomplete
- Unrelated to the main use case
- Difficult to estimate
- Possibly out of scope

### If a feature was discussed:
- Include it in-scope (if consensus)
- Move to out-of-scope with clear reason (if appropriate)
- Mark with `[To be confirmed]` (if ambiguous)
- DO NOT silently omit

### Why this matters:
- Client may have different priorities than One Thousand
- "Minor" features might be important to specific stakeholders
- Scope creep works both directions: features can be cut, but removal must be explicit

### Example:

**Hallucination**:
```
Features discussed in hackathon: Extraction, Classification, Reporting
Features in scope doc: Extraction only
(Skipped classification and reporting without explanation)
```

**Correct**:
```
In Scope:
2.1 Invoice Data Extraction
2.2 Human Review Interface

Out of Scope (deferred to Phase 2):
— Invoice Classification: Discussed in hackathon but deferred to allow focus on core extraction
— Advanced Reporting Dashboard: Recommended for Phase 2 when broader data set available
```

---

## Rule 13: Pricing/Investment Only if Provided

**Binding Rule**: Do not estimate or invent financial figures unless explicitly provided in source.

### Prohibited:
- "PoC investment estimated at $50,000" (guessed)
- "ROI of 150% in year one" (calculated from invented assumptions)
- "Payback period of 6 months" (assumed)
- "Cost savings of $500K annually" (inferred)

### Correct:
- If budget is specified: use it → "Client budget for PoC: $40,000"
- If not specified: don't include → "Investment and pricing to be discussed"
- If client provided estimate: document it → "Client estimate: approximately $60K based on preliminary scope"

### Example:

**Hallucination**:
```
"Investment: $75,000
Expected ROI: 200% in 18 months
Payback period: 9 months"
```

**Correct**:
```
"Investment and financial terms: To be determined based on final scope and resource allocation."
```

---

## Rule 14: Sprint Durations Only if Documented

**Binding Rule**: Do not assign sprint lengths unless they were explicitly discussed and agreed in source.

### Prohibited:
- Using standard 1-week or 2-week sprints (assumption)
- Assuming Agile/Scrum if not mentioned
- Assigning durations based on feature size (estimated)
- Using "typical" project patterns

### Correct:
- If hackathon or client notes mention sprint structure: use it
- If not mentioned: propose or flag → "Sprint structure: [To be confirmed - recommend 1-week sprints for rapid validation]"
- If timeline exists but not divided into sprints: don't force a sprint structure

### Example:

**Hallucination**:
```
Sprint 0: 1 week
Sprint 1: 2 weeks
Sprint 2: 1 week
(Standard assumed structure)
```

**Correct** (if timeline given but no sprint structure):
```
Proposed Timeline: 4 weeks total

Sprint structure: [To be confirmed during kickoff - preliminary recommendation:
1-week setup sprint, 2-week feature sprint, 1-week testing sprint]
```

---

## Rule 15: Cross-Check Features Against Architecture

**Binding Rule**: Every in-scope feature must have corresponding architectural support documented. If it doesn't, flag the gap.

### Check for each feature:
```
Feature: Document Classification
Requires components: ✓ Classifier Service, ✓ ML Model, ✓ Training Pipeline
Data flows: ✓ From extraction service, ✓ To approval workflow
If any required component is missing → FLAG as gap
```

### What to do if component is missing:
- Don't invent the component
- Flag: "Feature depends on [Component] which requires [To be confirmed]"
- Or move feature to out-of-scope with reason

### Example:

**Hallucination**:
```
2.3 Automatic Approval Workflow (in scope feature)
[Architecture diagram doesn't include approval system or workflow engine]
(Mismatch not noted)
```

**Correct**:
```
2.3 Human Review Interface

Note: A future automatic approval workflow was discussed in the hackathon but is not
included in this PoC scope. It would require additional workflow engine components
beyond what is specified in Section 4 (Architecture).
```

---

## Rule 16: Flag Contradictions Explicitly

**Binding Rule**: When source documents contain contradictions, explicitly call them out rather than choosing one and hiding the conflict.

### When to flag:
- Two sections say different things: timeline 3 weeks vs. 4 weeks
- Feature described two different ways
- Conflicting success metrics
- Contradictory architecture descriptions
- Inconsistent technology recommendations

### How to flag:
```
"Timeline: The hackathon recommended 4 weeks, but preliminary client feedback
suggests a 3-week expectation. These timelines need to be reconciled during kickoff."
```

### What NOT to do:
- Choose one and ignore the other
- Average the values
- Try to resolve without client input
- Assume the larger/smaller number is correct

### Example:

**Hallucination**:
```
"The PoC will be delivered in 4 weeks."
(Source has both 3-week and 4-week mentions; picked 4 and ignored 3)
```

**Correct**:
```
"Timeline: Timeline discussion in hackathon materials suggests 4 weeks; however,
preliminary indication from client notes suggests 3-week target. This contradiction
requires clarification at kickoff."
```

---

## Rule 17: No Assumptions About Timelines

**Binding Rule**: Do not assume when a project starts, when decisions will be made, or when prerequisites will be available.

### Prohibited:
- "PoC begins April 1st" (assumed date)
- "Prerequisites will be available within 1 week" (assumed timeline)
- "Client will decide on architecture by March 20th" (assumed decision date)
- "Testing phase will start after feature development completes" (inferred sequencing)

### Correct:
- If documented: use it
- If not: make it explicit → "Start date: [To be confirmed with client once prerequisites are met]"
- If dependent: describe dependency → "Feature 2 cannot begin until [Prerequisite X] is available"

### Example:

**Hallucination**:
```
"PoC Kickoff: Monday, March 25, 2024
Week 1: Setup and infrastructure (completion target: April 1)
Week 2-3: Feature development (completion target: April 15)
```
(All dates assumed)

**Correct**:
```
"Proposed Timeline: 4 weeks from kickoff

Week 1: Setup and infrastructure
Week 2-3: Feature development
Week 4: Testing and documentation

Start Date: [To be confirmed with client once prerequisites are confirmed (see Section 5)]"
```

---

## Checking Rules: Pre-Generation Validation

Before outputting the final scope document, run these checks:

### For every metric/number:
- [ ] Is there a source document reference?
- [ ] Is the number an exact quote or clearly attributed?
- [ ] If estimated: is it marked as estimate?
- [ ] If inferred: is the inference explicitly noted?

### For every feature:
- [ ] Does it appear in the hackathon documentation?
- [ ] Is the name the exact name from source (or clearly explained if different)?
- [ ] Does the description match source, or is difference explained?
- [ ] Are acceptance criteria sourced or marked `[To be confirmed]`?

### For every timeline commitment:
- [ ] Is it explicitly stated in source?
- [ ] If assumed: is it marked as preliminary recommendation?
- [ ] Are dependencies documented?
- [ ] Is risk noted if timeline is aggressive?

### For every architecture component:
- [ ] Does it appear in hackathon architecture?
- [ ] Can I trace its purpose to a feature it supports?
- [ ] Is its technology choice explained?
- [ ] Are gaps marked `[To be confirmed]`?

### For every prerequisite:
- [ ] Can I trace why it's needed to a specific feature?
- [ ] Is the owner role accurate?
- [ ] Is the deadline realistic or marked `[To be confirmed]`?

### For every claim:
- [ ] Can I find it in a source document?
- [ ] Is it a direct quote, paraphrase, or inference?
- [ ] If inference: is the logic sound and explicitly stated?
- [ ] Would a different reader draw the same conclusion?

---

## What To Do When You're Tempted to Make Something Up

**Decision Tree**:
```
I want to include [claim/metric/feature/timeline] because [reason]

Is it explicitly in the hackathon doc?
├─ YES → Include it with source reference
└─ NO  → Is it in user notes/email/clarification?
    ├─ YES → Include it with source reference
    └─ NO  → Does the client need to decide on it?
        ├─ YES → Include as [To be confirmed with client]
        └─ NO  → Move to "Recommendations for Phase 2" or Out-of-Scope section

NEVER: Proceed with making it up
```

---

## Examples: Hallucination vs. Anti-Hallucination

### Example 1: Accuracy Metric

**Hallucination**:
```
"The extraction system will achieve 95% accuracy"
(No source for this number; hackathon showed 85%)
```

**Anti-Hallucination**:
```
"The hackathon testing demonstrated 85% accuracy with Azure Form Recognizer
on 50 representative invoice samples. Target accuracy for production will be
determined during the PoC based on actual client data diversity."
```

### Example 2: Architecture Component

**Hallucination**:
```
Architecture Components:
- REST API Gateway
- Microservices mesh
- Load balancer
- Kubernetes orchestration
- Message queue
- Cache layer
```
(Several components not mentioned in hackathon)

**Anti-Hallucination**:
```
Architecture Components (per hackathon exploration):
- REST API Service
- Document Processing Service
- Extraction Service (using Azure Form Recognizer)
- Database

Additional scalability components (caching, orchestration, messaging) are
recommended for Phase 2 production deployment.
```

### Example 3: Timeline

**Hallucination**:
```
Week 1-2: Setup and infrastructure (Sept 3-14)
Week 3-4: Feature development (Sept 17-28)
Week 5: Testing (Oct 1-5)
Week 6: Deployment (Oct 8-12)
```
(All dates assumed)

**Anti-Hallucination**:
```
Proposed 4-Week Timeline:
Week 1: Setup and infrastructure
Week 2-3: Core feature development
Week 4: Testing and documentation

Start Date: [To be confirmed with client once prerequisites listed in
Section 5 are confirmed]
```

### Example 4: Feature

**Hallucination**:
```
2.3 Advanced Analytics Dashboard
Provides executive-level insights into invoice processing patterns,
including predictive analytics for processing volume forecasting.
```
(Dashboard mentioned casually once; predictive analytics never discussed)

**Anti-Hallucination**:
```
2.3 Basic Reporting (if in source)

OR if only mentioned casually:

Out of Scope:
— Advanced Analytics Dashboard: Was mentioned in the hackathon as a future
capability but is not included in the Phase 1 PoC scope to maintain focus
on core extraction functionality.
```

### Example 5: Prerequisite

**Hallucination**:
```
The client will provide sample invoices for training and testing
(approximately 100-200 documents).
```
(Hackathon never specified a number)

**Anti-Hallucination**:
```
Client will provide representative sample invoices for training and testing
(quantity: [To be confirmed - initial estimate: 50-100 documents]).
```

---

## Final Directive

**If in doubt about whether something is sourced: DO NOT INCLUDE IT OR MARK IT `[To be confirmed]`.**

The cost of being conservative (flagging something as uncertain) is low.
The cost of hallucinating (including false information) is high.

Always err on the side of transparency about what is and isn't verified.
