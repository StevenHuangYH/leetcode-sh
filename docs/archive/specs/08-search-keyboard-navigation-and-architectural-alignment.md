# Spec 08: Search Keyboard Navigation, Precision Filtering, and Architectural Smells Alignment

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Users navigating the `leetcode-sh` Study Station via keyboard face friction when filtering problems: pressing `Enter` in the search box does not automatically select the top matched result or transfer keyboard focus to the notes pane, forcing manual mouse clicks to begin reading. Furthermore, numeric searches without strict problem-identifier isolation surface false-positive matches (such as matching arbitrary numbers inside markdown note bodies or substring matches like problem `1` matching `100`), diluting search precision. In addition, clearing a search query causes the sidebar tree to reset its scroll position to the top, losing the learner's active context.

Behind the scenes, architectural code smells identified during codebase review—such as `switchItem` polluting the global `viewMode` state when encountering code-only problems, feature envy in graph compilation, duplicate static difficulty lookups in README synchronization, and missing hook setup instructions in repository documentation—accumulate technical debt and degrade maintainability across compiler modules.

---

## Solution

1. **Instant Keyboard Selection & Focus Transfer**: Equip the client search engine with `Enter` key handling. When the user presses `Enter` inside the search bar, the top filtered `.problem-item` is automatically selected, smoothly scrolled into the sidebar viewport, and DOM focus is routed to the notes viewer (`tabIndex = -1`) for direct arrow/space key scrolling and distraction-free active recall.
2. **Problem-Identifier Precision Filtering**: Upgrade search matching logic to isolate exact problem number tokens (`\b\d+\b`) against canonical problem numbers and title stems, eliminating false-positive number matches against markdown prose.
3. **Active Selection & Scroll Restoration**: Preserve and restore the active problem item in the sidebar viewport when clearing the search box so that user navigation context is never lost.
4. **Global `viewMode` State Isolation**: Ensure fallback rendering for code-only problems displays instructional cues without mutating the user's global `viewMode` preference, preserving notes-first viewing when switching back to problems with notes.
5. **Compiler Smell Elimination & Dynamic Metadata Sourcing**:
   - Encapsulate search blob generation within `DocumentEntity` domain methods.
   - Refactor README synchronization to source difficulty statistics and counts dynamically from `ProblemCollector`, eliminating hardcoded summary counts and raw table replacement tuples.
   - Introduce typed `FilePairing` dataclasses in `ProblemCollector`.
6. **Version-Controlled Git Hooks & Setup Instructions**: Establish a tracked `.githooks/pre-commit` script in the repository and document the hook activation command in repository setup guides.

---

## User Stories

1. As a keyboard-first learner, I want pressing `Enter` in the search bar to immediately activate the top matching problem, so that I can switch problems without touching the mouse.
2. As a keyboard-first learner, I want pressing `Enter` in the search bar to transfer focus to the notes viewer pane, so that I can immediately scroll through the algorithmic walkthrough using Up/Down arrow keys or the Space bar.
3. As an algorithmic student searching for problem `1` or `15`, I want exact numeric ID matches prioritized over substring containment (e.g. not matching `100` or `153`), so that I find single and double-digit problems instantly.
4. As an algorithmic student searching for a number, I want search to match problem numbers and titles rather than arbitrary numbers embedded in note explanations, so that search results remain highly relevant.
5. As a user clearing a search query, I want the sidebar tree to restore its previous active selection and scroll position seamlessly, so that my navigation context is never lost.
6. As a learner navigating between problems with and without companion notes, I want opening a code-only problem to not permanently lock the workspace into code view, so that subsequent problems with notes open in notes-first view as expected.
7. As a developer maintaining the study station compiler, I want graph construction to utilize clean entity domain methods rather than feature envy property unpacking, so that schema modifications don't break graph compilation.
8. As a developer synchronizing documentation tables, I want README generators to share the single source of truth for problem difficulties from the compiler collector, so that difficulty ratings never drift between views.
9. As a developer running README synchronization, I want difficulty totals, note counts, and percentages to be calculated dynamically from collected problem entities, so that adding new problems requires zero manual arithmetic.
10. As a repository contributor, I want git pre-commit hooks to be version-controlled in the repository, so that note validation and index rebuild checks execute reliably across development environments.
11. As a new contributor onboarding to the repository, I want clear git hook activation instructions in the setup documentation, so that my local commits automatically adhere to repository quality gates.

---

## Implementation Decisions

### 1. Client Search Keyboard Contract & Focus Routing
- Attach an explicit `keydown` listener to the search input:
  - On `Enter`: query the first visible `.problem-item` (or `.nav-item[data-key]`), invoke `switchItem(topMatchKey, false)`, scroll the item into view, and call `document.getElementById("notesViewer").focus()`.
  - Ensure `#notesViewer` has `tabIndex="-1"` and `:focus-visible` styling is suppressed to maintain dark-mode IDE aesthetics.
- In tree rendering, explicitly tag all problem rows with both `nav-item` and `problem-item` classes so DOM queries distinguish problems from folder headers and root document nodes.
- In `clearSearch()`, after re-rendering the unfiltered tree, locate the currently active item and invoke `scrollIntoView({ block: "nearest" })`.

### 2. Precise Numeric Search Matching
- In `matchesSearchQuery`, tokenize the query by whitespace:
  - If a token is entirely numeric (`^\d+$`), match it against the canonical problem number extracted from `lc_num` or title identifier (`\b0*${token}\b`).
  - Non-numeric tokens continue to match against the aggregated `search_blob` across title, slug, category, and tags.

### 3. Non-Mutating Fallback in `switchItem`
- When `switchItem` is invoked on an item that has code but no companion note, render an informative placeholder inside `#notesViewer` directing the user to code/dual view.
- Strictly avoid executing `setViewMode("code")` in fallback branches to ensure the global `viewMode` variable remains unchanged.

### 4. Compiler Domain Encapsulation & Dynamic README Sync
- Equip `DocumentEntity` with a factory method `create_problem` that automatically computes `search_blob` from title, slug, tags, and category properties.
- In `ProblemCollector`, model code/note file pairings via a typed `FilePairing` dataclass (`stem`, `py_file`, `md_file`).
- Refactor `scripts/sync_readme.py` to source all problem entities dynamically from `ProblemCollector.collect()`, calculating Easy, Medium, and Hard counts, note totals, percentages, and problem count badges directly from collected data without hardcoded dictionary counts.

### 5. Version-Controlled Pre-Commit Hooks
- Establish `.githooks/pre-commit` executing note structure validation and index rebuild.
- Document `git config core.hooksPath .githooks` in both `AGENTS.md` and `README.md`.

---

## Testing Decisions

- **Testing Philosophy**: Verify external observable contracts and user-facing behaviors at public module seams rather than testing private internal implementation details.
- **Client Search & Focus Contract (DOM Seam)**:
  - Tested in `tests/test_preview_and_generator.py`: verify that the compiled `index.html` contains the search `Enter` keyboard handler targeting `.problem-item`, `#notesViewer` has `tabindex="-1"`, and `switchItem` does not mutate global `viewMode` on notes fallback.
- **Compiler Dynamic Metadata & README Sync Seam**:
  - Tested in `tests/test_update_index.py`: verify `DocumentEntity.search_blob` generation, typed `FilePairing` construction, and dynamic difficulty calculation in `scripts/sync_readme.py`.
- **Repository Tracking & Integrity Seam**:
  - Tested in `tests/test_tracking_integrity.py` and `tests/test_note_structure.py`: assert zero untracked problem files and 100% 7-section compliance for all companion notes.
- **Prior Art**:
  - `tests/test_preview_and_generator.py` (DOM structure and JavaScript contract validation).
  - `tests/test_update_index.py` (Compiler pipeline and entity resolution tests).
  - `tests/test_tracking_integrity.py` (Tracking integrity assertions).

---

## Out of Scope

- Modifying the visual color palette, split ratio defaults, or IDE layout structure.
- Modifying the contents of existing `.py` solution files (strictly adhering to Core Rule 1).
- Adding full-text search indexing over Markdown body text (keeping search lightweight and fast over metadata/titles).

---

## Further Notes

- Fully adheres to `AGENTS.md` Core Rules (Notes-First layout, Left-Notes/Right-Code orientation, SVG iconography, zero `.py` mutations).
