# LC 0131: Palindrome Partitioning | 分割回文串

- **LeetCode ID**: LC 0131
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 08: Backtracking)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/palindrome-partitioning/)
- **Solution File**: [`36-lc-0131-palindrome-partitioning.py`](problems/luffy/36-lc-0131-palindrome-partitioning.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### [CN] 中文描述
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

### Constraints / 约束条件
1 <= s.length <= 16

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Traverse View] ➔ [Backtracking]`

```
┌────────────────────────────────────────────────────────┐
│ 回溯切割线: 枚举当前切割子串 s[start...i]             │
│ 若 s[start...i] 是回文: path.append(...); dfs(i + 1)   │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
回文前缀合法性：当前切割出的子串必须是回文串，才允许递归处理剩余后缀。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-131

#Palindrome Partitioning

#A palindrome is a string that reads the same forward and backward.
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def is_palindrome(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def dfs(start_index):
            if start_index>=len(s):
                result.append(path.copy())
                return

            for i in range(start_index, len(s)):
                if is_palindrome(start_index, i):
                    path.append(s[start_index:i+1])
                    dfs(i+1)
                    path.pop()


        dfs(0)
        return result


#pick or not pick solution
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def dfs(starting_index, i):
            if starting_index==len(s):
                result.append(path.copy())
                return
            if i==len(s):
                return

            #need the cur_string and check the next string
            dfs(starting_index,i+1)


            temper_str=s[starting_index:i+1]
            if temper_str==temper_str[::-1]: #string reversed
                path.append(temper_str)
                dfs(i+1,i+1)
                path.pop()


        dfs(0,0)
        return result
```

1. 基于 `36-lc-0131-palindrome-partitioning.py` 原版源码拆解核心数据结构与初始化。
2. 按关键算法循环推进主体计算逻辑与状态转移。
3. 维护核心算法不变量并返回最终有效结果。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何加速回文子串判定？”*
  - **Candidate**: 可预先使用区间 DP 预处理 $O(n^2)$ 的 `is_pal[i][j]` 表，将回文判定由 $O(n)$ 降为 $O(1)$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 切片越界 | s[start:i] 漏掉第 i 位 | 切片区间错误 | 切片必须为 s[start:i+1] |

### Complete Dry-Run Table / 实例推演表

s='aab' -> [['a','a','b'], ['aa','b']]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n \cdot 2^n)$ | $n-1$ 个切割点共有 $2^{n-1}$ 种分割方案。 |
| **Space Complexity** | $O(n)$ | 递归栈。 |
