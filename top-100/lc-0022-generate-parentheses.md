# LeetCode 22. Generate Parentheses (括号生成)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 括号有效性前缀不变量 / 剪枝优化 / 卡特兰数)
- **Tags:** String, Dynamic Programming, Backtracking
- **Corresponding Python File:** [`top-100/lc-0022-generate-parentheses.py`](top-100/lc-0022-generate-parentheses.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.
* **[CN]** 数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

### Constraints / 约束条件
* $1 \le n \le 8$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 括号有效性前缀平衡不变量 (Prefix Balance Invariant):                     │
│    • 任意合法括号序列的长度为 2n，且在任意前缀位置 i 中：                   │
│      左括号数量 >= 右括号数量 (count('(') >= count(')'))                     │
│    • 当填入的左括号总数达到 n 时，不可再填左括号 (open_count < n)。          │
│    • 当已填右括号数小于已填左括号数时，方可填入右括号 (close < open_count)。│
│ 2. 状态空间树剪枝 (State-Space Tree Pruning):                               │
│    • 总序列长度为 2n，暴力穷举共有 2^(2n) 种二进制序列。                    │
│    • 利用前缀合法性守卫，仅在合法分支递归，将搜索树压缩至卡特兰数 Cn 个有效叶子。│
│ 3. 定长路径原位覆盖优化 (In-Place Buffer Overwrite Invariant):               │
│    • 预先开辟 path = [""] * (2n)，第 i 层直接写入 path[i] = '(' 或 ')'，    │
│      递归返回天然被后续兄弟节点覆盖，避免频繁的字符串拼接与列表拷贝。        │
│ 4. 空间与递归深度 (O(n) Stack Depth):                                       │
│    • 递归树最大深度为 2n，系统调用栈与辅助路径空间均严格为 O(n)。            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 宏观拓扑图谱归属 (Topology Node Macro Anchor)
`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

---

### 🧠 回溯组合思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Backtracking & Sequence Generation Family Tree (回溯与序列构造思维谱系)   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Base Primitive 1: LC 20 Valid Parentheses                                  │
│  └─ 核心识别: 栈模型与平衡不变量 —— 任何时刻右括号不能多于左括号             │
│        │                                                                    │
│  Base Primitive 2: LC 17 Letter Combinations of a Phone Number              │
│  └─ 核心识别: 定长递归树构建与原位覆盖 path = [""] * m                      │
│        │                                                                    │
│        ▼                                                                    │
│  Level 2 (In-Flight Pruning / Valid Sequence): LC 22 Generate Parentheses★ │
│  └─ 演进 Twist: 将「后验校验」前置为「实时分支剪枝」                         │
│     • 左括号剩余 > 0: 随时可选 '('                                          │
│     • 右括号剩余 > 左括号剩余: 方可选 ')' (确保任意前缀 count('(') >= count(')'))│
│        │                                                                    │
│        ├─► [演进 Twist 1: 子集与组合数筛选]                                 │
│        │   LC 78 Subsets / LC 77 Combinations                               │
│        │   └─ 元素选或不选 (0/1 树) 与剩余元素容量剪枝                      │
│        │                                                                    │
│        ├─► [演进 Twist 2: 目标和无限/有限重复]                              │
│        │   LC 39 / LC 40 Combination Sum I & II                             │
│        │   └─ 递归分支中累加和剪枝 + 同层去重                               │
│        │                                                                    │
│        └─► [演进 Twist 3: 二维网格路径与棋盘状态决策]                       │
│            LC 79 Word Search / LC 51 N-Queens                               │
│            └─ 空间标记与多维约束冲突检测回溯                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🧠 形式化逻辑推演 (Catalan Number & Mathematical Proof)

设 $n$ 对括号构成的合法组合数为 $C_n$（即第 $n$ 个卡特兰数，Catalan Number）。

1. **组合数学公式 (Closed-form Formula)**:
   $$C_n = \frac{1}{n+1} \binom{2n}{n} = \frac{(2n)!}{(n+1)!\,n!}$$

2. **渐近增长量级 (Stirling Approximation)**:
   根据斯特林公式（Stirling's approximation $n! \approx \sqrt{2\pi n}(\frac{n}{e})^n$），卡特兰数的渐近阶为：
   $$C_n \sim \frac{4^n}{n\sqrt{\pi n}} = \mathcal{O}\left(\frac{4^n}{n^{1.5}}\right)$$

3. **Dyck 路径与折线法 (Reflection Principle)**:
   * 将 `(` 视为向右上步进 $(+1, +1)$，`)` 视为向右下步进 $(+1, -1)$。
   * 从 $(0, 0)$ 出发走到 $(2n, 0)$ 且始终不穿过 $y=0$ 下方的路径数，严格等于 $C_n$。
   * 前 $n$ 项数值：
     * $n=1 \implies C_1 = 1$ (`"()"`)
     * $n=2 \implies C_2 = 2$ (`"(())"`, `"()()"`)
     * $n=3 \implies C_3 = 5$ (`"((()))"`, `"(()())"`, `"(())()"`, `"()(())"`, `"()()()"`)
     * $n=4 \implies C_4 = 14$
     * $n=8 \implies C_8 = 1430$

---

### 🎨 ASCII 决策剪枝搜索树 (`n = 2, m = 4`)

```
                                  dfs(i=0, open_count=0) ["", "", "", ""]
                                                |
                                        path[0] = '('
                                                |
                                  dfs(i=1, open_count=1) ["(", "", "", ""]
                                     /                          \
                          path[1] = '('                     path[1] = ')'
                                 /                                  \
             dfs(i=2, open_count=2) ["((", "", ""]             dfs(i=2, open_count=1) ["()", "", ""]
                   |                                           /               \
             path[2] = ')'                              path[2] = '('      [path[2]=')' 剪枝]
                   |                                         /            (close=2 > open_count=1 ❌)
             dfs(i=3, open_count=2) ["(()", ""]         dfs(i=3, open_count=2) ["()(", ""]
                   |                                         |
             path[3] = ')'                             path[3] = ')'
                   |                                         |
             dfs(i=4, open_count=2)                          dfs(i=4, open_count=2)
                "(())" (✓)                                "()()" (✓)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`top-100/lc-0022-generate-parentheses.py`](top-100/lc-0022-generate-parentheses.py) 中的 baseline 结构进行逐行逻辑剖析：

```python
from typing import List, Optional

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1. 计算总字符长度 m = 2 * n (n 对括号共有 2n 个字符)
        m = n * 2
        ans = []
        # 2. 预先开辟定长字符路径列表，避免深层递归中的字符串频繁拼接与拷贝开销
        path = [""] * m 

        # 3. 定义回溯递归函数:
        #    i: 当前正在填充 path 的下标 (0 <= i <= m)
        #    open_count: 当前路径中已填入的左括号 '(' 数量
        def dfs(i, open_count):
            # 递归基 (Base Case): 当填满 m 个位置时，当前 path 构成一个完整合法的括号组合
            if i == m:
                ans.append("".join(path))
                return

            # 分支 1: 只要已填左括号数量未达到 n，就可以在当前位置填入 '('
            if open_count < n:
                path[i] = "("
                dfs(i + 1, open_count + 1)
            
            # 分支 2: 当已填右括号数量 (i - open_count) 小于已填左括号数量 (open_count) 时，方可填入 ')'
            # 注: 当前已填入的总字符数为 i，其中 open_count 个是左括号，因此已填右括号数 close = i - open_count
            # 合法放右括号的约束为: close < open_count 即 i - open_count < open_count (等价于 i < 2 * open_count)
            if i - open_count < open_count:
                path[i] = ")"
                dfs(i + 1, open_count)

        # 4. 从下标 0、已用左括号 0 开始搜索
        dfs(0, 0)
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 剩余计数法（Remaining Count）与字符串参数传递写法

* **面试官**：除了使用 `open_count` 已填计数与定长数组原位覆盖，面试中很多候选人喜欢用 `left_rem` 与 `right_rem`（剩余可用左/右括号数），这种模式该如何书写？
* **候选人解析**：
  * 维护 `left`（剩余可用左括号数）和 `right`（剩余可用右括号数）。
  * 初始状态 `left = n, right = n`。
  * **选左括号条件**：`left > 0` $\implies$ `dfs(left - 1, right, cur + "(")`。
  * **选右括号条件**：`right > left`（说明已填入的左括号比右括号多，有未闭合的左括号） $\implies$ `dfs(left, right - 1, cur + ")")`。

```python
# 附: 剩余计数法模板 (Remaining Count Template)
class SolutionRemainingCount:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(left: int, right: int, cur: str) -> None:
            if len(cur) == 2 * n:
                ans.append(cur)
                return
            
            # 只要还有剩余左括号，就可以放 '('
            if left > 0:
                dfs(left - 1, right, cur + "(")
            # 只有当剩余右括号严格大于剩余左括号时，才能放 ')'
            if right > left:
                dfs(left, right - 1, cur + ")")
                
        dfs(n, n, "")
        return ans
```

---

### 追问 2: 动态规划 / 分治结构分解法 (Divide & Conquer / DP)

* **面试官**：能否不使用回溯 DFS，而是通过子问题的组合关系（动态规划 / 分治）自底向上构造？
* **候选人解析**：
  * 任意一个长度为 $2n$ 的合法括号序列 $S$，其最左边的第一个字符必定是 `'('`。
  * 这个 `'('` 必定有且仅有一个与之匹配的闭合 `')'`。
  * 设这个匹配的 `')'` 出现在位置 $2k + 1$，则该括号内部包裹着一个由 $k$ 对括号构成的合法序列 $A$，而其右侧紧跟着一个由 $n - 1 - k$ 对括号构成的合法序列 $B$（其中 $0 \le k < n$）。
  * **状态转移方程**：
    $$\mathcal{S}_n = \bigcup_{k=0}^{n-1} \left\{ \text{"("} + a + \text{")"} + b \;\middle|\; a \in \mathcal{S}_k, \; b \in \mathcal{S}_{n-1-k} \right\}$$

```python
# 附: 动态规划分治构造模板 (Divide & Conquer DP Template)
class SolutionDP:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        
        for i in range(1, n + 1):
            for k in range(i):
                # k 对括号在内部，(i - 1 - k) 对括号在外部
                for left_str in dp[k]:
                    for right_str in dp[i - 1 - k]:
                        dp[i].append(f"({left_str}){right_str}")
                        
        return dp[n]
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **右括号剪枝变量误写 (`open_count < open_count`)** | 输出全为空或仅有左括号报错 | 条件误将 `close < open_count`（即 `i - open_count < open_count`）误敲为 `open_count < open_count`，导致右括号分支永远为 `False` 无法进入 | 明确定义变量：`close = i - open_count`，守卫条件严格为 `if close < open_count:` |
| **前缀失衡提前闭合 (`close > open_count`)** | 输出无效括号序列如 `")("`, `"())("` | 允许在右括号数超过左括号数时生成分支，破坏前缀平衡不变量 | 严格限制放右括号的前提是未闭合左括号数 $>0$，即 `close < open_count` |
| **递归触底未加 `return`** | 抛出 `IndexError: list assignment index out of range` | 命中 `i == m` 收集答案后未中断，继续执行后续赋值 `path[i]` | 触底 `ans.append` 后必须立即执行 `return` |
| **递归参数累加副作用 (`open_count += 1`)** | 兄弟分支状态污染，生成错乱组合 | 在调用前执行 `open_count += 1` 而回溯时未复原 `open_count -= 1` | 保持纯函数传参 `dfs(i + 1, open_count + 1)`，或在修改后显式回溯撤销 |

---

### 🔍 全流程推演表 (Dry-Run Matrix for $n = 2$)

| 递归调用栈 (Call Stack) | 当前下标 $i$ | 已放左括号 `open_count` | 已放右括号 `close` ($i - open\_count$) | 当前 `path` 状态 | 决策分支与动作 (Decision) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `dfs(0, 0)` | 0 | 0 | 0 | `["", "", "", ""]` | `open_count < 2` $\implies$ `path[0]='('`, 递归 `dfs(1, 1)` |
| ├── `dfs(1, 1)` | 1 | 1 | 0 | `["(", "", "", ""]` | `open_count < 2` $\implies$ `path[1]='('`, 递归 `dfs(2, 2)`<br>`close < 1` $\implies$ `path[1]=')'`, 递归 `dfs(2, 1)` |
| │   ├── `dfs(2, 2)` | 2 | 2 | 0 | `["(", "(", "", ""]` | `open_count == 2` (不可放左); `close(0) < 2` $\implies$ `path[2]=')'`, 递归 `dfs(3, 2)` |
| │   │   └── `dfs(3, 2)` | 3 | 2 | 1 | `["(", "(", ")", ""]` | `close(1) < 2` $\implies$ `path[3]=')'`, 递归 `dfs(4, 2)` |
| │   │       └── `dfs(4, 2)` | 4 | 2 | 2 | `["(", "(", ")", ")"]` | $i == 4 \implies$ 收集 **`"(())"`**，`return` |
| │   └── `dfs(2, 1)` | 2 | 1 | 1 | `["(", ")", "", ""]` | `open_count(1) < 2` $\implies$ `path[2]='('`, 递归 `dfs(3, 2)`<br>`close(1) == open_count(1)` (不可放右) |
| │       └── `dfs(3, 2)` | 3 | 2 | 1 | `["(", ")", "(", ""]` | `close(1) < 2` $\implies$ `path[3]=')'`, 递归 `dfs(4, 2)` |
| │           └── `dfs(4, 2)` | 4 | 2 | 2 | `["(", ")", "(", ")"]` | $i == 4 \implies$ 收集 **`"()()"`**，`return` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}\left(\dfrac{4^n}{\sqrt{n}}\right)$ | 有效括号组合的总数严格等于第 $n$ 个卡特兰数 $C_n = \frac{1}{n+1}\binom{2n}{n} \sim \mathcal{O}\left(\frac{4^n}{n\sqrt{n}}\right)$。<br>在回溯剪枝树中，所有生成的中间状态节点数量与合法叶子节点数量同阶，每个叶子节点执行一次长度为 $2n$ 的字符串复制 `"".join(path)` 需要 $\mathcal{O}(n)$ 时间。<br>因此总时间复杂度为 $\mathcal{O}(C_n \cdot n) = \mathcal{O}\left(\frac{4^n}{\sqrt{n}}\right)$。<br>当 $n=8$ 时，$C_8 = 1430$，总运算步骤 $< 3 \times 10^4$，耗时 $< 2\text{ms}$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(n)$ | 不计存储最终答案列表的输出空间：<br>1. 系统递归调用栈的深度固定为 $2n$；<br>2. 预先开辟的原位字符覆盖数组 `path` 的长度固定为 $2n$。<br>因此辅助空间开销严格为线性 $\mathcal{O}(n)$。 |
