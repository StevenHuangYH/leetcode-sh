# Spec 12: Topology Relation Chain Validation and Compiler Integrity Hardening

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Following the establishment of the 38-Node Compound Algorithmic Topology Graph and the updated repository rule requiring all LeetCode sources to maintain their relation chain in the topology graph, several architectural blind spots and code quality gaps were identified across the repository:

1. **Incomplete Directory Auditing in Note Validator**:
   - In `NoteStructureValidator.audit_notes_directory`, the file filter strictly checked `if md_file.name.startswith("lc-"):`. This regex flaw caused the validator to silently skip all 53 curriculum notes under the `luffy/` track (which use numbered prefixes such as `01-lc-2235-add-two-integers.md`). As a result, regressions in curriculum notes could bypass automated CI validation undetected.

2. **Permissive Pre-Commit Hook Gate**:
   - The `.githooks/pre-commit` quality gate invoked `update_index.py --lint` without the `--strict` flag. Consequently, note validation errors returned exit code 0 rather than blocking the git commit. Additionally, the hook omitted automated unit test execution (`python3 -m unittest discover tests`), allowing broken compiler contracts to be committed.

3. **Lack of Automated Topology Relation Chain Verification**:
   - While `AGENTS.md` mandates that all LeetCode notes declare topology taxonomy tags, macro anchors, and ASCII pattern lineage maps matching `CANONICAL_TOPOLOGY_NODES`, there is no automated unit test asserting that note tags and macro anchors correspond to valid registered nodes in `scripts/compiler/topology_definitions.py`.

4. **Vestigial Pipeline Artifacts & Dead Code**:
   - The compiler parser retained legacy parsing routines (`parse_roadmap_data`) and obsolete data classes (`RoadmapPhase`, `RoadmapTopic`, `RoadmapProblem`) targeting a deprecated `ROADMAP.md` file that has been entirely superseded by the interactive 38-Node Topology DAG.

5. **Feature Envy in Topology Graph Construction**:
   - `GraphBuilder` accessed raw dictionary fields and internal search blobs of `DocumentEntity` when matching topic keywords, rather than delegating matching logic to encapsulated methods on `DocumentEntity`.

---

## Solution

1. **Universal Companion Note Directory Auditing**:
   - Update `NoteStructureValidator` directory scanning to match all LeetCode companion Markdown notes across all tracks (`top-100/`, `daily-practice/`, and `luffy/`), supporting both standard `lc-*.md` and numbered `\d{2}-lc-*.md` naming conventions.

2. **Hardened Pre-Commit Gate with Test Discovery**:
   - Update `.githooks/pre-commit` to execute strict note validation (`update_index.py --lint --strict`), run full unit test discovery (`python3 -m unittest discover tests`), and compile `index.html`, strictly aborting the commit if any stage fails.

3. **Automated Topology Graph Relation Chain Validation**:
   - Implement automated test assertions in `tests/test_note_structure.py` and `tests/test_graph_builder.py` verifying that all audited companion notes declare valid canonical topology taxonomy tags and macro anchors present in `CANONICAL_TOPOLOGY_NODES`.

4. **Elimination of Vestigial Roadmap Code**:
   - Remove obsolete `ROADMAP.md` parsing functions and unused data models from `scripts/compiler/parser.py` and `scripts/compiler/engine.py`, streamlining the compiler pipeline.

5. **Encapsulated Domain Matching in DocumentEntity & GraphBuilder**:
   - Introduce an encapsulated `matches_topology_keywords` method on `DocumentEntity` and consolidate problem projection dictionary creation, eliminating feature envy and duplication in `GraphBuilder`.

---

## User Stories

1. As a student studying LeetCode patterns, I want all companion notes across all tracks (including `luffy/` curriculum notes) to be strictly validated against the 7-section schema, so that I always receive complete and reliable mental models.
2. As a student navigating the interactive Roadmap, I want every LeetCode note to declare verified topology tags and macro anchors, so that problems are accurately grouped into their corresponding topology nodes.
3. As a developer adding a new LeetCode problem, I want the pre-commit hook to catch schema and unit test violations before commit, so that broken notes or compiler regressions are never pushed to the remote repository.
4. As a compiler maintainer, I want `GraphBuilder` to interact with `DocumentEntity` through clean domain methods rather than probing internal dictionary structures, so that the compiler codebase remains maintainable and resilient.
5. As a repository maintainer, I want dead parsing code for obsolete files (`ROADMAP.md`) removed, so that the compiler pipeline is clean and free of confusing vestigial artifacts.
6. As a test engineer, I want `audit_notes_directory` to cover 100% of existing Markdown notes across all workspace directories, so that test metrics accurately reflect repository health.
7. As a curriculum author, I want clear diagnostic error messages when a note references a non-existent topology node, so that taxonomy typos are immediately caught and corrected.
8. As an AI assistant generating new solutions, I want explicit automated test gates verifying the 4-step protocol and topology relation chains, so that compliance with `AGENTS.md` is guaranteed.

---

## Implementation Decisions

### 1. Universal Note File Matching in NoteStructureValidator
- In the note structure validation module:
  - Update `audit_notes_directory` to match any `.md` file whose stem contains `-lc-` or starts with `lc-` (specifically `r'(?:^\d{2}-)?lc-'`), ensuring all notes in `top-100/`, `daily-practice/`, and `luffy/` are discovered.
  - Exclude non-problem documentation files (e.g. topic overviews, OOP guides) from strict LeetCode 7-section schema enforcement, auditing them with domain-appropriate structural rules.

### 2. Automated Topology Node and Keyword Verification
- In the validation rules:
  - Validate that declared `Tags:` in Section 1 contain at least one keyword matching the canonical keyword set of `CANONICAL_TOPOLOGY_NODES`.
  - Validate that Section 3 contains a parseable `Topology Node:` macro anchor matching an existing node ID or display category in the 38-Node Topology Graph.

### 3. Pre-Commit Quality Gate Hardening
- In `.githooks/pre-commit`:
  - Run `python3 update_index.py --lint --strict` and ensure a non-zero exit code halts the commit.
  - Run `python3 -m unittest discover tests` and abort if any test fails.
  - Execute `python3 update_index.py` to ensure `index.html` is compiled and synchronized.

### 4. GraphBuilder Encapsulation & Dead Code Removal
- In `scripts/compiler/entities.py`:
  - Add `matches_keywords(self, keywords: List[str]) -> bool` and `to_topology_summary(self) -> Dict[str, Any]` to `DocumentEntity`.
- In `scripts/compiler/graph_builder.py`:
  - Replace manual attribute probing and duplicated dictionary constructions with entity method invocations.
- In `scripts/compiler/parser.py` and `scripts/compiler/engine.py`:
  - Delete `parse_roadmap_data`, `RoadmapPhase`, `RoadmapTopic`, and `RoadmapProblem`.

---

## Testing Decisions

- **Testing Philosophy**: Verify end-to-end domain contracts and public interfaces without binding tests to internal helper implementations.
- **Primary Seam (`tests/test_note_structure.py`)**:
  - Assert that `audit_notes_directory` discovers and validates all companion notes across `daily-practice/`, `top-100/`, and `luffy/` directories.
  - Assert that notes with invalid topology tags or missing macro anchors fail validation with informative diagnostic messages.
- **Compiler Seam (`tests/test_graph_builder.py` & `tests/test_update_index.py`)**:
  - Assert that `GraphBuilder` builds the complete 38-node topology DAG using entity methods with zero errors.
  - Assert that pre-commit script contracts (`--lint --strict`, unit tests, compilation) are preserved.
- **Prior Art**:
  - `tests/test_note_structure.py` (Note schema validation tests).
  - `tests/test_graph_builder.py` (Topology DAG builder unit tests).
  - `tests/test_update_index.py` (Compiler pipeline and pre-commit checks).

---

## Out of Scope

- Modifying existing Python algorithm solutions (preserving Core Rule 1 immutability).
- Writing the 81 missing Top-100 companion notes (tracked as separate content authoring tasks).
- Changing frontend CSS visual themes or viewport layouts.

---

## Further Notes

- All changes must strictly comply with `AGENTS.md` (Core Rules 1 through 6) and `CONTEXT.md` architectural models.
