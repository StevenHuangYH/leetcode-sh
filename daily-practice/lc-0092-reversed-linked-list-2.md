# LC 0092: Reverse Linked List II | 反转链表 II

- **LeetCode ID**: LC 0092
- **Difficulty**: Medium
- **Source Link**: [LeetCode Problem](https://leetcode.com/problems/reverse-linked-list-ii/)
- **Solution File**: [lc-0092-reversed-linked-list-2.py](file:///mnt/c/Users/steve/iCloudDrive/Desktop/leetcode-sh/daily-practice/lc-0092-reversed-linked-list-2.py)

---

## 1. Problem Statement & Constraints / 题目描述与约束

### [EN] English Description
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

### [CN] 中文描述
给你单链表的头指针 `head` 和两个整数 `left` 和 `right` ，其中 `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 反转后的链表 。

### Constraints / 约束条件
- 链表中节点数目为 `n`
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

---

## 2. Core Idea, Mental Model & Pattern Lineage / 核心思维模型与算法谱系

### 算法思维谱系演化图 (ASCII Pattern Lineage Map)

```
┌────────────────────────────────────────────────────────┐
│ LC 206 Reverse Linked List (全局反转)                  │
│ 核心三指针: nxt = cur.next, cur.next = prev, 整体推进  │
└───────────────────────────┬────────────────────────────┘
                            │ 引入区间限制与哨兵节点
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 92 Reverse Linked List II (区间局部反转 - 本题)     │
│ 1. 哨兵 dummy 处理 left = 1 边界                       │
│ 2. 找到 p0 = left - 1 节点                             │
│ 3. 反转 right - left + 1 个节点                        │
│ 4. 重新缝合: p0.next.next = cur, p0.next = prev        │
└───────────────────────────┬────────────────────────────┘
                            │ 推广为循环分段反转
                            ▼
┌────────────────────────────────────────────────────────┐
│ LC 25 Reverse Nodes in k-Group (K个一组反转链表)       │
└────────────────────────────────────────────────────────┘
```

### 核心思维模型与数学不变量

为了处理反转起点为头节点（`left = 1`）的边界情况，必须引入**哨兵节点 (Dummy Node)** `dummy = ListNode(next=head)`。
整个过程分为三大步骤：
1. **定位反转前驱节点 `p0`**：从 `dummy` 走 `left - 1` 步，停在待反转区间的前一个节点。
2. **执行区间反转**：标准三指针迭代反转 `right - left + 1` 次。
3. **首尾缝合 (Re-linking)**：
   - 反转前的区间起点（此时为反转后的尾部）`p0.next` 连接到未反转部分的起点 `cur`：`p0.next.next = cur`。
   - `p0` 指向反转后的新头部 `prev`：`p0.next = prev`。

```
     p0        (反转前区间)                cur
     [1] ──> [2] ──> [3] ──> [4] ──> [5]
             prev (反转后)
     
     缝合后:
     [1] ──────> [4] ──> [3] ──> [2] ──────> [5]
      p0         prev            p0.next      cur
```

---

## 3. Step-by-Step Code Walkthrough / 源码逐行精析

基于用户原版 Python 代码逐行拆解：

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        cur = p0.next
        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        p0.next.next = cur
        p0.next = prev

        return dummy.next
```

1. **哨兵节点创建与前驱定位**：
   - `dummy = ListNode(next=head)`
   - `for _ in range(left - 1): p0 = p0.next`: `p0` 停在反转区间的前驱。
2. **标准链表反转循环**：
   - 循环 `right - left + 1` 次，使用 `nxt, cur, prev` 翻转指针方向。
   - 循环结束后，`prev` 指向反转后区间的头，`cur` 指向未反转区间的第一个节点。
3. **两步缝合**：
   - `p0.next.next = cur`: 将反转后的尾巴连接到后续链表。
   - `p0.next = prev`: 将前驱连接到反转后的新头部。
4. **返回**：`return dummy.next`。

---

## 4. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

- **Interviewer**: *“如果不使用头插法或三指针，如何用递归方式反转前 N 个节点？”*
  - **Candidate Response**: 定义 `reverseN(head, n)` 递归翻转前 `n` 个节点并记录第 `n+1` 个后继节点 `successor`。当 `left == 1` 时直接调用 `reverseN(head, right)`；当 `left > 1` 时递归调用 `head.next = self.reverseBetween(head.next, left - 1, right - 1)`。

---

## 5. The Error Log & Complete Dry-Run / 错题排查与实例推演

### Anti-Patterns & Defensive Fixes (反模式诊断表)

| 常见陷阱 / Buggy Pattern | 典型报错与失效场景 | 根本原因 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
|---|---|---|---|
| 缝合顺序颠倒 | `AttributeError: NoneType has no attribute next` | 先执行 `p0.next = prev` 会覆盖原本指向老头部的 `p0.next` | 必须先执行 `p0.next.next = cur`，再执行 `p0.next = prev` |
| 未使用 dummy 处理 `left = 1` | 当 `left = 1` 时无前驱节点导致逻辑分支繁琐 | 头节点发生变更时没有统一的前驱哨兵 | 强制引入 `dummy = ListNode(next=head)` 统一边界 |

### Complete Dry-Run Table / 实例推演表

输入: `head = [1, 2, 3, 4, 5], left = 2, right = 4`

| Step | Operation | `p0` | `prev` | `cur` | Pointers Status |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Init | 走 `left-1=1` 步 | 1 | None | 2 | `p0.next = 2` |
| Rev 1 | 反转 2 | 1 | 2 | 3 | `2 -> None` |
| Rev 2 | 反转 3 | 1 | 3 | 4 | `3 -> 2 -> None` |
| Rev 3 | 反转 4 | 1 | 4 | 5 | `4 -> 3 -> 2 -> None` |
| Link 1 | `p0.next.next = cur` | 1 | 4 | 5 | `2 -> 5` |
| Link 2 | `p0.next = prev` | 1 | 4 | 5 | `1 -> 4 -> 3 -> 2 -> 5` |

---

## 6. Complexity Analysis / 复杂度分析

| Dimension | Complexity | Mathematical Rationale |
|---|---|---|
| **Time Complexity** | $O(n)$ | 仅单趟遍历链表，最坏情况下走 $right$ 步，时间与节点数线性相关。 |
| **Space Complexity** | $O(1)$ | 原地指针修改，仅创建固定的常数级辅助节点与指针。 |
