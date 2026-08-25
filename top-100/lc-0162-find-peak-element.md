# LeetCode 162. Find Peak Element (寻找峰值)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 二分查找极值点)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0162-find-peak-element.py`](top-100/lc-0162-find-peak-element.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** A peak element is an element that is strictly greater than its neighbors.
  * Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.
  * You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
  * **Requirement:** You must write an algorithm that runs in $\mathcal{O}(\log n)$ time.
* **[CN]** 峰值元素是指其值严格大于左右相邻值的元素。
  * 给你一个整数数组 `nums`，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。
  * 你可以假设 `nums[-1] = nums[n] = -∞` 。也就是说，任何超出数组边界的相邻元素都视作负无穷小。
  * **要求**：你必须设计并实现时间复杂度为 $\mathcal{O}(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 1000$
* $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$
* 对于所有有效的 $i$，都有 $\text{nums}[i] \neq \text{nums}[i + 1]$（相邻元素严格不相等）。

---

## 2. Core Idea: Why Binary Search Works on Unsorted Arrays / 核心解法：为什么无序数组也能二分？

### 💡 核心洞察与数学原理
很多人误以为二分查找只能用于“单调有序”的数组。但二分查找的本质是 **“两段性 (Bipartiteness)”** —— 只要每次通过某项性质能够明确 **排除掉一半不可能包含答案（或必然包含答案）的搜索空间**，即可进行对半缩小，在 $\mathcal{O}(\log n)$ 复杂度内找到解。

#### 1. 边界条件奠定极值基础：
题目假设 $nums[-1] = nums[n] = -\infty$，且相邻元素绝不相等（$nums[i] \neq nums[i+1]$）。
这保证了数组从边界出发必然是一个“升坡”，在另一侧边界前必然是一个“降坡”，**整个数组中必定至少存在一个局部峰值**。

#### 2. “上坡必有顶”引理 (The Climbing Theorem)：
我们任选一个位置 $mid$，比较 $nums[mid]$ 和其右侧相邻元素 $nums[mid + 1]$：

```
       情况 1: nums[mid] < nums[mid+1] (上坡)        情况 2: nums[mid] > nums[mid+1] (下坡)
                 峰值必定在右侧 (含 mid+1)                     峰值必定在左侧 (含 mid 本身)

                   /\                                     /\
                  /  \                                   /  \
                 /    \   ... nums[n]=-∞                /    \
                /                                            \
           mid+1                                              mid
            /                                                  \
          mid                                                 mid+1
          /                                                       \
  nums[-1]=-∞                                                    nums[n]=-∞
```

* **情况 1：$nums[mid] < nums[mid + 1]$（处于上坡段）**
  * 从 $mid$ 到 $mid + 1$ 数值在增大。
  * 由于数组右边界 $nums[n] = -\infty$，从 $mid + 1$ 向右走最终必定要“下落”。
  * 因此，**在 $[mid + 1, \dots]$ 的右半区间内必定存在至少一个峰值**！
  * 我们只需往右半区缩小搜索范围。
* **情况 2：$nums[mid] > nums[mid + 1]$（处于下坡段）**
  * 从 $mid$ 到 $mid + 1$ 数值在减小。
  * 由于数组左边界 $nums[-1] = -\infty$，从 $mid$ 向左走最终也必定要“下落”。
  * 因此，**在 $[\dots, mid]$ 的左半区间内（包含 $mid$ 本身）必定存在至少一个峰值**！
  * 我们只需往左半区（保留 $mid$）缩小搜索范围。

---

### 🎨 红蓝染色法模型 (Red-Blue Coloring Framework)
采用灵茶山艾府的红蓝染色体系：
* **蓝色性质 (Blue)**：满足 $nums[i] > nums[i + 1]$（处于峰值或下坡段，答案在 $i$ 或其左侧）。
* **红色性质 (Red)**：满足 $nums[i] < nums[i + 1]$（处于上坡段，答案在 $i$ 的严格右侧）。
* 初始时，所有位置未知。二分不断将左半边染成红色，右半边染成蓝色。
* 最终收敛点：**第一个蓝色位置即为一个合法的峰值元素索引**！

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

以开区间 `(-1, n - 1)` 模版为例：

```python
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 开区间 (-1, n - 1)
        left = -1
        right = len(nums) - 1
```

* **[EN] Action:** Initializes the open interval search range `(left, right) = (-1, n - 1)`.
  * **Why `right = len(nums) - 1` instead of `len(nums)`?** Because we will compare `nums[mid]` with `nums[mid + 1]`. To prevent index out-of-bound errors on `mid + 1`, `mid` must not exceed `n - 2`. In an open interval `(-1, n - 1)`, the maximum possible value of `mid` is $n - 2$.
* **[CN] 动作**：初始化开区间二分范围 `(left, right) = (-1, n - 1)`。
  * **为什么 `right = len(nums) - 1` 而不是 `len(nums)`？** 因为后续我们要访问 `nums[mid + 1]`。为了保证 `mid + 1` 不越界，`mid` 最大只能取到 $n - 2$。在开区间 `(-1, n - 1)` 中，内部的候选下标最大正好是 $n - 2$。

---

```python
        while left + 1 < right:
            mid = (left + right) // 2
```

* **[EN] Action:** Continues binary search while the open interval contains at least one unchecked element (`left + 1 < right`). Computes the middle index `mid`.
* **[CN] 动作**：当开区间内仍有未探明元素时（即 `left + 1 < right`）持续循环，计算中点 `mid`。

---

```python
            if nums[mid] > nums[mid + 1]:
                right = mid  # 染为蓝色，峰值在 mid 或其左侧
            else:
                left = mid   # 染为红色，峰值在 mid 的严格右侧
```

* **[EN] Logic:**
  * If `nums[mid] > nums[mid + 1]`: The sequence is sloping downwards. The peak is at `mid` or somewhere to the left of `mid`. Shrink the open interval right boundary to `mid` (`right = mid`).
  * Else (`nums[mid] < nums[mid + 1]`): The sequence is sloping upwards. The peak is strictly to the right of `mid`. Shrink the open interval left boundary to `mid` (`left = mid`).
* **[CN] 逻辑**：
  * 若 `nums[mid] > nums[mid + 1]`：处于下坡段，`mid` 可能是峰顶，或者峰顶在 `mid` 的左侧。将右边界收缩至 `mid`（开区间右边界不包含，但 `right` 指针记录了当前已知的蓝色最左位置）。
  * 否则（`nums[mid] < nums[mid + 1]`）：处于上坡段，`mid` 绝不可能是峰顶，峰顶必然在 `mid` 的严格右侧。将左边界收缩至 `mid`。

---

```python
        return right
```

* **[EN] Action:** When the loop terminates, `left + 1 == right`. `right` points to the first blue element (the peak), which is our answer.
* **[CN] 动作**：循环终止时 `left + 1 == right`，`right` 精确指向第一个染为蓝色的元素（即峰值位置），直接返回 `right`。

---

## 4. The Three Interval Paradigms / 二分查找的三种区间模版深度对比

本题可无缝适配二分查找的三种经典区间模版（闭区间、左闭右开、开区间）：

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
| **若 $nums[mid] < nums[mid+1]$** | `left = mid + 1` | `left = mid + 1` | `left = mid` |
| **若 $nums[mid] > nums[mid+1]$** | `right = mid - 1` | `right = mid` | `right = mid` |
| **循环结束状态** | `right + 1 == left` | `left == right` | `left + 1 == right` |
| **返回值** | `return left` | `return left` (或 `right`) | `return right` |

### 三种模版的完整代码对比：

```python
from typing import List

# 1. 开区间模版 (-1, n - 1) —— 推荐，边界极其对称优雅
class SolutionOpen:
    def findPeakElement(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right

# 2. 闭区间模版 [0, n - 2]
class SolutionClosed:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left

# 3. 左闭右开模版 [0, n - 1)
class SolutionHalfOpen:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
```

---

## 5. Step-by-Step Walkthrough with Examples / 样例图解分析

### 样例 1: `nums = [1, 2, 3, 1]` ($n = 4$)
目标：寻找峰值元素（峰值为 `3`，下标为 `2`）。

* **初始化**（开区间）：`left = -1`, `right = 3` (搜索开区间 `(-1, 3)`)
* **第 1 轮**：
  * `mid = (-1 + 3) // 2 = 1`
  * 比较 `nums[1] = 2` 与 `nums[2] = 3`：`nums[1] < nums[2]`（上坡）
  * 红色区域扩大，令 `left = mid = 1`。区间变为 `(1, 3)`。
* **第 2 轮**：
  * `mid = (1 + 3) // 2 = 2`
  * 比较 `nums[2] = 3` 与 `nums[3] = 1`：`nums[2] > nums[3]`（下坡）
  * 蓝色区域扩大，令 `right = mid = 2`。区间变为 `(1, 2)`。
* **终止**：`left + 1 == 2 == right`，循环结束。
* **返回**：`right = 2`，对应值 `nums[2] = 3`，正确！

---

### 样例 2: `nums = [1, 2, 1, 3, 5, 6, 4]` ($n = 7$)
目标：数组中有两个峰值：下标 `1`（值为 2）和下标 `5`（值为 6），返回任一个均可。

* **初始化**：`left = -1`, `right = 6` (搜索开区间 `(-1, 6)`)
* **第 1 轮**：
  * `mid = (-1 + 6) // 2 = 2`
  * `nums[2] = 1 < nums[3] = 3` $\to$ `left = 2`。区间变为 `(2, 6)`。
* **第 2 轮**：
  * `mid = (2 + 6) // 2 = 4`
  * `nums[4] = 5 < nums[5] = 6` $\to$ `left = 4`。区间变为 `(4, 6)`。
* **第 3 轮**：
  * `mid = (4 + 6) // 2 = 5`
  * `nums[5] = 6 > nums[6] = 4` $\to$ `right = 5`。区间变为 `(4, 5)`。
* **终止**：`left + 1 == right`，返回 `right = 5`（值为 6），正确！

---

### 极端情况测试：
1. **单调递增数组** `[1, 2, 3, 4, 5]`：
   * 每次比较均满足 $nums[mid] < nums[mid+1]$，`left` 会不断右移，最终收敛于最后一个元素下标 `4`（值为 5）。
2. **单调递减数组** `[5, 4, 3, 2, 1]`：
   * 每次比较均满足 $nums[mid] > nums[mid+1]$，`right` 会不断左移，最终收敛于第一个元素下标 `0`（值为 5）。
3. **单元素数组** `[1]` ($n = 1$)：
   * `left = -1`, `right = 0`。
   * `left + 1 < right` 条件为 `-1 + 1 < 0` $\to$ `0 < 0` (False)，循环直接不执行，返回 `right = 0`，完美成立！

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 为什么区间右边界只到 $n - 2$（或开区间 $n - 1$）？
* 因为循环体内需要访问 `nums[mid + 1]`。
* 如果 $mid$ 能够取到 $n - 1$，访问 `nums[mid + 1]` 就会变成 `nums[n]`，从而触发 **IndexError (数组越界)**。
* 限制搜索上限后，$mid$ 的最大可能取值为 $n - 2$，因此 $mid + 1 \le n - 1$，绝对安全。

### Q2: 为什么题目保证相邻元素严格不相等？如果有相等元素（如 `[1, 2, 2, 1]`）还能二分吗？
* 如果存在相等元素（$nums[mid] == nums[mid+1]$），当出现平坡时，我们**无法判断峰值在左边还是在右边**（例如 `[1, 1, 1, 2, 1]` vs `[1, 2, 1, 1, 1]`，中点处都是平坡，但峰值分布在不同侧）。
* 在存在相等相邻元素的情况下，最坏情况下必须退化为 $\mathcal{O}(n)$ 的线性扫描（类似 LeetCode 154 旋转排序数组的最小值的特判逻辑）。

### Q3: 为什么这道题有多个峰值时，二分仍能正确找到其中一个？
* 二分的过程每次都丢弃一段必然包含或不包含某类特征的半区。
* 即使两侧都有峰值，只要我们选择的一侧根据“爬坡定理”**必定存在至少一个峰值**，二分就能沿着该路径锁定该侧的局部峰值，满足题目“返回任何一个峰值”的要求。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(\log n)$ | 每次比较中点相邻两元素即可将搜索空间减半，最大循环次数为 $\lceil\log_2 n\rceil$。满足题目严格要求的对数时限。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用 `left`, `right`, `mid` 等几个常数级辅助指针变量，无任何额外内存开销。 |
