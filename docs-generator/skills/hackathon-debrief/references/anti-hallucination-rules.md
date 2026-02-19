# Anti-Hallucination Verification Framework

This framework ensures all generated content is grounded in source data. Apply this verification after generating all sections.

---

## Verification Checks

### 1. Metrics Check (Weight: 20%)

Every number, percentage, time duration, or quantitative claim must trace to a specific location in the source material.

**What to verify:**
- All percentages (e.g., "40% improvement")
- All time values (e.g., "200 hours per month")
- All counts (e.g., "450 employees")
- All monetary values
- All date references

**Action if fails:** Flag the metric and ask the user to confirm or remove it.

### 2. Terminology Check (Weight: 20%)

Domain-specific terms must match the source document, NOT the sample excerpts.

**What to verify:**
- Company name matches exactly (no variations)
- Industry terminology comes from source, not samples
- Technical system names match source (e.g., "SAP S/4HANA" not "SAP CRM" if source says S/4HANA)
- Process names match source terminology
- Product/service names are accurate

**Common mistakes to catch:**
- Using "Dokumentenbündelung" (from LOGEX sample) when the actual client does something different
- Using "three-way matching" (from TechFlow sample) for a non-procurement use case
- Copying participant names from samples instead of actual participants

**Action if fails:** Replace with correct terminology from source.

### 3. Style Patterns Check (Weight: 30%)

All 5 mandatory style patterns must be correctly applied.

**Checklist:**
- [ ] Three Pillars: Conclusion starts with the three pillars phrase
- [ ] Forward-Looking: Document ends with "Wir würden uns sehr freuen..." / "We would be delighted..."
- [ ] AI Journey: Background uses "KI-Reise"/"AI journey" terminology
- [ ] Collaborative Tone: "wir"/"we" used more than "sie"/"they"
- [ ] Evidence-Based: All metrics trace to source data

**Action if fails:** Regenerate the failing section with the correct pattern applied.

### 4. Completeness Check (Weight: 30%)

All required content must be present.

**What to verify:**
- All sections from the section order are present (background through conclusion)
- All pain points from the source appear in the Challenge section
- All data sources are listed in the Data section
- Recommendations and next steps reflect source content
- Participants list is complete

**Action if fails:** Add the missing content from source data.

---

## Anti-Hallucination Rules

1. **NEVER invent metrics or statistics** — If a number isn't in the source, don't include it
2. **NEVER fabricate company details** — Employee count, revenue, location must come from source
3. **NEVER add technologies not mentioned** — Only reference tools/systems from the source
4. **NEVER invent participant names** — Only list people explicitly named in source
5. **NEVER copy domain terms from samples** — LOGEX/TechFlow terminology stays in samples only
6. **NEVER assume timelines** — Only include dates/deadlines explicitly stated in source
7. **NEVER add features not discussed** — Stick to what was actually explored in the hackathon
8. **Mark unknowns explicitly** — Use "[Noch zu bestätigen]" (DE) or "[To be confirmed]" (EN) for gaps
9. **Cross-check all sections** — Every claim in Results must align with Challenge/Goal/Approach
10. **Prefer omission over invention** — Better to have a shorter, accurate document than a longer fabricated one

---

## Scoring Dimensions

When scoring each section, evaluate these 5 dimensions (each 0-20 points):

1. **Source Grounding (0-20):** Is every claim traceable to the source document?
2. **Specificity (0-20):** Are names, tools, integrations specific rather than generic?
3. **Completeness (0-20):** Does the section cover its full purpose?
4. **Actionability (0-20):** Can someone act on this content?
5. **Anti-Hallucination (0-20):** Is the section free of invented details?

### Section-Specific Thresholds

| Section | Threshold | Rationale |
|---------|-----------|-----------|
| Participants | 90 | Just data extraction — should be nearly perfect |
| Background | 75 | Some framing language is generic by nature |
| Hackathon Structure | 70 | Structural description with some standard elements |
| Challenge | 80 | Core problem statement — must be precise |
| Goal | 75 | Derived from challenge — allows some synthesis |
| Data | 75 | Data listing must be accurate |
| Approach | 80 | Technical solution — must be precise |
| Results | 80 | Metrics must be exact |
| Canvas (optional) | 65 | Structured framework allows some synthesis |
| User Flow (optional) | 65 | Process description allows some synthesis |
| Conclusion | 75 | Summary with forward-looking — some synthesis allowed |
