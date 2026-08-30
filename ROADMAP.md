# 算法刷题全景路线图 (LeetCode Algorithm Master Roadmap)

> **算法刷题全景路线图与核心解题框架体系全景图谱**  
> 本指南系统整理了仓库中所有已实现的 **187+ 题目、配套 Python 源码与 7 节标准题解笔记**，按照从基石到进阶的认知规律构建 5 大阶段、12 个核心专题。

## 三大核心能力支柱 (Three Pillars of Algorithmic Mastery)

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ 🏛️ 算法思维三大元支柱 (Three Meta-Pillars)                                              │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Core Linear Structures & Array Techniques (线性结构与连续内存优化)                   │
│    • 覆盖阶段：Phase 1 (线性结构与双指针) + Phase 2 (经典二分与极限搜索)                │
│    • 核心考点：前缀和、差分、快慢/对撞双指针、滑动窗口、红蓝二分染色法、单调栈/队列与哈希表 │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Non-Linear Architectures & Tree Hierarchies (非线性架构与树状层级)                   │
│    • 覆盖阶段：Phase 3 (树形结构与递归本原)                                             │
│    • 核心考点：单向/双向链表、二叉树/BST 遍历、堆与优先队列、Trie 前缀树、图论遍历与状态机 │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Search Algorithms & Dynamic Problem-Solving Paradigms (搜索算法与动态规划范式)       │
│    • 覆盖阶段：Phase 4 (搜索与回溯穷举) + Phase 5 (动态规划与进阶算法)                  │
│    • 核心考点：BFS 最短路、DFS/回溯状态空间剪枝、分治降维、动态规划状态转移与贪心数学逻辑 │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 全景知识拓扑与学习路线 (Master Topology Map)

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                 算法通关核心总路线图                                    │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                             │
      ┌──────────────────────────────────────┴──────────────────────────────────────┐
      ▼                                                                             ▼
┌───────────────────────────────┐                             ┌───────────────────────────────┐
│ 【Phase 1】线性结构与双指针   │                             │ 【Phase 2】经典二分与极限搜索 │
├───────────────────────────────┤                             ├───────────────────────────────┤
│ • 01 数组与哈希查找           │                             │ • 05 二分查找与红蓝染色法     │
│ • 02 双指针与滑动窗口         │                             │ • 06 二分答案与单调性判定     │
│ • 03 单链表穿针引线与快慢指针 │                             └───────────────┬───────────────┘
│ • 04 栈与队列、单调栈         │                                             │
└──────────────┬────────────────┘                                             │
               │                                                              │
               └──────────────────────────────┬───────────────────────────────┘
                                              ▼
                              ┌───────────────────────────────┐
                              │ 【Phase 3】树形结构与递归本原 │
                              ├───────────────────────────────┤
                              │ • 07 二叉树与递归分治 (DFS)   │
                              │ • 08 广度优先搜索与层序 (BFS) │
                              │ • 09 二叉搜索树性质与操作     │
                              └───────────────┬───────────────┘
                                              │
               ┌──────────────────────────────┴───────────────────────────────┐
               ▼                                                             ▼
┌───────────────────────────────┐                             ┌───────────────────────────────┐
│ 【Phase 4】暴力搜索与回溯算法 │                             │ 【Phase 5】动态规划与进阶算法 │
├───────────────────────────────┤                             ├───────────────────────────────┤
│ • 10 回溯三问模型与决策树     │                             │ • 11 动态规划核心与子问题递推 │
│   (子集/组合/排列/分割/网格)  │                             │ • 12 图论拓扑排序与博弈数论   │
└───────────────────────────────┘                             └───────────────────────────────┘
```

---

## 阶段目录与核心专题索引

- [Phase 1: 线性结构与双指针基石](#phase-1-线性结构与双指针基石)
  - [Topic 1: 数组与哈希查找 (Array, Prefix Sum & Difference Array)](#topic-1-数组与哈希查找)
  - [Topic 2: 双指针与滑动窗口 (Two Pointers & Sliding Window)](#topic-2-双指针与滑动窗口)
  - [Topic 3: 单链表穿针引线与快慢指针 (Linked List In-Place Mastery)](#topic-3-单链表穿针引线与快慢指针)
  - [Topic 4: 栈与队列、单调栈 (Stack, Queue & Monotonic Stack)](#topic-4-栈与队列单调栈)
- [Phase 2: 经典二分与极限搜索](#phase-2-经典二分与极限搜索)
  - [Topic 5: 二分查找与红蓝染色法 (Binary Search & Red-Blue Framework)](#topic-5-二分查找与红蓝染色法)
  - [Topic 6: 二分答案与单调性判定 (Binary Search on Answer)](#topic-6-二分答案与单调性判定)
- [Phase 3: 树形结构与递归本原](#phase-3-树形结构与递归本原)
  - [Topic 7: 二叉树与递归分治 (Binary Tree DFS & Divide-and-Conquer)](#topic-7-二叉树与递归分治)
  - [Topic 8: 广度优先搜索与层序遍历 (Binary Tree BFS & Level Order)](#topic-8-广度优先搜索与层序遍历)
  - [Topic 9: 二叉搜索树性质与操作 (Binary Search Tree BST)](#topic-9-二叉搜索树性质与操作)
- [Phase 4: 暴力搜索与回溯算法](#phase-4-暴力搜索与回溯算法)
  - [Topic 10: 回溯三问模型与决策树 (Backtracking & Search Trees)](#topic-10-回溯三问模型与决策树)
- [Phase 5: 动态规划与进阶算法](#phase-5-动态规划与进阶算法)
  - [Topic 11: 动态规划核心与子问题递推 (Dynamic Programming Foundations)](#topic-11-动态规划核心与子问题递推)
  - [Topic 12: 图论拓扑排序与博弈数论 (Graph Topology & Game Theory)](#topic-12-图论拓扑排序与博弈数论)

---

## Phase 1: 线性结构与双指针基石

### Topic 1: 数组与哈希查找

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 两数之和哈希映射: 边遍历边记录 complement = target - num。                │
│ 2. 前缀和数组: s[i+1] = s[i] + nums[i]，区间 [l, r] 和为 s[r+1] - s[l]。   │
│ 3. 差分数组: 区间 [l, r] 增加 x -> diff[l] += x; diff[r+1] -= x。           │
│ 4. 原地哈希 / 循环排序: 满足 1 <= nums[i] <= n 时，将 nums[i] 放置在下标    │
│    nums[i] - 1 处，以 O(1) 空间检测缺失正数。                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 1** | Two Sum (两数之和) | Easy | 哈希表配对 | [`luffy/02-lc-0001.py`](luffy/02-lc-0001-two-sum.py) · [`luffy/02-lc-0001.md`](luffy/02-lc-0001-two-sum.md) |
| **LC 303** | Range Sum Query (区域和检索) | Easy | 前缀和原语 | [`luffy/10-lc-0303.py`](luffy/10-lc-0303-range-sum-query-immutable.py) · [`luffy/10-lc-0303.md`](luffy/10-lc-0303-range-sum-query-immutable.md) |
| **LC 560** | Subarray Sum Equals K (和为 K 的子数组) | Medium | 前缀和 + 哈希 | [`luffy/11-lc-0560.py`](luffy/11-lc-0560-subarray-sum-equals-k.py) · [`luffy/11-lc-0560.md`](luffy/11-lc-0560-subarray-sum-equals-k.md) |
| **LC 1109** | Corporate Flight Bookings (航班预订) | Medium | 差分数组 | [`luffy/12-lc-1109.py`](luffy/12-lc-1109-corporate-flight-bookings.py) · [`luffy/12-lc-1109.md`](luffy/12-lc-1109-corporate-flight-bookings.md) |
| **LC 56** | Merge Intervals (合并区间) | Medium | 排序 + 区间合并 | [`luffy/13-lc-0056.py`](luffy/13-lc-0056-merge-intervals.py) · [`luffy/13-lc-0056.md`](luffy/13-lc-0056-merge-intervals.md) |
| **LC 41** | First Missing Positive (缺失的第一个正数) | Hard | 原地哈希置换 | [`luffy/14-lc-0041.py`](luffy/14-lc-0041-first-missing-positive.py) · [`luffy/14-lc-0041.md`](luffy/14-lc-0041-first-missing-positive.md) |

---

### Topic 2: 双指针与滑动窗口

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 对撞双指针: 数组有序或几何短板效应，左右指针向内逼近（LC 11, LC 167）。    │
│ 2. 三数之和 2-Way 极限剪枝: min_sum > 0 -> break; max_sum < 0 -> continue。 │
│ 3. 动态滑动窗口模版:                                                         │
│    • for right, c in enumerate(s):                                          │
│          更新窗口状态                                                        │
│          while 窗口不合法: 移出 left 元素; left += 1                         │
│          更新最长/最短结果                                                   │
│ 4. 连续子数组计数公理: 合法窗口内以 right 结尾的子数组数量恰为 right-left+1。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 11** | Container With Most Water (盛最多水的容器) | Medium | 短板贪心对撞 | [`top-100/lc-0011.py`](top-100/lc-0011-container-with-most-water.py) · [`top-100/lc-0011.md`](top-100/lc-0011-container-with-most-water.md) |
| **LC 15** | 3Sum (三数之和) | Medium | 排序+双指针+剪枝 | [`top-100/lc-0015.py`](top-100/lc-0015-3sum.py) · [`top-100/lc-0015.md`](top-100/lc-0015-3sum.md) |
| **LC 16** | 3Sum Closest (最接近的三数之和) | Medium | 距离绝对值最小化 | [`top-100/lc-0016.py`](top-100/lc-0016-3-sum-closest.py) · [`top-100/lc-0016.md`](top-100/lc-0016-3-sum-closest.md) |
| **LC 167** | Two Sum II (两数之和 II 有序数组) | Medium | 单调对撞双指针 | [`top-100/lc-0167.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py) · [`top-100/lc-0167.md`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.md) |
| **LC 26** | Remove Duplicates (删除有序数组重复项) | Easy | 快慢双指针 | [`luffy/05-lc-0026.py`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.py) · [`luffy/05-lc-0026.md`](luffy/05-lc-0026-remove-duplicates-from-sorted-array.md) |
| **LC 3** | Longest Substring (无重复字符最长子串) | Medium | 动态哈希滑窗 | [`top-100/lc-0003.py`](top-100/lc-0003-longest-substring-without-repeating-characters.py) · [`top-100/lc-0003.md`](top-100/lc-0003-longest-substring-without-repeating-characters.md) |
| **LC 209** | Minimum Size Subarray Sum (长度最小子数组) | Medium | 正数和滑窗收缩 | [`top-100/lc-0209.py`](top-100/lc-0209-minimum-size-subarray-sum.py) · [`top-100/lc-0209.md`](top-100/lc-0209-minimum-size-subarray-sum.md) |
| **LC 713** | Subarray Product Less Than K (乘积小于K子数组)| Medium | 乘积滑窗计数 | [`top-100/lc-0713.py`](top-100/lc-0713-subarray-product-less-than-k.py) · [`top-100/lc-0713.md`](top-100/lc-0713-subarray-product-less-than-k.md) |
| **LC 3090** | Max Substring At Most 2 Occurrences | Easy | 频数约束滑窗 | [`daily-practice/lc-3090.py`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.py) · [`daily-practice/lc-3090.md`](daily-practice/lc-3090-maximum-length-substring-with-at-most-two-occurrences.md) |
| **LC 3471** | Largest Almost Missing Integer | Easy | 定长滑窗/数学讨论 | [`daily-practice/lc-3471.py`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.py) · [`daily-practice/lc-3471.md`](daily-practice/lc-3471-find-the-largest-almost-missing-integer.md) |

---

### Topic 3: 单链表穿针引线与快慢指针

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 虚拟哨兵节点: dummy = ListNode(next=head)，统一头节点与普通节点删除/插入。│
│ 2. 链表反转三指针模版 (LC 206): pre = None; cur = head;                     │
│    while cur: nxt = cur.next; cur.next = pre; pre = cur; cur = nxt;          │
│ 3. 局部区间反转 (LC 92): p0 定位到待反转前驱，反转后 p0.next.next=cur; p0.next=pre│
│ 4. 快慢指针两大经典场景:                                                     │
│    • 寻找中点 (LC 876): slow 走 1 步，fast 走 2 步；                          │
│    • 环形检测与入口 (LC 141/142): 2:1 碰撞后，head 与 slow 同速同走必在入口相遇。│
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 206** | Reverse Linked List (反转链表) | Easy | 3 指针穿针引线 | [`top-100/lc-0206.py`](top-100/lc-0206-reverse-linked-list.py) · [`top-100/lc-0206.md`](top-100/lc-0206-reverse-linked-list.md) |
| **LC 92** | Reverse Linked List II (反转链表 II) | Medium | 局部区间反转 | [`daily-practice/lc-0092.py`](daily-practice/lc-0092-reversed-linked-list-2.py) · [`daily-practice/lc-0092.md`](daily-practice/lc-0092-reversed-linked-list-2.md) |
| **LC 25** | Reverse Nodes in k-Group (K个一组反转链表) | Hard | k-Group 循环反转 | [`daily-practice/lc-0025.py`](daily-practice/lc-0025-reverse-nodes-in-k-group.py) · [`daily-practice/lc-0025.md`](daily-practice/lc-0025-reverse-nodes-in-k-group.md) |
| **LC 876** | Middle of Linked List (链表的中间结点) | Easy | 快慢指针中点 | [`daily-practice/lc-0876.py`](daily-practice/lc-0876-middle-of-the-linked-list.py) · [`daily-practice/lc-0876.md`](daily-practice/lc-0876-middle-of-the-linked-list.md) |
| **LC 143** | Reorder List (重排链表) | Medium | 中点+反转+归并 | [`daily-practice/lc-0143.py`](daily-practice/lc-0143-reorder-list.py) · [`daily-practice/lc-0143.md`](daily-practice/lc-0143-reorder-list.md) |
| **LC 141** | Linked List Cycle (环形链表) | Easy | 快慢指针相遇 | [`top-100/lc-0141.py`](top-100/lc-0141-linked-list-cycle.py) · [`top-100/lc-0141.md`](top-100/lc-0141-linked-list-cycle.md) |
| **LC 142** | Linked List Cycle II (环形链表 II) | Medium | 环入口数学碰撞 | [`top-100/lc-0142.py`](top-100/lc-0142-linked-list-cycle-ii.py) · [`top-100/lc-0142.md`](top-100/lc-0142-linked-list-cycle-ii.md) |
| **LC 21** | Merge Two Sorted Lists (合并有序链表) | Easy | 双指针归并 | [`luffy/16-lc-0021.py`](luffy/16-lc-0021-merge-two-sorted-lists.py) · [`luffy/16-lc-0021.md`](luffy/16-lc-0021-merge-two-sorted-lists.md) |
| **LC 19** | Remove Nth Node From End (删除倒数第N节点)| Medium | 定长间隙双指针 | [`top-100/lc-0019.py`](top-100/lc-0019-remove-nth-node-from-end-of-list.py) · [`top-100/lc-0019.md`](top-100/lc-0019-remove-nth-node-from-end-of-list.md) |
| **LC 82** | Remove Duplicates from Sorted List II | Medium | 哨兵双步探测 | [`daily-practice/lc-0082.py`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.py) · [`daily-practice/lc-0082.md`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.md) |
| **LC 83** | Remove Duplicates from Sorted List | Easy | 原地相邻去重 | [`daily-practice/lc-0083.py`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.py) · [`daily-practice/lc-0083.md`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.md) |
| **LC 237** | Delete Node in Linked List (删除节点) | Medium | 替罪羊值覆盖 | [`daily-practice/lc-0237.py`](daily-practice/lc-0237-delete-node-in-a-linked-list.py) · [`daily-practice/lc-0237.md`](daily-practice/lc-0237-delete-node-in-a-linked-list.md) |

---

### Topic 4: 栈与队列、单调栈

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 括号匹配: 遇左括号压栈其对应右括号，遇右括号弹出核对。                     │
│ 2. 最小栈 MinStack: 辅助栈同步压入当前历史最小值 min(x, min_stack[-1])。     │
│ 3. 双栈模拟队列: in_stack 负责入队，out_stack 负责出队，均摊 O(1)。         │
│ 4. 接雨水 (LC 42):                                                           │
│    • 前后缀最值法: water[i] = min(pre_max[i], suf_max[i]) - height[i]；      │
│    • O(1) 对撞双指针法: pre_max < suf_max 时处理左侧，否则处理右侧。         │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 20** | Valid Parentheses (有效的括号) | Easy | 栈后进先出匹配 | [`luffy/19-lc-0020.py`](luffy/19-lc-0020-valid-parentheses.py) · [`luffy/19-lc-0020.md`](luffy/19-lc-0020-valid-parentheses.md) |
| **LC 155** | Min Stack (最小栈) | Medium | 辅助最小栈设计 | [`luffy/21-lc-0155.py`](luffy/21-lc-0155-min-stack.py) · [`luffy/21-lc-0155.md`](luffy/21-lc-0155-min-stack.md) |
| **LC 232** | Implement Queue using Stacks | Easy | 双栈倒水模拟 | [`luffy/24-lc-0232.py`](luffy/24-lc-0232-implement-queue-using-stacks.py) · [`luffy/24-lc-0232.md`](luffy/24-lc-0232-implement-queue-using-stacks.md) |
| **LC 227** | Basic Calculator II (基本计算器 II) | Medium | 优先级与符号栈 | [`luffy/22-lc-0227.py`](luffy/22-lc-0227-basic-calculator-ii.py) · [`luffy/22-lc-0227.md`](luffy/22-lc-0227-basic-calculator-ii.md) |
| **LC 394** | Decode String (字符串解码) | Medium | 双栈 (倍数+字符串) | [`luffy/23-lc-0394.py`](luffy/23-lc-0394-decode-string.py) · [`luffy/23-lc-0394.md`](luffy/23-lc-0394-decode-string.md) |
| **LC 42** | Trapping Rain Water (接雨水) | Hard | 双指针/前后缀极值 | [`top-100/lc-0042.py`](top-100/lc-0042-trapping-rain-water.py) · [`top-100/lc-0042.md`](top-100/lc-0042-trapping-rain-water.md) |

---

## Phase 2: 经典二分与极限搜索

### Topic 5: 二分查找与红蓝染色法

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 红蓝开区间二分模版 (-1, n):                                              │
│    • left = -1, right = n;                                                  │
│    • while left + 1 < right:                                                │
│          mid = (left + right) // 2                                          │
│          if is_blue(mid): right = mid (蓝色左缩)                            │
│          else: left = mid (红色右缩)                                        │
│    • 终止时不变量: left 严格处于红区，right 严格处于蓝区。                    │
│ 2. 万能 lower_bound 4 种区间等价映射:                                       │
│    • >= target : lower_bound(target)                                        │
│    • > target  : lower_bound(target + 1)                                    │
│    • < target  : lower_bound(target) - 1                                    │
│    • <= target : lower_bound(target + 1) - 1                                │
│ 3. 旋转数组与峰值判定:                                                       │
│    • 旋转数组以末尾元素 x = nums[-1] 为参考锚点判断阶梯；                   │
│    • 寻找峰值比较 nums[mid] > nums[mid+1] 斜率判定上下坡。                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 704** | Binary Search (二分查找) | Easy | 开闭区间标准二分 | [`luffy/07-lc-0704.py`](luffy/07-lc-0704-binary-search.py) · [`luffy/07-lc-0704.md`](luffy/07-lc-0704-binary-search.md) |
| **LC 34** | First & Last Position in Sorted Array | Medium | 万能 lower_bound | [`top-100/lc-0034.py`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py) · [`top-100/lc-0034.md`](top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.md) |
| **LC 33** | Search in Rotated Sorted Array | Medium | 旋转数组断点二分 | [`top-100/lc-0033.py`](top-100/lc-0033-search-in-rotated-sorted-array.py) · [`top-100/lc-0033.md`](top-100/lc-0033-search-in-rotated-sorted-array.md) |
| **LC 153** | Find Min in Rotated Sorted Array | Medium | `nums[-1]` 锚点二分 | [`daily-practice/lc-0153.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py) · [`daily-practice/lc-0153.md`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.md) |
| **LC 162** | Find Peak Element (寻找峰值) | Medium | 导数斜率红蓝二分 | [`top-100/lc-0162.py`](top-100/lc-0162-find-peak-element.py) · [`top-100/lc-0162.md`](top-100/lc-0162-find-peak-element.md) |

---

### Topic 6: 二分答案与单调性判定

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 二分答案判定三步法:                                                       │
│    • ① 确认答案的值域范围 [low, high]；                                     │
│    • ② 证明单调性: 若 mid 合法，则更小/更大的一侧必定也合法；               │
│    • ③ 编写 check(mid) 贪心验证函数，二分逼近最优极值点。                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 3: 树形结构与递归本原

### Topic 7: 二叉树与递归分治

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 递归本原两重视角:                                                         │
│    • 自顶向下 (Pre-order): 携带当前深度/路径参数深入子树；                   │
│    • 自底向上 (Post-order 分治): 向子树要答案，汇总左右子树返回值（如树高）。 │
│ 2. 对称性与相同树 (LC 100/101): isMirror(p.left, q.right) & isMirror(p.right, q.left)│
│ 3. 平衡二叉树 (LC 110): 自底向上计算高度，出现不平衡立即短路返回 -1。        │
│ 4. 最近公共祖先 LCA (LC 236): 四状态归并 (左右均非空返回 root，单侧非空返回子树)│
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 104** | Maximum Depth of Binary Tree (二叉树最大深度) | Easy | 分治后序递归 | [`top-100/lc-0104.py`](top-100/lc-0104-maximum-depth-of-binary-tree.py) · [`top-100/lc-0104.md`](top-100/lc-0104-maximum-depth-of-binary-tree.md) |
| **LC 100** | Same Tree (相同的树) | Easy | 双树同步递归 | [`daily-practice/lc-0100.py`](daily-practice/lc-0100-same-tree.py) · [`daily-practice/lc-0100.md`](daily-practice/lc-0100-same-tree.md) |
| **LC 101** | Symmetric Tree (对称二叉树) | Easy | 镜像双子树递归 | [`top-100/lc-0101.py`](top-100/lc-0101-symmetric-tree.py) · [`top-100/lc-0101.md`](top-100/lc-0101-symmetric-tree.md) |
| **LC 110** | Balanced Binary Tree (平衡二叉树) | Easy | 自底向上树高-1剪枝 | [`daily-practice/lc-0110.py`](daily-practice/lc-0110-balanced-binary-tree.py) · [`daily-practice/lc-0110.md`](daily-practice/lc-0110-balanced-binary-tree.md) |
| **LC 236** | Lowest Common Ancestor (最近公共祖先) | Medium | 四状态分治汇聚 | [`top-100/lc-0236.py`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.py) · [`top-100/lc-0236.md`](top-100/lc-0236-lowest-common-ancestor-of-a-binary-tree.md) |
| **LC 105** | Construct Tree from Pre & Inorder | Medium | 前序根+中序子树切分 | [`luffy/30-lc-0105.py`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.py) · [`luffy/30-lc-0105.md`](luffy/30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal.md) |
| **LC 94** | Binary Tree Inorder Traversal (中序遍历) | Easy | 递归/显式栈模拟 | [`luffy/25-lc-0094.py`](luffy/25-lc-0094-binary-tree-inorder-traversal.py) · [`luffy/25-lc-0094.md`](luffy/25-lc-0094-binary-tree-inorder-traversal.md) |
| **LC 144** | Binary Tree Preorder Traversal (前序遍历)| Easy | 根-左-右 | [`luffy/25-lc-0144.py`](luffy/25-lc-0144-binary-tree-preorder-traversal.py) · [`luffy/25-lc-0144.md`](luffy/25-lc-0144-binary-tree-preorder-traversal.md) |
| **LC 145** | Binary Tree Postorder Traversal (后序遍历)| Easy | 左-右-根 | [`luffy/25-lc-0145.py`](luffy/25-lc-0145-binary-tree-postorder-traversal.py) · [`luffy/25-lc-0145.md`](luffy/25-lc-0145-binary-tree-postorder-traversal.md) |

---

### Topic 8: 广度优先搜索与层序遍历

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 单队列快照 BFS: 每轮通过 for _ in range(len(q)) 一次性消费当前层所有节点。 │
│ 2. 双数组滚动 BFS: cur 存放当前层，nxt 收集下一层，无队列 pop 开销。          │
│ 3. 逆序 BFS (LC 513): 先入队 node.right 再入队 node.left，队列弹出的最后一个 │
│    节点必然是树的最底最左节点！                                              │
│ 4. 锯齿层序遍历 (LC 103): 依据当前层数奇偶性翻转 vals[::-1]。                │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 102** | Binary Tree Level Order (二叉树层序遍历) | Medium | 双数组滚动/单队列快照 | [`top-100/lc-0102.py`](top-100/lc-0102-binary-tree-level-order-traversal.py) · [`top-100/lc-0102.md`](top-100/lc-0102-binary-tree-level-order-traversal.md) |
| **LC 103** | Zigzag Level Order (锯齿形层序遍历) | Medium | 奇偶层动态翻转 | [`daily-practice/lc-0103.py`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.py) · [`daily-practice/lc-0103.md`](daily-practice/lc-0103-binary-tree-zigzag-level-order-traversal.md) |
| **LC 513** | Find Bottom Left Tree Value (找树左下角的值) | Medium | 逆序 BFS (先右后左) | [`daily-practice/lc-0513.py`](daily-practice/lc-0513-find-bottom-left-tree-value.py) · [`daily-practice/lc-0513.md`](daily-practice/lc-0513-find-bottom-left-tree-value.md) |
| **LC 199** | Binary Tree Right Side View (二叉树右视图) | Medium | 根-右-左 DFS / BFS | [`daily-practice/lc-0199.py`](daily-practice/lc-0199-binary-tree-right-side-view.py) · [`daily-practice/lc-0199.md`](daily-practice/lc-0199-binary-tree-right-side-view.md) |

---

### Topic 9: 二叉搜索树性质与操作

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. BST 范围上下界约束: dfs(node, low, high) 满足 low < node.val < high。    │
│ 2. 中序遍历严格单调递增: BST 的中序遍历序列必为严格递增序列。               │
│ 3. BST 最近公共祖先: 利用有序性分流：                                        │
│    • 若 p, q 均小于 root.val，祖先在左子树；                                 │
│    • 若 p, q 均大于 root.val，祖先在右子树；                                 │
│    • 出现分叉时当前 root 即为 LCA！                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 98** | Validate Binary Search Tree (验证BST) | Medium | 上下界约束/中序单调 | [`luffy/29-lc-0098.py`](luffy/29-lc-0098-validate-binary-search-tree-inorder.py) · [`luffy/29-lc-0098.md`](luffy/29-lc-0098-validate-binary-search-tree-inorder.md) |
| **LC 235** | LCA of Binary Search Tree (BST最近公共祖先) | Medium | 值域分流判定 | [`daily-practice/lc-0235.py`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.py) · [`daily-practice/lc-0235.md`](daily-practice/lc-0235-lowest-common-ancestor-of-a-binary-search-tree.md) |

---

## Phase 4: 暴力搜索与回溯算法

### Topic 10: 回溯三问模型与决策树

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 经典「回溯三问」模型:                                                     │
│    • ① 当前操作？ 枚举当前位置 path[i] 或枚举下一个可选元素 nums[j]。        │
│    • ② 子问题？   从下标 >= i 的剩余范围中构造解。                           │
│    • ③ 下一个子问题？ 从下标 >= j + 1 中构造解。                            │
│ 2. 子集问题的两大视角 (LC 78):                                               │
│    • 输入视角: 每个元素 0/1 选或不选二叉树（叶子收集）；                     │
│    • 答案视角: 每个节点本身都是合法子集，进入即收集 ans.append(path.copy())。 │
│ 3. 树层去重定理 (LC 40, LC 90): 排序后若 j > i 且 nums[j] == nums[j-1] 跳过。 │
│ 4. 字符串切分隔板模型 (LC 131): 仅在当前切出的子串为回文时递归进入下一层。    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 17** | Letter Combinations (电话号码字母组合) | Medium | 跨集合笛卡尔积 | [`top-100/lc-0017.py`](top-100/lc-0017-letter-combinations-of-a-phone-number.py) · [`top-100/lc-0017.md`](top-100/lc-0017-letter-combinations-of-a-phone-number.md) |
| **LC 78** | Subsets (子集) | Medium | 0-1 选与不选/多叉树 | [`top-100/lc-0078.py`](top-100/lc-0078-subsets.py) · [`top-100/lc-0078.md`](top-100/lc-0078-subsets.md) |
| **LC 77** | Combinations (组合) | Medium | 定长组合+剩余剪枝 | [`luffy/31-lc-0077.py`](luffy/31-lc-0077-combinations.py) · [`luffy/31-lc-0077.md`](luffy/31-lc-0077-combinations.md) |
| **LC 39** | Combination Sum (组合总和) | Medium | 无限复用回溯 | [`luffy/34-lc-0039.py`](luffy/34-lc-0039-combination-sum.py) · [`luffy/34-lc-0039.md`](luffy/34-lc-0039-combination-sum.md) |
| **LC 40** | Combination Sum II (组合总和 II) | Medium | 排序+树层去重 | [`luffy/35-lc-0040.py`](luffy/35-lc-0040-combination-sum-ii.py) · [`luffy/35-lc-0040.md`](luffy/35-lc-0040-combination-sum-ii.md) |
| **LC 46** | Permutations (全排列) | Medium | used 标记/原地交换 | [`luffy/32-lc-0046.py`](luffy/32-lc-0046-permutations.py) · [`luffy/32-lc-0046.md`](luffy/32-lc-0046-permutations.md) |
| **LC 131** | Palindrome Partitioning (分割回文串) | Medium | 隔板切分+回文剪枝 | [`daily-practice/lc-0131.py`](daily-practice/lc-0131-palindrome-partitioning.py) · [`daily-practice/lc-0131.md`](daily-practice/lc-0131-palindrome-partitioning.md) |
| **LC 79** | Word Search (单词搜索) | Medium | 2D 网格 DFS + 回溯 | [`luffy/37-lc-0079.py`](luffy/37-lc-0079-word-search.py) · [`luffy/37-lc-0079.md`](luffy/37-lc-0079-word-search.md) |

---

## Phase 5: 动态规划与进阶算法

### Topic 11: 动态规划核心与子问题递推

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 状态转移基本功: 定义 dp[i] 的严格物理意义（以 nums[i] 结尾或前 i 个元素）。│
│ 2. Kadane 算法 (LC 53): current_sum = max(num, current_sum + num)。          │
│ 3. 背包九讲极简归纳:                                                         │
│    • 0-1 背包: 每件物品选或不选，倒序遍历容量避免重复计算；                  │
│    • 完全背包: 每件物品可选无限次，正序遍历容量允许累加。                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 53** | Maximum Subarray (最大子数组和) | Medium | Kadane 状态压缩 | [`top-100/lc-0053.py`](top-100/lc-0053-maximum-subarray.py) · [`top-100/lc-0053.md`](top-100/lc-0053-maximum-subarray.md) |
| **LC 130** | Surrounded Regions (被围绕的区域) | Medium | 边界逆向 FloodFill | [`luffy/39-lc-0130.py`](luffy/39-lc-0130-surrounded-regions.py) · [`luffy/39-lc-0130.md`](luffy/39-lc-0130-surrounded-regions.md) |
| **LC 200** | Number of Islands (岛屿数量) | Medium | 沉岛 DFS / 并查集 | [`luffy/38-lc-0200.py`](luffy/38-lc-0200-number-of-islands.py) · [`luffy/38-lc-0200.md`](luffy/38-lc-0200-number-of-islands.md) |
| **LC 994** | Rotting Oranges (腐烂的橘子) | Medium | 多源网格 BFS | [`luffy/40-lc-0994.py`](luffy/40-lc-0994-rotting-oranges.py) · [`luffy/40-lc-0994.md`](luffy/40-lc-0994-rotting-oranges.md) |
| **LC 1091** | Shortest Path in Binary Matrix | Medium | 8 联通最短路 BFS | [`luffy/41-lc-1091.py`](luffy/41-lc-1091-shortest-path-in-binary-matrix.py) · [`luffy/41-lc-1091.md`](luffy/41-lc-1091-shortest-path-in-binary-matrix.md) |

---

### Topic 12: 图论拓扑排序与博弈数论

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 核心思维模型与解题心法                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 拓扑排序 Kahn 算法 (LC 207):                                             │
│    • 统计所有节点入度 in_degree；将入度为 0 的节点入队；                     │
│    • 出队并扣减邻居入度，若产生新 0 度节点则入队；若出队数 == n 则无环。      │
│ 2. 模 3 同余博弈 (LC 2029): 将石子按 % 3 分类，利用 cnt0 奇偶性分析先后手翻转。│
└─────────────────────────────────────────────────────────────────────────────┘
```

| 题号 | 题目名称 (中英) | 难度 | 考点分类 | Python 源码与 7 节题解笔记 |
| :-: | :--- | :-: | :--- | :--- |
| **LC 207** | Course Schedule (课程表) | Medium | 拓扑排序 Kahn BFS / 3色DFS | [`luffy/42-lc-0207.py`](luffy/42-lc-0207-course-schedule.py) · [`luffy/42-lc-0207.md`](luffy/42-lc-0207-course-schedule.md) |
| **LC 2029** | Stone Game IX (石子游戏 IX) | Medium | 模 3 同余分类与博弈论 | [`daily-practice/lc-2029.py`](daily-practice/lc-2029-stone-game-ix.py) · [`daily-practice/lc-2029.md`](daily-practice/lc-2029-stone-game-ix.md) |
