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

    def test_missing_topology_lineage_diagram_fails(self):
        broken_note = VALID_NOTE_SAMPLE.replace("```\n[LC 0033] -> [LC 0153] -> [LC 0154]\n```", "Just plain text without diagram or model.")
        result = self.validator.validate(broken_note, "mock-no-lineage.md")
        self.assertFalse(result.is_valid)
        self.assertTrue(any("Topology Anchor" in err or "Pattern Lineage" in err for err in result.errors))

    def test_sample_repository_notes(self):

        sample_paths = [
            REPO_ROOT / "top-100" / "lc-0015-3sum.md",
            REPO_ROOT / "daily-practice" / "lc-0153-find-minimum-in-rotated-sorted-array.md",
            REPO_ROOT / "daily-practice" / "lc-0216-combination-sum-3.md",
            REPO_ROOT / "luffy" / "31-lc-0077-combinations.md",
        ]
        for note_path in sample_paths:
            if note_path.exists():
                content = note_path.read_text(encoding="utf-8")
                res = self.validator.validate(content, note_path.name)
                self.assertTrue(res.is_valid, f"Repo note {note_path.name} failed validation: {res.errors}")

    def test_universal_notes_directory_auditing_covers_all_luffy_notes(self):
        """Assert audit_notes_directory discovers and validates all numbered notes in luffy/."""
        from scripts.validator.note_validator import audit_notes_directory
        luffy_results = audit_notes_directory(REPO_ROOT / "luffy")
        self.assertEqual(len(luffy_results), 49, "Should audit exactly 49 LC companion notes in luffy/")
        for name, res in luffy_results.items():

            self.assertTrue(res.is_valid, f"Luffy note {name} failed validation: {res.errors}")

    def test_daily_practice_notes_auditing(self):
        """Assert all companion notes in daily-practice/ pass 7-section validation."""
        from scripts.validator.note_validator import audit_notes_directory
        daily_results = audit_notes_directory(REPO_ROOT / "daily-practice")
        self.assertGreaterEqual(len(daily_results), 20, "Should audit all daily practice companion notes")
        for name, res in daily_results.items():
            self.assertTrue(res.is_valid, f"Daily practice note {name} failed validation: {res.errors}")


if __name__ == "__main__":
    unittest.main()

