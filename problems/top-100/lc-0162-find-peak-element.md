# LC 0162: Find Peak Element | 寻找峰值

- **LeetCode ID**: LC 0162
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/find-peak-element/)
- **Solution File**: [lc-0162-find-peak-element.py](problems/top-100/lc-0162-find-peak-element.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that `nums[-1] = nums[n] = -\infty`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in $O(\log n)$ time.

### [CN] 中文描述
峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 `nums[-1] = nums[n] = -\infty` 。换句话说，任何超出数组范围的相邻元素都被视为负无穷。
你必须实现时间复杂度为 $O(\log n)$ 的算法来解决此问题。

### Constraints / 约束条件
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- 对于所有有效的 `i` 都有 `nums[i] != nums[i + 1]`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 线性扫描 O(n)                                          │
│ 寻找第一个满足 nums[i] > nums[i+1] 的位置               │
└───────────────────────────┬────────────────────────────┘
                            │ 发现山峰单调爬坡性质 (二分排除法)
                            ▼
┌────────────────────────────────────────────────────────┐
│ 爬坡二分查找模型 (Hill Climbing Binary Search)         │
│ • 上坡段 (nums[mid] < nums[mid+1]): 峰值必在右侧       │
│ • 下坡段 (nums[mid] > nums[mid+1]): 峰值在 mid 或左侧  │
└───────────────────────────┬────────────────────────────┘
                            │ 红蓝二分统一规范
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 162 寻找峰值红蓝染色法 (本题)                        │
│ 蓝色 (Blue): nums[mid] > nums[mid+1] (下坡, right=mid) │
│ 红色 (Red):  nums[mid] < nums[mid+1] (上坡, left=mid)  │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

题目设定边界 `nums[-1] = nums[n] = -\infty`，这意味着只要有上坡，就**必然存在至少一个峰顶**。
比较相邻两项 `nums[mid]` 与 `nums[mid + 1]`：
- 若 `nums[mid] < nums[mid + 1]`：当前处于上坡段，往高处走，`mid + 1` 及其右侧必存在峰值（染为红色，`left = mid`）。
- 若 `nums[mid] > nums[mid + 1]`：当前处于下坡段，往高处走，`mid` 及其左侧必存在峰值（染为蓝色，`right = mid`）。

循环不变量：`left` 始终在红色区域（上坡），`right` 始终在蓝色区域（下坡或峰顶）。最终 `right` 即为峰顶下标。

```
              /\  (Peak)
             /  \
            /    \ (Blue: nums[mid] > nums[mid+1], 往左走)
           /
(Red: nums[mid] < nums[mid+1], 往右走)
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1  # nums[-1] 边界保证

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid  # 下坡段，峰值在 mid 或其左侧
            else:
                left = mid   # 上坡段，峰值在 mid+1 或其右侧

        return right
```

1. **开区间初始化**：
   - `left = -1`: 红色区域下界（负无穷哨兵）。
   - `right = len(nums) - 1`: 蓝色区域初始点。因为 `nums[n] = -\infty`，所以 `nums[n-1] > nums[n]` 恒成立，最后一位必定属于蓝色下坡区域。
2. **二分循环 `while left + 1 < right`**：
   - 比较 `nums[mid]` 与 `nums[mid + 1]`（由于 `right = n - 1`，`mid < n - 1`，因此 `mid + 1` 绝对不会越界）。
   - `if nums[mid] > nums[mid + 1]`: 满足蓝色条件，`right = mid`。
   - `else`: 处于上坡段，`left = mid`。
3. **返回结果**：
   - 退出循环时 `right` 是第一个蓝色节点，即峰顶下标。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么二分查找能够应用在未排序的无序数组上？”*
  - **Candidate Response**: 二分查找的核心本质并非“全局有序”，而是**状态判定二段性 (Monotonic Decision Property)**。只要每次比较能够以 $O(1)$ 的代价确定目标所在的半区并安全舍弃另一半，即可实现 $O(\log n)$ 二分收缩。

- **Interviewer**: *“如果数组中允许相邻元素相等（如 LC 1901 二维矩阵峰值或存在平原），如何处理？”*
  - **Candidate Response**: 若存在平原且相邻相等，无法通过单点比较判断峰值方向，最坏情况下必须线性搜索 $O(n)$。在二维矩阵中则可以在每行求最大值后再对行进行二分查找。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 比较 `nums[mid]` 与 `nums[mid-1]` 导致下标越界 | `IndexError` 当 `mid = 0` 时 | `mid - 1` 可能为 `-1` 产生越界 | 统一定义为向右比较 `nums[mid] vs nums[mid + 1]` |
| 闭区间误将 `right` 初始化为 `len(nums)` | 导致 `mid + 1` 越界 | `mid` 最大可取到 `n - 1`，此时 `nums[mid + 1]` 崩溃 | 严格初始化 `right = len(nums) - 1` |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [1, 2, 1, 3, 5, 6, 4]`

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[mid+1]` | Slope Condition | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | -1 | 6 | - | - | - | - | 初始开区间 (-1, 6) |
| 1 | -1 | 6 | 2 | 1 | 3 | `1 < 3` (上坡) | `left = 2` |
| 2 | 2 | 6 | 4 | 5 | 6 | `5 < 6` (上坡) | `left = 4` |
| 3 | 4 | 6 | 5 | 6 | 4 | `6 > 4` (下坡, 峰顶) | `right = 5` |
| End | 4 | 5 | - | - | - | `left + 1 == right` 退出 | 返回 `right = 5` (值为 6) |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(\log n)$ | 每次迭代严格将搜索范围减半，最大循环次数为 $\lceil \log_2 n \rceil$。 |
| **Space Complexity** | $O(1)$ | 仅使用 `left, right, mid` 等标量指针，无额外内存开销。 |
