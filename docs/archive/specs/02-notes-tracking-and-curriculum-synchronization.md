# Spec: Comprehensive Problem Tracking Synchronization & Curriculum Standardization

**Triage Label:** `ready-for-agent`

---

## Problem Statement

When maintaining and studying through the algorithm repository, users and contributors encounter tracking discrepancies, incomplete study notes, and redundant metadata structures:
1. **Desynchronized Problem Tracking**: Multiple problems present in `top-100/` and `daily-practice/` are missing from the primary tracker tables in `README.md`, making it difficult to assess real progress against study goals.
2. **Conflicting Repository Metrics**: Statistics badges, summary table totals, and roadmap counts report conflicting problem numbers (e.g. `164+`, `171`, `188`), degrading trust in the documentation.
3. **Inconsistent Note Structure Across Tracks**: While `top-100/` and `daily-practice/` companion notes have been upgraded to the exam-oriented 7-section blueprint, notes in `luffy/` remain placeholder stubs lacking ASCII Pattern Lineage Maps, Interview Follow-ups, and Error Logs.
4. **Scattered Metadata Duplication**: Topic groupings and problem metadata are duplicated between markdown documentation and generator scripts, causing maintenance friction and shotgun surgery whenever a topic or problem is updated.

---

## Solution

Establish an automated, single-source-of-truth problem tracking and curriculum standardization pipeline:
1. **Authoritative Problem Audit & Tracker Synchronization**: Perform an exhaustive audit of all problem files across `top-100/`, `daily-practice/`, and `luffy/`, updating all `README.md` tracking tables and harmonizing all metrics badges and summary statistics to exact, verified counts.
2. **Full Curriculum 7-Section Note Standardization**: Systematically upgrade all foundational curriculum notes to the active recall 7-section format (Bilingual Statement, ASCII Lineage Map, Python Walkthrough, Interview Follow-ups, Anti-Pattern Error Log, Dry-Run Table, Complexity Analysis).
3. **Single-Source Metadata Ingestion**: Refactor the generator pipeline to parse topic hierarchies and metadata directly from documentation sources, eliminating hardcoded duplicated data blobs.
4. **Automated Verification Harness**: Introduce automated regression tests to guarantee that every problem file on disk is tracked in `README.md`, all notes adhere to the standard 7-section format, and the web viewer compiles cleanly with zero unparsed sections.

---

## User Stories

1. As a developer browsing the repository, I want the `README.md` tracking table to accurately reflect every problem implemented in the codebase, so that I have a complete picture of my study progress.
2. As a developer checking repository statistics, I want the top badge counts, track summary table totals, and compiled web station metrics to match exactly, so that repository metrics are trustworthy and consistent.
3. As a developer studying foundational algorithm concepts in the 42-topic curriculum, I want each topic note to provide an ASCII Pattern Lineage Map, so that I can understand how advanced algorithms evolve from simple primitives.
4. As a candidate preparing for technical interviews, I want every problem note to include an "Interview Simulation" section with follow-up pivots and comparative analysis, so that I am prepared for deep follow-up questions from interviewers.
5. As a candidate debugging tricky edge cases, I want each note to feature an "Error Log" table mapping anti-patterns, failure symptoms, and defensive invariants, so that I avoid high-frequency implementation bugs.
6. As a student reading code explanations, I want line-by-line walkthroughs to strictly reflect the immutable Python baseline code, so that there is zero confusion between documented explanations and runnable source code.
7. As a maintainer adding a new problem or topic, I want repository generation scripts to ingest topic hierarchies dynamically from markdown files rather than maintaining separate hardcoded Python dictionaries, so that updates do not require shotgun surgery.
8. As a maintainer running test suites before pushing commits, I want automated validation that fails if any problem is omitted from `README.md` or if any note lacks required sections, so that repository quality regressions are prevented automatically.

---

## Implementation Decisions

1. **Repository Audit & Tracking Table Population**:
   - Scan `top-100/`, `daily-practice/`, and `luffy/` to produce a unified manifest of all problem entities.
   - Rebuild the `README.md` Track 1 (Top 100 Liked), Track 2 (Daily Practice), and Track 3 (42-Topic Curriculum) tables so every `.py` and `.md` pair is indexed.
   - Synchronize top badges (`Total Problems Solved`) and Summary Metric tables to reflect the exact counted total.

2. **Curriculum Note Upgrade Protocol**:
   - Upgrade curriculum notes to the standard 7-section structure defined in repository rules:
     - Section 1: Problem Statement & Constraints (Bilingual English & Chinese)
     - Section 2: Core Idea, Mental Model & ASCII Pattern Lineage Map
     - Section 3: Step-by-Step Code Walkthrough (strictly based on authoritative `.py` baseline)
     - Section 4: Interview Simulation: Alternative Paradigms & Follow-up Pivots
     - Section 5: The Error Log & Complete Dry-Run Table
     - Section 6: Key Boundary Edge Cases & Invariants
     - Section 7: Complexity Analysis (Time & Space with mathematical proof)
   - Ensure all intra-document links to `.py` source files use portable relative markdown links.

3. **Generator Pipeline Refactoring**:
   - Eliminate hardcoded data dictionaries in generator scripts by dynamically extracting topic sections and problem groupings directly from markdown files.
   - Bundle loose primitive parameters into structured data objects for document representation.

4. **Automated Consistency Validation**:
   - Add automated test assertions verifying:
     - Bi-directional tracking: every problem file on disk has a corresponding row in `README.md`, and every row in `README.md` points to an existing file.
     - Section completeness: companion `.md` notes contain all required 7-section headers.
     - Build integrity: `index.html` static compilation succeeds with zero unparsed sections.

---

## Testing Decisions

- **Good Test Philosophy**: Tests verify observable repository invariants and public compilation artifacts without coupling to internal parsing regexes or generator private helpers.
- **Modules Tested**:
  - `update_index.py` workspace ingestion and document builder interfaces.
  - Repository tracking integrity and filesystem consistency.
  - Note structure compliance across all markdown files.
- **Prior Art**:
  - `tests/test_update_index.py` (verifies topic curriculum parsing).
  - `tests/test_lc_0034.py` (verifies binary search interval consistency).

---

## Out of Scope

- Introducing dynamic server-side backend services or database dependencies (the project remains a 100% static, client-side SPA).
- Refactoring or altering existing Python solution algorithms (`.py` files remain strictly immutable per repository core rules).
- Adding unrequested external UI frameworks or third-party web dependencies.

---

## Further Notes

- Maintains 100% compliance with `AGENTS.md` and repository guidelines.
- Preserves the monochromatic developer aesthetic across `index.html` and documentation.
