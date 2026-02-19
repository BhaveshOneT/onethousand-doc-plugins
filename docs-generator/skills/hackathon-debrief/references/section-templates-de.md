# Hackathon Debrief Abschnitt-Templates — Deutsch

Prompt-Vorlagen, Wortbudgets und Stilmuster für jeden Abschnitt des Hackathon-Debrief-Dokuments.

---

## Section: participants

**Title (DE):** Teilnehmer
**Description:** Lists all participants from the client side and One Thousand team members who attended the hackathon.
**Required Fields:** participants
**Style Patterns:** collaborative-tone
**Word Count:** 40–130 words

### Prompt Template

```
Generate the Participants section for the hackathon debrief document.

List all participants organized by organization:

**Client participants ({{company.name}}):**
{{participants.client}}

**One Thousand participants:**
{{participants.oneThousand}}

Requirements:
1. Use a clean list format with full names and roles where available.
2. Group by organization (client first, then One Thousand).
3. If roles or titles are provided, include them after each name.
4. Do NOT invent or add any participants not listed in the source data.
5. Use a professional, concise format.

Output the section in {{language}} language.
```

---

## Section: background

**Title (DE):** Hintergrund
**Description:** Company context, AI journey framing, and introduction to the One Thousand partnership.
**Required Fields:** company.name, company.industry, company.background, company.aiOpportunity
**Style Patterns:** ai-journey, collaborative-tone
**Word Count:** 170–300 words

### Prompt Template

```
Generate the Background section for the hackathon debrief document.

Company information:
- Company name: {{company.name}}
- Industry: {{company.industry}}
- Background: {{company.background}}
- AI opportunity: {{company.aiOpportunity}}

Requirements:
1. Frame the company's AI adoption as a journey (use "KI-Reise" in German or "AI journey" in English).
2. Introduce the company with specific details from the source data (employee count, locations, products/services).
3. Explain why AI/automation is relevant to this company's situation.
4. Introduce the partnership with One Thousand naturally.
5. Use collaborative tone — "wir" (we) instead of "sie" (they).
6. CRITICAL: Only use facts from the provided source data. Do NOT invent company details, employee numbers, or revenue figures.
7. Include the AI opportunity as the bridge to the hackathon.

Output the section in {{language}} language.
```

---

## Section: hackathon_structure

**Title (DE):** Hackathon
**Description:** Event details including dates, location, format, and agenda overview.
**Required Fields:** metadata.title, metadata.date, metadata.location, metadata.format
**Style Patterns:** collaborative-tone
**Word Count:** 160–280 words

### Prompt Template

```
Generate the Hackathon Structure section for the debrief document.

Event details:
- Title: {{metadata.title}}
- Date: {{metadata.date}}
- Location: {{metadata.location}}
- Format: {{metadata.format}}

Requirements:
1. Describe the hackathon event with specific details (date, location, format).
2. Outline the agenda or structure of the day(s).
3. Mention what was covered and how the day was organized.
4. Use collaborative tone — emphasize the joint work between teams.
5. Do NOT invent agenda items or activities not mentioned in the source data.
6. If the format was hybrid or in-person, mention this specifically.
7. Keep the tone professional but energetic — convey the productive atmosphere.

Output the section in {{language}} language.
```

---

## Section: challenge

**Title (DE):** Herausforderung
**Description:** Pain points and current process challenges that the hackathon addressed.
**Required Fields:** useCases[0].painPoints, useCases[0].challenge, useCases[0].currentProcess
**Style Patterns:** evidence-based
**Word Count:** 220–360 words

### Prompt Template

```
Generate the Challenge section for the hackathon debrief document.

Challenge information:
- Pain points: {{useCases[0].painPoints}}
- Core challenge: {{useCases[0].challenge}}
- Current process: {{useCases[0].currentProcess}}

Requirements:
1. Present the pain points as a numbered list with clear descriptions.
2. Explain the current process and where it falls short.
3. Use specific numbers and metrics from the source data where available.
4. Frame challenges as opportunities for improvement, not criticisms.
5. CRITICAL: Every pain point must come directly from the source data. Do NOT add generic challenges like "data silos" or "lack of visibility" unless explicitly mentioned.
6. Connect the challenges to measurable business impact where the source data supports it.
7. Use evidence-based language ("konkret", "messbar" in German; "specifically", "measurable" in English).

Output the section in {{language}} language.
```

---

## Section: goal

**Title (DE):** Ziel
**Description:** Primary and secondary goals of the hackathon use case.
**Required Fields:** useCases[0].goal, useCases[0].title, useCases[0].expectedBenefits
**Style Patterns:** collaborative-tone, evidence-based
**Word Count:** 170–300 words

### Prompt Template

```
Generate the Goal section for the hackathon debrief document.

Goal information:
- Use case title: {{useCases[0].title}}
- Primary goal: {{useCases[0].goal}}
- Expected benefits: {{useCases[0].expectedBenefits}}

Requirements:
1. State the primary goal clearly and concisely.
2. List secondary goals or expected benefits.
3. Connect goals to the challenges described in the previous section.
4. Use collaborative language — "our goal was" or "unser Ziel war es".
5. Include measurable targets where the source data provides them.
6. CRITICAL: Do NOT invent goals or benefits not present in the source data.
7. Frame goals positively — what we aimed to achieve, not just what we wanted to fix.

Output the section in {{language}} language.
```

---

## Section: data

**Title (DE):** Daten
**Description:** Data sources used during the hackathon, including types, formats, and volumes.
**Required Fields:** useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 190–320 words

### Prompt Template

```
Generate the Data section for the hackathon debrief document.

Data sources:
{{useCases[0].dataSources}}

Requirements:
1. List all data sources that were used or analyzed during the hackathon.
2. For each data source, describe: type, format, volume (if known), and relevance.
3. Explain how the data was used in the hackathon approach.
4. Mention any data quality observations or preprocessing steps.
5. CRITICAL: Only list data sources explicitly mentioned in the source material. Do NOT assume the existence of data sources based on industry norms.
6. If data volumes or formats are specified, include them with exact numbers.
7. Use evidence-based language throughout.

Output the section in {{language}} language.
```

---

## Section: approach

**Title (DE):** Ansatz
**Description:** Technical solution and methodology used during the hackathon.
**Required Fields:** useCases[0].proposedSolution, useCases[0].technicalDetails, useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 220–360 words

### Prompt Template

```
Generate the Approach section for the hackathon debrief document.

Solution information:
- Proposed solution: {{useCases[0].proposedSolution}}
- Technical details: {{useCases[0].technicalDetails}}
- Data sources used: {{useCases[0].dataSources}}

Requirements:
1. Describe the technical approach step by step.
2. Explain the methodology and tools used.
3. Connect the approach to the data sources and challenges.
4. Include technical details at an appropriate level — specific enough to be credible, accessible enough for non-technical stakeholders.
5. CRITICAL: Only mention technologies, tools, and methods that are documented in the source material. Do NOT add technologies that sound impressive but were not used.
6. Describe what was actually built or prototyped during the hackathon.
7. Use evidence-based language and reference specific results where available.

Output the section in {{language}} language.
```

---

## Section: results

**Title (DE):** Ergebnisse
**Description:** Outcomes and measurable results from the hackathon.
**Required Fields:** useCases[0].results, useCases[0].expectedBenefits
**Style Patterns:** evidence-based
**Word Count:** 220–340 words

### Prompt Template

```
Generate the Results section for the hackathon debrief document.

Results information:
- Results: {{useCases[0].results}}
- Expected benefits: {{useCases[0].expectedBenefits}}

Requirements:
1. Present results with specific metrics and numbers from the source data.
2. Distinguish between demonstrated results (what was proven) and projected benefits (what could be achieved at scale).
3. Use concrete language — percentages, time savings, error reductions.
4. CRITICAL: Every metric MUST come directly from the source data. Do NOT invent or estimate numbers. If a metric is not available, do not include it.
5. Connect results back to the original goals and challenges.
6. Highlight the most impactful findings.
7. Use evidence-based patterns: "Die Ergebnisse zeigen konkret" (DE) or "The results specifically show" (EN).

Output the section in {{language}} language.
```

---

## Section: canvas

**Title (DE):** AI Breakthrough Canvas
**Description:** Structured canvas analysis of the AI opportunity. This section is OPTIONAL — only include if canvas data is provided.
**Required Fields:** canvas.pain, canvas.data, canvas.approach, canvas.value, canvas.risks
**Style Patterns:** evidence-based
**Word Count:** 240–400 words

### Prompt Template

```
Generate the AI Breakthrough Canvas section for the hackathon debrief document.

Canvas data:
- Pain: {{canvas.pain}}
- Data: {{canvas.data}}
- Approach: {{canvas.approach}}
- Value: {{canvas.value}}
- Risks: {{canvas.risks}}

Requirements:
1. Present the canvas in a structured format with clear sections.
2. Each canvas dimension should be a subsection with 2-4 bullet points.
3. Connect the canvas elements to the hackathon findings.
4. CRITICAL: Only include canvas data that was actually discussed. Do NOT fill in canvas dimensions with generic content.
5. The canvas should tell a coherent story: pain leads to data need, data enables approach, approach delivers value, risks are managed.
6. Use evidence-based language throughout.
7. This section is OPTIONAL — only generate if canvas data is provided in the source material.

Output the section in {{language}} language.
```

---

## Section: user_flow

**Title (DE):** Benutzerfluss
**Description:** Process flow description showing how the solution works from input to output. This section is OPTIONAL — only include if user flow data is provided.
**Required Fields:** userFlow.inputSources, userFlow.steps, userFlow.outputFormat
**Style Patterns:** evidence-based
**Word Count:** 200–340 words

### Prompt Template

```
Generate the User Flow section for the hackathon debrief document.

User flow data:
- Input sources: {{userFlow.inputSources}}
- Process steps: {{userFlow.steps}}
- Output format: {{userFlow.outputFormat}}

Requirements:
1. Describe the process flow from input to output in clear, numbered steps.
2. For each step, explain: what happens, what technology/method is used, what the output is.
3. Include input sources and their formats.
4. Describe the final output and how the user interacts with it.
5. CRITICAL: Only describe steps that were actually demonstrated or discussed. Do NOT add steps that seem logical but were not part of the hackathon.
6. Use evidence-based language and connect to specific hackathon findings.
7. This section is OPTIONAL — only generate if user flow data is provided in the source material.

Output the section in {{language}} language.
```

---

## Section: conclusion

**Title (DE):** Fazit und Ausblick
**Description:** Summary of findings, recommendations, and next steps. Must include mandatory style patterns.
**Required Fields:** recommendations, nextSteps, company.name
**Style Patterns:** three-pillars, forward-looking, collaborative-tone
**Word Count:** 220–360 words

### Prompt Template

```
Generate the Conclusion section for the hackathon debrief document.

Conclusion information:
- Recommendations: {{recommendations}}
- Next steps: {{nextSteps}}
- Company name: {{company.name}}
- Three pillars phrase: {{threePillarsPhrase}}
- Forward-looking phrase: {{forwardLookingPhrase}}

Requirements:
1. CRITICAL: The conclusion MUST begin with the three pillars phrase: {{threePillarsPhrase}}
   - German: "Während des Hackathons haben wir uns intensiv mit den drei Hauptpfeilern beschäftigt: [pillar 1], [pillar 2] und [pillar 3]."
   - English: "During the hackathon, we focused intensively on the three main pillars: [pillar 1], [pillar 2], and [pillar 3]."
2. Summarize the key findings and their business impact.
3. Present concrete recommendations based on hackathon results.
4. Outline clear next steps with suggested timelines if available.
5. CRITICAL: The conclusion MUST end with the forward-looking phrase: {{forwardLookingPhrase}}
   - German: "Wir würden uns sehr freuen, diese Erfolgsgeschichte gemeinsam mit Ihnen schreiben zu dürfen!"
   - English: "We would be delighted to write this success story together with you!"
6. Use collaborative tone throughout — "wir" (we), "gemeinsam" (together).
7. Connect the conclusion back to the original challenge and goals.
8. Do NOT invent recommendations or next steps not supported by the source data.

Output the section in {{language}} language.
```
