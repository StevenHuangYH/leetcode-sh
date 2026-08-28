# LeetCode 92. Reverse Linked List II (反转链表 II)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (单链表局部区间反转 / 哨兵头节点 / 3 指针穿针引线 / 前驱指针定位)
- **Tags:** Linked List
- **Corresponding Python File:** [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.
* **[CN]** 给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。

### Constraints / 约束条件
* 链表中节点数目为 `n`
* $1 \le n \le 500$
* $-500 \le \text{Node.val} \le 500$
* $1 \le \text{left} \le \text{right} \le n$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 哨兵前驱定位不变量 (Sentinel & p0 Invariant):                            │
│    • 创建 dummyNode = ListNode(next=head)，p0 = dummyNode。                 │
│    • p0 向前走 left - 1 步，严格停在【待反转区间的前驱节点】。                │
│ 2. 标准 3 指针区间反转 (Subsegment Reversal):                               │
│    • 迭代 right - left + 1 次，执行标准 3 指针反转 (LC 206 原语)。           │
│ 3. 缝合拼接双重赋值不变量 (Reconnection Invariant):                         │
│    • 反转后：pre 成为区间新头，cur 成为区间后继首节点。                       │
│    • p0.next (原区间首节点，现为区间尾节点) 的 next 指向 cur: p0.next.next = cur│
│    • p0.next 指向新区间头节点 pre: p0.next = pre                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件 [`daily-practice/lc-0092-reversed-linked-list-2.py`](daily-practice/lc-0092-reversed-linked-list-2.py) 中的实现进行逐行深入解析：

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # 1. 设立虚拟哨兵头节点，完美处理 left = 1 涉及头节点反转的边界情况
        dummyNode = ListNode(next=head)
        p0 = dummyNode

        # 2. 定位 p0 到待反转区间的前一个节点 (步进 left - 1 步)
        for _ in range(left - 1):
            p0 = p0.next

        # 3. 局部区间标准 3 指针反转，共执行 (right - left + 1) 次
        pre = None
        cur = p0.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # 4. 核心缝合重新连线
        p0.next.next = cur # 原区间的首节点（现为尾部）连接到剩余链表 cur
        p0.next = pre      # 前驱节点 p0 连接到反转后的新头节点 pre

        return dummyNode.next
```

---

## 4. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(n)$ | 单次遍历链表定位 $p_0$ 并反转 $right - left + 1$ 个节点，最多访问 $n$ 个节点一次，严格为 $\mathcal{O}(n)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 仅使用 `dummyNode`, `p0`, `pre`, `cur`, `nxt` 几个指针变量，就地修改指针，额外空间为 $\mathcal{O}(1)$。 |
