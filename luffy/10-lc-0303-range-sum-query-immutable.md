# 303. Range Sum Query - Immutable
## Problem Walkthrough & Solution Notes

- **Difficulty:** Easy
- **Category:** Luffy Structured Curriculum
- **Core Technique:** Prefix Sum Array
- **LeetCode Link:** [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- **Corresponding Python File:** [`luffy/10-lc-0303-range-sum-query-immutable.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/luffy/10-lc-0303-range-sum-query-immutable.py)

---

## 1. Problem Overview & Core Strategy

Precompute prefix sums: query(i, j) = prefix[j+1] - prefix[i] in O(1).

---

## 2. Key Algorithmic Steps

1. **Initialization**: Set up required variables, pointers, hash maps, or queues.
2. **State Transition / Traversal**: Process elements iteratively or recursively while maintaining invariant states.
3. **Result Calculation & Return**: Return optimal answer.

---

## 3. Complexity Analysis

- **Time Complexity:** Optimal based on algorithm constraint.
- **Space Complexity:** Controlled within minimal required auxiliary space.
