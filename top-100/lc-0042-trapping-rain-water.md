# LC 0042: Trapping Rain Water | 接雨水

- **LeetCode ID**: LC 0042
- **Difficulty**: Hard
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/trapping-rain-water/)
- **Solution File**: [lc-0042-trapping-rain-water.py](top-100/lc-0042-trapping-rain-water.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### [CN] 中文描述
给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

### Constraints / 约束条件
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Two Pointer]`

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 11 Container With Most Water (双指针求木桶短板)      │
│ 短板贪心对撞: 容量由 min(h[l], h[r]) * (r - l) 决定    │
└───────────────────────────┬────────────────────────────┘
                            │ 拓展为柱体离散局域储水
                            ▼
┌────────────────────────────────────────────────────────┐
│ 前后缀最值分解法 (Prefix/Suffix Max Arrays)             │
│ 公式: water[i] = min(pre_max[i], suf_max[i]) - height[i]│
└───────────────────────────┬────────────────────────────┘
                            │ 空间压缩：双指针动态维护左右短板
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 42 接雨水双指针空间优化版 (本题)                      │
│ 核心机制: 若 pre_max < suf_max，左侧必定为全局短板      │
│ 状态转移: ans += pre_max - height[left], left += 1     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

对于下标为 `i` 的柱子，其上方所能容纳的雨水高度仅取决于**其左侧最高柱子与右侧最高柱子的较小者**（木桶短板效应）：
$$\text{water}[i] = \max(0, \min(\text{pre\_max}[i], \text{suf\_max}[i]) - \text{height}[i])$$

通过双指针 `left = 0, right = n - 1`，分别维护左侧前缀最大值 `pre_max` 和右侧后缀最大值 `suf_max`：
- 若 `pre_max < suf_max`：无论 `[left, right]` 中间还有多高的柱子，`left` 处木桶短板必定是 `pre_max`，立即结算 `left` 处雨水并 `left += 1`。
- 若 `pre_max >= suf_max`：右侧柱子的全局木桶短板必定是 `suf_max`，立即结算 `right` 处雨水并 `right -= 1`。

```
     pre_max                                suf_max
        █                                      █
        █   █~~~█                              █
        █_█_█_█_█_█____________________________█
        left ──>                               <── right
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码（前后缀预处理与双指针两种实现）解析：

```python
# 方案 1: 前后缀最值数组 (O(n) 空间)
class SolutionPrefixSuffix:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h
        return ans

# 方案 2: 双指针相向而行 (O(1) 空间极致优化)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        pre_max = 0
        suf_max = 0

        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
```

1. **前后缀预处理法**：
   - 正向遍历计算前缀最大值 `pre_max[i]`。
   - 逆向遍历计算后缀最大值 `suf_max[i]`。
   - 遍历每个位置，累加 `min(pre, suf) - h`。
2. **双指针相向收缩法**：
   - `pre_max` 和 `suf_max` 动态更新为当前遍历到的两端最值。
   - `if pre_max < suf_max`: 左侧是绝对短板，`ans += pre_max - height[left]`，然后 `left += 1`。
   - `else`: 右侧是绝对短板，`ans += suf_max - height[right]`，然后 `right -= 1`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“除了前后缀数组和双指针，单调栈解法是按什么维度接雨水的？”*
  - **Candidate Response**:
    - **双指针 / 前后缀法**：**按列（竖直方向）计算**，每次计算一根宽度为 1 的柱子能储多少水。
    - **单调栈法**：**按层（水平方向）计算**，维护单调递减栈。当遇到高于栈顶的柱子时，弹出栈顶作为凹槽底部 `bottom`，新栈顶和当前柱子构成左右边界，计算水平水柱面积 $(min(h_{left}, h_{right}) - h_{bottom}) \times (right - left - 1)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 双指针结算前未先更新 `pre_max/suf_max` | 出现负数水容量报错 | 当前柱子高于前缀最大值时，若未更新会造成 `pre_max - height[left] < 0` | 必须在移动前先更新 `pre_max = max(pre_max, height[left])` |
| 边界长度小于 3 时未处理 | 不影响，但需验证稳健性 | $n < 3$ 时无法形成凹槽，储水量必为 0 | 循环条件 `while left < right` 自然返回 0，无需额外特判 |

### Complete Dry-Run Table / 实例推演表

输入: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`

| Step | `left` | `right` | `h[l]` | `h[r]` | `pre_max` | `suf_max` | Short Board | Water Added | `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 11 | 0 | 1 | 0 | 1 | `pre < suf` | `0 - 0 = 0` | 0 |
| 2 | 1 | 11 | 1 | 1 | 1 | 1 | `pre >= suf` | `1 - 1 = 0` | 0 |
| 3 | 1 | 10 | 1 | 2 | 1 | 2 | `pre < suf` | `1 - 1 = 0` | 0 |
| 4 | 2 | 10 | 0 | 2 | 1 | 2 | `pre < suf` | `1 - 0 = 1` | 1 |
| 5 | 3 | 10 | 2 | 2 | 2 | 2 | `pre >= suf` | `2 - 2 = 0` | 1 |
| 6 | 3 | 9 | 2 | 1 | 2 | 2 | `pre >= suf` | `2 - 1 = 1` | 2 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | Total: 6 |

---

## 6. Complexity Analysis / 复杂度分析

| Approach | Time Complexity | Space Complexity | Rationale |
|---|---|---|---|
| **Prefix/Suffix Arrays** | $O(n)$ | $O(n)$ | 两次线性扫描构建前后缀数组，一次线性汇总。 |
| **Two Pointers (Optimal)** | $O(n)$ | $O(1)$ | 左右双指针相向移动恰好遍历数组一次，仅使用常数级标量空间。 |
