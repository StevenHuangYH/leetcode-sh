# LeetCode 86. Partition List (分隔链表)
## Step-by-Step Code Walkthrough & Notes / 代码逐行详解与知识点总结

- **Difficulty:** Medium (双哨兵哑节点 / 链表分流重组 / 显式断链防环)
- **Tags:** Linked List, Two Pointers, partition-list
- **Corresponding Python File:** [`problems/daily-practice/lc-0086-partition.py`](problems/daily-practice/lc-0086-partition.py)

---

## 1. Problem Statement / 题目描述

* **[EN]** Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal to** `x`.
  You should **preserve the original relative order** of the nodes in each of the two partitions.
* **[CN]** 给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。
  你应当 **保留** 两个分区中每个节点的初始相对位置。

### Constraints / 约束条件
* 链表中节点的数目在范围 $[0, 200]$ 内
* $-100 \le \text{Node.val} \le 100$
* $-200 \le x \le 200$

---

## 2. Problem Blueprint & Core Invariant / 题意考点蓝图与核心不变量

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🎯 考试与面试考察核心蓝图 (Interview Blueprint)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. 核心考点：分流 (Forking) 与 缝合 (Stitching)                             │
│    • 将一条单链表根据节点值与 x 的大小关系，拆分成两条独立的逻辑子链：        │
│      - 小于链表 (Sublist 1): 收集所有 node.val < x 的节点                   │
│      - 大于等于链表 (Sublist 2): 收集所有 node.val >= x 的节点              │
│    • 最后将 Sublist 1 尾部接在 Sublist 2 头部，完成重组。                   │
│                                                                             │
│ 2. 双哨兵不变量 (Dual Sentinel Invariant):                                  │
│    • 分别为两条子链设立虚拟哑节点 (Dummy Heads): d1 与 d2。                 │
│    • 维护两个移动指针 p1, p2，始终分别指向两条子链当前的最新尾节点。         │
│    • 消除空链表插入时的各种边界特判（无需判断是否是第一个节点）。           │
│                                                                             │
│ 3. ★ 致命成环陷阱与显式断链 (Cycle Prevention & Link Severing Invariant):   │
│    • 链表重组时最大的隐形 Bug: 原链表后继指针残留导致链表成环 (Cycle)！     │
│    • 当遍历节点 p 时，如果不把 p 从原链表中解绑，原链表末尾节点若落入 d2，   │
│      而其原本指向的后继节点可能落入了 d1，缝合后直接导致环状死循环！        │
│    • 黄金法则: 节点归队前或推进时，必须显式切断后继 (p.next = None)。       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Core Idea, Mental Model & Pattern Lineage / 核心思路与思维谱系

`Topology Node: [Linear Structures] ➔ [Linked List] ➔ [Two Pointer]`

### 🧠 链表双指针分流与重组思维谱系演化树 (Pattern Lineage)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🧠 Linked List Multi-Pointer Evolution (链表多指针分合思维谱系演化树)        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 1 (Merge/归流): LC 21 Merge Two Sorted Lists                         │
│  └─ 核心概念: 两个有序链表通过双指针比较，汇入一个 Dummy 哑节点主链 (合流)。│
│        │                                                                    │
│        ▼ [演进 Twist: 逆向思维，一分为二，条件分流与重组 (本题 ★)]          │
│  Level 2 (Partition/分流): LC 86 Partition List                             │
│  └─ 不变量 (Invariant): 两个 Dummy 哨兵构建两条子链，断链防环，尾部重接。   │
│        │                                                                    │
│        ▼ [演进 Twist: 结合快慢指针取中点 + 链表反转 + 交叉合并]             │
│  Level 3 (Reorder/洗牌): LC 143 Reorder List                                │
│  └─ 不变量 (Invariant): 找中点切断 (LC 876) + 局部翻转 (LC 206) + 交错缝合。 │
│        │                                                                    │
│        ▼ [演进 Twist: 链表分治归并排序]                                     │
│  Level 4 (Sort/排序): LC 148 Sort List                                      │
│  └─ 不变量 (Invariant): 自顶向下/自底向上 Divide & Conquer，递归拆半与合并。 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 💡 核心机制：为什么必须有 `p.next = None`？（成环隐患深度剖析）

考虑输入示例 `head = [1, 4, 3, 2, 5, 2], x = 3`：

```
原链表节点分布:
   [1] (<3) ──► [4] (>=3) ──► [3] (>=3) ──► [2] (<3) ──► [5] (>=3) ──► [2] (<3) ──► None

如果不切断节点的 next 指针直接将 p 挂载到 p1 或 p2:
  • 小于 3 的链表 d1: dummy1 ──► [1] ──► [2] ──► [2]
  • 大于等于 3 的链表 d2: dummy2 ──► [4] ──► [3] ──► [5]
  
注意最后一个被处理的节点是值为 2 的节点，它被挂到了 d1。
而 d2 的末尾节点是 [5]！
在原链表中，[5] 的 next 指向的是 [2]！
如果没有在处理 [5] 或退出循环时切断 [5].next，那么 [5].next 依然牢牢指向 [2]！

此时执行缝合: p1.next = d2.next:
  d1.next 形成结构:
  [1] ──► [2] ──► [2] ──► [4] ──► [3] ──► [5]
                   ▲                       │
                   └───────────────────────┘ (死循环成环!)
  
因此，原代码中在每次迭代中采用「暂存后继、就地斩断」的优雅不变量：
  temp = p.next   # 保护后继防丢失
  p.next = None   # 斩断节点对外连接，保证被放入子链后其尾指针绝对纯净
  p = temp        # 推进主遍历指针
```

---

### 🎨 ASCII 完整分流与缝合推演图解

以 `head = [1, 4, 3, 2, 5, 2], x = 3` 为例：

```
Step 0: 初始化两个哨兵哑节点与指针
    d1 (p1) ──► None      (收集 < 3)
    d2 (p2) ──► None      (收集 >= 3)
    p 指向 [1]

═════════════════════════════════════════════════════════════════════
Step 1: p = [1] (< 3)
    p1.next = [1]; p1 = p1.next; [1].next = None
    d1 ──► [1] (p1)
    d2 ──► None (p2)
    p 推进至 [4]

═════════════════════════════════════════════════════════════════════
Step 2: p = [4] (>= 3)
    p2.next = [4]; p2 = p2.next; [4].next = None
    d1 ──► [1] (p1)
    d2 ──► [4] (p2)
    p 推进至 [3]

═════════════════════════════════════════════════════════════════════
Step 3: p = [3] (>= 3)
    p2.next = [3]; p2 = p2.next; [3].next = None
    d1 ──► [1] (p1)
    d2 ──► [4] ──► [3] (p2)
    p 推进至 [2]

═════════════════════════════════════════════════════════════════════
Step 4: p = [2] (< 3)
    p1.next = [2]; p1 = p1.next; [2].next = None
    d1 ──► [1] ──► [2] (p1)
    d2 ──► [4] ──► [3] (p2)
    p 推进至 [5]

═════════════════════════════════════════════════════════════════════
Step 5: p = [5] (>= 3)
    p2.next = [5]; p2 = p2.next; [5].next = None
    d1 ──► [1] ──► [2] (p1)
    d2 ──► [4] ──► [3] ──► [5] (p2)
    p 推进至 [2]

═════════════════════════════════════════════════════════════════════
Step 6: p = [2] (< 3)
    p1.next = [2]; p1 = p1.next; [2].next = None
    d1 ──► [1] ──► [2] ──► [2] (p1)
    d2 ──► [4] ──► [3] ──► [5] (p2)
    p 推进至 None，循环终止！

═════════════════════════════════════════════════════════════════════
Step 7: 缝合两段子链 (p1.next = d2.next)
    d1 ──► [1] ──► [2] ──► [2] ──► [4] ──► [3] ──► [5] ──► None
                             p1       d2.next

最终返回 d1.next，得到完美按序分隔后的链表！
```

---

## 4. Step-by-Step Code Walkthrough / 代码逐行详解

基于原 Python 文件中的权威实现进行逐行剖析：

```python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # 1. 创建两个哨兵哑节点 (Dummy Heads)
        #    d1: 作为所有小于 x 的节点子链的哨兵头
        #    d2: 作为所有大于或等于 x 的节点子链的哨兵头
        d1 = ListNode(-1)
        d2 = ListNode(-1)

        # 2. 初始化双移动指针，分别对准两条子链的尾端
        #    不变量: p1 永远指向 d1 子链当前的最后一个节点
        #            p2 永远指向 d2 子链当前的最后一个节点
        p1 = d1
        p2 = d2

        # 3. p 作为原链表的遍历指针，从头节点 head 出发
        p = head

        # 4. 单趟遍历原链表，分流所有节点
        while p:
            # 5. 条件分支: 节点值大于或等于 x，分流到 d2 链表
            if p.val >= x:
                p2.next = p
                p2 = p2.next

            # 6. 条件分支: 节点值小于 x，分流到 d1 链表
            else:
                p1.next = p
                p1 = p1.next

            # 7. ★ 防环核心三步法 (Severing the link):
            #    temp 提前保存原链表中 p 的后继节点
            temp = p.next
            #    断开 p 的 next 指针，保证新加入子链的尾节点干净无外部牵连
            p.next = None
            #    将遍历指针 p 推进至下一个待处理节点
            p = temp

        # 8. 链表缝合 (Stitch):
        #    将小于链表的尾端 p1.next 接到大于等于链表的首个真实节点 d2.next
        p1.next = d2.next

        # 9. 返回小于链表的首个真实节点 (若小于链表为空，d1.next 此时会自动指向 d2.next)
        return d1.next
```

---

## 5. Interview Simulation: Alternative Paradigms & Follow-up Pivots / 面试官追问演练

### 追问 1: 必须在循环体内步步断链 (`p.next = None`) 吗？能否在循环外批量断链？

* **面试官**：我看你在循环内部每次都写了 `temp = p.next; p.next = None; p = temp`。如果我不每步都断开，有没有更紧凑的写法？
* **候选人解析**：
  * **完全可行！** 在循环内部如果不断链，`p1` 和 `p2` 只是贪心地往后挂载原节点。
  * 当循环全部结束时，`p1` 链表的尾部会在下一步被 `p1.next = d2.next` 覆盖，因此 `p1` 的原尾指针不会造成成环风险。
  * **但是，`p2` 链表的最后一个节点**（即 `p2` 本身）如果在原链表中的下一个节点恰好落入了 `p1`，其 `.next` 指针依然保留着旧引用，从而形成闭环！
  * 因此，只需在循环退出后，**强制令 `p2.next = None`**，即可一劳永逸切断潜在闭环。

```python
# 附: 循环后一次性截断写法 (Post-Loop Single Severing Alternative)
class SolutionAlternative:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1, d2 = ListNode(-1), ListNode(-1)
        p1, p2 = d1, d2
        p = head
        
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
            
        # ★ 关键一步: 手动斩断大于等于子链的尾指针，避免成环
        p2.next = None
        # 缝合
        p1.next = d2.next
        return d1.next
```

* **方案权衡**：
  * 原代码的「步步清空」风格防御性极强，随时保证子链节点引用纯净；
  * 「循环后统一截断 `p2.next = None`」代码行数更精炼少写一个 `temp` 变量，两者在时空效率上完全一致。

---

### 追问 2: 本题的分隔与快速排序 (QuickSort) 中的 Partition 有何本质差异？

| 维度 (Dimension) | LC 86 链表分隔 (Linked List Partition) | 经典数组快排划分 (Array Partition / Lomuto / Hoare) |
| :--- | :--- | :--- |
| **稳定性 (Stability)** | **必须保持相对顺序 (Stable)** | 通常为非稳定划分 (Unstable，原地交换破坏相对顺序) |
| **实现机制** | 利用指针将节点接入两个虚拟头链表，拼接即可 | 在连续内存数组中进行前后双指针交换 (`swap`) |
| **空间开销** | 原地修改指针，额外空间严格 $\mathcal{O}(1)$ | 原地交换同样为 $\mathcal{O}(1)$，但若强求稳定需 $\mathcal{O}(N)$ 辅助数组 |
| **核心启示** | 链表的指针动态链接特性使得「稳定划分」极其廉价自然 | 数组的随机访问优势适合二分交换，但不适合稳定插入移动 |

---

### 追问 3: 如果原链表中所有节点都 $< x$ 或都 $\ge x$，代码会出现空指针异常吗？

* **面试官**：请分析极端情况：如果输入链表的所有节点值都大于等于 $x$（即小于链表为空），你的代码是如何正确处理的？
* **候选人解析**：
  * 若所有节点都 $\ge x$，则整个循环中 `d1` 从未挂载任何新节点，`p1` 始终停留在 `d1`。
  * 循环结束后执行 `p1.next = d2.next`，即 `d1.next = d2.next`。
  * 最终返回 `d1.next`，恰好直接返回了 `d2.next`（即完整的包含所有 $\ge x$ 节点的链表头）！
  * 反之，若所有节点都 $< x$，$d2.next$ 始终为 `None`，缝合后 `p1.next = None`，返回完整的 $d1.next$。
  * **结论**：双哨兵哑节点设计天生消除了一切分支特判，代码具有极高鲁棒性。

---

## 6. The Error Log & Complete Dry-Run / 错题排查与实例推演

### ⚠️ The Error Log: Anti-Patterns & Defensive Fixes (反模式诊断表)

| 典型错误模式 (Buggy Pattern) | 触发场景 & 异常表现 (Symptom) | 根因分析 (Root Cause) | 防御性修复与不变量 (Defensive Fix) |
| :--- | :--- | :--- | :--- |
| **未切断尾节点后继造成死循环成环** | 提交时抛出 `Memory Limit Exceeded` 或链表遍历无限循环 | 大于等于链表末尾节点的原 `next` 依然指向某个小于 $x$ 的节点，缝合后导致闭环 | 在循环中执行 `p.next = None`，或在循环结束后强制 `p2.next = None` |
| **未使用哨兵哑节点 (Dummy Heads)** | 处理空链表或首节点即需要被转移时出现 `AttributeError: 'NoneType'` | 缺少哨兵导致需要为两个子链分别特判第一个节点的初始化逻辑，极易漏判 | 必须初始化 `d1 = ListNode(-1)` 与 `d2 = ListNode(-1)`，统一节点挂载逻辑 |
| **缝合拼接方向颠倒** | 返回链表结果截断或小于分区丢失 | 错误地将 `p2.next = d1.next` 或 `d1.next = d2.next`（混淆了指针游标与哨兵节点） | 严格遵守拓扑缝合不变量：小于链表的末端游标接大于链表首节点 `p1.next = d2.next` |
| **尝试就地交换节点值 (`val`)** | 面试直接判定不合格，大对象节点拷贝开销过大 | 误用数组思维去修改节点数值，违背了链表考察指针结构重构的核心意图 | 严格操作节点的 `.next` 指针，完成原位指针拓扑重组 |

---

### 🔍 极端边界用例推演 (Dry-Run Matrix)

| 输入用例 (Input Case) | 分隔基准 $x$ | 执行过程剖析 (Execution Trace) | 返回结果 (Result) |
| :--- | :---: | :--- | :--- |
| **空链表 `head = []`** | $x = 0$ | $p$ 初始为 `None`，循环不执行；`p1.next = d2.next` ($None$)；返回 `d1.next` | `[]` (通过) |
| **单节点 `< x`: `[1]`** | $x = 2$ | $p1$ 接入 `[1]`；$d2.next = None$；$p1.next = None$；返回 `[1]` | `[1]` (通过) |
| **单节点 $\ge x$: `[2]`** | $x = 2$ | $p2$ 接入 `[2]`；$d1$ 为空；$p1.next = [2]$；返回 `[2]` | `[2]` (通过) |
| **全小于: `[1, 2, 3]`** | $x = 4$ | $d1$ 接入所有节点；$d2.next = None$；$p1.next = None$；返回原序列 | `[1, 2, 3]` (通过) |
| **全大于: `[5, 6, 7]`** | $x = 3$ | $d1$ 为空；$d2$ 接入所有节点；$d1.next = d2.next$；返回原序列 | `[5, 6, 7]` (通过) |
| **全相等且等于 $x$: `[3, 3]`** | $x = 3$ | 全部走 $\ge x$ 分支接入 $d2$；$d1.next = d2.next$；相对顺序完好 | `[3, 3]` (通过) |

---

## 7. Complexity Analysis / 复杂度分析

| 维度 (Dimension) | 复杂度 (Complexity) | 数学证明与核心原由 (Mathematical Rationale) |
| :--- | :---: | :--- |
| **时间复杂度 (Time Complexity)** | $\mathcal{O}(N)$ | 其中 $N$ 为单链表的节点总数。算法仅使用单指针 $p$ 对原始链表进行了一次线性顺序扫描，每个节点在遍历过程中仅经历常数次判断、解绑与挂载操作。后续链表缝合只需一次 $\mathcal{O}(1)$ 指针赋值，因此总体时间复杂度严格为 $\mathcal{O}(N)$。 |
| **空间复杂度 (Space Complexity)** | $\mathcal{O}(1)$ | 算法仅额外创建了两个辅助哨兵节点 `d1` 与 `d2`，以及常数个引用指针变量（`p1`, `p2`, `p`, `temp`）。所有原链表节点均是通过修改 `.next` 原地重构链接，并未创建任何新节点或依赖递归调用栈，故辅助空间复杂度为严格的 $\mathcal{O}(1)$。 |
