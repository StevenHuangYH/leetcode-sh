# Spec 14: Universal Topology Macro Anchor Migration and Strict Validation Hardening

**Triage Label**: `ready-for-agent`

---

## Problem Statement

Following the establishment of the 38-Node Compound Algorithmic Topology Graph and the dynamic keyword registry alignment in Spec 13, a significant architectural gap remains across the repository's companion notes:

1. **Permissive Soft Fallback on Missing Macro Anchors**:
   - The note structure validator treats the `Topology Node:` macro anchor as optional. If a companion note omits the macro anchor entirely, the validation gate still passes as long as an ASCII code block or pattern lineage text is present. This soft fallback allows newly added or legacy companion notes to bypass topological taxonomy mapping undetected.

2. **Incomplete Macro Anchor Declarations Across Existing Tracks**:
   - Legacy companion notes across curriculum and practice tracks lack explicit `Topology Node:` macro anchor declarations in Section 3, resulting in unanchored notes that cannot be deterministically mapped to their corresponding nodes in the 38-Node Topology DAG.

3. **Incomplete Structural Auditing for Non-Problem Documentation**:
   - Non-problem overview documents lack structured assertions for bilingual topic headings and standard overview summaries, leaving curriculum guides verified only by loose file-level checks.

4. **Vestigial Duplicate Fallback Keyword Sets**:
   - Defensive static keyword and entity sets within the validation module duplicate the canonical topology registry, creating maintenance overhead and potential drift.

---

## Solution

1. **Universal Companion Note Macro Anchor Migration**:
   - Migrate all existing companion Markdown notes across all tracks (`top-100/`, `daily-practice/`, and `luffy/`) to declare standardized `Topology Node:` macro anchors in Section 3, mapping every tracked problem directly to its canonical node path in the 38-Node Topology Graph.

2. **Strict Mandatory Macro Anchor Enforcement in NoteStructureValidator**:
   - Remove the permissive soft fallback in the note validator, making the `Topology Node:` macro anchor strictly mandatory in Component 3. If a companion note lacks an explicit macro anchor or references an unregistered topology node, the validation gate strictly fails with clear diagnostics.

3. **Enhanced Non-Problem Documentation Schema Verification**:
   - Upgrade non-problem documentation validation to verify standard bilingual headings, structured overview sections, and local file reference integrity without imposing algorithm-specific 7-section schema rules.

4. **Elimination of Duplicate Static Taxonomy Fallbacks**:
   - Remove hardcoded static keyword fallbacks, ensuring the validation module exclusively loads taxonomy definitions from the canonical topology registry with clear diagnostic errors on load failure.

---

## User Stories

1. As a student studying algorithmic patterns, I want every companion note across all tracks to explicitly declare its `Topology Node:` macro anchor, so that I can immediately understand where each problem fits in the macro 38-node knowledge graph.
2. As a learner exploring the interactive Roadmap DAG, I want all companion notes to be fully registered with valid topology anchors, so that clicking into any topology node shows all associated problems without omissions.
3. As a developer adding a new LeetCode problem note, I want the validator to strictly fail if I forget the `Topology Node:` macro anchor line, so that I never accidentally commit an unanchored note.
4. As a test engineer, I want `update_index.py --lint --strict` to pass with 0 warnings across 100% of repository notes, so that CI quality gates remain clean and uncompromising.
5. As a compiler maintainer, I want the validator to source topology metadata strictly from the canonical registry without duplicate fallback dictionaries, so that adding new topology nodes never requires updating validator constants.
6. As a curriculum author, I want non-problem guide documents to be validated for bilingual headers and overview sections, so that curriculum overview notes maintain high editorial quality.
7. As a code reviewer, I want automated test suites to assert that omitting a macro anchor strictly fails validation, preventing future regressions from loosening schema enforcement.
8. As a student reviewing linked list problems, I want notes in both `luffy/` and `daily-practice/` tracks to use uniform macro anchor syntax (e.g. `Topology Node: [Linear Structures] ➔ [Linked Lists] ➔ [Two Pointers / Fast & Slow]`), ensuring seamless visual consistency.
9. As a student studying dynamic programming, I want DP problem notes to anchor to `[Linear Structures / Recursive Traverse] ➔ [Subproblem View] ➔ [Dynamic Programming]`, reinforcing the divide-and-conquer mental model.
10. As an AI assistant generating new solutions, I want explicit contracts requiring macro anchor lines in Section 3, ensuring all generated notes pass strict pre-commit hooks on the first attempt.

---

## Implementation Decisions

### 1. Macro Anchor Annotation Across All Repository Notes
- In all existing companion Markdown notes across all tracks:
  - In Section 3 ("Core Idea, Mental Model & Pattern Lineage"), insert a standardized macro anchor line immediately above the pattern lineage ASCII tree:
    `Topology Node: [Macro Group] ➔ [Subgroup] ➔ [Canonical Node ID / Display Title]`
  - Ensure every problem's anchor matches its canonical topic node registered in the 38-Node Compound Algorithmic Topology Graph.

### 2. Strict Macro Anchor Enforcement in NoteStructureValidator
- In the validation module:
  - In Section 3 validation, enforce that a `Topology Node:` line MUST be present.
  - Extract the declared anchor and verify that it contains at least one registered node ID, display category, or canonical tag present in the 38-Node Topology Graph.
  - If no `Topology Node:` line is found, fail validation with an explicit error: `"Component 3 is missing required 'Topology Node:' macro anchor."`
  - If the declared anchor does not match any registered node or category, fail validation with an informative diagnostic listing the unmapped anchor.

### 3. Non-Problem Documentation Auditing Hardening
- In the non-problem validation logic:
  - Assert that non-problem overview and guide documents contain a top-level H1 heading, non-empty body, balanced code block fences, and valid on-disk relative links.
  - Verify that overview documents include structured overview markers (e.g. `## Overview` or `## 概述` or `# Topic ...`).

### 4. Taxonomy Registry Purity
- In the validation module:
  - Remove all redundant static keyword/entity sets, relying cleanly on dynamic loading from the canonical topology registry.
  - If the registry fails to import, raise a descriptive configuration error.

---

## Testing Decisions

- **Testing Philosophy**: Verify public validation contracts and directory auditing end-to-end without coupling tests to internal regex details.
- **Primary Seam (`tests/test_note_structure.py`)**:
  - Assert that notes with missing `Topology Node:` macro anchors strictly fail validation.
  - Assert that notes with invalid `Topology Node:` macro anchors strictly fail validation.
  - Assert that notes with valid `Topology Node:` macro anchors pass validation.
  - Assert that 100% of audited companion notes across `top-100/`, `daily-practice/`, and `luffy/` pass strict 7-section validation with 0 errors.
  - Assert that non-problem documentation auditing passes for all curriculum guides.
- **Compiler Quality Gate Seam (`tests/test_update_index.py`)**:
  - Assert that `python3 update_index.py --lint --strict` succeeds with exit code 0 across the entire repository.

---

## Out of Scope

- Modifying existing Python algorithm solutions (preserving Core Rule 1 immutability).
- Writing the missing Top-100 companion notes (tracked as separate content authoring tasks).
- Changing frontend CSS visual themes or viewport layouts.

---

## Further Notes

- All changes must strictly comply with `AGENTS.md` (Core Rules 1 through 6) and `CONTEXT.md` architectural models.
