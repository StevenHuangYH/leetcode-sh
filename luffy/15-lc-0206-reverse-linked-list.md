# LC 0206: Reverse Linked List | 反转链表

- **LeetCode ID**: LC 0206
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 05: Linked Lists)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/reverse-linked-list/)
- **Solution File**: [`15-lc-0206-reverse-linked-list.py`](luffy/15-lc-0206-reverse-linked-list.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

### [CN] 中文描述
给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

### Constraints / 约束条件
节点数介于 0 到 5000

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ 三指针迭代反转: prev=None, curr=head                   │
│ nxt = curr.next; curr.next = prev; prev = curr; curr = nxt│
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
反转拓扑不变量：`prev` 始终指向已反转链表的新头节点。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cur=None 
#         while head!=None:
#             cur =ListNode(head.val,cur)
#             head=head.next

#         return cur



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        
        while head!=None:
            next_node=head.next
            head.next=pre
            pre=head
            head=next_node
        return pre
```

1. 基于 `15-lc-0206-reverse-linked-list.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如何用递归方式实现？”*
  - **Candidate**: 递归反转 `head.next` 后让 `head.next.next = head; head.next = None` 并返回新头。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 成环丢失 | 未断开原头节点 next | 未设 prev=None | 初始 prev 必须为 None |

### Complete Dry-Run Table / 实例推演表

1->2->3 -> 1<-2 3 -> 1<-2<-3 -> return 3

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 单遍遍历链表节点。 |
| **Space Complexity** | $O(1)$ | 迭代仅需常数级指针。 |
