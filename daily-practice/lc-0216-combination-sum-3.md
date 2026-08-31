# LC 0216. Combination Sum III | 组合总和 III

## 1. Header & File Links
- **LeetCode ID**: LC 216
- **Difficulty**: Medium
- **Tags**: `backtracking`, `recursion`, `combinatorics`, `dfs`
- **Problem Link**: [LeetCode 216 - Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
- **Companion Source**: [`lc-0216-combination-sum-3.py`](./lc-0216-combination-sum-3.py)

---

## 2. Problem Statement & Constraints

### [EN]
Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:
- Only numbers `1` through `9` are used.
- Each number is used **at most once**.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

### [CN]
找出所有相加之和为 `n` 的 `k` 个数的组合，且满足下列条件：
- 只使用数字 `1` 到 `9`。
- 每个数字 **最多使用一次**。

返回所有可能的有效组合的列表。列表中不能包含相同的组合两次，组合可以以任何顺序返回。

### Constraints / 约束条件
- `2 <= k <= 9`
- `1 <= n <= 60`

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 宏观拓扑知识图谱归属 (Macro Topology Anchor)
`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

### 🧠 回溯组合求和思维谱系演化树 (ASCII Pattern Lineage Map)
```
┌────────────────────────────────────────────────────────┐
│  LC 0077: Combinations (从 1..n 选 k 个数基础回溯)      │
└───────────────────────────┬────────────────────────────┘
                            │ 引入和约束 (Sum Target = n) 与数字集限制 [1..9]
                            ▼
┌────────────────────────────────────────────────────────┐
│  LC 0216: Combination Sum III (无重复元素, 固定长度 k, 和为 n)│ ◄── [当前题目]
└───────────────────────────┬────────────────────────────┘
                            │ 拓展：允许重复选取 / 集合含重
            ┌───────────────┴───────────────┐
            ▼                               ▼
┌──────────────────────────────┐ ┌──────────────────────────────┐
│ LC 0039: Combination Sum     │ │ LC 0040: Combination Sum II  │
│ (无重复元素, 允许无限次重复选)  │ │ (含重复元素, 每个数至多用一次)│
└──────────────────────────────┘ └──────────────────────────────┘
```

### 决策树与极值剪枝模型 (Decision Tree & Pruning Invariant)
1. **状态空间搜索**：在集合 $\{1, 2, \dots, 9\}$ 中选取 $k$ 个不同的数，使得累加和等于 $n$。
2. **倒序枚举与剩余数量剪枝**：
   - 设当前路径已选取元素数量为 $\text{len}(path)$，还需选取的元素个数为 $d = k - \text{len}(path)$。
   - 若当前待选最大数为 $j$，要选出 $d$ 个互不相同的数，最小需要有 $d$ 个正整数可用，因此当前枚举的下界为 $d$（即 `range(i, d - 1, -1)`）。
3. **递归基底 (Base Case)**：当 $\text{len}(path) == k$ 时，检验和是否满足条件并保存快照。

```
dfs(i=9, d=3)
 ├── 选 9 ──> dfs(i=8, d=2)
 │             ├── 选 8 ──> dfs(i=7, d=1) ──> 选 7 ──> [9, 8, 7] (Sum = 24)
 │             └── ...
 ├── 选 8 ──> ...
 └── 选 3 ──> [3, 2, 1] (最小可能和为 6)
```

---

## 4. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(i):
            # d 表示当前还需要选取的元素个数
            d = k - len(path)
            
            # 终止条件：已选够 k 个数
            if len(path) == k:
                # 若当前路径和等于目标值 n（或通过求和验证），记录有效组合
                if sum(path) == n:
                    ans.append(path.copy())
                return
            
            # 倒序枚举候选数 j：从当前可用最大值 i 开始，递减至下界 d
            for j in range(i, d - 1, -1):
                path.append(j)       # 做出选择
                dfs(j - 1)           # 递归探索下一个更小的数
                path.pop()           # 撤销选择 (回溯)

        # 从可选的最大数 9 开始倒序搜索（若 n < 9 可从 min(9, n) 开始）
        dfs(min(9, n))
        return ans
```

> **关键机制说明**：
> 1. `d = k - len(path)`：动态计算剩余槽位。
> 2. `range(i, d - 1, -1)`：保证剩余候选数字总数至少能填满剩余的 $d$ 个槽位，实现天然无死角的剪枝。
> 3. `path.copy()`：避免 Python 引用传递在后续回溯时清空结果。

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1：如何利用“剩余和 (Remaining Sum)”进行极致前置剪枝？
> **面试官**：如果在递归过程中实时维护剩余和 $t = n - \sum(path)$，能否在未选满 $k$ 个数之前直接判断无解？

- **候选人回答**：
  完全可以。当剩余需要选取的 $d$ 个数即使选最小的连续数字（$\frac{d(1+d)}{2}$）其和也大于当前剩余和 $t$，或者选最大的连续数字（$\frac{d(2j-d+1)}{2}$）其和仍小于 $t$ 时，当前子树必然无解，可直接提前 `return` 剪枝。

```python
# 实时剩余和双向极值剪枝模板
def dfs_optimized(i: int, target: int):
    d = k - len(path)
    if target < 0 or target > (2 * i - d + 1) * d // 2: # 最大可能和不足
        return
    if target < d * (d + 1) // 2:                       # 最小可能和超标
        return
    if d == 0:
        ans.append(path.copy())
        return
    for j in range(i, d - 1, -1):
        path.append(j)
        dfs_optimized(j - 1, target - j)
        path.pop()
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ 反模式诊断表 (Anti-Patterns & Traps)

| Buggy Pattern / 常见陷阱 | Symptom & Fail Case | Root Cause / 根本原因 | Defensive Fix & Invariant |
| :--- | :--- | :--- | :--- |
| **未判断路径和等于 n** | 输出所有长度为 $k$ 的组合，包含和不等于 $n$ 的解 | 递归终止时只检查了 `len(path) == k`，遗漏了 `sum(path) == n` | 在收集结果前增加 `sum(path) == n` 判定，或实时递减 target |
| **浅拷贝陷阱 (`ans.append(path)`)** | 最终输出 `[[], [], []]` 全部为空列表 | Python 中 `path` 是引用传递，后续回溯 `path.pop()` 会清空已存列表 | 必须存入深/浅快照 `ans.append(path.copy())` 或 `path[:]` |
| **候选区间越界** | 选取了大于 9 的数字或选入了 0 | 循环初始值或下界未限定在 $[1, 9]$ 闭区间内 | 初始入口严格限定 `dfs(min(9, n))`，下界限制为 $1$ |
| **剪枝下界计算错误** | 漏解或生成长度不足 $k$ 的组合 | 倒序循环终点未包含下界 $d$，导致可选数不足 | 正确设置区间 `range(i, d - 1, -1)` |

### 完整实例推演 (Dry-Run: $k = 3, n = 7$)

| Step | Call / Action | `path` | $d$ | Remaining Candidates | Output / Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `dfs(7)` | `[]` | 3 | $j \in [7, 6, 5, 4, 3]$ | 选取 $j=4$ |
| 2 | `dfs(3)` | `[4]` | 2 | $j \in [3, 2]$ | 选取 $j=2$ |
| 3 | `dfs(1)` | `[4, 2]` | 1 | $j \in [1]$ | 选取 $j=1$ |
| 4 | `dfs(0)` | `[4, 2, 1]` | 0 | Base Case reached | $\text{sum}=7 \implies$ **收集 `[4, 2, 1]`** |
| 5 | 回溯 | `[4, 2]` | 1 | 循环结束 | 回溯到 `[4]` |
| 6 | 尝试其他分支 | ... | ... | 和均超过 7 或小于 7 | 剪枝跳过 |

**最终输出**：`[[1, 2, 4]]`（或 `[[4, 2, 1]]`）。

---

## 7. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}\left(C(9, k) \cdot k\right)$ | 从 9 个数字中选 $k$ 个的最大组合数为 $C(9, k) \le C(9, 4) = 126$。每个有效解拷贝路径需 $\mathcal{O}(k)$ 时间，总体常数极小（$< 10^3$ 次操作），运行耗时 $\approx 0\text{ ms}$。 |
| **Space Complexity** | $\mathcal{O}(k)$ | 递归调用栈的最大深度为 $k$，且 `path` 数组占用的辅助空间为 $\mathcal{O}(k)$。不计返回结果数组，额外辅助空间为 $\mathcal{O}(k)$。 |
