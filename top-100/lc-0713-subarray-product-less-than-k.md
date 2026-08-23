# LeetCode 713. Subarray Product Less Than K (乘积小于 K 的子数组)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (滑动窗口经典题 / 区间计数)
- **Tags:** Array, Sliding Window
- **Corresponding Python File:** [`top-100/lc-0713-subarray-product-less-than-k.py`](file:///mnt/c/Users/steve/iCloudDrive/desktop/leetcode-sh/top-100/lc-0713-subarray-product-less-than-k.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.
* **[CN]** 给你一个整数数组 `nums` 和一个整数 `k` ，请你返回子数组内所有元素的乘积严格小于 `k` 的连续子数组的数目。

---

## 2. Code Implementation / 代码实现

```python
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 边界特判：正整数数组子数组乘积最小为 1。当 k <= 1 时，不可能严格小于 k，直接返回 0
        if k <= 1:
            return 0

        ans = 0
        prod = 1
        left = 0

        for right, x in enumerate(nums):
            # 1. 扩张窗口：将新元素乘入当前窗口总乘积
            prod *= x
            
            # 2. 收缩窗口：当乘积 >= k（不合法）时，持续从左端移出元素
            while prod >= k:
                prod //= nums[left]
                left += 1
                
            # 3. 核心计数：以当前 right 为固定右端点的合法连续子数组数目恰为窗口长度
            ans += right - left + 1

        return ans
```

---

## 3. Step-by-Step Code Walkthrough / 逐行逻辑剖析

### Step 1: 边界特判 (`if k <= 1: return 0`)
* **[EN] Why `k <= 1` returns 0?**
  * Per problem constraints, all elements in `nums` are positive integers ($\ge 1$).
  * The minimum possible product of any non-empty subarray is $1$.
  * If $k = 0$ or $k = 1$, no subarray can have a product **strictly less than** $k$. We can immediately return $0$.
  * **Critical Side Benefit:** Guaranteeing $k \ge 2$ in the loop ensures that `left` will never run past `right + 1`.
* **[CN] 为什么 `k <= 1` 直接返回 0？**
  * 题目规定数组中所有元素都是正整数（$\ge 1$）。
  * 任意非空子数组的乘积至少为 1。
  * 若 $k = 0$ 或 $k = 1$，不可能存在乘积**严格小于** $k$ 的子数组，因此直接返回 0。
  * **额外关键收益**：保证了后续循环中 $k \ge 2$，从而彻底避免了 `left` 指针越界的问题。

---

### Step 2: 扩张窗口 (`prod *= x`)
* **[EN] Action:** For each element $x$ at index `right`, multiply `prod` by $x$ to expand the current window `nums[left..right]`.
* **[CN] 动作**：右指针 `right` 逐个枚举元素 $x$，将 $x$ 乘入当前窗口总乘积 `prod` 中。

---

### Step 3: 收缩窗口 (`while prod >= k: prod //= nums[left]; left += 1`)
* **[EN] Action:** If `prod >= k`, the current window's product is too large. Shrink the window from the left by dividing out `nums[left]` and moving `left` forward until `prod < k`.
* **[CN] 动作**：若乘积 `prod >= k` 超出上限，则不断通过除以左端点 `nums[left]` 并右移 `left += 1` 来收缩窗口，直到窗口内乘积重新满足 `prod < k`。

---

### Step 4: 核心计数公式 (`ans += right - left + 1`)
* **[EN] Why `right - left + 1`?**
  * When `nums[left..right]` has a product $< k$, **every contiguous subarray ending at `right`** starting from index $i$ ($left \le i \le right$) is guaranteed to have a product $< k$ (because all numbers $\ge 1$, shorter subarrays have $\le$ products).
  * The number of valid subarrays ending at index `right` is exactly `right - left + 1`.
  * For example, with window `[10, 5, 2]` (`left = 0, right = 2`), valid subarrays ending at `2` are:
    1. `[2]` (length 1)
    2. `[5, 2]` (length 2)
    3. `[10, 5, 2]` (length 3)
    Total = $2 - 0 + 1 = 3$.
* **[CN] 为什么累加的是 `right - left + 1`？**
  * 当区间 `nums[left..right]` 的乘积 $< k$ 时，由于所有数均为正整数，以 `right` 结尾、起点在 $[left, right]$ 范围内的**所有连续子数组**乘积必然也都 $< k$。
  * 以当前 `right` 为**右端点**的合法子数组个数，刚好等于当前窗口的长度：`right - left + 1`。
  * 例如当前窗口是 `[10, 5, 2]`（`left=0, right=2`），以末尾 `2` 结尾的合法子数组为：
    1. `[2]`
    2. `[5, 2]`
    3. `[10, 5, 2]`
    刚好是 $2 - 0 + 1 = 3$ 个！每次枚举 `right` 时累加新增的这批子数组，不重不漏。

---

## 4. Deep Dive: Why Write It This Way? / 深度追问：为什么这么写？

### Q1: 为什么是除法 `prod //= nums[left]`？为什么用整除 `//=`？
* **乘法的逆运算**：在求和的滑动窗口中，移出元素使用减法（`sum -= nums[left]`）；在求乘积的滑动窗口中，移出元素对应的逆运算即为除法。
* **避免浮点数精度误差**：$nums[left]$ 是乘积 `prod` 的因数，整除保证除得尽且结果始终为 `int`，避免浮点数计算产生的舍入误差（如 `1.0000000000000002`）。

### Q2: 为什么用 `while` 循环而不是 `if`？
* 加入新元素 $x$ 后，乘积可能会变得非常大，仅移出 1 个 $nums[left]$ 不一定能满足 $< k$ 的要求。
* 必须通过 `while` 循环持续移出多个左端元素，直到乘积严格小于 $k$ 为止。

### Q3: 会不会发生 `left` 越界或死循环？
* **不会**。若单元素 $nums[right] \ge k$：
  * `left` 会一直右移直到 `left == right`，执行 `prod //= nums[right]` 后 `prod` 变为 `1`，且 `left` 变为 `right + 1`。
  * 因为前置检查保证了 $k \ge 2$，下一轮检查 `while prod >= k` 即 `1 >= k` 判定为 `False`，循环立即退出。
  * 此时 `right - left + 1 = right - (right + 1) + 1 = 0`，对答案贡献为 0，完全正确且安全。

---

## 5. Execution Trace Example / 模拟运行全过程

以 `nums = [10, 5, 2, 6], k = 100` 为例：

| `right` | `x` | `prod` (乘入后) | `while prod >= 100` (收缩) | 最终 `left` | 最终窗口 `nums[left..right]` | 新增合法子数组 (以 `right` 结尾) | `ans += right - left + 1` | 当前 `ans` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 10 | 10 | 不触发 (10 < 100) | 0 | `[10]` | `[10]` | $0 - 0 + 1 = 1$ | **1** |
| 1 | 5 | 50 | 不触发 (50 < 100) | 0 | `[10, 5]` | `[5]`, `[10, 5]` | $1 - 0 + 1 = 2$ | **3** |
| 2 | 2 | 100 | **触发**：`prod //= 10` $\rightarrow$ 10, `left` = 1 | 1 | `[5, 2]` | `[2]`, `[5, 2]` | $2 - 1 + 1 = 2$ | **5** |
| 3 | 6 | 60 | 不触发 (60 < 100) | 1 | `[5, 2, 6]` | `[6]`, `[2, 6]`, `[5, 2, 6]` | $3 - 1 + 1 = 3$ | **8** |

* 最终总合法子数组数目为：**`8`**。

---

## 6. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 核心解析 |
| :--- | :--- | :--- |
| **时间复杂度 (Time)** | $\mathcal{O}(n)$ | 每个元素最多被 `right` 乘入 1 次，被 `left` 除出 1 次，两指针均单调递增，总运算次数 $\le 2n$。 |
| **空间复杂度 (Space)** | $\mathcal{O}(1)$ | 仅使用 `ans`, `prod`, `left`, `right` 四个变量，空间常数级。 |
