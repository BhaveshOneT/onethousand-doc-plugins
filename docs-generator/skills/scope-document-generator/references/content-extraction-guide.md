# Content Extraction Guide for Scope Document Generator

Comprehensive guide for extracting actionable content from hackathon documentation (PDFs, DOCX, presentations) to populate scope documents automatically or semi-automatically.

---

## Overview

The scope document generator needs structured, validated data extracted from hackathon materials. This guide provides:
1. Where to find key information in hackathon docs
2. What to extract and how to categorize it
3. How to handle multi-use-case hackathon docs
4. How to merge hackathon data with user-provided notes
5. Red flags that indicate missing or contradictory information
6. Output format specification (JSON schema)

---

## Section 1: Where to Find Information in Hackathon Documents

### Typical Hackathon Document Structure

#### Cover/Title Page
- **Location**: First page
- **Extract**:
  - Hackathon title
  - Hackathon dates
  - Client organization name
  - Project/use case title
  - Partners involved (One Thousand, etc.)

#### Executive Summary / Overview
- **Location**: Usually pages 1-3
- **Extract**:
  - High-level problem statement
  - Business objectives
  - Why the hackathon was conducted
  - Key findings at a glance
  - Expected impact/benefits

#### Problem Statement / Business Context
- **Location**: Pages 2-5, often in "Background" or "Context" section
- **Extract**:
  - Current business problem
  - Impact on client (time, cost, quality metrics)
  - Root causes
  - Current process description
  - System landscapes / existing tools mentioned

#### Hackathon Goals & Exploration
- **Location**: Dedicated section, pages 5-8
- **Extract**:
  - What was explored during the hackathon
  - Specific hypotheses or questions to answer
  - Scope of the exploration
  - Constraints during hackathon (time, data access, etc.)

#### Technical Exploration Results
- **Location**: Core content, pages 8-15+
- **Extract**:
  - Technologies explored/validated
  - Architecture components tested
  - Data sources examined
  - API integrations attempted
  - Performance metrics/benchmarks from hackathon
  - Accuracy/success rates observed
  - Code snippets or prototypes created
  - Assumptions validated

#### Data & Infrastructure
- **Location**: Technical sections, often mid-document
- **Extract**:
  - Data sources identified (systems, databases, formats)
  - Data volume/scale
  - Data freshness requirements
  - Existing infrastructure
  - IT environment details
  - Security/compliance considerations mentioned

#### Use Cases & Features
- **Location**: Sections titled "Use Cases," "Features," "Capabilities," "Solution Design"
- **Extract**:
  - Each distinct use case or feature
  - User workflows described
  - Specific user actions/interactions
  - Expected outcomes per use case
  - User roles mentioned
  - Frequency of use

#### Architecture & Technical Design
- **Location**: Dedicated architecture section, usually mid-document
- **Extract**:
  - System components described
  - Data flow diagrams or descriptions
  - Integration points
  - Technology stack mentioned
  - Assumptions made
  - Scalability considerations

#### Timeline & Resources
- **Location**: Often near end, "Project Plan" or "Next Steps"
- **Extract**:
  - Proposed timeline
  - Sprint breakdown (if mentioned)
  - Resource requirements
  - Skill sets needed
  - Team composition recommendations
  - Estimated effort (person-weeks, etc.)

#### Recommendations & Next Steps
- **Location**: Final sections
- **Extract**:
  - Recommended PoC scope
  - Suggested features for Phase 1
  - Items deferred to Phase 2+
  - Prerequisites for proceeding
  - Risk factors identified
  - Success metrics proposed

#### Appendices
- **Location**: End of document
- **Extract**:
  - Detailed data specifications
  - Sample data/screenshots
  - Code samples
  - Meeting notes
  - Attendees/stakeholders list
  - References to external systems

---

## Section 2: What to Extract and How to Categorize

### Category 1: Client & Project Information

**Fields to extract:**
```
client_name: string
client_industry: string
hackathon_date_start: date (YYYY-MM-DD)
hackathon_date_end: date (YYYY-MM-DD)
hackathon_location: string (optional)
project_title: string
project_description: string (2-3 sentences)
stakeholders: array of {name, role, title, email}
```

**Where to find:**
- Cover page
- Executive summary
- Meeting notes/attendees list

**Example extraction:**
```json
{
  "client_name": "Acme Financial Services",
  "hackathon_date_start": "2024-03-15",
  "hackathon_date_end": "2024-03-16",
  "project_title": "Invoice Automation PoC",
  "stakeholders": [
    {"name": "John Smith", "role": "CFO", "email": "j.smith@acmefs.com"}
  ]
}
```

### Category 2: Business Problem & Context

**Fields to extract:**
```
business_problem: string (the core challenge)
problem_impact: array of {
  metric: string,
  current_value: number|string,
  desired_value: number|string,
  unit: string
}
current_process: string (how they do it now)
pain_points: array of string
business_objectives: array of string
success_metrics: array of {metric: string, target: string|number}
```

**Where to find:**
- Executive summary
- "Problem Statement" or "Business Context" section
- Any quantified metrics section

**Example extraction:**
```json
{
  "business_problem": "Manual invoice processing is time-consuming and error-prone",
  "problem_impact": [
    {"metric": "Processing time per invoice", "current_value": 45, "desired_value": 10, "unit": "minutes"}
  ],
  "pain_points": [
    "Manual data entry errors causing payment delays",
    "High processing cost per invoice",
    "Lack of visibility into invoice processing status"
  ],
  "success_metrics": [
    {"metric": "Reduce processing time", "target": "80% reduction"}
  ]
}
```

### Category 3: Hackathon Findings & Validation

**Fields to extract:**
```
hackathon_findings: array of {
  finding: string,
  validation_method: string (how was it validated?),
  confidence: "high" | "medium" | "low",
  supporting_evidence: string
}
technologies_validated: array of {
  technology: string,
  use_case: string,
  result: "success" | "partial" | "failed",
  notes: string
}
assumptions_validated: array of string
key_insights: array of string
```

**Where to find:**
- "Results" or "Findings" section
- Technical exploration sections
- Conclusion/summary

**Example extraction:**
```json
{
  "hackathon_findings": [
    {
      "finding": "Rule-based extraction can achieve 85% accuracy on invoice headers",
      "validation_method": "Tested on 50 representative invoices",
      "confidence": "high",
      "supporting_evidence": "Actual test results showed 85% accuracy, 95% precision"
    }
  ],
  "technologies_validated": [
    {"technology": "Azure Form Recognizer", "use_case": "Invoice field extraction", "result": "success"}
  ]
}
```

### Category 4: Use Cases & Features

**Fields to extract:**
```
use_cases: array of {
  id: string (e.g., "UC-1"),
  name: string,
  description: string,
  actors: array of string (who uses it),
  main_flow: array of string (step-by-step),
  expected_outcome: string,
  frequency: string (daily, weekly, per-transaction, etc.),
  volume: string (number of transactions/day, etc.),
  related_systems: array of string
}
features: array of {
  id: string (e.g., "F-1"),
  name: string,
  description: string,
  related_use_cases: array of string (which UCs does it support),
  technical_approach: string (how it will work),
  data_inputs: array of {source: string, data_type: string},
  outputs: array of {type: string, format: string, destination: string},
  acceptance_criteria: array of string
}
```

**Where to find:**
- "Use Cases" or "Requirements" section
- Feature descriptions
- User workflow diagrams/descriptions
- "Solution Design" sections

**Example extraction:**
```json
{
  "use_cases": [
    {
      "id": "UC-1",
      "name": "Extract Invoice Data",
      "description": "Automatically extract key fields from incoming invoices",
      "actors": ["Accounts Payable Specialist"],
      "main_flow": [
        "Invoice arrives via email or upload",
        "System scans invoice for vendor, amount, invoice number",
        "System populates AP system with extracted data",
        "User reviews and approves or corrects"
      ],
      "expected_outcome": "Invoice data available in AP system within 5 minutes",
      "frequency": "per invoice",
      "volume": "200-300 invoices per day"
    }
  ],
  "features": [
    {
      "id": "F-1",
      "name": "Invoice Field Extraction",
      "description": "Extract vendor name, amount, invoice number from PDF or image",
      "related_use_cases": ["UC-1"],
      "technical_approach": "Azure Form Recognizer with custom training on sample invoices",
      "data_inputs": [
        {"source": "email attachment or web upload", "data_type": "PDF or image"}
      ],
      "outputs": [
        {"type": "structured data", "format": "JSON", "destination": "AP system via API"}
      ],
      "acceptance_criteria": [
        "Extract vendor name with 95% accuracy",
        "Extract amount with 98% accuracy",
        "Processing time < 10 seconds per invoice"
      ]
    }
  ]
}
```

### Category 5: Architecture & Technical Design

**Fields to extract:**
```
architecture: {
  description: string (narrative description of the architecture),
  components: array of {
    name: string,
    type: string (e.g., "service", "database", "API", "UI", "integration"),
    purpose: string,
    technology: string (specific tool/framework if mentioned),
    connects_to: array of string (component names it integrates with)
  },
  data_flows: array of {
    from: string (component name),
    to: string (component name),
    data_type: string,
    frequency: string
  },
  external_systems: array of {
    name: string,
    type: string,
    purpose: string,
    integration_type: string (API, file transfer, webhook, etc.)
  }
}
technology_stack: array of {
  layer: string (frontend, backend, data, ML, etc.),
  technology: string,
  rationale: string (why was it chosen?)
}
```

**Where to find:**
- "Architecture" or "Technical Design" section
- Architecture diagrams (extract the structure)
- Technical approach sections
- Tool selection discussions

**Example extraction:**
```json
{
  "architecture": {
    "description": "Three-tier architecture with document processing pipeline",
    "components": [
      {
        "name": "Invoice Intake Service",
        "type": "service",
        "purpose": "Receive and validate incoming invoices",
        "technology": "Node.js REST API",
        "connects_to": ["Document Processing Pipeline", "Extraction Service"]
      },
      {
        "name": "Extraction Service",
        "type": "service",
        "purpose": "Extract fields from invoices using AI",
        "technology": "Python with Azure Form Recognizer",
        "connects_to": ["AP Integration Service"]
      }
    ],
    "external_systems": [
      {
        "name": "Acme AP System",
        "type": "financial software",
        "purpose": "System of record for invoices",
        "integration_type": "REST API"
      }
    ]
  },
  "technology_stack": [
    {"layer": "frontend", "technology": "React", "rationale": "User review interface for extracted data"},
    {"layer": "backend", "technology": "Node.js + Python", "rationale": "Mixed for API and ML processing"},
    {"layer": "ml/ai", "technology": "Azure Form Recognizer", "rationale": "Validated during hackathon"}
  ]
}
```

### Category 6: Data & Infrastructure

**Fields to extract:**
```
data_sources: array of {
  name: string,
  type: string (database, API, file system, SaaS, etc.),
  system: string (which system does it belong to?),
  description: string,
  data_types: array of string (what kind of data?),
  volume: string (e.g., "10,000 invoices/month"),
  update_frequency: string (real-time, daily, weekly),
  access_method: string (API, database connection, file export, etc.),
  current_status: "available" | "to_be_provided" | "unknown"
}
infrastructure: {
  current_environment: string (on-premises, cloud, hybrid, SaaS),
  cloud_provider: string (AWS, Azure, GCP, etc.),
  network_environment: string (description of network/security considerations),
  data_residency_requirements: string,
  security_requirements: array of string,
  performance_requirements: {
    latency_target: string,
    throughput_requirement: string,
    availability_target: string
  }
}
```

**Where to find:**
- Technical sections discussing data
- Architecture diagrams
- Infrastructure sections
- Security/compliance mentions
- Appendices with technical specs

**Example extraction:**
```json
{
  "data_sources": [
    {
      "name": "Incoming Invoices",
      "type": "file",
      "system": "Email and web portal",
      "description": "PDF invoices from vendors",
      "data_types": ["PDF documents"],
      "volume": "200-300 invoices/day",
      "update_frequency": "real-time (as invoices arrive)",
      "access_method": "Email attachment or web upload",
      "current_status": "available"
    },
    {
      "name": "AP System Database",
      "type": "database",
      "system": "Acme AP Software",
      "description": "Invoice records and approval workflows",
      "volume": "historical + 300/day",
      "update_frequency": "real-time",
      "access_method": "REST API or direct database connection",
      "current_status": "to_be_provided"
    }
  ],
  "infrastructure": {
    "current_environment": "on-premises with cloud integration",
    "cloud_provider": "Azure",
    "security_requirements": ["Data encryption in transit and at rest", "SOC 2 compliance"]
  }
}
```

### Category 7: Prerequisites & Dependencies

**Fields to extract:**
```
prerequisites_from_client: array of {
  category: string (data, infrastructure, people, resources),
  item: string,
  description: string,
  why_needed: string,
  estimated_effort_for_client: string,
  owner_role: string,
  target_date: string (optional),
  current_status: "confirmed" | "in_progress" | "at_risk" | "unknown"
}
dependencies: array of {
  item: string,
  depends_on: string,
  risk_level: "low" | "medium" | "high",
  mitigation: string
}
```

**Where to find:**
- "Next Steps" or "Prerequisites" sections
- "Project Plan" sections
- Risk sections
- Appendices discussing setup requirements

**Example extraction:**
```json
{
  "prerequisites_from_client": [
    {
      "category": "data",
      "item": "Sample invoices",
      "description": "50-100 representative invoices for training and testing",
      "why_needed": "For model training and accuracy validation",
      "estimated_effort_for_client": "2 hours",
      "owner_role": "AP Manager",
      "current_status": "confirmed"
    },
    {
      "category": "infrastructure",
      "item": "Test environment access",
      "description": "Non-production instance of Acme AP System",
      "why_needed": "Safe integration testing without affecting live data",
      "estimated_effort_for_client": "4 hours (IT setup)",
      "owner_role": "IT Manager",
      "current_status": "in_progress"
    }
  ],
  "dependencies": [
    {
      "item": "Start extraction model training",
      "depends_on": "Receive sample invoices from client",
      "risk_level": "high",
      "mitigation": "Request samples immediately, offer contingency: use synthetic data"
    }
  ]
}
```

### Category 8: Timeline & Delivery

**Fields to extract:**
```
timeline: {
  proposed_poc_duration: string (e.g., "4 weeks"),
  proposed_start_date: string (optional, YYYY-MM-DD),
  proposed_end_date: string (optional, YYYY-MM-DD),
  critical_milestones: array of {date: string, milestone: string}
}
sprint_outline: array of {
  sprint_number: number,
  duration: string (e.g., "1 week"),
  focus: string,
  deliverables: array of string,
  estimated_resources: string (optional)
}
effort_estimates: {
  total_person_weeks: number (if mentioned),
  by_role: object (if breakdown provided)
}
```

**Where to find:**
- "Project Plan" or "Timeline" sections
- "Recommendations" sections
- "Next Steps"
- Effort estimation tables

**Example extraction:**
```json
{
  "timeline": {
    "proposed_poc_duration": "4 weeks",
    "proposed_start_date": "2024-04-22",
    "proposed_end_date": "2024-05-20",
    "critical_milestones": [
      {"date": "2024-04-22", "milestone": "PoC kickoff"},
      {"date": "2024-05-06", "milestone": "Core extraction feature complete"}
    ]
  },
  "sprint_outline": [
    {
      "sprint_number": 0,
      "duration": "1 week",
      "focus": "Setup and infrastructure",
      "deliverables": ["Development environment ready", "Data connections established"]
    },
    {
      "sprint_number": 1,
      "duration": "2 weeks",
      "focus": "Core extraction feature",
      "deliverables": ["Working extraction API", "95% accuracy on test set"]
    }
  ]
}
```

### Category 9: Out-of-Scope Items

**Fields to extract:**
```
out_of_scope: array of {
  item: string,
  reason: string (why excluded?),
  suggested_phase: string (when might it be included?),
  severity: "informational" | "important" | "critical"
}
```

**Where to find:**
- "Scope" or "Out of Scope" sections
- "Recommendations" sections
- Risk/limitation discussions
- Explicitly stated limitations

**Example extraction:**
```json
{
  "out_of_scope": [
    {
      "item": "Production deployment",
      "reason": "PoC delivered in test environment; production hardening requires separate engagement",
      "suggested_phase": "Phase 2: Production Ready",
      "severity": "important"
    },
    {
      "item": "User training",
      "reason": "Training materials provided; delivery of actual training sessions is separate",
      "suggested_phase": "Phase 2: Rollout",
      "severity": "important"
    }
  ]
}
```

---

## Section 3: Handling Multi-Use-Case Hackathon Documents

### Identifying Distinct Use Cases

Some hackathon documents explore multiple independent use cases. To extract properly:

1. **Look for clear separation**:
   - Section headers indicating different use cases
   - Different sections of architecture diagram
   - Separate problem statements per use case

2. **Use case boundaries**:
   - If use case A and use case B share zero features → separate scope documents
   - If use case A is a subset of use case B → consider combining
   - If they share infrastructure but different features → can be combined or separate

3. **Decision tree**:
   ```
   Are the use cases served by the same software instance?
   ├─ YES → Can be combined (if manageable scope)
   │         Check: are feature sets interrelated?
   │         ├─ YES → combine into single scope doc with clearly delineated features
   │         └─ NO  → consider separate PoCs for clarity
   └─ NO  → Create separate scope documents for each
   ```

### Extraction Pattern for Multi-Use-Case Docs

```json
{
  "hackathon_document": {
    "title": "Invoice & PO Automation Hackathon Results",
    "use_cases_included": 2,
    "use_case_1": {
      "name": "Invoice Automation",
      "features": ["Feature A", "Feature B"],
      "data_sources": ["Invoice system"],
      "scope_document_id": "scope-invoice-poc"
    },
    "use_case_2": {
      "name": "PO Automation",
      "features": ["Feature C", "Feature D"],
      "data_sources": ["PO system"],
      "shared_infrastructure": ["AI model training pipeline", "API gateway"],
      "scope_document_id": "scope-po-poc"
    },
    "decision": "Create two separate scope documents sharing architecture components"
  }
}
```

---

## Section 4: Merging Hackathon Data with User Notes

### User Notes Format

Users may provide supplementary information beyond the hackathon doc:
- Email notes with additional requirements
- Spreadsheet with revised timeline
- Slack messages with clarifications
- Updated stakeholder list
- Additional constraints (budget, timeline, team size)

### Merge Strategy

**Step 1: Identify conflicts**
```
Hackathon doc says: "4-week PoC"
User notes say: "Need to deliver in 3 weeks"
→ FLAG as potential conflict, verify with user
```

**Step 2: Apply priority rules**
```
Priority 1: User's explicit new information (highest priority)
Priority 2: Clarifications in user notes to hackathon findings
Priority 3: Hackathon document content
Priority 4: Inferred information (lowest priority)
```

**Step 3: Merge non-conflicting information**
```json
{
  "source_hackathon": {
    "sprint_outline": [Sprint 0, Sprint 1, Sprint 2, Sprint 3]
  },
  "source_user_notes": {
    "additional_prerequisite": "Domain expert availability",
    "updated_timeline": "3 weeks instead of 4"
  },
  "merged_result": {
    "sprint_outline": [Sprint 0, combined Sprint 1-2, accelerated Sprint 3],
    "prerequisites": [original list + new domain expert item],
    "timeline": "3 weeks",
    "merge_notes": "Timeline compressed per user notes; Sprint 0 duration reduced"
  }
}
```

**Step 4: Flag unresolvable conflicts**
```json
{
  "conflict": {
    "field": "timeline",
    "hackathon_says": "Needs 4 weeks for thorough testing",
    "user_says": "Must deliver in 3 weeks",
    "resolution_required": true,
    "flag_level": "critical",
    "message": "Confirm if 3-week timeline is achievable without reducing scope"
  }
}
```

---

## Section 5: Red Flags in Extracted Content

### Critical Red Flags (Prevent document generation)

These indicate missing or contradictory information that must be resolved:

1. **Missing client name or project title**
   - Risk: Vague or unidentifiable deliverable
   - Action: Request clarification before proceeding

2. **No clear business problem statement**
   - Risk: Scope document lacks justification
   - Action: Extract from executive summary or request from user

3. **Contradictory success metrics**
   - Example: "Reduce time 50%" vs. "Reduce time 80%" in different sections
   - Risk: Conflicting expectations
   - Action: Verify which is correct with user

4. **Undefined architecture with multiple interpretations**
   - Risk: Implementation scope unclear
   - Action: Clarify with user which architecture was validated

5. **Timeline conflicts**
   - Example: "4-week PoC" in one section, "2-week PoC" in another
   - Risk: Impossible promises
   - Action: Get user confirmation on actual timeline

6. **Critical prerequisites missing entirely**
   - Example: Hackathon doc mentions "requires API access" but doesn't list it as a prerequisite
   - Risk: PoC blocked immediately
   - Action: Explicitly add to prerequisites list with "[To be confirmed]" status

### Moderate Red Flags (May proceed with caution)

These suggest gaps but don't prevent document generation; they should be marked with "[To be confirmed]":

1. **Vague performance targets**
   - Example: "System should be fast" without numbers
   - Action: Mark as "[To be confirmed with client]" in scope doc
   - Retry: "Expected response time: [To be confirmed]"

2. **Features mentioned but not detailed**
   - Example: "Support for multi-vendor workflows" mentioned once but never described
   - Action: List as feature with "[Exact requirements to be defined with client]"

3. **Data volumes estimated, not confirmed**
   - Example: "Approximately 200 invoices/day" without verification
   - Action: Mark in scope doc as "Estimated at 200/day, to be confirmed"

4. **Integration points unclear**
   - Example: "Integrate with accounting system" but system name never specified
   - Action: Note in prerequisites: "Confirm which accounting system version"

5. **Team/resource estimates missing**
   - Example: PoC described but team size not specified
   - Action: Flag for user input before finalizing scope

### Low-Level Red Flags (Informational)

These are minor gaps that don't block document generation:

1. **Stakeholder details incomplete**
   - Missing email addresses for some attendees
   - Action: Note for follow-up, proceed with available info

2. **Dates in vague format**
   - Example: "Late March" instead of specific date
   - Action: Request clarification, use "mid-March" in document

3. **Terminology inconsistencies**
   - Example: "Extract," "parse," "identify" used interchangeably
   - Action: Standardize to one term in scope doc

4. **Assumptions not explicitly called out**
   - Example: "System assumes data is pre-validated" mentioned casually
   - Action: Explicitly list in architecture assumptions section

---

## Section 6: Structured Extraction Output Format (JSON Schema)

The output of content extraction should conform to this JSON schema for consistent input to the scope document generator:

```json
{
  "extraction_metadata": {
    "source_file": "string (path to hackathon document)",
    "source_format": "PDF|DOCX|PPT|other",
    "extraction_date": "YYYY-MM-DD",
    "extractor": "string (human or AI tool name)",
    "confidence_score": "0.0-1.0 (overall extraction confidence)",
    "manual_review_required": "boolean",
    "red_flags": ["array of red flag descriptions"],
    "red_flags_critical": ["array of critical issues requiring resolution"]
  },
  "client_and_project": {
    "client_name": "string",
    "client_industry": "string",
    "client_country": "string",
    "hackathon_date_start": "YYYY-MM-DD",
    "hackathon_date_end": "YYYY-MM-DD",
    "hackathon_location": "string (optional)",
    "project_title": "string",
    "project_description": "string",
    "one_thousand_participants": ["array of One Thousand team members]",
    "client_stakeholders": [
      {
        "name": "string",
        "title": "string",
        "role": "string (business role at client)",
        "email": "string (optional)",
        "organization_unit": "string (optional)"
      }
    ]
  },
  "business_context": {
    "business_problem": "string (one-sentence problem statement)",
    "detailed_problem_statement": "string (2-3 sentences)",
    "problem_impact": [
      {
        "impact_area": "string (cost|time|quality|risk)",
        "current_state": "string or number",
        "desired_state": "string or number",
        "metric": "string",
        "unit": "string"
      }
    ],
    "current_process": "string (how they do it today)",
    "pain_points": ["array of specific pain points"],
    "business_objectives": ["array of 3-5 objectives"],
    "success_metrics": [
      {
        "metric": "string",
        "target": "string or number",
        "how_measured": "string"
      }
    ],
    "why_poc_approach": "string (why PoC instead of full implementation?)"
  },
  "hackathon_findings": {
    "key_insights": ["array of major insights"],
    "findings": [
      {
        "finding": "string",
        "validation_method": "string (how was it validated?)",
        "confidence": "high|medium|low",
        "evidence": "string (supporting evidence or data)",
        "applies_to_features": ["array of feature IDs this supports"]
      }
    ],
    "technologies_explored": [
      {
        "technology": "string",
        "use_case": "string (what was it explored for?)",
        "result": "success|partial_success|failed|inconclusive",
        "performance_notes": "string (optional)",
        "recommendation": "include|evaluate|avoid"
      }
    ],
    "assumptions_validated": ["array of validated assumptions"],
    "assumptions_needing_validation": ["array of assumptions not yet validated"]
  },
  "use_cases_and_features": {
    "use_cases": [
      {
        "id": "string (UC-1, UC-2, etc.)",
        "name": "string",
        "description": "string",
        "actors": ["array of user roles"],
        "trigger": "string (what starts this use case?)",
        "main_flow": ["step 1", "step 2", "..."],
        "alternative_flows": ["optional alternative paths"],
        "expected_outcome": "string",
        "business_value": "string (why does this matter?)",
        "frequency": "string (per-day, per-week, per-transaction)",
        "volume": "string (how many per period?)",
        "related_systems": ["array of systems involved"]
      }
    ],
    "features": [
      {
        "id": "string (F-1, F-2, etc.)",
        "name": "string",
        "category": "string (extraction|classification|prediction|integration|ui|etc.)",
        "description": "string",
        "related_use_cases": ["array of UC IDs"],
        "user_benefit": "string (what does user gain?)",
        "technical_approach": "string (how will it be implemented?)",
        "data_inputs": [
          {
            "source": "string (system or data source)",
            "data_type": "string (document, database, API, etc.)",
            "format": "string (PDF, JSON, CSV, etc.)",
            "volume_per_period": "string (optional)"
          }
        ],
        "outputs": [
          {
            "type": "string (structured data, report, etc.)",
            "format": "string (JSON, XML, CSV, etc.)",
            "destination": "string (which system?)",
            "frequency": "string (real-time, batch, etc.)"
          }
        ],
        "acceptance_criteria": ["array of measurable criteria"],
        "estimated_effort": "string (optional, e.g., '1 week')"
      }
    ],
    "out_of_scope_items": [
      {
        "item": "string",
        "reason": "string (why excluded?)",
        "suggested_phase": "string (when might it be included?)",
        "severity": "informational|important|critical"
      }
    ]
  },
  "architecture_and_technology": {
    "architecture_description": "string (overall architecture narrative)",
    "components": [
      {
        "id": "string (COMP-1, etc.)",
        "name": "string",
        "type": "service|database|integration|ui|ml_model|etc.",
        "purpose": "string (what does it do?)",
        "technology_stack": "string (specific tool/framework/language)",
        "justification": "string (why this choice?)",
        "connects_to": ["array of other component IDs"],
        "inputs": ["array of data types it accepts"],
        "outputs": ["array of data types it produces"]
      }
    ],
    "data_flows": [
      {
        "from_component": "string (component ID)",
        "to_component": "string (component ID)",
        "data_type": "string (what kind of data?)",
        "frequency": "string (real-time, batch, event-driven)",
        "volume": "string (optional, e.g., '500 msgs/sec')",
        "protocol": "string (API, direct DB, file transfer, etc.)"
      }
    ],
    "external_integrations": [
      {
        "external_system": "string (name of external system)",
        "system_type": "string (SaaS, on-prem, API, etc.)",
        "purpose": "string (what data/services does it provide?)",
        "integration_type": "REST API|SOAP|File|Webhook|Direct DB|other",
        "frequency": "string (real-time, daily sync, etc.)",
        "current_status": "available|to_be_provided|at_risk"
      }
    ],
    "technology_decisions": [
      {
        "decision": "string (e.g., 'Use Azure Form Recognizer for extraction')",
        "rationale": "string (why was this chosen?)",
        "alternatives_considered": ["array of other options"],
        "validated_in_hackathon": "boolean",
        "risk_level": "low|medium|high"
      }
    ],
    "architectural_assumptions": ["array of explicit assumptions made"]
  },
  "data_and_infrastructure": {
    "data_sources": [
      {
        "id": "string (DS-1, etc.)",
        "name": "string",
        "type": "database|api|file_system|saas|message_queue|other",
        "parent_system": "string (which system owns this data?)",
        "description": "string",
        "data_types": ["array of data types provided"],
        "volume": "string (e.g., '10000 records/day')",
        "update_frequency": "real-time|hourly|daily|weekly|batch|other",
        "freshness_requirement": "string (how current must data be?)",
        "access_method": "REST API|GraphQL|SOAP|SQL|File Export|Webhook|other",
        "authentication": "string (OAuth|API Key|Service Account|Windows Auth|other)",
        "current_status": "available|to_be_provided|at_risk|unknown",
        "access_by_poc": "confirmed|pending|not_yet_requested"
      }
    ],
    "data_stores": [
      {
        "id": "string (DS-1, etc.)",
        "name": "string (name of database/data store)",
        "type": "SQL|NoSQL|File Store|Data Warehouse|Cache|other",
        "purpose": "string (what data does it hold?)",
        "technology": "string (specific product: PostgreSQL, MongoDB, etc.)",
        "current_status": "existing|to_be_created|shared_with_other_systems",
        "volume": "string (e.g., '1 TB')",
        "growth_rate": "string (optional)"
      }
    ],
    "infrastructure": {
      "deployment_target": "on-premises|cloud|hybrid|saas",
      "cloud_providers": ["array of cloud providers if cloud/hybrid"],
      "cloud_regions": ["array of regions if applicable"],
      "network_environment": "string (description of network architecture)",
      "data_residency_requirements": ["array of residency constraints"],
      "backup_requirements": "string (backup frequency, retention)",
      "disaster_recovery_requirement": "string (RTO, RPO if specified)"
    },
    "security_and_compliance": {
      "compliance_frameworks": ["array: SOC2|ISO27001|HIPAA|GDPR|PCI-DSS|etc."],
      "data_classification": "string (public|internal|confidential|restricted)",
      "encryption_requirements": {
        "in_transit": "required|recommended|not_specified",
        "at_rest": "required|recommended|not_specified"
      },
      "authentication_requirements": "string (OAuth|SAML|MFA|etc.)",
      "data_privacy_requirements": ["array of privacy requirements"],
      "audit_requirements": "string (audit logging requirements if any)"
    },
    "performance_requirements": {
      "latency_target": "string (e.g., 'sub-100ms for extractions')",
      "throughput_requirement": "string (e.g., '500 documents/min')",
      "availability_target": "string (e.g., '99.5% uptime')",
      "concurrent_users": "string or number (if applicable)",
      "storage_capacity": "string (estimated total storage needed)"
    }
  },
  "prerequisites_and_dependencies": {
    "prerequisites_from_client": [
      {
        "id": "string (PREREQ-1, etc.)",
        "category": "data|infrastructure|people|resources|access",
        "item": "string (what must they provide?)",
        "description": "string",
        "why_needed": "string (what blocks without this?)",
        "related_features": ["array of feature IDs that need this"],
        "owner_role": "string (e.g., 'IT Manager', 'Data Steward')",
        "estimated_effort_for_client": "string (e.g., '2-4 hours')",
        "target_date": "string (YYYY-MM-DD, optional)",
        "current_status": "confirmed|in_progress|at_risk|unknown",
        "risk_if_delayed": "low|medium|high",
        "mitigation_if_delayed": "string (optional plan B)"
      }
    ],
    "dependencies": [
      {
        "depends_on_item": "string (what does this depend on?)",
        "blocking_for": "string (what can't start without it?)",
        "dependency_type": "data|infrastructure|decision|approval|etc.",
        "risk_level": "low|medium|high",
        "critical_path": "boolean (is this on the critical path?)",
        "mitigation": "string (how to mitigate if this blocks?)"
      }
    ]
  },
  "timeline_and_delivery": {
    "proposed_poc_duration": "string (e.g., '4 weeks')",
    "proposed_start_date": "YYYY-MM-DD (optional)",
    "proposed_end_date": "YYYY-MM-DD (optional)",
    "critical_milestones": [
      {
        "date": "YYYY-MM-DD",
        "milestone": "string",
        "deliverables": ["array of deliverables due"],
        "critical": "boolean"
      }
    ],
    "sprint_breakdown": [
      {
        "sprint_number": "number (0, 1, 2, etc.)",
        "sprint_name": "string (e.g., 'Setup & Integration')",
        "duration": "string (e.g., '1 week')",
        "start_date": "YYYY-MM-DD (optional)",
        "end_date": "YYYY-MM-DD (optional)",
        "focus": "string (what is this sprint about?)",
        "features_in_scope": ["array of feature IDs"],
        "deliverables": ["list of specific deliverables"],
        "key_activities": ["array of activities"],
        "estimated_resource_allocation": "string (optional)"
      }
    ],
    "effort_estimates": {
      "total_person_weeks": "number (optional)",
      "by_role": {
        "role_name": "number of weeks (optional)"
      },
      "by_function": {
        "development": "number",
        "testing": "number",
        "integration": "number",
        "documentation": "number"
      }
    },
    "timeline_risks": [
      {
        "risk": "string (what could cause delays?)",
        "probability": "low|medium|high",
        "impact": "low|medium|high",
        "mitigation": "string"
      }
    ]
  },
  "recommendations": {
    "poc_scope_recommendation": "string (One Thousand's recommendation on what to include)",
    "features_recommended_for_phase_1": ["array of feature IDs"],
    "features_deferred_to_phase_2": ["array of feature IDs and reasons"],
    "success_factors": ["array of critical factors for PoC success"],
    "key_risks": [
      {
        "risk": "string",
        "mitigation": "string"
      }
    ],
    "next_steps": ["array of recommended next steps"]
  },
  "validation_and_quality": {
    "extraction_completeness": {
      "client_info": "100-90-80-70-60% (completeness %)",
      "business_context": "100-90-80-70-60%",
      "findings": "100-90-80-70-60%",
      "features": "100-90-80-70-60%",
      "architecture": "100-90-80-70-60%",
      "data": "100-90-80-70-60%",
      "prerequisites": "100-90-80-70-60%",
      "timeline": "100-90-80-70-60%"
    },
    "missing_sections": ["array of sections with gaps"],
    "contradictions_found": ["array of conflicting information"],
    "assumptions_made": ["array of inferences made during extraction"],
    "ready_for_document_generation": "boolean (can we generate scope doc from this?)",
    "blockers_to_generation": ["array of critical missing pieces"],
    "warnings": ["array of yellow flags that may affect document quality"]
  }
}
```

---

## Section 7: Usage Examples

### Example 1: Simple Single-Use-Case Extraction

**Input**: Hackathon PDF about invoice automation
**Process**:
1. Extract client name from cover page → "Acme Financial"
2. Extract problem statement from page 3 → "Manual invoice processing..."
3. Extract findings from page 8 → "85% accuracy with Form Recognizer"
4. Extract feature list from pages 10-12 → [feature A, feature B, feature C]
5. Extract architecture from diagram page 14 → [three-tier architecture]
6. Extract prerequisites from "Next Steps" page 18 → [sample data, test environment]

**Output**: JSON document ready for scope document generation

### Example 2: Multi-Use-Case Document

**Input**: Hackathon DOCX with both invoice AND PO automation
**Process**:
1. Identify that document covers two distinct use cases
2. Extract using same process for each use case separately
3. Note shared infrastructure components
4. Extract timeline (can they run in parallel or serial?)
5. Create decision: "Generate two separate scope documents or one combined?"
6. Output two extracted content files, one per use case

### Example 3: Incomplete Hackathon Doc + User Clarifications

**Input**: Hackathon PDF (missing prerequisite details) + email from client with clarifications
**Process**:
1. Extract from hackathon doc (gets ~80% of needed info)
2. Receive email clarifying timeline: "Need 3 weeks, not 4"
3. Receive email adding prerequisite: "Must have domain expert available 10 hrs/week"
4. Merge data with user notes as authoritative source
5. Flag timeline as "user-requested reduction" with potential risk
6. Mark domain expert as critical prerequisite

**Output**: Merged JSON with red flags noted for scope document validation

---

## Validation Checklist

Before outputting the JSON extraction, verify:

- [ ] Client name is present and spelled correctly
- [ ] At least one business problem is identified
- [ ] At least 2 use cases or 3 features are documented
- [ ] Architecture has at least 2 components
- [ ] At least 1 data source is identified
- [ ] At least 2 prerequisites are listed
- [ ] Timeline has at least rough duration (weeks/months)
- [ ] Success metrics are defined
- [ ] Out-of-scope items are explicitly listed
- [ ] No critical red flags are unaddressed
- [ ] Conflicting information is flagged
- [ ] Assumptions are explicitly called out
- [ ] All extracted values are quoted/attributed to source
- [ ] No invented details added
- [ ] Terminology is consistent throughout

If any checkbox is unchecked, adjust extraction to fill gaps or flag as missing/risky in the JSON output.
