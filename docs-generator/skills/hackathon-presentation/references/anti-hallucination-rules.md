# Anti-Hallucination Rules for Hackathon Presentations

These rules prevent fabrication of content in hackathon presentations. Every claim, metric, feature name, and technical detail must be traceable to source material.

---

## Core Principle

**EVERY claim on a slide must trace directly to source data.** If information isn't in the source material, it doesn't go on the slide. Use `[To be confirmed]` markers instead of inventing details.

---

## The 12 Rules

### Rule 1: Traceability Requirement

Every piece of content must have a documented source:
- Pain points → from sales email, client interview, or discovery meeting
- Data sources → from technical discussions or data inventory
- Approach steps → from hackathon planning or technical assessment
- Challenges → from technical discovery or domain analysis
- Business value metrics → from client statements or documented estimates
- Team members → from confirmed participant lists

**If you can't point to where the information came from, don't include it.**

### Rule 2: No Invented Metrics

Never invent or estimate:
- Number of tasks/processes per day/week/month
- Time savings (hours, FTEs, percentages)
- Error rates or accuracy numbers
- Cost savings or ROI figures
- Conversion rate improvements
- Customer satisfaction scores

**Use the client's own numbers or mark as `[To be confirmed]`.**

### Rule 3: No Invented Feature Names

Use the exact terminology from the source material:
- If the client says "SP numbers", don't change it to "product codes" or "SKUs"
- If the source says "REST API", don't upgrade to "microservices architecture"
- If the client calls it "ERP system", don't rename it to "enterprise platform"

### Rule 4: Preserve Technical Terminology

Don't translate, simplify, or replace technical terms:
- "Delphi" stays "Delphi" (don't change to "legacy system")
- "Azure" stays "Azure" (don't generalize to "cloud")
- "C# modules" stays "C# modules" (don't change to "modern components")

### Rule 5: No Invented Pain Points

Only include pain points that are:
- Explicitly stated by the client
- Clearly implied by documented process descriptions
- Confirmed in meeting notes or emails

**Do NOT add generic pain points like "data silos" or "lack of visibility" unless specifically mentioned.**

### Rule 6: No Invented Data Sources

Only list data that:
- The client confirmed they have access to
- Was demonstrated or shown during discovery
- Is mentioned in technical documentation

**Do NOT assume the existence of data sources based on industry norms.**

### Rule 7: No Invented Approach Steps

The approach must reflect:
- What was actually discussed/planned for the hackathon
- Capabilities that are technically feasible given the described system landscape
- Steps that map to documented pain points and available data

**Do NOT add capabilities that sound impressive but weren't discussed.**

### Rule 8: No Invented Challenges

Challenges must be:
- Specific to this client's situation
- Grounded in known technical or organizational factors
- Realistic obstacles that the hackathon might encounter

**Do NOT add generic AI challenges like "explainability" or "bias" unless specifically relevant.**

### Rule 9: Business Value Only If Provided

Business value metrics (FTEs, time savings, conversion improvements) can ONLY be included if:
- The client explicitly stated the number
- A documented estimate exists from a meeting or email
- The source material contains the specific metric

**Do NOT estimate business value based on industry benchmarks or comparable cases.**

### Rule 10: Team Members Must Be Confirmed

Only include team member names that are:
- Confirmed as hackathon participants
- Mentioned in planning emails or documents
- Provided by the user

**Do NOT guess team compositions based on company size or project scope.**

### Rule 11: System Landscape Must Match Source

When describing the technical environment:
- Only mention systems that are documented (ERP, CRM, APIs)
- Don't add components not in the source (don't assume a data warehouse exists)
- Preserve the exact system names mentioned by the client

### Rule 12: Flag Gaps Explicitly

When information is missing:
- Use `[To be confirmed]` markers
- Don't fill gaps with plausible-sounding content
- Ask the user for the missing information
- If the user says "proceed anyway", keep the markers visible

---

## Decision Tree for Content Inclusion

For any claim you want to include in the presentation:

```
Is it explicitly stated in the source material?
├── YES → Include it with the source's exact terminology
├── PARTIALLY → Include what's stated, mark uncertain parts with [To be confirmed]
└── NO
    ├── Is it strongly implied by the source?
    │   ├── YES → Include it but phrase conservatively
    │   └── NO → Do NOT include it
    └── Is it generic industry knowledge?
        └── Do NOT include it — hackathon presentations must be client-specific
```

---

## Pre-Generation Checklist

Before generating the content.json, verify:

- [ ] Every pain point traces to source material
- [ ] Every data source was confirmed as available
- [ ] Every approach step maps to a discussed capability
- [ ] Every challenge is specific to this client
- [ ] Every metric comes from the client, not from estimation
- [ ] Every team member name is confirmed
- [ ] Technical terms match the client's exact vocabulary
- [ ] No generic/boilerplate content was added

---

## Common Hallucination Traps

| Trap | What Happens | Prevention |
|------|-------------|------------|
| **Rounding up capabilities** | "Full end-to-end automation" when only partial was discussed | Use exact scope from source |
| **Adding industry pain points** | Including "data silos" when not mentioned | Only use client-stated pains |
| **Inventing metrics** | "Reduce processing time by 80%" when no number given | Use `[To be confirmed]` |
| **Upgrading tech stack** | "Microservices on Kubernetes" when client said "REST API on Azure" | Preserve exact terms |
| **Adding team members** | Guessing additional participants | Only include confirmed names |
| **Inflating business value** | "Save €500K annually" when client said "free up ~1 FTE" | Use client's own estimate |
| **Generic challenges** | "AI explainability concerns" when not discussed | Only client-specific challenges |
