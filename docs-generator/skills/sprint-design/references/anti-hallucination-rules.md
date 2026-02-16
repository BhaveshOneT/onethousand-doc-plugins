# Anti-Hallucination Rules for Design Plans

These rules are MANDATORY for all design plan content. Every section must pass these checks before publication to Confluence.

---

## Core Principle

**If it's not in the source (hackathon doc, customer conversation, or Confluence lookup), it does not go in the design plan.**

---

## Rules

### Rule 1: No Invented Metrics
- NEVER invent KPIs, benchmarks, performance numbers, or statistics
- NEVER fabricate processing times, throughput figures, or accuracy percentages
- If metrics were discussed in the hackathon, use the EXACT numbers from the source
- If approximate: use "[exact figure to be confirmed]"

### Rule 2: No Fabricated Technology Names
- NEVER invent tool names, library versions, or service tiers
- Use EXACT technology names from the source (e.g., "Firestore" not "NoSQL database")
- If the source says "a cloud database", keep it vague — do NOT specify a product
- Do NOT assume cloud providers (AWS vs. Azure vs. GCP) unless stated

### Rule 3: No Assumed Timelines
- NEVER invent sprint durations unless explicitly discussed
- Do NOT default to "2-week sprints" unless the source says so
- Calendar week (CW) numbers ONLY if provided in source material
- If timeline is unclear, use relative timing: "Sprint 1 (duration TBD)"

### Rule 4: No Added Features
- NEVER add features, components, or capabilities not in the source
- If the hackathon explored Feature A and the customer mentioned Feature B, include BOTH — but don't invent Feature C
- "Nice to have" features only if explicitly mentioned as such

### Rule 5: No Assumed Team Sizes or Effort
- NEVER invent person-day estimates or team allocations
- If effort was discussed, use exact figures from source
- If not discussed, use "[Effort estimation to be confirmed]"
- Do NOT assume roles (e.g., "2 backend developers") unless stated

### Rule 6: No Invented Architecture Components
- Include ONLY components mentioned in hackathon or customer discussions
- Do NOT add "standard" infrastructure (monitoring, logging, CI/CD) unless discussed
- If the source mentions "cloud hosting", don't assume specific services

### Rule 7: Preserve Exact Terminology
- Use the client's exact domain terms (e.g., "Abrechnungseinheiten" not "billing units")
- Preserve feature names as given (e.g., "Produktberater" not "Product Advisor" unless the source uses both)
- Don't rename, rebrand, or "improve" terminology

### Rule 8: Flag Conflicts Between Sources
- If hackathon doc says X and customer conversation says Y, include BOTH with clear attribution:
  - "Per the hackathon: [X]. Updated per customer discussion: [Y]."
- NEVER silently pick one version over another
- The customer conversation generally takes precedence, but BOTH must be visible

### Rule 9: Status Markers Must Be Verified
- Only mark items as "Done", "→ Done", or "✓ Completed" if explicitly confirmed in source
- Default status for new items is unmarked or "Planned"
- Don't assume completion based on sprint timing

### Rule 10: Dependencies Must Be Stated, Not Inferred
- Only list dependencies that are explicitly mentioned
- Don't infer dependencies from architecture (e.g., "needs API access" unless specifically stated)
- External collaborations only if named in source

---

## Decision Tree for Uncertain Content

```
I want to include [claim/detail] because [reason]

Is it EXPLICITLY stated in the hackathon document?
├─ YES → Include with confidence. Note source.
└─ NO  → Is it EXPLICITLY stated in customer conversation?
    ├─ YES → Include with confidence. Note source.
    └─ NO  → Was it found in Confluence (smart lookup)?
        ├─ YES → Include with source page reference. Note it's from Confluence.
        └─ NO  → Is it a reasonable inference that the client needs to confirm?
            ├─ YES → Include as "[To be confirmed]" / "[Noch zu bestätigen]"
            └─ NO  → DO NOT INCLUDE IT. Period.
```

---

## Confidence Impact

Hallucination directly reduces the **Anti-hallucination** dimension of the confidence score:
- Each fabricated detail: -5 points
- Each assumed timeline: -4 points
- Each invented component: -5 points
- Each missing source attribution: -3 points

A section with ANY fabricated content cannot score above 15/20 on Anti-hallucination.

---

## Language-Specific Markers

### English
- `[To be confirmed]`
- `[Exact figure to be determined]`
- `[Timeline TBD]`
- `[Effort estimation pending]`

### German
- `[Noch zu bestätigen]`
- `[Genaue Zahl noch zu bestimmen]`
- `[Zeitplan offen]`
- `[Aufwandsschätzung ausstehend]`
