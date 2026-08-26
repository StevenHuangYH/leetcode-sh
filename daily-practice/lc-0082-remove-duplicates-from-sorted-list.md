# LeetCode 82. Remove Duplicates from Sorted List II (删除排序链表中的重复元素 II)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (哨兵哑节点 / 跨越整段重复子链 / 前驱指针悬停)
- **Tags:** Linked List, Two Pointers
- **Corresponding Python File:** [`daily-practice/lc-0082-remove-duplicates-from-sorted-list.py`](daily-practice/lc-0082-remove-duplicates-from-sorted-list.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return the linked list **sorted** as well.
* **[CN]** 给定一个已排序的链表的头 `head` ， *删除原始链表中所有重复数字的节点，只留下不同的数字* 。返回 *已排序的链表* 。

### Constraints / 约束条件
* 链表中节点数目在范围 $[0, 300]$ 内
* $-100 \le \text{Node.val} \le 100$
* 题目数据保证链表已经按 **升序** 排列

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 核心挑战与与 LC 83 的本质区别 (Core Difference vs LC 83):                 │
│    • LC 83: 重复元素【保留 1 个副本】，头节点必然安全，无需哨兵 dummy。       │
│    • LC 82: 重复元素【全部删除 / 0 个保留】，头节点可能被抹除，必须用 dummy！│
│ 2. 双步探路不变量 (Two-Step Lookahead Invariant):                           │
│    • 指针 cur 始终停留在【绝对安全且已确认保留的节点】（初始为 dummy）。    │
│    • 每次探测接下来的两个节点: cur.next 与 cur.next.next。                   │
│    • 若 cur.next.val == cur.next.next.val: 发现重复段！                      │
│      记录 val，用内部 while 循环一口气架空所有值为 val 的连续节点。          │
│      【关键注意: 剔除后 cur 绝不前进】，因为新接上的 cur.next 可能仍是重复段! │
│    • 若值不相等: cur.next 确认为独立唯一节点，安全后移 cur = cur.next。     │
│ 3. 极致时空: 严格单趟扫描 O(N) 时间，O(1) 额外空间。                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

### 🧠 链表去重演进思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Deduplication Evolution (链表去重思维谱系演化树)              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Keep 1 Copy): LC 83 Remove Duplicates from Sorted List            │
│  └─ 核心概念: 单指针相邻对比，遇到相同就跳过后继，头节点恒保留 (无需 dummy)。│
│        │                                                                    │
│        ▼ [演进 Twist: 全部剔除 (0 副本)，引入哨兵与前驱悬停 (本题 ★)]       │
│  Level 2 (Eradicate Duplicates): LC 82 Remove Duplicates from Sorted List II│
│  └─ 不变量 (Invariant): dummy 哨兵 + 探路 2 步 + 内部循环跨越整段重复子链。 │
│        │                                                                    │
│        ▼ [演进 Twist: 区间局部翻转与分段治理]                               │
│  Level 3 (Segment Mutation): LC 92 & LC 25 Reverse Linked List II & k-Group │
│  └─ 不变量 (Invariant): 哨兵 dummy 维护段前驱 p0，分组断链与整体重接。      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：为什么剔除整段重复节点后，`cur` 不能向后移动？

考虑输入链表为 `[1, 2, 2, 3, 3, 4]`，指针 `cur` 处于节点 `[1]`：

```
初始状态:
    dummy ──► [1] ──► [2] ──► [2] ──► [3] ──► [3] ──► [4] ──► None
               ▲       ▲       ▲
              cur    cur.next  cur.next.next (值相等 2 == 2)

═════════════════════════════════════════════════════════════════════
执行整段删除:
    记录 val = 2，内部 while 循环架空所有值为 2 的节点:
    dummy ──► [1] ──────────────────► [3] ──► [3] ──► [4] ──► None
               ▲                       ▲       ▲
              cur                   cur.next  cur.next.next

═════════════════════════════════════════════════════════════════════
【核心关键】此时 cur 依然停在 [1]：
    新的 cur.next 是 [3]，cur.next.next 也是 [3]！
    因为 cur 没移动，下一轮外层循环可以立刻检测出 [3, 3] 这一段新的重复子链！

若此时错误执行 cur = cur.next:
    cur 会跳到第一个 [3] 上，导致第一个 [3] 被当作唯一节点保留下来，产生严重 Bug！
```

---

### 🎨 ASCII 完整去重推演图解

以输入 `head = [1, 2, 3, 3, 4, 4, 5]` 为例：

```
Step 0: 构建 dummy 哨兵，cur 指向 dummy
    dummy ──► [1] ──► [2] ──► [3] ──► [3] ──► [4] ──► [4] ──► [5] ──► None
      ▲        ▲       ▲
     cur    cur.next  cur.next.next (1 != 2, 不重复)
    -> 安全推进: cur = cur.next

═════════════════════════════════════════════════════════════════════
Step 1: cur 移动到 [1]
    dummy ──► [1] ──► [2] ──► [3] ──► [3] ──► [4] ──► [4] ──► [5] ──► None
               ▲       ▲       ▲
              cur   cur.next  cur.next.next (2 != 3, 不重复)
    -> 安全推进: cur = cur.next

═════════════════════════════════════════════════════════════════════
Step 2: cur 移动到 [2]
    dummy ──► [1] ──► [2] ──► [3] ──► [3] ──► [4] ──► [4] ──► [5] ──► None
                       ▲       ▲       ▲
                      cur   cur.next  cur.next.next (3 == 3, 重复!)
    -> 记录 val = 3，内部 while 跨过所有 3
    dummy ──► [1] ──► [2] ───────────► [4] ──► [4] ──► [5] ──► None
                       ▲                ▲       ▲
                      cur            cur.next  cur.next.next
    -> cur 保持在 [2]

═════════════════════════════════════════════════════════════════════
Step 3: cur 仍在 [2]，探测到 4 == 4 (重复!)
    -> 记录 val = 4，内部 while 跨过所有 4
    dummy ──► [1] ──► [2] ──────────────────► [5] ──► None
                       ▲                       ▲
                      cur                   cur.next
    -> cur.next.next 为 None，外层循环终止！

最终返回 dummy.next: [1] ──► [2] ──► [5] ──► None
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
        # 1. 创建哨兵哑节点 dummy，next 指向 head
        #    作用: 消除原链表头节点可能因为重复而被彻底删除的特判逻辑
        dummy = ListNode(next =  head)
        
        # 2. cur 指针初始化指向 dummy
        #    不变量: cur 始终指向当前已经确认无重复、确定保留的链表节点末尾
        cur = dummy
        
        # 3. 探路 2 步: 只要 cur 后面至少还有 2 个节点，才能比较是否存在重复值
        while cur.next and cur.next.next:
            # 4. 取出紧跟在 cur 后面的节点值
            val = cur.next.val
            
            # 5. 比较紧邻的两个后继节点值是否相等
            if cur.next.next.val == val:
                # 6. 发现重复段: 启动内部 while 循环，跨越所有值为 val 的连续节点
                #    条件 cur.next 保证不发生空指针异常
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
                # 注意: 循环结束后，cur 保持不动，留在原位等待下一轮检验新接上的 cur.next
            else:
                # 7. 两个后继节点值不相等: 说明 cur.next 是唯一的独立节点，安全推进
                cur = cur.next

        # 8. 返回 dummy.next (即真正去重后的链表头节点)
        return dummy.next
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: LC 83 与 LC 82 核心逻辑对比表

| 考察维度 (Dimension) | LC 83 (保留 1 份副本) | LC 82 (完全删除重复元素 / 0 副本) |
| :--- | :--- | :--- |
| **头节点是否需要 dummy** | ❌ 不需要 (头节点必定被保留) | ✅ 必须使用 (头节点本身可能被全删) |
| **探路步数** | 1 步 (`cur.next`) | 2 步 (`cur.next and cur.next.next`) |
| **指针推进时机** | `cur.next.val != cur.val` 时后移 | `cur.next.next.val != cur.next.val` 时后移 |
| **删除操作** | `cur.next = cur.next.next` (单次架空) | `while cur.next.val == val: cur.next = cur.next.next` (整段跨越) |

---

### 追问 2: 能否使用递归 (Divide and Conquer) 优雅实现 LC 82？

* **面试官**：如果让你用纯递归函数写出 LC 82，代码该如何组织？
* **候选人解析**：
  * **递归基 (Base Case)**：若 `not head or not head.next`，无重复可能，直接返回 `head`。
  * **分支 1 (发现重复)**：若 `head.val == head.next.val`，使用 while 循环跳过所有值为 `head.val` 的节点，得到首个新值节点 `cur`，然后直接返回对 `cur` 递归去重的结果 `self.deleteDuplicates(cur)`（原 `head` 及其所有同值副本被彻底丢弃）。
  * **分支 2 (无重复)**：若 `head.val != head.next.val`，`head` 确认保留，递归连接后续链表 `head.next = self.deleteDuplicates(head.next)`，返回 `head`。

```python
# 附: 递归解法 (Recursive Elegant Approach)
class SolutionRecursive:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        if head.val == head.next.val:
            # 找到首个不同值的后续节点
            cur = head.next
            while cur and cur.val == head.val:
                cur = cur.next
            return self.deleteDuplicates(cur)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
```
* **复杂度权衡**：迭代法空间为严格 $O(1)$，递归法由于递归调用栈空间为 $O(N)$，面试中首推迭代双指针。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **缺少 `dummy` 哨兵** | 输入 `[1, 1, 2]` 返回 `[1, 2]`，头节点的重复项未被清除 | 原 `head` 自身也是重复节点，缺少指向 `head` 的前驱节点导致无法架空头节点 | 必须创建 `dummy = ListNode(next=head)`，`cur` 从 `dummy` 开始运行 |
| **跨越重复段后错误执行 `cur = cur.next`** | 输入 `[1, 2, 2, 3, 3, 4]` 返回 `[1, 3, 4]` (节点 3 未被删除) | 删除了 `[2, 2]` 之后 `cur` 盲目后移，跳过了新接上的 `[3, 3]` 的重复检测 | 剔除重复段后保持 `cur` 不动，仅在 `else`（两后继值不相等）时推进 `cur` |
| **内部 while 循环漏写 `cur.next` 判空** | 输入 `[1, 2, 3, 3]` 尾部重复时抛出 `AttributeError: 'NoneType' has no attribute 'val'` | 遍历至链表最末尾节点后，`cur.next` 变为 `None`，继续读取 `.val` 发生崩溃 | 内部 while 条件严格声明 `while cur.next and cur.next.val == val:` |
| **空间复杂度退化为 $O(N)$ (使用哈希表计数)** | 面试官追问 $O(1)$ 原地空间时无法应对 | 依赖了无序链表的频次统计字典，未利用输入已排序的升序性质 | 牢记升序链表重复元素必相邻的性质，采用双步探路原地指针跳过 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 初始状态 (Initial State) | 循环步数与操作过程 (Step-by-Step Actions) | 最终返回值 (Return Value) |
| :--- | :--- | :--- | :--- |
| **空链表 `head = []`** | `dummy.next = None` | `cur.next` 为 `None`，while 循环不执行 | `None` (通过) |
| **全重复节点 `[1, 1, 1]`** | `dummy -> [1] -> [1] -> [1]` | ① 检测到 `1 == 1` $\rightarrow$ 跨过所有 1 (`dummy.next = None`)<br>② `cur.next` 为 `None`，退出循环 | `None` (通过) |
| **头部有重复 `[1, 1, 2]`** | `dummy -> [1] -> [1] -> [2]` | ① 检测到 `1 == 1` $\rightarrow$ 跨过所有 1 (`dummy.next = [2]`)<br>② 检测 `cur.next.next` 为 `None`，退出循环 | `[2]` (通过) |
| **全唯一节点 `[1, 2, 3]`** | `dummy -> [1] -> [2] -> [3]` | ① 1 != 2 $\rightarrow$ `cur = [1]`<br>② 2 != 3 $\rightarrow$ `cur = [2]`<br>③ `cur.next.next` 为 `None`，退出 | `[1, 2, 3]` (通过) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | $N$ 为链表节点总数。虽然代码存在内外两层 `while` 循环，但每个链表节点在整个执行流程中最多只被指针访问常数次（要么被 `cur` 遍历一次，要么在内部 while 中被跳过一次）。总操作步数严格线性于 $N$，故时间复杂度为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 算法只申请了 1 个哨兵 `dummy` 节点以及常数个基本类型变量（`cur`, `val`），直接就地修改原链表节点的指针指向，未占用任何依赖于 $N$ 的辅助空间，额外空间复杂度严格为 $\mathcal{O}(1)$。 |
