"""
Graph Builder: Generates the structured Cytoscape.js directed acyclic graph (DAG)
for the algorithm curriculum topology, automatically enriched with problem counts from workspace items.
"""
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Any, Optional

@dataclass
class TopologyNodeData:
    id: str
    topic_id: str
    label: str
    category: str
    status: str = "mastered"
    summary: str = ""
    keywords: List[str] = field(default_factory=list)
    problem_count: int = 0

@dataclass
class TopologyEdgeData:
    id: str
    source: str
    target: str
    label: str = ""

def build_topology_graph(items: Optional[Dict[str, Any]] = None) -> Dict[str, List[Dict[str, Any]]]:
    """Constructs the canonical directed algorithm roadmap graph, enriched with workspace problem counts."""
    raw_nodes = [
        # Root Node
        TopologyNodeData(
            id="root",
            topic_id="topic-all",
            label="数据结构与算法\nDSA Master",
            category="Root Paradigm",
            status="mastered",
            summary="程序 = 数据结构 + 算法。涵盖核心线性结构、树图非线性拓扑与高级搜索/动规范式。",
            keywords=["overview", "all"]
        ),
        # First-Level Split
        TopologyNodeData(
            id="array_root",
            topic_id="topic-01-arrays-sliding-window",
            label="数组 (Array)",
            category="Linear Structures",
            status="mastered",
            summary="连续内存分配，O(1) 随机访问。重点考察区间操作、原地修改与指针移动。",
            keywords=["array", "数组"]
        ),
        TopologyNodeData(
            id="linked_list_root",
            topic_id="topic-05-linked-lists",
            label="链表 (Linked List)",
            category="Linear Structures",
            status="mastered",
            summary="离散内存指针连接。核心技巧：虚拟头节点 (Dummy Node)、快慢指针与反转操作。",
            keywords=["linked-list", "链表", "linked_list"]
        ),
        # Array Subtree - Operations Pipeline
        TopologyNodeData(
            id="arr_ops",
            topic_id="topic-01-arrays-sliding-window",
            label="数组操作",
            category="Array Basics",
            status="mastered",
            summary="原地删除元素、移动零、区间覆盖与基础数组重排。",
            keywords=["remove-element", "move-zeroes", "rotate-array"]
        ),
        TopologyNodeData(
            id="prefix_sum",
            topic_id="topic-03-prefix-sum",
            label="前缀和 (Prefix Sum)",
            category="Array Techniques",
            status="mastered",
            summary="预处理 O(N) 实现静态区间查询 O(1)，结合哈希表快速求解子数组和为 K 问题。",
            keywords=["prefix-sum", "prefix_sum", "前缀和", "subarray-sum", "range-sum"]
        ),
        TopologyNodeData(
            id="diff_array",
            topic_id="topic-03-prefix-sum",
            label="差分数组 (Diff Array)",
            category="Array Techniques",
            status="learning",
            summary="频繁对区间 [i, j] 进行 +val 更新时，借助差分数组将区间修改从 O(N) 降至 O(1)。",
            keywords=["difference-array", "差分", "corporate-flight", "car-pooling"]
        ),
        TopologyNodeData(
            id="matrix_2d",
            topic_id="topic-04-intervals",
            label="二维数组 (2D Matrix)",
            category="Array Techniques",
            status="learning",
            summary="二维前缀和、顺时针旋转矩阵、螺旋遍历与对角线对称折叠技巧。",
            keywords=["matrix", "rotate-image", "spiral-matrix", "set-matrix-zeroes"]
        ),
        # Array Subtree - Two Pointers Pipeline
        TopologyNodeData(
            id="two_pointers_tech",
            topic_id="topic-01-arrays-sliding-window",
            label="双指针技巧",
            category="Two Pointers",
            status="mastered",
            summary="快慢指针、左右对撞指针与首尾滑动指针，用单调性减少暴力搜索维度。",
            keywords=["two-pointers", "双指针"]
        ),
        TopologyNodeData(
            id="arr_two_pointers",
            topic_id="topic-01-arrays-sliding-window",
            label="数组双指针",
            category="Two Pointers",
            status="mastered",
            summary="左右对撞双指针、有序数组两数之和、接雨水体积计算。",
            keywords=["container-with-most-water", "3sum", "two-sum-ii", "trapping-rain-water"]
        ),
        TopologyNodeData(
            id="sliding_window",
            topic_id="topic-01-arrays-sliding-window",
            label="滑动窗口 (Sliding Window)",
            category="Two Pointers",
            status="mastered",
            summary="维护左右动态闭区间窗口，通过扩张与收缩寻找极值或可行解。",
            keywords=["sliding-window", "滑动窗口", "longest-substring", "min-window"]
        ),
        TopologyNodeData(
            id="binary_search",
            topic_id="topic-02-binary-search",
            label="二分搜索 (Binary Search)",
            category="Searching",
            status="mastered",
            summary="利用单调性每次将搜索空间减半。涵盖闭区间模版、红蓝染色法与二分答案法。",
            keywords=["binary-search", "二分", "search-in-rotated", "find-first-and-last"]
        ),
        TopologyNodeData(
            id="random_algo",
            topic_id="topic-02-binary-search",
            label="随机算法 (Randomized)",
            category="Searching",
            status="unvisited",
            summary="蓄水池抽样算法 (Reservoir Sampling)、Fisher-Yates 原地随机洗牌算法。",
            keywords=["random", "shuffle", "reservoir"]
        ),
        # Array Subtree - Data Structures Pipeline
        TopologyNodeData(
            id="basic_ds",
            topic_id="topic-06-stacks-queues",
            label="基础数据结构\n(循环数组/栈与队列/哈希/设计)",
            category="Data Structures",
            status="mastered",
            summary="循环队列、单调栈/单调队列、哈希表冲突处理与 LRU/LFU 缓存机制设计。",
            keywords=["stack", "queue", "lru", "lfu", "min-stack", "daily-temperatures"]
        ),
        TopologyNodeData(
            id="adv_ds",
            topic_id="topic-07-trees-bst",
            label="高级数据结构\n(二叉搜索树/堆/字典树/图论)",
            category="Data Structures",
            status="learning",
            summary="二叉搜索树性质与平衡、大顶堆/小顶堆优先队列、Trie 前缀树与图论邻接表。",
            keywords=["bst", "heap", "trie", "priority-queue", "kth-largest"]
        ),
        # Linked List & Tree Subtree - Bridge
        TopologyNodeData(
            id="ll_two_pointers",
            topic_id="topic-05-linked-lists",
            label="链表双指针",
            category="Linked List",
            status="mastered",
            summary="寻找链表中点、Floyd 判圈算法检测环形链表、合并 K 个有序链表。",
            keywords=["linked-list-cycle", "reverse-linked-list", "middle-of-the-linked-list", "merge-two-sorted-lists"]
        ),
        TopologyNodeData(
            id="recursion_tree",
            topic_id="topic-07-trees-bst",
            label="递归 (Recursion)",
            category="Recursive Mindset",
            status="mastered",
            summary="数学归纳法与调用栈本原：明确递归基、单层处理逻辑与返回值契约。",
            keywords=["recursion", "递归"]
        ),
        TopologyNodeData(
            id="binary_tree_root",
            topic_id="topic-07-trees-bst",
            label="二叉树 (Binary Tree)",
            category="Tree Hierarchies",
            status="mastered",
            summary="所有高级搜索与动态规划的母体结构。分为层序遍历视角与递归遍历视角。",
            keywords=["binary-tree", "二叉树", "tree"]
        ),
        # Tree Subtree - Level Order Pipeline
        TopologyNodeData(
            id="level_order",
            topic_id="topic-07-trees-bst",
            label="层序遍历 (Level-order)",
            category="Tree Traversal",
            status="mastered",
            summary="基于队列 Queue 实现自顶向下的逐层扫描与树的广度探索。",
            keywords=["level-order", "层序", "binary-tree-level-order"]
        ),
        TopologyNodeData(
            id="bfs_search",
            topic_id="topic-09-graphs",
            label="广度优先搜索 (BFS)",
            category="Search Algorithms",
            status="mastered",
            summary="水波纹扩散模型，求解无权图中的全局最短步数与路径。",
            keywords=["bfs", "word-ladder", "open-the-lock"]
        ),
        TopologyNodeData(
            id="shortest_path",
            topic_id="topic-09-graphs",
            label="最短路径 (Shortest Path)",
            category="Search Algorithms",
            status="learning",
            summary="Dijkstra 带权最短路、双向 BFS 搜索剪枝与 0-1 BFS 双端队列。",
            keywords=["dijkstra", "shortest-path", "network-delay-time"]
        ),
        # Tree Subtree - Recursive Traversal Multi-Branching
        TopologyNodeData(
            id="recursive_traversal",
            topic_id="topic-07-trees-bst",
            label="递归遍历 (Recursive Traversal)",
            category="Tree Paradigms",
            status="mastered",
            summary="前序/中序/后序遍历，是回溯搜索与分治降维的算法理论源泉。",
            keywords=["inorder", "preorder", "postorder", "max-depth", "invert-binary-tree"]
        ),
        # Traversal Perspective: Backtracking -> DFS
        TopologyNodeData(
            id="backtracking",
            topic_id="topic-08-backtracking",
            label="回溯算法 (Backtracking)",
            category="Exhaustive Search",
            status="mastered",
            summary="在多叉决策树上做选择、递归深入、撤销选择 (Choose -> Explore -> Unchoose)。",
            keywords=["backtracking", "回溯", "subsets", "permutations", "combination-sum", "n-queens"]
        ),
        TopologyNodeData(
            id="dfs_search",
            topic_id="topic-09-graphs",
            label="深度优先搜索 (DFS)",
            category="Exhaustive Search",
            status="mastered",
            summary="连通分量计数、网格岛屿沉没、拓扑排序与状态空间深度穷举。",
            keywords=["dfs", "number-of-islands", "surrounded-regions", "pacific-atlantic"]
        ),
        # Subproblem Perspective: Divide & Conquer -> DP
        TopologyNodeData(
            id="divide_and_conquer",
            topic_id="topic-07-trees-bst",
            label="分治算法 (Divide & Conquer)",
            category="Subproblems",
            status="mastered",
            summary="大问题拆解为互不相交的子问题，分别求解后归并（如归并排序、快速排序）。",
            keywords=["divide-and-conquer", "分治", "merge-sort", "quick-sort"]
        ),
        TopologyNodeData(
            id="dynamic_programming",
            topic_id="topic-10-dp-math",
            label="动态规划 (DP)",
            category="Optimization",
            status="learning",
            summary="重叠子问题、最优子结构与状态转移方程。分为自顶向下带备忘录与自底向上递推表格。",
            keywords=["dynamic-programming", "dp", "coin-change", "climbing-stairs", "longest-increasing-subsequence"]
        ),
        # Miscellaneous: Math -> Greedy
        TopologyNodeData(
            id="math_algo",
            topic_id="topic-10-dp-math",
            label="数学 (Math)",
            category="Discrete Math",
            status="mastered",
            summary="位运算 (Bit Manipulation)、快速幂、辗转相除法 GCD 与素数筛法。",
            keywords=["math", "bit-manipulation", "power-of-two", "single-number", "gcd"]
        ),
        TopologyNodeData(
            id="greedy_algo",
            topic_id="topic-10-dp-math",
            label="贪心算法 (Greedy)",
            category="Optimization",
            status="learning",
            summary="局部最优解能推导至全局最优解，需严格证明无后效性（如区间调度、跳跃游戏）。",
            keywords=["greedy", "贪心", "jump-game", "gas-station"]
        ),
    ]

    nodes = []
    for node in raw_nodes:
        node_dict = asdict(node)
        keywords = node_dict.pop("keywords", [])
        if items:
            count = 0
            for k, entity in items.items():
                if entity.get("type") == "problem":
                    search_blob = entity.get("search_blob", "").lower()
                    slug = entity.get("slug", "").lower()
                    tags = entity.get("tags", "").lower()
                    if any(kw.lower() in search_blob or kw.lower() in slug or kw.lower() in tags for kw in keywords):
                        count += 1
            node_dict["problem_count"] = count
        nodes.append({"data": node_dict})

    raw_edges = [
        # Root Branching
        TopologyEdgeData(id="e-root-arr", source="root", target="array_root", label="数组分支"),
        TopologyEdgeData(id="e-root-ll", source="root", target="linked_list_root", label="链表分支"),

        # Array Subtree - Operations Pipeline
        TopologyEdgeData(id="e-arr-ops", source="array_root", target="arr_ops"),
        TopologyEdgeData(id="e-ops-prefix", source="arr_ops", target="prefix_sum"),
        TopologyEdgeData(id="e-prefix-diff", source="prefix_sum", target="diff_array"),
        TopologyEdgeData(id="e-diff-2d", source="diff_array", target="matrix_2d"),

        # Array Subtree - Two Pointers Pipeline
        TopologyEdgeData(id="e-arr-tp", source="array_root", target="two_pointers_tech"),
        TopologyEdgeData(id="e-tp-arrtp", source="two_pointers_tech", target="arr_two_pointers"),
        TopologyEdgeData(id="e-arrtp-sw", source="arr_two_pointers", target="sliding_window"),
        TopologyEdgeData(id="e-sw-bs", source="sliding_window", target="binary_search"),
        TopologyEdgeData(id="e-bs-rand", source="binary_search", target="random_algo"),

        # Array Subtree - Data Structures Pipeline
        TopologyEdgeData(id="e-arr-bds", source="array_root", target="basic_ds"),
        TopologyEdgeData(id="e-bds-ads", source="basic_ds", target="adv_ds"),

        # Linked List & Tree Subtree - Bridge
        TopologyEdgeData(id="e-ll-tp", source="linked_list_root", target="ll_two_pointers"),
        TopologyEdgeData(id="e-tp-rec", source="ll_two_pointers", target="recursion_tree"),
        TopologyEdgeData(id="e-rec-bt", source="recursion_tree", target="binary_tree_root"),

        # Tree Subtree - Level Order Pipeline
        TopologyEdgeData(id="e-bt-lo", source="binary_tree_root", target="level_order", label="层序遍历"),
        TopologyEdgeData(id="e-lo-bfs", source="level_order", target="bfs_search"),
        TopologyEdgeData(id="e-bfs-sp", source="bfs_search", target="shortest_path"),

        # Tree Subtree - Recursive Traversal Multi-Branching
        TopologyEdgeData(id="e-bt-rec", source="binary_tree_root", target="recursive_traversal", label="递归遍历"),
        # Traversal Perspective
        TopologyEdgeData(id="e-rec-btk", source="recursive_traversal", target="backtracking", label="遍历视角"),
        TopologyEdgeData(id="e-btk-dfs", source="backtracking", target="dfs_search"),
        # Subproblem Perspective
        TopologyEdgeData(id="e-rec-dc", source="recursive_traversal", target="divide_and_conquer", label="子问题视角"),
        TopologyEdgeData(id="e-dc-dp", source="divide_and_conquer", target="dynamic_programming"),
        # Miscellaneous
        TopologyEdgeData(id="e-rec-math", source="recursive_traversal", target="math_algo", label="其他算法"),
        TopologyEdgeData(id="e-math-greedy", source="math_algo", target="greedy_algo"),
    ]

    edges = [{"data": asdict(edge)} for edge in raw_edges]

    return {
        "nodes": nodes,
        "edges": edges
    }
