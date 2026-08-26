# LeetCode 83. Remove Duplicates from Sorted List (删除排序链表中的重复元素)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Easy (单指针线性扫描 / 局部相邻去重 / 原地链表重链)
- **Tags:** Linked List
- **Corresponding Python File:** [`daily-practice/lc-0083-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0083-remove-duplicates-from-sorted-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list **sorted** as well.
* **[CN]** 给定一个已排序的链表的头 `head` ， *删除所有重复的元素，使每个元素只出现一次* 。返回 *已排序的链表* 。

### Constraints / 约束条件
* 链表中节点数目在范围 $[0, 300]$ 内
* $-100 \\le \\text{Node.val} \\le 100$
* 题目数据保证链表已经按 **升序** 排列

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 核心性质 (Core Characteristic):                                          │
│    • 链表已按升序排列，所有值相同的重复节点在物理上严格【连续相邻】。        │
│ 2. 遍历不变量 (Loop Invariant):                                             │
│    • 指针 cur 始终指向已确认保留的去重链表尾部节点。                         │
│    • 当 cur.next.val == cur.val: 发现相邻重复，执行 cur.next = cur.next.next │
│      【关键注意: 此时 cur 绝不前进】，继续检查新的 cur.next 是否仍与 cur 重复。│
│    • 当 cur.next.val != cur.val: 相邻不重复，安全后移 cur = cur.next。       │
│ 3. 边界鲁棒性 (Boundary Robustness):                                        │
│    • 空链表 (head is None) 或单节点链表直接返回 head。                       │
│    • 头节点必然保留（无论是否有重复，保留首个出现者），无需哨兵 dummy。       │
│ 4. 极致时空: 严格单趟扫描 O(N) 时间，O(1) 额外空间。                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 链表去重算法思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Deduplication Pattern Lineage (链表去重思维谱系演化树)        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Array In-Place): LC 26 Remove Duplicates from Sorted Array        │
│  └─ 核心概念: 快慢双指针覆盖写入，保留单份唯一元素。                          │
│        │                                                                    │
│        ▼ [演进 Twist: 单向链表指针重链，保留单个副本 (本题 ★)]               │
│  Level 2 (Single-Pointer Skip): LC 83 Remove Duplicates from Sorted List    │
│  └─ 不变量 (Invariant): cur 与 cur.next 比较，相等则架空 cur.next，不移 cur。│
│        │                                                                    │
│        ▼ [演进 Twist: 完全剔除所有重复元素，一个不留]                        │
│  Level 3 (Total Erasure + Dummy): LC 82 Remove Duplicates from Sorted List II│
│  └─ 不变量 (Invariant): 必须引入 dummy 哨兵，前驱 pre 跨越整段重复子区间。   │
│        │                                                                    │
│        ▼ [演进 Twist: 无序链表去重]                                         │
│  Level 4 (Unsorted Deduplication): LCR 024 / Hash Set Filter                │
│  └─ 不变量 (Invariant): 无法依赖相邻性，必须引入哈希表记录已见值。           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：为什么删除节点后 `cur` 不能立即后移？

假设链表为 `[1, 1, 1, 2]`，指针 `cur` 处于第一个 `1`：

```
初始状态:
    [1] ──► [1] ──► [1] ──► [2] ──► None
     ▲       ▲
    cur   cur.next (值相等 1 == 1)

═════════════════════════════════════════════════════════════════════
执行删除: cur.next = cur.next.next (架空第二个 1)
    [1] ───────────► [1] ──► [2] ──► None
     ▲                ▲
    cur            cur.next (注意: cur 依然停在第一个 1，新的 cur.next 仍为 1)

═════════════════════════════════════════════════════════════════════
若此时错误执行 cur = cur.next:
    指针会跳到第三个 1 上，导致无法检测到第一个 1 与第三个 1 之间的重复关系！

正确策略 (In-Place Retention):
    只有当 cur.next.val != cur.val 时，才允许 cur = cur.next！
```

---

### 🎨 ASCII 完整去重推演图解

以输入 `head = [1, 1, 2, 3, 3]` 为例：

```
Step 0: cur = head (指向节点 1)
    [1] ──► [1] ──► [2] ──► [3] ──► [3] ──► None
     ▲       ▲
    cur   cur.next (1 == 1, 重复!)
    -> 执行 cur.next = cur.next.next

═════════════════════════════════════════════════════════════════════
Step 1: cur 保持在原位
    [1] ──────────► [2] ──► [3] ──► [3] ──► None
     ▲               ▲
    cur           cur.next (1 != 2, 不重复)
    -> 执行 cur = cur.next

═════════════════════════════════════════════════════════════════════
Step 2: cur 移动到节点 2
    [1] ──► [2] ──► [3] ──► [3] ──► None
             ▲       ▲
            cur   cur.next (2 != 3, 不重复)
    -> 执行 cur = cur.next

═════════════════════════════════════════════════════════════════════
Step 3: cur 移动到节点 3
    [1] ──► [2] ──► [3] ──► [3] ──► None
                     ▲       ▲
                    cur   cur.next (3 == 3, 重复!)
    -> 执行 cur.next = cur.next.next

═════════════════════════════════════════════════════════════════════
Step 4: cur 保持在节点 3，此时 cur.next 为 None
    [1] ──► [2] ──► [3] ──► None
                     ▲       ▲
                    cur   cur.next (None, while 循环终止)

最终返回 head: [1] ──► [2] ──► [3] ──► None
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件中的实现进行逐行深入解析：

```python
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 边界特判: 若链表为空，无任何节点可去重，直接返回 None
        if head is None:
            return head

        # 2. 初始化工作指针 cur 指向链表头节点
        #    因为首个节点必然属于去重结果集合中的第一个元素，头指针不会被删除
        cur = head
        
        # 3. 循环遍历链表，只要当前节点的后继节点存在 (cur.next is not None)
        while cur.next:
            # 4. 判定相邻节点数值是否重复
            if cur.next.val == cur.val:
                # 5. 发现重复值: 将当前节点的 next 指向其后继的后继，架空跳过重复节点
                #    注意: 此分支下 cur 绝不向后移动，以应对连续 3 个及以上相同值的场景
                cur.next = cur.next.next
            else:
                # 6. 相邻值不相同: 当前节点确认唯一无重复，指针安全向后移动一位
                cur = cur.next

        # 7. 返回原链表头节点 head
        return head
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: LC 83 (保留一个副本) vs LC 82 (完全删除重复元素)，核心差异是什么？

* **面试官**：在 LC 82 中，如果有重复元素（例如 `[1, 2, 3, 3, 4, 4, 5]`），要求把所有重复的节点全部删掉，结果为 `[1, 2, 5]`。这两道题的解法框架有什么本质不同？
* **候选人解析**：
  * **头节点稳定性**：LC 83 中头节点绝对安全（首个元素必定保留）；而在 LC 82 中头节点自身可能是重复的（如 `[1, 1, 2]`），因此 LC 82 **必须使用 `dummy` 哨兵节点**。
  * **指针前驱控制**：LC 82 需要维护前驱指针 `pre`，遇到重复区间时通过内部 `while` 循环跨越整段相同值的节点群，执行 `pre.next = cur.next`。

```python
# 附: LC 82 进阶对比实现 (Remove All Duplicate Occurrences)
class SolutionLC82:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                # 跨越整段重复子链
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummy.next
```

---

### 追问 2: 能否使用纯函数式递归 (Recursive Post-order) 实现 LC 83？

* **面试官**：你能写出本题的递归版本吗？递归的子问题定义是什么？
* **候选人解析**：
  * **递归基 (Base Case)**：`if not head or not head.next: return head`。
  * **递推公式 (Subproblem)**：先对 `head.next` 进行去重，得到去重后的子链表 `head.next = self.deleteDuplicates(head.next)`。
  * **合并逻辑 (Merge)**：检查 `head.val` 是否与 `head.next.val` 相等；若相等，则返回 `head.next` 跳过当前 `head`；否则返回 `head`。

```python
# 附: 递归解法 (Recursive Elegant Approach)
class SolutionRecursive:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # 递归处理后续子链表
        head.next = self.deleteDuplicates(head.next)
        
        # 若当前节点与去重后子链表的头节点相同，则跳过当前节点
        return head.next if head.val == head.next.val else head
```

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **无条件后移指针 (`cur = cur.next` 放在 if 外面)** | 连续多重重复如 `[1, 1, 1, 2]` 处理后残留 `[1, 1, 2]` | 删除了一个节点后指针盲目后移，漏检了原节点的第三个及后续重复项 | 严格遵循 `if-else` 分流：仅在不相等时才执行 `cur = cur.next` |
| **循环条件写为 `while cur:`** | 遍历至链表尾节点时抛出 `AttributeError: NoneType object has no attribute val` | 尾节点的 `cur.next` 为 `None`，访问 `cur.next.val` 导致空指针异常 | 循环终止条件必须为 `while cur and cur.next:` 或提前特判后使用 `while cur.next:` |
| **未处理空链表输入 (`head is None`)** | 输入 `head = []` 时抛出 `AttributeError` | 没有空指针防御，直接执行 `cur.next` | 在入口处显式添加 `if not head: return head` 防御分支 |
| **C/C++ 内存未释放** | LeetCode/工程环境内存泄露 | 仅断开了指针链，未调用 `delete` 释放被剔除节点的堆内存 | 临时保存指针 `ListNode* tmp = cur->next; cur->next = tmp->next; delete tmp;` |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 初始状态 (Initial State) | 循环步数与操作过程 (Step-by-Step Actions) | 最终返回值 (Return Value) |
| :--- | :--- | :--- | :--- |
| **空链表 `head = []`** | `head = None` | 命中 `if head is None:` 直接返回 | `None` (通过) |
| **全相同节点 `[1, 1, 1]`** | `cur -> 1` | ① `cur.next.val == 1` $\\rightarrow$ 架空第 2 个 1 (`[1] -> [1]`)<br>② `cur.next.val == 1` $\\rightarrow$ 架空第 3 个 1 (`[1] -> None`)<br>③ `cur.next` 为 `None`，退出循环 | `[1]` (通过) |
| **全唯一无重复 `[1, 2, 3]`** | `cur -> 1` | ① `1 != 2` $\\rightarrow$ `cur = [2]`<br>② `2 != 3` $\\rightarrow$ `cur = [3]`<br>③ `cur.next` 为 `None`，退出循环 | `[1, 2, 3]` (通过) |
| **首尾均有重复 `[1, 1, 2, 3, 3]`** | `cur -> 1` | ① 删第 2 个 1 $\\rightarrow$ ② 移至 2 $\\rightarrow$ ③ 移至 3 $\\rightarrow$ ④ 删第 2 个 3 | `[1, 2, 3]` (通过) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\\mathcal{O}(N)$ | $N$ 为链表节点总数。每次循环迭代中，要么删除了一个重复节点（链表长度减少 1），要么指针 `cur` 向后移动 1 位。整个链表中的每个节点最多被访问一次，总操作次数严格上界为 $N$，故时间复杂度为 $\\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\\mathcal{O}(1)$ | 迭代算法仅使用了一个辅助指针 `cur`，直接在原链表上就地修改指针指向，未申请任何与输入规模成正比的辅助内存空间，故额外空间复杂度严格为 $\\mathcal{O}(1)$。 |
