# LC 0141: Linked List Cycle | 环形链表

- **LeetCode ID**: LC 0141
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 05: Linked Lists)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/linked-list-cycle/)
- **Solution File**: [`17-lc-0141-linked-list-cycle.py`](luffy/17-lc-0141-linked-list-cycle.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

### [CN] 中文描述
给你一个链表的头节点 `head` ，判断链表中是否有环。

### Constraints / 约束条件
链表中节点的数目范围是 [0, 10^4]

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ Floyd 快慢指针 (2:1 相对速度追击)                     │
│ slow 走 1 步，fast 走 2 步                             │
│ 若有环，相对速度为 1，fast 必在环内追上 slow           │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
相对速度追击公理：相对速度为 1 步/轮，两指针距离每轮减少 1，绝不会发生跨越穿透。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-141
#listed list cycle

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#floyd-warshall



class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False
```

1. 基于 `17-lc-0141-linked-list-cycle.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“为什么快指针每次走 2 步而不是 3 步？”*
  - **Candidate**: 每次走 2 步相对速度为 1，必相遇；若走 3 步相对速度为 2，偶数步环可能发生跨跃套圈。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空指针异常 | fast.next.next 未判空 | 空指针越界 | 循环条件必须为 fast and fast.next |

### Complete Dry-Run Table / 实例推演表

head=[3,2,0,-4], pos=1 -> slow/fast 在环内节点相遇 -> return True

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 无环 $n/2$ 步退出，有环追击距离小于环长。 |
| **Space Complexity** | $O(1)$ | 仅维护两个指针。 |
