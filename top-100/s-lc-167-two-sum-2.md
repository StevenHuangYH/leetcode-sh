# LeetCode 167. Two Sum II - Input Array Is Sorted (两数之和 II)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (经典双指针对撞)
- **Tags:** Array, Two Pointers, Binary Search
- **Corresponding Python File:** [`top-100/s-lc-167-two-sum-2.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/s-lc-167-two-sum-2.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Return the indices `[index1, index2]` (1-based).
  * **Constraints:** Must use only $\mathcal{O}(1)$ extra space.
* **[CN]** 给你一个下标从 **1 开始** 的整数数组 `numbers` ，该数组已按 **非递减顺序排列** 。找出满足相加之和等于目标数 `target` 的两个数，以长为 2 的整数数组 `[index1, index2]` 返回其 1-based 下标。
  * **约束条件**：只能使用 $\mathcal{O}(1)$ 额外空间。

---

## 2. Code Implementation / 代码实现

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        n = len(numbers)
        right = n - 1

        while left < right:
            result = numbers[left] + numbers[right]

            if result == target:
                break
            if result > target:
                right -= 1
            else:
                left += 1

        # 题目要求 1-based index
        return [left + 1, right + 1]
```

---

## 3. Step-by-Step Walkthrough / 逐步核心逻辑

1. **双指针初始化**：`left = 0` 指向首端（最小值），`right = n - 1` 指向末端（最大值）。
2. **指针移动逻辑**：
   * 若 `result > target`：说明当前和偏大，将右指针左移 `right -= 1` 减小数值。
   * 若 `result < target`：说明当前和偏小，将左指针右移 `left += 1` 增大数值。
   * 若 `result == target`：找到目标两数，直接 `break` 退出循环。
3. **返回 1-based 索引**：因为 Python 索引从 0 开始，最终返回 `[left + 1, right + 1]`。

---

## 4. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time):** $\mathcal{O}(n)$
* **空间复杂度 (Space):** $\mathcal{O}(1)$ (满足常数额外空间约束)
