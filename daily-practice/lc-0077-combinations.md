# LeetCode 77. Combinations (组合)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 组合型枚举 / 剪枝优化 / 子集状态树)
- **Tags:** Backtracking, Combinatorics, Recursion, Pruning
- **Corresponding Python File:** [`daily-practice/lc-0077-combinations.py`](daily-practice/lc-0077-combinations.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given two integers `n` and `k`, return *all possible combinations of `k` numbers chosen from the range `[1, n]`*. You may return the answer in **any order**.
* **[CN]** 给定两个整数 `n` 和 `k`，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。你可以按 **任何顺序** 返回答案。

### Constraints / 约束条件
* $1 \le n \le 20$
* $1 \le k \le n$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 组合问题考察核心蓝图 (Combinations Blueprint)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 组合与排列的根本差异 (Order Insensitive):                                │
│    • 组合 [1, 2] 与 [2, 1] 视作相同，必须维持元素选取的递增/倒序不变量。    │
│    • 采用倒序枚举 (从 n 递减到 1) 或正序枚举 (从 1 递增到 n)，避免重复枚举。│
│ 2. 剪枝不变量 (Pruning Invariant / 边界早停条件):                           │
│    • 设当前 path 长度为 len(path)，仍需选取元素个数 d = k - len(path)。     │
│    • 当前候选池区间为 [1, i]，可用元素数量恰好为 i。                        │
│    • 若 i < d：剩余全部可用数字数量不足以填满目标长度 k，无需继续递归搜索！ │
│    • 因此循环下界收紧为 j >= d，即 for j in range(i, d - 1, -1)。           │
│ 3. 回溯对称性 (Backtracking State Symmetry):                                │
│    • path.append(j) 推进决策 -> dfs(j - 1) 递归下一状态 -> path.pop() 回溯。│
│ 4. 叶子收集与深拷贝不变量 (Snapshot Copy Invariant):                         │
│    • 当 len(path) == k 时，必须使用 ans.append(path.copy()) 记录当前快照。   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 组合型回溯思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Backtracking & Combinatorial Lineage (组合回溯思维谱系)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Direct Power Set): LC 78 Subsets (子集)                           │
│  └─ 任意长度组合: 每一个元素选或不选，状态树上所有节点均为合法答案。         │
│        │                                                                    │
│        ▼ [演进 Twist 1: 固定长度约束 + 上下界精确剪枝 (Fixed Length & Prune)] │
│  Level 2 (Fixed Length Combinations): LC 77 Combinations (本题★)            │
│  └─ 固定长度 k: 深度达到 k 时收集；剩余元素不足 k - len(path) 时提前剪枝。   │
│        │                                                                    │
│        ▼ [演进 Twist 2: 元素带重复 / 目标和约束 (Combination Sum)]          │
│  Level 3 (Targeted Combinations): LC 39 / LC 40 / LC 216                    │
│  └─ 累加和限制与同层去重: path_sum == target，配合排序与前驱元素去重。      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 🌲 状态决策空间与剪枝图解 (Decision Tree with Pruning)

以 $n = 4, k = 2$ 为例（倒序选择视角）：

```
                       dfs(4) [path=[], d=2]
                      /           \            \
                  j=4             j=3          j=2       (j=1 被剪枝, 1 < 2)
                 /                 \             \
             path=[4]           path=[3]       path=[2]
             dfs(3) [d=1]       dfs(2) [d=1]   dfs(1) [d=1]
            /   |   \           /     \           |
          j=3  j=2  j=1       j=2     j=1        j=1
          /     |     \        /       \          |
       [4,3]  [4,2]  [4,1]   [3,2]    [3,1]     [2,1]
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原作者实现逐行剖析：

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            # 1. 计算当前距离填满 k 个元素还差的数字个数 d
            d = k - len(path)
            
            # 2. 收集结果：当前路径长度已达到目标长度 k
            if len(path) == k:
                ans.append(path.copy())
                return
            
            # 3. 核心剪枝枚举：候选池为 [1, i]，必须满足 j >= d
            # 倒序枚举从 i 递减到 d (包含 d，即 range(i, d - 1, -1))
            for j in range(i, d-1, -1):
                path.append(j)     # 做选择
                dfs(j-1)           # 递归子问题：从 [1, j-1] 中继续选
                path.pop()         # 撤销选择 (回溯)

        dfs(n)
        return ans
```

* **Line 11-13**: 初始化结果集 `ans` 与当前路径栈 `path`。
* **Line 14**: 定义辅助深度优先搜索函数 `dfs(i)`，含义为「当前正准备从区间 $[1, i]$ 中选择下一个数字」。
* **Line 16**: 计算距离目标还需选取的数字个数 `d = k - len(path)`。
* **Line 18-20**: 递归终止条件。当 `len(path) == k` 时，说明当前路径已组合出合法的 $k$ 个数，使用 `path.copy()` 生成列表深拷贝并加入 `ans`，然后立即 `return`。
* **Line 23**: 核心剪枝循环。由于从 $[1, j]$ 中最多还能再选 $j$ 个数，如果 $j < d$，则即便将剩下所有数全选也无法凑够 $k$ 个，因此循环下界为 $d$。即 `range(i, d - 1, -1)`。
* **Line 24-26**: 标准回溯模板——压栈 `path.append(j)`，向下递归 `dfs(j - 1)`，弹栈还原 `path.pop()`。
* **Line 28-29**: 从最大数 $n$ 开始启动全局搜索 `dfs(n)`，最终返回 `ans`。

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 🎤 面试官追问：你能写出正序枚举以及选/不选 (Pick/Skip) 模型的实现吗？

```python
# 方案 A: 正序枚举模板 (Forward Enumeration with Pruning)
class SolutionForward:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, path = [], []
        def dfs(start):
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            # 正序剪枝：最多枚举到 n - d + 1
            for j in range(start, n - d + 2):
                path.append(j)
                dfs(j + 1)
                path.pop()
        dfs(1)
        return ans

# 方案 B: 选/不选二叉决策模型 (Binary Choice: Pick vs Skip)
class SolutionPickSkip:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, path = [], []
        def dfs(i):
            d = k - len(path)
            if d == 0:
                ans.append(path.copy())
                return
            if i < d:
                return  # 剪枝：剩余元素数量不足 d
            # 不选 i
            dfs(i - 1)
            # 选 i
            path.append(i)
            dfs(i - 1)
            path.pop()
        dfs(n)
        return ans
```

### 📊 算法范式对比表 (Paradigm Comparison Table)

| 范式维度 | 原实现 (倒序区间剪枝) | 方案 A (正序枚举剪枝) | 方案 B (选/不选二叉决策) |
| :--- | :--- | :--- | :--- |
| **思维模型** | 从 $n$ 递减选数，下界为 $d$ | 从 $1$ 递增选数，上界为 $n - d + 1$ | 每个数字独立决策：选或不选 |
| **分支因子** | 动态递减，极窄 | 动态递增，极窄 | 严格二叉树（高度 $n$） |
| **剪枝直观度** | ⭐⭐⭐⭐⭐ `j >= d` 极其简洁 | ⭐⭐⭐⭐ `start <= n - d + 1` | ⭐⭐⭐⭐⭐ `i < d` 显式递归基 |
| **空间开销** | $O(k)$ 递归栈 | $O(k)$ 递归栈 | $O(n)$ 递归栈深度 |

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误 / 常见陷阱 | 触发场景 / 错误现象 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix & Invariant) |
| :--- | :--- | :--- | :--- |
| **引用直接追加** (`ans.append(path)`) | 返回的所有组合均为空列表 `[[], [], ...]` | `path` 在后续回溯中被反复修改并最终弹空，传递的是对象引用而非快照 | 必须追加快照深拷贝：`ans.append(path.copy())` 或 `ans.append(list(path))` |
| **剪枝边界 off-by-one** (`range(i, d, -1)`) | 遗漏包含最小候选数的有效组合（如丢失 `[..., 1]`） | Python `range(start, stop, step)` 的 `stop` 为开区间，若写 `d` 则只能枚举到 `d + 1` | `stop` 参数必须设置为 `d - 1`，确保 $j = d$ 能够被遍历到 |
| **重复元素组合** (`dfs(j)` 而非 `dfs(j - 1)`) | 出现 `[4, 4]` 等重复元素组合 | 本题要求数字不能重复选取，下次递归必须收缩到 `j - 1`（或 `j + 1`） | 下一级递归必须传入严格收缩的子区间 `dfs(j - 1)` |
| **无剪枝暴力枚举** (`range(i, 0, -1)`) | $n=20, k=10$ 时产生大量无效递归分支，执行耗时成倍增加 | 未利用「剩余元素必须足够凑齐 $k$ 个」的数学不等式 $i \ge d$ | 引入变量 $d = k - |\text{path}|$，收紧循环边界为 $j \ge d$ |

---

### 🧪 实例推演表 (Dry-Run: $n = 4, k = 2$)

| 递归调用 | 当前状态 `path` | 需选个数 `d` | 循环区间 `range(i, d-1, -1)` | 当前分支 `j` | 动作说明 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `dfs(4)` | `[]` | $2$ | `[4, 3, 2]` | $j=4$ | 选取 4，`path=[4]`，进入 `dfs(3)` |
| `dfs(3)` | `[4]` | $1$ | `[3, 2, 1]` | $j=3$ | 选取 3，`path=[4,3]`，进入 `dfs(2)` |
| `dfs(2)` | `[4,3]` | $0$ | — | — | `len==2`，**收集 `[4, 3]`**，`return` |
| `dfs(3)` | `[4]` | $1$ | `[3, 2, 1]` | $j=2$ | 选取 2，`path=[4,2]`，**收集 `[4, 2]`** |
| `dfs(3)` | `[4]` | $1$ | `[3, 2, 1]` | $j=1$ | 选取 1，`path=[4,1]`，**收集 `[4, 1]`** |
| `dfs(4)` | `[]` | $2$ | `[4, 3, 2]` | $j=3$ | 选取 3，`path=[3]`，进入 `dfs(2)` |
| `dfs(2)` | `[3]` | $1$ | `[2, 1]` | $j=2$ | 选取 2，`path=[3,2]`，**收集 `[3, 2]`** |
| `dfs(2)` | `[3]` | $1$ | `[2, 1]` | $j=1$ | 选取 1，`path=[3,1]`，**收集 `[3, 1]`** |
| `dfs(4)` | `[]` | $2$ | `[4, 3, 2]` | $j=2$ | 选取 2，`path=[2]`，进入 `dfs(1)` |
| `dfs(1)` | `[2]` | $1$ | `[1]` | $j=1$ | 选取 1，`path=[2,1]`，**收集 `[2, 1]`** |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度评级 | 严格数学推导与证明 |
| :--- | :--- | :--- |
| **Time Complexity (时间复杂度)** | $\mathcal{O}\left(\binom{n}{k} \cdot k\right)$ | 组合数总共有 $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ 种不同结果。在剪枝优化下，搜索树的每一个叶子节点均对应一个合法组合，中间无效分支被剪枝消除。每次到达叶子节点时执行 `path.copy()` 需要 $\mathcal{O}(k)$ 的拷贝耗时，故总时间复杂度为 $\mathcal{O}\left(\binom{n}{k} \cdot k\right)$。 |
| **Space Complexity (空间复杂度)** | $\mathcal{O}(k)$ | 辅助空间主要由路径栈 `path` 和递归调用栈深度决定。递归树的最大深度为 $k$，因此辅助栈空间复杂度为 $\mathcal{O}(k)$（不计存储答案列表 `ans` 所需的 $\mathcal{O}\left(\binom{n}{k} \cdot k\right)$ 空间）。 |

