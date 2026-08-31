# LeetCode 3. Longest Substring Without Repeating Characters (无重复字符的最长子串)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (滑动窗口 / 双指针 / 动态伸缩窗口 / 哈希计数去重)
- **Tags:** Hash Table, String, Sliding Window
- **Corresponding Python File:** [`problems/top-100/lc-0003-longest-substring-without-repeating-characters.py`](problems/top-100/lc-0003-longest-substring-without-repeating-characters.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given a string `s`, find the length of the **longest substring** without duplicate characters.
* **[CN]** 给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

### Constraints / 约束条件
* $0 \le 	ext{s.length} \le 5 	imes 10^4$
* `s` 由英文字母、数字、符号和空格组成。

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 窗口无重复字符不变量 (No-Duplicate Window Invariant):                    │
│    • 任意时刻，窗口 s[left...right] 内所有字符的计数 cnt[c] 必须 <= 1。      │
│ 2. 右扩张与左收缩单调性 (Monotonic Sliding Window):                         │
│    • 右指针 right 逐位右移，将字符加入窗口 cnt[c] += 1。                     │
│    • 若触发 cnt[c] > 1，左指针 left 必须持续右移并扣减计数，直至冲突消除。    │
│ 3. 动态极值结算 (Maximum Length Calculation):                               │
│    • 恢复合法状态后，窗口长度为 right - left + 1，实时更新 ans = max(ans, ...)。 │
│ 4. 边界处理: 空字符串 s = "" 时自然返回 0。                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures] ➔ [Two Pointers] ➔ [Sliding Window]`

### 🧠 滑动窗口思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Sliding Window & Two Pointers Lineage (滑动窗口思维谱系图)                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Fixed Window): LC 643 Maximum Average Subarray I                  │
│  └─ 定长窗口: 窗口大小固定为 k，右进左出平移                                │
│        │                                                                    │
│        ▼ [演进 Twist 1: 不定长动态伸缩窗口 (Dynamic Shrink)]                │
│  Level 2 (Dynamic Window / No Repeat): LC 3 Longest Substring (本题★)       │
│  └─ 核心: 出现重复字符时，left 持续右移直至窗口内无重复字符                 │
│        │                                                                    │
│        ├─► [演进 Twist 2: 允许最多 k 次重复/替换 (At Most K)]               │
│        │   LC 3090 (最多2次) / LC 424 Longest Repeating Character           │
│        │   └─ 策略: 仅当 cnt[c] > k 时才收缩 left                           │
│        │                                                                    │
│        └─► [演进 Twist 3: 子数组乘积/求和约束 (Monotonic Math Constraint)]   │
│            LC 209 (和>=target最短) / LC 713 (积<k方案数)                    │
│            └─ 策略: 基于单调数值累加/累乘控制 left 伸缩                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎨 ASCII 滑动窗口状态迁移图解 (`s = "pwwkew"`)

```
Step 1: right=0, c='p' -> cnt={'p':1} -> [p] (len=1, ans=1)
Step 2: right=1, c='w' -> cnt={'p':1, 'w':1} -> [p, w] (len=2, ans=2)
Step 3: right=2, c='w' -> cnt={'p':1, 'w':2} 冲突！
        left=0 ('p'): cnt['p']-=1, left=1
        left=1 ('w'): cnt['w']-=1, left=2
        -> [w] (len=1, ans=2)
Step 4: right=3, c='k' -> [w, k] (len=2, ans=2)
Step 5: right=4, c='e' -> [w, k, e] (len=3, ans=3)
Step 6: right=5, c='w' -> cnt['w']=2 冲突！left=2 ('w') 移出 -> [k, e, w] (len=3, ans=3)
最终最长无重复子串长度 = 3 ("wke")
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`problems/top-100/lc-0003-longest-substring-without-repeating-characters.py`](problems/top-100/lc-0003-longest-substring-without-repeating-characters.py) 中的实现进行逐行深入解析：

```python
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter() # 1. 初始化哈希频数表 (字符 -> 出现次数)
        left = 0        # 2. 初始化滑动窗口左边界
        
        # 3. 枚举窗口右边界 right 与当前字符 c
        for right, c in enumerate(s):
            cnt[c] += 1 # 将当前字符加入窗口，频数加 1
            
            # 4. 核心收缩逻辑：若 c 出现冲突 (频数 > 1)，左边界持续右移吐出字符
            while cnt[c] > 1:
                cnt[s[left]] -= 1 # 将窗口最左侧字符计数减 1
                left += 1         # 左指针右移
                
            # 5. 当前窗口 [left, right] 必无重复字符，更新最长子串长度
            ans = max(ans, right - left + 1)
            
        return ans
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 使用哈希表记录字符最新下标实现 $\mathcal{O}(1)$ 快速左指针跳跃？

* **面试官**：当前解法中 `while cnt[c] > 1` 需要一步步移动 `left`。能否让 `left` 直接跳跃到重复字符的下一个位置？
* **候选人解析**：
  * 使用字典 `last_pos` 记录每个字符**上一次出现的索引**。
  * 遇到字符 `c` 时，若 `c in last_pos`，直接将左指针跳转到 `max(left, last_pos[c] + 1)`，避免逐步累加。

```python
# 附: 下标直跳优化模板 (Index Jump Optimization)
class SolutionIndexJump:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_pos = {}
        left = 0
        ans = 0
        for right, c in enumerate(s):
            if c in last_pos:
                left = max(left, last_pos[c] + 1)
            last_pos[c] = right
            ans = max(ans, right - left + 1)
        return ans
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **下标跳跃未取 `max`** | 跳到了窗口左边界更左侧的历史重复字符，导致 `left` 逆行 | 历史字符位置可能小于当前 `left` | 必须写为 `left = max(left, last_pos[c] + 1)` |
| **忘记扣减 `cnt[s[left]]`** | 循环内未更新移出字符的频数，死循环 | 左指针移出时未同步维护哈希表 | 每次 `left += 1` 前必须执行 `cnt[s[left]] -= 1` |
| **空字符串返回 1** | 输入 `""` 时错误返回 `1` | 默认 `ans` 初始值设置错误 | `ans` 必须初始为 `0` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 字符特征 | 窗口行为 | 最终输出 (Output) |
| :--- | :--- | :--- | :---: |
| **空串 `""`** | 长度 0 | 循环不执行 | `0` |
| **全同字符 `"bbbbb"`** | 长度 5 | 每次右移均触发左移，窗口最大为 1 | `1` |
| **无重复 `"abcde"`** | 长度 5 | 从未触发收缩，窗口一路扩展到 5 | `5` |
| **标准用例 `"abcabcbb"`** | 长度 8 | `"abc"` 长度为 3 | `3` |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 其中 $n$ 为字符串长度。每个字符最多被 `right` 访问加入窗口一次，最多被 `left` 访问移出窗口一次。左右指针均单调向右移动，总操作步数不超过 $2n$，因此时间复杂度严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(|\Sigma|)$ | 其中 $|\Sigma|$ 为字符集大小（ASCII 字符集 $|\Sigma| \le 128$）。哈希表 `cnt` 存储窗口中出现的不同字符，最多占用常数空间 $\mathcal{O}(1)$（若任意字符集则为 $\mathcal{O}(\min(n, |\Sigma|))$）。 |
