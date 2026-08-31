# Spec 13: Dynamic Topology Anchor Validation, Tokenized Keyword Matching, and Code Smell Remediation

**Triage Label**: `ready-for-agent`

---

## Problem Statement

During comprehensive two-axis code reviews across recent compiler and problem additions (Spec 12 and LeetCode 22), several architectural inconsistencies, validation blind spots, and code smells were identified:

1. **Static Keyword Duplication & Permissive Macro Anchor Validation**:
   - The note validator maintained redundant, hardcoded sets of topology taxonomy keywords instead of dynamically referencing the canonical topology graph registry.
   - The validator's Section 3 check relied on loose keyword presence and allowed notes to pass validation even if their declared `Topology Node:` macro anchor did not correspond to any registered node identifier or display category in the 38-Node Topology Graph.

2. **Primitive Obsession & False-Positive Substring Collisions in Entity Matching**:
   - Entity keyword matching relied on ad-hoc string concatenation and fuzzy substring containment (`keyword in blob`). This created false-positive token collisions where short keyword stems (such as `tree`, `path`, or `diff`) could match unrelated words inside titles or slugs (such as `street`, `empathy`, or `difficult`).

3. **Skipped Structural Auditing for Non-Problem Documentation**:
   - Directory auditing silently skipped non-problem documentation files (e.g., track overviews and architectural guides) without applying domain-appropriate structural validation rules, leaving general documentation unverified by automated gates.

4. **Code Smells and Parameter Shadowing in Algorithm Solutions**:
   - Backtracking solutions in algorithm sources shadowed Python built-ins (such as using `open` for tracking left parentheses count instead of `open_count` or `left_cnt`), diminishing code clarity and raising linter warnings.
   - README synchronization logic contained duplicate markdown note link formatting routines across track builders.

---

## Solution

1. **Dynamic Taxonomy Registry Alignment & Strict Macro Anchor Validation**:
   - Align the note validator directly with the canonical topology registry, eliminating all duplicated hardcoded keyword lists.
   - Implement strict macro anchor parsing in the note validator that verifies the declared `Topology Node:` path against registered node identifiers or display categories in the 38-Node Compound Algorithmic Topology Graph.

2. **Tokenized Word-Boundary Matching on DocumentEntity**:
   - Refactor `DocumentEntity` keyword matching to utilize word-boundary token sets and normalized identifier matching, eliminating substring collision false positives while maintaining fast O(1) keyword lookup.

3. **Domain-Appropriate Auditing for Non-Problem Documentation**:
   - Introduce dedicated structural rules for general overview notes and curriculum guide files within directory auditing, asserting foundational structure (bilingual headers, overview sections, valid markdown) while exempting them from LeetCode-specific 7-section algorithms contracts.

4. **Code Smell Remediation & Clean Link Formatting**:
   - Refactor algorithm backtracking parameter naming to use explicit domain identifiers (`open_count`, `left_cnt`), keeping companion notes and walkthrough dry-run tables in lockstep.
   - Consolidate README note link formatting into a unified, reusable helper method across all track generators.

---

## User Stories

1. As a student navigating the interactive Roadmap, I want every companion note's `Topology Node:` anchor to strictly map to a real node in the 38-Node Topology Graph, so that I can reliably trace the algorithmic lineage without broken graph associations.
2. As an algorithm learner studying backtracking solutions, I want clean parameter naming that does not shadow built-in Python functions like `open`, so that the mental model and code readability are unambiguous.
3. As a developer writing new companion notes, I want the validator to import canonical keywords dynamically from the topology registry, so that updating the topology definitions never requires changing validator constants in parallel.
4. As a developer running pre-commit checks, I want precise diagnostic errors when a note declares a misspelled or non-existent macro topology node, so that taxonomy mistakes are caught immediately before commit.
5. As a compiler maintainer, I want `DocumentEntity` keyword matching to use word boundaries and token sets, so that short keywords do not accidentally associate problems with unrelated topology nodes due to substring collisions.
6. As a documentation maintainer, I want non-problem guide documents to be audited with appropriate structural checks, so that general curriculum overviews remain well-formatted without failing LeetCode 7-section rules.
7. As a curriculum author, I want README synchronization to generate markdown note links through a single clean helper, so that table generation remains DRY and consistent across all tracks.
8. As a repository maintainer, I want automated test suites to assert both negative and positive macro anchor validation cases, so that regressions in validation gates cannot slip through CI undetected.
9. As a candidate reviewing Top 100 solutions, I want companion walkthrough notes and dry-run matrices to match the cleaned Python variable names exactly, so that there is zero cognitive dissonance between code and explanation.
10. As an AI assistant generating new solutions, I want explicit contracts on macro anchor formatting and tokenized tag taxonomy, so that all future problem submissions pass automated quality gates on the first attempt.

---

## Implementation Decisions

### 1. Dynamic Topology Taxonomy & Macro Anchor Validation
- In the validation module:
  - Dynamically load canonical taxonomy keywords directly from the topology definitions module, establishing a fallback only if dynamic imports fail.
  - Parse Section 3 of companion notes to extract the declared `Topology Node:` anchor.
  - Verify that the extracted anchor string contains at least one recognized node ID, display category, or canonical tag present in the 38-Node Compound Algorithmic Topology Graph.
  - Return descriptive validation errors if Section 3 lacks a parseable macro anchor or references an unregistered topology node.

### 2. Word-Boundary & Tokenized Matching on DocumentEntity
- In the domain entities module:
  - Refactor `matches_keywords` on `DocumentEntity` to tokenize search metadata (splitting slug, tags, title, and categories on non-alphanumeric boundaries into a normalized token set).
  - Perform matching via exact token set intersection or hyphenated phrase boundary matching, preventing partial substring collisions (such as `tree` matching `street`).
  - Ensure compatibility with multi-word canonical tags (e.g. `sliding-window`, `fast-slow-pointers`, `prefix-sum`).

### 3. Structural Validation for Non-Problem Documentation
- In the validation auditing module:
  - Differentiate between LeetCode companion problem notes (matching `lc-*.md` or `\d{2}-lc-*.md`) and general curriculum/overview documentation.
  - For non-problem documentation, enforce domain-appropriate checks: verify top-level markdown heading, non-empty content body, valid UTF-8 encoding, and absence of broken local asset links.
  - Retain strict 7-section active-recall validation for all LeetCode companion notes across all tracks.

### 4. Code Smell Remediation & Parameter Normalization
- In the problem solutions and companion notes:
  - In backtracking problem sources (e.g. LeetCode 22), rename `open` parameter to `open_count` or `left_cnt` to avoid shadowing Python's built-in `open()`.
  - Update line-by-line code walkthroughs, parameter invariant tables, and dry-run matrices in companion markdown notes to maintain exact synchrony with the modified Python source.
- In the README synchronization module:
  - Consolidate repetitive markdown note link creation into an encapsulated helper function, eliminating duplicated branch formatting across track builders.

---

## Testing Decisions

- **Testing Philosophy**: Test public domain contracts and external behaviors end-to-end without coupling assertions to internal regex helpers or private variables.
- **Primary Schema Seam (`tests/test_note_structure.py`)**:
  - Assert that companion notes with invalid or non-existent `Topology Node:` macro anchors fail validation with informative diagnostic messages.
  - Assert that companion notes with valid macro anchors matching canonical nodes pass validation.
  - Assert that non-problem documentation files are audited successfully without triggering 7-section schema errors.
- **Compiler Seam (`tests/test_graph_builder.py`)**:
  - Assert that `DocumentEntity.matches_keywords` correctly matches valid tokens and multi-word tags while rejecting substring collision false positives (e.g. `tree` does not match `street`).
  - Assert that topology graph aggregation builds the complete 38-node DAG with accurate problem counts.
- **Synchronization Seam (`tests/test_update_index.py`)**:
  - Assert that README generation uses the consolidated note link formatting and produces identical, valid Markdown tables for Top-100, Daily Practice, and Luffy tracks.

---

## Out of Scope

- Modifying algorithmic time/space complexities of established LeetCode solutions.
- Creating companion notes for remaining unauthored Top-100 problems.
- Modifying frontend CSS theme variables or mobile navigation styles.

---

## Further Notes

- All changes must strictly comply with `AGENTS.md` (Core Rules 1 through 6) and `CONTEXT.md` architectural models.
