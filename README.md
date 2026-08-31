# LeetCode Self-Practices & Algorithm Curriculum

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116.svg?logo=leetcode&logoColor=white)](https://leetcode.com/)
[![Problems Solved](https://img.shields.io/badge/Problems_Indexed-176+-brightgreen.svg)]()
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
| **Easy** | 8 | ~8% | 8 |
| **Medium** | 87 | ~91% | 167 |
| **Hard** | 1 | ~1% | 1 |
| **Total** | **96 In-Depth Notes** | **100%** | **176 Problem Entities** |

---

## Repository Structure

```tree
leetcode-sh/
├── top-100/                      # LeetCode Top 100 Liked Problems & In-Depth Notes
│   ├── lc-0003-longest-substring-without-repeating-characters.py / .md
│   ├── lc-0011-container-with-most-water.py / .md
│   ├── lc-0015-3sum.py / .md
│   ├── lc-0016-3-sum-closest.py / .md
│   ├── lc-0017-letter-combinations-of-a-phone-number.py / .md
│   ├── lc-0019-remove-nth-node-from-end-of-list.py / .md
│   ├── lc-0033-search-in-rotated-sorted-array.py / .md
│   ├── lc-0034-find-first-and-last-position-of-element-in-sorted-array.py / .md
│   ├── lc-0042-trapping-rain-water.py / .md
│   ├── lc-0053-maximum-subarray.py / .md
│   ├── lc-0078-subsets.py / .md
│   ├── lc-0101-symmetric-tree.py / .md
│   ├── lc-0102-binary-tree-level-order-traversal.py / .md
│   ├── lc-0104-maximum-depth-of-binary-tree.py / .md
│   ├── lc-0141-linked-list-cycle.py / .md
│   ├── lc-0142-linked-list-cycle-ii.py / .md
│   ├── lc-0162-find-peak-element.py / .md
│   ├── lc-0167-two-sum-ii-input-array-is-sorted.py / .md
│   ├── lc-0206-reverse-linked-list.py / .md
│   ├── lc-0209-minimum-size-subarray-sum.py / .md
│   ├── lc-0236-lowest-common-ancestor-of-a-binary-tree.py / .md
│   └── lc-0713-subarray-product-less-than-k.py / .md
├── daily-practice/               # Daily LeetCode Practices & Weekly Contest Challenges
│   ├── lc-0025-reverse-nodes-in-k-group.py / .md
│   ├── lc-0077-combinations.py / .md
│   ├── lc-0082-remove-duplicates-from-sorted-list.py / .md
│   ├── lc-0083-remove-duplicates-from-sorted-list.py / .md
│   ├── lc-0092-reversed-linked-list-2.py / .md
│   ├── lc-0100-same-tree.py / .md
│   ├── lc-0103-binary-tree-zigzag-level-order-traversal.py / .md
│   ├── lc-0110-balanced-binary-tree.py / .md
│   ├── lc-0131-palindrome-partitioning.py / .md
│   ├── lc-0143-reorder-list.py / .md
│   ├── lc-0153-find-minimum-in-rotated-sorted-array.py / .md
│   ├── lc-0199-binary-tree-right-side-view.py / .md
│   ├── lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py / .md
│   ├── lc-0237-delete-node-in-a-linked-list.py / .md
│   ├── lc-0513-find-bottom-left-tree-value.py / .md
│   ├── lc-0876-middle-of-the-linked-list.py / .md
│   ├── lc-2029-stone-game-ix.py / .md
│   ├── lc-3090-maximum-length-substring-with-at-most-two-occurrences.py / .md
│   └── lc-3471-find-the-largest-almost-missing-integer.py / .md
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
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py)<br>[`top-100/lc-0001-two-sum.py`](top-100/lc-0001-two-sum.py)<br>[`luffy/02-lc-0001-two-sum.md`](luffy/02-lc-0001-two-sum.md) | Easy | Hash Map |
| **2** | Add Two Numbers | [LC 2](https://leetcode.com/problems/add-two-numbers/) | [`top-100/lc-0002-add-two-numbers.py`](top-100/lc-0002-add-two-numbers.py) | Medium | High-Frequency Top 100 Pattern |
| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`luffy/04-lc-0003-longest-substring-without-repeating-characters.py`](luffy/04-lc-0003-longest-substring-without-repeating-characters.py)<br>[`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py)<br>[`luffy/04-lc-0003-longest-substring-without-repeating-characters.md`](luffy/04-lc-0003-longest-substring-without-repeating-characters.md)<br>[`top-100/lc-0003-longest-substring-without-repeating-characters.md`](top-100/lc-0003-longest-substring-without-repeating-characters.md) | Medium | Sliding Window |
| **4** | Median Of Two Sorted Arrays | [LC 4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [`top-100/lc-0004-median-of-two-sorted-arrays.py`](top-100/lc-0004-median-of-two-sorted-arrays.py) | Hard | High-Frequency Top 100 Pattern |
| **5** | Longest Palindromic Substring | [LC 5](https://leetcode.com/problems/longest-palindromic-substring/) | [`top-100/lc-0005-longest-palindromic-substring.py`](top-100/lc-0005-longest-palindromic-substring.py) | Medium | High-Frequency Top 100 Pattern |
| **10** | Regular Expression Matching | [LC 10](https://leetcode.com/problems/regular-expression-matching/) | [`top-100/lc-0010-regular-expression-matching.py`](top-100/lc-0010-regular-expression-matching.py) | Hard | High-Frequency Top 100 Pattern |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py)<br>[`top-100/lc-0011-container-with-most-water.md`](top-100/lc-0011-container-with-most-water.md) | Medium | Two Pointers (Left/Right) |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/lc-0015-3sum.py`](top-100/lc-0015-3sum.py)<br>[`top-100/lc-0015-3sum.md`](top-100/lc-0015-3sum.md) | Medium | Two Pointers / Extreme Pruning |
| **16** | 3Sum Closest | [LC 16](https://leetcode.com/problems/3-sum-closest/) | [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)<br>[`top-100/lc-0016-3-sum-closest.md`](top-100/lc-0016-3-sum-closest.md) | Medium | Two Pointers / 2-Way Bound Pruning |
| **17** | Letter Combinations of a Phone Number | [LC 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [`top-100/lc-0017-letter-combinations-of-a-phone-number.py`](top-100/lc-0017-letter-combinations-of-a-phone-number.py)<br>[`top-100/lc-0017-letter-combinations-of-a-phone-number.md`](top-100/lc-0017-letter-combinations-of-a-phone-number.md) | Medium | Backtracking (Cartesian Product) |
| **19** | Remove Nth Node From End of List | [LC 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [`top-100/lc-0019-remove-nth-node-from-end-of-list.py`](top-100/lc-0019-remove-nth-node-from-end-of-list.py)<br>[`top-100/lc-0019-remove-nth-node-from-end-of-list.md`](top-100/lc-0019-remove-nth-node-from-end-of-list.md) | Medium | Dummy + Fixed-Gap Two Pointers |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)<br>[`luffy/20-lc-0020-valid-parentheses-dict.py`](luffy/20-lc-0020-valid-parentheses-dict.py)<br>[`top-100/lc-0020-valid-parentheses.py`](top-100/lc-0020-valid-parentheses.py)<br>[`luffy/19-lc-0020-valid-parentheses.md`](luffy/19-lc-0020-valid-parentheses.md)<br>[`luffy/20-lc-0020-valid-parentheses-dict.md`](luffy/20-lc-0020-valid-parentheses-dict.md) | Easy | Stack |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-0021-merge-two-sorted-lists.py`](luffy/16-lc-0021-merge-two-sorted-lists.py)<br>[`top-100/lc-0021-merge-two-sorted-lists.py`](top-100/lc-0021-merge-two-sorted-lists.py)<br>[`luffy/16-lc-0021-merge-two-sorted-lists.md`](luffy/16-lc-0021-merge-two-sorted-lists.md) | Easy | Dummy Head + Two Pointers |
| **22** | Generate Parentheses | [LC 22](https://leetcode.com/problems/generate-parentheses/) | [`top-100/lc-0022-generate-parentheses.py`](top-100/lc-0022-generate-parentheses.py)<br>[`top-100/lc-0022-generate-parentheses.md`](top-100/lc-0022-generate-parentheses.md) | Medium | Backtracking / Prefix Balance |
| **23** | Merge K Sorted Lists | [LC 23](https://leetcode.com/problems/merge-k-sorted-lists/) | [`top-100/lc-0023-merge-k-sorted-lists.py`](top-100/lc-0023-merge-k-sorted-lists.py) | Hard | High-Frequency Top 100 Pattern |
| **31** | Next Permutation | [LC 31](https://leetcode.com/problems/next-permutation/) | [`top-100/lc-0031-next-permutation.py`](top-100/lc-0031-next-permutation.py) | Medium | High-Frequency Top 100 Pattern |
| **32** | Longest Valid Parentheses | [LC 32](https://leetcode.com/problems/longest-valid-parentheses/) | [`top-100/lc-0032-longest-valid-parentheses.py`](top-100/lc-0032-longest-valid-parentheses.py) | Hard | High-Frequency Top 100 Pattern |
| **33** | Search in Rotated Sorted Array | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)<br>[`top-100/lc-0033-search-in-rotated-sorted-array.md`](top-100/lc-0033-search-in-rotated-sorted-array.md) | Medium | Binary Search on Rotated Array (`nums[-1]`) |
| **34** | Find First and Last Position of Element in Sorted Array | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)<br>[`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md) | Medium | Binary Search (`lower_bound`) |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-0039-combination-sum.py`](luffy/34-lc-0039-combination-sum.py)<br>[`top-100/lc-0039-combination-sum.py`](top-100/lc-0039-combination-sum.py)<br>[`luffy/34-lc-0039-combination-sum.md`](luffy/34-lc-0039-combination-sum.md) | Medium | Backtracking (Unbounded Choice) |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py)<br>[`top-100/lc-0042-trapping-rain-water.md`](top-100/lc-0042-trapping-rain-water.md) | Hard | Two Pointers / Pre-Suf Max |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-0046-permutations.py`](luffy/32-lc-0046-permutations.py)<br>[`top-100/lc-0046-permutations.py`](top-100/lc-0046-permutations.py)<br>[`luffy/32-lc-0046-permutations.md`](luffy/32-lc-0046-permutations.md) | Medium | Backtracking (Used Array) |
| **48** | Rotate Image | [LC 48](https://leetcode.com/problems/rotate-image/) | [`top-100/lc-0048-rotate-image.py`](top-100/lc-0048-rotate-image.py) | Medium | High-Frequency Top 100 Pattern |
| **49** | Group Anagrams | [LC 49](https://leetcode.com/problems/group-anagrams/) | [`top-100/lc-0049-group-anagrams.py`](top-100/lc-0049-group-anagrams.py) | Medium | High-Frequency Top 100 Pattern |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py)<br>[`top-100/lc-0053-maximum-subarray.md`](top-100/lc-0053-maximum-subarray.md) | Medium | Kadane's Algorithm / DP |
| **55** | Jump Game | [LC 55](https://leetcode.com/problems/jump-game/) | [`top-100/lc-0055-jump-game.py`](top-100/lc-0055-jump-game.py) | Medium | High-Frequency Top 100 Pattern |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-0056-merge-intervals.py`](luffy/13-lc-0056-merge-intervals.py)<br>[`top-100/lc-0056-merge-intervals.py`](top-100/lc-0056-merge-intervals.py)<br>[`luffy/13-lc-0056-merge-intervals.md`](luffy/13-lc-0056-merge-intervals.md) | Medium | Interval Sorting |
| **62** | Unique Paths | [LC 62](https://leetcode.com/problems/unique-paths/) | [`top-100/lc-0062-unique-paths.py`](top-100/lc-0062-unique-paths.py) | Medium | High-Frequency Top 100 Pattern |
| **64** | Minimum Path Sum | [LC 64](https://leetcode.com/problems/minimum-path-sum/) | [`top-100/lc-0064-minimum-path-sum.py`](top-100/lc-0064-minimum-path-sum.py) | Medium | High-Frequency Top 100 Pattern |
| **70** | Climbing Stairs | [LC 70](https://leetcode.com/problems/climbing-stairs/) | [`top-100/lc-0070-climbing-stairs.py`](top-100/lc-0070-climbing-stairs.py) | Easy | High-Frequency Top 100 Pattern |
| **72** | Edit Distance | [LC 72](https://leetcode.com/problems/edit-distance/) | [`top-100/lc-0072-edit-distance.py`](top-100/lc-0072-edit-distance.py) | Hard | High-Frequency Top 100 Pattern |
| **75** | Sort Colors | [LC 75](https://leetcode.com/problems/sort-colors/) | [`top-100/lc-0075-sort-colors.py`](top-100/lc-0075-sort-colors.py) | Medium | High-Frequency Top 100 Pattern |
| **76** | Minimum Window Substring | [LC 76](https://leetcode.com/problems/minimum-window-substring/) | [`top-100/lc-0076-minimum-window-substring.py`](top-100/lc-0076-minimum-window-substring.py) | Hard | High-Frequency Top 100 Pattern |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-0078-subsets.py`](luffy/33-lc-0078-subsets.py)<br>[`top-100/lc-0078-subsets.py`](top-100/lc-0078-subsets.py)<br>[`luffy/33-lc-0078-subsets.md`](luffy/33-lc-0078-subsets.md)<br>[`top-100/lc-0078-subsets.md`](top-100/lc-0078-subsets.md) | Medium | Backtracking (0-1 Pick vs Multi-way Loop) |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-0079-word-search.py`](luffy/37-lc-0079-word-search.py)<br>[`top-100/lc-0079-word-search.py`](top-100/lc-0079-word-search.py)<br>[`luffy/37-lc-0079-word-search.md`](luffy/37-lc-0079-word-search.md) | Medium | 2D Grid DFS + Backtracking |
| **84** | Largest Rectangle In Histogram | [LC 84](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [`top-100/lc-0084-largest-rectangle-in-histogram.py`](top-100/lc-0084-largest-rectangle-in-histogram.py) | Hard | High-Frequency Top 100 Pattern |
| **85** | Maximal Rectangle | [LC 85](https://leetcode.com/problems/maximal-rectangle/) | [`top-100/lc-0085-maximal-rectangle.py`](top-100/lc-0085-maximal-rectangle.py) | Hard | High-Frequency Top 100 Pattern |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-0094-binary-tree-inorder-traversal.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py)<br>[`luffy/25-tree-traversal-advanced-patterns.py`](luffy/25-tree-traversal-advanced-patterns.py)<br>[`top-100/lc-0094-binary-tree-inorder-traversal.py`](top-100/lc-0094-binary-tree-inorder-traversal.py)<br>[`luffy/25-lc-0094-binary-tree-inorder-traversal.md`](luffy/25-lc-0094-binary-tree-inorder-traversal.md)<br>[`luffy/25-tree-traversal-advanced-patterns.md`](luffy/25-tree-traversal-advanced-patterns.md) | Easy | DFS (Left, Root, Right) |
| **96** | Unique Binary Search Trees | [LC 96](https://leetcode.com/problems/unique-binary-search-trees/) | [`top-100/lc-0096-unique-binary-search-trees.py`](top-100/lc-0096-unique-binary-search-trees.py) | Medium | High-Frequency Top 100 Pattern |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-bounds.py`](luffy/29-lc-0098-validate-binary-search-tree-bounds.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.py`](luffy/29-lc-0098-validate-binary-search-tree-recursion.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.py`](luffy/29-lc-0098-validate-binary-search-tree-stack.py)<br>[`top-100/lc-0098-validate-binary-search-tree.py`](top-100/lc-0098-validate-binary-search-tree.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-bounds.md`](luffy/29-lc-0098-validate-binary-search-tree-bounds.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-inorder.md`](luffy/29-lc-0098-validate-binary-search-tree-inorder.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.md`](luffy/29-lc-0098-validate-binary-search-tree-recursion.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.md`](luffy/29-lc-0098-validate-binary-search-tree-stack.md) | Medium | BST Range Bounds / Inorder |
| **101** | Symmetric Tree | [LC 101](https://leetcode.com/problems/symmetric-tree/) | [`top-100/lc-0101-symmetric-tree.py`](top-100/lc-0101-symmetric-tree.py)<br>[`top-100/lc-0101-symmetric-tree.md`](top-100/lc-0101-symmetric-tree.md) | Easy | Dual-Subtree Mirror Recursion |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-0102-binary-tree-level-order-traversal.py`](luffy/28-lc-0102-binary-tree-level-order-traversal.py)<br>[`top-100/lc-0102-binary-tree-level-order-traversal.py`](top-100/lc-0102-binary-tree-level-order-traversal.py)<br>[`luffy/28-lc-0102-binary-tree-level-order-traversal.md`](luffy/28-lc-0102-binary-tree-level-order-traversal.md)<br>[`top-100/lc-0102-binary-tree-level-order-traversal.md`](top-100/lc-0102-binary-tree-level-order-traversal.md) | Medium | Dual-Buffer BFS / Level Snapshot |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-0104-maximum-depth-of-binary-tree.py`](luffy/26-lc-0104-maximum-depth-of-binary-tree.py)<br>[`top-100/lc-0104-maximum-depth-of-binary-tree.py`](top-100/lc-0104-maximum-depth-of-binary-tree.py)<br>[`luffy/26-lc-0104-maximum-depth-of-binary-tree.md`](luffy/26-lc-0104-maximum-depth-of-binary-tree.md)<br>[`top-100/lc-0104-maximum-depth-of-binary-tree.md`](top-100/lc-0104-maximum-depth-of-binary-tree.md) | Easy | Post-order Divide & Conquer |
| **105** | Construct Binary Tree from Preorder & Inorder | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)<br>[`top-100/lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](top-100/lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)<br>[`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) | Medium | Divide & Conquer / Hash Map |
| **114** | Flatten Binary Tree To Linked List | [LC 114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | [`top-100/lc-0114-flatten-binary-tree-to-linked-list.py`](top-100/lc-0114-flatten-binary-tree-to-linked-list.py) | Medium | High-Frequency Top 100 Pattern |
| **121** | Best Time To Buy And Sell Stock | [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [`top-100/lc-0121-best-time-to-buy-and-sell-stock.py`](top-100/lc-0121-best-time-to-buy-and-sell-stock.py) | Easy | High-Frequency Top 100 Pattern |
| **124** | Binary Tree Maximum Path Sum | [LC 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [`top-100/lc-0124-binary-tree-maximum-path-sum.py`](top-100/lc-0124-binary-tree-maximum-path-sum.py) | Hard | High-Frequency Top 100 Pattern |
| **128** | Longest Consecutive Sequence | [LC 128](https://leetcode.com/problems/longest-consecutive-sequence/) | [`top-100/lc-0128-longest-consecutive-sequence.py`](top-100/lc-0128-longest-consecutive-sequence.py) | Medium | High-Frequency Top 100 Pattern |
| **136** | Single Number | [LC 136](https://leetcode.com/problems/single-number/) | [`top-100/lc-0136-single-number.py`](top-100/lc-0136-single-number.py) | Easy | High-Frequency Top 100 Pattern |
| **139** | Word Break | [LC 139](https://leetcode.com/problems/word-break/) | [`top-100/lc-0139-word-break.py`](top-100/lc-0139-word-break.py) | Medium | High-Frequency Top 100 Pattern |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`luffy/17-lc-0141-linked-list-cycle.py`](luffy/17-lc-0141-linked-list-cycle.py)<br>[`top-100/lc-0141-linked-list-cycle.py`](top-100/lc-0141-linked-list-cycle.py)<br>[`luffy/17-lc-0141-linked-list-cycle.md`](luffy/17-lc-0141-linked-list-cycle.md)<br>[`top-100/lc-0141-linked-list-cycle.md`](top-100/lc-0141-linked-list-cycle.md) | Easy | Floyd's Fast & Slow Pointers |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`luffy/18-lc-0142-linked-list-cycle-ii.py`](luffy/18-lc-0142-linked-list-cycle-ii.py)<br>[`top-100/lc-0142-linked-list-cycle-ii.py`](top-100/lc-0142-linked-list-cycle-ii.py)<br>[`luffy/18-lc-0142-linked-list-cycle-ii.md`](luffy/18-lc-0142-linked-list-cycle-ii.md)<br>[`top-100/lc-0142-linked-list-cycle-ii.md`](top-100/lc-0142-linked-list-cycle-ii.md) | Medium | Floyd's Algorithm + Math |
| **146** | Lru Cache | [LC 146](https://leetcode.com/problems/lru-cache/) | [`top-100/lc-0146-lru-cache.py`](top-100/lc-0146-lru-cache.py) | Medium | High-Frequency Top 100 Pattern |
| **148** | Sort List | [LC 148](https://leetcode.com/problems/sort-list/) | [`top-100/lc-0148-sort-list.py`](top-100/lc-0148-sort-list.py) | Medium | High-Frequency Top 100 Pattern |
| **152** | Maximum Product Subarray | [LC 152](https://leetcode.com/problems/maximum-product-subarray/) | [`top-100/lc-0152-maximum-product-subarray.py`](top-100/lc-0152-maximum-product-subarray.py) | Medium | High-Frequency Top 100 Pattern |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-0155-min-stack.py`](luffy/21-lc-0155-min-stack.py)<br>[`top-100/lc-0155-min-stack.py`](top-100/lc-0155-min-stack.py)<br>[`luffy/21-lc-0155-min-stack.md`](luffy/21-lc-0155-min-stack.md) | Medium | Auxiliary Stack / Pair Stack |
| **160** | Intersection Of Two Linked Lists | [LC 160](https://leetcode.com/problems/intersection-of-two-linked-lists/) | [`top-100/lc-0160-intersection-of-two-linked-lists.py`](top-100/lc-0160-intersection-of-two-linked-lists.py) | Easy | High-Frequency Top 100 Pattern |
| **162** | Find Peak Element | [LC 162](https://leetcode.com/problems/find-peak-element/) | [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)<br>[`top-100/lc-0162-find-peak-element.md`](top-100/lc-0162-find-peak-element.md) | Medium | Binary Search (Slope Peak / Open Interval) |
| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.md`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.md)<br>[`top-100/lc-0167-two-sum-ii-input-array-is-sorted.md`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.md) | Medium | Two Pointers (Inward) |
| **169** | Majority Element | [LC 169](https://leetcode.com/problems/majority-element/) | [`top-100/lc-0169-majority-element.py`](top-100/lc-0169-majority-element.py) | Easy | High-Frequency Top 100 Pattern |
| **198** | House Robber | [LC 198](https://leetcode.com/problems/house-robber/) | [`top-100/lc-0198-house-robber.py`](top-100/lc-0198-house-robber.py) | Medium | High-Frequency Top 100 Pattern |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-0200-number-of-islands.py`](luffy/38-lc-0200-number-of-islands.py)<br>[`top-100/lc-0200-number-of-islands.py`](top-100/lc-0200-number-of-islands.py)<br>[`luffy/38-lc-0200-number-of-islands.md`](luffy/38-lc-0200-number-of-islands.md) | Medium | Grid DFS / BFS (Sink Island) |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-0206-reverse-linked-list.py`](luffy/15-lc-0206-reverse-linked-list.py)<br>[`top-100/lc-0206-reverse-linked-list.py`](top-100/lc-0206-reverse-linked-list.py)<br>[`luffy/15-lc-0206-reverse-linked-list.md`](luffy/15-lc-0206-reverse-linked-list.md)<br>[`top-100/lc-0206-reverse-linked-list.md`](top-100/lc-0206-reverse-linked-list.md) | Easy | Iterative Pointer Reversal |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`luffy/42-lc-0207-course-schedule.py`](luffy/42-lc-0207-course-schedule.py)<br>[`top-100/lc-0207-course-schedule.py`](top-100/lc-0207-course-schedule.py)<br>[`luffy/42-lc-0207-course-schedule.md`](luffy/42-lc-0207-course-schedule.md) | Medium | Topological Sort (Kahn's / DFS) |
| **208** | Implement Trie Prefix Tree | [LC 208](https://leetcode.com/problems/implement-trie-prefix-tree/) | [`top-100/lc-0208-implement-trie-prefix-tree.py`](top-100/lc-0208-implement-trie-prefix-tree.py) | Medium | High-Frequency Top 100 Pattern |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`luffy/06-lc-0209-minimum-size-subarray-sum.py`](luffy/06-lc-0209-minimum-size-subarray-sum.py)<br>[`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)<br>[`luffy/06-lc-0209-minimum-size-subarray-sum.md`](luffy/06-lc-0209-minimum-size-subarray-sum.md)<br>[`top-100/lc-0209-minimum-size-subarray-sum.md`](top-100/lc-0209-minimum-size-subarray-sum.md) | Medium | Sliding Window |
| **215** | Kth Largest Element In An Array | [LC 215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [`top-100/lc-0215-kth-largest-element-in-an-array.py`](top-100/lc-0215-kth-largest-element-in-an-array.py) | Medium | High-Frequency Top 100 Pattern |
| **221** | Maximal Square | [LC 221](https://leetcode.com/problems/maximal-square/) | [`top-100/lc-0221-maximal-square.py`](top-100/lc-0221-maximal-square.py) | Medium | High-Frequency Top 100 Pattern |
| **226** | Invert Binary Tree | [LC 226](https://leetcode.com/problems/invert-binary-tree/) | [`top-100/lc-0226-invert-binary-tree.py`](top-100/lc-0226-invert-binary-tree.py) | Easy | High-Frequency Top 100 Pattern |
| **234** | Palindrome Linked List | [LC 234](https://leetcode.com/problems/palindrome-linked-list/) | [`top-100/lc-0234-palindrome-linked-list.py`](top-100/lc-0234-palindrome-linked-list.py) | Easy | High-Frequency Top 100 Pattern |
| **236** | Lowest Common Ancestor of Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py)<br>[`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py)<br>[`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md)<br>[`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.md`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.md) | Medium | Postorder Divide & Conquer (4-State Aggregation) |
| **238** | Product Of Array Except Self | [LC 238](https://leetcode.com/problems/product-of-array-except-self/) | [`top-100/lc-0238-product-of-array-except-self.py`](top-100/lc-0238-product-of-array-except-self.py) | Medium | High-Frequency Top 100 Pattern |
| **239** | Sliding Window Maximum | [LC 239](https://leetcode.com/problems/sliding-window-maximum/) | [`top-100/lc-0239-sliding-window-maximum.py`](top-100/lc-0239-sliding-window-maximum.py) | Hard | High-Frequency Top 100 Pattern |
| **240** | Search A 2D Matrix Ii | [LC 240](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [`top-100/lc-0240-search-a-2d-matrix-ii.py`](top-100/lc-0240-search-a-2d-matrix-ii.py) | Medium | High-Frequency Top 100 Pattern |
| **279** | Perfect Squares | [LC 279](https://leetcode.com/problems/perfect-squares/) | [`top-100/lc-0279-perfect-squares.py`](top-100/lc-0279-perfect-squares.py) | Medium | High-Frequency Top 100 Pattern |
| **283** | Move Zeroes | [LC 283](https://leetcode.com/problems/move-zeroes/) | [`top-100/lc-0283-move-zeroes.py`](top-100/lc-0283-move-zeroes.py) | Easy | High-Frequency Top 100 Pattern |
| **287** | Find The Duplicate Number | [LC 287](https://leetcode.com/problems/find-the-duplicate-number/) | [`top-100/lc-0287-find-the-duplicate-number.py`](top-100/lc-0287-find-the-duplicate-number.py) | Medium | High-Frequency Top 100 Pattern |
| **297** | Serialize And Deserialize Binary Tree | [LC 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | [`top-100/lc-0297-serialize-and-deserialize-binary-tree.py`](top-100/lc-0297-serialize-and-deserialize-binary-tree.py) | Hard | High-Frequency Top 100 Pattern |
| **300** | Longest Increasing Subsequence | [LC 300](https://leetcode.com/problems/longest-increasing-subsequence/) | [`top-100/lc-0300-longest-increasing-subsequence.py`](top-100/lc-0300-longest-increasing-subsequence.py) | Medium | High-Frequency Top 100 Pattern |
| **301** | Remove Invalid Parentheses | [LC 301](https://leetcode.com/problems/remove-invalid-parentheses/) | [`top-100/lc-0301-remove-invalid-parentheses.py`](top-100/lc-0301-remove-invalid-parentheses.py) | Hard | High-Frequency Top 100 Pattern |
| **309** | Best Time To Buy And Sell Stock With Cooldown | [LC 309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [`top-100/lc-0309-best-time-to-buy-and-sell-stock-with-cooldown.py`](top-100/lc-0309-best-time-to-buy-and-sell-stock-with-cooldown.py) | Medium | High-Frequency Top 100 Pattern |
| **312** | Burst Balloons | [LC 312](https://leetcode.com/problems/burst-balloons/) | [`top-100/lc-0312-burst-balloons.py`](top-100/lc-0312-burst-balloons.py) | Hard | High-Frequency Top 100 Pattern |
| **322** | Coin Change | [LC 322](https://leetcode.com/problems/coin-change/) | [`top-100/lc-0322-coin-change.py`](top-100/lc-0322-coin-change.py) | Medium | High-Frequency Top 100 Pattern |
| **337** | House Robber Iii | [LC 337](https://leetcode.com/problems/house-robber-iii/) | [`top-100/lc-0337-house-robber-iii.py`](top-100/lc-0337-house-robber-iii.py) | Medium | High-Frequency Top 100 Pattern |
| **338** | Counting Bits | [LC 338](https://leetcode.com/problems/counting-bits/) | [`top-100/lc-0338-counting-bits.py`](top-100/lc-0338-counting-bits.py) | Easy | High-Frequency Top 100 Pattern |
| **347** | Top K Frequent Elements | [LC 347](https://leetcode.com/problems/top-k-frequent-elements/) | [`top-100/lc-0347-top-k-frequent-elements.py`](top-100/lc-0347-top-k-frequent-elements.py) | Medium | High-Frequency Top 100 Pattern |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-0394-decode-string.py`](luffy/23-lc-0394-decode-string.py)<br>[`top-100/lc-0394-decode-string.py`](top-100/lc-0394-decode-string.py)<br>[`luffy/23-lc-0394-decode-string.md`](luffy/23-lc-0394-decode-string.md) | Medium | Stack (Counts & Strings) |
| **399** | Evaluate Division | [LC 399](https://leetcode.com/problems/evaluate-division/) | [`top-100/lc-0399-evaluate-division.py`](top-100/lc-0399-evaluate-division.py) | Medium | High-Frequency Top 100 Pattern |
| **406** | Queue Reconstruction By Height | [LC 406](https://leetcode.com/problems/queue-reconstruction-by-height/) | [`top-100/lc-0406-queue-reconstruction-by-height.py`](top-100/lc-0406-queue-reconstruction-by-height.py) | Medium | High-Frequency Top 100 Pattern |
| **416** | Partition Equal Subset Sum | [LC 416](https://leetcode.com/problems/partition-equal-subset-sum/) | [`top-100/lc-0416-partition-equal-subset-sum.py`](top-100/lc-0416-partition-equal-subset-sum.py) | Medium | High-Frequency Top 100 Pattern |
| **437** | Path Sum Iii | [LC 437](https://leetcode.com/problems/path-sum-iii/) | [`top-100/lc-0437-path-sum-iii.py`](top-100/lc-0437-path-sum-iii.py) | Medium | High-Frequency Top 100 Pattern |
| **438** | Find All Anagrams In A String | [LC 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | [`top-100/lc-0438-find-all-anagrams-in-a-string.py`](top-100/lc-0438-find-all-anagrams-in-a-string.py) | Medium | High-Frequency Top 100 Pattern |
| **448** | Find All Numbers Disappeared In An Array | [LC 448](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | [`top-100/lc-0448-find-all-numbers-disappeared-in-an-array.py`](top-100/lc-0448-find-all-numbers-disappeared-in-an-array.py) | Easy | High-Frequency Top 100 Pattern |
| **494** | Target Sum | [LC 494](https://leetcode.com/problems/target-sum/) | [`top-100/lc-0494-target-sum.py`](top-100/lc-0494-target-sum.py) | Medium | High-Frequency Top 100 Pattern |
| **538** | Convert Bst To Greater Tree | [LC 538](https://leetcode.com/problems/convert-bst-to-greater-tree/) | [`top-100/lc-0538-convert-bst-to-greater-tree.py`](top-100/lc-0538-convert-bst-to-greater-tree.py) | Medium | High-Frequency Top 100 Pattern |
| **543** | Diameter Of Binary Tree | [LC 543](https://leetcode.com/problems/diameter-of-binary-tree/) | [`top-100/lc-0543-diameter-of-binary-tree.py`](top-100/lc-0543-diameter-of-binary-tree.py) | Easy | High-Frequency Top 100 Pattern |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-0560-subarray-sum-equals-k.py`](luffy/11-lc-0560-subarray-sum-equals-k.py)<br>[`top-100/lc-0560-subarray-sum-equals-k.py`](top-100/lc-0560-subarray-sum-equals-k.py)<br>[`luffy/11-lc-0560-subarray-sum-equals-k.md`](luffy/11-lc-0560-subarray-sum-equals-k.md) | Medium | Prefix Sum + Hash Map |
| **581** | Shortest Unsorted Continuous Subarray | [LC 581](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | [`top-100/lc-0581-shortest-unsorted-continuous-subarray.py`](top-100/lc-0581-shortest-unsorted-continuous-subarray.py) | Medium | High-Frequency Top 100 Pattern |
| **617** | Merge Two Binary Trees | [LC 617](https://leetcode.com/problems/merge-two-binary-trees/) | [`top-100/lc-0617-merge-two-binary-trees.py`](top-100/lc-0617-merge-two-binary-trees.py) | Easy | High-Frequency Top 100 Pattern |
| **621** | Task Scheduler | [LC 621](https://leetcode.com/problems/task-scheduler/) | [`top-100/lc-0621-task-scheduler.py`](top-100/lc-0621-task-scheduler.py) | Medium | High-Frequency Top 100 Pattern |
| **647** | Palindromic Substrings | [LC 647](https://leetcode.com/problems/palindromic-substrings/) | [`top-100/lc-0647-palindromic-substrings.py`](top-100/lc-0647-palindromic-substrings.py) | Medium | High-Frequency Top 100 Pattern |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py)<br>[`top-100/lc-0713-subarray-product-less-than-k.md`](top-100/lc-0713-subarray-product-less-than-k.md) | Medium | Sliding Window / Product Counting |
| **739** | Daily Temperatures | [LC 739](https://leetcode.com/problems/daily-temperatures/) | [`top-100/lc-0739-daily-temperatures.py`](top-100/lc-0739-daily-temperatures.py) | Medium | High-Frequency Top 100 Pattern |

---

## Daily Practice Track

Tracking daily challenge questions, weekly contest problems, and algorithmic practice.

| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |
| :-: | :--- | :-: | :--- | :-: | :--- |
| **25** | Reverse Nodes in k-Group | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [`daily-practice/lc-0025-reverse-nodes-in-k-group.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py)<br>[`daily-practice/lc-0025-reverse-nodes-in-k-group.md`](daily-practice/lc-0025-reverse-nodes-in-k-group.md) | Hard | Sentinel Dummy + k-Group Reversal (`p0`, `pre`, `cur`) |
| **77** | Combinations | [LC 77](https://leetcode.com/problems/combinations/) | [`daily-practice/lc-0077-combinations.py`](daily-practice/lc-0077-combinations.py)<br>[`luffy/31-lc-0077-combinations.py`](luffy/31-lc-0077-combinations.py)<br>[`daily-practice/lc-0077-combinations.md`](daily-practice/lc-0077-combinations.md)<br>[`luffy/31-lc-0077-combinations.md`](luffy/31-lc-0077-combinations.md) | Medium | Backtracking + Remaining Count Bound Pruning (`j >= d`) |
| **82** | Remove Duplicates from Sorted List II | [LC 82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | [`daily-practice/lc-0082-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.py)<br>[`daily-practice/lc-0082-remove-duplicates-from-sorted-list.md`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.md) | Medium | Dummy Sentinel + 2-Step Lookahead Segment Erasure |
| **83** | Remove Duplicates from Sorted List | [LC 83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [`daily-practice/lc-0083-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.py)<br>[`daily-practice/lc-0083-remove-duplicates-from-sorted-list.md`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.md) | Easy | In-Place Adjacent Deduplication (`cur.next = cur.next.next`) |
| **92** | Reverse Linked List II | [LC 92](https://leetcode.com/problems/reverse-linked-list-ii/) | [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)<br>[`daily-practice/lc-0092-reversed-linked-list-2.md`](daily-practice/lc-0092-reversed-linked-list-2.md) | Medium | Dummy Node + Local Segment Reversal (`p0`, `pre`, `cur`) |
| **100** | Same Tree | [LC 100](https://leetcode.com/problems/same-tree/) | [`daily-practice/lc-0100-same-tree.py`](daily-practice/lc-0100-same-tree.py)<br>[`daily-practice/lc-0100-same-tree.md`](daily-practice/lc-0100-same-tree.md) | Easy | Dual Tree Synchronous Recursion (`p is q`, `p.val == q.val`, `left`, `right`) |
| **103** | Binary Tree Zigzag Level Order Traversal | [LC 103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py)<br>[`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.md`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.md) | Medium | Dual-Buffer BFS + Parity Toggle / Level Reversal |
| **110** | Balanced Binary Tree | [LC 110](https://leetcode.com/problems/balanced-binary-tree/) | [`daily-practice/lc-0110-balanced-binary-tree.py`](daily-practice/lc-0110-balanced-binary-tree.py)<br>[`daily-practice/lc-0110-balanced-binary-tree.md`](daily-practice/lc-0110-balanced-binary-tree.md) | Easy | Post-Order Bottom-Up Height + Short-Circuit Sentinel (`-1`) |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`daily-practice/lc-0131-palindrome-partitioning.py`](daily-practice/lc-0131-palindrome-partitioning.py)<br>[`luffy/36-lc-0131-palindrome-partitioning.py`](luffy/36-lc-0131-palindrome-partitioning.py)<br>[`daily-practice/lc-0131-palindrome-partitioning.md`](daily-practice/lc-0131-palindrome-partitioning.md)<br>[`luffy/36-lc-0131-palindrome-partitioning.md`](luffy/36-lc-0131-palindrome-partitioning.md) | Medium | Backtracking + Substring Palindrome Check (`s[i:j+1]`) |
| **143** | Reorder List | [LC 143](https://leetcode.com/problems/reorder-list/) | [`daily-practice/lc-0143-reorder-list.py`](daily-practice/lc-0143-reorder-list.py)<br>[`daily-practice/lc-0143-reorder-list.md`](daily-practice/lc-0143-reorder-list.md) | Medium | Fast/Slow Mid (LC 876) + Reverse 2nd Half (LC 206) + Zip-Merge |
| **153** | Find Minimum in Rotated Sorted Array | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)<br>[`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md) | Medium | Binary Search on Two-Segment Step Array (`nums[-1]`) |
| **199** | Binary Tree Right Side View | [LC 199](https://leetcode.com/problems/binary-tree-right-side-view/) | [`daily-practice/lc-0199-binary-tree-right-side-view.py`](daily-practice/lc-0199-binary-tree-right-side-view.py)<br>[`daily-practice/lc-0199-binary-tree-right-side-view.md`](daily-practice/lc-0199-binary-tree-right-side-view.md) | Medium | DFS Root-Right-Left Traversal (`depth == len(ans)`) |
| **216** | Combination Sum III | [LC 216](https://leetcode.com/problems/combination-sum-iii/) | [`daily-practice/lc-0216-combination-sum-3.py`](daily-practice/lc-0216-combination-sum-3.py)<br>[`daily-practice/lc-0216-combination-sum-3.md`](daily-practice/lc-0216-combination-sum-3.md) | Medium | Backtracking + Remaining Count Bound Pruning (`j >= d`) |
| **235** | Lowest Common Ancestor of a BST | [LC 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py)<br>[`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.md`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.md) | Medium | BST Value-Directed Split / Interval Divergence |

| **237** | Delete Node in a Linked List | [LC 237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [`daily-practice/lc-0237-delete-node-in-a-linked-list.py`](daily-practice/lc-0237-delete-node-in-a-linked-list.py)<br>[`daily-practice/lc-0237-delete-node-in-a-linked-list.md`](daily-practice/lc-0237-delete-node-in-a-linked-list.md) | Medium | Scapegoat Value Copy + Bypass Next Node |
| **513** | Find Bottom Left Tree Value | [LC 513](https://leetcode.com/problems/find-bottom-left-tree-value/) | [`daily-practice/lc-0513-find-bottom-left-tree-value.py`](daily-practice/lc-0513-find-bottom-left-tree-value.py)<br>[`daily-practice/lc-0513-find-bottom-left-tree-value.md`](daily-practice/lc-0513-find-bottom-left-tree-value.md) | Medium | Reverse BFS (Right-to-Left Queue) / Final Deque Node |
| **876** | Middle of the Linked List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | [`daily-practice/lc-0876-middle-of-the-linked-list.py`](daily-practice/lc-0876-middle-of-the-linked-list.py)<br>[`daily-practice/lc-0876-middle-of-the-linked-list.md`](daily-practice/lc-0876-middle-of-the-linked-list.md) | Easy | Fast & Slow Pointers (`slow=1`, `fast=2`) |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py)<br>[`daily-practice/lc-2029-stone-game-ix.md`](daily-practice/lc-2029-stone-game-ix.md) | Medium | Modulo 3 Arithmetic / Game Theory |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)<br>[`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md) | Easy | Sliding Window / Frequency Map |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py)<br>[`daily-practice/lc-3471-find-the-largest-almost-missing-integer.md`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.md) | Easy | Fixed Sliding Window + Frequency Hashing |

---

## Topic-Wise Curriculum & Problem Index

### 1. Arrays, Strings, Two Pointers & Sliding Window

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/02-lc-0001-two-sum.py`](luffy/02-lc-0001-two-sum.py)<br>[`top-100/lc-0001-two-sum.py`](top-100/lc-0001-two-sum.py)<br>[`luffy/02-lc-0001-two-sum.md`](luffy/02-lc-0001-two-sum.md) | Easy | Hash Map | Single-pass hash map storing complement `target - num`. |
| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`luffy/04-lc-0003-longest-substring-without-repeating-characters.py`](luffy/04-lc-0003-longest-substring-without-repeating-characters.py)<br>[`top-100/lc-0003-longest-substring-without-repeating-characters.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py)<br>[`luffy/04-lc-0003-longest-substring-without-repeating-characters.md`](luffy/04-lc-0003-longest-substring-without-repeating-characters.md)<br>[`top-100/lc-0003-longest-substring-without-repeating-characters.md`](top-100/lc-0003-longest-substring-without-repeating-characters.md) | Medium | Sliding Window | Maintain set/dict window; contract left pointer when duplicate seen. |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py)<br>[`top-100/lc-0011-container-with-most-water.md`](top-100/lc-0011-container-with-most-water.md) | Medium | Two Pointers (Left/Right) | Move the pointer pointing to the shorter line to potentially maximize area. |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/lc-0015-3sum.py`](top-100/lc-0015-3sum.py)<br>[`top-100/lc-0015-3sum.md`](top-100/lc-0015-3sum.md) | Medium | Two Pointers / Extreme Pruning | Sort array; fix anchor $nums[i]$; 2-way extreme pruning & deduplication. |
| **16** | 3Sum Closest | [LC 16](https://leetcode.com/problems/3sum-closest/) | [`top-100/lc-0016-3-sum-closest.py`](top-100/lc-0016-3-sum-closest.py)<br>[`top-100/lc-0016-3-sum-closest.md`](top-100/lc-0016-3-sum-closest.md) | Medium | Two Pointers / 2-Way Bound Pruning | Sort array; fix anchor $nums[i]$; track closest $|sum - target|$ with $\mathcal{O}(1)$ min/max sum pruning. |
| **26** | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`luffy/05-lc-0026-remove-duplicates-from-sorted-array.py`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.py)<br>[`luffy/05-lc-0026-remove-duplicates-from-sorted-array.md`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.md) | Easy | Two Pointers (Slow/Fast) | Overwrite duplicate elements in-place with slow pointer. |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/lc-0042-trapping-rain-water.py`](top-100/lc-0042-trapping-rain-water.py)<br>[`top-100/lc-0042-trapping-rain-water.md`](top-100/lc-0042-trapping-rain-water.md) | Hard | Two Pointers / Pre-Suf Max | Inward two-pointer sweep tracking `pre_max` and `suf_max`. |
| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/08-lc-0059-spiral-matrix-ii.py`](luffy/08-lc-0059-spiral-matrix-ii.py)<br>[`luffy/09-lc-0059-spiral-matrix-ii-alt.py`](luffy/09-lc-0059-spiral-matrix-ii-alt.py)<br>[`luffy/08-lc-0059-spiral-matrix-ii.md`](luffy/08-lc-0059-spiral-matrix-ii.md)<br>[`luffy/09-lc-0059-spiral-matrix-ii-alt.md`](luffy/09-lc-0059-spiral-matrix-ii-alt.md) | Medium | Matrix Simulation | Layer-by-layer traversal with boundary tracking (top, bottom, left, right). |
| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`top-100/lc-0167-two-sum-ii-input-array-is-sorted.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)<br>[`luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.md`](luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.md)<br>[`top-100/lc-0167-two-sum-ii-input-array-is-sorted.md`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.md) | Medium | Two Pointers (Inward) | Exploit sorted order; shrink search space based on sum vs target (1-based index). |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`luffy/06-lc-0209-minimum-size-subarray-sum.py`](luffy/06-lc-0209-minimum-size-subarray-sum.py)<br>[`top-100/lc-0209-minimum-size-subarray-sum.py`](top-100/lc-0209-minimum-size-subarray-sum.py)<br>[`luffy/06-lc-0209-minimum-size-subarray-sum.md`](luffy/06-lc-0209-minimum-size-subarray-sum.md)<br>[`top-100/lc-0209-minimum-size-subarray-sum.md`](top-100/lc-0209-minimum-size-subarray-sum.md) | Medium | Sliding Window | Expand right pointer to reach target sum, then shrink left to minimize window. |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/lc-0713-subarray-product-less-than-k.py`](top-100/lc-0713-subarray-product-less-than-k.py)<br>[`top-100/lc-0713-subarray-product-less-than-k.md`](top-100/lc-0713-subarray-product-less-than-k.md) | Medium | Sliding Window / Product Counting | Maintain window product `prod < k`; count valid subarrays ending at `right` with `right - left + 1`. |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py)<br>[`daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md) | Easy | Sliding Window / Frequency Map | Window condition: maintain character frequency `<= 2`. |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/lc-3471-find-the-largest-almost-missing-integer.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py)<br>[`daily-practice/lc-3471-find-the-largest-almost-missing-integer.md`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.md) | Easy | Fixed Sliding Window / Hash Table | Slide fixed window of size $k$; count frequencies across distinct windows using set deduplication. |

---

### 2. Binary Search

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **33** | Search in Rotated Sorted Array | [LC 33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)<br>[`top-100/lc-0033-search-in-rotated-sorted-array.md`](top-100/lc-0033-search-in-rotated-sorted-array.md) | Medium | Binary Search on Rotated Array (`nums[-1]`) | Compare `nums[mid]` & `target` with `nums[-1]`; classify segment via Red-Blue framework in $O(\log n)$. |
| **34** | Find First and Last Position of Element in Sorted Array | [LC 34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)<br>[`top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md) | Medium | Binary Search (`lower_bound`) | Use `lower_bound(target)` for start and `lower_bound(target + 1) - 1` for end in $O(\log n)$. |
| **153** | Find Minimum in Rotated Sorted Array | [LC 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)<br>[`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md) | Medium | Binary Search on Two-Segment Array (`nums[-1]`) | Compare `nums[mid]` with `nums[-1]`; identify left/right step segment in $O(\log n)$. |
| **162** | Find Peak Element | [LC 162](https://leetcode.com/problems/find-peak-element/) | [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)<br>[`top-100/lc-0162-find-peak-element.md`](top-100/lc-0162-find-peak-element.md) | Medium | Binary Search (Slope Peak / Open Interval) | Check `nums[mid] > nums[mid+1]` slope; shrink search space via Red-Blue framework in $O(\log n)$. |
| **704** | Binary Search | [LC 704](https://leetcode.com/problems/binary-search/) | [`luffy/07-lc-0704-binary-search.py`](luffy/07-lc-0704-binary-search.py)<br>[`luffy/07-lc-0704-binary-search.md`](luffy/07-lc-0704-binary-search.md) | Easy | Binary Search (Closed Interval) | `left <= right` with `mid = left + (right - left) // 2` to prevent overflow. |

---

### 3. Prefix Sum & Difference Arrays

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-0303-prefix-sum-practices.py`](luffy/10-lc-0303-prefix-sum-practices.py)<br>[`luffy/10-lc-0303-range-sum-query-immutable-alt.py`](luffy/10-lc-0303-range-sum-query-immutable-alt.py)<br>[`luffy/10-lc-0303-range-sum-query-immutable.py`](luffy/10-lc-0303-range-sum-query-immutable.py)<br>[`luffy/11-prefix-sum-basic-example.py`](luffy/11-prefix-sum-basic-example.py)<br>[`luffy/10-lc-0303-prefix-sum-practices.md`](luffy/10-lc-0303-prefix-sum-practices.md)<br>[`luffy/10-lc-0303-range-sum-query-immutable-alt.md`](luffy/10-lc-0303-range-sum-query-immutable-alt.md)<br>[`luffy/10-lc-0303-range-sum-query-immutable.md`](luffy/10-lc-0303-range-sum-query-immutable.md)<br>[`luffy/11-prefix-sum-basic-example.md`](luffy/11-prefix-sum-basic-example.md) | Easy | Prefix Sum Array | Precompute cumulative sum array: `query(i, j) = prefix[j+1] - prefix[i]` in $O(1)$. |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-0560-subarray-sum-equals-k.py`](luffy/11-lc-0560-subarray-sum-equals-k.py)<br>[`top-100/lc-0560-subarray-sum-equals-k.py`](top-100/lc-0560-subarray-sum-equals-k.py)<br>[`luffy/11-lc-0560-subarray-sum-equals-k.md`](luffy/11-lc-0560-subarray-sum-equals-k.md) | Medium | Prefix Sum + Hash Map | Track frequency of running prefix sums; check if `curr_sum - k` occurred. |
| **1109** | Corporate Flight Bookings | [LC 1109](https://leetcode.com/problems/corporate-flight-bookings/) | [`luffy/12-lc-1109-corporate-flight-bookings.py`](luffy/12-lc-1109-corporate-flight-bookings.py)<br>[`luffy/12-lc-1109-corporate-flight-bookings.md`](luffy/12-lc-1109-corporate-flight-bookings.md) | Medium | Difference Array | Range update $[l, r]$ by `diff[l] += val` and `diff[r+1] -= val`, then compute prefix sums. |

---

### 4. Intervals & In-Place Array Hashing

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **41** | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`luffy/14-lc-0041-first-missing-positive.py`](luffy/14-lc-0041-first-missing-positive.py)<br>[`luffy/14-lc-0041-first-missing-positive.md`](luffy/14-lc-0041-first-missing-positive.md) | Hard | Cyclic Sort / In-Place Hash | Place number `x` at index `x - 1` in $O(n)$ time and $O(1)$ extra space. |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-0056-merge-intervals.py`](luffy/13-lc-0056-merge-intervals.py)<br>[`top-100/lc-0056-merge-intervals.py`](top-100/lc-0056-merge-intervals.py)<br>[`luffy/13-lc-0056-merge-intervals.md`](luffy/13-lc-0056-merge-intervals.md) | Medium | Interval Sorting | Sort intervals by start time and merge overlapping segments (`curr.start <= prev.end`). |

---

### 5. Linked Lists

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **19** | Remove Nth Node From End of List | [LC 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [`top-100/lc-0019-remove-nth-node-from-end-of-list.py`](top-100/lc-0019-remove-nth-node-from-end-of-list.py)<br>[`top-100/lc-0019-remove-nth-node-from-end-of-list.md`](top-100/lc-0019-remove-nth-node-from-end-of-list.md) | Medium | Dummy + Fixed-Gap Two Pointers | Advance `right` by $n$ steps from `dummy`, then move `left` and `right` synchronously until `right.next` is `None`; delete `left.next` in $O(L)$ time and $O(1)$ space. |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-0021-merge-two-sorted-lists.py`](luffy/16-lc-0021-merge-two-sorted-lists.py)<br>[`top-100/lc-0021-merge-two-sorted-lists.py`](top-100/lc-0021-merge-two-sorted-lists.py)<br>[`luffy/16-lc-0021-merge-two-sorted-lists.md`](luffy/16-lc-0021-merge-two-sorted-lists.md) | Easy | Dummy Head + Two Pointers | Build new list with dummy head, appending the smaller node at each step. |
| **25** | Reverse Nodes in k-Group | [LC 25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [`daily-practice/lc-0025-reverse-nodes-in-k-group.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py)<br>[`daily-practice/lc-0025-reverse-nodes-in-k-group.md`](daily-practice/lc-0025-reverse-nodes-in-k-group.md) | Hard | Length Check + k-Group In-Place Reversal | Precompute length $n$; reverse $k$ nodes iteratively; 4-step stitch and advance $p_0$ in $O(n)$ time and $O(1)$ space. |
| **82** | Remove Duplicates from Sorted List II | [LC 82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) | [`daily-practice/lc-0082-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.py)<br>[`daily-practice/lc-0082-remove-duplicates-from-sorted-list.md`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.md) | Medium | Sentinel Dummy + 2-Step Lookahead | Use `dummy -> head`; when `cur.next.val == cur.next.next.val`, record `val` and loop `cur.next = cur.next.next` while `cur.next.val == val` without advancing `cur` in $O(N)$ time and $O(1)$ space. |
| **83** | Remove Duplicates from Sorted List | [LC 83](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | [`daily-practice/lc-0083-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.py)<br>[`daily-practice/lc-0083-remove-duplicates-from-sorted-list.md`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.md) | Easy | In-Place Adjacent Deduplication | If `cur.next.val == cur.val`, bypass duplicate with `cur.next = cur.next.next` without moving `cur`; else advance `cur = cur.next` in $O(N)$ time and $O(1)$ space. |
| **92** | Reverse Linked List II | [LC 92](https://leetcode.com/problems/reverse-linked-list-ii/) | [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)<br>[`daily-practice/lc-0092-reversed-linked-list-2.md`](daily-practice/lc-0092-reversed-linked-list-2.md) | Medium | Sentinel Dummy + 3-Pointer Reversal | Advance $p_0$ to $left-1$, reverse $right-left+1$ nodes, reconnect tail/head in $O(n)$ time. |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`luffy/17-lc-0141-linked-list-cycle.py`](luffy/17-lc-0141-linked-list-cycle.py)<br>[`top-100/lc-0141-linked-list-cycle.py`](top-100/lc-0141-linked-list-cycle.py)<br>[`luffy/17-lc-0141-linked-list-cycle.md`](luffy/17-lc-0141-linked-list-cycle.md)<br>[`top-100/lc-0141-linked-list-cycle.md`](top-100/lc-0141-linked-list-cycle.md) | Easy | Floyd's Fast & Slow Pointers | Fast moves 2 steps, slow moves 1 step; relative speed 1 guarantees collision in cycle. |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`luffy/18-lc-0142-linked-list-cycle-ii.py`](luffy/18-lc-0142-linked-list-cycle-ii.py)<br>[`top-100/lc-0142-linked-list-cycle-ii.py`](top-100/lc-0142-linked-list-cycle-ii.py)<br>[`luffy/18-lc-0142-linked-list-cycle-ii.md`](luffy/18-lc-0142-linked-list-cycle-ii.md)<br>[`top-100/lc-0142-linked-list-cycle-ii.md`](top-100/lc-0142-linked-list-cycle-ii.md) | Medium | Floyd's Algorithm + Math | Reset head upon collision; both advance by 1 step ($a=c$) to meet at cycle entry in $O(n)$ time and $O(1)$ space. |
| **143** | Reorder List | [LC 143](https://leetcode.com/problems/reorder-list/) | [`daily-practice/lc-0143-reorder-list.py`](daily-practice/lc-0143-reorder-list.py)<br>[`daily-practice/lc-0143-reorder-list.md`](daily-practice/lc-0143-reorder-list.md) | Medium | Mid + Reverse + Zip-Merge | Find mid, reverse second half, and interleave merge both halves with `while head2.next:` in $O(n)$ time and $O(1)$ space. |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-0206-reverse-linked-list.py`](luffy/15-lc-0206-reverse-linked-list.py)<br>[`top-100/lc-0206-reverse-linked-list.py`](top-100/lc-0206-reverse-linked-list.py)<br>[`luffy/15-lc-0206-reverse-linked-list.md`](luffy/15-lc-0206-reverse-linked-list.md)<br>[`top-100/lc-0206-reverse-linked-list.md`](top-100/lc-0206-reverse-linked-list.md) | Easy | Iterative Pointer Reversal | Maintain `prev`, `curr`, and `nxt` pointers to reverse next links in-place in $O(n)$ time and $O(1)$ space. |
| **237** | Delete Node in a Linked List | [LC 237](https://leetcode.com/problems/delete-node-in-a-linked-list/) | [`daily-practice/lc-0237-delete-node-in-a-linked-list.py`](daily-practice/lc-0237-delete-node-in-a-linked-list.py)<br>[`daily-practice/lc-0237-delete-node-in-a-linked-list.md`](daily-practice/lc-0237-delete-node-in-a-linked-list.md) | Medium | Scapegoat Node Overwrite | Overwrite node's value with next node's value (`node.val = node.next.val`) and bypass next node in $O(1)$ time and $O(1)$ space. |
| **876** | Middle of the Linked List | [LC 876](https://leetcode.com/problems/middle-of-the-linked-list/) | [`daily-practice/lc-0876-middle-of-the-linked-list.py`](daily-practice/lc-0876-middle-of-the-linked-list.py)<br>[`daily-practice/lc-0876-middle-of-the-linked-list.md`](daily-practice/lc-0876-middle-of-the-linked-list.md) | Easy | Fast & Slow Pointers (2:1 Speed) | `slow` moves 1 step, `fast` moves 2 steps; when `fast` finishes, `slow` is at middle. |

---

### 6. Stacks & Queues

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-0020-valid-parentheses.py`](luffy/19-lc-0020-valid-parentheses.py)<br>[`luffy/20-lc-0020-valid-parentheses-dict.py`](luffy/20-lc-0020-valid-parentheses-dict.py)<br>[`top-100/lc-0020-valid-parentheses.py`](top-100/lc-0020-valid-parentheses.py)<br>[`luffy/19-lc-0020-valid-parentheses.md`](luffy/19-lc-0020-valid-parentheses.md)<br>[`luffy/20-lc-0020-valid-parentheses-dict.md`](luffy/20-lc-0020-valid-parentheses-dict.md) | Easy | Stack | Push opening brackets; pop and match corresponding closing bracket. |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-0155-min-stack.py`](luffy/21-lc-0155-min-stack.py)<br>[`top-100/lc-0155-min-stack.py`](top-100/lc-0155-min-stack.py)<br>[`luffy/21-lc-0155-min-stack.md`](luffy/21-lc-0155-min-stack.md) | Medium | Auxiliary Stack / Pair Stack | Track running minimum alongside each pushed value in $O(1)$. |
| **227** | Basic Calculator II | [LC 227](https://leetcode.com/problems/basic-calculator-ii/) | [`luffy/22-lc-0227-basic-calculator-ii.py`](luffy/22-lc-0227-basic-calculator-ii.py)<br>[`luffy/22-lc-0227-basic-calculator-ii.md`](luffy/22-lc-0227-basic-calculator-ii.md) | Medium | Stack / Parsing | Evaluate `*` and `/` immediately on top of stack; sum all values for `+` and `-`. |
| **232** | Implement Queue using Stacks | [LC 232](https://leetcode.com/problems/implement-queue-using-stacks/) | [`luffy/24-lc-0232-implement-queue-using-stacks.py`](luffy/24-lc-0232-implement-queue-using-stacks.py)<br>[`luffy/24-lc-0232-implement-queue-using-stacks.md`](luffy/24-lc-0232-implement-queue-using-stacks.md) | Easy | Two Stacks (`in_stack`, `out_stack`) | Amortized $O(1)$ pop/peek by transferring elements only when `out_stack` is empty. |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-0394-decode-string.py`](luffy/23-lc-0394-decode-string.py)<br>[`top-100/lc-0394-decode-string.py`](top-100/lc-0394-decode-string.py)<br>[`luffy/23-lc-0394-decode-string.md`](luffy/23-lc-0394-decode-string.md) | Medium | Stack (Counts & Strings) | Push current string and multiplier onto stack when encountering `[`; pop on `]`. |

---

### 7. Trees & Binary Search Trees (BST)

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-0094-binary-tree-inorder-traversal.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py)<br>[`luffy/25-tree-traversal-advanced-patterns.py`](luffy/25-tree-traversal-advanced-patterns.py)<br>[`top-100/lc-0094-binary-tree-inorder-traversal.py`](top-100/lc-0094-binary-tree-inorder-traversal.py)<br>[`luffy/25-lc-0094-binary-tree-inorder-traversal.md`](luffy/25-lc-0094-binary-tree-inorder-traversal.md)<br>[`luffy/25-tree-traversal-advanced-patterns.md`](luffy/25-tree-traversal-advanced-patterns.md) | Easy | DFS (Left, Root, Right) | Traversal yields sorted order for BSTs; implemented recursively & iteratively. |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-0098-validate-binary-search-tree-bounds.py`](luffy/29-lc-0098-validate-binary-search-tree-bounds.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-inorder.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.py`](luffy/29-lc-0098-validate-binary-search-tree-recursion.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.py`](luffy/29-lc-0098-validate-binary-search-tree-stack.py)<br>[`top-100/lc-0098-validate-binary-search-tree.py`](top-100/lc-0098-validate-binary-search-tree.py)<br>[`luffy/29-lc-0098-validate-binary-search-tree-bounds.md`](luffy/29-lc-0098-validate-binary-search-tree-bounds.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-inorder.md`](luffy/29-lc-0098-validate-binary-search-tree-inorder.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-recursion.md`](luffy/29-lc-0098-validate-binary-search-tree-recursion.md)<br>[`luffy/29-lc-0098-validate-binary-search-tree-stack.md`](luffy/29-lc-0098-validate-binary-search-tree-stack.md) | Medium | BST Range Bounds / Inorder | Validate node with strictly bounded $(min\_val, max\_val)$ interval. |
| **100** | Same Tree | [LC 100](https://leetcode.com/problems/same-tree/) | [`daily-practice/lc-0100-same-tree.py`](daily-practice/lc-0100-same-tree.py)<br>[`daily-practice/lc-0100-same-tree.md`](daily-practice/lc-0100-same-tree.md) | Easy | Dual-Tree Synchronous Recursion | Both null -> True (`p is q`); values must match and both subtrees match in $O(\min(N, M))$ time. |
| **101** | Symmetric Tree | [LC 101](https://leetcode.com/problems/symmetric-tree/) | [`top-100/lc-0101-symmetric-tree.py`](top-100/lc-0101-symmetric-tree.py)<br>[`top-100/lc-0101-symmetric-tree.md`](top-100/lc-0101-symmetric-tree.md) | Easy | Dual-Subtree Mirror Recursion | Single tree symmetric ⟺ `isMirror(root.left, root.right)`; cross-match outer `(p.l, q.r)` and inner `(p.r, q.l)` in $O(N)$ time. |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-0102-binary-tree-level-order-traversal.py`](luffy/28-lc-0102-binary-tree-level-order-traversal.py)<br>[`top-100/lc-0102-binary-tree-level-order-traversal.py`](top-100/lc-0102-binary-tree-level-order-traversal.py)<br>[`luffy/28-lc-0102-binary-tree-level-order-traversal.md`](luffy/28-lc-0102-binary-tree-level-order-traversal.md)<br>[`top-100/lc-0102-binary-tree-level-order-traversal.md`](top-100/lc-0102-binary-tree-level-order-traversal.md) | Medium | Dual-Buffer BFS / Level Snapshot | Maintain `cur` and `nxt` buffers to isolate levels; append `node.val` and roll `cur = nxt` in $O(N)$ time and $O(N)$ space. |
| **103** | Binary Tree Zigzag Level Order Traversal | [LC 103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py)<br>[`daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.md`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.md) | Medium | BFS / Zigzag Level Traversal | Traverse with `cur` & `nxt` buffers; append `vals[::-1] if even else vals` and toggle `even = not even` in $O(N)$ time. |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-0104-maximum-depth-of-binary-tree.py`](luffy/26-lc-0104-maximum-depth-of-binary-tree.py)<br>[`top-100/lc-0104-maximum-depth-of-binary-tree.py`](top-100/lc-0104-maximum-depth-of-binary-tree.py)<br>[`luffy/26-lc-0104-maximum-depth-of-binary-tree.md`](luffy/26-lc-0104-maximum-depth-of-binary-tree.md)<br>[`top-100/lc-0104-maximum-depth-of-binary-tree.md`](top-100/lc-0104-maximum-depth-of-binary-tree.md) | Easy | Post-order Divide & Conquer | Depth = $1 + \max(\text{left}, \text{right})$; foundational primitive for Tree DP. |
| **105** | Construct Binary Tree from Preorder & Inorder | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)<br>[`top-100/lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py`](top-100/lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py)<br>[`luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) | Medium | Divide & Conquer / Hash Map | Preorder gives root; Inorder splits left and right subtrees. |
| **110** | Balanced Binary Tree | [LC 110](https://leetcode.com/problems/balanced-binary-tree/) | [`daily-practice/lc-0110-balanced-binary-tree.py`](daily-practice/lc-0110-balanced-binary-tree.py)<br>[`daily-practice/lc-0110-balanced-binary-tree.md`](daily-practice/lc-0110-balanced-binary-tree.md) | Easy | Post-order Bottom-Up Height + Short-Circuit Pruning | Post-order compute height; if left/right subtree is -1 or $|h_l - h_r| > 1$, return -1; else return $\max(h_l, h_r) + 1$ in $O(N)$ time. |
| **144** | Binary Tree Preorder Traversal | [LC 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [`luffy/25-lc-0144-binary-tree-preorder-traversal.py`](luffy/25-lc-0144-binary-tree-preorder-traversal.py)<br>[`luffy/25-lc-0144-binary-tree-preorder-traversal.md`](luffy/25-lc-0144-binary-tree-preorder-traversal.md) | Easy | DFS (Root, Left, Right) | Root processed before recursive traversal of subtrees. |
| **145** | Binary Tree Postorder Traversal | [LC 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [`luffy/25-lc-0145-binary-tree-postorder-traversal.py`](luffy/25-lc-0145-binary-tree-postorder-traversal.py)<br>[`luffy/25-lc-0145-binary-tree-postorder-traversal.md`](luffy/25-lc-0145-binary-tree-postorder-traversal.md) | Easy | DFS (Left, Right, Root) | Subtrees processed before processing the root node. |
| **199** | Binary Tree Right Side View | [LC 199](https://leetcode.com/problems/binary-tree-right-side-view/) | [`daily-practice/lc-0199-binary-tree-right-side-view.py`](daily-practice/lc-0199-binary-tree-right-side-view.py)<br>[`daily-practice/lc-0199-binary-tree-right-side-view.md`](daily-practice/lc-0199-binary-tree-right-side-view.md) | Medium | DFS Root-Right-Left Traversal | Visit right subtree first; append node value when `depth == len(ans)` in $O(N)$ time and $O(H)$ space. |
| **235** | Lowest Common Ancestor of a BST | [LC 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | [`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py)<br>[`daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.md`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.md) | Medium | BST Value-Directed Split / Divergence | Compare with `root.val`; if both smaller go left, if both greater go right; first divergence point is LCA in $O(H)$ time. |
| **236** | Lowest Common Ancestor of Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.py)<br>[`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py)<br>[`luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md`](luffy/27-lc-0236-lowest-common-ancestor-of-a-binary-tree.md)<br>[`top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.md`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.md) | Medium | Postorder Divide & Conquer (4-State Aggregation) | If both left and right return non-null, root is LCA; else propagate non-null child in $O(N)$ time and $O(H)$ space. |
| **513** | Find Bottom Left Tree Value | [LC 513](https://leetcode.com/problems/find-bottom-left-tree-value/) | [`daily-practice/lc-0513-find-bottom-left-tree-value.py`](daily-practice/lc-0513-find-bottom-left-tree-value.py)<br>[`daily-practice/lc-0513-find-bottom-left-tree-value.md`](daily-practice/lc-0513-find-bottom-left-tree-value.md) | Medium | Reverse BFS Queue (Right-to-Left) | Push right child before left child; last popped node in BFS is bottom-left in $O(N)$ time and $O(W)$ space. |
| **Misc** | Advanced Tree Practices | — | [`luffy/25-tree-traversal-advanced-patterns.py`](luffy/25-tree-traversal-advanced-patterns.py) | Medium | Tree Patterns | Comprehensive tree construction and traversal utilities. |

---

### 8. Backtracking & Combinatorics

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **17** | Letter Combinations of a Phone Number | [LC 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [`top-100/lc-0017-letter-combinations-of-a-phone-number.py`](top-100/lc-0017-letter-combinations-of-a-phone-number.py)<br>[`top-100/lc-0017-letter-combinations-of-a-phone-number.md`](top-100/lc-0017-letter-combinations-of-a-phone-number.md) | Medium | Backtracking (Cartesian Product) | Backtracking three-step model; in-place array overwrite `path[i] = char` to enumerate digit letters in $O(4^n \cdot n)$ time. |
| **22** | Generate Parentheses | [LC 22](https://leetcode.com/problems/generate-parentheses/) | [`top-100/lc-0022-generate-parentheses.py`](top-100/lc-0022-generate-parentheses.py)<br>[`top-100/lc-0022-generate-parentheses.md`](top-100/lc-0022-generate-parentheses.md) | Medium | Backtracking / Prefix Balance | Maintain prefix balance invariant $\text{count}(\text{'('}) \ge \text{count}(\text{')'})$ and in-place buffer overwrite to generate $C_n$ valid sequences in $O(\frac{4^n}{\sqrt{n}})$ time. |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-0039-combination-sum.py`](luffy/34-lc-0039-combination-sum.py)<br>[`top-100/lc-0039-combination-sum.py`](top-100/lc-0039-combination-sum.py)<br>[`luffy/34-lc-0039-combination-sum.md`](luffy/34-lc-0039-combination-sum.md) | Medium | Backtracking (Unbounded Choice) | Pass `start_index` to allow reuse of the current element without duplicate permutations. |
| **40** | Combination Sum II | [LC 40](https://leetcode.com/problems/combination-sum-ii/) | [`luffy/35-lc-0040-combination-sum-ii.py`](luffy/35-lc-0040-combination-sum-ii.py)<br>[`luffy/35-lc-0040-combination-sum-ii.md`](luffy/35-lc-0040-combination-sum-ii.md) | Medium | Backtracking + Deduplication | Sort candidates; skip duplicate elements at the same tree depth (`if i > start and nums[i] == nums[i-1]: continue`). |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-0046-permutations.py`](luffy/32-lc-0046-permutations.py)<br>[`top-100/lc-0046-permutations.py`](top-100/lc-0046-permutations.py)<br>[`luffy/32-lc-0046-permutations.md`](luffy/32-lc-0046-permutations.md) | Medium | Backtracking (Used Array) | Maintain `used` boolean array or swap elements in-place to explore all orderings. |
| **77** | Combinations | [LC 77](https://leetcode.com/problems/combinations/) | [`daily-practice/lc-0077-combinations.py`](daily-practice/lc-0077-combinations.py)<br>[`luffy/31-lc-0077-combinations.py`](luffy/31-lc-0077-combinations.py)<br>[`daily-practice/lc-0077-combinations.md`](daily-practice/lc-0077-combinations.md)<br>[`luffy/31-lc-0077-combinations.md`](luffy/31-lc-0077-combinations.md) | Medium | Backtracking + Pruning | Prune search branch if remaining candidates are insufficient to reach size $k$ (`range(i, d-1, -1)`). |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-0078-subsets.py`](luffy/33-lc-0078-subsets.py)<br>[`top-100/lc-0078-subsets.py`](top-100/lc-0078-subsets.py)<br>[`luffy/33-lc-0078-subsets.md`](luffy/33-lc-0078-subsets.md)<br>[`top-100/lc-0078-subsets.md`](top-100/lc-0078-subsets.md) | Medium | Backtracking (0-1 Pick vs Multi-way Loop) | 0-1 choose/skip binary tree or multi-way start index loop; record `path.copy()` to generate all $2^n$ subsets in $O(2^n \cdot n)$ time. |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-0079-word-search.py`](luffy/37-lc-0079-word-search.py)<br>[`top-100/lc-0079-word-search.py`](top-100/lc-0079-word-search.py)<br>[`luffy/37-lc-0079-word-search.md`](luffy/37-lc-0079-word-search.md) | Medium | 2D Grid DFS + Backtracking | Mark visited cells in-place (e.g. `'#'`); restore character on backtracking. |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`daily-practice/lc-0131-palindrome-partitioning.py`](daily-practice/lc-0131-palindrome-partitioning.py)<br>[`luffy/36-lc-0131-palindrome-partitioning.py`](luffy/36-lc-0131-palindrome-partitioning.py)<br>[`daily-practice/lc-0131-palindrome-partitioning.md`](daily-practice/lc-0131-palindrome-partitioning.md)<br>[`luffy/36-lc-0131-palindrome-partitioning.md`](luffy/36-lc-0131-palindrome-partitioning.md) | Medium | Backtracking + Substring Palindrome Check | Partition string into palindromic segments; validate $s[i:j+1] == (s[i:j+1])[::-1]$ and backtrack in $O(n \cdot 2^n)$ time. |

---

### 9. Graph Algorithms (DFS, BFS, Topological Sort)

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **130** | Surrounded Regions | [LC 130](https://leetcode.com/problems/surrounded-regions/) | [`luffy/39-lc-0130-surrounded-regions.py`](luffy/39-lc-0130-surrounded-regions.py)<br>[`luffy/39-lc-0130-surrounded-regions.md`](luffy/39-lc-0130-surrounded-regions.md) | Medium | Boundary Flood Fill (DFS/BFS) | Flood fill from outer border `'O'`s to protect them; flip remaining interior `'O'`s. |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-0200-number-of-islands.py`](luffy/38-lc-0200-number-of-islands.py)<br>[`top-100/lc-0200-number-of-islands.py`](top-100/lc-0200-number-of-islands.py)<br>[`luffy/38-lc-0200-number-of-islands.md`](luffy/38-lc-0200-number-of-islands.md) | Medium | Grid DFS / BFS (Sink Island) | Increment count upon finding `'1'`; recursively sink connected island to `'0'`. |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`luffy/42-lc-0207-course-schedule.py`](luffy/42-lc-0207-course-schedule.py)<br>[`top-100/lc-0207-course-schedule.py`](top-100/lc-0207-course-schedule.py)<br>[`luffy/42-lc-0207-course-schedule.md`](luffy/42-lc-0207-course-schedule.md) | Medium | Topological Sort (Kahn's / DFS) | Detect cycles in directed graph using in-degrees (Kahn's BFS) or 3-state DFS. |
| **994** | Rotting Oranges | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`luffy/40-lc-0994-rotting-oranges.py`](luffy/40-lc-0994-rotting-oranges.py)<br>[`luffy/40-lc-0994-rotting-oranges.md`](luffy/40-lc-0994-rotting-oranges.md) | Medium | Multi-source BFS | Enqueue all initially rotten oranges; propagate minute by minute to adjacent fresh ones. |
| **1091** | Shortest Path in Binary Matrix | [LC 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [`luffy/41-lc-1091-shortest-path-in-binary-matrix.py`](luffy/41-lc-1091-shortest-path-in-binary-matrix.py)<br>[`luffy/41-lc-1091-shortest-path-in-binary-matrix.md`](luffy/41-lc-1091-shortest-path-in-binary-matrix.md) | Medium | 8-Directional BFS | Find shortest path in unweighted grid; BFS guarantees minimum distance. |

---

### 10. Dynamic Programming & Math / Game Theory

| # | Problem Title | LeetCode Link | Solution Code & Notes | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/lc-0053-maximum-subarray.py`](top-100/lc-0053-maximum-subarray.py)<br>[`top-100/lc-0053-maximum-subarray.md`](top-100/lc-0053-maximum-subarray.md) | Medium | Kadane's Algorithm / DP | `curr_max = max(num, curr_max + num)`; maintains maximum contiguous sum in $O(n)$. |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/lc-2029-stone-game-ix.py`](daily-practice/lc-2029-stone-game-ix.py)<br>[`daily-practice/lc-2029-stone-game-ix.md`](daily-practice/lc-2029-stone-game-ix.md) | Medium | Modulo Arithmetic / Game Theory | Count residues modulo 3 ($c_0, c_1, c_2$); analyze winning conditions based on $c_0 \pmod 2$. |

---

### 11. Object-Oriented Programming (OOP) & Foundations

| # | Topic / Concept | Reference File | Difficulty | Core Concept | Description |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **2235** | Add Two Integers | [`luffy/01-lc-2235-add-two-integers.py`](luffy/01-lc-2235-add-two-integers.py) | Easy | Basic Arithmetic | Python function syntax and return values. |
| **OOP** | Car Class & Inheritance | [`luffy/car-object-oriented-example.py`](luffy/car-object-oriented-example.py)<br>[`luffy/10-oop-pre-main-practice.py`](luffy/10-oop-pre-main-practice.py) | Easy | OOP Principles | Encapsulation, `__init__`, class methods, and object instantiation in Python. |

---

## Interactive Web Viewer & Study Station

This repository features an automated, standalone single-page application (`index.html`) designed for distraction-free local study:

* **Interactive Algorithm Roadmap**: Explore a full-landscape curriculum organized into 5 progressive phases and 12 core topics, featuring mental model formulas and instant problem links.
* **Dual Split-Pane Layout**: Read detailed Markdown explanations while simultaneously reviewing syntax-highlighted Python solutions side-by-side.
* **View Mode Controls**: Switch instantly between `[Split View]`, `[Notes Only]`, and `[Code Only]`, with dedicated single-pane tab navigation on mobile devices.
* **Category Accordion**: Collapse / expand categories (`Top 100`, `Daily Practice`, `Luffy Curriculum`, `Topic Index`) or use `Expand All` / `Fold All`.
* **Difficulty & Pattern Filter Pills**: Filter by `Easy`, `Medium`, `Hard`, or specific algorithmic patterns.
* **Keyboard Shortcuts**: Press `/` to focus the search box, `Cmd+B` / `Ctrl+B` to toggle the sidebar, and `Esc` to clear search.

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

### 4. Enable Local Quality Gate (Pre-Commit Hook)
Activate the repository's automated pre-commit quality gate to validate note schema compliance and rebuild `index.html` on commit:
```bash
git config core.hooksPath .githooks
```
