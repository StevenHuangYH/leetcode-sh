# LeetCode Self-Practices & Algorithm Curriculum

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116.svg?logo=leetcode&logoColor=white)](https://leetcode.com/)
[![Problems Solved](https://img.shields.io/badge/Problems_Indexed-164+-brightgreen.svg)]()
[![Interactive Viewer](https://img.shields.io/badge/Web_Viewer-index.html-blueviolet.svg)]()

Welcome to my personal LeetCode question cracking collections. This repository is where I store my solutions, and categorize my various data structures or problem sets.

---

## Table of Contents

1. [Practice Statistics & Summary](#practice-statistics--summary)
2. [Repository Structure](#repository-structure)
3. [Top 100 Liked Track](#top-100-liked-track)
4. [Daily Practice Track](#daily-practice-track)
5. [Topic-Wise Curriculum & Problem Index](#topic-wise-curriculum--problem-index)
   - [1. Arrays, Strings, Two Pointers & Sliding Window](#1-arrays-strings-two-pointers--sliding-window)
   - [2. Binary Search](#2-binary-search)
   - [3. Prefix Sum & Difference Arrays](#3-prefix-sum--difference-arrays)
   - [4. Intervals & In-Place Array Hashing](#4-intervals--in-place-array-hashing)
   - [5. Linked Lists](#5-linked-lists)
   - [6. Stacks & Queues](#6-stacks--queues)
   - [7. Trees & Binary Search Trees (BST)](#7-trees--binary-search-trees-bst)
   - [8. Backtracking & Combinatorics](#8-backtracking--combinatorics)
   - [9. Graph Algorithms (DFS, BFS, Topological Sort)](#9-graph-algorithms-dfs-bfs-topological-sort)
   - [10. Dynamic Programming & Math / Game Theory](#10-dynamic-programming--math--game-theory)
   - [11. Object-Oriented Programming (OOP) & Foundations](#11-object-oriented-programming-oop--foundations)
6. [Interactive Web Viewer & Study Station](#interactive-web-viewer--study-station)
7. [How to Run & Practice](#how-to-run--practice)

---

## Practice Statistics & Summary

| Difficulty | Companion Notes Count | Percentage | Total Tracked Solutions / Stubs |
| :--- | :---: | :---: | :---: |
| **Easy** | 25 | ~33% | 24 |
| **Medium** | 47 | ~63% | 137 |
| **Hard** | 3 | ~4% | 3 |
| **Total** | **75 In-Depth Notes** | **100%** | **164 Problem Entities** |

---

## Repository Structure

```tree
leetcode-sh/
├── top-100/                      # LeetCode Top 100 Liked Problems & In-Depth Notes
│   ├── lc-0003-longest-substring-without-repeating-characters.py
│   ├── lc-0003-longest-substring-without-repeating-characters.md
│   ├── lc-0011-container-with-most-water.py
│   ├── lc-0011-container-with-most-water.md
│   ├── lc-0015-3sum.py
│   ├── lc-0015-3sum.md
│   ├── lc-0016-3-sum-closest.py
│   ├── lc-0016-3-sum-closest.md
│   ├── lc-0033-search-in-rotated-sorted-array.py
│   ├── lc-0033-search-in-rotated-sorted-array.md
│   ├── lc-0034-find-first-and-last-position-of-element-in-sorted-array.py
│   ├── lc-0034-find-first-and-last-position-of-element-in-sorted-array.md
│   ├── lc-0042-trapping-rain-water.py
│   ├── lc-0042-trapping-rain-water.md
│   ├── lc-0053-maximum-subarray.py
│   ├── lc-0053-maximum-subarray.md
│   ├── lc-0141-linked-list-cycle.py
│   ├── lc-0141-linked-list-cycle.md
│   ├── lc-0142-linked-list-cycle-ii.py
│   ├── lc-0142-linked-list-cycle-ii.md
│   ├── lc-0162-find-peak-element.py
│   ├── lc-0162-find-peak-element.md
│   ├── lc-0167-two-sum-ii-input-array-is-sorted.py
│   ├── lc-0167-two-sum-ii-input-array-is-sorted.md
│   ├── lc-0209-minimum-size-subarray-sum.py
│   ├── lc-0209-minimum-size-subarray-sum.md
│   ├── lc-0713-subarray-product-less-than-k.py
│   └── lc-0713-subarray-product-less-than-k.md
├── daily-practice/               # Daily LeetCode Practices & Weekly Contest Challenges
│   ├── lc-0025-reverse-nodes-in-k-group.py
│   ├── lc-0025-reverse-nodes-in-k-group.md
│   ├── lc-0092-reversed-linked-list-2.py
│   ├── lc-0092-reversed-linked-list-2.md
│   ├── lc-0153-find-minimum-in-rotated-sorted-array.py
│   ├── lc-0153-find-minimum-in-rotated-sorted-array.md
│   ├── lc-0206-reversed-linked-list.py
│   ├── lc-0206-reversed-linked-list.md
│   ├── lc-0876-middle-of-the-linked-list.py
│   ├── lc-0876-middle-of-the-linked-list.md
│   ├── lc-2029-stone-game-ix.py
│   ├── lc-2029-stone-game-ix.md
│   ├── lc-3090-maximum-length-substring-with-at-most-two-occurrences.py
│   ├── lc-3090-maximum-length-substring-with-at-most-two-occurrences.md
│   ├── lc-3471-find-the-largest-almost-missing-integer.py
│   └── lc-3471-find-the-largest-almost-missing-integer.md
├── luffy/                        # Core 42-Topic Structured Algorithm Curriculum
│   ├── 01-lc-2235-add-two-integers.py / .md
│   ├── 02-lc-0001-two-sum.py / .md
│   ├── ...
│   ├── 42-lc-0207-course-schedule.py / .md
│   └── file_topics.txt           # Topic index reference
├── index.html                    # Single-Page App (SPA) Study Station & Split-Pane Viewer
├── update_index.py               # Automated index builder, watcher & git hook installer
└── README.md                     # Repository documentation & guide
```

---

## Top 100 Liked Track

A dedicated tracking index for **LeetCode Top 100 Liked / High-Frequency Interview** problems implemented in this repository.

| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |
| :-: | :--- | :-: | :--- | :-: | :--- |
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py)<br>[`luffy/02-lc-0001-two-sum.md`](luffy/02-lc-0001-two-sum.md) | Easy | Hash Map (Complement `target - num`) |
| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py)<br>[`top-100/lc-0003-longest-substring-without-repeating-characters.md`](top-100/lc-0003-longest-substring-without-repeating-characters.md) | Medium | Dynamic Sliding Window |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py)<br>[`top-100/lc-0011-container-with-most-water.md`](top-100/lc-0011-container-with-most-water.md) | Medium | Two Pointers (Greedy Shorter Line) |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/lc-0015-3sum.py`](top-100/lc-0015-3sum.py)<br>[`top-100/lc-0015-3sum.md`](top-100/lc-0015-3sum.md) | Medium | Sort + Two Pointers + 2-Way Extreme Pruning |
| **16** | 3Sum Closest | [LC 16](https://leetcode.com/problems/3sum-closest/) | [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)<br>[`top-100/lc-0016-3-sum-closest.md`](top-100/lc-0016-3-sum-closest.md) | Medium | Sort + Two Pointers + 2-Way Extreme Pruning |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)<br>[`luffy/19-lc-0020-valid-parentheses.md`](luffy/19-lc-0020-valid-parentheses.md) | Easy | Stack Matching |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-0021-merge-two-sorted-lists.py`](luffy/16-lc-0021-merge-two-sorted-lists.py)<br>[`luffy/16-lc-0021-merge-two-sorted-lists.md`](luffy/16-lc-0021-merge-two-sorted-lists.md) | Easy | Dummy Head + Two Pointers |
| **26** | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`luffy/05-lc-0026-remove-duplicates-from-sorted-array.py`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.py)<br>[`luffy/05-lc-0026-remove-duplicates-from-sorted-array.md`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.md) | Easy | Slow/Fast Two Pointers (In-place) |
| **33** | Search in Rotated Sorted Array | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)<br>[`top-100/lc-0033-search-in-rotated-sorted-array.md`](top-100/lc-0033-search-in-rotated-sorted-array.md) | Medium | Red-Blue Binary Search (`nums[-1]`) |
| **34** | Find First and Last Position of Element in Sorted Array | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)<br>[`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md) | Medium | Universal `lower_bound` Binary Search Framework |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-0039-combination-sum.py`](luffy/34-lc-0039-combination-sum.py)<br>[`luffy/34-lc-0039-combination-sum.md`](luffy/34-lc-0039-combination-sum.md) | Medium | Backtracking (Unbounded Choice) |
| **41** | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`luffy/14-lc-0041-first-missing-positive.py`](luffy/14-lc-0041-first-missing-positive.py)<br>[`luffy/14-lc-0041-first-missing-positive.md`](luffy/14-lc-0041-first-missing-positive.md) | Hard | Cyclic Sort / In-Place Hashing ($O(1)$ space) |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py)<br>[`top-100/lc-0042-trapping-rain-water.md`](top-100/lc-0042-trapping-rain-water.md) | Hard | Two Pointers Sweep / Prefix-Suffix Max |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-0046-permutations.py`](luffy/32-lc-0046-permutations.py)<br>[`luffy/32-lc-0046-permutations.md`](luffy/32-lc-0046-permutations.md) | Medium | Backtracking (`used` array / in-place swap) |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py)<br>[`top-100/lc-0053-maximum-subarray.md`](top-100/lc-0053-maximum-subarray.md) | Medium | Kadane's Algorithm / DP ($O(1)$ space) |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-0056-merge-intervals.py`](luffy/13-lc-0056-merge-intervals.py)<br>[`luffy/13-lc-0056-merge-intervals.md`](luffy/13-lc-0056-merge-intervals.md) | Medium | Interval Sorting & Merging |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-0078-subsets.py`](luffy/33-lc-0078-subsets.py)<br>[`luffy/33-lc-0078-subsets.md`](luffy/33-lc-0078-subsets.md) | Medium | Backtracking / Cascading |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-0079-word-search.py`](luffy/37-lc-0079-word-search.py)<br>[`luffy/37-lc-0079-word-search.md`](luffy/37-lc-0079-word-search.md) | Medium | 2D Grid DFS + Backtracking |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-0094-binary-tree-inorder-traversal.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py)<br>[`luffy/25-lc-0094-binary-tree-inorder-traversal.md`](luffy/25-lc-0094-binary-tree-inorder-traversal.md) | Easy | Inorder DFS (L-Root-R) |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-inorder.md`](luffy/29-lc-0098-validate-binary-search-tree-inorder.md) | Medium | BST Range Bounds & Inorder Monotonicity |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-0102-binary-tree-level-order-traversal.py`](luffy/28-lc-0102-binary-tree-level-order-traversal.py)<br>[`luffy/28-lc-0102-binary-tree-level-order-traversal.md`](luffy/28-lc-0102-binary-tree-level-order-traversal.md) | Medium | Level-by-Level Queue BFS |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-0104-maximum-depth-of-binary-tree.py`](luffy/26-lc-0104-maximum-depth-of-binary-tree.py)<br>[`luffy/26-lc-0104-maximum-depth-of-binary-tree.md`](luffy/26-lc-0104-maximum-depth-of-binary-tree.md) | Easy | Divide & Conquer / DFS |
| **105** | Construct Tree from Pre & Inorder | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)<br>[`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) | Medium | Preorder Root + Inorder Subtree Splitting |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`luffy/36-lc-0131-palindrome-partitioning.py`](luffy/36-lc-0131-palindrome-partitioning.py)<br>[`luffy/36-lc-0131-palindrome-partitioning.md`](luffy/36-lc-0131-palindrome-partitioning.md) | Medium | Backtracking + Palindrome Verification |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`top-100/lc-0141-linked-list-cycle.py`](top-100/lc-0141-linked-list-cycle.py)<br>[`top-100/lc-0141-linked-list-cycle.md`](top-100/lc-0141-linked-list-cycle.md)<br>[`luffy/17-lc-0141-linked-list-cycle.py`](luffy/17-lc-0141-linked-list-cycle.py) | Easy | Floyd's Fast & Slow Pointers (2:1 Speed Collision) |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`top-100/lc-0142-linked-list-cycle-ii.py`](top-100/lc-0142-linked-list-cycle-ii.py)<br>[`top-100/lc-0142-linked-list-cycle-ii.md`](top-100/lc-0142-linked-list-cycle-ii.md)<br>[`luffy/18-lc-0142-linked-list-cycle-ii.py`](luffy/18-lc-0142-linked-list-cycle-ii.py) | Medium | Fast/Slow Pointer + Mathematical Collision Entry ($a = c$) |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-0155-min-stack.py`](luffy/21-lc-0155-min-stack.py)<br>[`luffy/21-lc-0155-min-stack.md`](luffy/21-lc-0155-min-stack.md) | Medium | Auxiliary Min Stack |
| **162** | Find Peak Element | [LC 162](https://leetcode.com/problems/find-peak-element/) | [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)<br>[`top-100/lc-0162-find-peak-element.md`](top-100/lc-0162-find-peak-element.md) | Medium | Binary Search on Slope / Red-Blue Interval |
| **167** | Two Sum II - Sorted Array | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`top-100/lc-0167-two-sum-ii-input-array-is-sorted.md`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.md) | Medium | Sorted Array Inward Two Pointers |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-0200-number-of-islands.py`](luffy/38-lc-0200-number-of-islands.py)<br>[`luffy/38-lc-0200-number-of-islands.md`](luffy/38-lc-0200-number-of-islands.md) | Medium | 2D Grid Sink Islands (DFS / BFS) |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-0206-reverse-linked-list.py`](luffy/15-lc-0206-reverse-linked-list.py)<br>[`luffy/15-lc-0206-reverse-linked-list.md`](luffy/15-lc-0206-reverse-linked-list.md) | Easy | In-Place 3-Pointer Iteration (`prev, curr, nxt`) |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`luffy/42-lc-0207-course-schedule.py`](luffy/42-lc-0207-course-schedule.py)<br>[`luffy/42-lc-0207-course-schedule.md`](luffy/42-lc-0207-course-schedule.md) | Medium | Topological Sort (Kahn's BFS / DFS) |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)<br>[`top-100/lc-0209-minimum-size-subarray-sum.md`](top-100/lc-0209-minimum-size-subarray-sum.md) | Medium | Dynamic Sliding Window |
| **236** | Lowest Common Ancestor of Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py)<br>[`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md) | Medium | Postorder DFS |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-0394-decode-string.py`](luffy/23-lc-0394-decode-string.py)<br>[`luffy/23-lc-0394-decode-string.md`](luffy/23-lc-0394-decode-string.md) | Medium | Dual Stack (Count & String Stacks) |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-0560-subarray-sum-equals-k.py`](luffy/11-lc-0560-subarray-sum-equals-k.py)<br>[`luffy/11-lc-0560-subarray-sum-equals-k.md`](luffy/11-lc-0560-subarray-sum-equals-k.md) | Medium | Prefix Sum + Hash Map |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py)<br>[`top-100/lc-0713-subarray-product-less-than-k.md`](top-100/lc-0713-subarray-product-less-than-k.md) | Medium | Sliding Window & Subarray Counting |
| **994** | Rotting Oranges | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`luffy/40-lc-0994-rotting-oranges.py`](luffy/40-lc-0994-rotting-oranges.py)<br>[`luffy/40-lc-0994-rotting-oranges.md`](luffy/40-lc-0994-rotting-oranges.md) | Medium | Multi-source BFS Queue |

---

## Daily Practice Track

Tracking daily challenge questions, weekly contest problems, and algorithmic practice.

| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |
| :-: | :--- | :-: | :--- | :-: | :--- |
| **25** | Reverse Nodes in k-Group | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [`daily-practice/lc-0025-reverse-nodes-in-k-group.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py)<br>[`daily-practice/lc-0025-reverse-nodes-in-k-group.md`](daily-practice/lc-0025-reverse-nodes-in-k-group.md) | Hard | Sentinel Dummy + k-Group Reversal (`p0`, `pre`, `cur`) |
| **92** | Reverse Linked List II | [LC 92](https://leetcode.com/problems/reverse-linked-list-ii/) | [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)<br>[`daily-practice/lc-0092-reversed-linked-list-2.md`](daily-practice/lc-0092-reversed-linked-list-2.md) | Medium | Dummy Node + Local Segment Reversal (`p0`, `pre`, `cur`) |
| **153** | Find Minimum in Rotated Sorted Array | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)<br>[`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md) | Medium | Binary Search on Two-Segment Step Array (`nums[-1]`) |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`daily-practice/lc-0206-reversed-linked-list.py`](daily-practice/lc-0206-reversed-linked-list.py)<br>[`daily-practice/lc-0206-reversed-linked-list.md`](daily-practice/lc-0206-reversed-linked-list.md) | Easy | 3-Pointer Pointer Reversal (`pre`, `cur`, `nxt`) |
| **876** | Middle of the Linked List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | [`daily-practice/lc-0876-middle-of-the-linked-list.py`](daily-practice/lc-0876-middle-of-the-linked-list.py)<br>[`daily-practice/lc-0876-middle-of-the-linked-list.md`](daily-practice/lc-0876-middle-of-the-linked-list.md) | Easy | Fast & Slow Pointers (`slow=1`, `fast=2`) |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py)<br>[`daily-practice/lc-2029-stone-game-ix.md`](daily-practice/lc-2029-stone-game-ix.md) | Medium | Modulo 3 Arithmetic / Game Theory |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)<br>[`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md) | Easy | Sliding Window / Frequency Map |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py)<br>[`daily-practice/lc-3471-find-the-largest-almost-missing-integer.md`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.md) | Easy | Fixed Sliding Window + Frequency Hashing |

---

## Topic-Wise Curriculum & Problem Index

### 1. Arrays, Strings, Two Pointers & Sliding Window

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py) | Easy | Hash Map | Single-pass hash map storing complement `target - num`. |
| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py) | Medium | Sliding Window | Maintain set/dict window; contract left pointer when duplicate seen. |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py) | Medium | Two Pointers (Left/Right) | Move the pointer pointing to the shorter line to potentially maximize area. |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/lc-0015-3sum.py`](top-100/lc-0015-3sum.py)<br>[`top-100/lc-0015-3sum.md`](top-100/lc-0015-3sum.md) | Medium | Two Pointers / Extreme Pruning | Sort array; fix anchor $nums[i]$; 2-way extreme pruning & deduplication. |
| **16** | 3Sum Closest | [LC 16](https://leetcode.com/problems/3sum-closest/) | [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)<br>[`top-100/lc-0016-3-sum-closest.md`](top-100/lc-0016-3-sum-closest.md) | Medium | Two Pointers / 2-Way Bound Pruning | Sort array; fix anchor $nums[i]$; track closest $|sum - target|$ with $\mathcal{O}(1)$ min/max sum pruning. |
| **26** | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`luffy/05-lc-0026-remove-duplicates-from-sorted-array.py`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.py) | Easy | Two Pointers (Slow/Fast) | Overwrite duplicate elements in-place with slow pointer. |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py) | Hard | Two Pointers / Pre-Suf Max | Inward two-pointer sweep tracking `pre_max` and `suf_max`. |
| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py) | Medium | Matrix Simulation | Layer-by-layer traversal with boundary tracking (top, bottom, left, right). |
| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py) | Medium | Two Pointers (Inward) | Exploit sorted order; shrink search space based on sum vs target (1-based index). |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py) | Medium | Sliding Window | Expand right pointer to reach target sum, then shrink left to minimize window. |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py) | Medium | Sliding Window / Product Counting | Maintain window product `prod < k`; count valid subarrays ending at `right` with `right - left + 1`. |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py) | Easy | Sliding Window / Frequency Map | Window condition: maintain character frequency `<= 2`. |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py) | Easy | Fixed Sliding Window / Hash Table | Slide fixed window of size $k$; count frequencies across distinct windows using set deduplication. |

---

### 2. Binary Search

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **33** | Search in Rotated Sorted Array | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)<br>[`top-100/lc-0033-search-in-rotated-sorted-array.md`](top-100/lc-0033-search-in-rotated-sorted-array.md) | Medium | Binary Search on Rotated Array (`nums[-1]`) | Compare `nums[mid]` & `target` with `nums[-1]`; classify segment via Red-Blue framework in $O(\log n)$. |
| **34** | Find First and Last Position of Element in Sorted Array | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)<br>[`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md) | Medium | Binary Search (`lower_bound`) | Use `lower_bound(target)` for start and `lower_bound(target + 1) - 1` for end in $O(\log n)$. |
| **153** | Find Minimum in Rotated Sorted Array | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)<br>[`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md) | Medium | Binary Search on Two-Segment Array (`nums[-1]`) | Compare `nums[mid]` with `nums[-1]`; identify left/right step segment in $O(\log n)$. |
| **162** | Find Peak Element | [LC 162](https://leetcode.com/problems/find-peak-element/) | [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)<br>[`top-100/lc-0162-find-peak-element.md`](top-100/lc-0162-find-peak-element.md) | Medium | Binary Search (Slope Peak / Open Interval) | Check `nums[mid] > nums[mid+1]` slope; shrink search space via Red-Blue framework in $O(\log n)$. |
| **704** | Binary Search | [LC 704](https://leetcode.com/problems/binary-search/) | [`luffy/07-lc-0704-binary-search.py`](luffy/07-lc-0704-binary-search.py) | Easy | Binary Search (Closed Interval) | `left <= right` with `mid = left + (right - left) // 2` to prevent overflow. |

---

### 3. Prefix Sum & Difference Arrays

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py) | Easy | Prefix Sum Array | Precompute cumulative sum array: `query(i, j) = prefix[j+1] - prefix[i]` in $O(1)$. |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-0560-subarray-sum-equals-k.py`](luffy/11-lc-0560-subarray-sum-equals-k.py) | Medium | Prefix Sum + Hash Map | Track frequency of running prefix sums; check if `curr_sum - k` occurred. |
| **1109** | Corporate Flight Bookings | [LC 1109](https://leetcode.com/problems/corporate-flight-bookings/) | [`luffy/12-lc-1109-corporate-flight-bookings.py`](luffy/12-lc-1109-corporate-flight-bookings.py) | Medium | Difference Array | Range update $[l, r]$ by `diff[l] += val` and `diff[r+1] -= val`, then compute prefix sums. |

---

### 4. Intervals & In-Place Array Hashing

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **41** | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`luffy/14-lc-0041-first-missing-positive.py`](luffy/14-lc-0041-first-missing-positive.py) | Hard | Cyclic Sort / In-Place Hash | Place number `x` at index `x - 1` in $O(n)$ time and $O(1)$ extra space. |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-0056-merge-intervals.py`](luffy/13-lc-0056-merge-intervals.py) | Medium | Interval Sorting | Sort intervals by start time and merge overlapping segments (`curr.start <= prev.end`). |

---

### 5. Linked Lists

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-0021-merge-two-sorted-lists.py`](luffy/16-lc-0021-merge-two-sorted-lists.py) | Easy | Dummy Head + Two Pointers | Build new list with dummy head, appending the smaller node at each step. |
| **25** | Reverse Nodes in k-Group | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [`daily-practice/lc-0025-reverse-nodes-in-k-group.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py)<br>[`daily-practice/lc-0025-reverse-nodes-in-k-group.md`](daily-practice/lc-0025-reverse-nodes-in-k-group.md) | Hard | Length Check + k-Group In-Place Reversal | Precompute length $n$; reverse $k$ nodes iteratively; 4-step stitch and advance $p_0$ in $O(n)$ time and $O(1)$ space. |
| **92** | Reverse Linked List II | [LC 92](https://leetcode.com/problems/reverse-linked-list-ii/) | [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)<br>[`daily-practice/lc-0092-reversed-linked-list-2.md`](daily-practice/lc-0092-reversed-linked-list-2.md) | Medium | Sentinel Dummy + 3-Pointer Reversal | Advance $p_0$ to $left-1$, reverse $right-left+1$ nodes, reconnect tail/head in $O(n)$ time. |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`top-100/lc-0141-linked-list-cycle.py`](top-100/lc-0141-linked-list-cycle.py)<br>[`top-100/lc-0141-linked-list-cycle.md`](top-100/lc-0141-linked-list-cycle.md)<br>[`luffy/17-lc-0141-linked-list-cycle.py`](luffy/17-lc-0141-linked-list-cycle.py) | Easy | Floyd's Fast & Slow Pointers | Fast moves 2 steps, slow moves 1 step; relative speed 1 guarantees collision in cycle. |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`top-100/lc-0142-linked-list-cycle-ii.py`](top-100/lc-0142-linked-list-cycle-ii.py)<br>[`top-100/lc-0142-linked-list-cycle-ii.md`](top-100/lc-0142-linked-list-cycle-ii.md)<br>[`luffy/18-lc-0142-linked-list-cycle-ii.py`](luffy/18-lc-0142-linked-list-cycle-ii.py) | Medium | Floyd's Algorithm + Math | Reset head upon collision; both advance by 1 step ($a=c$) to meet at cycle entry in $O(n)$ time and $O(1)$ space. |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-0206-reverse-linked-list.py`](luffy/15-lc-0206-reverse-linked-list.py) | Easy | Iterative Pointer Reversal | Maintain `prev`, `curr`, and `next` pointers to reverse next links in-place. |
| **876** | Middle of the Linked List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | [`daily-practice/lc-0876-middle-of-the-linked-list.py`](daily-practice/lc-0876-middle-of-the-linked-list.py)<br>[`daily-practice/lc-0876-middle-of-the-linked-list.md`](daily-practice/lc-0876-middle-of-the-linked-list.md) | Easy | Fast & Slow Pointers (2:1 Speed) | `slow` moves 1 step, `fast` moves 2 steps; when `fast` finishes, `slow` is at middle. |

---

### 6. Stacks & Queues

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py) | Easy | Stack | Push opening brackets; pop and match corresponding closing bracket. |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-0155-min-stack.py`](luffy/21-lc-0155-min-stack.py) | Medium | Auxiliary Stack / Pair Stack | Track running minimum alongside each pushed value in $O(1)$. |
| **227** | Basic Calculator II | [LC 227](https://leetcode.com/problems/basic-calculator-ii/) | [`luffy/22-lc-0227-basic-calculator-ii.py`](luffy/22-lc-0227-basic-calculator-ii.py) | Medium | Stack / Parsing | Evaluate `*` and `/` immediately on top of stack; sum all values for `+` and `-`. |
| **232** | Implement Queue using Stacks | [LC 232](https://leetcode.com/problems/implement-queue-using-stacks/) | [`luffy/24-lc-0232-implement-queue-using-stacks.py`](luffy/24-lc-0232-implement-queue-using-stacks.py) | Easy | Two Stacks (`in_stack`, `out_stack`) | Amortized $O(1)$ pop/peek by transferring elements only when `out_stack` is empty. |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-0394-decode-string.py`](luffy/23-lc-0394-decode-string.py) | Medium | Stack (Counts & Strings) | Push current string and multiplier onto stack when encountering `[`; pop on `]`. |

---

### 7. Trees & Binary Search Trees (BST)

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-0094-binary-tree-inorder-traversal.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py) | Easy | DFS (Left, Root, Right) | Traversal yields sorted order for BSTs; implemented recursively & iteratively. |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py) | Medium | BST Range Bounds / Inorder | Validate node with strictly bounded $(min\_val, max\_val)$ interval. |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-0102-binary-tree-level-order-traversal.py`](luffy/28-lc-0102-binary-tree-level-order-traversal.py) | Medium | BFS (Queue) | Level-by-level queue traversal using `len(queue)` snapshots. |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-0104-maximum-depth-of-binary-tree.py`](luffy/26-lc-0104-maximum-depth-of-binary-tree.py) | Easy | DFS / Divide & Conquer | `max_depth = 1 + max(left_depth, right_depth)`. |
| **105** | Construct Binary Tree from Preorder & Inorder | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py) | Medium | Divide & Conquer / Hash Map | Preorder gives root; Inorder splits left and right subtrees. |
| **144** | Binary Tree Preorder Traversal | [LC 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [`luffy/25-lc-0144-binary-tree-preorder-traversal.py`](luffy/25-lc-0144-binary-tree-preorder-traversal.py) | Easy | DFS (Root, Left, Right) | Root processed before recursive traversal of subtrees. |
| **145** | Binary Tree Postorder Traversal | [LC 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [`luffy/25-lc-0145-binary-tree-postorder-traversal.py`](luffy/25-lc-0145-binary-tree-postorder-traversal.py) | Easy | DFS (Left, Right, Root) | Subtrees processed before processing the root node. |
| **236** | Lowest Common Ancestor of Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py) | Medium | Postorder DFS | If both left and right return non-null, root is the LCA. |
| **Misc** | Advanced Tree Practices | — | [`luffy/25-tree-traversal-advanced-patterns.py`](luffy/25-tree-traversal-advanced-patterns.py) | Medium | Tree Patterns | Comprehensive tree construction and traversal utilities. |

---

### 8. Backtracking & Combinatorics

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-0039-combination-sum.py`](luffy/34-lc-0039-combination-sum.py) | Medium | Backtracking (Unbounded Choice) | Pass `start_index` to allow reuse of the current element without duplicate permutations. |
| **40** | Combination Sum II | [LC 40](https://leetcode.com/problems/combination-sum-ii/) | [`luffy/35-lc-0040-combination-sum-ii.py`](luffy/35-lc-0040-combination-sum-ii.py) | Medium | Backtracking + Deduplication | Sort candidates; skip duplicate elements at the same tree depth (`if i > start and nums[i] == nums[i-1]: continue`). |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-0046-permutations.py`](luffy/32-lc-0046-permutations.py) | Medium | Backtracking (Used Array) | Maintain `used` boolean array or swap elements in-place to explore all orderings. |
| **77** | Combinations | [LC 77](https://leetcode.com/problems/combinations/) | [`luffy/31-lc-0077-combinations.py`](luffy/31-lc-0077-combinations.py) | Medium | Backtracking + Pruning | Prune search branch if remaining candidates are insufficient to reach size $k$. |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-0078-subsets.py`](luffy/33-lc-0078-subsets.py) | Medium | Backtracking / Cascading | Append path copy at every recursion step; explore subsets of length $0 \dots n$. |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-0079-word-search.py`](luffy/37-lc-0079-word-search.py) | Medium | 2D Grid DFS + Backtracking | Mark visited cells in-place (e.g. `'#'`); restore character on backtracking. |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`luffy/36-lc-0131-palindrome-partitioning.py`](luffy/36-lc-0131-palindrome-partitioning.py) | Medium | Backtracking + Palindrome Check | Partition string at valid palindrome prefixes; recurse on remaining suffix. |

---

### 9. Graph Algorithms (DFS, BFS, Topological Sort)

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **130** | Surrounded Regions | [LC 130](https://leetcode.com/problems/surrounded-regions/) | [`luffy/39-lc-0130-surrounded-regions.py`](luffy/39-lc-0130-surrounded-regions.py) | Medium | Boundary Flood Fill (DFS/BFS) | Flood fill from outer border `'O'`s to protect them; flip remaining interior `'O'`s. |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-0200-number-of-islands.py`](luffy/38-lc-0200-number-of-islands.py) | Medium | Grid DFS / BFS (Sink Island) | Increment count upon finding `'1'`; recursively sink connected island to `'0'`. |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`luffy/42-lc-0207-course-schedule.py`](luffy/42-lc-0207-course-schedule.py) | Medium | Topological Sort (Kahn's / DFS) | Detect cycles in directed graph using in-degrees (Kahn's BFS) or 3-state DFS. |
| **994** | Rotting Oranges | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`luffy/40-lc-0994-rotting-oranges.py`](luffy/40-lc-0994-rotting-oranges.py) | Medium | Multi-source BFS | Enqueue all initially rotten oranges; propagate minute by minute to adjacent fresh ones. |
| **1091** | Shortest Path in Binary Matrix | [LC 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [`luffy/41-lc-1091-shortest-path-in-binary-matrix.py`](luffy/41-lc-1091-shortest-path-in-binary-matrix.py) | Medium | 8-Directional BFS | Find shortest path in unweighted grid; BFS guarantees minimum distance. |

---

### 10. Dynamic Programming & Math / Game Theory

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py) | Medium | Kadane's Algorithm / DP | `curr_max = max(num, curr_max + num)`; maintains maximum contiguous sum in $O(n)$. |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py) | Medium | Modulo Arithmetic / Game Theory | Count residues modulo 3 ($c_0, c_1, c_2$); analyze winning conditions based on $c_0 \pmod 2$. |

---

### 11. Object-Oriented Programming (OOP) & Foundations

| # | Topic / Concept | Reference File | Difficulty | Core Concept | Description |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **2235** | Add Two Integers | [`luffy/01-lc-2235-add-two-integers.py`](luffy/01-lc-2235-add-two-integers.py) | Easy | Basic Arithmetic | Python function syntax and return values. |
| **OOP** | Car Class & Inheritance | [`luffy/car-object-oriented-example.py`](luffy/car-object-oriented-example.py)<br>[`luffy/10-oop-pre-main-practice.py`](luffy/10-oop-pre-main-practice.py) | Easy | OOP Principles | Encapsulation, `__init__`, class methods, and object instantiation in Python. |

---

## Interactive Web Viewer & Study Station

This repository features an automated, standalone single-page application (`index.html`) designed for distraction-free local study:

* **Dual Split-Pane Layout**: Read detailed Markdown explanations on the left while simultaneously reviewing syntax-highlighted Python solutions on the right.
* **View Mode Controls**: Switch instantly between `[Split View]`, `[Notes Only]`, and `[Code Only]`.
* **Category Accordion**: Collapse / expand categories (`Top 100`, `Daily Practice`, `Luffy Curriculum`, `Topic Index`) or use `Expand All` / `Fold All`.
* **Difficulty & Pattern Filter Pills**: Filter by `Easy`, `Medium`, `Hard`, or specific algorithmic patterns.
* **Keyboard Shortcuts**: Press `/` to focus the search box, `Esc` to clear.

---

## How to Run & Practice

### 1. Launch the Interactive Study Station
Open `index.html` in your default browser:
```bash
python update_index.py --open
```

### 2. Auto-Rebuild on File Changes (Watch Mode)
```bash
python update_index.py --watch
```

### 3. Run Any Solution Locally
Execute any Python script directly with Python 3:
```bash
# Example: Run 3Sum solution
python3 top-100/lc-0015-3sum.py

# Example: Run Subarray Product Less Than K
python3 top-100/lc-0713-subarray-product-less-than-k.py
```
