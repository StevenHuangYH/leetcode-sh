# LC 0056: Merge Intervals | 合并区间

- **LeetCode ID**: LC 0056
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 04: Intervals)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/merge-intervals/)
- **Solution File**: [`13-lc-0056-merge-intervals.py`](luffy/13-lc-0056-merge-intervals.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given an array of `intervals` where `intervals[i] = [start, end]`, merge all overlapping intervals, and return an array of the non-overlapping intervals.

### [CN] 中文描述
以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [start, end]` 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组 。

### Constraints / 约束条件
1 <= intervals.length <= 10^4, intervals[i].length == 2, 0 <= start <= end <= 10^4

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures / Recursive Traverse] ➔ [Other] ➔ [Greedy]`

```
┌────────────────────────────────────────────────────────┐
│ 排序 + 贪心合并                                        │
│ 按 start 升序排序                                      │
│ 若 cur.start <= prev.end: prev.end = max(prev.end, cur.end) │
│ 否则开启新区间                                         │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
左端点有序性：排序后相交区间必在数组中相邻连续出现。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-56
#Merge Intervals
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

      #need to be sorted first
        # def get_start_num(nums):
        #     return nums[0]
        # intervals.sort(get_start_num)

        #or use lambda [input : return] simplify funtion express
        intervals.sort(key=lambda x:x[0])


        #merge
        res = []
        i=0
        cur = intervals[0]

        while i+1<len(intervals):
            next=intervals[i+1]
            if cur[1]>=next[0]:  #overlapped
                cur[1]=max(cur[1],next[1])
            else: #if not overlapped
                res.append(cur)
                cur=next
            i=i+1
        res.append(cur)
            
        return res
```

1. 基于 `13-lc-0056-merge-intervals.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果区间已经是按右端点排序的，该如何合并？”*
  - **Candidate**: 可以从后向前遍历反向合并，或者依然提取并检查相邻重叠。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 未更新 max(end) | 直接用 cur.end 覆盖导致大区间被缩小 | 未取 max | 必须使用 max(ans[-1][1], interval[1]) |

### Complete Dry-Run Table / 实例推演表

[[1,3],[2,6],[8,10]] -> [1,3]+[2,6] -> [1,6], [8,10] 不重叠 -> [[1,6],[8,10]]

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n \log n)$ | 区间排序耗时。 |
| **Space Complexity** | $O(n)$ | 存储合并结果。 |
