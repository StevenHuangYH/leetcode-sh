import sys
import unittest
from pathlib import Path

# Add top-100 to path
sys.path.insert(0, str(Path(__file__).parent.parent / "top-100"))

# Import module
import importlib
lc_0034 = importlib.import_module("lc-0034-find-first-and-last-position-of-element-in-sorted-array")

class TestLC0034(unittest.TestCase):
    def setUp(self):
        self.solution = lc_0034.Solution()
        self.lb_closed = lc_0034.lower_bound
        self.lb_half_open = lc_0034.lower_bound2
        self.lb_open = lc_0034.lower_bound3

    def test_search_range_standard_cases(self):
        self.assertEqual(self.solution.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(self.solution.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
        self.assertEqual(self.solution.searchRange([], 0), [-1, -1])
        self.assertEqual(self.solution.searchRange([1], 1), [0, 0])
        self.assertEqual(self.solution.searchRange([2, 2], 2), [0, 1])

    def test_lower_bound_templates_consistency(self):
        test_cases = [
            ([5, 7, 7, 8, 8, 10], 8, 3),
            ([5, 7, 7, 8, 8, 10], 6, 1),
            ([5, 7, 7, 8, 8, 10], 5, 0),
            ([5, 7, 7, 8, 8, 10], 11, 6),
            ([2, 2], 2, 0),
            ([2, 2], 1, 0),
            ([2, 2], 3, 2),
            ([1], 1, 0),
            ([], 0, 0),
        ]
        
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target):
                self.assertEqual(self.lb_closed(nums, target), expected, f"Closed interval failed for {nums}, {target}")
                self.assertEqual(self.lb_half_open(nums, target), expected, f"Half-open interval failed for {nums}, {target}")
                self.assertEqual(self.lb_open(nums, target), expected, f"Open interval failed for {nums}, {target}")

if __name__ == "__main__":
    unittest.main()
