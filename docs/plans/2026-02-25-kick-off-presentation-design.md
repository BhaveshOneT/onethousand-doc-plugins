# Kick-Off Presentation Skill — Design & Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a new skill in onethousand-doc-plugins that generates branded project kick-off presentation decks (.pptx) from scope documents, sprint design plans (Confluence), and Miro boards.

**Architecture:** Template-based approach using the existing OT corporate PPTX template (derived from sample kick-off decks). A Python script opens the template, adjusts slide count based on use-case count and kick-off type, fills in content from JSON files, and embeds provided images. The SKILL.md orchestrates multi-source input collection, content extraction, confidence scoring, and assembly.

**Tech Stack:** python-pptx, pdfplumber, Pillow, lxml, Graphviz (optional), Confluence MCP, Miro MCP (context_explore/context_get)

---

## Task 1: Create Template PPTX

**Files:**
- Source: `/Users/bhaveshy/Desktop/Kick Off Slides/20250321 Haba UC4 Projekt Kick-Off.pptx`
- Create: `docs-generator/skills/kick-off-presentation/assets/templates/ot-kickoff-template.pptx`

**Approach:** Use python-pptx to open the HABA UC4 deck, strip all content-specific text (replace with template markers like `{{PROJECT_TITLE}}`), remove content-specific images, preserve all shapes/layouts/formatting/tables. Save as template.

The template should have 20 base slides matching the standard kick-off structure. The generator script will duplicate/remove slides as needed for multi-UC or rollout variants.

---

## Task 2: Write generate_kickoff_pptx.py

**Files:**
- Create: `docs-generator/skills/kick-off-presentation/scripts/generate_kickoff_pptx.py`

**Approach:** Follow the same patterns as `generate_hackathon_pptx.py`:
- argparse CLI: `--template`, `--variables`, `--content`, `--output`, `--verbose`
- Load variables.json and content.json
- Open template, fill slides with content
- Handle multi-UC (duplicate Pain×Data slides)
- Handle rollout variant (skip hackathon/step-by-step)
- Build Gantt table from timeline data
- Fill sprint goal cards
- Embed images where provided, leave placeholders where not
- Brand constants: same as hackathon skill

**Key slides the script must handle:**
- Slide 0: Cover (Title Lime + one Logo, idx 40) — fill title, subtitle, date; embed client logo
- Slides 1-2, 4, 9, 13, 16, 18: TOC/Agenda dividers (idx 78) — fill section names, page numbers, highlight active section
- Slide 3: Check-in (Bullet Points Lime, idx 0) — fill questions, embed GIF
- Slide 5: Pain×Data (Bullet Points Lime, idx 0) — fill pain/data/solution bullets, embed GIF
- Slide 6: Hackathon (DEFAULT, idx 79) — embed Miro board images
- Slide 7: Step by step (Bullet Points Lime, idx 0) — fill phase labels, embed screenshots
- Slide 8: Architecture (Bullet Points Lime, idx 0) — embed architecture diagram image
- Slide 10: Sprint goals (1_Bullet Points Lime, idx 69) — fill sprint cards
- Slide 11: Timeline/Gantt (Calendar Lime, idx 22) — fill table cells
- Slide 12: Progress/Risks (Bullet Points Lime, idx 0) — fill risk bullets
- Slides 14-15: Participants/Meetings (Bullet Points Lime, idx 0) — fill meeting details
- Slide 17: Discussion (Bullet Points Lime, idx 0) — mostly static
- Slide 19: Thank you (Bullet Points Lime, idx 0) — mostly static

---

## Task 3: Write SKILL.md

**Files:**
- Create: `docs-generator/skills/kick-off-presentation/SKILL.md`

**Structure:** Follow exact plugin conventions:
- YAML frontmatter (name, description with triggers, license)
- Phase 1: Input Collection (scope doc, sprint design, optional images, language, kick-off type)
- Phase 2: Source Enrichment (read scope doc, Confluence sprint design, auto Miro search, read reference files in parallel)
- Phase 3: Content Extraction & Anti-Hallucination
- Phase 4: Content Generation with Confidence Scoring (variables.json + content.json)
- Phase 5: Presentation Assembly (run generator script)
- Phase 6: Visual QA & Delivery

---

## Task 4: Write Reference Files

**Files:**
- Copy: `docs-generator/skills/kick-off-presentation/references/anti-hallucination-rules.md` (from scope-document-generator)
- Create: `docs-generator/skills/kick-off-presentation/references/section-templates-en.md`
- Create: `docs-generator/skills/kick-off-presentation/references/section-templates-de.md`
- Create: `docs-generator/skills/kick-off-presentation/references/slide-structure-guide.md`

---

## Task 5: Update package.json

**Files:**
- Modify: `docs-generator/package.json`

Add keywords: "kick-off", "kick-off-presentation", "project-kick-off", "projekt-kick-off"

---

## Execution Order

Tasks 1-4 can be executed in parallel (no dependencies).
Task 5 is a quick final step.
