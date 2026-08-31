# LeetCode 131. Palindrome Partitioning (分割回文串)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (回溯算法 / 字符串切片分割 / 回文串动态验证 / 回溯三问)
- **Tags:** String, Dynamic Programming, Backtracking
- **Corresponding Python File:** [`problems/daily-practice/lc-0131-palindrome-partitioning.py`](problems/daily-practice/lc-0131-palindrome-partitioning.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of `s`*.
* **[CN]** 给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是 **回文串** 。返回 `s` 所有可能的分割方案。

### Constraints / 约束条件
* $1 \le \text{s.length} \le 16$
* `s` 仅由小写英文字母组成。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 字符串分割的隔板模型 (Divider Partition Model):                          │
│    • 长度为 n 的字符串共有 n - 1 个可用切分间隙 (隔板)。                     │
│    • 每个间隙选或不选切分，理论存在 2^(n-1) 种分割方案。                     │
│ 2. 经典「回溯三问」模型 (The Three Core Questions of Partition):             │
│    • ① 当前操作？ 枚举当前子串右边界 j in [i, n-1]，提取子串 t = s[i:j+1]；  │
│                   若 t 为回文串，则加入 path.append(t)。                    │
│    • ② 子问题？   从下标 >= i 的后缀字符串中构造所有可能的回文分割方案。     │
│    • ③ 下一个子问题？ 从下标 >= j + 1 的后缀字符串中构造回文分割方案。        │
│ 3. 递归基与整串覆盖不变量 (Full Coverage Base Case Invariant):               │
│    • 只有当起始索引 i == n 时，才代表整个字符串被完全且合法地分割完毕，       │
│      此时必须执行 ans.append(path.copy()) 记录快照并 return。                │
│ 4. 状态还原对称性 (State Restoration Invariant):                             │
│    • 严格维持 path.append(t) -> dfs(j + 1) -> path.pop() 的对称结构。         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

### 🧠 字符串回溯分割思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 String Partition & Backtracking Lineage (字符串回溯分割谱系演化图)       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Direct Power Set): LC 78 Subsets                                  │
│  └─ 集合子集枚举: 每个元素选或不选 / 枚举下一个元素下标                      │
│        │                                                                    │
│        ▼ [演进 Twist 1: 连续子串切分 + 谓词约束 (Substring Validation)]      │
│  Level 2 (Conditional Partition): LC 131 Palindrome Partitioning (本题★)    │
│  └─ 约束切分: 枚举右端点 j in range(i, n)，仅当 s[i:j+1] 为回文时递归 dfs(j+1)│
│        │                                                                    │
│        ├─► [演进 Twist 2: 固定段数 + 数值范围约束 (Fixed Segments)]          │
│        │   LC 93 Restore IP Addresses                                       │
│        │   └─ 策略: 限制恰好切分为 4 段，且每段数值在 [0, 255] 无前导零     │
│        │                                                                    │
│        ├─► [演进 Twist 3: 词典字典树匹配切分 (Dictionary Match)]             │
│        │   LC 140 Word Break II                                             │
│        │   └─ 策略: 仅当 s[i:j+1] 在 wordDict 中时递归 dfs(j+1)             │
│        │                                                                    │
│        └─► [演进 Twist 4: 从枚举方案转为求最优步数 (Min Cut DP)]             │
│            LC 132 Palindrome Partitioning II                                │
│            └─ 策略: 放弃回溯穷举，改用 1D DP + 预处理回文矩阵求最少分割次数 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 ASCII 回溯搜索树推演图解 (`s = "aab"`)

```
                               dfs(0) [全串 "aab"]
                             /                    \
                     j=0: t="a" (回文✓)         j=1: t="aa" (回文✓)   j=2: t="aab" (非回文✗ 剪枝)
                         /                            \
                     dfs(1) ["ab"]                   dfs(2) ["b"]
                   /               \                      |
           j=1: t="a" (✓)      j=2: t="ab" (✗)       j=2: t="b" (✓)
               /                                          |
           dfs(2) ["b"]                                dfs(3) [到达末尾 i == 3]
              |                                           |
           j=2: t="b" (✓)                            ans.append(["aa", "b"]) (✓)
              |
           dfs(3) [到达末尾 i == 3]
              |
           ans.append(["a", "a", "b"]) (✓)
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`problems/daily-practice/lc-0131-palindrome-partitioning.py`](problems/daily-practice/lc-0131-palindrome-partitioning.py) 中的实现进行逐行深入解析：

```python
from typing import List

# 回溯三问核心框架：
# 1. 当前操作？选择当前后缀的一个前缀回文子串 s[i...j]，加入 path
# 2. 子问题？  从下标 >= i 的后缀字符串中构造所有的回文分割方案
# 3. 下一个子问题？从下标 >= j + 1 的剩余后缀中构造回文分割方案

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        path = []
        n = len(s)

        # dfs(i) 表示当前正在处理从下标 i 开始的后缀子串 s[i...n-1]
        def dfs(i):
            # 递归基 (Base Case):
            # 当 i == n 时，说明已经顺利切分到字符串末尾，path 中是一组完整的合法回文分割
            if i == n:
                ans.append(path.copy()) # 必须对 path 进行浅拷贝快照
                return 

            # 枚举以 i 为起始、j 为结束的所有子串 s[i...j]
            for j in range(i, n):
                t = s[i:j + 1]  # 提取前闭后开切片 [i, j+1) 即 s[i...j]
                
                # 核心剪枝验证：只有当当前子串是回文串时，才继续深入递归
                if t == t[::-1]:
                    path.append(t) # 做出选择：将当前回文子串加入当前分割路径
                    dfs(j + 1)     # 递归子问题：从下一个未被切分的位置 j + 1 继续切分
                    path.pop()     # 回溯：撤销选择，恢复现场，尝试更长的右边界 j

        # 从下标 0 开始启动递归搜索
        dfs(0)
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 双指针切片 `t == t[::-1]` 每次需 $\mathcal{O}(L)$ 时间，如何用 DP 预处理矩阵优化？

* **面试官**：在 `dfs` 过程中每次都执行 `t == t[::-1]` 会产生重复的反转与切片开销。如何预处理回文状态将单次判定的时间复杂度降至 $\mathcal{O}(1)$？
* **候选人解析**：
  * **二维 DP 预处理**：定义布尔矩阵 `is_pal[i][j]` 表示子串 `s[i...j]` 是否为回文串。
  * **状态转移方程**：
    $$\text{is\_pal}[i][j] = (s[i] == s[j]) \land (j - i \le 2 \lor \text{is\_pal}[i+1][j-1])$$
  * **遍历顺序**：$i$ 从 $n-1$ 逆序遍历到 $0$，$j$ 从 $i$ 正序遍历到 $n-1$。
  * **优化收益**：在 `dfs` 中直接查询 `if is_pal[i][j]:`，将每次字符串拷贝与比较的耗时从 $\mathcal{O}(n)$ 彻底消除为 $\mathcal{O}(1)$。

```python
# 附: DP 预处理加速回溯模板 (DP Table Acceleration Template)
class SolutionDPPrecomputed:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 1. 预处理 O(n^2) 回文 DP 矩阵
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    
        ans = []
        path = []
        
        # 2. O(1) 判定回溯
        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                if is_pal[i][j]: # O(1) 快速查询
                    path.append(s[i:j + 1])
                    dfs(j + 1)
                    path.pop()
                    
        dfs(0)
        return ans
```

---

### 追问 2: LC 131 (分割方案) 与 LC 132 (最少分割次数) 算法选择有何本质区别？

* **面试官**：很多候选人混淆 LC 131 与 LC 132。这两道题在算法设计上有什么核心分水岭？
* **候选人解析**：
  * **LC 131（本题）**：要求输出**所有具体的分割方案**（解集规模指数级），必须使用**回溯穷举**。
  * **LC 132（分割回文串 II）**：仅要求输出**最少分割次数**（单个数值极值问题）。若继续使用回溯会严重超时（TLE），必须使用**一维动态规划**：
    $$dp[i] = \min_{0 \le j \le i, \text{is\_pal}[j][i]} (dp[j - 1] + 1)$$
    在 $\mathcal{O}(n^2)$ 时间内解决。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **递归传递错误下标 `dfs(i + 1)`** | 递归无限陷入死循环，报 `RecursionError: maximum recursion depth exceeded` | 混淆了当前循环变量 `j` 与外层起始变量 `i`，导致子串边界无法向前推进 | 递归下一层必须传入 `dfs(j + 1)` |
| **切片上界偏移 `s[i:j]`** | 漏掉末尾字符，无法生成完整原串的分割 | Python 切片 `s[i:j]` 不包含下标 `j` 的字符 | 闭区间 $[i, j]$ 切片必须写为 `s[i:j + 1]` |
| **结果集未浅拷贝** | 最终输出 `[[], [], ...]` 全为空列表 | `ans.append(path)` 存入的是列表引用，后续回溯 `pop` 彻底清空了内容 | 必须存入列表快照：`ans.append(path.copy())` |
| **非回文未剪枝直接递归** | 输出中包含了非回文子串（如 `["a", "ab"]`） | 缺少 `if t == t[::-1]:` 条件判断 | 只有在当前切出的子串为回文时才执行 `path.append` 与递归 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 字符特征 | 递归深度与分支情况 | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **单字符 `s = "a"`** | $n = 1$ | 仅 1 层递归，`t="a"` 是回文 $\rightarrow$ 命中 `i == 1` | `[["a"]]` |
| **全同字符 `s = "aaa"`** | $n = 3$ | 所有子串全为回文，包含 4 种全量分割形态 | `[["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]]` |
| **无重复字符 `s = "abc"`** | $n = 3$ | 仅单字符为回文，多字符分支全部被剪枝 | `[["a", "b", "c"]]` |
| **标准用例 `s = "aab"`** | $n = 3$ | 包含单字符与双字符回文 | `[["a", "a", "b"], ["aa", "b"]]` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n \cdot 2^n)$ | 其中 $n$ 为输入字符串 `s` 的长度。长度为 $n$ 的字符串有 $n-1$ 个切分位置，最坏情况下（如 `s = "aaaa"` 全同字符），共有 $2^{n-1}$ 种合法的分割方案。对于每种方案：<br>1. 递归路径深度最多为 $n$；<br>2. 验证回文切片与执行 `path.copy()` 需要 $\mathcal{O}(n)$ 时间。<br>因此总时间复杂度严格为 $\mathcal{O}(n \cdot 2^n)$。在题目约束 $n \le 16$ 时，总计算步数 $\approx 16 \times 65536 \approx 10^6$，耗时 $< 20\text{ms}$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(n)$ | 不计用于保存最终所有合法分割方案的输出列表：<br>1. 系统递归调用栈的深度最大为 $n$；<br>2. 临时路径列表 `path` 在任意时刻最多存储 $n$ 个子串。<br>因此额外辅助空间复杂度严格为 $\mathcal{O}(n)$。 |
