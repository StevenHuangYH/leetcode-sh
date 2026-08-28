import os
import re
from pathlib import Path
from scripts.generate_luffy_batch import create_note

REPO_ROOT = Path(__file__).parent.parent
LUFFY_DIR = REPO_ROOT / "luffy"

DB_PART2 = {
    "21-lc-0155-min-stack": {
        "id": "0155", "title_en": "Min Stack", "title_cn": "最小栈", "diff": "Medium", "topic": "Topic 06: Stacks",
        "en_desc": "Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.",
        "cn_desc": "设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。",
        "constraints": "-2^31 <= val <= 2^31 - 1, 最多调用 3 * 10^4 次 push, pop, top, getMin",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 双栈法 / 辅助最小栈 (Min Stack Pair)                   │\n│ 主栈 stack 存数据，辅助栈 min_stack 同步存当前最小值   │\n│ min_stack[-1] 始终为全局最小值                         │\n└────────────────────────────────────────────────────────┘",
        "invariant": "前缀极值同步性：`min_stack[i]` 严格等于 `min(stack[0...i])`。",
        "interview_qa": "- **Interviewer**: *“如何只用一个栈做到 O(1) 空间支持 getMin？”*\n  - **Candidate**: 可以在栈中存入当前值与当前最小值的差值 `diff = val - min_val`，或在栈内压入 `(val, cur_min)` 二元组。",
        "anti_patterns": [("pop 未同步更新 min", "仅从主栈 pop 导致 min 栈未同步", "状态脱节", "主栈与辅助栈必须严格同步 push/pop")],
        "dry_run": "push(-2), push(0), push(-3) -> getMin()=-3, pop() -> getMin()=-2",
        "time": ("$O(1)$", "所有操作均为常数时间。"), "space": ("$O(n)$", "辅助栈占用额外空间。")
    },
    "22-lc-0227-basic-calculator-ii": {
        "id": "0227", "title_en": "Basic Calculator II", "title_cn": "基本计算器 II", "diff": "Medium", "topic": "Topic 06: Stack & Parsing",
        "en_desc": "Given a string `s` which represents an expression, evaluate this expression and return its value. The integers in the expression are non-negative, and operators are '+', '-', '*', '/'.",
        "cn_desc": "给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。整数除法仅保留整数部分。",
        "constraints": "1 <= s.length <= 3 * 10^5, s 由整数和算符 ('+', '-', '*', '/') 组成",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 栈运算符优先级计算                                     │\n│ 遇到 +: stack.append(num)                              │\n│ 遇到 -: stack.append(-num)                             │\n│ 遇到 *: stack.append(stack.pop() * num)                │\n│ 遇到 /: stack.append(int(stack.pop() / num))           │\n│ 最后求和 sum(stack)                                    │\n└────────────────────────────────────────────────────────┘",
        "invariant": "高优先级即时结合：乘除法立即出栈计算压回，加减法转化为正负数最后统求和。",
        "interview_qa": "- **Interviewer**: *“Python 负数除法整除向负无穷取整的问题如何处理？”*\n  - **Candidate**: Python 的 `//` 面对负数时如 `-3 // 2 = -2`，必须使用 `int(a / b)` 向零截断。",
        "anti_patterns": [("负数整除截断错误", "使用 // 导致向负无穷取整", "除法舍入", "必须使用 int(float(a) / b)")],
        "dry_run": "s='3+2*2' -> stack=[3, 4] -> sum=7",
        "time": ("$O(n)$", "遍历字符串一次。"), "space": ("$O(n)$", "数字栈。")
    },
    "23-lc-0394-decode-string": {
        "id": "0394", "title_en": "Decode String", "title_cn": "字符串解码", "diff": "Medium", "topic": "Topic 06: Stack & Recursion",
        "en_desc": "Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times.",
        "cn_desc": "给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。",
        "constraints": "1 <= s.length <= 30",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 双栈法 (倍数栈 count_stack + 字符串栈 str_stack)       │\n│ 遇 '[': 将当前 res 和 k 压栈，清空临时变量             │\n│ 遇 ']': 弹出上一层字符串与倍数: res = prev + k * res   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "括号嵌套层级维护：栈中保存上一层级的字符前缀和当前层级的重复倍数。",
        "interview_qa": "- **Interviewer**: *“如何用递归方式实现？”*\n  - **Candidate**: 将括号内容视作子问题递归调用，遇到 `]` 返回当前层级结果与消费后的索引指针。",
        "anti_patterns": [("多位数解析错误", "遇到多位数字如 100 仅解析了首位", "数字累加", "k = k * 10 + int(c)")],
        "dry_run": "s='3[a2[c]]' -> a2[c]->acc -> 3[acc]->accaccacc",
        "time": ("$O(S)$", "$S$ 为解码后最终字符串的总长度。"), "space": ("$O(S)$", "栈存储嵌套层级字符。")
    },
    "24-lc-0232-implement-queue-using-stacks": {
        "id": "0232", "title_en": "Implement Queue using Stacks", "title_cn": "用栈实现队列", "diff": "Easy", "topic": "Topic 06: Stacks & Queues",
        "en_desc": "Implement a first in first out (FIFO) queue using only two stacks.",
        "cn_desc": "请你仅使用两个栈实现先入先出 (FIFO) 的队列。",
        "constraints": "最多调用 100 次",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 双栈模拟 (In-Stack & Out-Stack)                        │\n│ push: 直接压入 in_stack                                │\n│ pop/peek: 若 out_stack 为空，将 in_stack 全部倒入      │\n│           再从 out_stack 弹出/查看                     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "倒序抵消原理：两次 LIFO 后进先出等价于一次 FIFO 先入先出。",
        "interview_qa": "- **Interviewer**: *“pop 操作的均摊时间复杂度是多少？”*\n  - **Candidate**: 均摊 $O(1)$。每个元素最多进出 `in_stack` 和 `out_stack` 各一次，总步数 $4n$。",
        "anti_patterns": [("每次 push 都倒栈", "push 复杂度退化为 O(n)", "过早搬运", "仅在 pop/peek 且 out 为空时倒栈")],
        "dry_run": "push(1), push(2) -> in=[1,2], out=[] -> pop() -> in=[], out=[2,1] -> return 1",
        "time": ("均摊 $O(1)$", "每个元素最多被移动 2 次。"), "space": ("$O(n)$", "两栈总容量。")
    },
    "25-lc-0094-binary-tree-inorder-traversal": {
        "id": "0094", "title_en": "Binary Tree Inorder Traversal", "title_cn": "二叉树的中序遍历", "diff": "Easy", "topic": "Topic 07: Tree Traversal",
        "en_desc": "Given the `root` of a binary tree, return the inorder traversal of its nodes' values.",
        "cn_desc": "给定一个二叉树的根节点 root ，返回它的 中序 遍历。",
        "constraints": "树中节点数目在范围 [0, 100] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 中序遍历 DFS (Left -> Root -> Right)                   │\n│ 对于 BST，中序遍历结果严格单调递增                     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "左根右递归不变量：左子树遍历结果 + 根节点值 + 右子树遍历结果。",
        "interview_qa": "- **Interviewer**: *“如何用迭代栈实现中序遍历？”*\n  - **Candidate**: 一路向左将所有左节点压栈；弹出栈顶记录结果，转向其右子树重复此过程。",
        "anti_patterns": [("空树未防御", "root=None 报错", "未判空", "首行 if not root: return []")],
        "dry_run": "root=[1,null,2,3] -> 1 -> 3 -> 2 -> [1, 3, 2]",
        "time": ("$O(n)$", "每个节点访问一次。"), "space": ("$O(n)$", "最坏链状树递归栈深度 $O(n)$。")
    },
    "25-lc-0144-binary-tree-preorder-traversal": {
        "id": "0144", "title_en": "Binary Tree Preorder Traversal", "title_cn": "二叉树的前序遍历", "diff": "Easy", "topic": "Topic 07: Tree Traversal",
        "en_desc": "Given the `root` of a binary tree, return the preorder traversal of its nodes' values.",
        "cn_desc": "给你二叉树的根节点 root ，返回它节点值的 前序 遍历。",
        "constraints": "树中节点数目在范围 [0, 100] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 前序遍历 DFS (Root -> Left -> Right)                   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "根左右递归不变量：根节点值 + 左子树结果 + 右子树结果。",
        "interview_qa": "- **Interviewer**: *“Morris 遍历如何做到 O(1) 空间？”*\n  - **Candidate**: 利用叶子节点的空闲右指针建立指向中序前驱的线索（Threaded Binary Tree）。",
        "anti_patterns": [("递归未终止", "未写 Base Case", "递归溢出", "递归基检查 if not root")],
        "dry_run": "root=[1,null,2,3] -> [1, 2, 3]",
        "time": ("$O(n)$", "节点总数。"), "space": ("$O(n)$", "递归调用栈。")
    },
    "25-lc-0145-binary-tree-postorder-traversal": {
        "id": "0145", "title_en": "Binary Tree Postorder Traversal", "title_cn": "二叉树的后序遍历", "diff": "Easy", "topic": "Topic 07: Tree Traversal",
        "en_desc": "Given the `root` of a binary tree, return the postorder traversal of its nodes' values.",
        "cn_desc": "给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。",
        "constraints": "树中节点的数目在范围 [0, 100] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 后序遍历 DFS (Left -> Right -> Root)                   │\n│ 分治与树形 DP 的天然遍历顺序                           │\n└────────────────────────────────────────────────────────┘",
        "invariant": "左右根归纳不变量：必须先收集完左右子树的全部信息，再在根节点进行状态合并。",
        "interview_qa": "- **Interviewer**: *“为什么树形 DP 大多基于后序遍历？”*\n  - **Candidate**: 树形 DP 需要子树的计算结果（高度、最优值）自底向上汇总至当前根节点。",
        "anti_patterns": [("左右子树未完全遍历即返回", "过早返回局部状态", "后序逻辑混淆", "先递归 left/right 再处理 root")],
        "dry_run": "root=[1,null,2,3] -> [3, 2, 1]",
        "time": ("$O(n)$", "每个节点遍历一次。"), "space": ("$O(n)$", "递归栈。")
    },
    "25-tree-traversal-advanced-patterns": {
        "id": "0094", "title_en": "Tree Traversal Advanced Patterns", "title_cn": "二叉树高级遍历与构造模式", "diff": "Medium", "topic": "Topic 07: Advanced Tree Patterns",
        "en_desc": "Comprehensive paradigms for tree serialization, iterative traversals, and multi-threaded tree patterns.",
        "cn_desc": "二叉树迭代遍历、序列化与线索化高级模式汇总。",
        "constraints": "通用二叉树结构",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 树遍历三大范式: 递归分治 / 显式辅助栈 / Morris 线索化 │\n└────────────────────────────────────────────────────────┘",
        "invariant": "拓扑结构一致性：遍历序列与树结构一一映射。",
        "interview_qa": "- **Interviewer**: *“哪两种遍历序列组合可以唯一确定一棵二叉树？”*\n  - **Candidate**: 前序+中序，或后序+中序（必须包含中序遍历以划分左右子树）。",
        "anti_patterns": [("前序+后序试图唯一确定一般树", "非满二叉树存在歧义", "歧义性", "必须有中序才能准确定位左右子树")],
        "dry_run": "Tree DFS/BFS 统一调度模板",
        "time": ("$O(n)$", "遍历全体节点。"), "space": ("$O(n)$", "辅助栈。")
    },
    "26-lc-0104-maximum-depth-of-binary-tree": {
        "id": "0104", "title_en": "Maximum Depth of Binary Tree", "title_cn": "二叉树的最大深度", "diff": "Easy", "topic": "Topic 07: Tree Divide & Conquer",
        "en_desc": "Given the `root` of a binary tree, return its maximum depth.",
        "cn_desc": "给定一个二叉树 root ，返回其最大深度。",
        "constraints": "树中节点的数目在范围 [0, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 分治递推: depth = 1 + max(maxDepth(left), maxDepth(right)) │\n└────────────────────────────────────────────────────────┘",
        "invariant": "深度归纳基石：空树深度为 0，非空树深度为左右子树最大深度加 1。",
        "interview_qa": "- **Interviewer**: *“如何用层序遍历 (BFS) 计算最大深度？”*\n  - **Candidate**: 使用队列进行 BFS，每处理完一整层 `depth += 1`，直到队列为空返回 `depth`。",
        "anti_patterns": [("Base Case 遗漏", "root=None 未返回 0", "死递归", "首行 if not root: return 0")],
        "dry_run": "root=[3,9,20,null,null,15,7] -> 1 + max(1, 2) = 3",
        "time": ("$O(n)$", "每个节点遍历一次。"), "space": ("$O(h)$", "树高 $h$ 递归栈。")
    },
    "27-lc-0236-lowest-common-ancestor-of-a-binary-tree": {
        "id": "0236", "title_en": "Lowest Common Ancestor of a Binary Tree", "title_cn": "二叉树的最近公共祖先", "diff": "Medium", "topic": "Topic 07: Tree Post-Order",
        "en_desc": "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.",
        "cn_desc": "给定一个二叉树, 找到该树中两个指定节点的最近公共祖先 (LCA)。",
        "constraints": "树中节点数目在范围 [2, 10^5] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 后序分治四态判定:                                      │\n│ 1. 若 root 是 p 或 q 或 None -> 返回 root              │\n│ 2. left 和 right 均非空 -> root 即为 LCA               │\n│ 3. 仅一边非空 -> 向上透传该非空子树结果                │\n└────────────────────────────────────────────────────────┘",
        "invariant": "祖先汇聚判定：首次在左右两侧同时捕获到目标节点的分叉点即为最近公共祖先。",
        "interview_qa": "- **Interviewer**: *“如果两个节点在同一子树中，算法如何正确返回？”*\n  - **Candidate**: 较高层级的节点匹配到 `root in (p, q)` 直接返回自身，天然覆盖了其子树包含另一节点的情况。",
        "anti_patterns": [("未向上透传单侧非空结果", "一边为空直接返回 None", "逻辑断裂", "return left or right")],
        "dry_run": "root=[3,5,1,6,2,0,8], p=5, q=1 -> left=5, right=1 -> return 3",
        "time": ("$O(n)$", "遍历每个节点一次。"), "space": ("$O(h)$", "递归栈深度。")
    },
    "28-lc-0102-binary-tree-level-order-traversal": {
        "id": "0102", "title_en": "Binary Tree Level Order Traversal", "title_cn": "二叉树的层序遍历", "diff": "Medium", "topic": "Topic 07: Tree BFS",
        "en_desc": "Given the `root` of a binary tree, return the level order traversal of its nodes' values.",
        "cn_desc": "给你二叉树的根节点 root ，返回其节点值的 层序遍历 。",
        "constraints": "树中节点数目在范围 [0, 2000] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 队列 BFS / 双缓冲区层序遍历                            │\n│ while queue:                                           │\n│   for _ in range(len(queue)): 弹出并收集当前层所有节点 │\n│   将该层子节点加入队列，结果存入 ans                   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "层级隔离不变量：通过 `len(queue)` 快照或双列表隔离上一层与下一层节点。",
        "interview_qa": "- **Interviewer**: *“如何用 DFS 递归实现层序遍历？”*\n  - **Candidate**: DFS 入参携带 `depth`，若 `depth == len(ans)` 则 `ans.append([])`，将 `node.val` 追加到 `ans[depth]`。",
        "anti_patterns": [("动态修改队列导致长度变化", "在 for 循环中未固定当前层长度", "层级混淆", "必须使用 for _ in range(len(q)) 快照")],
        "dry_run": "root=[3,9,20,null,null,15,7] -> [[3], [9, 20], [15, 7]]",
        "time": ("$O(n)$", "每个节点入队出队一次。"), "space": ("$O(n)$", "最宽层最多 $n/2$ 个节点。")
    },
    "29-lc-0098-validate-binary-search-tree-bounds": {
        "id": "0098", "title_en": "Validate BST (Range Bounds)", "title_cn": "验证二叉搜索树 (区间上下界法)", "diff": "Medium", "topic": "Topic 07: BST Validation",
        "en_desc": "Given the root of a binary tree, determine if it is a valid binary search tree (BST) using pre-order range bounds.",
        "cn_desc": "给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树（采用开区间界限法）。",
        "constraints": "树中节点数目在范围 [1, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 开区间上下界递推: is_valid(node, low, high)            │\n│ 约束: low < node.val < high                            │\n│ 左子树: is_valid(node.left, low, node.val)             │\n│ 右子树: is_valid(node.right, node.val, high)           │\n└────────────────────────────────────────────────────────┘",
        "invariant": "全局边界传递性：节点值必须严格介于当前祖先链路决定的开区间 $(low, high)$ 内。",
        "interview_qa": "- **Interviewer**: *“只比较 root.val > root.left.val 是否足够？”*\n  - **Candidate**: 远远不够。BST 要求左子树中所有节点都小于根，单纯局部比较无法检测到左子树深层节点大于祖先节点的情况（如 `[5, 1, 6, null, null, 3, 7]` 中 3 小于 5 的违规）。",
        "anti_patterns": [("使用闭区间导致等于号判断错误", "BST 严禁出现重复值", "相等违背", "必须严格使用 < 和 >")],
        "dry_run": "root=[2,1,3] -> valid(2, -inf, inf) -> left valid(1, -inf, 2), right valid(3, 2, inf) -> True",
        "time": ("$O(n)$", "遍历所有节点。"), "space": ("$O(h)$", "树高递归栈。")
    },
    "29-lc-0098-validate-binary-search-tree-inorder": {
        "id": "0098", "title_en": "Validate BST (Inorder Monotonicity)", "title_cn": "验证二叉搜索树 (中序单调递增法)", "diff": "Medium", "topic": "Topic 07: BST Validation",
        "en_desc": "Validate BST by verifying that its in-order traversal yields a strictly monotonically increasing sequence.",
        "cn_desc": "通过中序遍历严格单调递增性质验证二叉搜索树。",
        "constraints": "树中节点数目在范围 [1, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 中序单调递增特性: pre_val < cur_node.val               │\n└────────────────────────────────────────────────────────┘",
        "invariant": "BST 中序遍历等价定理：二叉树是有效 BST 充要条件为其遍历结果严格单调递增。",
        "interview_qa": "- **Interviewer**: *“中序遍历验证时如何提早短路退出？”*\n  - **Candidate**: 发现 `cur_val <= pre_val` 立即返回 `False`，无需继续遍历后续子树。",
        "anti_patterns": [("pre_val 初值设为 0", "若节点含负数如 -2^31 则失效", "初值错误", "pre_val 必须初始化为 -inf")],
        "dry_run": "root=[5,1,4,null,null,3,6] -> 中序: 1, 5, 3 (3<=5 违背) -> return False",
        "time": ("$O(n)$", "最坏全树，平均提前退出。"), "space": ("$O(h)$", "栈空间。")
    },
    "29-lc-0098-validate-binary-search-tree-recursion": {
        "id": "0098", "title_en": "Validate BST (Postorder Min/Max Range)", "title_cn": "验证二叉搜索树 (后序极值汇总)", "diff": "Medium", "topic": "Topic 07: BST Validation",
        "en_desc": "Validate BST using post-order tree DP returning (min_val, max_val) sub-tree bounds.",
        "cn_desc": "使用后序遍历自底向上返回子树 `(min_val, max_val)` 极值范围验证 BST。",
        "constraints": "树中节点数目在范围 [1, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 后序自底向上: 返回 (is_bst, min_val, max_val)          │\n└────────────────────────────────────────────────────────┘",
        "invariant": "子树极值包络性：`node.val` 必须大于左子树的最大值，且小于右子树的最小值。",
        "interview_qa": "- **Interviewer**: *“后序极值法与前序区间法相比有何特点？”*\n  - **Candidate**: 后序法自底向上汇总，利于转化为求解最大 BST 子树（LC 333）等扩展问题。",
        "anti_patterns": [("空节点极值反向初始化错误", "空节点 min/max 设置反了", "极值反转", "空节点 min=inf, max=-inf")],
        "dry_run": "空节点返回 (inf, -inf)，叶子节点返回 (val, val)",
        "time": ("$O(n)$", "每个节点遍历一次。"), "space": ("$O(h)$", "树高。")
    },
    "29-lc-0098-validate-binary-search-tree-stack": {
        "id": "0098", "title_en": "Validate BST (Iterative Stack)", "title_cn": "验证二叉搜索树 (显式栈迭代法)", "diff": "Medium", "topic": "Topic 07: BST Validation",
        "en_desc": "Validate BST using an explicit stack for in-order traversal to eliminate recursion overhead.",
        "cn_desc": "使用显式辅助栈进行中序遍历验证 BST，消除函数调用栈开销。",
        "constraints": "树中节点数目在范围 [1, 10^4] 内",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 显式中序栈: while stack or root -> push all left nodes │\n└────────────────────────────────────────────────────────┘",
        "invariant": "栈内状态一致性：栈顶元素为当前未访问的最左侧子节点。",
        "interview_qa": "- **Interviewer**: *“迭代中序遍历在内存受限系统中的优势？”*\n  - **Candidate**: 避免栈溢出风险，且易于在中途终止时手动清理释放堆栈。",
        "anti_patterns": [("root = root.right 遗漏", "死循环卡在当前节点", "指针移动遗漏", "弹出节点后必须将 root 转向其右孩子")],
        "dry_run": "压左孩子入栈 -> 弹出比较 -> 转右孩子",
        "time": ("$O(n)$", "线性时间。"), "space": ("$O(h)$", "显式栈大小。")
    },
    "30-lc-0105-construct-binary-tree-from-preorder-and-inorder-traversal": {
        "id": "0105", "title_en": "Construct Binary Tree from Preorder & Inorder", "title_cn": "从前序与中序遍历序列构造二叉树", "diff": "Medium", "topic": "Topic 07: Tree Construction",
        "en_desc": "Given two integer arrays `preorder` and `inorder`, construct and return the binary tree.",
        "cn_desc": "给定两个整数数组 preorder 和 inorder ，构造二叉树并返回其根节点。",
        "constraints": "1 <= preorder.length <= 3000, inorder.length == preorder.length",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 递归分治定位:                                          │\n│ preorder[0] 是根节点 root_val                          │\n│ 在 inorder 中定位 root_val 索引 k:                     │\n│   左子树大小 size = k - in_left                        │\n│   左子树: preorder[1...size], inorder[...k-1]          │\n│   右子树: preorder[size+1...], inorder[k+1...]         │\n└────────────────────────────────────────────────────────┘",
        "invariant": "子树划分对偶性：前序序列的根节点在中序序列中精确划分左子树与右子树的节点集合。",
        "interview_qa": "- **Interviewer**: *“如何避免递归切片导致的 O(n^2) 时间复杂度？”*\n  - **Candidate**: 预先用哈希表记录 `inorder` 各元素下标，递归时仅传递下标范围 `(pre_l, pre_r, in_l, in_r)` 做到 $O(n)$。",
        "anti_patterns": [("数组切片复制开销", "nums[1:k] 产生额外拷贝", "时间退化", "采用索引边界传参或哈希表辅助")],
        "dry_run": "preorder=[3,9,20,15,7], inorder=[9,3,15,20,7] -> root=3, left=[9], right=[20,15,7]",
        "time": ("$O(n)$", "带哈希表索引查询。"), "space": ("$O(n)$", "哈希表与递归树。")
    },
    "31-lc-0077-combinations": {
        "id": "0077", "title_en": "Combinations", "title_cn": "组合", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.",
        "cn_desc": "给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。",
        "constraints": "1 <= n <= 20, 1 <= k <= n",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 回溯树剪枝: 当剩余候选数不足以填满 k 时立即剪枝        │\n│ 上界: i <= n - (k - len(path)) + 1                     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "组合无序性：通过规定后选数字严格大于当前数字（`for i in range(start, ...)`）消除重复排列。",
        "interview_qa": "- **Interviewer**: *“组合剪枝的上界是如何推导出来的？”*\n  - **Candidate**: 还需选 $k - |path|$ 个数，从 $i$ 到 $n$ 共有 $n - i + 1$ 个数，令 $n - i + 1 \\ge k - |path|$ 即可解出 $i \\le n - (k - |path|) + 1$。",
        "anti_patterns": [("未做剪枝遍历过多无效分支", "无剪枝暴搜超时", "效率低下", "添加上界剪枝优化")],
        "dry_run": "n=4, k=2 -> [1,2],[1,3],[1,4],[2,3],[2,4],[3,4]",
        "time": ("$O(C(n, k) \\cdot k)$", "组合数乘以单次复制耗时。"), "space": ("$O(k)$", "递归路径深度。")
    },
    "32-lc-0046-permutations": {
        "id": "0046", "title_en": "Permutations", "title_cn": "全排列", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given an array `nums` of distinct integers, return all the possible permutations.",
        "cn_desc": "给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。",
        "constraints": "1 <= nums.length <= 6",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 回溯全排列: used 标记数组 或 原地 swap 交换            │\n│ 每层递归选择一个未被 used 的元素加入 path              │\n└────────────────────────────────────────────────────────┘",
        "invariant": "排列有序性：每个位置均可选取任意未被前序位置占用的元素。",
        "interview_qa": "- **Interviewer**: *“如果数组中包含重复数字（LC 47），该如何去重？”*\n  - **Candidate**: 先排序，在同一树层遇 `nums[i] == nums[i-1]` 且 `not used[i-1]` 时跳过剪枝。",
        "anti_patterns": [("忘记 path.pop() 恢复现场", "回溯状态污染后续分支", "未回溯", "递归后必须执行 path.pop()")],
        "dry_run": "nums=[1,2,3] -> 6 种全排列",
        "time": ("$O(n! \\cdot n)$", "全排列数 $n!$。"), "space": ("$O(n)$", "递归栈与 used 标记。")
    },
    "33-lc-0078-subsets": {
        "id": "0078", "title_en": "Subsets", "title_cn": "子集", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given an integer array `nums` of unique elements, return all possible subsets (the power set).",
        "cn_desc": "给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。",
        "constraints": "1 <= nums.length <= 10, -10 <= nums[i] <= 10",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 子集生成两大流派:                                      │\n│ 1. 选/不选二叉树 (0-1 Pick / Skip)                     │\n│ 2. 枚举下一个元素多叉树 (Every Node is a Solution)     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "幂集完全性：长度为 $n$ 的集合恰好存在 $2^n$ 个互异子集。",
        "interview_qa": "- **Interviewer**: *“如何用二进制位掩码 (Bitmask) 非递归生成子集？”*\n  - **Candidate**: 遍历 $0$ 到 $2^n - 1$ 的每一个整数 $mask$，若第 $i$ 位为 1 则将 $nums[i]$ 放入当前子集。",
        "anti_patterns": [("忘记 path.copy()", "追加引用导致最终全是空列表", "浅拷贝失误", "ans.append(path.copy())")],
        "dry_run": "nums=[1,2,3] -> 8 个子集",
        "time": ("$O(2^n \\cdot n)$", "共 $2^n$ 个子集，复制每个耗时 $O(n)$。"), "space": ("$O(n)$", "路径栈。")
    },
    "34-lc-0039-combination-sum": {
        "id": "0039", "title_en": "Combination Sum", "title_cn": "组合总和", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations where the chosen numbers sum to `target`.",
        "cn_desc": "给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 。",
        "constraints": "1 <= candidates.length <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 可重复选择的组合回溯                                   │\n│ 排序后递归: dfs(remain - x, i) (传 i 允许重复选自身)  │\n│ 若 remain - x < 0: 立即 break 剪枝                     │\n└────────────────────────────────────────────────────────┘",
        "invariant": "非降序消除排列重复：下一次选择只能从下标 $\\ge i$ 的候选数中挑选。",
        "interview_qa": "- **Interviewer**: *“为什么传 i 而不是 i + 1？”*\n  - **Candidate**: 题目允许同一个数字被无限制重复选取，因此递归入参继续保留当前下标 $i$。",
        "anti_patterns": [("未排序就 break 剪枝", "无序数组 break 误剪有效分支", "过早剪枝", "必须先排序后才能 break")],
        "dry_run": "candidates=[2,3,6,7], target=7 -> [2,2,3], [7]",
        "time": ("$O(S)$", "$S$ 为所有可行解长度之和。"), "space": ("$O(target)$", "最坏全选最小元素递归深度。")
    },
    "35-lc-0040-combination-sum-ii": {
        "id": "0040", "title_en": "Combination Sum II", "title_cn": "组合总和 II", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations where candidate numbers sum to `target`. Each number may only be used once in the combination.",
        "cn_desc": "给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。candidates 中的每个数字在每个组合中只能使用 一次 。",
        "constraints": "1 <= candidates.length <= 100, 1 <= candidates[i] <= 50, 1 <= target <= 30",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 树层去重 (Breadth Deduplication)                       │\n│ 排序 candidates;                                       │\n│ 在同层 for 循环中: if i > start and nums[i] == nums[i-1]: continue │\n└────────────────────────────────────────────────────────┘",
        "invariant": "树枝可重，树层去重：同一路径可包含原数组中的重复值，但同一分叉层不能选取相同数值开头。",
        "interview_qa": "- **Interviewer**: *“为什么 `i > start` 能区分树层重复和树枝重复？”*\n  - **Candidate**: `i == start` 是当前树枝向下深入探索的第一个元素（允许与前一个数值相同）；`i > start` 则是同一层回溯后的横向切换（禁止选取相同值）。",
        "anti_patterns": [("误用 i > 0", "将树枝上的合法相同数也剪掉了", "过度剪枝", "必须判定 i > start")],
        "dry_run": "candidates=[10,1,2,7,6,1,5], target=8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]",
        "time": ("$O(2^n)$", "搜索树剪枝。"), "space": ("$O(n)$", "递归栈。")
    },
    "36-lc-0131-palindrome-partitioning": {
        "id": "0131", "title_en": "Palindrome Partitioning", "title_cn": "分割回文串", "diff": "Medium", "topic": "Topic 08: Backtracking",
        "en_desc": "Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.",
        "cn_desc": "给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。",
        "constraints": "1 <= s.length <= 16",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 回溯切割线: 枚举当前切割子串 s[start...i]             │\n│ 若 s[start...i] 是回文: path.append(...); dfs(i + 1)   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "回文前缀合法性：当前切割出的子串必须是回文串，才允许递归处理剩余后缀。",
        "interview_qa": "- **Interviewer**: *“如何加速回文子串判定？”*\n  - **Candidate**: 可预先使用区间 DP 预处理 $O(n^2)$ 的 `is_pal[i][j]` 表，将回文判定由 $O(n)$ 降为 $O(1)$。",
        "anti_patterns": [("切片越界", "s[start:i] 漏掉第 i 位", "切片区间错误", "切片必须为 s[start:i+1]")],
        "dry_run": "s='aab' -> [['a','a','b'], ['aa','b']]",
        "time": ("$O(n \\cdot 2^n)$", "$n-1$ 个切割点共有 $2^{n-1}$ 种分割方案。"), "space": ("$O(n)$", "递归栈。")
    },
    "37-lc-0079-word-search": {
        "id": "0079", "title_en": "Word Search", "title_cn": "单词搜索", "diff": "Medium", "topic": "Topic 09: 2D Grid DFS",
        "en_desc": "Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.",
        "cn_desc": "给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。",
        "constraints": "m == board.length, n = board[i].length, 1 <= m, n <= 6, 1 <= word.length <= 15",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 网格 DFS + 原地回溯标记                                │\n│ 匹配当前字符: temp = board[r][c]; board[r][c] = '#'    │\n│ 向四方向探索: dfs(r+dr, c+dc, k+1)                     │\n│ 回溯恢复现场: board[r][c] = temp                       │\n└────────────────────────────────────────────────────────┘",
        "invariant": "路径不重复性：同一路径在单词匹配过程中不能重复经过同一个网格单元。",
        "interview_qa": "- **Interviewer**: *“如何进行词频剪枝优化？”*\n  - **Candidate**: 统计网格和目标单词的字符频次，若网格字符不足直接返回 `False`；若单词末尾字符频次少于开头，反转单词可减少初期分叉搜索。",
        "anti_patterns": [("忘记回溯恢复网格字符", "网格永远变为 '#'", "状态污染", "必须在递归返回前 board[r][c] = temp")],
        "dry_run": "board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word='ABCCED' -> True",
        "time": ("$O(M \\cdot N \\cdot 3^L)$", "网格每个起点出发 3 方向搜索深度 $L$。"), "space": ("$O(L)$", "单词长度递归栈。")
    },
    "38-lc-0200-number-of-islands": {
        "id": "0200", "title_en": "Number of Islands", "title_cn": "岛屿数量", "diff": "Medium", "topic": "Topic 09: Flood Fill (DFS/BFS)",
        "en_desc": "Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.",
        "cn_desc": "给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。",
        "constraints": "m == grid.length, n == grid[i].length, 1 <= m, n <= 300",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 沉岛策略 / 泛洪填充 (Flood Fill)                       │\n│ 遍历每个格子，遇到 '1':                                │\n│   ans += 1                                             │\n│   DFS/BFS 扩散并将所有相连的 '1' 淹没覆写为 '0'        │\n└────────────────────────────────────────────────────────┘",
        "invariant": "连通分量计数定理：每次触发 DFS 扩散，恰好将一个完整的连通图全部标记/沉没。",
        "interview_qa": "- **Interviewer**: *“DFS 与并查集 (Union-Find) 解决本题有何区别？”*\n  - **Candidate**: DFS 实现最简且时间 $O(mn)$；并查集适合动态增删陆地（如 LC 305 动态岛屿）的在线维护场景。",
        "anti_patterns": [("未标记访问导致死循环", "相邻格子互相调用递归爆栈", "无限循环", "必须在进入时立即 grid[r][c] = '0'")],
        "dry_run": "4x5 网格遇到首个 '1' -> 沉没整座岛 -> 答案加 1",
        "time": ("$O(m \\cdot n)$", "每个格子最多访问常数次。"), "space": ("$O(m \\cdot n)$", "递归栈最坏铺满网格。")
    },
    "39-lc-0130-surrounded-regions": {
        "id": "0130", "title_en": "Surrounded Regions", "title_cn": "被围绕的区域", "diff": "Medium", "topic": "Topic 09: 2D Grid DFS",
        "en_desc": "Given an `m x n` matrix `board` containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.",
        "cn_desc": "给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：连接所有与 'X' 边缘不相连的 'O' 并替换为 'X'。",
        "constraints": "1 <= m, n <= 200",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 逆向思维: 从四条边界的 'O' 出发 DFS 标记为 'A' (保活)  │\n│ 遍历全图: 'A' 恢复为 'O' (边界相连未被包围)            │\n│           'O' 捕获为 'X' (被包围)                      │\n└────────────────────────────────────────────────────────┘",
        "invariant": "边界连通等价性：任何没有被完全包围的 'O' 必然至少与一条外边界上的某个 'O' 四向连通。",
        "interview_qa": "- **Interviewer**: *“为什么从边界反向搜索优于从内部正向搜索？”*\n  - **Candidate**: 内部正向搜索需要走到边界才能判断是否被包围，状态回溯繁琐；从边界出发只需单向标记，逻辑极为清晰。",
        "anti_patterns": [("漏扫某条边界", "只扫描了第一行第一列", "遗漏四边", "四条边界需全部启动 DFS")],
        "dry_run": "边界 'O' -> 'A' -> 内部 'O' 变 'X' -> 'A' 恢复 'O'",
        "time": ("$O(m \\cdot n)$", "网格遍历与 DFS 访问。"), "space": ("$O(m \\cdot n)$", "DFS 递归栈。")
    },
    "40-lc-0994-rotting-oranges": {
        "id": "0994", "title_en": "Rotting Oranges", "title_cn": "腐烂的橘子", "diff": "Medium", "topic": "Topic 09: Multi-source BFS",
        "en_desc": "You are given an `m x n` grid where each cell can have one of three values: 0 empty, 1 fresh orange, 2 rotten orange. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If impossible, return -1.",
        "cn_desc": "在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一: 0 空, 1 新鲜橘子, 2 腐烂橘子。返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。",
        "constraints": "1 <= m, n <= 10",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 多源广度优先搜索 (Multi-source BFS)                   │\n│ 1. 将所有初始腐烂橘子 '2' 同时压入队列，统计新鲜数     │\n│ 2. 按分钟层序 BFS 扩散腐烂相邻 '1'，fresh -= 1         │\n│ 3. 若 fresh == 0 返回 minutes，否则返回 -1             │\n└────────────────────────────────────────────────────────┘",
        "invariant": "多源波前同步性：所有腐烂源以相同速度向外蔓延，层序步数即为全局最短扩散时间。",
        "interview_qa": "- **Interviewer**: *“如果初始没有新鲜橘子，应返回几分钟？”*\n  - **Candidate**: 直接返回 0 分钟，初始判空特判 `if fresh == 0: return 0`。",
        "anti_patterns": [("初始无新鲜橘子返回非 0", "fresh=0 错误返回 minutes", "边界特判", "初始 fresh==0 直接 return 0")],
        "dry_run": "grid=[[2,1,1],[1,1,0],[0,1,1]] -> 4 分钟全部腐烂",
        "time": ("$O(m \\cdot n)$", "每个格子最多入队出队一次。"), "space": ("$O(m \\cdot n)$", "BFS 队列空间。")
    },
    "41-lc-1091-shortest-path-in-binary-matrix": {
        "id": "1091", "title_en": "Shortest Path in Binary Matrix", "title_cn": "二进制矩阵中的最短路径", "diff": "Medium", "topic": "Topic 09: 8-Directional BFS",
        "en_desc": "Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no such path, return -1.",
        "cn_desc": "给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中 最短畅通路径 的长度。如果不存在这样的路径，返回 -1 。",
        "constraints": "n == grid.length == grid[i].length, 1 <= n <= 100, grid[i][j] 为 0 或 1",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ 8 方向 BFS 逐层扩散                                    │\n│ 起点 (0,0) 必须为 0，终点 (n-1, n-1) 必须为 0          │\n│ queue.append((0, 0, 1)), grid[0][0] = 1                │\n│ 首次到达终点返回当前步数                               │\n└────────────────────────────────────────────────────────┘",
        "invariant": "BFS 最短路公理：无权图中 BFS 首次抵达终点所经过的步数必然为最短路径。",
        "interview_qa": "- **Interviewer**: *“为什么入队时必须立即标记已访问，而不是出队时标记？”*\n  - **Candidate**: 出队时标记会导致同一个格子被相邻多个节点重复推入队列，造成队列空间与计算量指数级爆炸膨胀。",
        "anti_patterns": [("出队才标记访问", "导致队列重复入队 O(8^d) 爆内存", "标记时机错误", "入队时必须立即 grid[nr][nc] = 1")],
        "dry_run": "grid=[[0,1],[1,0]] -> (0,0)->(1,1) 步长 2",
        "time": ("$O(n^2)$", "每个格子最多访问一次。"), "space": ("$O(n^2)$", "BFS 队列。")
    },
    "42-lc-0207-course-schedule": {
        "id": "0207", "title_en": "Course Schedule", "title_cn": "课程表", "diff": "Medium", "topic": "Topic 09: Topological Sort (Kahn / DFS)",
        "en_desc": "There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. Given prerequisites array, return `true` if you can finish all courses.",
        "cn_desc": "你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。请你判断是否可能完成所有课程的学习？",
        "constraints": "1 <= numCourses <= 2000, 0 <= prerequisites.length <= 5000",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ Kahn 拓扑排序 (入度表 + BFS)                           │\n│ 1. 统计每个节点入度 in_degree[i] 和邻接表 graph        │\n│ 2. 将所有入度为 0 的课程推入队列                       │\n│ 3. 弹出节点，将其指向的所有邻居入度减 1，减为 0 则入队 │\n│ 4. 统计弹出总数 count == numCourses                    │\n└────────────────────────────────────────────────────────┘",
        "invariant": "有向无环图 (DAG) 判定：有向图存在拓扑排序充要条件为图中无有向环。",
        "interview_qa": "- **Interviewer**: *“如何用三色标记法 (DFS) 检测有向图中的环？”*\n  - **Candidate**: 0: 未访问，1: 正在当前递归栈中（遇到 1 说明发现返祖边/环），2: 已完全访问完毕。遇到 1 立即判定有环。",
        "anti_patterns": [("先修方向建反", "将 [a, b] (b->a) 建成了 a->b", "图方向混淆", "b 是 a 的前置，边应为 b -> a")],
        "dry_run": "numCourses=2, prerequisites=[[1,0]] -> in_deg[0]=0, in_deg[1]=1 -> 0 出队 -> in_deg[1]=0 -> 1 出队 -> count=2 == numCourses -> True",
        "time": ("$O(V + E)$", "点数与边数之和。"), "space": ("$O(V + E)$", "邻接表与入度数组。")
    },
    "car-object-oriented-example": {
        "id": "0000", "title_en": "Car Object-Oriented Example", "title_cn": "汽车类面向对象建模实例", "diff": "Easy", "topic": "Topic 11: OOP Foundations",
        "en_desc": "Complete Python class implementation showcasing encapsulation, instance methods, and attributes.",
        "cn_desc": "Python 面向对象封装与实例方法完整示例。",
        "constraints": "Python 3 OOP 规范",
        "ascii": "┌────────────────────────────────────────────────────────┐\n│ Car Class: make, model, year, color, drive(), stop()   │\n└────────────────────────────────────────────────────────┘",
        "invariant": "对象状态自治：实例方法通过 `self` 访问和修改对象专属属性。",
        "interview_qa": "- **Interviewer**: *“Python 中的类方法 `@classmethod` 和静态方法 `@staticmethod` 有何区别？”*\n  - **Candidate**: `@classmethod` 首参接收 `cls`，可访问类属性与工厂方法；`@staticmethod` 不绑定实例与类，纯粹作为命名空间工具函数。",
        "anti_patterns": [("实例方法漏写 self", "运行时报 TypeError", "语法规范", "实例方法首参必须为 self")],
        "dry_run": "car = Car('Ford') -> car.drive() -> 'This Ford is driving'",
        "time": ("$O(1)$", "方法调用。"), "space": ("$O(1)$", "实例内存。")
    }
}

def generate_part2():
    count = 0
    for stem, data in DB_PART2.items():
        filename = f"{stem}.md"
        py_filename = f"{stem}.py"
        py_path = LUFFY_DIR / py_filename
        py_code = py_path.read_text(encoding="utf-8") if py_path.exists() else "# Solution code"
        
        walkthrough_steps = [
            f"基于 `{py_filename}` 原版源码拆解核心数据结构与初始化。",
            f"按关键算法循环推进主体计算逻辑与状态转移。",
            f"维护核心算法不变量并返回最终有效结果。"
        ]
        
        create_note(
            filename=filename,
            lc_id=data["id"],
            title_en=data["title_en"],
            title_cn=data["title_cn"],
            diff=data["diff"],
            topic=data["topic"],
            en_desc=data["en_desc"],
            cn_desc=data["cn_desc"],
            constraints=data["constraints"],
            ascii_art=data["ascii"],
            invariant=data["invariant"],
            py_code=py_code,
            walkthrough_steps=walkthrough_steps,
            interview_qa=data["interview_qa"],
            anti_patterns=data["anti_patterns"],
            dry_run_table=data["dry_run"],
            time_comp=data["time"],
            space_comp=data["space"]
        )
        count += 1
    print(f"Successfully generated/upgraded {count} notes in Luffy Topics 21-42.")

if __name__ == "__main__":
    generate_part2()
