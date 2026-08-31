# LC 1109: Corporate Flight Bookings | 航班预订统计

- **LeetCode ID**: LC 1109
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 03: Difference Array)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/corporate-flight-bookings/)
- **Solution File**: [`12-lc-1109-corporate-flight-bookings.py`](luffy/12-lc-1109-corporate-flight-bookings.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
There are `n` flights labeled from 1 to `n`. Given a list of flight bookings `bookings` where `bookings[i] = [first, last, seats]`, return an array `answer` of length `n` representing total seats booked for each flight.

### [CN] 中文描述
这里有 n 个航班，它们分别从 1 到 n 进行编号。有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [first, last, seats] 意味着在从 first 到 last 的每个航班上预订了 seats 个座位。请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位总数。

### Constraints / 约束条件
1 <= n <= 2 * 10^4, 1 <= bookings.length <= 2 * 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Array Basics] ➔ [Diff Array]`

```
┌────────────────────────────────────────────────────────┐
│ 差分数组区间修改: diff[first-1] += seats, diff[last] -= seats│
│ 前缀和复原原数组: ans[i] = ans[i-1] + diff[i]          │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
差分区间累加性：对差分数组进行单点增减可在前缀和还原时等价于对整个区间加值。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-1109
#corporate flight bookings

from typing import List

#[0]*n -> create a list with n elements, each element is 0

class Solution: #general way: worst case
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * n
        for first, last, seats in bookings:
            for i in range(first-1, last):
                answer[i] += seats

        return answer

#large range modify 
#use difference array

class Solution2:  #difference array
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0]*(n+1)
        for first, last, seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats
        
        answer =[0]*n
        last_Seats = 0 
        for i in range(n):
            answer[i]=last_Seats + diff[i]
            last_Seats = answer[i]
        return answer
```

1. 基于 `12-lc-1109-corporate-flight-bookings.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“差分数组适用于什么场景？”*
  - **Candidate**: 适用于频繁进行区间增减 $[l, r, val]$，且最终仅需全量查询一次最终状态的高频场景。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 1-indexed 越界 | last 越界导致 diff 数组越界 | 未校验 last < n | 当 last < n 时才扣减 diff[last] |

### Complete Dry-Run Table / 实例推演表

n=5, bookings=[[1,2,10],[2,3,20],[2,5,25]] -> diff=[10, 45, -10, 0, -25] -> ans=[10, 55, 45, 25, 25]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n + m)$ | $m$ 次区间修改 $O(1)$，单次前缀和还原 $O(n)$。 |
| **Space Complexity** | $O(n)$ | 差分数组。 |
