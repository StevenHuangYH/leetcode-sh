# LC 0059: Spiral Matrix II (Alternative / Linked List Model) | 螺旋矩阵 II (变体与链表基石)

- **LeetCode ID**: LC 0059
- **Difficulty**: Medium
- **Category**: Luffy Structured Curriculum (Topic 01: Matrix & Linked List Pre)
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/spiral-matrix-ii-(alternative-/-linked-list-model)/)
- **Solution File**: [`09-lc-0059-spiral-matrix-ii-alt.py`](luffy/09-lc-0059-spiral-matrix-ii-alt.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Foundational node definitions and traversal alternatives for spiral structures and list elements.

### [CN] 中文描述
螺旋矩阵与链表基础节点的结构定义及遍历变体模型。

### Constraints / 约束条件
1 <= n <= 20

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

```
┌────────────────────────────────────────────────────────┐
│ 链表节点与矩阵结构演进模型                             │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量
指针单向链式引用不变量：`node.next` 形成单向链条。

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast: # 相遇
                point1=head
                point2=slow
                while point1!=point2:
                    point1=point1.next
                    point2=point2.next

                # 此时point1 和 point2 相遇在 入口
                return point1

        # 此时说明没有 环
        return None
```

1. 基于 `09-lc-0059-spiral-matrix-ii-alt.py` 原版源码拆解核心数据结构与初始化。
2. 按关键循环与状态转移推进算法主体逻辑。
3. 维护核心不变状态并返回最终有效解。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“链表结构与二维矩阵扁平化的联系？”*
  - **Candidate**: 二维矩阵在行主序映射下可看作步长为 $n$ 的跳表或链式索引。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 空指针异常 | 访问 None.val | 未判空 | 操作前必须先判空 |

### Complete Dry-Run Table / 实例推演表

ListNode(1) -> ListNode(2)

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(1)$ | 节点初始化。 |
| **Space Complexity** | $O(1)$ | 单个节点分配。 |
