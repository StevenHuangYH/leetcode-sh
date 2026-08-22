# LeetCode Master Problem Index (INDEX.md)

Welcome to the **Master Problem Index** for the LeetCode self-practices and algorithm curriculum. This index provides a complete, structured catalog of all 52+ problem solutions, notes, and topic classifications across the entire repository.

---

# LeetCode Self-Practices & Algorithm Curriculum

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Practice-FFA116.svg?logo=leetcode&logoColor=white)](https://leetcode.com/)
[![Problems Solved](https://img.shields.io/badge/Problems_Indexed-50+-brightgreen.svg)]()

Welcome to the **LeetCode Self-Practices** repository! This repository contains Python implementations, problem notes, and structured practice tracks covering foundational to advanced data structures and algorithmic patterns.

---

## Table of Contents

1. [Practice Statistics & Summary](#practice-statistics--summary)
2. [Repository Structure](#repository-structure)
3. [🔥 Top 100 Liked Track](#-top-100-liked-track)
4. [📅 Daily Practice Track](#-daily-practice-track)
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
6. [How to Run & Practice](#how-to-run--practice)

---

## Practice Statistics & Summary

| Difficulty | Count | Percentage |
| :--- | :--- | :--- |
| **Easy** | 17 | ~33% |
| **Medium** | 33 | ~63% |
| **Hard** | 2 | ~4% |
| **Total** | **52+ Solutions** | **100%** |

---

## Repository Structure

```tree
leetcode-sh/
├── luffy/                        # Core structured curriculum (categorized 01-42)
│   ├── 01-___BASICS___.txt       # Topic division markers
│   ├── 02-___ARRAYS_AND_STRINGS___.txt
│   ├── 07-___BINARY_SEARCH___.txt
│   ├── ...
│   ├── file_topics.txt           # Topic index reference
│   └── *.py                      # Python solution implementations
├── top-100/                      # Top 100 Liked Problems & Notes
│   ├── s-lc-3-longest-substring-without-repeating-characters.py
│   ├── s-lc-3-longest-substring-without-repeating-characters.md
│   ├── s-lc-11-contain-with-most-water.py
│   ├── s-lc-11-contain-with-most-water.md
│   ├── s-lc-15-3-sum.py
│   ├── s-lc-15-3-sum.md
│   ├── s-lc-42-trapping-rain-water.py
│   ├── s-lc-42-trapping-rain-water.md
│   ├── s-lc-53-maxiumu-subarry.py
│   ├── s-lc-53-maxiumu-subarry.md
│   ├── s-lc-167-two-sum-2.py
│   ├── s-lc-167-two-sum-2.md
│   ├── s-lc-209-minimum-size-subarry-sum.py
│   ├── s-lc-209-minimum-size-subarry-sum.md
│   ├── s-lc-713.py
│   └── s-lc-713.md
├── daily-practice/               # Daily LeetCode Practices & In-Depth Notes
│   ├── s-lc-2029.py
│   ├── s-lc-2029.md
│   ├── leetcode_2029_stone_game_ix.md
│   ├── s-lc-3090.py
│   ├── s-lc-3090.md
│   ├── s-lc-3471.py
│   └── s-lc-3471.md
└── README.md                     # Repository documentation & guide
```

---

## 🔥 Top 100 Liked Track

A dedicated tracking index for **LeetCode Top 100 Liked / High-Frequency Interview** problems implemented in this repository.

| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |
| :-: | :--- | :-: | :--- | :-: | :--- |
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/2-lc-1-two-sum-lc.py`](luffy/2-lc-1-two-sum-lc.py) | Easy | Hash Map (Complement `target - num`) |
| **3** | Longest Substring Without Repeating | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/s-lc-3-longest-substring-without-repeating-characters.py`](top-100/s-lc-3-longest-substring-without-repeating-characters.py)<br>[`top-100/s-lc-3-longest-substring-without-repeating-characters.md`](top-100/s-lc-3-longest-substring-without-repeating-characters.md)<br>[`luffy/4-lc-3-longest-substring-without-repeating-characters.py`](luffy/4-lc-3-longest-substring-without-repeating-characters.py) | Medium | Dynamic Sliding Window |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/s-lc-11-contain-with-most-water.py`](top-100/s-lc-11-contain-with-most-water.py)<br>[`top-100/s-lc-11-contain-with-most-water.md`](top-100/s-lc-11-contain-with-most-water.md) | Medium | Two Pointers (Greedy Shorter Line) |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/s-lc-15-3-sum.py`](top-100/s-lc-15-3-sum.py)<br>[`top-100/s-lc-15-3-sum.md`](top-100/s-lc-15-3-sum.md) | Medium | Sort + Two Pointers + 2-Way Extreme Pruning |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-stack-1-brackets.py`](luffy/19-lc-stack-1-brackets.py)<br>[`luffy/20-lc-stack2.py`](luffy/20-lc-stack2.py) | Easy | Stack Matching |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-21.py`](luffy/16-lc-21.py) | Easy | Dummy Head + Two Pointers |
| **26** | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`luffy/5-lc-26-remove-duplicates-from-sorted-array.py`](luffy/5-lc-26-remove-duplicates-from-sorted-array.py) | Easy | Slow/Fast Two Pointers (In-place) |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-39.py`](luffy/34-lc-39.py) | Medium | Backtracking (Unbounded Choice) |
| **41** | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`luffy/14-lc-41.py`](luffy/14-lc-41.py) | Hard | Cyclic Sort / In-Place Hashing ($O(1)$ space) |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/s-lc-42-trapping-rain-water.py`](top-100/s-lc-42-trapping-rain-water.py)<br>[`top-100/s-lc-42-trapping-rain-water.md`](top-100/s-lc-42-trapping-rain-water.md) | Hard | Two Pointers Sweep / Prefix-Suffix Max |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-46.py`](luffy/32-lc-46.py) | Medium | Backtracking (`used` array / in-place swap) |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/s-lc-53-maxiumu-subarry.py`](top-100/s-lc-53-maxiumu-subarry.py)<br>[`top-100/s-lc-53-maxiumu-subarry.md`](top-100/s-lc-53-maxiumu-subarry.md) | Medium | Kadane's Algorithm / DP ($O(1)$ space) |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-56-merge.py`](luffy/13-lc-56-merge.py) | Medium | Interval Sorting & Merging |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-78.py`](luffy/33-lc-78.py) | Medium | Backtracking / Cascading |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-79.py`](luffy/37-lc-79.py) | Medium | 2D Grid DFS + Backtracking |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-94-inorder.py`](luffy/25-lc-94-inorder.py) | Easy | Tree DFS (Inorder: L-Root-R) |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-98-sol-1.py`](luffy/29-lc-98-sol-1.py)... | Medium | BST Range Bounds `(min_val, max_val)` |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-102.py`](luffy/28-lc-102.py) | Medium | Queue BFS Level-by-Level |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-104py`](luffy/26-lc-104py) | Easy | Tree DFS / Divide & Conquer |
| **105** | Construct Tree from Preorder & Inorder | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-105.py`](luffy/30-lc-105.py) | Medium | Divide & Conquer / Subtree Slicing |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`luffy/36-lc-131.py`](luffy/36-lc-131.py) | Medium | Backtracking + Palindrome Verification |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`luffy/17-lc-141.py`](luffy/17-lc-141.py) | Easy | Floyd's Fast & Slow Pointers |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`luffy/18-lc-142.py`](luffy/18-lc-142.py) | Medium | Fast/Slow Pointers + Cycle Entry Math |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-stack3-min-stack.py`](luffy/21-lc-stack3-min-stack.py) | Medium | Auxiliary Min Stack ($O(1)$ `getMin`) |
| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/s-lc-167-two-sum-2.py`](top-100/s-lc-167-two-sum-2.py)<br>[`top-100/s-lc-167-two-sum-2.md`](top-100/s-lc-167-two-sum-2.md) | Medium | Two Pointers on Sorted Array ($O(1)$ space) |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-200.py`](luffy/38-lc-200.py) | Medium | Grid DFS / BFS (Sink Islands) |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-206.py`](luffy/15-lc-206.py) | Easy | Pointer Reversal (`prev`, `curr`, `next`) |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`42-lc-207.py`](luffy/42-lc-207.py) | Medium | Topological Sort (Kahn's BFS / DFS) |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/s-lc-209-minimum-size-subarry-sum.py`](top-100/s-lc-209-minimum-size-subarry-sum.py)<br>[`top-100/s-lc-209-minimum-size-subarry-sum.md`](top-100/s-lc-209-minimum-size-subarry-sum.md)<br>[`luffy/6-lc-209-minimum-size-subarray-sum.py`](luffy/6-lc-209-minimum-size-subarray-sum.py) | Medium | Dynamic Sliding Window ($O(n)$ time, $O(1)$ space) |
| **236** | Lowest Common Ancestor of Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-236.py`](luffy/27-lc-236.py) | Medium | Postorder DFS Traversal |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-394.py`](luffy/23-lc-394.py) | Medium | Dual Stack (Count Stack + Str Stack) |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-560-Subarray-Sum-equals-k`](luffy/11-lc-560-Subarray-Sum-equals-k) | Medium | Prefix Sum + Frequency Hash Map |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/s-lc-713.py`](top-100/s-lc-713.py)<br>[`top-100/s-lc-713.md`](top-100/s-lc-713.md) | Medium | Sliding Window & Subarray Counting ($O(n)$) |
| **994** | Rotting Oranges | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`luffy/40-lc-994.py`](luffy/40-lc-994.py) | Medium | Multi-source Breadth-First Search (BFS) |

---

## 📅 Daily Practice Track

Dedicated tracking index for daily practice problems and latest contest questions organized in [`daily-practice/`](daily-practice).

| # | Problem Title | LeetCode Link | Solutions & Notes | Difficulty | Pattern / Core Technique |
| :-: | :--- | :-: | :--- | :-: | :--- |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/s-lc-2029.py`](daily-practice/s-lc-2029.py)<br>[`daily-practice/s-lc-2029.md`](daily-practice/s-lc-2029.md)<br>[`daily-practice/leetcode_2029_stone_game_ix.md`](daily-practice/leetcode_2029_stone_game_ix.md) | Medium | Modulo Arithmetic / Game Theory |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/s-lc-3090.py`](daily-practice/s-lc-3090.py)<br>[`daily-practice/s-lc-3090.md`](daily-practice/s-lc-3090.md) | Easy | Sliding Window / Frequency Map |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/s-lc-3471.py`](daily-practice/s-lc-3471.py)<br>[`daily-practice/s-lc-3471.md`](daily-practice/s-lc-3471.md) | Easy | Fixed Sliding Window / Math |

---

## 5. Topic-Wise Curriculum & Problem Index

### 1. Arrays, Strings, Two Pointers & Sliding Window

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **1** | Two Sum | [LC 1](https://leetcode.com/problems/two-sum/) | [`2-lc-1-two-sum-lc.py`](luffy/2-lc-1-two-sum-lc.py) | Easy | Hash Map | Single-pass hash map storing complement `target - num`. |
| **3** | Longest Substring Without Repeating Characters | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`top-100/s-lc-3-longest-substring-without-repeating-characters.py`](top-100/s-lc-3-longest-substring-without-repeating-characters.py)<br>[`top-100/s-lc-3-longest-substring-without-repeating-characters.md`](top-100/s-lc-3-longest-substring-without-repeating-characters.md)<br>[`luffy/4-lc-3-longest-substring-without-repeating-characters.py`](luffy/4-lc-3-longest-substring-without-repeating-characters.py) | Medium | Sliding Window | Maintain set/dict window; contract left pointer when duplicate seen (`cnt[s[left]] -= 1`). |
| **11** | Container With Most Water | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/s-lc-11-contain-with-most-water.py`](top-100/s-lc-11-contain-with-most-water.py)<br>[`top-100/s-lc-11-contain-with-most-water.md`](top-100/s-lc-11-contain-with-most-water.md) | Medium | Two Pointers (Left/Right) | Move the pointer pointing to the shorter line to potentially maximize area. |
| **15** | 3Sum | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/s-lc-15-3-sum.py`](top-100/s-lc-15-3-sum.py)<br>[`top-100/s-lc-15-3-sum.md`](top-100/s-lc-15-3-sum.md) | Medium | Two Pointers / Extreme Pruning | Sort array; fix anchor $nums[i]$; 2-way extreme pruning (min-sum break, max-sum continue) & deduplication. |
| **26** | Remove Duplicates from Sorted Array | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`5-lc-26-remove-duplicates-from-sorted-array.py`](luffy/5-lc-26-remove-duplicates-from-sorted-array.py) | Easy | Two Pointers (Slow/Fast) | Overwrite duplicate elements in-place with slow pointer. |
| **42** | Trapping Rain Water | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/s-lc-42-trapping-rain-water.py`](top-100/s-lc-42-trapping-rain-water.py)<br>[`top-100/s-lc-42-trapping-rain-water.md`](top-100/s-lc-42-trapping-rain-water.md) | Hard | Two Pointers / Pre-Suf Max | Maintain `pre_max` and `suf_max` or two-pointer inward sweep to trap water. |
| **59** | Spiral Matrix II | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`8-lc-59-spiral-martix.py`](luffy/8-lc-59-spiral-martix.py)<br>[`9-lc-59-spiral-martx-2.py`](luffy/9-lc-59-spiral-martx-2.py) | Medium | Matrix Simulation | Layer-by-layer traversal with boundary tracking (top, bottom, left, right). |
| **167** | Two Sum II - Input Array Is Sorted | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/s-lc-167-two-sum-2.py`](top-100/s-lc-167-two-sum-2.py)<br>[`top-100/s-lc-167-two-sum-2.md`](top-100/s-lc-167-two-sum-2.md)<br>[`3-lc-167-two-sum-2.py`](luffy/3-lc-167-two-sum-2.py) | Medium | Two Pointers (Left/Right) | Exploit sorted order; shrink search space based on sum vs target (1-based index). |
| **209** | Minimum Size Subarray Sum | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/s-lc-209-minimum-size-subarry-sum.py`](top-100/s-lc-209-minimum-size-subarry-sum.py)<br>[`top-100/s-lc-209-minimum-size-subarry-sum.md`](top-100/s-lc-209-minimum-size-subarry-sum.md)<br>[`6-lc-209-minimum-size-subarray-sum.py`](luffy/6-lc-209-minimum-size-subarray-sum.py) | Medium | Sliding Window | Expand right pointer to reach target sum, then shrink left to minimize window. |
| **713** | Subarray Product Less Than K | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/s-lc-713.py`](top-100/s-lc-713.py)<br>[`top-100/s-lc-713.md`](top-100/s-lc-713.md) | Medium | Sliding Window / Product Counting | Maintain window product `prod < k`; count valid subarrays ending at `right` with `right - left + 1`. |
| **3090** | Maximum Length Substring With at Most Two Occurrences | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/s-lc-3090.py`](daily-practice/s-lc-3090.py)<br>[`daily-practice/s-lc-3090.md`](daily-practice/s-lc-3090.md) | Easy | Sliding Window / Frequency Map | Window condition: maintain character frequency `<= 2`. |
| **3471** | Find the Largest Almost Missing Integer | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/s-lc-3471.py`](daily-practice/s-lc-3471.py)<br>[`daily-practice/s-lc-3471.md`](daily-practice/s-lc-3471.md) | Easy | Fixed Sliding Window / Hash Table | Slide fixed window of size $k$; count frequencies across distinct windows using set deduplication. |

---

### 2. Binary Search

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **704** | Binary Search | [LC 704](https://leetcode.com/problems/binary-search/) | [`7-lc-207-binary-search`](luffy/7-lc-207-binary-search) | Easy | Binary Search (Closed Interval) | `left <= right` with `mid = left + (right - left) // 2` to prevent overflow. |

---

### 3. Prefix Sum & Difference Arrays

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **303** | Range Sum Query - Immutable | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`10-lc-303-general-Range-sum-query-immutable.py`](luffy/10-lc-303-general-Range-sum-query-immutable.py)<br>[`10-lc-303-new.py`](luffy/10-lc-303-new.py)<br>[`10-pre-lc-303-practices.py`](luffy/10-pre-lc-303-practices.py) | Easy | Prefix Sum Array | Precompute cumulative sum array: `query(i, j) = prefix[j+1] - prefix[i]` in $O(1)$. |
| **560** | Subarray Sum Equals K | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`11-lc-560-Subarray-Sum-equals-k`](luffy/11-lc-560-Subarray-Sum-equals-k)<br>[`11-prefixSum-example.py`](luffy/11-prefixSum-example.py) | Medium | Prefix Sum + Hash Map | Track frequency of running prefix sums; check if `curr_sum - k` occurred. |
| **1109** | Corporate Flight Bookings | [LC 1109](https://leetcode.com/problems/corporate-flight-bookings/) | [`12-lc-1109.py`](luffy/12-lc-1109.py) | Medium | Difference Array | Range update $[l, r]$ by `diff[l] += val` and `diff[r+1] -= val`, then compute prefix sums. |

---

### 4. Intervals & In-Place Array Hashing

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **41** | First Missing Positive | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`14-lc-41.py`](luffy/14-lc-41.py) | Hard | Cyclic Sort / In-Place Hash | Place number `x` at index `x - 1` in $O(n)$ time and $O(1)$ extra space. |
| **56** | Merge Intervals | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`13-lc-56-merge.py`](luffy/13-lc-56-merge.py) | Medium | Interval Sorting | Sort intervals by start time and merge overlapping segments (`curr.start <= prev.end`). |

---

### 5. Linked Lists

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **21** | Merge Two Sorted Lists | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`16-lc-21.py`](luffy/16-lc-21.py) | Easy | Dummy Head + Two Pointers | Build new list with dummy head, appending the smaller node at each step. |
| **141** | Linked List Cycle | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`17-lc-141.py`](luffy/17-lc-141.py) | Easy | Floyd's Fast & Slow Pointers | Fast moves 2 steps, slow moves 1 step; collision indicates cycle. |
| **142** | Linked List Cycle II | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`18-lc-142.py`](luffy/18-lc-142.py) | Medium | Floyd's Algorithm + Math | Reset one pointer to head upon collision; both advance by 1 to meet at cycle entry. |
| **206** | Reverse Linked List | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`15-lc-206.py`](luffy/15-lc-206.py) | Easy | Iterative Pointer Reversal | Maintain `prev`, `curr`, and `next` pointers to reverse next links in-place. |

---

### 6. Stacks & Queues

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **20** | Valid Parentheses | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`19-lc-stack-1-brackets.py`](luffy/19-lc-stack-1-brackets.py)<br>[`20-lc-stack2.py`](luffy/20-lc-stack2.py) | Easy | Stack | Push opening brackets; pop and match corresponding closing bracket. |
| **155** | Min Stack | [LC 155](https://leetcode.com/problems/min-stack/) | [`21-lc-stack3-min-stack.py`](luffy/21-lc-stack3-min-stack.py) | Medium | Auxiliary Stack / Pair Stack | Track running minimum alongside each pushed value in $O(1)$. |
| **227** | Basic Calculator II | [LC 227](https://leetcode.com/problems/basic-calculator-ii/) | [`22-lc-227.py`](luffy/22-lc-227.py) | Medium | Stack / Parsing | Evaluate `*` and `/` immediately on top of stack; sum all values for `+` and `-`. |
| **232** | Implement Queue using Stacks | [LC 232](https://leetcode.com/problems/implement-queue-using-stacks/) | [`24-lc-232.py`](luffy/24-lc-232.py) | Easy | Two Stacks (`in_stack`, `out_stack`) | Amortized $O(1)$ pop/peek by transferring elements only when `out_stack` is empty. |
| **394** | Decode String | [LC 394](https://leetcode.com/problems/decode-string/) | [`23-lc-394.py`](luffy/23-lc-394.py) | Medium | Stack (Counts & Strings) | Push current string and multiplier onto stack when encountering `[`; pop on `]`. |

---

### 7. Trees & Binary Search Trees (BST)

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **94** | Binary Tree Inorder Traversal | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`25-lc-94-inorder.py`](luffy/25-lc-94-inorder.py) | Easy | DFS (Left, Root, Right) | Traversal yields sorted order for BSTs; implemented recursively & iteratively. |
| **98** | Validate Binary Search Tree | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`29-lc-98-sol-1.py`](luffy/29-lc-98-sol-1.py)<br>[`29-lc-98-sol-2.py`](luffy/29-lc-98-sol-2.py)<br>[`29-lc-98-sol-3.py`](luffy/29-lc-98-sol-3.py)<br>[`29-lc-98-sol-4.py`](luffy/29-lc-98-sol-4.py) | Medium | BST Range Bounds / Inorder | Validate node with strictly bounded $(min\_val, max\_val)$ interval. |
| **102** | Binary Tree Level Order Traversal | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`28-lc-102.py`](luffy/28-lc-102.py) | Medium | BFS (Queue) | Level-by-level queue traversal using `len(queue)` snapshots. |
| **104** | Maximum Depth of Binary Tree | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`26-lc-104py`](luffy/26-lc-104py) | Easy | DFS / Divide & Conquer | `max_depth = 1 + max(left_depth, right_depth)`. |
| **105** | Construct Binary Tree from Preorder and Inorder Traversal | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`30-lc-105.py`](luffy/30-lc-105.py) | Medium | Divide & Conquer / Hash Map | Preorder gives root; Inorder splits left and right subtrees. |
| **144** | Binary Tree Preorder Traversal | [LC 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [`25-lc-144.py`](luffy/25-lc-144.py) | Easy | DFS (Root, Left, Right) | Root processed before recursive traversal of subtrees. |
| **145** | Binary Tree Postorder Traversal | [LC 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [`25-lc-145.py`](luffy/25-lc-145.py) | Easy | DFS (Left, Right, Root) | Subtrees processed before processing the root node. |
| **236** | Lowest Common Ancestor of a Binary Tree | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`27-lc-236.py`](luffy/27-lc-236.py) | Medium | Postorder DFS | If both left and right return non-null, root is the LCA. |
| **Misc** | Advanced Tree Practices | — | [`25-advanced-.py`](luffy/25-advanced-.py) | Medium | Tree Patterns | Comprehensive tree construction and traversal utilities. |

---

### 8. Backtracking & Combinatorics

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **39** | Combination Sum | [LC 39](https://leetcode.com/problems/combination-sum/) | [`34-lc-39.py`](luffy/34-lc-39.py) | Medium | Backtracking (Unbounded Choice) | Pass `start_index` to allow reuse of the current element without duplicate permutations. |
| **40** | Combination Sum II | [LC 40](https://leetcode.com/problems/combination-sum-ii/) | [`35-lc-40.py`](luffy/35-lc-40.py) | Medium | Backtracking + Deduplication | Sort candidates; skip duplicate elements at the same tree depth (`if i > start and nums[i] == nums[i-1]: continue`). |
| **46** | Permutations | [LC 46](https://leetcode.com/problems/permutations/) | [`32-lc-46.py`](luffy/32-lc-46.py) | Medium | Backtracking (Used Array) | Maintain `used` boolean array or swap elements in-place to explore all orderings. |
| **77** | Combinations | [LC 77](https://leetcode.com/problems/combinations/) | [`31-lc-77.py`](luffy/31-lc-77.py) | Medium | Backtracking + Pruning | Prune search branch if remaining candidates are insufficient to reach size $k$. |
| **78** | Subsets | [LC 78](https://leetcode.com/problems/subsets/) | [`33-lc-78.py`](luffy/33-lc-78.py) | Medium | Backtracking / Cascading | Append path copy at every recursion step; explore subsets of length $0 \dots n$. |
| **79** | Word Search | [LC 79](https://leetcode.com/problems/word-search/) | [`37-lc-79.py`](luffy/37-lc-79.py) | Medium | 2D Grid DFS + Backtracking | Mark visited cells in-place (e.g. `'#'`); restore character on backtracking. |
| **131** | Palindrome Partitioning | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`36-lc-131.py`](luffy/36-lc-131.py) | Medium | Backtracking + Palindrome Check | Partition string at valid palindrome prefixes; recurse on remaining suffix. |

---

### 9. Graph Algorithms (DFS, BFS, Topological Sort)

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **130** | Surrounded Regions | [LC 130](https://leetcode.com/problems/surrounded-regions/) | [`39-lc-130.py`](luffy/39-lc-130.py) | Medium | Boundary Flood Fill (DFS/BFS) | Flood fill from outer border `'O'`s to protect them; flip remaining interior `'O'`s. |
| **200** | Number of Islands | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`38-lc-200.py`](luffy/38-lc-200.py) | Medium | Grid DFS / BFS (Sink Island) | Increment count upon finding `'1'`; recursively sink connected island to `'0'`. |
| **207** | Course Schedule | [LC 207](https://leetcode.com/problems/course-schedule/) | [`42-lc-207.py`](luffy/42-lc-207.py) | Medium | Topological Sort (Kahn's / DFS) | Detect cycles in directed graph using in-degrees (Kahn's BFS) or 3-state DFS. |
| **994** | Rotting Oranges | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`40-lc-994.py`](luffy/40-lc-994.py) | Medium | Multi-source BFS | Enqueue all initially rotten oranges; propagate minute by minute to adjacent fresh ones. |
| **1091** | Shortest Path in Binary Matrix | [LC 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [`41-lc-1091.py`](luffy/41-lc-1091.py) | Medium | 8-Directional BFS | Find shortest path in unweighted grid; BFS guarantees minimum distance. |

---

### 10. Dynamic Programming & Math / Game Theory

| # | Problem Title | LeetCode Link | Solution File | Difficulty | Core Technique | Key Takeaways / Notes |
| :-: | :--- | :-: | :--- | :-: | :--- | :--- |
| **53** | Maximum Subarray | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/s-lc-53-maxiumu-subarry.py`](top-100/s-lc-53-maxiumu-subarry.py)<br>[`top-100/s-lc-53-maxiumu-subarry.md`](top-100/s-lc-53-maxiumu-subarry.md) | Medium | Kadane's Algorithm / DP | `curr_max = max(num, curr_max + num)`; maintains maximum contiguous sum in $O(n)$. |
| **2029** | Stone Game IX | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/s-lc-2029.py`](daily-practice/s-lc-2029.py)<br>[`daily-practice/s-lc-2029.md`](daily-practice/s-lc-2029.md)<br>[`daily-practice/leetcode_2029_stone_game_ix.md`](daily-practice/leetcode_2029_stone_game_ix.md) | Medium | Modulo Arithmetic / Game Theory | Count residues modulo 3 ($c_0, c_1, c_2$); analyze winning conditions based on $c_0 \pmod 2$. |

---

### 11. Object-Oriented Programming (OOP) & Foundations

| # | Topic / Concept | Reference File | Difficulty | Core Concept | Description |
| :-: | :--- | :--- | :-: | :--- | :--- |
| **2235** | Add Two Integers | [`1-lc-2235.py`](luffy/1-lc-2235.py) | Easy | Basic Arithmetic | Python function syntax and return values. |
| **OOP** | Car Class & Inheritance | [`car_object-oriented-example.py`](luffy/car_object-oriented-example.py)<br>[`10-pre-main.py`](luffy/10-pre-main.py) | Easy | OOP Principles | Encapsulation, `__init__`, class methods, and object instantiation in Python. |

---

## 6. How to Run & Practice

### Running a Solution Locally
Execute any Python script directly using Python 3:

```bash
# Example: Run Two Sum solution (Luffy track)
python luffy/2-lc-1-two-sum-lc.py

# Example: Run 3Sum solution (Top 100 track)
python top-100/s-lc-15-3-sum.py

# Example: Run Two Sum II solution (Top 100 track)
python top-100/s-lc-167-two-sum-2.py

# Example: Run Minimum Size Subarray Sum solution (Top 100 track)
python top-100/s-lc-209-minimum-size-subarry-sum.py

# Example: Run Stone Game IX solution (Daily Practice track)
python daily-practice/s-lc-2029.py

# Example: Run Almost Missing Integer solution (Daily Practice track)
python daily-practice/s-lc-3471.py
```

### Adding New Solutions
When adding a new solution:
1. Place the Python solution script and Markdown notes in the relevant topic folder:
   - `top-100/` for LeetCode Top 100 Liked problems.
   - `daily-practice/` for daily challenges and contest problems.
   - `luffy/` for curriculum progression tracks.
2. Follow the naming convention: `<index>-lc-<problem_number>-<title>.py` or `s-lc-<problem_number>.py`.
3. Update the corresponding topic table in [README.md](README.md).


