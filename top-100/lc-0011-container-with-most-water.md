# LeetCode 11. Container With Most Water (盛最多水的容器)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (对撞双指针 / 贪心剪枝 / 面积最大化单调性)
- **Tags:** Array, Two Pointers, Greedy
- **Corresponding Python File:** [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the $i^{th}$ line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.
* **[CN]** 给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。

### Constraints / 约束条件
* $n == 	ext{height.length}$
* $2 \le n \le 10^5$
* $0 \le 	ext{height}[i] \le 10^4$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 容积公式与短板效应 (Bottle-neck Invariant):                              │
│    • Area(i, j) = (j - i) * min(height[i], height[j])                       │
│ 2. 对撞双指针贪心剪枝定理 (Greedy Pruning Theorem):                         │
│    • 若 height[left] < height[right]，以 left 为一端的所有其他容器容积必定   │
│      小于当前 Area(left, right)（因为宽度减小的同时，高度至多为 height[left]）│
│    • 因此移动较矮板 left += 1 可以安全剪掉一整行的搜索空间，不会遗漏最优解。   │
│ 3. 初始状态与收敛: left = 0, right = n - 1，向内收缩直至对撞 left == right。 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 对撞双指针思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Inward Two Pointers Family Tree (对撞双指针算法思维谱系图)                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Sorted Target Sum): LC 167 Two Sum II                             │
│  └─ 单调有序数组求和: sum < target -> left++, sum > target -> right--       │
│        │                                                                    │
│        ▼ [演进 Twist 1: 无序数组贪心极值搜索 (Greedy Bound Pruning)]         │
│  Level 2 (Geometric Area Optimization): LC 11 Container Most Water (本题★)  │
│  └─ 核心: 舍弃较矮板 (height[l] < height[r] -> l++)，保证不漏解             │
│        │                                                                    │
│        ├─► [演进 Twist 2: 降维固定锚点 + 双指针 (Fix Anchor)]               │
│        │   LC 15 3Sum / LC 16 3Sum Closest                                  │
│        │   └─ 策略: 排序后固定第 1 个数，转化为双指针对撞搜索               │
│        │                                                                    │
│        └─► [演进 Twist 3: 柱体储水前缀后缀极值 (Trapping Rain Water)]        │
│            LC 42 Trapping Rain Water                                        │
│            └─ 策略: 维护 pre_max 与 suf_max 对撞移动较小侧                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 ASCII 对撞双指针推演图解 (`height = [1,8,6,2,5,4,8,3,7]`)

```
  8 │    █                   █
  7 │    █                   █       █
  6 │    █   █               █       █
  5 │    █   █       █       █       █
  4 │    █   █       █   █   █       █
  3 │    █   █       █   █   █   █   █
  2 │    █   █   █   █   █   █   █   █
  1 │█   █   █   █   █   █   █   █   █
────┴─────────────────────────────────
     0   1   2   3   4   5   6   7   8
   left=0 (h=1)                    right=8 (h=7) -> Area = 8 * min(1,7) = 8. 移动 left -> 1
       left=1 (h=8)                right=8 (h=7) -> Area = 7 * min(8,7) = 49. 移动 right -> 7
       left=1 (h=8)            right=7 (h=3)     -> Area = 6 * min(8,3) = 18. 移动 right -> 6
       left=1 (h=8)        right=6 (h=8)         -> Area = 5 * min(8,8) = 40. 移动 right -> 5
最大容积 = 49 (位于 [1, 8] 之间)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0011-container-with-most-water.py`](top-100/lc-0011-container-with-most-water.py) 中的实现进行逐行深入解析：

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. 初始化对撞双指针
        left = 0
        right = len(height) - 1
        result = 0

        # 2. 双指针向内收敛循环
        while left < right:
            # 计算当前左右边界围成的容器面积
            area = (right - left) * min(height[left], height[right])
            # 维护全局最大面积
            result = max(result, area)

            # 3. 贪心决策：移动较矮板所在的一侧指针
            if height[left] < height[right]:
                left += 1   # 左边较矮，舍弃 left，向右寻找更高的板
            else:
                right -= 1  # 右边较矮或相等，舍弃 right，向左寻找更高的板

        return result
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 为什么移动较高板绝不可能产生更大容积？请给出严格数学证明。

* **面试官**：能否数学证明为什么必须移动较矮的一侧？
* **候选人解析**：
  * 设当前左板高度为 $h_l$，右板高度为 $h_r$，且 $h_l < h_r$，宽度为 $w = r - l$。当前容积为 $V = w \cdot h_l$。
  * 若保持 $l$ 不动，移动右板到任意 $r' < r$：
    * 新宽度 $w' = r' - l < w$；
    * 新高度 $h' = \min(h_l, h_{r'}) \le h_l$；
    * 因此新容积 $V' = w' \cdot h' < w \cdot h_l = V$ 恒成立！
  * 这证明了以 $l$ 为左边界的所有其他右边界 $r' \in (l, r)$ 都绝不可能比当前 $V$ 更大。因此安全舍弃 $l$ 具有完全的正确性。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **移动较高的一侧板** | 遗漏全局最优解，输出偏小的面积 | 违背了短板决策定理，在宽度变窄的同时无法突破高度瓶颈 | 严格判断 `if height[left] < height[right]: left += 1` |
| **循环条件写为 `left <= right`** | 在 `left == right` 时多计算一次面积 0 | 宽度为 0 容器无意义，虽然不影响结果但浪费一次判断 | 严格保持 `while left < right:` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 其中 $n$ 为数组 `height` 的长度。双指针初始位于两端，每轮循环必定使 $right - left$ 减少 1，直至两指针相遇。总循环次数严格为 $n - 1$ 次，每次操作耗时 $\mathcal{O}(1)$，总时间复杂度严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 算法仅使用了 `left`, `right`, `result`, `area` 几个常数级别的局部变量，额外空间复杂度严格为 $\mathcal{O}(1)$。 |
