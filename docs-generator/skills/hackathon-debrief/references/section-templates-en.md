# Hackathon Debrief Section Templates — English

Prompt templates, word budgets, format specifications, and quality criteria for each section of the hackathon debrief document.

---

## Section: background

**Title (EN):** Background
**Description:** Company context, industry insight, AI opportunity, and One Thousand partnership.
**Required Fields:** company.name, company.industry, company.background, company.aiOpportunity
**Style Patterns:** ai-journey, collaborative-tone
**Word Count:** 170–300 words
**Format:** 4 bullet points (use markdown `- ` list), NOT prose paragraphs.

### Format Structure

1. **Industry context** — 1-2 sentences of genuine industry insight explaining WHY AI matters in this specific sector
2. **Company specifics** — what they do, products/services, market position, scale indicators (employee count, locations, revenue if available)
3. **AI opportunity** — what specific process/challenge makes AI relevant NOW for this company
4. **Partnership** — how One Thousand is working with them and why this hackathon exists

### Prompt Template

```
Generate the Background section for the hackathon debrief document.

Company information:
- Company name: {{company.name}}
- Industry: {{company.industry}}
- Background: {{company.background}}
- AI opportunity: {{company.aiOpportunity}}

Format: Write EXACTLY 4 bullet points (markdown `- ` list):
1. Industry context — open with 1-2 sentences of genuine industry insight relevant to WHY AI matters for this company's sector. This should be accurate, non-generic knowledge.
2. Company specifics — what they do, products/services, market position, scale indicators.
3. AI opportunity — what specific process or challenge makes AI relevant NOW.
4. Partnership — how One Thousand is working with them and why.

Quality rules:
- Each bullet must contain at least 2 specific facts from the source data.
- NO generic filler like "the company is on an exciting AI journey" — let specifics speak.
- Use "AI journey" / "KI-Reise" framing naturally, not as a forced phrase.
- CRITICAL: Only use facts from the provided source data. Do NOT invent company details, employee numbers, or revenue figures.

Output the section in {{language}} language.
```

---

## Section: hackathon_structure

**Title (EN):** Hackathon
**Description:** Event details including dates, location, participant count, day structure, and atmosphere.
**Required Fields:** metadata.title, metadata.date, metadata.location, metadata.format
**Style Patterns:** collaborative-tone
**Word Count:** 160–280 words
**Format:** Opening paragraph → "Day 1: [subtitle]" (bold) → bullet list → "Day 2: [subtitle]" (bold) → bullet list → context paragraph → check-in/expectations paragraph → appreciation note.

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
- **Day 1: [subtitle]** (bold heading) → bullet list of what actually happened
- **Day 2: [subtitle]** (bold heading) → bullet list of what actually happened
- Context paragraph about the working environment or check-in/expectations
- End with a genuine appreciation note about team collaboration.

Quality rules:
- Day structure should list what ACTUALLY happened, not generic agenda items.
- Include specific activities, workshops, or milestones from the source data.
- Do NOT invent agenda items or activities not mentioned in the source data.
- Keep tone professional but warm — convey productive atmosphere.

Output the section in {{language}} language.
```

---

## Section: challenge

**Title (EN):** Challenge
**Description:** Use-case label, pain points with evidence and business impact, summary synthesis.
**Required Fields:** useCases[0].painPoints, useCases[0].challenge, useCases[0].currentProcess
**Style Patterns:** evidence-based
**Word Count:** 220–360 words
**Format:** "Use-case: [use case title]" (bold label) → introductory paragraph → "Pain" (bold label) → numbered paragraphs (1. 2. 3. ...) each with bold opening phrase + detailed explanation → summary paragraph.

### Prompt Template

```
Generate the Challenge section for the hackathon debrief document.

Challenge information:
- Use case title: {{useCases[0].title}}
- Pain points: {{useCases[0].painPoints}}
- Core challenge: {{useCases[0].challenge}}
- Current process: {{useCases[0].currentProcess}}

Format:
- Start with: **Use-case: [exact use case title from source]**
- Introductory paragraph framing the business context
- **Pain** (bold label on its own line)
- Numbered pain points (1. 2. 3. ...) where each follows the pattern:
  **Bold opening phrase.** Specific explanation with numbers/evidence and business impact.
- Summary paragraph synthesizing all pain points into a single business problem statement.

Quality rules:
- Each numbered pain point MUST contain specific details: numbers, percentages, time durations, system names, or concrete examples from the source.
- WRONG: "The process is slow and error-prone."
- RIGHT: "**High manual effort.** With approximately 50 quotations per day, each requiring 2–3 minutes of experienced judgment for steel grade interpretation..."
- The summary paragraph should synthesize all pains into one coherent business problem — situation → tension → implication.
- Frame challenges as opportunities for improvement, not criticisms.
- CRITICAL: Every pain point must come directly from the source data.

Output the section in {{language}} language.
```

---

## Section: goal

**Title (EN):** Goal
**Description:** Primary strategic goal, secondary goals, and success criteria.
**Required Fields:** useCases[0].goal, useCases[0].title, useCases[0].expectedBenefits
**Style Patterns:** collaborative-tone, evidence-based
**Word Count:** 170–300 words
**Format:** Primary strategic goal paragraph → solution description paragraph → "During the hackathon, we aimed to address the following secondary goals:" → numbered goals (1. 2. 3.) → "Success criteria for this use case include:" → bullet list.

### Prompt Template

```
Generate the Goal section for the hackathon debrief document.

Goal information:
- Use case title: {{useCases[0].title}}
- Primary goal: {{useCases[0].goal}}
- Expected benefits: {{useCases[0].expectedBenefits}}
- Success criteria: {{useCases[0].successCriteria}}

Format:
- Primary strategic goal paragraph — frame the hackathon in the company's broader strategy, not just "automate X."
- Solution description paragraph — what the proposed solution would look like.
- "During the hackathon, we aimed to address the following secondary goals:" → numbered list (1. 2. 3.)
- "Success criteria for this use case include:" → bullet list of testable criteria.

Quality rules:
- The primary goal should connect to business strategy, not just technical automation.
- Secondary goals should be specific and measurable.
- Success criteria should be testable — could someone check if they were met?
- CRITICAL: Do NOT invent goals or benefits not present in the source data.

Output the section in {{language}} language.
```

---

## Section: data

**Title (EN):** Data
**Description:** Data sources with formats, volumes, and quality observations.
**Required Fields:** useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 190–320 words
**Format:** "The following data sources were available for the hackathon:" → hierarchical bullet list where each top-level bullet is a data source category (bold) followed by sub-bullets with specific details.

### Prompt Template

```
Generate the Data section for the hackathon debrief document.

Data sources:
{{useCases[0].dataSources}}

Format:
- Opening line: "The following data sources were available for the hackathon:"
- Hierarchical bullet list:
  - **Data source category** (bold top-level bullet)
    - Sub-bullet: what it contains
    - Sub-bullet: format (JSON/PDF/Excel/API/etc.)
    - Sub-bullet: approximate volume or scope
    - Sub-bullet: quality observations (if any)

Quality rules:
- For each data source, include: what it contains, format, approximate volume or scope, and any quality observations.
- Be very specific — "Around 15 inquiry emails in different languages (Italian, French, German)" is better than "Customer inquiry data."
- CRITICAL: Only list data sources explicitly mentioned in the source material. Do NOT assume the existence of data sources.
- If data volumes or formats are specified, include them with exact numbers.

Output the section in {{language}} language.
```

---

## Section: approach

**Title (EN):** Approach
**Description:** Methodology, architecture, security considerations, technologies, and processing steps.
**Required Fields:** useCases[0].proposedSolution, useCases[0].technicalDetails, useCases[0].dataSources
**Style Patterns:** evidence-based
**Word Count:** 220–360 words
**Format:** Opening sentence → "Methodology:" paragraph → "Initial architecture draft for the MVP:" paragraph + figure reference (if architecture image provided) → "Security:" paragraph → "Technologies used:" → bullet list → "Processing steps:" → numbered list (7-10 steps) → summary paragraph.

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
- Opening sentence describing the overall approach
- **Methodology:** paragraph explaining the chosen method and rationale
- **Initial architecture draft for the MVP:** paragraph describing the architecture. If an architecture diagram is provided, reference it as "Fig N:" with a caption.
- **Security:** paragraph covering data privacy and security considerations
- **Technologies used:** bullet list of specific technologies by name
- **Processing steps:** numbered list (7-10 steps) tracing the complete flow from input to output
- Summary paragraph

Quality rules:
- Mention specific technologies by name — never use vague terms like "modern AI tools."
- Include security/privacy considerations if mentioned in source data.
- Processing steps should trace the COMPLETE flow from raw input to final output.
- CRITICAL: Only mention technologies, tools, and methods documented in the source material.

Output the section in {{language}} language.
```

---

## Section: results

**Title (EN):** Results
**Description:** Prototype description, demo outcomes, participant feedback, feasibility statement.
**Required Fields:** useCases[0].results, useCases[0].expectedBenefits
**Style Patterns:** evidence-based
**Word Count:** 220–340 words
**Format:** Opening sentence → "Developed prototype:" description paragraph → figure references for screenshots → extra features paragraph (if any) → prototype capability descriptions → "Live demo:" paragraph → summary paragraph.

### Prompt Template

```
Generate the Results section for the hackathon debrief document.

Results information:
- Results: {{useCases[0].results}}
- Expected benefits: {{useCases[0].expectedBenefits}}
- Demo observations: {{useCases[0].demoResults}}
- Participant feedback: {{useCases[0].participantFeedback}}

Format:
- Opening sentence establishing the results context
- **Developed prototype:** description paragraph of what was built and how it works
- Figure references for screenshots/images if available (use "Fig N:" with captions)
- Extra features or bonus capabilities paragraph (if any were discovered)
- Prototype capability descriptions
- **Live demo:** paragraph describing what was shown and reactions
- Summary paragraph with clear feasibility statement

Quality rules:
- Focus on what was DEMONSTRATED, not what was planned.
- If screenshots/images are available, embed them with "Fig N:" captions.
- Mention any surprise/bonus features discovered during the hackathon.
- Synthesize participant feedback into coherent narrative — don't list raw feedback verbatim.
- End with a clear statement of feasibility.
- CRITICAL: Every metric MUST come directly from the source data. Do NOT invent or estimate numbers.

Output the section in {{language}} language.
```

---

## Section: canvas

**Title (EN):** AI Breakthrough Canvas
**Description:** Structured canvas analysis of the AI opportunity. This section is OPTIONAL — only include if the user explicitly provides structured canvas data.
**Required Fields:** canvas.pain, canvas.data, canvas.approach, canvas.value, canvas.risks
**Style Patterns:** evidence-based
**Word Count:** 240–400 words

**Note:** This section is NOT a default section. Only generate if canvas data is explicitly provided in the source material.

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
4. CRITICAL: Only include canvas data that was actually discussed.
5. This section is OPTIONAL — only generate if canvas data is provided.

Output the section in {{language}} language.
```

---

## Section: user_flow

**Title (EN):** User Flow
**Description:** Process flow description showing how the solution works. This section is OPTIONAL — only include if the user explicitly provides user flow data.
**Required Fields:** userFlow.inputSources, userFlow.steps, userFlow.outputFormat
**Style Patterns:** evidence-based
**Word Count:** 200–340 words

**Note:** This section is NOT a default section. Only generate if user flow data is explicitly provided in the source material.

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
3. CRITICAL: Only describe steps that were actually demonstrated or discussed.
4. This section is OPTIONAL — only generate if user flow data is provided.

Output the section in {{language}} language.
```

---

## Section: conclusion

**Title (EN):** Conclusion
**Description:** Strategic summary covering feasibility, vision, competitive value, and partnership commitment.
**Required Fields:** recommendations, nextSteps, company.name
**Style Patterns:** forward-looking, collaborative-tone
**Word Count:** 220–360 words
**Format:** 4 paragraphs: (1) Feasibility proof, (2) Broader vision, (3) Strategic/competitive value, (4) Partnership commitment + forward-looking ending.

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
1. **Feasibility proof** — "The hackathon has proven that AI can deliver tangible value in {{company.name}}'s daily operations..." Summarize what was demonstrated and proven.
2. **Broader vision** — Beyond the hackathon use case, what transformation roadmap opens up? What adjacent processes or capabilities could follow?
3. **Strategic/competitive value** — Why this investment matters in the company's market. Frame AI adoption as competitive advantage, not just efficiency.
4. **Partnership commitment + forward-looking ending** — Express commitment to the partnership and end with the forward-looking phrase: {{forwardLookingPhrase}}

Quality rules:
- NO three-pillars opening required. The three-pillars structure is optional — use it ONLY if it naturally fits.
- NO bullet lists of next steps — that's too tactical. Next steps are discussed in the meeting, not the document.
- The conclusion should read like a strategic executive summary that makes the reader excited about the future.
- Every paragraph should contain specific references to this hackathon's findings.
- The strategic paragraph should include genuine industry context — e.g., "In a commoditized market where the product itself offers limited differentiation, investing in AI-driven process excellence becomes a genuine competitive advantage."
- CRITICAL: The conclusion MUST end with the forward-looking phrase.
- Do NOT invent recommendations not supported by the source data.

Output the section in {{language}} language.
```
