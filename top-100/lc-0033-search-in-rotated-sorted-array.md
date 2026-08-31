# LC 0033: Search in Rotated Sorted Array | 搜索旋转排序数组

- **LeetCode ID**: LC 0033
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- **Solution File**: [lc-0033-search-in-rotated-sorted-array.py](top-100/lc-0033-search-in-rotated-sorted-array.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with $O(\log n)$ runtime complexity.

### [CN] 中文描述
整数数组 `nums` 按升序排列，数组中的值互不相同。
在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`1 <= k < nums.length`）上进行了旋转，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标从 0 开始计数）。
给你旋转后的数组 `nums` 和一个整数 `target`，如果 `nums` 中存在这个目标值 `target`，则返回它的下标，否则返回 `-1`。
你必须设计一个时间复杂度为 $O(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- `nums` 中的每个值都独一无二
- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
- `-10^4 <= target <= 10^4`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Binary Search]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 704 Binary Search (标准单调区间二分)                 │
│ 判定规则: nums[mid] >= target (红蓝单调二分)            │
└───────────────────────────┬────────────────────────────┘
                            │ 引入旋转断崖 (Discontinuity Pivot)
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 153 Find Minimum in Rotated Sorted Array            │
│ 锚点性质: 比较 nums[mid] 与 nums[-1]，寻找旋转断崖分界  │
└───────────────────────────┬────────────────────────────┘
                            │ 结合 target 区间位置进行复合染色
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 33 Search in Rotated Sorted Array (本题)            │
│ 核心机制: is_blue(i) 复合判定 target 与 nums[i] 分段归属│
│ 染色定义: target <= nums[mid] 且处于相同单调区间       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

旋转排序数组被分割为两个单调递增的区间段：**左段高坡**与**右段低坡**，且左段所有元素严格大于右段所有元素（以 `nums[-1]` 为分界基准线）。
在红蓝染色法中，我们定义 `is_blue(i)` 为：**`target` 是否在 `nums[i]` 的左侧或刚好在 `nums[i]`**。
- 若 `nums[i] > nums[-1]`：说明 `nums[i]` 在左侧高坡。
  - 如果 `target > nums[-1]`（`target` 也在高坡），则标准比较 `nums[i] >= target`。
  - 如果 `target <= nums[-1]`（`target` 在低坡），则高坡上的任何 `nums[i]` 都在 `target` 左侧，`is_blue(i)` 为 `False`。
- 若 `nums[i] <= nums[-1]`：说明 `nums[i]` 在右侧低坡。
  - 如果 `target > nums[-1]`（`target` 在高坡），则低坡上的任何 `nums[i]` 都在 `target` 右侧，`is_blue(i)` 为 `True`。
  - 如果 `target <= nums[-1]`（`target` 也在低坡），则标准比较 `nums[i] >= target`。

```
       / (左段高坡: nums[i] > nums[-1])
      /
     / 
────┼─────────────────────── (基准线: end = nums[-1])
                            / (右段低坡: nums[i] <= nums[-1])
                           /
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target

        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid

        if right == len(nums) or nums[right] != target:
            return -1
        return right
```

1. **`is_blue(i)` 辅助函数**：
   - 提取尾部锚点 `end = nums[-1]`。
   - `if nums[i] > end`: `nums[i]` 在第一段。若 `target` 也在第一段且 `nums[i] >= target`，返回 `True`（蓝色，说明目标在 `i` 或其左侧）；否则返回 `False`（红色）。
   - `else`: `nums[i]` 在第二段。若 `target` 在第一段（必在 `i` 左侧）或 `nums[i] >= target`，返回 `True`；否则返回 `False`。
2. **开区间收缩 `left = -1, right = len(nums)`**：
   - 循环条件 `while left + 1 < right:` 确保区间不为空。
   - 若 `is_blue(mid)` 为真，收缩右边界 `right = mid`。
   - 否则收缩左边界 `left = mid`。
3. **有效性检验与下标返回**：
   - 循环结束时 `right` 是第一个满足 `is_blue` 的下标。
   - 若 `right == len(nums)` 或 `nums[right] != target`，说明 `target` 不存在，返回 `-1`；否则返回 `right`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果不写复合染色辅助函数 `is_blue`，如何用传统二分分类讨论解决？”*
  - **Candidate Response**: 可以先判断 `[left, mid]` 是否有序（即 `nums[left] <= nums[mid]`）：
    - 若 `[left, mid]` 有序，检查 `target` 是否在 `[nums[left], nums[mid]]` 范围内；若是则 `right = mid - 1`，否则 `left = mid + 1`。
    - 若 `[mid, right]` 有序，检查 `target` 是否在 `[nums[mid], nums[right]]` 范围内；若是则 `left = mid + 1`，否则 `right = mid - 1`。

- **Interviewer**: *“如果数组中包含重复元素（如 LC 81），时间复杂度会退化吗？”*
  - **Candidate Response**: 会退化为 $O(n)$。当 `nums[left] == nums[mid] == nums[right]` 时，无法判断哪一半是有序的，必须线性移动边界 `left += 1` 或 `right -= 1` 消除重复。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 忽略 `right == len(nums)` 越界检查 | `IndexError: list index out of range` | 当 `target` 大于数组中所有元素时，`right` 最终停在 `len(nums)` | 必须先校验 `right < len(nums)`，再访问 `nums[right]` |
| 混淆 `nums[-1]` 与 `nums[0]` 作为分界基准 | 在单调未旋转数组中判断失真 | `nums[-1]` 在所有旋转场景下都是右段的上界，性质唯一稳定 | 始终统一以 `nums[-1]` 作为锚点基准值 |
| 误写开区间边界初始化为 `0` 和 `n-1` | 遗漏第 0 或第 n-1 位元素 | 开区间模版严格要求两端均为开区间点 `left = -1, right = n` | 牢记开区间模版 `left = -1, right = len(nums)` |

### Complete Dry-Run Table / 实例推演表

输入: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`, `end = nums[-1] = 2`

| Step | `left` | `right` | `mid` | `nums[mid]` | `nums[mid]>end` | `target>end` | `is_blue(mid)` | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | -1 | 7 | - | - | - | - | - | 初始开区间 (-1, 7) |
| 1 | -1 | 7 | 3 | 7 | True | False | False (7在高坡，0在低坡) | `left = 3` |
| 2 | 3 | 7 | 5 | 1 | False | False | True (1>=0) | `right = 5` |
| 3 | 3 | 5 | 4 | 0 | False | False | True (0>=0) | `right = 4` |
| End | 3 | 4 | - | - | `left + 1 == right`, 退出循环 | - | - | `nums[4] == 0`, 返回 `4` |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(\log n)$ | 每次通过 `is_blue(mid)` 可以在 $O(1)$ 时间内严格将搜索空间排除一半。 |
| **Space Complexity** | $O(1)$ | 仅维护 `left, right, mid` 常数级指针与闭包变量。 |
