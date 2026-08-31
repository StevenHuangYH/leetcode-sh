# Algorithmic Mastery Roadmap (5-Phase Curriculum)

This roadmap establishes the 5-phase progressive curriculum aligned with the **38-Node Compound Topology Graph** (`scripts/compiler/graph_builder.py`) and Labuladong's algorithmic mental models.

---

## Phase 1: Linear Foundations & Basic Operations (线性基石与核心操作)

Master contiguous memory buffers, pointer manipulations, range aggregations, and fundamental abstract data types (ADT).

### Topic 01: Array Operations (数组基础与原地操作)

┌─────────────────────────────────────────────────────────────┐
│ In-Place Modification: Fast/Slow Pointer Element Removal    │
├─────────────────────────────────────────────────────────────┤
│ • Slow pointer tracks boundary of valid retained elements.  │
│ • Fast pointer scans ahead, skipping target/duplicate items.│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 26** | Remove Duplicates from Sorted Array (删除有序数组中的重复项) | Easy | Array Operations | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/luffy/05-lc-0026-remove-duplicates-from-sorted-array.py) |
| **LC 27** | Remove Element (移除元素) | Easy | Array Operations | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0026-remove-duplicates-from-sorted-array.py) |
| **LC 283** | Move Zeroes (移动零) | Easy | Array Operations | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0283-move-zeroes.py) |

### Topic 02: Prefix Sum (前缀和与区间查询)

┌─────────────────────────────────────────────────────────────┐
│ Static Range Query: prefix[i] = prefix[i-1] + nums[i-1]     │
├─────────────────────────────────────────────────────────────┤
│ • Sum(i, j) = prefix[j + 1] - prefix[i] in O(1) time.       │
│ • Combine with Hash Map to solve Subarray Sum = K in O(N).  │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 303** | Range Sum Query - Immutable (区域和检索 - 数组不可变) | Easy | Prefix Sum | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0560-subarray-sum-equals-k.py) |
| **LC 560** | Subarray Sum Equals K (和为 K 的子数组) | Medium | Prefix Sum | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0560-subarray-sum-equals-k.py) |

### Topic 03: Difference Array (差分数组与频繁区间修改)

┌─────────────────────────────────────────────────────────────┐
│ Range Increment [i, j] += val: diff[i] += val, diff[j+1] -= │
├─────────────────────────────────────────────────────────────┤
│ • Converts O(N) range updates into O(1) boundary increments.│
│ • Recover original array via prefix sum accumulation.       │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 1109** | Corporate Flight Bookings (航班预订统计) | Medium | Difference Array | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0560-subarray-sum-equals-k.py) |
| **LC 1094** | Car Pooling (拼车) | Medium | Difference Array | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0560-subarray-sum-equals-k.py) |

### Topic 04: 2D Matrix (二维矩阵与原地变换)

┌─────────────────────────────────────────────────────────────┐
│ Matrix Geometry: Diagonal Reflection + Horizontal Reversal  │
├─────────────────────────────────────────────────────────────┤
│ • Clockwise 90° rotation = Transpose matrix + Reverse rows. │
│ • Spiral Matrix: Maintain 4 dynamic boundaries (U, D, L, R).│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 48** | Rotate Image (旋转图像) | Medium | 2D Matrix | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0048-rotate-image.py) |
| **LC 54** | Spiral Matrix (螺旋矩阵) | Medium | 2D Matrix | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0054-spiral-matrix.py) |
| **LC 73** | Set Matrix Zeroes (矩阵置零) | Medium | 2D Matrix | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0073-set-matrix-zeroes.py) |

### Topic 05: Linked List Foundations (单链表基石与虚拟头节点)

┌─────────────────────────────────────────────────────────────┐
│ Pointer Re-Linking: Dummy Head & In-Place Link Reversal     │
├─────────────────────────────────────────────────────────────┤
│ • Dummy head eliminates edge cases for head-node mutations. │
│ • Multi-pointer step tracking prevents memory leaks/cycles. │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 206** | Reverse Linked List (反转链表) | Easy | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0206-reverse-linked-list.py) |
| **LC 21** | Merge Two Sorted Lists (合并两个有序链表) | Easy | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0021-merge-two-sorted-lists.py) |
| **LC 237** | Delete Node in a Linked List (删除链表中的节点) | Medium | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0237-delete-node-in-a-linked-list.py) |
| **LC 83** | Remove Duplicates from Sorted List (删除排序链表中的重复元素) | Easy | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0083-remove-duplicates-from-sorted-list.py) |
| **LC 82** | Remove Duplicates from Sorted List II (删除排序链表中的重复元素 II) | Medium | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0082-remove-duplicates-from-sorted-list.py) |

### Topic 06: Circular Array (环形数组与循环队列)

┌─────────────────────────────────────────────────────────────┐
│ Modulo Arithmetic: index = (i + offset) % capacity          │
├─────────────────────────────────────────────────────────────┤
│ • Seamless circular buffering without memory re-allocation. │
│ • Distinguish empty vs full states via count or dummy slot. │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 189** | Rotate Array (轮转数组) | Medium | Circular Array | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0189-rotate-array.py) |

### Topic 07: Stack & Monotonic Queue (栈与单调结构)

┌─────────────────────────────────────────────────────────────┐
│ Monotonic Ordering: Maintain strictly increasing/decreasing │
├─────────────────────────────────────────────────────────────┤
│ • Monotonic Stack: Finds next greater / previous smaller.   │
│ • Monotonic Queue: Maintains max/min in dynamic window O(1).│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 20** | Valid Parentheses (有效的括号) | Easy | Stack & Queue | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0020-valid-parentheses.py) |
| **LC 155** | Min Stack (最小栈) | Medium | Stack & Queue | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0155-min-stack.py) |
| **LC 739** | Daily Temperatures (每日温度) | Medium | Monotonic Stack | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0739-daily-temperatures.py) |
| **LC 239** | Sliding Window Maximum (滑动窗口最大值) | Hard | Monotonic Queue | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0239-sliding-window-maximum.py) |

### Topic 08: Hashing & Design (哈希表与高级缓存设计)

┌─────────────────────────────────────────────────────────────┐
│ Dual Structure Composite: Hash Map + Doubly Linked List     │
├─────────────────────────────────────────────────────────────┤
│ • O(1) Key-Value lookup + O(1) dynamic node eviction order. │
│ • LRU (Least Recently Used) and LFU frequency ranking.      │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 1** | Two Sum (两数之和) | Easy | Hashing | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0001-two-sum.py) |
| **LC 146** | LRU Cache (LRU 缓存) | Medium | Design | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0146-lru-cache.py) |

---

## Phase 2: Two Pointers & Search Paradigms (双指针与搜索进阶)

Leverage mathematical monotonicity, window bounds, and binary search spaces.

### Topic 09: Two Pointers Collision (对撞指针与两数之和)

┌─────────────────────────────────────────────────────────────┐
│ Opposite Collision: Shrink search space based on monotonic sum │
├─────────────────────────────────────────────────────────────┤
│ • Left and right pointers start at boundaries and converge. │
│ • Eliminates sub-optimal candidate spaces in O(N) time.     │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 167** | Two Sum II - Input Array Is Sorted (两数之和 II) | Medium | Two Pointers | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py) |
| **LC 15** | 3Sum (三数之和) | Medium | Two Pointers | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0015-3sum.py) |
| **LC 11** | Container With Most Water (盛最多水的容器) | Medium | Two Pointers | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0011-container-with-most-water.py) |
| **LC 42** | Trapping Rain Water (接雨水) | Hard | Two Pointers | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0042-trapping-rain-water.py) |

### Topic 10: Sliding Window (滑动窗口与动态区间伸缩)

┌─────────────────────────────────────────────────────────────┐
│ Sliding Bounds: Expand right to satisfy, shrink left to optimize │
├─────────────────────────────────────────────────────────────┤
│ • window[char] counter records dynamic state.               │
│ • Monotonic right++ and left++ guarantees O(N) pass.        │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 3** | Longest Substring Without Repeating Characters (无重复字符的最长子串) | Medium | Sliding Window | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0003-longest-substring-without-repeating-characters.py) |
| **LC 76** | Minimum Window Substring (最小覆盖子串) | Hard | Sliding Window | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0076-minimum-window-substring.py) |
| **LC 438** | Find All Anagrams in a String (找到字符串中所有字母异位词) | Medium | Sliding Window | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0438-find-all-anagrams-in-a-string.py) |
| **LC 3090** | Maximum Length Substring With at Most Two Occurrences (每个字符最多出现两次的最长子字符串) | Easy | Sliding Window | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py) |

### Topic 11: Binary Search Variants (二分搜索与左右边界)

┌─────────────────────────────────────────────────────────────┐
│ Closed Interval [left, right]: mid = left + (right - left)/2 │
├─────────────────────────────────────────────────────────────┤
│ • Standard Target: nums[mid] == target -> return mid.       │
│ • Left Bound: nums[mid] >= target -> right = mid - 1.       │
│ • Right Bound: nums[mid] <= target -> left = mid + 1.       │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 704** | Binary Search (二分查找) | Easy | Binary Search | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0035-search-insert-position.py) |
| **LC 34** | Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置) | Medium | Binary Search | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py) |
| **LC 33** | Search in Rotated Sorted Array (搜索旋转排序数组) | Medium | Binary Search | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0033-search-in-rotated-sorted-array.py) |
| **LC 153** | Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值) | Medium | Binary Search | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py) |

### Topic 12: Randomized Algorithms (随机算法与水塘抽样)

┌─────────────────────────────────────────────────────────────┐
│ Reservoir Sampling: Pick k-th element with probability 1/k  │
├─────────────────────────────────────────────────────────────┤
│ • Handles dynamic unbounded data streams with equal chance. │
│ • Fisher-Yates shuffle achieves uniform permutation in O(N).│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 384** | Shuffle an Array (打乱数组) | Medium | Randomize | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0033-search-in-rotated-sorted-array.py) |

### Topic 13: Linked List Two Pointers (链表双指针与快慢指针)

┌─────────────────────────────────────────────────────────────┐
│ Floyd's Tortoise & Hare: 2k - k = n * cycle_length          │
├─────────────────────────────────────────────────────────────┤
│ • Fast advances 2 steps, Slow advances 1 step.              │
│ • Detects cycles, locates entry points, and finds midpoints.│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 876** | Middle of the Linked List (链表的中间结点) | Easy | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0876-middle-of-the-linked-list.py) |
| **LC 141** | Linked List Cycle (环形链表) | Easy | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0141-linked-list-cycle.py) |
| **LC 142** | Linked List Cycle II (环形链表 II) | Medium | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0142-linked-list-cycle-ii.py) |
| **LC 143** | Reorder List (重排链表) | Medium | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0143-reorder-list.py) |
| **LC 92** | Reverse Linked List II (反转链表 II) | Medium | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0092-reversed-linked-list-2.py) |
| **LC 25** | Reverse Nodes in k-Group (K 个一组翻转链表) | Hard | Linked List | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0025-reverse-nodes-in-k-group.py) |

---

## Phase 3: Tree Hierarchies & Level-Order Search (树形层次与层序图论)

Transition from discrete pointer nodes to recursive branching hierarchies and queue-driven graph wavefront expansions.

### Topic 14: Recursion Foundations (递归思维与数学归纳法)

┌─────────────────────────────────────────────────────────────┐
│ Recursive Contract: Base Case + Inductive Step              │
├─────────────────────────────────────────────────────────────┤
│ • Define exact function contract before implementing code.  │
│ • Trust the recursive call to return sub-tree solution.     │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 226** | Invert Binary Tree (翻转二叉树) | Easy | Recursion | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0226-invert-binary-tree.py) |

### Topic 15: Binary Tree Hierarchies (二叉树结构与三序遍历)

┌─────────────────────────────────────────────────────────────┐
│ Triple-Order Perspectives: Preorder / Inorder / Postorder   │
├─────────────────────────────────────────────────────────────┤
│ • Preorder: Top-down state transmission & tree cloning.     │
│ • Postorder: Bottom-up sub-tree aggregation (e.g. depth).   │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 104** | Maximum Depth of Binary Tree (二叉树的最大深度) | Easy | Binary Tree | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0104-maximum-depth-of-binary-tree.py) |
| **LC 100** | Same Tree (相同的树) | Easy | Binary Tree | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0100-same-tree.py) |
| **LC 110** | Balanced Binary Tree (平衡二叉树) | Easy | Binary Tree | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0110-balanced-binary-tree.py) |
| **LC 94** | Binary Tree Inorder Traversal (二叉树的中序遍历) | Easy | Binary Tree | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0094-binary-tree-inorder-traversal.py) |

### Topic 16: Level-Order Traversal (层序遍历与逐层扫描)

┌─────────────────────────────────────────────────────────────┐
│ Queue Layer Scanning: sz = queue.size() fixes layer boundary │
├─────────────────────────────────────────────────────────────┤
│ • FIFO Queue guarantees top-to-bottom and left-to-right.    │
│ • Layer size snapshot decouples layer height from children. │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 102** | Binary Tree Level Order Traversal (二叉树的层序遍历) | Medium | Level Traverse | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0102-binary-tree-level-order-traversal.py) |
| **LC 103** | Binary Tree Zigzag Level Order Traversal (二叉树的锯齿形层序遍历) | Medium | Level Traverse | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py) |
| **LC 199** | Binary Tree Right Side View (二叉树的右视图) | Medium | Level Traverse | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0199-binary-tree-right-side-view.py) |
| **LC 513** | Find Bottom Left Tree Value (找树左下角的值) | Medium | Level Traverse | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0513-find-bottom-left-tree-value.py) |

### Topic 17: Breadth-First Search (BFS 广度优先搜索与波纹扩散)

┌─────────────────────────────────────────────────────────────┐
│ Wavefront Expansion: visited set prevents redundant cycles   │
├─────────────────────────────────────────────────────────────┤
│ • Guarantees finding minimum steps in unweighted state graph.│
│ • Bidirectional BFS prunes search tree exponential growth. │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 752** | Open the Lock (打开转盘锁) | Medium | BFS | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0102-binary-tree-level-order-traversal.py) |

### Topic 18: Shortest Path & Dijkstra (加权最短路径与单源最短路)

┌─────────────────────────────────────────────────────────────┐
│ Dijkstra Algorithm: Priority Queue + distTo Relaxing Array  │
├─────────────────────────────────────────────────────────────┤
│ • Greedy selection of unvisited node with minimum distance. │
│ • distTo[v] = min(distTo[v], distTo[u] + weight(u, v)).     │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 743** | Network Delay Time (网络延迟时间) | Medium | Shortest Path | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0102-binary-tree-level-order-traversal.py) |

---

## Phase 4: Recursive Multi-Branching: Traversal vs Subproblem (递归分叉与两大认知视角)

Explore the dual perspectives of recursive algorithms: exhaustive state-space decision trees versus optimal overlapping subproblem decompositions.

### Topic 19: Backtracking & State Decision Trees (回溯算法与决策树穷举)

┌─────────────────────────────────────────────────────────────┐
│ Choose -> Explore -> Unchoose Paradigm                      │
├─────────────────────────────────────────────────────────────┤
│ • Iterate through candidates at current decision level.     │
│ • Mutate path state, recurse, then revert back (backtrack). │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 46** | Permutations (全排列) | Medium | Backtracking | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0046-permutations.py) |
| **LC 78** | Subsets (子集) | Medium | Backtracking | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0078-subsets.py) |
| **LC 39** | Combination Sum (组合总和) | Medium | Backtracking | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0039-combination-sum.py) |
| **LC 51** | N-Queens (N 皇后) | Hard | Backtracking | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0078-subsets.py) |
| **LC 131** | Palindrome Partitioning (分割回文串) | Medium | Backtracking | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0131-palindrome-partitioning.py) |

### Topic 20: Depth-First Search on Graphs (DFS 深度优先搜索与连通分量)

┌─────────────────────────────────────────────────────────────┐
│ Graph DFS: Flood fill, topological sort, and cycle check    │
├─────────────────────────────────────────────────────────────┤
│ • onPath array tracks current recursive call stack cycles.  │
│ • visited array prevents visiting same component twice.     │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 200** | Number of Islands (岛屿数量) | Medium | DFS | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0200-number-of-islands.py) |
| **LC 130** | Surrounded Regions (被围绕的区域) | Medium | DFS | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0200-number-of-islands.py) |

### Topic 21: Divide & Conquer (分治算法与子问题合并)

┌─────────────────────────────────────────────────────────────┐
│ Divide & Conquer: Break into disjoint subproblems & merge   │
├─────────────────────────────────────────────────────────────┤
│ • Merge Sort: Divide array in half, sort sub-arrays, merge. │
│ • Quick Select: Partition around pivot for O(N) K-th search.│
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 215** | Kth Largest Element in an Array (数组中的第 K 个最大元素) | Medium | Divide & Conquer | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0215-kth-largest-element-in-an-array.py) |
| **LC 148** | Sort List (排序链表) | Medium | Divide & Conquer | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0148-sort-list.py) |

### Topic 22: Dynamic Programming Foundations (动态规划状态转移与备忘录)

┌─────────────────────────────────────────────────────────────┐
│ DP Triad: Base Case + State Transitions + Memoization       │
├─────────────────────────────────────────────────────────────┤
│ • Overlapping Subproblems: Cache intermediate results.      │
│ • Optimal Substructure: Global optimum built from sub-opt.  │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 70** | Climbing Stairs (爬楼梯) | Easy | Dynamic Programming | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0070-climbing-stairs.py) |
| **LC 322** | Coin Change (零钱兑换) | Medium | Dynamic Programming | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0322-coin-change.py) |
| **LC 300** | Longest Increasing Subsequence (最长递增子序列) | Medium | Dynamic Programming | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0300-longest-increasing-subsequence.py) |
| **LC 1143** | Longest Common Subsequence (最长公共子序列) | Medium | Dynamic Programming | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-1143-longest-common-subsequence.py) |

### Topic 23: Math & Bit Manipulation (离散数学与位运算技巧)

┌─────────────────────────────────────────────────────────────┐
│ Bit Tricks: n & (n - 1) removes lowest set bit              │
├─────────────────────────────────────────────────────────────┤
│ • XOR property: a ^ a = 0, a ^ 0 = a for single element.   │
│ • Fast Exponentiation & Euclidean GCD algorithm.            │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 136** | Single Number (只出现一次的数字) | Easy | Math | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0136-single-number.py) |
| **LC 2029** | Stone Game IX (石子游戏 IX) | Medium | Math | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-2029-stone-game-ix.py) |

### Topic 24: Greedy Algorithms (贪心选择性质与无后效性)

┌─────────────────────────────────────────────────────────────┐
│ Greedy Paradigm: Local optimal choice yields global optimum │
├─────────────────────────────────────────────────────────────┤
│ • Interval Scheduling: Sort by end times to maximize jobs.  │
│ • Jump Game: Monotonically track furthest reachable index.  │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 55** | Jump Game (跳跃游戏) | Medium | Greedy | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0055-jump-game.py) |
| **LC 45** | Jump Game II (跳跃游戏 II) | Medium | Greedy | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0045-jump-game-ii.py) |

---

## Phase 5: Advanced Data Structures & Graph Theory (高阶拓扑与数据结构进阶)

Master specialized tree topologies, priority queues, prefix trees, and graph adjacency structures.

### Topic 25: Binary Search Tree (BST 属性与二叉搜索树操作)

┌─────────────────────────────────────────────────────────────┐
│ BST Invariant: Left.val < Root.val < Right.val              │
├─────────────────────────────────────────────────────────────┤
│ • Inorder traversal of BST yields strictly sorted sequence. │
│ • Logarithmic search, insertion, and deletion.              │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 98** | Validate Binary Search Tree (验证二叉搜索树) | Medium | BST | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0098-validate-binary-search-tree.py) |
| **LC 235** | Lowest Common Ancestor of a BST (二叉搜索树的最近公共祖先) | Medium | BST | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py) |

### Topic 26: Priority Queue & Binary Heap (堆与优先级队列)

┌─────────────────────────────────────────────────────────────┐
│ Heap Invariant: Parent <= Children (Min-Heap)               │
├─────────────────────────────────────────────────────────────┤
│ • Complete binary tree stored in contiguous 1D array.       │
│ • Swim (Shift Up) and Sink (Shift Down) in O(log N) time.   │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 295** | Find Median from Data Stream (数据流的中位数) | Hard | Heap | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0295-find-median-from-data-stream.py) |
| **LC 347** | Top K Frequent Elements (前 K 个高频元素) | Medium | Heap | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0347-top-k-frequent-elements.py) |

### Topic 27: Trie Prefix Tree (前缀树与字典树高效检索)

┌─────────────────────────────────────────────────────────────┐
│ Trie Multi-Way Tree: Children dictionary / array on edges   │
├─────────────────────────────────────────────────────────────┤
│ • O(L) prefix matching, auto-completion, and wildcards.     │
│ • Shared string prefix paths save memory and search time.   │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| :--- | :--- | :--- | :--- | :--- |
| **LC 208** | Implement Trie (Prefix Tree) (实现 Trie 前缀树) | Medium | Trie | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0208-implement-trie-prefix-tree.py) |

### Topic 28: Graph Adjacency & Topological Sort (图论表达与拓扑排序)

┌─────────────────────────────────────────────────────────────┐
│ Topological Sort: In-degree Queue (Kahn) or DFS Postorder   │
├─────────────────────────────────────────────────────────────┤
│ • Represents dependencies in Directed Acyclic Graph (DAG).  │
│ • Union-Find (Disjoint Set) manages connected components.   │
└─────────────────────────────────────────────────────────────┘

| Problem | Title | Difficulty | Category | Solution Link |
| **LC 207** | Course Schedule (课程表) | Medium | Graph | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0207-course-schedule.py) |
| **LC 210** | Course Schedule II (课程表 II) | Medium | Graph | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0210-course-schedule-ii.py) |
| **LC 399** | Evaluate Division (除法求值) | Medium | Graph | [Python](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0399-evaluate-division.py) |
