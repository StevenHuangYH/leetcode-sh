# LeetCode 153. Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 二分查找分段单调性)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py`](daily-practice/lc-0153-find-minimum-in-rotated-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.
  * For example, the array `nums = [0,1,2,4,5,6,7]` might become:
    * `[4,5,6,7,0,1,2]` if it was rotated 4 times.
    * `[0,1,2,4,5,6,7]` if it was rotated 7 times (0 times / full rotation).
  * Given the sorted rotated array `nums` of **unique** elements, return the **minimum element** of this array.
  * **Requirement:** You must write an algorithm that runs in $\mathcal{O}(\log n)$ time.
* **[CN]** 已知一个长度为 `n` 的升序排列数组，预先在未知某个点上进行了旋转（例如，数组 `[0,1,2,4,5,6,7]` 可能在旋转 4 次后变为 `[4,5,6,7,0,1,2]` ）。
  * 给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了旋转。
  * 请你找出并返回数组中的 **最小元素** 。
  * **要求**：你必须设计一个时间复杂度为 $\mathcal{O}(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
* $n == \text{nums.length}$
* $1 \le n \le 5000$
* $-5000 \le \text{nums}[i] \le 5000$
* `nums` 中的所有整数 **互不相同**。
* `nums` 原先是一个升序数组，并进行了 $1$ 至 $n$ 次旋转。

---

## 2. Core Idea & Mathematical Intuition / 核心解法思路与数学原理

### 💡 旋转数组的双段单调性 (Two-Segment Monotonicity)
原升序数组旋转后，在几何上被分割为两个递增的“分段”（断崖式结构）：

```
 数值 (Value)
   ^
   |        左半段 (Left Segment: nums[i] > nums[-1])
   |           /|
   |          / |
   |         /  |
   |        /   |   右半段 (Right Segment: nums[i] <= nums[-1])
   |       /    |          /
   |      /     |         /
   |     /      |        /
   |    /       |       /   <--- nums[-1] (基准参考锚点 Anchor)
   |            |      /
   |            |     /
   |            |    /
   |            |   * <--- 最小值 (MINIMUM: 右半段的第一个元素)
   +----------------------------------------------------> 下标 (Index)
```

#### 关键几何特征：
1. **左半段 (Left Segment)**：所有元素均 **严格大于** 数组末尾元素（$nums[i] > nums[-1]$）。
2. **右半段 (Right Segment)**：所有元素均 **小于等于** 数组末尾元素（$nums[i] \le nums[-1]$）。
3. **全局最小值 (Minimum Element)**：正是 **右半段的第一个元素**（也是断崖下落后的第一个点）。

---

### 🎯 为什么以 `nums[-1]` 作为二分基准参考点？
很多人在初学旋转数组时会犹豫该与 `nums[0]` 还是 `nums[-1]` 比较：
* **如果与 `nums[0]` 比较**：
  * 当数组完全没有旋转（或旋转了 $n$ 次，如 `[1, 2, 3, 4, 5]`）时，所有元素都 $\ge nums[0]$。
  * 此时无法通过统一的比较逻辑直接区分“整体单调升序”与“处于旋转断崖左侧”，必须增加额外的分支特判。
* **如果与 `nums[-1]` 比较（极简且普适）**：
  * 无论数组是否发生实质性旋转，$nums[-1]$ 永远属于右半段！
  * **若 $nums[mid] > nums[-1]$**：$mid$ 必然落在 **左半段**，最小值必定在 $mid$ 的严格右侧，搜索区间右移（$left = mid + 1$）。
  * **若 $nums[mid] \le nums[-1]$**：$mid$ 必然落在 **右半段**，最小值可能是 $mid$ 本身或在 $mid$ 左侧，搜索区间左移（$right = mid$ 或 $right = mid - 1$）。

---

### 🎨 红蓝染色法模型 (Red-Blue Binary Search)
* **蓝色性质 (Blue)**：满足 $nums[i] \le nums[-1]$（处于右半段，答案在 $i$ 或其左侧）。
* **红色性质 (Red)**：满足 $nums[i] > nums[-1]$（处于左半段，答案在 $i$ 的严格右侧）。
* **目标**：寻找 **第一个染为蓝色的元素下标**（即右半段的起点）。

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

以开区间 `(-1, n - 1)` 模版为例：

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. 初始化开区间 (-1, n - 1)
        left = -1
        right = len(nums) - 1
```

* **[EN] Action:** Initializes the open interval search range `(left, right) = (-1, n - 1)`.
  * **Why `right = len(nums) - 1`?** Because the last element `nums[-1]` is trivially $\le nums[-1]$ (always blue). We search for the earliest blue index in `(-1, n - 1)`.
* **[CN] 动作**：初始化开区间 `(left, right) = (-1, n - 1)`。
  * **为什么 `right = len(nums) - 1`？** 最后一个元素自身必定满足 $nums[-1] \le nums[-1]$（天然是蓝色）。我们要找的是第一个蓝色的位置，候选范围是开区间 `(-1, n - 1)`。

---

```python
        while left + 1 < right:
            mid = (left + right) // 2
```

* **[EN] Action:** Loops while the open interval contains at least one candidate index (`left + 1 < right`). Computes the middle index `mid`.
* **[CN] 动作**：当开区间内仍有未探明的候选位置时（`left + 1 < right`）持续循环，计算中点 `mid`。

---

```python
            if nums[mid] <= nums[-1]:
                right = mid  # mid 在右半段（蓝色），最小值在 mid 或其左侧
            else:
                left = mid   # mid 在左半段（红色），最小值在 mid 的严格右侧
```

* **[EN] Logic:**
  * If `nums[mid] <= nums[-1]`: `mid` belongs to the **Right Segment**. The minimum is either `mid` itself or somewhere to the left of `mid`. Contract right boundary to `mid` (`right = mid`).
  * Else (`nums[mid] > nums[-1]`): `mid` belongs to the **Left Segment**. The minimum is strictly to the right of `mid`. Contract left boundary to `mid` (`left = mid`).
* **[CN] 逻辑**：
  * 若 `nums[mid] <= nums[-1]`：说明当前处于右半段（蓝色区域），最小值可能是 `mid` 或在 `mid` 左侧，收缩右边界 `right = mid`。
  * 否则（`nums[mid] > nums[-1]`）：说明当前处于左半段（红色区域），最小值必然在 `mid` 的严格右侧，收缩左边界 `left = mid`。

---

```python
        return nums[right]
```

* **[EN] Action:** When the loop terminates, `left + 1 == right`. `right` points to the first blue element (the minimum value). Return `nums[right]`.
* **[CN] 动作**：循环结束时 `left + 1 == right`，`right` 精确指向第一个染为蓝色的元素（右半段起点），返回其数值 `nums[right]`。

---

## 4. The Three Interval Paradigms / 二分查找的三种区间模版深度对比

```
1. 闭区间 [0, n - 2]           2. 左闭右开 [0, n - 1)          3. 开区间 (-1, n - 1)
   left         right             left         right             left         right
    ↓             ↓                ↓             ↓                ↓             ↓
 [  0   . . .   n-2  ]          [  0   . . .   n-1  )          ( -1   . . .   n-1  )
```

| 维度 | 1. 闭区间 `[left, right]` | 2. 左闭右开 `[left, right)` | 3. 开区间 `(left, right)` |
| :--- | :--- | :--- | :--- |
| **初始范围** | `left = 0, right = n - 2` | `left = 0, right = n - 1` | `left = -1, right = n - 1` |
| **循环条件** | `while left <= right:` | `while left < right:` | `while left + 1 < right:` |
| **若 $nums[mid] \le nums[-1]$** | `right = mid - 1` | `right = mid` | `right = mid` |
| **若 $nums[mid] > nums[-1]$** | `left = mid + 1` | `left = mid + 1` | `left = mid` |
| **循环结束状态** | `right + 1 == left` | `left == right` | `left + 1 == right` |
| **返回值** | `return nums[left]` | `return nums[left]` (或 `nums[right]`) | `return nums[right]` |

### 三种模版的完整代码对比：

```python
from typing import List

# 1. 开区间模版 (-1, n - 1) —— 推荐
class SolutionOpen:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]


# 2. 闭区间模版 [0, n - 2]
class SolutionClosed:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]


# 3. 左闭右开模版 [0, n - 1)
class SolutionHalfOpen:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

---

## 5. Step-by-Step Walkthrough with Examples / 样例图解分析

### 样例 1: `nums = [3, 4, 5, 1, 2]` ($n = 5$, 旋转了 3 次)
目标：寻找最小值（最小值为 `1`，位于下标 `3`）。
参考锚点：`nums[-1] = nums[4] = 2`

* **初始化**（开区间）：`left = -1`, `right = 4` (区间 `(-1, 4)`)
* **第 1 轮**：
  * `mid = (-1 + 4) // 2 = 1`
  * 比较 `nums[1] = 4` 与 `nums[-1] = 2`：`4 > 2`（左半段 / 红色）
  * 令 `left = mid = 1`，区间缩小为 `(1, 4)`。
* **第 2 轮**：
  * `mid = (1 + 4) // 2 = 2`
  * 比较 `nums[2] = 5` 与 `nums[-1] = 2`：`5 > 2`（左半段 / 红色）
  * 令 `left = mid = 2`，区间缩小为 `(2, 4)`。
* **第 3 轮**：
  * `mid = (2 + 4) // 2 = 3`
  * 比较 `nums[3] = 1` 与 `nums[-1] = 2`：`1 <= 2`（右半段 / 蓝色）
  * 令 `right = mid = 3`，区间缩小为 `(2, 3)`。
* **终止**：`left + 1 == 3 == right`，循环结束。
* **返回**：`nums[right] = nums[3] = 1`，完全正确！

---

### 样例 2: 未旋转的原升序数组 `nums = [11, 13, 15, 17]` ($n = 4$)
参考锚点：`nums[-1] = nums[3] = 17`

* **初始化**：`left = -1`, `right = 3`
* **第 1 轮**：`mid = 1`, `nums[1] = 13 <= 17` $\to$ `right = 1`。
* **第 2 轮**：`mid = 0`, `nums[0] = 11 <= 17` $\to$ `right = 0`。
* **终止**：`left + 1 == 0 == right`。
* **返回**：`nums[0] = 11`，无需任何额外特判，自动正确收敛！

---

### 样例 3: 单元素数组 `nums = [1]` ($n = 1$)
* **初始化**：`left = -1`, `right = 0`。
* `left + 1 < right` $\to$ `0 < 0` (False)，循环直接不执行。
* **返回**：`nums[0] = 1`，边界极其优雅安全。

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 为什么右端点初始值不需要包含最后一个元素（即 `right = len(nums) - 1` 为开区间边界，闭区间为 `len(nums) - 2`）？
* 数组末尾元素 `nums[-1]` 自身与自身比较恒有 `nums[-1] <= nums[-1]`（必然属于右半段/蓝色）。
* 无论何时，`nums[-1]` 都已经是一个已知属于右半段的兜底保底解，因此我们只需要在它左边的范围（`[0, n - 2]`）内寻找是否还有更靠左的右半段元素。

### Q2: 本题为什么能保证 $\mathcal{O}(\log n)$？如果数组中有重复元素会怎样？
* 本题明确保证 **所有元素互不相同**，因此 $nums[mid]$ 与 $nums[-1]$ 只有严格的“大于”或“小于”两种关系，每次都能绝对安全地丢弃一半搜索空间。
* **引申思考（LeetCode 154）**：若数组中存在重复元素（如 `[2, 2, 2, 0, 2]` 与 `[2, 0, 2, 2, 2]`），当 $nums[mid] == nums[-1]$ 时，我们无法断定最小值在左还是在右，此时只能令 `right -= 1` 进行单步缩小，最坏情况下退化为 $\mathcal{O}(n)$。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(\log n)$ | 标准二分查找，每轮比较中点与末尾元素即可排除一半区间，循环次数为 $\lceil\log_2 n\rceil$。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用 `left`, `right`, `mid` 常数个整型辅助指针，不消耗额外内存空间。 |
