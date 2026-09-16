import unittest
from pathlib import Path
from scripts.validator import NoteStructureValidator, validate_note

REPO_ROOT = Path(__file__).parent.parent

VALID_NOTE_SAMPLE = r"""# LC 0153. Find Minimum in Rotated Sorted Array | 寻找旋转排序数组中的最小值

## 1. Header & File Links
- Problem Link: [LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- Companion Source: [lc-0153-find-minimum-in-rotated-sorted-array.py](./lc-0153-find-minimum-in-rotated-sorted-array.py)

## 2. Problem Statement & Constraints
### [EN]
Suppose an array of length n sorted in ascending order is rotated.

### [CN]
已知一个长度为 n 的升序数组在预先未知的某个点上进行了旋转。

## 3. Core Idea, Mental Model & Pattern Lineage
`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`
```
[LC 0033] -> [LC 0153] -> [LC 0154]
```

## 4. Step-by-Step Code Walkthrough
Step by step analysis.

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots
Interviewer questions and answers.

## 6. The Error Log & Complete Dry-Run
| Buggy Pattern / Traps | Symptom & Fail Case | Root Cause | Defensive Fix & Invariant |
| :--- | :--- | :--- | :--- |
| Binary Search Boundary | Infinite loop | mid calculation | Use left + (right - left) // 2 |

## 7. Complexity Analysis
| Dimension | Complexity | Rationale |
| :--- | :--- | :--- |
| Time Complexity | $O(\log n)$ | Binary reduction per iteration |
| Space Complexity | $O(1)$ | Constant extra space |
"""

class TestNoteStructureValidator(unittest.TestCase):
    def setUp(self):
        self.validator = NoteStructureValidator()

    def test_valid_7_section_note_passes(self):
        result = self.validator.validate(VALID_NOTE_SAMPLE, "mock-note.md")
        self.assertTrue(result.is_valid, f"Valid note failed: {result.errors}")
        self.assertEqual(len(result.missing_sections), 0)
        self.assertEqual(len(result.errors), 0)

    def test_missing_section_fails_with_diagnostic(self):
        # Remove section 6
        broken_note = VALID_NOTE_SAMPLE.replace("## 6. The Error Log & Complete Dry-Run", "## 6. Something Else")
        result = self.validator.validate(broken_note, "mock-broken.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Error Log" in err or "Component 6" in err for err in result.errors))

    def test_missing_bilingual_tags_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace("### [EN]", "### English")
        result = self.validator.validate(broken_note, "mock-no-en.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("bilingual" in err for err in result.errors))

    def test_invalid_topology_tag_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace("## 1. Header & File Links", "## 1. Header & File Links\n- Tags: completely_unrelated_nonsense_xyz")
        result = self.validator.validate(broken_note, "mock-bad-tags.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("topology taxonomy keyword" in err for err in result.errors))

    def test_missing_topology_macro_anchor_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace(
            "`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`\n", ""
        )
        result = self.validator.validate(broken_note, "mock-no-anchor.md")
        self.assertFalse(result.is_valid)
        self.assertIn("Component 3 is missing required 'Topology Node:' macro anchor.", result.errors)

    def test_missing_topology_lineage_diagram_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace(
            "```\n[LC 0033] -> [LC 0153] -> [LC 0154]\n```", "Just plain text without diagram or model."
        )
        result = self.validator.validate(broken_note, "mock-no-lineage.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Pattern Lineage" in err for err in result.errors))

    def test_invalid_topology_macro_anchor_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace(
            "`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`",
            "`Topology Node: [FakeCategory] ➔ [UnknownSubtree] ➔ [NonExistentEntity]`"
        )
        result = self.validator.validate(broken_note, "mock-bad-macro-anchor.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Topology Node" in err and "CANONICAL_TOPOLOGY_NODES" in err for err in result.errors))

    def test_valid_topology_macro_anchors_pass(self):
        valid_anchors = [
            "Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]",
            "Topology Node: [Exhaustive Search] ➔ [Traverse View] ➔ [Backtracking]",
            "`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`",
            "Topology Node: [Data Structures] ➔ [Stack & Queue]",
            "Topology Node: [Array Techniques] ➔ [Diff Array]",
        ]
        for anchor in valid_anchors:
            note = VALID_NOTE_SAMPLE.replace(
                "`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`",
                anchor
            )
            res = self.validator.validate(note, "mock-valid-anchor.md")
            self.assertTrue(res.is_valid, f"Anchor '{anchor}' failed validation: {res.errors}")

    def test_non_problem_documentation_auditing_validates_without_7_section_schema(self):
        guide_content = """# Topic 11: OOP Foundations & Design Overview

This guide provides a comprehensive overview of object-oriented programming foundations and class encapsulation patterns.

## Overview
- Encapsulation: bundling data and methods.
- Inheritance: extending base behavior.
- Polymorphism: uniform interface for different types.
"""
        # Full 7-section validator would fail this guide (missing sections 2-7)
        full_res = self.validator.validate(guide_content, "guide.md")
        self.assertFalse(full_res.is_valid)

        # Non-problem doc validator should pass
        doc_res = self.validator.validate_non_problem_doc(guide_content, "guide.md")
        self.assertTrue(doc_res.is_valid, f"Non-problem doc validation failed: {doc_res.errors}")

    def test_sample_repository_notes(self):
        sample_paths = [
            REPO_ROOT / "problems" / "top-100" / "lc-0022-generate-parentheses.md",
            REPO_ROOT / "problems" / "daily-practice" / "lc-0077-combinations.md",
            REPO_ROOT / "problems" / "daily-practice" / "lc-0216-combination-sum-3.md",
            REPO_ROOT / "problems" / "daily-practice" / "lc-0153-find-minimum-in-rotated-sorted-array.md",
        ]
        for note_path in sample_paths:
            if note_path.exists():
                content = note_path.read_text(encoding="utf-8")
                res = self.validator.validate(content, note_path.name)
                self.assertTrue(res.is_valid, f"Repo note {note_path.name} failed validation: {res.errors}")

    def test_universal_notes_directory_auditing_covers_all_luffy_notes_and_docs(self):
        """Assert audit_notes_directory discovers all markdown files in luffy/ and all pass auditing."""
        from scripts.validator.note_validator import audit_notes_directory
        luffy_results = audit_notes_directory(REPO_ROOT / "problems" / "luffy")
        self.assertEqual(len(luffy_results), 53, "Should audit all 53 markdown files in luffy/")
        for name, res in luffy_results.items():
            self.assertTrue(res.is_valid, f"Luffy note {name} failed validation: {res.errors}")

    def test_daily_practice_notes_auditing(self):
        """Assert all companion notes in daily-practice/ pass validation."""
        from scripts.validator.note_validator import audit_notes_directory
        daily_results = audit_notes_directory(REPO_ROOT / "problems" / "daily-practice")
        self.assertEqual(len(daily_results), 21, "Should audit all 21 daily practice companion notes")
        for name, res in daily_results.items():
            self.assertTrue(res.is_valid, f"Daily practice note {name} failed validation: {res.errors}")

    def test_top_100_notes_auditing(self):
        """Assert all companion notes in top-100/ pass validation."""
        from scripts.validator.note_validator import audit_notes_directory
        top_100_results = audit_notes_directory(REPO_ROOT / "problems" / "top-100")
        self.assertEqual(len(top_100_results), 23, "Should audit all 23 top-100 companion notes")
        for name, res in top_100_results.items():
            self.assertTrue(res.is_valid, f"Top-100 note {name} failed validation: {res.errors}")

    def test_audit_workspace_tracks(self):
        """Assert audit_workspace_tracks audits all registered tracks across the repository."""
        from scripts.validator.note_validator import audit_workspace_tracks
        from scripts.compiler.track_definitions import TrackRegistry

        track_results = audit_workspace_tracks(REPO_ROOT)
        expected_tracks = set(TrackRegistry.get_track_paths())
        self.assertEqual(set(track_results.keys()), expected_tracks)

        for track_path, file_results in track_results.items():
            self.assertTrue(len(file_results) > 0, f"Track {track_path} should contain audited notes")
            for filename, result in file_results.items():
                self.assertTrue(result.is_valid, f"Note {filename} in {track_path} failed: {result.errors}")

    def test_canonical_topology_data_cache_consistency(self):
        """Assert _get_canonical_topology_data caches keywords and entities properly."""
        from scripts.validator.note_validator import (
            _get_canonical_topology_data,
            get_canonical_topology_keywords,
            get_canonical_topology_entities,
        )
        data1 = _get_canonical_topology_data()
        data2 = _get_canonical_topology_data()
        self.assertIs(data1, data2, "Cached helper should return identical tuple reference")
        keywords = get_canonical_topology_keywords()
        entities = get_canonical_topology_entities()
        self.assertEqual(keywords, data1[0])
        self.assertEqual(entities, data1[1])
        self.assertIn("backtracking", keywords)
        self.assertIn("binary search", entities)

    def test_non_problem_documentation_relative_link_auditing(self):
        """Assert validate_non_problem_document verifies relative links against disk."""
        # 1. Valid links: existing local file, anchor link, and web URL
        valid_doc = """# Guide Document

## Links
- [Python Source](./02-lc-0001-two-sum.py)
- [Anchor Link](#guide-document)
- [Web Link](https://example.com/docs)
"""
        res_valid = self.validator.validate_non_problem_doc(
            valid_doc,
            str(REPO_ROOT / "problems" / "luffy" / "02-lc-0001-two-sum.md")
        )
        self.assertTrue(res_valid.is_valid, f"Expected valid doc to pass: {res_valid.errors}")

        # 2. Broken relative link
        broken_doc = """# Guide Document

## Links
- [Broken Link](./non_existent_file_xyz_123.py)
"""
        res_broken = self.validator.validate_non_problem_doc(
            broken_doc,
            str(REPO_ROOT / "problems" / "luffy" / "02-lc-0001-two-sum.md")
        )
        self.assertFalse(res_broken.is_valid)
        self.assertTrue(any("Broken relative link" in err for err in res_broken.errors))

    def test_normalize_token_aliases_helper(self):
        """Assert _normalize_token_aliases generates expected token variants."""
        from scripts.validator.note_validator import _normalize_token_aliases
        self.assertEqual(_normalize_token_aliases(""), set())
        self.assertEqual(_normalize_token_aliases("  "), set())
        self.assertEqual(_normalize_token_aliases("binary-tree"), {"binary-tree", "binary tree"})
        self.assertEqual(_normalize_token_aliases("sliding_window"), {"sliding_window", "sliding window"})
        self.assertEqual(_normalize_token_aliases("Backtracking"), {"backtracking"})

    def test_problem_blueprint_component_3_variant_passes(self):
        """Assert notes with 'Problem Blueprint' in Section 2 or Section 3 pass Component 3 validation."""
        blueprint_note = VALID_NOTE_SAMPLE.replace(
            "## 3. Core Idea, Mental Model & Pattern Lineage",
            "## 3. Problem Blueprint & Core Invariant"
        )
        res = self.validator.validate(blueprint_note, "mock-blueprint.md")
        self.assertTrue(res.is_valid, f"Expected blueprint note to pass: {res.errors}")

    def test_non_problem_doc_missing_overview_structure_fails(self):
        """Assert non-problem docs missing overview structure or intro text fail."""
        empty_overview_doc = "# Title Only\n"
        res = self.validator.validate_non_problem_doc(empty_overview_doc, "empty_overview.md")
        self.assertFalse(res.is_valid)
        self.assertTrue(any("overview structure" in err for err in res.errors))


if __name__ == "__main__":
    unittest.main()

