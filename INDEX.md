# LeetCode Master Problem Database & Knowledge Index (INDEX.md)

Welcome to the **Master Problem Database** for the LeetCode repository. This index organizes all implemented solutions, companion deep-dive markdown notes, core algorithmic patterns, and complexities across **Top 100 Liked**, **Daily Practice**, and **Luffy Curriculum** tracks.

---

## 📊 Summary Statistics

| Category / Track | Solved Problems | Easy | Medium | Hard | Notes Available |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **🔥 Top 100 Liked Track** | 33 | 11 | 20 | 2 | 100% |
| **📅 Daily Practice Track** | 3 | 2 | 1 | 0 | 100% |
| **📚 Luffy Structured Curriculum (01-42)** | 42 | 15 | 25 | 2 | Core Topics |
| **Total Unique Solutions** | **52+** | **17** | **33** | **2** | **Full Coverage** |

---

## 🗂️ Master Problem Table

| # | Problem Title | Difficulty | Track | LeetCode Link | Python Solution | Detailed Walkthrough | Core Technique / Pattern | Time / Space |
| :-: | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| **1** | Two Sum | Easy | Top 100 / Luffy | [LC 1](https://leetcode.com/problems/two-sum/) | [`luffy/2-lc-1-two-sum-lc.py`](luffy/2-lc-1-two-sum-lc.py) | — | Hash Map (Complement) | $\mathcal{O}(n) / \mathcal{O}(n)$ |
| **3** | Longest Substring Without Repeating Characters | Medium | Top 100 / Luffy | [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [`luffy/4-lc-3-longest-substring-without-repeating-characters.py`](luffy/4-lc-3-longest-substring-without-repeating-characters.py) | — | Dynamic Sliding Window | $\mathcal{O}(n) / \mathcal{O}(|\Sigma|)$ |
| **11** | Container With Most Water | Medium | Top 100 | [LC 11](https://leetcode.com/problems/container-with-most-water/) | [`top-100/s-lc-11-contain-with-most-water.py`](top-100/s-lc-11-contain-with-most-water.py) | [`top-100/s-lc-11-contain-with-most-water.md`](top-100/s-lc-11-contain-with-most-water.md) | Two Pointers (Greedy Shorter Line) | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **15** | 3Sum | Medium | Top 100 | [LC 15](https://leetcode.com/problems/3sum/) | [`top-100/s-lc-15-3-sum.py`](top-100/s-lc-15-3-sum.py) | [`top-100/s-lc-15-3-sum.md`](top-100/s-lc-15-3-sum.md) | Sort + Two Pointers + 2-Way Extreme Pruning | $\mathcal{O}(n^2) / \mathcal{O}(1)$ |
| **20** | Valid Parentheses | Easy | Top 100 / Luffy | [LC 20](https://leetcode.com/problems/valid-parentheses/) | [`luffy/19-lc-stack-1-brackets.py`](luffy/19-lc-stack-1-brackets.py) | — | Stack Bracket Matching | $\mathcal{O}(n) / \mathcal{O}(n)$ |
| **21** | Merge Two Sorted Lists | Easy | Top 100 / Luffy | [LC 21](https://leetcode.com/problems/merge-two-sorted-lists/) | [`luffy/16-lc-21.py`](luffy/16-lc-21.py) | — | Dummy Head + Two Pointers | $\mathcal{O}(n+m) / \mathcal{O}(1)$ |
| **26** | Remove Duplicates from Sorted Array | Easy | Top 100 / Luffy | [LC 26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [`luffy/5-lc-26-remove-duplicates-from-sorted-array.py`](luffy/5-lc-26-remove-duplicates-from-sorted-array.py) | — | Slow & Fast Two Pointers | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **39** | Combination Sum | Medium | Top 100 / Luffy | [LC 39](https://leetcode.com/problems/combination-sum/) | [`luffy/34-lc-39.py`](luffy/34-lc-39.py) | — | Backtracking (Unbounded Choice) | $\mathcal{O}(2^t) / \mathcal{O}(t)$ |
| **40** | Combination Sum II | Medium | Luffy | [LC 40](https://leetcode.com/problems/combination-sum-ii/) | [`luffy/35-lc-40.py`](luffy/35-lc-40.py) | — | Backtracking + Deduplication | $\mathcal{O}(2^n) / \mathcal{O}(n)$ |
| **41** | First Missing Positive | Hard | Top 100 / Luffy | [LC 41](https://leetcode.com/problems/first-missing-positive/) | [`luffy/14-lc-41.py`](luffy/14-lc-41.py) | — | Cyclic Sort / In-Place Hashing | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **42** | Trapping Rain Water | Hard | Top 100 | [LC 42](https://leetcode.com/problems/trapping-rain-water/) | [`top-100/s-lc-42-trapping-rain-water.py`](top-100/s-lc-42-trapping-rain-water.py) | [`top-100/s-lc-42-trapping-rain-water.md`](top-100/s-lc-42-trapping-rain-water.md) | Inward Two Pointers Sweep | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **46** | Permutations | Medium | Top 100 / Luffy | [LC 46](https://leetcode.com/problems/permutations/) | [`luffy/32-lc-46.py`](luffy/32-lc-46.py) | — | Backtracking (Used Array / Swap) | $\mathcal{O}(n!) / \mathcal{O}(n)$ |
| **53** | Maximum Subarray | Medium | Top 100 | [LC 53](https://leetcode.com/problems/maximum-subarray/) | [`top-100/s-lc-53-maxiumu-subarry.py`](top-100/s-lc-53-maxiumu-subarry.py) | [`top-100/s-lc-53-maxiumu-subarry.md`](top-100/s-lc-53-maxiumu-subarry.md) | Kadane's Algorithm / DP | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **56** | Merge Intervals | Medium | Top 100 / Luffy | [LC 56](https://leetcode.com/problems/merge-intervals/) | [`luffy/13-lc-56-merge.py`](luffy/13-lc-56-merge.py) | — | Interval Sorting & Sweep | $\mathcal{O}(n \log n) / \mathcal{O}(n)$ |
| **59** | Spiral Matrix II | Medium | Luffy | [LC 59](https://leetcode.com/problems/spiral-matrix-ii/) | [`luffy/8-lc-59-spiral-martix.py`](luffy/8-lc-59-spiral-martix.py) | — | Boundary Layer Simulation | $\mathcal{O}(n^2) / \mathcal{O}(1)$ |
| **77** | Combinations | Medium | Luffy | [LC 77](https://leetcode.com/problems/combinations/) | [`luffy/31-lc-77.py`](luffy/31-lc-77.py) | — | Backtracking + Search Pruning | $\mathcal{O}(C_n^k) / \mathcal{O}(k)$ |
| **78** | Subsets | Medium | Top 100 / Luffy | [LC 78](https://leetcode.com/problems/subsets/) | [`luffy/33-lc-78.py`](luffy/33-lc-78.py) | — | Backtracking / Cascading | $\mathcal{O}(2^n) / \mathcal{O}(n)$ |
| **79** | Word Search | Medium | Top 100 / Luffy | [LC 79](https://leetcode.com/problems/word-search/) | [`luffy/37-lc-79.py`](luffy/37-lc-79.py) | — | 2D Grid DFS + Backtracking | $\mathcal{O}(m \cdot n \cdot 3^L) / \mathcal{O}(L)$ |
| **94** | Binary Tree Inorder Traversal | Easy | Top 100 / Luffy | [LC 94](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [`luffy/25-lc-94-inorder.py`](luffy/25-lc-94-inorder.py) | — | DFS Inorder (Left-Root-Right) | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **98** | Validate Binary Search Tree | Medium | Top 100 / Luffy | [LC 98](https://leetcode.com/problems/validate-binary-search-tree/) | [`luffy/29-lc-98-sol-1.py`](luffy/29-lc-98-sol-1.py) | — | BST Range Bounds $(min, max)$ | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **102** | Binary Tree Level Order Traversal | Medium | Top 100 / Luffy | [LC 102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [`luffy/28-lc-102.py`](luffy/28-lc-102.py) | — | BFS Queue Level-by-Level | $\mathcal{O}(n) / \mathcal{O}(w)$ |
| **104** | Maximum Depth of Binary Tree | Easy | Top 100 / Luffy | [LC 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [`luffy/26-lc-104py`](luffy/26-lc-104py) | — | Divide & Conquer / DFS | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **105** | Construct Tree from Pre & Inorder | Medium | Top 100 / Luffy | [LC 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | [`luffy/30-lc-105.py`](luffy/30-lc-105.py) | — | Preorder Root + Inorder Subtree Splitting | $\mathcal{O}(n) / \mathcal{O}(n)$ |
| **130** | Surrounded Regions | Medium | Luffy | [LC 130](https://leetcode.com/problems/surrounded-regions/) | [`luffy/39-lc-130.py`](luffy/39-lc-130.py) | — | Boundary Flood Fill (DFS) | $\mathcal{O}(m \cdot n) / \mathcal{O}(m \cdot n)$ |
| **131** | Palindrome Partitioning | Medium | Top 100 / Luffy | [LC 131](https://leetcode.com/problems/palindrome-partitioning/) | [`luffy/36-lc-131.py`](luffy/36-lc-131.py) | — | Backtracking + Palindrome Verification | $\mathcal{O}(n \cdot 2^n) / \mathcal{O}(n)$ |
| **141** | Linked List Cycle | Easy | Top 100 / Luffy | [LC 141](https://leetcode.com/problems/linked-list-cycle/) | [`luffy/17-lc-141.py`](luffy/17-lc-141.py) | — | Floyd's Fast & Slow Pointers | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **142** | Linked List Cycle II | Medium | Top 100 / Luffy | [LC 142](https://leetcode.com/problems/linked-list-cycle-ii/) | [`luffy/18-lc-142.py`](luffy/18-lc-142.py) | — | Fast/Slow Pointers + Cycle Entry Math | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **144** | Binary Tree Preorder Traversal | Easy | Luffy | [LC 144](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [`luffy/25-lc-144.py`](luffy/25-lc-144.py) | — | DFS Preorder (Root-Left-Right) | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **145** | Binary Tree Postorder Traversal | Easy | Luffy | [LC 145](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [`luffy/25-lc-145.py`](luffy/25-lc-145.py) | — | DFS Postorder (Left-Right-Root) | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **155** | Min Stack | Medium | Top 100 / Luffy | [LC 155](https://leetcode.com/problems/min-stack/) | [`luffy/21-lc-stack3-min -stack.py`](luffy/21-lc-stack3-min%20-stack.py) | — | Auxiliary Min Stack | $\mathcal{O}(1) / \mathcal{O}(n)$ |
| **167** | Two Sum II - Input Array Is Sorted | Medium | Top 100 / Luffy | [LC 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [`top-100/s-lc-167-two-sum-2.py`](top-100/s-lc-167-two-sum-2.py) | [`top-100/s-lc-167-two-sum-2.md`](top-100/s-lc-167-two-sum-2.md) | Sorted Array Inward Two Pointers | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **200** | Number of Islands | Medium | Top 100 / Luffy | [LC 200](https://leetcode.com/problems/number-of-islands/) | [`luffy/38-lc-200.py`](luffy/38-lc-200.py) | — | 2D Grid Sink Islands (DFS / BFS) | $\mathcal{O}(m \cdot n) / \mathcal{O}(m \cdot n)$ |
| **206** | Reverse Linked List | Easy | Top 100 / Luffy | [LC 206](https://leetcode.com/problems/reverse-linked-list/) | [`luffy/15-lc-206.py`](luffy/15-lc-206.py) | — | 3-Pointer Link Reversal (`prev, curr, nxt`) | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **207** | Course Schedule | Medium | Top 100 / Luffy | [LC 207](https://leetcode.com/problems/course-schedule/) | [`luffy/42-lc-207.py`](luffy/42-lc-207.py) | — | Topological Sort (Kahn's BFS / DFS) | $\mathcal{O}(V + E) / \mathcal{O}(V + E)$ |
| **209** | Minimum Size Subarray Sum | Medium | Top 100 / Luffy | [LC 209](https://leetcode.com/problems/minimum-size-subarray-sum/) | [`top-100/s-lc-209-minimum-size-subarry-sum.py`](top-100/s-lc-209-minimum-size-subarry-sum.py) | [`top-100/s-lc-209-minimum-size-subarry-sum.md`](top-100/s-lc-209-minimum-size-subarry-sum.md) | Dynamic Sliding Window | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **227** | Basic Calculator II | Medium | Luffy | [LC 227](https://leetcode.com/problems/basic-calculator-ii/) | [`luffy/22-lc-227.py`](luffy/22-lc-227.py) | — | Stack Precedence Parsing | $\mathcal{O}(n) / \mathcal{O}(n)$ |
| **232** | Implement Queue using Stacks | Easy | Luffy | [LC 232](https://leetcode.com/problems/implement-queue-using-stacks/) | [`luffy/24-lc-232.py`](luffy/24-lc-232.py) | — | Dual Stack (`in_stack, out_stack`) | Amortized $\mathcal{O}(1) / \mathcal{O}(n)$ |
| **236** | Lowest Common Ancestor of Binary Tree | Medium | Top 100 / Luffy | [LC 236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [`luffy/27-lc-236.py`](luffy/27-lc-236.py) | — | Postorder DFS Traversal | $\mathcal{O}(n) / \mathcal{O}(h)$ |
| **303** | Range Sum Query - Immutable | Easy | Luffy | [LC 303](https://leetcode.com/problems/range-sum-query-immutable/) | [`luffy/10-lc-303-general-Range-sum-query-immutable.py`](luffy/10-lc-303-general-Range-sum-query-immutable.py) | — | 1D Prefix Sum Array | $\mathcal{O}(1) 	ext{ query} / \mathcal{O}(n)$ |
| **394** | Decode String | Medium | Top 100 / Luffy | [LC 394](https://leetcode.com/problems/decode-string/) | [`luffy/23-lc-394.py`](luffy/23-lc-394.py) | — | Dual Stack (Count Stack + Str Stack) | $\mathcal{O}(N) / \mathcal{O}(N)$ |
| **560** | Subarray Sum Equals K | Medium | Top 100 / Luffy | [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/) | [`luffy/11-lc-560-Subarray-Sum-equals-k`](luffy/11-lc-560-Subarray-Sum-equals-k) | — | Prefix Sum + Hash Map | $\mathcal{O}(n) / \mathcal{O}(n)$ |
| **704** | Binary Search | Easy | Luffy | [LC 704](https://leetcode.com/problems/binary-search/) | [`luffy/7-lc-207-binary-search`](luffy/7-lc-207-binary-search) | — | Closed Interval Binary Search `[l, r]` | $\mathcal{O}(\log n) / \mathcal{O}(1)$ |
| **713** | Subarray Product Less Than K | Medium | Top 100 | [LC 713](https://leetcode.com/problems/subarray-product-less-than-k/) | [`top-100/s-lc-713.py`](top-100/s-lc-713.py) | [`top-100/s-lc-713.md`](top-100/s-lc-713.md) | Sliding Window & Contiguous Subarray Counting | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **994** | Rotting Oranges | Medium | Top 100 / Luffy | [LC 994](https://leetcode.com/problems/rotting-oranges/) | [`luffy/40-lc-994.py`](luffy/40-lc-994.py) | — | Multi-source BFS Queue | $\mathcal{O}(m \cdot n) / \mathcal{O}(m \cdot n)$ |
| **1091** | Shortest Path in Binary Matrix | Medium | Luffy | [LC 1091](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [`luffy/41-lc-1091.py`](luffy/41-lc-1091.py) | — | 8-Directional Grid BFS | $\mathcal{O}(n^2) / \mathcal{O}(n^2)$ |
| **1109** | Corporate Flight Bookings | Medium | Luffy | [LC 1109](https://leetcode.com/problems/corporate-flight-bookings/) | [`luffy/12-lc-1109.py`](luffy/12-lc-1109.py) | — | 1D Difference Array | $\mathcal{O}(n + m) / \mathcal{O}(n)$ |
| **2029** | Stone Game IX | Medium | Daily Track | [LC 2029](https://leetcode.com/problems/stone-game-ix/) | [`daily-practice/s-lc-2029.py`](daily-practice/s-lc-2029.py) | [`daily-practice/s-lc-2029.md`](daily-practice/s-lc-2029.md) | Modulo 3 Arithmetic / Game Theory | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **2235** | Add Two Integers | Easy | Luffy | [LC 2235](https://leetcode.com/problems/add-two-integers/) | [`luffy/1-lc-2235.py`](luffy/1-lc-2235.py) | — | Basic Arithmetic / Python Syntax | $\mathcal{O}(1) / \mathcal{O}(1)$ |
| **3090** | Maximum Length Substring With at Most Two Occurrences | Easy | Daily Track | [LC 3090](https://leetcode.com/problems/maximum-length-substring-with-at-most-two-occurrences/) | [`daily-practice/s-lc-3090.py`](daily-practice/s-lc-3090.py) | [`daily-practice/s-lc-3090.md`](daily-practice/s-lc-3090.md) | Dynamic Sliding Window / Frequency Map | $\mathcal{O}(n) / \mathcal{O}(1)$ |
| **3471** | Find the Largest Almost Missing Integer | Easy | Daily Track | [LC 3471](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) | [`daily-practice/s-lc-3471.py`](daily-practice/s-lc-3471.py) | [`daily-practice/s-lc-3471.md`](daily-practice/s-lc-3471.md) | Fixed-size Window + Frequency Hashing | $\mathcal{O}(n) / \mathcal{O}(n)$ |

---

## 🎯 Quick Navigation by Pattern

* **Sliding Window**: LC 3, LC 209, LC 713, LC 3090, LC 3471
* **Two Pointers**: LC 11, LC 15, LC 26, LC 42, LC 167
* **Prefix Sum & Difference**: LC 303, LC 560, LC 1109
* **In-Place Hashing & Intervals**: LC 41, LC 56
* **Linked Lists**: LC 21, LC 141, LC 142, LC 206
* **Stacks & Queues**: LC 20, LC 155, LC 227, LC 232, LC 394
* **Trees & BST**: LC 94, LC 98, LC 102, LC 104, LC 105, LC 144, LC 145, LC 236
* **Backtracking**: LC 39, LC 40, LC 46, LC 77, LC 78, LC 79, LC 131
* **Graph Algorithms**: LC 130, LC 200, LC 207, LC 994, LC 1091
* **Math & Game Theory**: LC 2029
