# LeetCode 33. Search in Rotated Sorted Array (搜索旋转排序数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (高频面试经典题 / 二分查找极值与分类讨论)
- **Tags:** Array, Binary Search
- **Corresponding Python File:** [`top-100/lc-0033-search-in-rotated-sorted-array.py`](top-100/lc-0033-search-in-rotated-sorted-array.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** There is an integer array `nums` sorted in ascending order (with **distinct** values).
  * Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).
  * Given the array `nums` after the possible rotation and an integer `target`, return the **index of `target`** if it is in `nums`, or `-1` if it is not in `nums`.
  * **Requirement:** You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.
* **[CN]** 整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。
  * 在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`1 <= k < nums.length`）上进行了 **旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标从 0 开始计数）。
  * 给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。
  * **要求**：你必须设计一个时间复杂度为 $\mathcal{O}(\log n)$ 的算法解决此问题。

### Constraints / 约束条件
* $1 \le \text{nums.length} \le 5000$
* $-10^4 \le \text{nums}[i] \le 10^4$
* `nums` 中的每个值都 **独一无二**
* 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
* $-10^4 \le \text{target} \le 10^4$

---

## 2. Core Idea: Red-Blue Binary Search with `nums[-1]` Reference / 核心解法：基于 `nums[-1]` 基准的红蓝二分法

### 💡 核心几何结构与两段性
升序数组旋转后呈现出断崖式双升序结构：

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
   |    /       |       /   <--- end = nums[-1] (基准参考锚点 Anchor)
   |            |      /
   |            |     /
   |            |    /
   |            |   * <--- 旋转断崖交界点
   +----------------------------------------------------> 下标 (Index)
```

---

### 🎨 红蓝二分染色逻辑 (`is_blue(i)`)

在标准的二分查找中，我们希望找到目标值 $target$ 第一次出现（$\ge target$）的位置。
我们将整个数组分成两个部分：
* **红色区域 (Red / False)**：位于 $target$ **严格左侧** 的元素。
* **蓝色区域 (Blue / True)**：$target$ 本身以及位于 $target$ **右侧** 的元素。

通过与末尾元素 `end = nums[-1]` 的比较，我们可以准确断定当前元素 $nums[i]$ 和目标值 $target$ 分别处于 **左半段** 还是 **右半段**：

#### 分类讨论判定表 (Decision Matrix)：

| 当前 $nums[i]$ 位置 | 目标 $target$ 位置 | $nums[i]$ 是否在 $target$ 的右侧（即是否染为蓝色 `is_blue`）？ |
| :--- | :--- | :--- |
| **左半段** ($nums[i] > end$) | **左半段** ($target > end$) | 同在左半段，由于左半段单调递增，当且仅当 $nums[i] \ge target$ 时为蓝色。<br>$\implies$ `target > end and nums[i] >= target` |
| **左半段** ($nums[i] > end$) | **右半段** ($target \le end$) | $nums[i]$ 在左半段，$target$ 在右半段，故 $nums[i]$ 必然在 $target$ 的严格左侧，恒为红色 (False)。 |
| **右半段** ($nums[i] \le end$) | **左半段** ($target > end$) | $nums[i]$ 在右半段，$target$ 在左半段，故 $nums[i]$ 必然在 $target$ 的严格右侧，恒为蓝色 (True)。 |
| **右半段** ($nums[i] \le end$) | **右半段** ($target \le end$) | 同在右半段，由于右半段单调递增，当且仅当 $nums[i] \ge target$ 时为蓝色。<br>$\implies$ `nums[i] >= target` |

#### 整合后的极简逻辑 (`is_blue`)：
```python
def is_blue(i: int) -> bool:
    end = nums[-1]
    if nums[i] > end:
        # nums[i] 在左半段：只有 target 也在左半段且 nums[i] >= target 时才是蓝色
        return target > end and nums[i] >= target
    else:
        # nums[i] 在右半段：若 target 在左半段则必为蓝色，若 target 也在右半段则 nums[i] >= target 为蓝色
        return target > end or nums[i] >= target
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于你实现的开区间 `(-1, n - 1)` 红蓝二分代码：

```python
from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target
```

* **[EN] Action:** Defines the predicate helper `is_blue(i)`. It compares $nums[i]$ and $target$ against $end = nums[-1]$ to determine if $nums[i]$ is at or to the right of $target$.
* **[CN] 动作**：定义二分染色判定函数 `is_blue(i)`。通过与 $end = nums[-1]$ 比较，精准判定 $nums[i]$ 是否落在包含 $target$ 及其右侧的蓝色区间。

---

```python
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
```

* **[EN] Action:** Initializes open interval `(left, right) = (-1, len(nums) - 1)`. Continuously bisects the search space while `left + 1 < right`:
  * If `is_blue(mid)` is True: Shrinks the right boundary `right = mid`.
  * If `is_blue(mid)` is False: Shrinks the left boundary `left = mid`.
* **[CN] 动作**：初始化开区间 `(-1, len(nums) - 1)`，进入标准开区间二分循环：
  * 若 `is_blue(mid)` 为 True：说明 `mid` 已进入蓝色区域，向左收缩右边界 `right = mid`。
  * 否则：说明 `mid` 仍在红色区域，向右收缩左边界 `left = mid`。

---

```python
        if right == len(nums) or nums[right] != target:
            return -1

        return right
```

* **[EN] Action:** Loop terminates with `left + 1 == right`. `right` points to the first blue element.
  * We check if `nums[right] == target`. If `target` does not exist in `nums` (or `nums[right] != target`), return `-1`. Otherwise, return the index `right`.
* **[CN] 动作**：循环终止时 `left + 1 == right`，`right` 精确停在第一个蓝色位置。
  * 检查该位置是否真的等于 $target$。若不等于（说明数组中不存在 $target$），返回 `-1`；否则返回下标 `right`。

---

## 4. Alternative Paradigms & Comparison / 多种解法对比

### 方案 1：一次二分法（红蓝染色 / 推荐，代码最凝练）
即当前代码，通过 `is_blue(i)` 一次二分直接在 $\mathcal{O}(\log n)$ 内定位 `target`。

### 方案 2：两次二分法（先找最小值断崖，再单段二分）
1. **第一步（LC 153）**：二分查找旋转数组的最小值下标 $pivot$（断崖分割点）。
2. **第二步**：根据 $target$ 与 $nums[-1]$ 的大小关系，确定 $target$ 落在左半段 $[0, pivot - 1]$ 还是右半段 $[pivot, n - 1]$。
3. **第三步**：在对应的严格单调升序子区间内调用标准 `lower_bound` 二分查找。

```python
# 两次二分实现示例
class SolutionTwoPass:
    def search(self, nums: List[int], target: int) -> int:
        # 1. 二分寻找最小值 pivot (断崖起点)
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        pivot = right
        
        # 2. 划分目标所在的单调区间
        if target > nums[-1]:
            left, right = -1, pivot  # 在左半段 [0, pivot - 1]
        else:
            left, right = pivot - 1, len(nums)  # 在右半段 [pivot, n - 1]
            
        # 3. 标准二分查找 target
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
                
        return right if right < len(nums) and nums[right] == target else -1
```

---

## 5. Step-by-Step Walkthrough with Examples / 样例图解分析

### 样例 1: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0` ($n = 7$)
基准锚点：`end = nums[-1] = 2`
$target = 0 \le 2$（$target$ 处于右半段）

* **初始化**：`left = -1`, `right = 6` (搜索开区间 `(-1, 6)`)
* **第 1 轮**：
  * `mid = (-1 + 6) // 2 = 2` $\to$ `nums[2] = 6 > 2`（左半段）
  * `is_blue(2)`: $nums[2]$ 在左半段而 $target$ 在右半段 $\to$ False (红色)
  * `left = mid = 2`，区间缩小为 `(2, 6)`。
* **第 2 轮**：
  * `mid = (2 + 6) // 2 = 4` $\to$ `nums[4] = 0 <= 2`（右半段）
  * `is_blue(4)`: $target \le 2$ 且 `nums[4] = 0 >= 0` $\to$ True (蓝色)
  * `right = mid = 4`，区间缩小为 `(2, 4)`。
* **第 3 轮**：
  * `mid = (2 + 4) // 2 = 3` $\to$ `nums[3] = 7 > 2`（左半段）
  * `is_blue(3)`: False (红色)
  * `left = mid = 3`，区间缩小为 `(3, 4)`。
* **终止**：`left + 1 == 3 + 1 == 4 == right`，循环结束。
* **校验与返回**：`nums[right] = nums[4] = 0 == target`，返回下标 `4`，完全正确！

---

### 样例 2: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 3` (不存在于数组中)
* 经过二分最终停在第一个蓝色位置 `right = 4` (`nums[4] = 0`)。
* 检查 `nums[4] != 3`，返回 `-1`，成功检测出元素缺失。

---

## 6. Key FAQs & Edge Cases / 核心答疑与边界分析

### Q1: 为什么使用 `nums[-1]` 作为锚点比使用 `nums[0]` 更统一？
* 比较 `nums[-1]` 能够完美兼顾**未发生旋转的原升序数组**（如 `[1, 2, 3, 4, 5]`）。在未旋转数组中，所有元素均 $\le nums[-1]$，整个数组被自然视作一个完整的“右半段”，无需任何分支特判即可完全复用标准二分逻辑。

### Q2: 数组只有一个元素时（$n = 1$）代码如何运转？
* 例如 `nums = [1]`, `target = 0`:
  * `left = -1, right = 0`。
  * `left + 1 < right` (即 `0 < 0`) 为 False，循环直接跳过。
  * 检查 `nums[0] = 1 != 0`，直接返回 `-1`。
* 例如 `nums = [1]`, `target = 1`:
  * 循环直接跳过，检查 `nums[0] == 1 == target`，直接返回 `0`。

---

## 7. Complexity Analysis / 复杂度分析

| 指标 | 复杂度 | 详解 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(\log n)$ | 单次标准二分查找，每轮通过 $\mathcal{O}(1)$ 的布尔逻辑判定将搜索空间减半，严格满足 $\mathcal{O}(\log n)$。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用常数个辅助变量（`left`, `right`, `mid`, `end`），无任何动态内存分配。 |
