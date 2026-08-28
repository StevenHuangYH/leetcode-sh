# LC 0034: Find First and Last Position of Element in Sorted Array | 在排序数组中查找元素的第一个和最后一个位置

- **LeetCode ID**: LC 0034
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- **Solution File**: [lc-0034-find-first-and-last-position-of-element-in-sorted-array.py](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/top-100/lc-0034-find-first-and-last-position-of-element-in-sorted-array.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
If `target` is not found in the array, return `[-1, -1]`.
You must write an algorithm with $O(\log n)$ runtime complexity.

### [CN] 中文描述
给你一个按照非递减顺序排列的整数数组 `nums`，和一个目标值 `target`。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 `target`，返回 `[-1, -1]`。
你必须设计并实现时间复杂度为 $O(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` 是一个非递减数组
- `-10^9 <= target <= 10^9`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 704 Binary Search (标准精准查找)                     │
│ 寻找唯一 target，无法处理重复元素区间边界              │
└───────────────────────────┬────────────────────────────┘
                            │ 泛化为寻找首个满足条件的下标
                            ▼
┌────────────────────────────────────────────────────────┐
│ 万能 lower_bound 基础原语                               │
│ 定义: 返回最小下标 i 使得 nums[i] >= target            │
└───────────────────────────┬────────────────────────────┘
                            │ 通过等价变换衍生 4 种二分边界
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 34 首末位置范围查找 (本题)                           │
│ • 起始位置 (>= target): start = lower_bound(target)    │
│ • 结束位置 (<= target): end = lower_bound(target + 1)-1│
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

所有二分边界问题都可以严格归约为标准的 `lower_bound`（即寻找第一个满足 $\ge$ 条件的位置）：
1. $\ge target \iff \text{lower\_bound}(target)$
2. $> target \iff \text{lower\_bound}(target + 1)$
3. $< target \iff \text{lower\_bound}(target) - 1$
4. $\le target \iff \text{lower\_bound}(target + 1) - 1$

因此，求解目标值的范围区间 $[start, end]$ 只需要调用两次标准的 `lower_bound`：
- `start = lower_bound(nums, target)`
- `end = lower_bound(nums, target + 1) - 1`

```
nums:     [ 5,  7,  7,  8,  8, 10 ]
target=8:              ▲     ▲
                       │     │
          lower_bound(8)     lower_bound(9) - 1
            (start = 3)          (end = 4)
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    n = len(nums)
    right = n - 1 # 闭区间: [left, right]
    while left <= right: # 区间不为空
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1 # target在左侧或mid，缩小右边界
        else:
            left = mid + 1  # target在右侧，缩小左边界
    return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
```

1. **`lower_bound` 闭区间模板**：
   - 闭区间初始化 `left = 0, right = len(nums) - 1`。
   - `while left <= right:` 维持区间有效性。
   - `if nums[mid] >= target:` 说明 `>= target` 的第一个元素在 `mid` 或其左边，收缩 `right = mid - 1`。
   - `else:` 说明 `nums[mid] < target`，在 `mid` 右侧，收缩 `left = mid + 1`。
   - 退出循环后 `left` 即为首个满足 `nums[i] >= target` 的下标。
2. **`searchRange` 主逻辑**：
   - 获取起始点 `start = lower_bound(nums, target)`。
   - 若 `start == len(nums)`（所有数都比 target 小）或 `nums[start] != target`（数组中无 target），说明不存在，直接返回 `[-1, -1]`。
   - 查找首个大于 `target` 的位置的前一个下标 `end = lower_bound(nums, target + 1) - 1`。
   - 返回 `[start, end]`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“闭区间、左闭右开区间、开区间的返回下标有什么记忆规律？”*
  - **Candidate Response**:
    - **闭区间 `[0, n-1]`**：循环 `left <= right`，返回 `left`（此时 `right = left - 1`）。
    - **左闭右开 `[0, n)`**：循环 `left < right`，返回 `left` 或 `right`（此时两者重合）。
    - **开区间 `(-1, n)`**：循环 `left + 1 < right`，返回 `right`（红色归 `left`，蓝色归 `right`）。

- **Interviewer**: *“如果不借助 `target + 1`，如何直接写查找末尾位置的二分？”*
  - **Candidate Response**: 可以编写 `upper_bound(nums, target)` 寻找满足 `nums[mid] <= target` 的最大位置（当 `nums[mid] <= target` 时移动 `left = mid + 1`，最后返回 `left - 1`）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 遗漏 `start == len(nums)` 校验 | `IndexError: list index out of range` | 当 `target` 大于数组所有元素时，`lower_bound` 返回 `len(nums)` | 必须先检查 `start < len(nums)` 再访问 `nums[start]` |
| 空数组处理失误 | 边界异常报错 | 数组为空时 `start = 0`，若直接访问 `nums[0]` 会越界 | 闭区间 `right = -1` 退出循环返回 `0 == len(nums)`，由越界校验保护 |
| 二分求中点溢出 (C++/Java) | 整数溢出死循环 | `(left + right) // 2` 在大数场景可能溢出 | Python 自动大整数；在静态语言中使用 `left + (right - left) // 2` |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [5, 7, 7, 8, 8, 10], target = 8`

| Step | Call | `left` | `right` | `mid` | `nums[mid]` | Condition | Action | Return |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `lower_bound(8)` | 0 | 5 | 2 | 7 | `7 < 8` | `left = 3` | - |
| 2 | `lower_bound(8)` | 3 | 5 | 4 | 8 | `8 >= 8` | `right = 3` | - |
| 3 | `lower_bound(8)` | 3 | 3 | 3 | 8 | `8 >= 8` | `right = 2` | `left=3` (`start=3`) |
| 4 | `lower_bound(9)` | 0 | 5 | 2 | 7 | `7 < 9` | `left = 3` | - |
| 5 | `lower_bound(9)` | 3 | 5 | 4 | 8 | `8 < 9` | `left = 5` | - |
| 6 | `lower_bound(9)` | 5 | 5 | 5 | 10 | `10 >= 9`| `right = 4`| `left=5` (`end=5-1=4`) |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(\log n)$ | 调用两次独立的二分查找，每次耗时 $O(\log n)$，总耗时为 $2 \times O(\log n) = O(\log n)$。 |
| **Space Complexity** | $O(1)$ | 仅使用固定的常数级指针变量，空间开销为 $O(1)$。 |
