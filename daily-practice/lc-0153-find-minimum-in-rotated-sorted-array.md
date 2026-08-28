# LC 0153: Find Minimum in Rotated Sorted Array | 寻找旋转排序数组中的最小值

- **LeetCode ID**: LC 0153
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **Solution File**: [lc-0153-find-minimum-in-rotated-sorted-array.py](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.
Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.
You must write an algorithm that runs in $O(\log n)$ time.

### [CN] 中文描述
已知一个长度为 `n` 的升序排列的整数数组，预先未知在某个点上进行了旋转。
给你一个元素值 互不相同 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了旋转。请你找出并返回数组中的 最小元素 。
你必须设计一个时间复杂度为 $O(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- `nums` 中的所有整数 互不相同
- `nums` 原先是一个升序数组，并进行了 `1` 至 `n` 次旋转

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ 线性扫描 O(n) 寻找断崖点                                │
│ 寻找第一个满足 nums[i] < nums[i-1] 的位置               │
└───────────────────────────┬────────────────────────────┘
                            │ 引入尾部锚点 nums[-1] 二段性判定
                            ▼
┌────────────────────────────────────────────────────────┐
│ 红蓝二分染色法 (Red-Blue Partitioning)                 │
│ • 红色 (nums[mid] > nums[-1]): 处于第一段高坡 (左半区) │
│ • 蓝色 (nums[mid] <= nums[-1]): 处于第二段低坡 (右半区)│
└───────────────────────────┬────────────────────────────┘
                            │ 二分收敛求首个蓝色节点
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 153 寻找旋转数组最小值 (本题)                        │
│ 最小值恰好是第二段低坡的第一个元素 (首个蓝色节点)       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

以 `nums[-1]` 作为全局基准锚点：
- **左侧高坡（红色）**：$nums[mid] > nums[-1]$，由于最小值一定在断崖右侧，最小值必在 $mid$ 右侧，收缩 $left = mid$。
- **右侧低坡（蓝色）**：$nums[mid] \le nums[-1]$，此时 $mid$ 可能是最小值本身或位于最小值右侧，收缩 $right = mid$。

最终 `right` 严格收敛于首个蓝色节点，即全局最小值所在位置。

```
           / (高坡段: nums[i] > nums[-1] -> Red)
          /
         /
────────┼─────────────────────── (基准线: nums[-1])
                                / (低坡段: nums[i] <= nums[-1] -> Blue)
                               / (首个蓝色点即为最小值 min)
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]: # 蓝色区域
                right = mid
            else:                    # 红色区域
                left = mid
        return nums[right]
```

1. **开区间初始化**：
   - `left = -1`: 红色区域左边界（哨兵）。
   - `right = len(nums) - 1`: 蓝色区域初始点。因为 `nums[-1] <= nums[-1]` 恒成立，最后一位必定是蓝色。
2. **二分循环 `while left + 1 < right`**：
   - `if nums[mid] < nums[-1]:` 处于蓝色区域，收缩 `right = mid`。
   - `else:` 处于红色区域，收缩 `left = mid`。
3. **返回结果**：
   - 退出循环后 `right` 即为首个蓝色元素下标，返回 `nums[right]`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么比较基准必须选 `nums[-1]` 而不能选 `nums[0]`？”*
  - **Candidate Response**: 若数组完全没有旋转（即完全升序），以 `nums[0]` 为基准时所有元素都会 $\ge nums[0]$，无法区分左右半区；而以 `nums[-1]` 为基准时，无论数组是否旋转，最小值所在的右半段所有元素都严格 $\le nums[-1]$，性质唯一且普适。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 使用 `nums[0]` 作基准在未旋转数组中失效 | `[1, 2, 3]` 误判为右半段 | 未旋转数组全数组 $\ge nums[0]$，二段性失效 | 统一使用 `nums[-1]` 作为不变量锚点 |
| 误将开区间初始 `right` 设为 `len(nums)` | 返回越界值 | 蓝色初始保证点必须是已知合法的 `nums[-1]` | 严格初始化 `right = len(nums) - 1` |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [4, 5, 6, 7, 0, 1, 2]`，`nums[-1] = 2`

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[mid] < 2?` | Region | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | -1 | 6 | - | - | - | - | 初始开区间 (-1, 6) |
| 1 | -1 | 6 | 2 | 6 | False | Red | `left = 2` |
| 2 | 2 | 6 | 4 | 0 | True | Blue | `right = 4` |
| 3 | 2 | 4 | 3 | 7 | False | Red | `left = 3` |
| End | 3 | 4 | - | - | `left + 1 == right` | - | 返回 `nums[4] = 0` |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(\log n)$ | 每次二分迭代排除一半区间，最大比较次数为 $\log_2 n$。 |
| **Space Complexity** | $O(1)$ | 仅使用 3 个整型指针，空间为常数开销。 |
