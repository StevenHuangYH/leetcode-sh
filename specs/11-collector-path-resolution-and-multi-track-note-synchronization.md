# Spec 11: Collector Path Resolution and Multi-Track Note Synchronization

**Triage Label**: `ready-for-agent`

---

## Problem Statement

During the transition to collector-driven README synchronization, two regressions and architectural code smells emerged:
1. In the README synchronization pipeline, `ProblemCollector` entities provide relative paths that already incorporate track directories (e.g. `luffy/33-lc-0078-subsets.py` or `daily-practice/lc-0077-combinations.md`). The index builder redundantly prepended the track directory name to these paths, causing filesystem verification checks to fail on all problem entities. Consequently, the multi-track file map resolved to an empty dictionary, stripping companion `.md` notes and cross-track `.py` solutions from Section 5 problem tables in `README.md`.
2. In the client search pipeline, an unnecessary delegator function (`matchesSearchQuery`) was retained, which re-compiles regular expressions on every invocation rather than directly leveraging pre-compiled query matcher closures.
3. Test suites lacked end-to-end assertions validating that Section 5 problem rows actually retain multi-track links (both `.py` and `.md`) after synchronization runs.

---

## Solution

1. **Normalized Path Resolution in File Indexing**:
   - Update the problem file indexer to directly consume normalized repository-relative paths emitted by `ProblemCollector` without manual string manipulation or redundant track directory prefixes.
   - Validate both Python solution scripts and companion Markdown walkthrough notes against the filesystem using clean, single-source-of-truth paths.
2. **Dynamic Multi-Track Solution and Note Synchronization**:
   - Ensure the Section 5 synchronization engine replaces problem table rows with comprehensive `<br>`-delimited lists of all associated solution code and walkthrough notes across `top-100/`, `daily-practice/`, and `luffy/` tracks.
3. **Elimination of Delegator Code Smells**:
   - Streamline client-side search execution to call the closure returned by the search matcher factory directly, removing middle-man delegator functions.
4. **End-to-End Contract and Seam Testing**:
   - Add automated test assertions verifying that multi-track problem rows in `README.md` contain both `.py` source and `.md` companion notes for multi-track problems (such as LC 77, LC 78, LC 131, LC 167, LC 3, LC 209, LC 59, LC 303, LC 20, and LC 98).

---

## User Stories

1. As a student studying multi-track problems in `README.md`, I want problem rows to show clickable links to all existing Python solutions and Markdown companion notes across all tracks, so that I have immediate access to code and walkthrough explanations.
2. As a developer maintaining repository documentation, I want `scripts/sync_readme.py` to correctly resolve collector paths without redundant directory concatenation, so that file existence checks never produce false negatives.
3. As a user searching for problems in the Study Station, I want search queries to execute against pre-compiled matcher closures without redundant wrapper overhead, so that client search remains responsive.
4. As a test maintainer, I want CI tests to assert the actual presence of multi-track `.py` and `.md` links in synchronized tables, so that path-doubling and link-stripping regressions are caught immediately.

---

## Implementation Decisions

### 1. Collector Path Consumption in README Synchronization
- In the README synchronization module:
  - Iterate over collected problem entities from `ProblemCollector`.
  - For each entity, extract `py_file` and `md_file` paths directly. Because `ProblemCollector` yields paths relative to the repository root, inspect and verify them against the repository root directly without prepending track directory names.
  - When formatting markdown links (`[`{rel_path}`]({rel_path})`), maintain stable ordering (`.py` files followed by companion `.md` notes).
  - Pass the aggregated mapping to the table synchronization engine to update multi-track rows in Section 5.

### 2. Search Matcher Direct Invocation
- In the client-side UI application script:
  - Remove redundant wrapper/delegator functions that re-instantiate query matchers on every item.
  - Ensure tree rendering and filtering logic instantiate the search matcher once per query and invoke the returned matcher closure across candidate entities.

### 3. Rebuilding Index and Synchronizing Repository
- Re-run synchronization and Study Station compilation to ensure `README.md` and `index.html` are completely updated and verified.

---

## Testing Decisions

- **Testing Philosophy**: Verify observable public contracts across the synchronization pipeline, README document structure, and client bundle.
- **Single High-Level Seam (`tests/test_update_index.py`)**:
  - Run the README synchronization process against current repository state.
  - Assert that Section 5 problem table rows for known multi-track problems (e.g. LC 77, LC 78, LC 131, LC 167, LC 3, LC 209, LC 59, LC 303, LC 20, LC 98) contain both `.py` and `.md` links.
  - Assert that `build_problem_files_index` returns non-empty link lists for all multi-track problems.
- **Client Search Engine Seam (`tests/test_preview_and_generator.py`)**:
  - Assert that client script templates construct matcher closures via `buildSearchMatcher` and eliminate redundant `matchesSearchQuery` middle-man delegates.
- **Prior Art**:
  - `tests/test_update_index.py` (Compiler & generator pipeline verification).
  - `tests/test_preview_and_generator.py` (DOM & JS search verification).
  - `tests/test_tracking_integrity.py` (Link & problem tracking verification).

---

## Out of Scope

- Modifying existing Python algorithm solutions (preserving Core Rule 1 immutability).
- Modifying note structure validator rules or altering the 7-section companion note schema.
- Changing CSS visual styles or viewport layouts.

---

## Further Notes

- Strict adherence to `AGENTS.md` (Core Rules 1-5) and `CONTEXT.md` architectural models.
