# LC 0021: Merge Two Sorted Lists | 合并两个有序链表

- **LeetCode ID**: LC 0021
- **Difficulty**: Easy
- **Category**: Luffy Structured Curriculum (Topic 05: Linked Lists)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/merge-two-sorted-lists/)
- **Solution File**: [`16-lc-0021-merge-two-sorted-lists.py`](luffy/16-lc-0021-merge-two-sorted-lists.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list and return its head.

### [CN] 中文描述
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### Constraints / 约束条件
两个链表的节点数目范围是 [0, 50], -100 <= Node.val <= 100

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ 哨兵头节点 + 双指针穿针引线                            │
│ dummy = ListNode(0), cur = dummy                       │
│ 比较 list1.val 与 list2.val，较小者接在 cur.next 后面  │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
升序缝合不变量：`cur` 始终指向合并链表的当前尾节点。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-21
#merge two sorted lists
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy-虚拟头节点
        dummy=ListNode()
        current=dummy
        while list1!=None and list2!=None:
            if list1.val <=list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        if list1 == None:
            current.next=list2
        else:
            current.next=list1

        return dummy.next
```

1. 基于 `16-lc-0021-merge-two-sorted-lists.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“哨兵节点 dummy 的核心价值是什么？”*
  - **Candidate**: 消除头节点为空或首次拼接时的特殊条件分支，简化代码逻辑。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 遗漏剩余链表 | while 结束后未拼接非空链表 | 遗漏拼接 | cur.next = list1 or list2 |

### Complete Dry-Run Table / 实例推演表

l1=[1,2,4], l2=[1,3,4] -> dummy->1->1->2->3->4->4

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n + m)$ | 两链表节点总数。 |
| **Space Complexity** | $O(1)$ | 原地拼接复用节点。 |
