# LeetCode 11. Container With Most Water (盛最多水的容器)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (经典对撞双指针)
- **Tags:** Array, Two Pointers, Greedy
- **Corresponding Python File:** [`top-100/lc-0011-container-with-most-water.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/lc-0011-container-with-most-water.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{th}$ line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.
* **[CN]** 给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。

---

## 2. Code Implementation / 代码实现

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)

            # 贪心策略：移动较短板的那一侧指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
```

---

## 3. Core Intuition & Proof / 贪心与双指针原理

1. **容器容积公式**：
   $$\text{Area} = (right - left) \times \min(height[left], height[right])$$
2. **为什么移动较矮的板？**
   * 无论移动 `left` 还是 `right`，宽度 $(right - left)$ 都会减小 $1$。
   * **若移动较高板**：容器高度由较矮板决定，高度至多不变甚至变小，宽度又变窄，**面积必然严格减小**。
   * **若移动较矮板**：虽然宽度变小，但新板可能更高，**面积有可能增大**。
   * 因此，每次舍弃并移动较矮的一端是最优贪心决策。

---

## 4. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time):** $\mathcal{O}(n)$ —— 左右指针向内扫描，每个元素最多访问一次。
* **空间复杂度 (Space):** $\mathcal{O}(1)$ —— 仅使用常数个指针变量。
