# Spec 03: Study Station Preview Optimization and Generator Architecture Modularization

**Status:** ready-for-agent

## Problem Statement

Users navigating the single-page study station (`index.html`) experience critical rendering and preview failures:
1. When selecting any of the 81 problem entities that currently lack companion markdown notes, the UI displays a blank "No documentation notes" placeholder while the corresponding Python solution code is hidden because `viewMode` defaults to notes-only view.
2. KaTeX mathematical formulas containing subscripts (such as `_`) and operators (such as `*`) are corrupted during client-side rendering because Markdown parsing converts them into italic `<em>` tags before KaTeX executes.
3. The generator script `update_index.py` has grown into a 2,339-line monolithic file that inlines 1,700 lines of CSS/HTML/JS and 500 lines of hardcoded data structures, making maintenance difficult and prone to regression.

## Solution

1. Optimize the SPA viewer in `index.html` to default to split `"dual"` pane view, ensuring Python code and markdown notes are immediately visible side-by-side.
2. Add adaptive viewer fallback: if a problem entity has no markdown notes, automatically maximize the code pane so the solution is immediately readable rather than presenting a blank placeholder.
3. Fix the KaTeX and Markdown rendering pipeline by using math delimiters protection or custom token processing so LaTeX formulas remain intact and render with mathematical precision.
4. Modularize the generator pipeline by separating frontend templates (HTML/CSS/JS) into dedicated asset files, dynamically parsing roadmap data from `ROADMAP.md`, and reducing `update_index.py` into a lightweight compiler under 250 lines.

## User Stories

1. As a LeetCode student, I want to see both the Python code and companion note simultaneously when I open a problem, so that I can study the algorithmic implementation alongside the theoretical walkthrough.
2. As a LeetCode student, I want problems without markdown notes to display their Python code immediately in full pane, so that I never encounter a blank or non-responsive screen.
3. As a student studying time and space complexities, I want mathematical formulas (e.g. $O(\log n)$, $\sum_{i=0}^n$, $a \equiv c \pmod L$) to render with clean typography without corrupted `<em>` italic tags, so that I can accurately read algorithmic formulas.
4. As a developer browsing topics from the Master Roadmap view, I want clicking a problem pill to navigate directly to the dual split-pane workspace with the correct file loaded.
5. As a repository maintainer, I want the generator script to be clean, modular, and concise, so that adding new curriculum topics or updating templates does not require editing a 2,000-line monolithic file.
6. As a CI/CD pipeline, I want automated unit tests to verify that `index.html` compiles cleanly, all problem entities have valid preview content, and mathematical delimiters are preserved without corruption.

## Implementation Decisions

1. **Viewer Default State & Adaptive Pane Sizing**:
   - Change default `viewMode` in the SPA client script from `"notes"` to `"dual"`.
   - In `switchItem(key)`, check if `item.notes` is empty and `item.code` is present. If true and `viewMode` is `"dual"` or `"notes"`, auto-adjust layout to show the code viewer prominently.

2. **KaTeX Pre-Processing & Formula Protection**:
   - Protect LaTeX math delimiters (`$$...$$` and `$...$`) before passing markdown text to `marked.parse()`, replacing math expressions with unique placeholder tokens, parsing markdown, and restoring raw math expressions before invoking KaTeX `renderMathInElement()`.

3. **Generator Architecture Modularization & Asset Separation**:
   - Extract frontend CSS, HTML structure, and client JavaScript into a dedicated `templates/` or asset directory (e.g. `templates/station_template.html`).
   - Extract roadmap parsing into a dynamic parser that ingests `ROADMAP.md` sections directly rather than maintaining a duplicated in-memory Python dictionary.
   - Reduce `update_index.py` to a single-responsibility build runner that reads workspace files, injects JSON payloads into the template, and outputs `index.html`.

4. **Data Model Refactoring**:
   - Refactor `create_document_item` and note generators from loose 18-parameter functions into strongly typed `dataclass` definitions (`DocumentEntity`, `ProblemNoteSpec`).

## Testing Decisions

1. **High-Level Seam (External Behavior Testing)**:
   - Test at the highest possible interface: `update_index.py` end-to-end compilation output (`index.html`).
   - Test suite `tests/test_preview_and_generator.py` asserting:
     - `index.html` contains default `viewMode = "dual"`.
     - KaTeX formula protection logic correctly renders formulas without `<em>` insertion.
     - Dynamic roadmap parser correctly extracts all phases and topics from `ROADMAP.md`.
     - Code length of `update_index.py` is under 350 lines.

## Out of Scope

- Modifying existing Python solution algorithms in `top-100/`, `daily-practice/`, or `luffy/`.
- Changing the 7-section markdown structure standard defined in `AGENTS.md`.
- Converting the SPA to an external React/Vue/Node.js build pipeline (must remain zero-dependency static Python compiler).

## Further Notes

- All changes must strictly follow `AGENTS.md` Core Rule 1 (`.py` immutability) and Core Rule 3 (regenerate `index.html` and verify tests before pushing).
