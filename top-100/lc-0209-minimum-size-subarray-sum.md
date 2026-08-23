# LeetCode 209. Minimum Size Subarray Sum (长度最小的子数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (滑动窗口经典入门题)
- **Tags:** Array, Binary Search, Sliding Window, Prefix Sum
- **Corresponding Python Files:**
  - [`top-100/lc-0209-minimum-size-subarray-sum.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/lc-0209-minimum-size-subarray-sum.py)
  - [`luffy/06-lc-0209-minimum-size-subarray-sum.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/luffy/06-lc-0209-minimum-size-subarray-sum.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a contiguous subarray `[nums[l], nums[l+1], ..., nums[r-1], nums[r]]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.
* **[CN]** 给定一个含有 `n` 个正整数的数组和一个正整数 `target` 。找出该数组中满足其总和大于等于 `target` 的长度最小的 **连续子数组** `[nums[l], nums[l+1], ..., nums[r-1], nums[r]]` ，并返回其长度。如果不存在符合条件的子数组，返回 `0` 。

---

## 2. Core Idea: Variable-Size Sliding Window / 核心解法：变长滑动窗口

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow = 0
        fast = 0
        sum = 0
        min_len = float('inf')
        
        while fast < len(nums):
            sum += nums[fast]
            
            while sum >= target:
                min_len = min(min_len, fast - slow + 1)
                sum -= nums[slow]
                slow += 1
                
            fast += 1
            
        return min_len if min_len != float('inf') else 0
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

### 1. 初始化指针与状态变量

```python
slow = 0
fast = 0
sum = 0
min_len = float('inf')
```

* **`slow` (左指针 / 窗口左边界)**：指向当前滑动窗口的起始位置。
* **`fast` (右指针 / 窗口右边界)**：指向当前滑动窗口的结束位置。
* **`sum` (窗口内元素累加和)**：记录区间 `[slow, fast]` 内所有正整数的和。
* **`min_len = float('inf')` (最小长度)**：初始化为正无穷大，用于后续取 `min` 更新。

---

### 2. 扩张窗口 (Expand Window via `fast`)

```python
while fast < len(nums):
    sum += nums[fast]
```

* **动作**：外层循环遍历数组，右指针 `fast` 每次向右扩展一步，将新元素 `nums[fast]` 加入窗口，累加到 `sum` 中。

---

### 3. 收缩窗口与更新答案 (Shrink Window via `slow`)

```python
    while sum >= target:
        min_len = min(min_len, fast - slow + 1)
        sum -= nums[slow]
        slow += 1
```

* **触发条件**：当当前窗口的累加和 `sum >= target` 时，说明当前区间 `[slow, fast]` 已经满足条件。
* **动作**：
  1. **更新最短长度**：当前窗口长度为 `fast - slow + 1`，用 `min_len = min(min_len, fast - slow + 1)` 记录历史最小值。
  2. **收缩左边界**：尝试将左端点 `nums[slow]` 移出窗口（`sum -= nums[slow]`），并将左指针向右移 `slow += 1`。
  3. **循环判断**：只要移出后 `sum` 仍然 `>= target`，就继续收缩，以寻找更短的合法窗口；直到 `sum < target` 时退出内层循环。

---

### 4. 步进右指针与返回结果

```python
    fast += 1
    
return min_len if min_len != float('inf') else 0
```

* **`fast += 1`**：右指针继续向右探索下一个元素。
* **返回值判断**：如果整轮扫描后 `min_len` 仍为初始值 `float('inf')`，说明没有任何子数组的和能够达到 `target`，按题意返回 `0`；否则返回找到的最短长度 `min_len`。

---

## 4. Execution Trace Example / 模拟运行全过程

假设 `target = 7, nums = [2, 3, 1, 2, 4, 3]`：

| 步骤 | `fast` (`num`) | `slow` | 窗口内元素 `nums[slow..fast]` | 窗口和 `sum` | `sum >= 7`? | 当前更新 `min_len` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 (`2`) | 0 | `[2]` | 2 | 否 | $\infty$ |
| 2 | 1 (`3`) | 0 | `[2, 3]` | 5 | 否 | $\infty$ |
| 3 | 2 (`1`) | 0 | `[2, 3, 1]` | 6 | 否 | $\infty$ |
| 4 | 3 (`2`) | 0 | `[2, 3, 1, 2]` | **8** | **是** | $\min(\infty, 3-0+1) = \mathbf{4}$ |
| 4a | (收缩) | 1 | `[3, 1, 2]` | 6 (减去2) | 否 | 4 |
| 5 | 4 (`4`) | 1 | `[3, 1, 2, 4]` | **10** | **是** | $\min(4, 4-1+1) = \mathbf{4}$ |
| 5a | (收缩) | 2 | `[1, 2, 4]` | **7** (减去3) | **是** | $\min(4, 4-2+1) = \mathbf{3}$ |
| 5b | (收缩) | 3 | `[2, 4]` | 6 (减去1) | 否 | 3 |
| 6 | 5 (`3`) | 3 | `[2, 4, 3]` | **9** | **是** | $\min(3, 5-3+1) = \mathbf{3}$ |
| 6a | (收缩) | 4 | `[4, 3]` | **7** (减去2) | **是** | $\min(3, 5-4+1) = \mathbf{2}$ |
| 6b | (收缩) | 5 | `[3]` | 3 (减去4) | 否 | 2 |

* 最终返回最优解：**`2`** (对应子数组 `[4, 3]`)。

---

## 5. Complexity Analysis / 复杂度分析

* **时间复杂度 (Time Complexity):** $\mathcal{O}(n)$
  * 核心关键：虽然代码中出现了两层嵌套的 `while` 循环，但每个元素在整个过程中**最多被 `fast` 访问加入窗口 1 次，最多被 `slow` 移出窗口 1 次**。
  * 操作总次数不超过 $2n$，均摊时间复杂度为严格的 $\mathcal{O}(n)$。
* **空间复杂度 (Space Complexity):** $\mathcal{O}(1)$
  * 仅使用了几个常数级别的整型指针与求和变量，无额外内存开销。
