# LC 0739: Daily Temperatures (Monotonic Stack) | 每日温度 (单调栈基石)

- **LeetCode ID**: LC 0739
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 06: Monotonic Stack)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/daily-temperatures-(monotonic-stack)/)
- **Solution File**: [`20-lc-0020-valid-parentheses-dict.py`](luffy/20-lc-0020-valid-parentheses-dict.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature.

### [CN] 中文描述
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。

### Constraints / 约束条件
1 <= temperatures.length <= 10^5, 30 <= temperatures[i] <= 100

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Data Structures] ➔ [Stack & Queue]`

```
┌────────────────────────────────────────────────────────┐
│ 单调递减栈 (Monotonic Decreasing Stack)                │
│ 栈内存放下标，保持对应温度单调递减                     │
│ 遇到更高温度 x 时，持续弹出栈顶元素并结算天数差        │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
单调性结算：当前温度高于栈顶温度时，栈顶元素的下一个更大值已被确定为当前索引。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#  lc-739-daily temperature

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]: 
        stack=[]
        n = len(temperatures)
        answer = [0]*n

        for i in range(n):
            cur_temperature = temperatures[i]

            while True:
                # comparing the current temperature with the past temp
                if stack!=[] and cur_temperature > temperatures[stack[-1]]:
                    pre_index=stack.pop()
                    answer[pre_index]=i-pre_index 
                else:
                    break

            stack.append(i)

        return answer


if __name__ == '__main__':
    s=Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])
```

1. 基于 `20-lc-0020-valid-parentheses-dict.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“单调栈适合解决什么类别的题目？”*
  - **Candidate**: 适合在 $O(n)$ 时间内寻找序列中每个元素左侧/右侧的第一个更大/更小元素（Next Greater Element）。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 栈内存放数值而非下标 | 无法计算下标天数差 | 存储内容失误 | 栈内应存储元素下标 i |

### Complete Dry-Run Table / 实例推演表

temperatures=[73,74,75,71,69,72,76,73] -> ans=[1,1,4,2,1,1,0,0]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 每个元素入栈出栈最多各一次。 |
| **Space Complexity** | $O(n)$ | 单调栈与输出数组。 |
