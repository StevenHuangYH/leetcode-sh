# Spec 16: Track Registry Deepening, Client Fallback Elimination, and Validation Integrity Consolidation

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Following the centralization of the Canonical Track Registry in Spec 15 and commit `030b6bc`, the subsequent code review identified remaining code smells, scope creep, and architectural gaps:

1. **Speculative Generality and Redundant Fallbacks in Client Runtime**:
   The client application bundle retains dead defensive fallback branches that fall back to hardcoded track arrays (`top-100`, `daily-practice`, `luffy`) if the injected track metadata is empty. Because track metadata is always compiled and injected at build time by the study station compiler, these fallback branches constitute speculative dead code that reintroduces the exact hardcoded string literals the centralization was intended to eradicate.

2. **Incomplete Registry Adoption Across Validation and Tracking Suites**:
   The note validator and repository tracking integrity test suite were omitted from consuming the centralized track registry. They continue to define loose string literals and hardcoded regular expressions for tracks, perpetuating shotgun surgery risk whenever problem tracks are added or reorganized.

3. **Schema Creep on the Track Configuration Domain Model**:
   The track configuration model introduced an unsolicited `legacy_prefix` attribute in its schema and client JSON payload. Backward-compatible route resolution should be derived deterministically from the track identifier rather than burdening the domain schema with redundant fields.

4. **String Duplication and Hardcoded Fallbacks in Documentation Sync**:
   The documentation synchronization tool employs inline string fallbacks rather than relying strictly on the registry domain model, and hardcodes track lookups instead of utilizing registry discovery helpers.

5. **Missing Client Category Filter Behavior Tests**:
   The test suite lacks assertions verifying that dynamically injected track metadata correctly populates client-side category filters and directory tree structures without falling back to hardcoded arrays.

---

## Solution

1. **Eliminate Client-Side Speculative Fallbacks and Redundant Logic**:
   - Remove dead hardcoded fallback arrays from the client application script (`treeStructure` and `resolveEntityReference`).
   - Derive sidebar category folders and entity reference search paths strictly from the compiler-injected track metadata.
   - Clean up redundant folder filter predicates to ensure concise and deterministic track matching.

2. **Complete Full-Workspace Registry Consumption**:
   - Provide a workspace-level track audit entry point in the note validator that discovers all tracks via the centralized registry.
   - Refactor repository tracking integrity tests to derive track paths and regex link patterns dynamically from the centralized registry.

3. **Streamline Track Configuration Domain Schema**:
   - Remove `legacy_prefix` from the track configuration dataclass and client payload; derive legacy path resolution dynamically in the client router from the track identifier (`${id}/`).

4. **Harden Documentation Synchronization**:
   - Update documentation synchronization routines to source relative track directories strictly from the track registry without raw string fallbacks.

5. **High-Seam Behavioral Testing**:
   - Enhance compiler integration tests to assert that generated HTML client scripts dynamically instantiate track folders matching the registry and contain zero hardcoded fallback arrays.
   - Add unit tests verifying that client-side category filter predicates correctly accept canonical paths, legacy paths, and reject cross-track mismatches.

---

## User Stories

1. As a frontend maintainer, I want the client JavaScript to derive category folders directly from injected track metadata, so that there are no duplicate hardcoded fallback lists in the client bundle.
2. As a software architect, I want speculative fallback branches removed from client routing and tree construction, so that the codebase honors YAGNI and avoids dead code.
3. As a developer adding a new problem track, I want to configure the track in a single registry module, so that the validator, tracking suite, compiler, and frontend automatically recognize it without editing multiple scripts.
4. As a test engineer, I want tracking integrity tests to query the track registry for directory paths and link patterns, so that test fixtures never drift from production compiler settings.
5. As a QA engineer, I want compiler integration tests to assert that the compiled client script contains no unreplaced placeholders and no hardcoded fallback arrays, so that regressions in bundling are caught immediately.
6. As a CI operator running pre-commit quality gates, I want the note validator to discover all problem directories via the registry, so that no track is accidentally omitted from note schema audits.
7. As an API consumer of the track configuration domain model, I want a lean and focused schema without redundant attributes like legacy prefixes, so that domain models remain cohesive and unbloated.
8. As a client router maintainer, I want legacy URL path compatibility derived dynamically from track identifiers, so that old bookmarks continue to resolve without manual schema configuration.
9. As a documentation sync maintainer, I want README generators to fail fast or handle missing tracks gracefully without falling back to hardcoded string literals, so that broken configurations are surfaced immediately.
10. As a code reviewer inspecting future pull requests, I want zero track-related string literals across compiler, test, and client scripts, so that code smell baselines remain clean.
11. As a mobile learner navigating problem tracks, I want dynamic category tabs to mirror the exact repository tracks, so that navigation is consistent between desktop and mobile views.
12. As an AI assistant authoring new problem notes, I want a single authoritative track registry, so that file placement and validation rules are unambiguous and programmatically discoverable.

---

## Implementation Decisions

### 1. Client Template Cleanup & Fallback Removal
- Remove all static fallback object arrays for tracks in the client application script.
- The sidebar tree structure will construct problem track folders directly from the injected track configuration array.
- The entity reference resolver will iterate over the injected track configuration paths and dynamic legacy prefixes derived from track identifiers (`${track.id}/`).
- Simplify the category folder filter predicate to match canonical directory paths and legacy track prefixes without redundant checks.

### 2. Track Configuration Model Simplification
- Remove the optional legacy prefix attribute from the track configuration domain model.
- Keep the domain schema minimal:
  - `id`: Normalized slug identifier (e.g. `top-100`).
  - `dir_path`: Relative directory path (e.g. `problems/top-100`).
  - `display_label`: Primary human-readable label for UI rendering.
  - `category_name`: Canonical track category name for entity grouping.
- Serialize this streamlined structure in the client JSON payload.

### 3. Note Validator & Tracking Integrity Suite Registry Alignment
- Introduce a workspace-level track audit function in the note validator that queries the track registry for all configured track paths.
- Update tracking integrity test suites to dynamically generate track directory manifests and regular expression link patterns from the registry rather than defining static string lists.

### 4. Documentation Synchronizer Robustness
- Remove inline string literal fallbacks in the README table generation routines.
- Raise an explicit domain error if a required canonical track is absent from the registry, ensuring fast failure rather than silent degradation.

---

## Testing Decisions

### Good Test Principles
- Tests must assert external observable behavior at the highest available seam rather than verifying internal implementation details.
- Avoid asserting private variables or internal helper functions; test compiler output and validator results against real and synthetic fixtures.

### Testing Seams
- **Primary Seam: End-to-End Compiler Seam (`compile_study_station`)**:
  - Test that compiling the application bundle with the track registry generates an HTML file whose embedded script dynamically populates category folders.
  - Assert that the compiled HTML output does not contain any hardcoded fallback track lists (`problems/top-100`, `problems/daily-practice`, `problems/luffy` in fallback branches).
- **Secondary Seam: Workspace Tracking Integrity Seam (`TestTrackingIntegrity`)**:
  - Test that all links and disk problem entities across registered tracks align with README documentation using registry-derived paths.
- **Tertiary Seam: Track Registry Domain Model Seam (`TrackRegistry`)**:
  - Assert that the simplified track configuration schema serializes cleanly to the client JSON payload without legacy prefix attributes.

### Prior Art
- Existing test suites under `tests/test_update_index.py`, `tests/test_tracking_integrity.py`, and `tests/test_note_structure.py`.

---

## Out of Scope

- Adding new problem tracks or reorganizing problem directory structures.
- Altering the 38-Node Compound Algorithmic Topology Graph taxonomy or edge relationships.
- Modifying problem solution code (`.py` files remain strictly immutable under Core Rule 1).
- Visual UI redesigns or stylesheet modifications outside track folder rendering.

---

## Further Notes

- This specification directly resolves all baseline smells and specification discrepancies documented during the code review of commit `030b6bc`.
- Execution must adhere to the Mandatory 4-Step Push & Walkthrough Protocol and pass all pre-commit quality gates upon completion.
