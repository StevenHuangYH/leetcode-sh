# 40. Combination Sum II
## Problem Walkthrough & Solution Notes

- **Difficulty:** Medium
- **Category:** Luffy Structured Curriculum
- **Core Technique:** Backtracking + Deduplication
- **LeetCode Link:** [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- **Corresponding Python File:** [`luffy/35-lc-0040-combination-sum-ii.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/luffy/35-lc-0040-combination-sum-ii.py)

---

## 1. Problem Overview & Core Strategy

Sort candidates; skip duplicates at same recursion depth with if i > start and nums[i] == nums[i-1].

---

## 2. Key Algorithmic Steps

1. **Initialization**: Set up required variables, pointers, hash maps, or queues.
2. **State Transition / Traversal**: Process elements iteratively or recursively while maintaining invariant states.
3. **Result Calculation & Return**: Return optimal answer.

---

## 3. Complexity Analysis

- **Time Complexity:** Optimal based on algorithm constraint.
- **Space Complexity:** Controlled within minimal required auxiliary space.
