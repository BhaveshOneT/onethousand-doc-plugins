# Hackathon Debrief Abschnitt-Templates — Deutsch

Prompt-Vorlagen, Wortbudgets, Formatspezifikationen und Qualitätskriterien für jeden Abschnitt des Hackathon-Debrief-Dokuments.

---

## Section: background

**Title (DE):** Hintergrund
**Description:** Company context, industry insight, AI opportunity, and One Thousand partnership.
**Required Fields:** company.name, company.industry, company.background, company.aiOpportunity
**Style Patterns:** ai-journey, collaborative-tone
**Word Count:** 170–300 words
**Format:** 4 bullet points (use markdown `- ` list), NOT prose paragraphs.

### Format Structure

1. **Branchenkontext** — 1-2 Sätze echte Branchenkenntnis, die erklären, WARUM KI in diesem Sektor relevant ist
2. **Unternehmensspezifika** — Produkte/Dienstleistungen, Marktposition, Kennzahlen (Mitarbeiter, Standorte, Umsatz falls vorhanden)
3. **KI-Chance** — welcher spezifische Prozess oder welche Herausforderung macht KI JETZT relevant
4. **Partnerschaft** — wie One Thousand mit dem Unternehmen zusammenarbeitet und warum

### Prompt Template

```
Generate the Background section for the hackathon debrief document.

Company information:
- Company name: {{company.name}}
- Industry: {{company.industry}}
- Background: {{company.background}}
- AI opportunity: {{company.aiOpportunity}}

Format: Write EXACTLY 4 bullet points (markdown `- ` list):
1. Branchenkontext — open with 1-2 sentences of genuine industry insight relevant to WHY AI matters for this company's sector.
2. Unternehmensspezifika — what they do, products/services, market position, scale indicators.
3. KI-Chance — what specific process or challenge makes AI relevant NOW.
4. Partnerschaft — how One Thousand is working with them and why.

Quality rules:
- Each bullet must contain at least 2 specific facts from the source data.
- NO generic filler like "das Unternehmen befindet sich auf einer spannenden KI-Reise" — let specifics speak.
- Use "KI-Reise" framing naturally, not as a forced phrase.
- CRITICAL: Only use facts from the provided source data. Do NOT invent company details, employee numbers, or revenue figures.

Output the section in {{language}} language.
```

---

## Section: hackathon_structure

**Title (DE):** Hackathon
**Description:** Event details including dates, location, participant count, day structure, and atmosphere.
**Required Fields:** metadata.title, metadata.date, metadata.location, metadata.format
**Style Patterns:** collaborative-tone
**Word Count:** 160–280 words
**Format:** Opening paragraph → "Tag 1: [Untertitel]" (bold) → bullet list → "Tag 2: [Untertitel]" (bold) → bullet list → context paragraph → check-in/expectations paragraph → appreciation note.

### Prompt Template

```
Generate the Hackathon section for the debrief document.

Event details:
- Title: {{metadata.title}}
- Date: {{metadata.date}}
- Location: {{metadata.location}}
- Format: {{metadata.format}}
- Participants: {{participants}}

Format:
- Opening paragraph: Establish date, location, participant count, and collaborative atmosphere in ONE sentence.
- **Tag 1: [Untertitel]** (bold heading) → bullet list of what actually happened
- **Tag 2: [Untertitel]** (bold heading) → bullet list of what actually happened
- Context paragraph about working environment or check-in/expectations
- End with a genuine appreciation note about team collaboration.

Quality rules:
- Day structure should list what ACTUALLY happened, not generic agenda items.
- Include specific activities, workshops, or milestones from the source data.
- Do NOT invent agenda items or activities not mentioned in the source data.
- Use collaborative tone — "Gemeinsam mit...", "Zusammen mit der wunderbaren Unterstützung durch Ihr Team..."

Output the section in {{language}} language.
```

---

## Section: challenge

**Title (DE):** Herausforderung
**Description:** Use-case label, pain points with evidence and business impact, summary synthesis.
**Required Fields:** useCases[0].painPoints, useCases[0].challenge, useCases[0].currentProcess
**Style Patterns:** evidence-based
**Word Count:** 220–360 words
**Format:** "Use-case: [Titel]" (bold label) → introductory paragraph → "Pain" (bold label) → numbered paragraphs (1. 2. 3. ...) each with bold opening phrase + detailed explanation → summary paragraph.

### Prompt Template

```
Generate the Challenge section for the hackathon debrief document.

Challenge information:
- Use case title: {{useCases[0].title}}
- Pain points: {{useCases[0].painPoints}}
- Core challenge: {{useCases[0].challenge}}
- Current process: {{useCases[0].currentProcess}}

Format:
- Start with: **Use-case: [exakter Titel des Anwendungsfalls aus der Quelle]**
- Einleitender Absatz mit dem geschäftlichen Kontext
- **Pain** (bold label on its own line)
- Numbered pain points (1. 2. 3. ...) where each follows the pattern:
  **Fettgedruckte Eröffnungsphrase.** Spezifische Erklärung mit Zahlen/Belegen und geschäftlicher Auswirkung.
- Summary paragraph synthesizing all pain points into a single business problem statement.

Quality rules:
- Each numbered pain point MUST contain specific details: numbers, percentages, time durations, system names, or concrete examples.
- WRONG: "Der Prozess ist langsam und fehleranfällig."
- RIGHT: "**Hoher manueller Aufwand.** Bei ca. 50 Angeboten pro Tag, die jeweils 2–3 Minuten erfahrener Beurteilung für Stahlsorteninterpretation, Einheitenumrechnung und Toleranzabgleich erfordern..."
- The summary should synthesize all pains into one coherent business problem.
- CRITICAL: Every pain point must come directly from the source data.

Output the section in {{language}} language.
```

---

## Section: goal

**Title (DE):** Ziel
**Description:** Primary strategic goal, secondary goals, and success criteria.
**Required Fields:** useCases[0].goal, useCases[0].title, useCases[0].expectedBenefits
**Style Patterns:** collaborative-tone, evidence-based
**Word Count:** 170–300 words
**Format:** Primary strategic goal paragraph → solution description paragraph → "Im Rahmen des Hackathons haben wir folgende sekundäre Ziele verfolgt:" → numbered goals (1. 2. 3.) → "Erfolgskriterien für diesen Anwendungsfall:" → bullet list.

### Prompt Template

```
Generate the Goal section for the hackathon debrief document.

Goal information:
- Use case title: {{useCases[0].title}}
- Primary goal: {{useCases[0].goal}}
- Expected benefits: {{useCases[0].expectedBenefits}}
- Success criteria: {{useCases[0].successCriteria}}

Format:
- Primary strategic goal paragraph — frame hackathon in company's broader strategy.
- Solution description paragraph.
- "Im Rahmen des Hackathons haben wir folgende sekundäre Ziele verfolgt:" → numbered list (1. 2. 3.)
- "Erfolgskriterien für diesen Anwendungsfall:" → bullet list of testable criteria.

Quality rules:
- The primary goal should connect to business strategy, not just technical automation.
- Secondary goals should be specific and measurable.
- Success criteria should be testable.
- CRITICAL: Do NOT invent goals or benefits not present in the source data.

Output the section in {{language}} language.
```

---

## Section: data

**Title (DE):** Daten
**Description:** Data sources with formats, volumes, and quality observations.
**Required Fields:** useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 190–320 words
**Format:** "Für den Hackathon standen folgende Datenquellen zur Verfügung:" → hierarchical bullet list where each top-level bullet is a data source category (bold) followed by sub-bullets with specific details.

### Prompt Template

```
Generate the Data section for the hackathon debrief document.

Data sources:
{{useCases[0].dataSources}}

Format:
- Opening: "Für den Hackathon standen folgende Datenquellen zur Verfügung:"
- Hierarchical bullet list:
  - **Datenquellenkategorie** (bold top-level bullet)
    - Sub-bullet: Inhalt
    - Sub-bullet: Format (JSON/PDF/Excel/API/etc.)
    - Sub-bullet: ungefähres Volumen oder Umfang
    - Sub-bullet: Qualitätsbeobachtungen (falls vorhanden)

Quality rules:
- For each data source, include: what it contains, format, approximate volume, and quality observations.
- Be very specific — "Rund 15 Anfrage-E-Mails in verschiedenen Sprachen (Italienisch, Französisch, Deutsch)" is better than "Kundenanfragedaten."
- CRITICAL: Only list data sources explicitly mentioned in the source material.

Output the section in {{language}} language.
```

---

## Section: approach

**Title (DE):** Ansatz
**Description:** Methodology, architecture, security considerations, technologies, and processing steps.
**Required Fields:** useCases[0].proposedSolution, useCases[0].technicalDetails, useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 220–360 words
**Format:** Opening sentence → "Methodik:" paragraph → "Erster Architekturentwurf für das MVP:" paragraph + figure reference → "Sicherheit:" paragraph → "Verwendete Technologien:" → bullet list → "Verarbeitungsschritte:" → numbered list (7-10 steps) → summary paragraph.

### Prompt Template

```
Generate the Approach section for the hackathon debrief document.

Solution information:
- Proposed solution: {{useCases[0].proposedSolution}}
- Technical details: {{useCases[0].technicalDetails}}
- Data sources used: {{useCases[0].dataSources}}
- Architecture: {{useCases[0].architecture}}
- Security considerations: {{useCases[0].security}}

Format:
- Opening sentence
- **Methodik:** paragraph explaining chosen method and rationale
- **Erster Architekturentwurf für das MVP:** paragraph describing architecture. If diagram provided, reference as "Abb. N:" with caption.
- **Sicherheit:** paragraph covering data privacy and security
- **Verwendete Technologien:** bullet list of specific technologies
- **Verarbeitungsschritte:** numbered list (7-10 steps) tracing complete flow
- Summary paragraph

Quality rules:
- Mention specific technologies by name.
- Include security/privacy considerations if in source data.
- Processing steps should trace COMPLETE flow from input to output.
- CRITICAL: Only mention technologies documented in source material.

Output the section in {{language}} language.
```

---

## Section: results

**Title (DE):** Ergebnisse
**Description:** Prototype description, demo outcomes, participant feedback, feasibility statement.
**Required Fields:** useCases[0].results, useCases[0].expectedBenefits
**Style Patterns:** evidence-based
**Word Count:** 220–340 words
**Format:** Opening sentence → "Entwickelter Prototyp:" description → figure references → extra features paragraph → prototype capabilities → "Live-Demo:" paragraph → summary paragraph.

### Prompt Template

```
Generate the Results section for the hackathon debrief document.

Results information:
- Results: {{useCases[0].results}}
- Expected benefits: {{useCases[0].expectedBenefits}}
- Demo observations: {{useCases[0].demoResults}}
- Participant feedback: {{useCases[0].participantFeedback}}

Format:
- Opening sentence
- **Entwickelter Prototyp:** description of what was built
- Figure references for screenshots (use "Abb. N:" with captions)
- Extra features paragraph (if any bonus capabilities)
- Prototype capability descriptions
- **Live-Demo:** paragraph describing what was shown and reactions
- Summary paragraph with clear feasibility statement

Quality rules:
- Focus on what was DEMONSTRATED, not what was planned.
- Synthesize participant feedback into coherent narrative — don't list raw feedback verbatim.
- End with clear feasibility statement.
- CRITICAL: Every metric MUST come directly from source data.

Output the section in {{language}} language.
```

---

## Section: canvas

**Title (DE):** AI Breakthrough Canvas
**Description:** Structured canvas analysis. OPTIONAL — only include if user explicitly provides canvas data.
**Required Fields:** canvas.pain, canvas.data, canvas.approach, canvas.value, canvas.risks
**Style Patterns:** evidence-based
**Word Count:** 240–400 words

**Note:** NOT a default section. Only generate if canvas data is explicitly provided.

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
1. Present canvas in structured format with clear sections.
2. Each dimension: subsection with 2-4 bullet points.
3. CRITICAL: Only include canvas data actually discussed.
4. OPTIONAL — only generate if canvas data is provided.

Output the section in {{language}} language.
```

---

## Section: user_flow

**Title (DE):** Benutzerfluss
**Description:** Process flow description. OPTIONAL — only include if user explicitly provides user flow data.
**Required Fields:** userFlow.inputSources, userFlow.steps, userFlow.outputFormat
**Style Patterns:** evidence-based
**Word Count:** 200–340 words

**Note:** NOT a default section. Only generate if user flow data is explicitly provided.

### Prompt Template

```
Generate the User Flow section for the hackathon debrief document.

User flow data:
- Input sources: {{userFlow.inputSources}}
- Process steps: {{userFlow.steps}}
- Output format: {{userFlow.outputFormat}}

Requirements:
1. Describe process flow in clear, numbered steps.
2. CRITICAL: Only describe steps actually demonstrated.
3. OPTIONAL — only generate if user flow data is provided.

Output the section in {{language}} language.
```

---

## Section: conclusion

**Title (DE):** Fazit
**Description:** Strategic summary covering feasibility, vision, competitive value, and partnership commitment.
**Required Fields:** recommendations, nextSteps, company.name
**Style Patterns:** forward-looking, collaborative-tone
**Word Count:** 220–360 words
**Format:** 4 paragraphs: (1) Machbarkeitsnachweis, (2) Breitere Vision, (3) Strategischer/wettbewerblicher Wert, (4) Partnerschaftsbekenntnis + zukunftsorientierter Abschluss.

### Prompt Template

```
Generate the Conclusion section for the hackathon debrief document.

Conclusion information:
- Key findings: {{keyFindings}}
- Recommendations: {{recommendations}}
- Company name: {{company.name}}
- Industry context: {{company.industry}}
- Forward-looking phrase: {{forwardLookingPhrase}}

Format — Write EXACTLY 4 paragraphs:
1. **Machbarkeitsnachweis** — "Der Hackathon hat gezeigt, dass KI einen konkreten Mehrwert in den täglichen Abläufen von {{company.name}} liefern kann..." Zusammenfassung des Gezeigten und Bewiesenen.
2. **Breitere Vision** — Über den Hackathon-Anwendungsfall hinaus: Welche Transformations-Roadmap eröffnet sich? Welche angrenzenden Prozesse oder Fähigkeiten könnten folgen?
3. **Strategischer/wettbewerblicher Wert** — Warum diese Investition im Marktumfeld des Unternehmens wichtig ist. KI-Adoption als Wettbewerbsvorteil, nicht nur Effizienz.
4. **Partnerschaftsbekenntnis + zukunftsorientierter Abschluss** — Bekenntnis zur Partnerschaft, enden mit: {{forwardLookingPhrase}}

Quality rules:
- NO three-pillars opening required. Use ONLY if it naturally fits.
- NO bullet lists of next steps — too tactical.
- The conclusion should read like a strategic executive summary.
- Include genuine industry context in the strategic paragraph.
- CRITICAL: MUST end with forward-looking phrase.
- Do NOT invent recommendations not supported by source data.

Output the section in {{language}} language.
```
