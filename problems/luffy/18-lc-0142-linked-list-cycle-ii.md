# LC 0142: Linked List Cycle II | 环形链表 II

- **LeetCode ID**: LC 0142
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 05: Linked Lists)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/linked-list-cycle-ii/)
- **Solution File**: [`18-lc-0142-linked-list-cycle-ii.py`](problems/luffy/18-lc-0142-linked-list-cycle-ii.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

### [CN] 中文描述
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

### Constraints / 约束条件
链表中节点的数目范围在范围 [0, 10^4] 内

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

```
┌────────────────────────────────────────────────────────┐
│ 数学推导与入环点相遇                                   │
│ 快慢指针相遇时：快指针走 2k 步，慢指针走 k 步          │
│ 距离关系: a = c + (n-1)(b+c) -> a ≡ c (mod L)          │
│ 让指针从 head 与 相遇点 同步单步走，必在入环点相遇     │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
步长等式定理：从头节点到入环点的距离 $a$ 等于从相遇点到入环点的距离 $c$ 加上若干整圈数。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
#lc-142
#listed-list-cycle
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Initialize Pointers / 初始化指针
        # Both slow and fast pointers start at the head of the linked list.
        # 慢指针和快指针都从链表头节点开始。
        slow = head
        fast = head
        
        # 2. Detect the Cycle / 检测环的存在
        # Move slow by 1 step and fast by 2 steps.
        # 每次让慢指针走1步，快指针走2步。
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, a cycle exists.
            # 如果快慢指针相遇，说明链表中存在环。
            if slow == fast:
                
                # 3. Find the Cycle Entrance / 寻找环的入口
                # The distance from the head to the cycle's entrance equals 
                # the distance from the meeting point to the entrance.
                # 从链表头部到环入口的距离，正好等于从相遇点到环入口的距离。
                point1 = head
                point2 = slow
                
                # Move both pointers 1 step at a time until they meet.
                # 两个新指针每次各走1步，直到它们再次相遇。
                while point1 != point2:
                    point1 = point1.next
                    point2 = point2.next
                    
                # 4. Return Result / 返回结果
                # The node where they meet is the start of the cycle.
                # 它们相遇的节点就是环的起始入口节点。
                return point1
                
        # If the loop finishes without returning, it means we reached the end of the list (no cycle).
        # 如果循环结束都没有相遇（遇到了 None），说明走到了链表尽头，不存在环。
        return None
```

1. 基于 `18-lc-0142-linked-list-cycle-ii.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“推导为什么 a = c？”*
  - **Candidate**: 慢指针路程 $s = a + b$，快指针路程 $f = a + n(b+c) + b = 2(a+b)$，化简得 $a = (n-1)(b+c) + c$。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 返回 True 替代节点 | 题目要求返回节点引用 | 返回值类型错误 | 返回相遇节点指针 |

### Complete Dry-Run Table / 实例推演表

相遇后 ptr1=head, ptr2=meetNode -> 同速前进 -> meet at cycle entry

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 相遇前 $O(n)$，找入环点 $O(n)$。 |
| **Space Complexity** | $O(1)$ | 常数指针。 |
