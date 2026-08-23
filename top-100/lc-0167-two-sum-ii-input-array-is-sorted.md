# LeetCode 167. Two Sum II - Input Array Is Sorted
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (面试高频 / 经典双指针)
- **Tags:** Array, Two Pointers, Binary Search
- **Corresponding Python File:** [`s-lc-167.py`](top-100/lc-0167-two-sum-ii-input-array-is-sorted.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
  * **Constraints:** You must use only $\mathcal{O}(1)$ extra space. There is exactly one solution. You may not use the same element twice.
* **[CN]** 给你一个下标从 **1 开始** 的整数数组 `numbers` ，该数组已按 **非递减顺序排列** 。请你从数组中找出满足相加之和等于目标数 `target` 的两个数。返回这两个数的下标 `index1` 和 `index2`（以长为 2 的整数数组 `[index1, index2]` 形式返回，下标从 1 开始）。
  * **约束条件**：你只能使用 $\mathcal{O}(1)$ 的额外空间；测试用例有且仅有一个有效答案；不能重复使用相同的元素。

---

## 2. Step-by-Step Code Walkthrough / 代码逐行详解

### 方案 1：双指针对撞法 (Two Pointers - Optimal $\mathcal{O}(1)$ Space)

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
```

* **[EN] Action:** Initializes `left` pointer at the first element index (`0`) and `right` pointer at the last element index (`len(numbers) - 1`).
  * **Why Two Pointers?** Because the array is **sorted**. The smallest elements are on the left, and the largest elements are on the right.
* **[CN] 动作**：初始化左指针 `left = 0` 指向数组首端（最小值），右指针 `right = len(numbers) - 1` 指向数组末端（最大值）。
  * **为什么用双指针？** 因为数组是**有序（非递减）**的。左侧是较小数，右侧是较大数，可以通过移动指针单调性地改变两数之和。

---

```python
        while left < right:
            curr_sum = numbers[left] + numbers[right]
```

* **[EN] Action:** Loops as long as `left < right`. Calculates the sum of the elements at the two pointers: `curr_sum = numbers[left] + numbers[right]`.
  * **Why `left < right` instead of `left <= right`?** The problem forbids using the exact same element twice (`1 <= index1 < index2 <= n`).
* **[CN] 动作**：当 `left < right` 时进入循环，计算当前左右指针所指两数之和 `curr_sum`。
  * **为什么是 `left < right` 而不是 `<=`？** 题目明确说明不能重复使用同一个元素两次（必须是两个不同位置的数）。

---

```python
            if curr_sum == target:
                return [left + 1, right + 1]
```

* **[EN] Action:** If `curr_sum == target`, the target pair is found.
  * **Why `+ 1`?** The problem states that the array is **1-indexed**, while Python lists are **0-indexed**. Adding `1` converts `0-based` indices into `1-based` indices.
* **[CN] 动作**：若两数之和刚好等于 `target`，立即返回下标数组。
  * **为什么要 `+ 1`？** 题目要求返回 **1-based index**（下标从 1 开始计），而 Python 列表是 0-based 索引，所以两端均需加 1。

---

```python
            elif curr_sum < target:
                left += 1
```

* **[EN] Logic:** If `curr_sum < target`, the sum is too small.
  * **Why `left += 1`?** Since the array is sorted in ascending order, moving `left` to the right (`left + 1`) increases the value of `numbers[left]`, thus increasing `curr_sum`.
* **[CN] 逻辑**：如果当前和 `curr_sum < target`，说明当前和偏小。
  * **为什么 `left += 1`？** 数组是升序排列的，将左指针向右移动一位可以增大 `numbers[left]` 的值，从而使两数之和增大。

---

```python
            else:
                right -= 1
```

* **[EN] Logic:** If `curr_sum > target`, the sum is too large.
  * **Why `right -= 1`?** Moving `right` to the left (`right - 1`) decreases the value of `numbers[right]`, thus reducing `curr_sum`.
* **[CN] 逻辑**：如果当前和 `curr_sum > target`，说明当前和偏大。
  * **为什么 `right -= 1`？** 将右指针向左移动一位可以减小 `numbers[right]` 的值，从而使两数之和减小。

---

```python
        return []
```

* **[EN] Action:** Fallback return. (Per constraints, a solution is guaranteed to exist).
* **[CN] 动作**：兜底返回（题目保证必定存在唯一解）。

---

## 3. Key FAQs & Concept Clarifications / 核心答疑与原理

### Q1: 为什么对撞双指针不会漏掉解？(Why are we sure no valid pair is missed?)
* 假设唯一正确的答案是下标对 $(i^*, j^*)$。
* 一开始 $left = 0 \le i^*$，$right = n-1 \ge j^*$。
* 如果 $left$ 还没到 $i^*$ 但 $right$ 已经到了 $j^*$：
  * 此时 $numbers[left] + numbers[right] = numbers[left] + numbers[j^*] < numbers[i^*] + numbers[j^*] = target$
  * 因为和必定小于 $target$，算法只会执行 `left += 1`，**绝不会把已经停在正确位置的 $right$ 左移**！
* 同理，若 $left$ 先到达 $i^*$，和必定大于 $target$，算法只会执行 `right -= 1`。
* 因此两个指针必然在 $(i^*, j^*)$ 处汇合，**绝不会错过正确答案**。

---

### Q2: LC 1 (Two Sum) vs LC 167 (Two Sum II) 的对比

| 维度 | LeetCode 1 (无序数组) | LeetCode 167 (有序数组) |
| :--- | :--- | :--- |
| **数组状态** | 无序 (Unsorted) | 已升序排序 (Sorted non-decreasing) |
| **推荐解法** | 哈希表 (Hash Map) | 双指针对撞 (Two Pointers) |
| **时间复杂度** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **空间复杂度** | $\mathcal{O}(n)$ (需要额外字典) | $\mathcal{O}(1)$ (仅双指针变量，满足进阶要求) |
| **下标规范** | 0-indexed | 1-indexed (需 `+ 1`) |

---

## 4. Alternative Methods / 其他解法对比

### 方案 2：二分查找 (Binary Search)
* **思路**：遍历每个元素 `numbers[i]`，在区间 `[i + 1, n - 1]` 中二分查找补数 `complement = target - numbers[i]`。
* **复杂度**：时间 $\mathcal{O}(n \log n)$，空间 $\mathcal{O}(1)$。

```python
class SolutionBinarySearch:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            low, high = i + 1, n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    low = mid + 1
                else:
                    high = mid - 1
        return []
```

---

## 5. Complexity Analysis / 复杂度分析

| 方法 | 时间复杂度 (Time) | 空间复杂度 (Space) | 评价 |
| :--- | :--- | :--- | :--- |
| **双指针对撞法 (Optimal)** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | ⭐ **最优解**，线性扫描，零额外内存开销 |
| **二分查找法** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | 满足空间要求，但时间稍慢 |
| **哈希表法** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | 不符合题目 $\mathcal{O}(1)$ 空间限制 |
