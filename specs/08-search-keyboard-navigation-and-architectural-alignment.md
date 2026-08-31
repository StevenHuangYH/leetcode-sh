# Spec 08: Search Keyboard Navigation, Precision Filtering, and Architectural Smells Alignment

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Users navigating the `leetcode-sh` Study Station via keyboard face friction when filtering problems: pressing `Enter` in the search box does not automatically select the top matched result or transfer keyboard focus to the notes pane, forcing manual mouse clicks to begin reading. Furthermore, numeric ID searches without word-boundary isolation surface false-positive matches (e.g. searching for problem `1` matches `10`, `11`, `100`), diluting search precision.

Behind the scenes, minor architectural code smells identified during full codebase review—such as feature envy in graph compilation (`scripts/compiler/graph_builder.py`), duplicate static difficulty lookups in `scripts/sync_readme.py`, and untracked local pre-commit hooks—accumulate technical debt and reduce maintainability across compiler modules.

---

## Solution

1. **Instant Keyboard Selection & Focus Transfer**: Equip the client search engine in `templates/src/scripts/app.js` with `Enter` key handling. When the user presses `Enter` inside `#search-input`, the top filtered problem is automatically selected, scrolled smoothly into the sidebar viewport, and DOM focus is transferred to `#notesViewer` (`tabIndex = -1`) for direct arrow/space key scrolling and distraction-free active recall.
2. **Word-Boundary Precision Filtering**: Upgrade `matchesSearchQuery` in client search logic to enforce exact word boundaries for numeric queries (`\b\d+\b`) while preserving fuzzy substring matches across problem titles, tags, and categories.
3. **Compiler Smell Elimination**:
   - Encapsulate search blob generation within `DocumentEntity` so `scripts/compiler/graph_builder.py` delegates directly rather than manually unpacking multiple string properties.
   - Refactor `scripts/sync_readme.py` to reuse dynamic metadata parsing from `scripts/compiler/collector.py`, eliminating redundant hardcoded difficulty tables.
   - Introduce typed file-pairing data structures in `scripts/compiler/collector.py`.
4. **Version-Controlled Git Hooks**: Establish a tracked `.githooks/pre-commit` script in the repository and configure automated pre-commit validation.

---

## User Stories

1. As a keyboard-first learner, I want pressing `Enter` in the search bar to immediately activate the top matching problem, so that I can switch problems without touching the mouse.
2. As a keyboard-first learner, I want pressing `Enter` in the search bar to focus the notes viewer pane, so that I can immediately scroll through the algorithmic walkthrough using Up/Down arrow keys or the Space bar.
3. As an algorithmic student searching for problem `1` or `15`, I want exact numeric ID matches prioritized over substring containment (e.g. not matching `100` or `153`), so that I find single and double-digit problems instantly.
4. As a user clearing a search query, I want the sidebar tree to restore its previous active selection and scroll position seamlessly, so that my navigation context is never lost.
5. As a developer maintaining the study station compiler, I want graph construction to utilize clean entity domain methods rather than feature envy property unpacking, so that schema modifications don't break graph compilation.
6. As a developer synchronizing documentation tables, I want README generators to share the single source of truth for problem difficulties from the compiler collector, so that difficulty ratings never drift between views.
7. As a repository contributor, I want git pre-commit hooks to be version-controlled in the repository, so that note validation and index rebuild checks execute reliably across development environments.

---

## Implementation Decisions

### 1. Client Search Keyboard Contract & Focus Routing
- In `templates/src/scripts/app.js`, attach an explicit `keydown` listener to `#search-input`:
  - On `Enter`: find the first visible `.problem-item` or matching `DocumentEntity` key in the filtered tree, invoke `switchItem(topMatchKey, false)`, and execute `document.getElementById("notesViewer").focus()`.
  - Ensure `#notesViewer` has `tabIndex="-1"` and `:focus-visible` styling is cleanly suppressed to maintain dark-mode IDE aesthetics.
- In `matchesSearchQuery`, enhance the token matcher: if a search token is entirely numeric (e.g. `^\d+$`), match it against problem numeric identifiers using exact word boundary equality (`entity.number === token` or regex `\b${token}\b`).

### 2. Domain Model Encapsulation for Search Blobs
- Enhance `DocumentEntity` in `scripts/compiler/entities.py` with a dedicated property `search_blob` that aggregates slug, tags, English title, Chinese title, category, and padded problem number.
- Refactor `scripts/compiler/graph_builder.py` to consume `entity.search_blob` directly, removing feature-envy dictionary unpacking.

### 3. Collector Metadata Reuse in README Sync
- Update `scripts/sync_readme.py` to import `ProblemCollector` from `scripts.compiler.collector`, sourcing all problem metadata dynamically and eliminating `KNOWN_DIFFICULTIES`.
- Define a typed dataclass `FilePairing` in `scripts/compiler/collector.py` to replace loose dictionary mapping for paired `.py` and `.md` files.

### 4. Version-Controlled Pre-Commit Hooks
- Create `.githooks/pre-commit` containing executable validation steps (`scripts.validator` and `StudyStationCompiler.compile()`).
- Document the hook activation configuration (`git config core.hooksPath .githooks`) in `AGENTS.md` and repository setup instructions.

---

## Testing Decisions

- **Testing Philosophy**: Test external behavior and contracts rather than internal helper implementation details.
- **Client Search & Focus Contract (Single High-Level Seam)**:
  - Test via `tests/test_preview_and_generator.py`: verify that the compiled `index.html` contains the search `Enter` keyboard handler, `#notesViewer` has `tabindex="-1"`, and numeric search tokens isolate exact problem numbers.
- **Compiler Integrity & Smell Tests**:
  - Test via `tests/test_update_index.py`: verify `DocumentEntity.search_blob` generation, `FilePairing` structure, and successful end-to-end HTML compilation across all tracks.
- **Prior Art**:
  - `tests/test_preview_and_generator.py` (DOM structure and JavaScript contract validation).
  - `tests/test_update_index.py` (Compiler pipeline and entity resolution tests).

---

## Out of Scope

- Modifying the visual color palette, split ratio defaults, or IDE layout structure.
- Modifying the contents of existing `.py` solution files (strictly adhering to Core Rule 1).
- Adding full-text search indexing over Markdown body text (keeping search lightweight and fast over metadata/titles).

---

## Further Notes

- Maintains strict compliance with `AGENTS.md` Core Rules (Notes-First layout, Left-Notes/Right-Code orientation, SVG iconography, zero `.py` mutations).
