# LeetCode 77. Combinations (组合)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 组合型枚举 / 倒序选数剪枝 / 经典回溯三问)
- **Tags:** Array, Backtracking
- **Corresponding Python File:** [`problems/daily-practice/lc-0077-combinations.py`](problems/daily-practice/lc-0077-combinations.py)

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
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 组合型枚举本质 (Combination vs Permutation):                              │
│    • 集合中元素无序，[1, 2] 与 [2, 1] 视为同一组合。                         │
│    • 为避免重复，通过「严格单调选择」（递增或递减）控制搜索空间。              │
│ 2. 经典「回溯三问」模型 (The Three Core Questions of Backtracking):           │
│    • ① 当前操作？ 枚举当前选取的数 j（从当前可用上界 i 倒序向下选至 d）；     │
│                   执行 path.append(j)。                                      │
│    • ② 子问题？   从 [1, i] 中选出 d = k - len(path) 个数的组合。             │
│    • ③ 下一个子问题？ 从 [1, j-1] 中选出 d - 1 个数的组合，即 dfs(j-1)。     │
│ 3. 核心剪枝不等式证明 (Extreme Pruning Invariant Proof):                     │
│    • 设当前 path 已有 len(path) 个数，还需选 d = k - len(path) 个数。        │
│    • 若从 [1, j] 中选数，剩余可用候选数总量仅为 j 个。                        │
│    • 必胜存在性条件: 可选数量必须 >= 需求数量，即 j >= d。                    │
│    • 故当前枚举下界可以直接收窄为 j = d，即 for j in range(i, d - 1, -1)。   │
│ 4. 递归基与快照不变量 (Base Case & Snapshot Invariant):                      │
│    • 当 len(path) == k 时，说明已收集满 k 个数，执行 ans.append(path.copy())│
│      记录独立快照并 return。                                                 │
│ 5. 状态还原对称性 (Backtracking State Restoration):                          │
│    • 严格保持 path.append(j) -> dfs(j - 1) -> path.pop() 的对称现场还原。    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

### 🧠 回溯组合思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🗺️ Topology Node: Phase 04 搜索与递归 ➔ [08. 回溯与组合 (Backtracking)]     │
│                 └─ Node: backtracking (遍历视角 / 状态空间决策树极值剪枝)   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🧠 Combinatorial Backtracking Lineage (组合回溯思维谱系演化图)              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Power Set - 任意长度子集): LC 78 Subsets                          │
│  └─ 无长度限制: 长度从 0 到 n 均合法，每个节点均记录答案                     │
│        │                                                                    │
│        ▼ [演进 Twist 1: 固定组合长度 k + 极值剪枝 (Fixed Size Pruning)]     │
│  Level 2 (Fixed Length Combinations): LC 77 Combinations (本题★)            │
│  └─ 仅当 len(path) == k 记录答案; 引入剩余候选数容量剪枝: j >= d            │
│        │                                                                    │
│        ├─► [演进 Twist 2: 固定长度 + 固定目标和 (Fixed Size & Sum)]         │
│        │   LC 216 Combination Sum III                                       │
│        │   └─ 策略: 限制选取 k 个数且和为 target，双重剪枝 (容量 + 数值和)  │
│        │                                                                    │
│        ├─► [演进 Twist 3: 可无限次重复选取 (Unlimited Reuse)]                │
│        │   LC 39 Combination Sum                                            │
│        │   └─ 策略: 递归传递 i 本身而非 i-1，通过 target 减至 0 作为出口     │
│        │                                                                    │
│        └─► [演进 Twist 4: 包含重复元素的去重组合 (Duplicates Deduplication)]│
│            LC 40 Combination Sum II                                         │
│            └─ 策略: 排序后同层跳过相同元素 (if j > start and nums[j] == ...)|
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 ASCII 倒序回溯搜索树推演图解 (`n = 4, k = 2`)

```
                                    dfs(4) [需选 2 个数, path=[]]
                                 /              |               \
                       j=4: 选 4            j=3: 选 3       j=2: 选 2  (j=1 剪枝: 1 < d=2 ✗)
                         /                      |                 \
                  dfs(3) [需选 1]          dfs(2) [需选 1]     dfs(1) [需选 1]
                 /     |      \              /     \               |
              j=3     j=2     j=1          j=2     j=1            j=1
               |       |       |            |       |              |
             [4,3]   [4,2]   [4,1]        [3,2]   [3,1]          [2,1]
              (✓)     (✓)     (✓)          (✓)     (✓)            (✓)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原实现 [`problems/daily-practice/lc-0077-combinations.py`](problems/daily-practice/lc-0077-combinations.py) 逐行精析：

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(i):
            # 1. 计算当前距离填满 k 个元素还差几个数
            d = k - len(path)
            
            # 2. 递归基出口：path 长度满足 k
            if len(path) == k:
                ans.append(path.copy()) # 深拷贝记录当前有效组合
                return
            
            # 3. 倒序枚举当前选取的数字 j
            # 极值剪枝核心: 从 [1, j] 中至少还要选 d 个数，故 j 必须满足 j >= d
            # 故 range 下界为 d-1（开区间停止于 d-1，即最后一次循环 j = d）
            for j in range(i, d - 1, -1):
                path.append(j)     # 做出选择
                dfs(j - 1)         # 递归探索子问题（下一轮只能选比 j 小的数，天然防重）
                path.pop()         # 撤销选择，恢复现场
        
        # 4. 从最大候选数 n 开始逆序向下搜索
        dfs(n)
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 🎯 面试官追问 1：如果习惯正序搜索（从 1 到 n），剪枝公式该如何推导？
* **应答策略**：正序枚举时，当前选 $j$，剩余可选范围为 $[j, n]$，元素个数为 $n - j + 1$。
* **剪枝条件**：剩余可用数 $n - j + 1 \ge d \implies j \le n - d + 1$。因此循环上界为 `range(start, n - d + 2)`。

```python
# 正序选数 + 剪枝模板
def combine_forward(n: int, k: int) -> List[List[int]]:
    ans, path = [], []
    def dfs(start):
        d = k - len(path)
        if len(path) == k:
            ans.append(path.copy())
            return
        for j in range(start, n - d + 2):
            path.append(j)
            dfs(j + 1)
            path.pop()
    dfs(1)
    return ans
```

---

### 🎯 面试官追问 2：能否用「选与不选」（0-1 背包视角 / 选/跳过二叉树）实现？
* **应答策略**：每个元素 $i$ 只有两种决策：① 选入 $path$；② 跳过不选。在每一步对剩余容量与剩余总元素做强剪枝。

| 范式对比 | 遍历视角 (多叉树循环) | 选与不选视角 (二叉决策树) |
| :--- | :--- | :--- |
| **单层决策** | 一次循环枚举当前位置放哪一个数 | 单独决定当前元素 $i$ 选还是不选 |
| **树的分支** | 动态 $n - d + 1$ 叉树 | 严格二叉树（选分支 / 不选分支） |
| **剪枝直观度** | 循环边界一行收窄 | `if len(path) + i < k: return` 提前截断 |

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| Buggy Pattern / Traps (典型错误) | Symptom & Fail Case (错误现象) | Root Cause (根因分析) | Defensive Fix & Invariant (防御性修复) |
| :--- | :--- | :--- | :--- |
| **浅拷贝引用污染** (`ans.append(path)`) | 返回结果全部为空列表 `[[], [], []]` | `path` 为同一个列表对象的引用，后续 `pop()` 最终清空原列表 | 必须执行深拷贝：`ans.append(path.copy())` 或 `path[:]` |
| **剪枝开闭区间搞错** (`range(i, d, -1)`) | 遗漏边界解（如 $n=4, k=2$ 遗漏 `[2, 1]`） | `range` 结束条件是开区间，写 `d` 会导致 $j=d$ 无法被执行 | 倒序步长为 -1 时，若要包含 $d$，右边界必须为 `d - 1` |
| **正反序混用越界** | 死循环或递归深度超限 | `dfs(j)` 而非 `dfs(j-1)`，导致重复选取同一元素 | 严格维持单调递减 `dfs(j-1)` 或单调递增 `dfs(j+1)` |
| **缺少剪枝暴力回溯** | $n=20, k=10$ 时运行耗时大幅上升（TLE 风险） | 探索了大量即使把剩下数全选也凑不满 $k$ 个的无效死分支 | 在进入循环前或循环边界处严格执行 $j \ge d$ 容量剪枝 |

---

### 📊 完整实例干跑推演表 (`n = 4, k = 2`)

| 步骤 | 递归调用 | 当前 `d = 2 - len(path)` | 候选 `j` 范围 `range(i, d-1, -1)` | 当前选择 `path` | 动作说明 |
| :-: | :--- | :-: | :--- | :--- | :--- |
| 1 | `dfs(4)` | 2 | `range(4, 1, -1)` $\rightarrow [4, 3, 2]$ | `[]` | 顶层开始探索 |
| 2 | $\hookrightarrow$ 选 4 $\rightarrow$ `dfs(3)` | 1 | `range(3, 0, -1)` $\rightarrow [3, 2, 1]$ | `[4]` | 深入第 1 层 |
| 3 | $\hookrightarrow\hookrightarrow$ 选 3 $\rightarrow$ `dfs(2)` | 0 | `len(path) == 2` (命中递归基) | `[4, 3]` | 记录快照 `ans.append([4, 3])`，回溯 |
| 4 | $\hookrightarrow\hookrightarrow$ 选 2 $\rightarrow$ `dfs(1)` | 0 | `len(path) == 2` | `[4, 2]` | 记录快照 `ans.append([4, 2])`，回溯 |
| 5 | $\hookrightarrow\hookrightarrow$ 选 1 $\rightarrow$ `dfs(0)` | 0 | `len(path) == 2` | `[4, 1]` | 记录快照 `ans.append([4, 1])`，回溯 |
| 6 | 回溯至 `dfs(4)`，选 3 $\rightarrow$ `dfs(2)` | 1 | `range(2, 0, -1)` $\rightarrow [2, 1]$ | `[3]` | 深入第 1 层 |
| 7 | $\hookrightarrow\hookrightarrow$ 选 2 $\rightarrow$ `dfs(1)` | 0 | `len(path) == 2` | `[3, 2]` | 记录快照 `ans.append([3, 2])`，回溯 |
| 8 | $\hookrightarrow\hookrightarrow$ 选 1 $\rightarrow$ `dfs(0)` | 0 | `len(path) == 2` | `[3, 1]` | 记录快照 `ans.append([3, 1])`，回溯 |
| 9 | 回溯至 `dfs(4)`，选 2 $\rightarrow$ `dfs(1)` | 1 | `range(1, 0, -1)` $\rightarrow [1]$ | `[2]` | 深入第 1 层 |
| 10 | $\hookrightarrow\hookrightarrow$ 选 1 $\rightarrow$ `dfs(0)` | 0 | `len(path) == 2` | `[2, 1]` | 记录快照 `ans.append([2, 1])`，回溯 |
| 11 | `dfs(4)` 循环结束 | - | - | `[]` | 返回全部 6 组有效组合结果 |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 | 复杂度 | 严谨数学证明与推导 |
| :--- | :---: | :--- |
| **时间复杂度** | $\mathcal{O}\left(\binom{n}{k} \cdot k\right)$ | 组合数公式总共生成 $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ 个有效叶子节点。得益于极值剪枝，搜索树中的死节点被完全修剪，每个有效解在叶子节点处执行 `path.copy()` 需要 $\mathcal{O}(k)$ 的列表复制耗时，因此总时间复杂度为严格的 $\mathcal{O}\left(\binom{n}{k} \cdot k\right)$。 |
| **空间复杂度** | $\mathcal{O}(k)$ | 递归调用栈的最大深度为 $k$，临时组合列表 `path` 占用的最大空间亦为 $k$。除返回值 `ans` 占用的存储空间外，额外辅助空间复杂度为严格的 $\mathcal{O}(k)$。 |
