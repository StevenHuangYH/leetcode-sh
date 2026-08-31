"""
Topology Definitions: Declarative domain entities and canonical node/edge registries
for the 38-node compound algorithm topology graph.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class TopologyNodePosition:
    x: float
    y: float

@dataclass
class TopologyNodeData:
    id: str
    topic_id: str
    label: str
    category: str
    node_type: str = "normal"  # "normal" | "group"
    parent: Optional[str] = None
    status: str = "mastered"
    summary: str = ""
    keywords: List[str] = field(default_factory=list)
    problem_count: int = 0
    color: Optional[Dict[str, str]] = None
    position: Optional[Dict[str, float]] = None

@dataclass
class TopologyEdgeData:
    id: str
    source: str
    target: str
    label: str = ""
    source_handle: str = "bottom"
    target_handle: str = "top"

CANONICAL_TOPOLOGY_NODES: List[TopologyNodeData] = [
    # Root Node
    TopologyNodeData(
        id="data-structure-algorithm",
        topic_id="topic-all",
        label="Data Structure & Algorithm\n数据结构与算法",
        category="Root Paradigm",
        node_type="normal",
        position={"x": 400, "y": 50},
        color={"lightMode": "#52c41a", "darkMode": "#389e0d"},
        status="mastered",
        summary="Programs = Data Structures + Algorithms. Comprehensive mastery across linear buffers, tree/graph topologies, and optimization paradigms.",
        keywords=["overview", "all"]
    ),

    # First-Level Split (Linear Roots)
    TopologyNodeData(
        id="array",
        topic_id="topic-01-arrays-sliding-window",
        label="Array\n数组",
        category="Linear Structures",
        node_type="normal",
        position={"x": 150, "y": 200},
        color={"lightMode": "#13c2c2", "darkMode": "#08979c"},
        status="mastered",
        summary="Contiguous memory buffer with O(1) random indexing. Focus on in-place mutations, range operations, and pointer movements.",
        keywords=["array", "数组", "nums"]
    ),
    TopologyNodeData(
        id="linked",
        topic_id="topic-05-linked-lists",
        label="Linked List\n链表",
        category="Linear Structures",
        node_type="normal",
        position={"x": 650, "y": 200},
        color={"lightMode": "#1890ff", "darkMode": "#096dd9"},
        status="mastered",
        summary="Discrete pointer-linked dynamic nodes. Core techniques: Dummy Head, Multi-Pointer Steps, and In-Place Linkage Reversals.",
        keywords=["linked-list", "链表", "linked_list", "listnode"]
    ),

    # -------------------------------------------------------------
    # Group 1: Array Operations Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="array-operation-group",
        topic_id="topic-01-arrays-sliding-window",
        label="Operations\n数组核心操作",
        category="Array Basics",
        node_type="group",
        position={"x": 40, "y": 350},
        status="mastered",
        summary="Foundational array transformation techniques: difference arrays, 2D matrix geometry, and prefix sum range query invariants."
    ),
    TopologyNodeData(
        id="diff-array",
        parent="array-operation-group",
        topic_id="topic-03-prefix-sum",
        label="Diff Array\n差分数组",
        category="Array Techniques",
        node_type="normal",
        position={"x": 100, "y": 380},
        status="learning",
        summary="Optimize frequent range updates [i, j] += val from O(N) down to O(1) boundary increments diff[i]+=val, diff[j+1]-=val.",
        keywords=["difference-array", "差分", "corporate-flight", "car-pooling", "flight", "booking"]
    ),
    TopologyNodeData(
        id="2d-array-ops",
        parent="array-operation-group",
        topic_id="topic-04-intervals",
        label="2D Array\n二维矩阵",
        category="Array Techniques",
        node_type="normal",
        position={"x": 100, "y": 450},
        status="learning",
        summary="2D prefix sums, in-place clockwise matrix rotation via diagonal reflection + horizontal row reversal, and spiral scanning.",
        keywords=["matrix", "rotate-image", "spiral-matrix", "set-matrix-zeroes", "game-of-life", "矩阵", "二维"]
    ),
    TopologyNodeData(
        id="prefix-sum",
        parent="array-operation-group",
        topic_id="topic-03-prefix-sum",
        label="Prefix Sum\n前缀和",
        category="Array Techniques",
        node_type="normal",
        position={"x": 100, "y": 520},
        status="mastered",
        summary="O(N) precomputation enables O(1) static range sum queries; combine with hash maps for Subarray Sum = K.",
        keywords=["prefix-sum", "prefix_sum", "前缀和", "subarray-sum", "range-sum", "running-sum"]
    ),

    # -------------------------------------------------------------
    # Group 2: Basic Data Structure Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="basic-ds-group",
        topic_id="topic-06-stacks-queues",
        label="Basic Data Structure\n基础数据结构",
        category="Data Structures",
        node_type="group",
        position={"x": 350, "y": 350},
        status="mastered",
        summary="Core linear abstract data types: circular queues, monotonic stacks, collision-resistant hash maps, and composite LRU cache designs."
    ),
    TopologyNodeData(
        id="cycle-array",
        parent="basic-ds-group",
        topic_id="topic-06-stacks-queues",
        label="Cycle Array\n环形数组",
        category="Data Structures",
        node_type="normal",
        position={"x": 365, "y": 385},
        status="mastered",
        summary="Modulo arithmetic (index = (i + offset) % cap) avoids memory re-allocation in circular queues and buffer wheels.",
        keywords=["cycle-array", "circular", "rotate-array", "ring-buffer", "环形"]
    ),
    TopologyNodeData(
        id="stack-queue",
        parent="basic-ds-group",
        topic_id="topic-06-stacks-queues",
        label="Stack & Queue\n栈与队列",
        category="Data Structures",
        node_type="normal",
        position={"x": 500, "y": 385},
        color={"lightMode": "#faad14", "darkMode": "#d48806"},
        status="mastered",
        summary="LIFO stack parentheses matching, monotonic stacks for Next Greater Element, and monotonic queues for Sliding Window Maximum.",
        keywords=["stack", "queue", "min-stack", "daily-temperatures", "valid-parentheses", "sliding-window-maximum", "单调栈", "队列"]
    ),
    TopologyNodeData(
        id="hashing",
        parent="basic-ds-group",
        topic_id="topic-04-intervals",
        label="Hashing\n哈希技术",
        category="Data Structures",
        node_type="normal",
        position={"x": 365, "y": 455},
        status="mastered",
        summary="O(1) average lookup and insertion; hash sets for deduplication, frequency counting, and in-place sign marking.",
        keywords=["hash", "hashing", "two-sum", "group-anagrams", "longest-consecutive", "哈希"]
    ),
    TopologyNodeData(
        id="design",
        parent="basic-ds-group",
        topic_id="topic-06-stacks-queues",
        label="Design\n结构设计",
        category="Data Structures",
        node_type="normal",
        position={"x": 500, "y": 455},
        status="mastered",
        summary="Composite data structure engineering: LRU cache (Hash Map + Doubly Linked List) and LFU frequency ranking.",
        keywords=["design", "lru", "lfu", "lru-cache", "trie", "设计"]
    ),

    # -------------------------------------------------------------
    # Group 3: Array Two Pointer Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="two-pointer-group",
        topic_id="topic-01-arrays-sliding-window",
        label="Array Two Pointer\n数组双指针",
        category="Two Pointers",
        node_type="group",
        position={"x": 40, "y": 650},
        status="mastered",
        summary="Techniques leveraging mathematical monotonicity to prune quadratic search spaces down to linear or logarithmic time."
    ),
    TopologyNodeData(
        id="two-pointer-array",
        parent="two-pointer-group",
        topic_id="topic-01-arrays-sliding-window",
        label="Two Pointer\n对撞与快慢指针",
        category="Two Pointers",
        node_type="normal",
        position={"x": 100, "y": 630},
        status="mastered",
        summary="Opposite collision pointers for sorted Two Sum / 3Sum and volumetric Trapping Rain Water computations.",
        keywords=["two-pointer", "two-pointers", "3sum", "container-with-most-water", "trapping-rain-water", "双指针", "对撞"]
    ),
    TopologyNodeData(
        id="sliding-window",
        parent="two-pointer-group",
        topic_id="topic-01-arrays-sliding-window",
        label="Sliding Window\n滑动窗口",
        category="Two Pointers",
        node_type="normal",
        position={"x": 100, "y": 700},
        color={"lightMode": "#13c2c2", "darkMode": "#08979c"},
        status="mastered",
        summary="Maintain dynamic closed bounds [left, right] with monotonic right++ expansion and left++ shrink conditions.",
        keywords=["sliding-window", "滑动窗口", "longest-substring", "min-window", "minimum-window", "find-all-anagrams", "substring"]
    ),
    TopologyNodeData(
        id="binary-search",
        parent="two-pointer-group",
        topic_id="topic-02-binary-search",
        label="Binary Search\n二分搜索",
        category="Searching",
        node_type="normal",
        position={"x": 100, "y": 770},
        status="mastered",
        summary="Halve search spaces by monotonicity: standard closed intervals, left/right bound searches, and search-by-answer ranges.",
        keywords=["binary-search", "二分", "search-in-rotated", "find-first-and-last", "search-a-2d-matrix", "find-minimum-in-rotated"]
    ),
    TopologyNodeData(
        id="random",
        parent="two-pointer-group",
        topic_id="topic-02-binary-search",
        label="Randomize\n随机算法",
        category="Searching",
        node_type="normal",
        position={"x": 100, "y": 840},
        status="unvisited",
        summary="Reservoir Sampling for dynamic data streams (1/k probability) and Fisher-Yates uniform in-place array shuffling.",
        keywords=["random", "shuffle", "reservoir", "sampling", "随机"]
    ),

    # -------------------------------------------------------------
    # Linked List & Tree Subtree - Pipeline Bridge
    # -------------------------------------------------------------
    TopologyNodeData(
        id="two-pointer-linked",
        topic_id="topic-05-linked-lists",
        label="Two Pointer\n链表双指针",
        category="Linked List",
        node_type="normal",
        position={"x": 720, "y": 350},
        status="mastered",
        summary="Floyd's Tortoise and Hare cycle detection (2k - k = n*cycle), finding midpoint, and K-group recursive reversals.",
        keywords=["linked-list-cycle", "middle-of-the-linked-list", "reorder-list", "reverse-nodes-in-k-group", "快慢指针", "环形链表"]
    ),
    TopologyNodeData(
        id="recursion-ops",
        topic_id="topic-07-trees-bst",
        label="Recursion\n递归思维",
        category="Recursive Mindset",
        node_type="normal",
        position={"x": 720, "y": 450},
        status="mastered",
        summary="Mathematical induction and call stack contracts: establish base cases, execute current layer logic, and trust return values.",
        keywords=["recursion", "recursive", "invert-binary-tree", "递归"]
    ),
    TopologyNodeData(
        id="binary-tree",
        topic_id="topic-07-trees-bst",
        label="Binary Tree\n二叉树",
        category="Tree Hierarchies",
        node_type="normal",
        position={"x": 720, "y": 550},
        color={"lightMode": "#1890ff", "darkMode": "#096dd9"},
        status="mastered",
        summary="Foundational hierarchy bridging linear lists to tree/graph topologies and dynamic programming state transitions.",
        keywords=["binary-tree", "二叉树", "tree", "treenode", "depth", "max-depth"]
    ),

    # -------------------------------------------------------------
    # Level-Order Pipeline
    # -------------------------------------------------------------
    TopologyNodeData(
        id="level-order-traverse",
        topic_id="topic-07-trees-bst",
        label="Level Traverse\n层序遍历",
        category="Tree Traversal",
        node_type="normal",
        position={"x": 850, "y": 670},
        status="mastered",
        summary="Queue-driven top-to-bottom breadth scanning; layer size snapshots (sz = q.size()) isolate tree levels cleanly.",
        keywords=["level-order", "层序", "binary-tree-level-order", "zigzag", "right-side-view", "bottom-left"]
    ),
    TopologyNodeData(
        id="bfs",
        topic_id="topic-09-graphs",
        label="BFS\n广度优先搜索",
        category="Search Algorithms",
        node_type="normal",
        position={"x": 850, "y": 785},
        color={"lightMode": "#1890ff", "darkMode": "#096dd9"},
        status="mastered",
        summary="Wavefront expansion model for finding global shortest paths and minimum transitions in unweighted state graphs.",
        keywords=["bfs", "breadth-first", "word-ladder", "open-the-lock", "广度优先"]
    ),
    TopologyNodeData(
        id="shortest-path",
        topic_id="topic-09-graphs",
        label="Shortest Path\n最短路径",
        category="Search Algorithms",
        node_type="normal",
        position={"x": 850, "y": 900},
        status="learning",
        summary="Dijkstra priority queue state relaxation, 0-1 BFS with double-ended queues, and bidirectional search branch pruning.",
        keywords=["dijkstra", "shortest-path", "network-delay-time", "cheapest-flights", "最短路径"]
    ),

    # -------------------------------------------------------------
    # Recursive Traversal Pipeline
    # -------------------------------------------------------------
    TopologyNodeData(
        id="recursive-traverse",
        topic_id="topic-07-trees-bst",
        label="Recursive Traverse\n递归遍历",
        category="Tree Paradigms",
        node_type="normal",
        position={"x": 620, "y": 670},
        status="mastered",
        summary="Preorder, Inorder, and Postorder traversals — the theoretical origin of Backtracking and Divide & Conquer.",
        keywords=["inorder", "preorder", "postorder", "construct-binary-tree", "diameter", "flatten"]
    ),

    # -------------------------------------------------------------
    # Group 4: Traverse View Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="traverse-view-group",
        topic_id="topic-08-backtracking",
        label="Traverse View\n遍历视角",
        category="Exhaustive Search",
        node_type="group",
        position={"x": 450, "y": 780},
        status="mastered",
        summary="Exhaustive decision tree exploration: maintain state path, explore child branches, and unchoose upon backtracking."
    ),
    TopologyNodeData(
        id="dfs",
        parent="traverse-view-group",
        topic_id="topic-09-graphs",
        label="DFS\n深度优先搜索",
        category="Exhaustive Search",
        node_type="normal",
        position={"x": 390, "y": 930},
        color={"lightMode": "#f5222d", "darkMode": "#cf1322"},
        status="mastered",
        summary="Connected components, flood fill algorithms, cycle detection via onPath arrays, and topological sorting.",
        keywords=["dfs", "depth-first", "number-of-islands", "surrounded-regions", "pacific-atlantic", "深度优先"]
    ),
    TopologyNodeData(
        id="backtracking",
        parent="traverse-view-group",
        topic_id="topic-08-backtracking",
        label="Backtracking\n回溯算法",
        category="Exhaustive Search",
        node_type="normal",
        position={"x": 390, "y": 1000},
        color={"lightMode": "#f5222d", "darkMode": "#cf1322"},
        status="mastered",
        summary="State-space decision trees: Choose -> Explore -> Unchoose pattern for subsets, permutations, combinations, and N-Queens.",
        keywords=["backtracking", "回溯", "subsets", "permutations", "combinations", "combination-sum", "combination", "n-queens", "palindrome-partitioning", "word-search", "组合"]
    ),



    # -------------------------------------------------------------
    # Group 5: Subproblem View Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="subproblem-view-group",
        topic_id="topic-10-dp-math",
        label="Subproblem View\n子问题视角",
        category="Optimization",
        node_type="group",
        position={"x": 650, "y": 780},
        status="mastered",
        summary="Deconstruct problems into smaller instances: independent subproblems (Divide & Conquer) vs overlapping states (DP)."
    ),
    TopologyNodeData(
        id="divide-conquer",
        parent="subproblem-view-group",
        topic_id="topic-07-trees-bst",
        label="Divide & Conquer\n分治算法",
        category="Subproblems",
        node_type="normal",
        position={"x": 640, "y": 930},
        status="mastered",
        summary="Deconstruct into disjoint subproblems, solve independently, and merge results (e.g. Merge Sort, Quick Select).",
        keywords=["divide-and-conquer", "分治", "merge-sort", "quick-sort", "kth-largest", "sort-list"]
    ),
    TopologyNodeData(
        id="dp",
        parent="subproblem-view-group",
        topic_id="topic-10-dp-math",
        label="DP\n动态规划",
        category="Optimization",
        node_type="normal",
        position={"x": 640, "y": 1000},
        color={"lightMode": "#722ed1", "darkMode": "#531dab"},
        status="learning",
        summary="Overlapping subproblems, optimal substructure, and state transition equations (memoization vs bottom-up tabulation).",
        keywords=["dynamic-programming", "dp", "coin-change", "climbing-stairs", "longest-increasing-subsequence", "longest-common", "动态规划"]
    ),

    # -------------------------------------------------------------
    # Group 6: Other Group & Children (Math & Greedy)
    # -------------------------------------------------------------
    TopologyNodeData(
        id="other-group",
        topic_id="topic-10-dp-math",
        label="Other\n其他算法",
        category="Discrete & Optimization",
        node_type="group",
        position={"x": 250, "y": 780},
        status="mastered",
        summary="Specialized algorithmic paradigms: mathematical logic, bitwise arithmetic, and greedy choice heuristics."
    ),
    TopologyNodeData(
        id="math",
        parent="other-group",
        topic_id="topic-10-dp-math",
        label="Math\n数学与位运算",
        category="Discrete Math",
        node_type="normal",
        position={"x": 200, "y": 930},
        status="mastered",
        summary="Bitwise manipulations (n & n-1), XOR properties, binary exponentiation, and Euclidean GCD algorithms.",
        keywords=["math", "bit-manipulation", "single-number", "power-of-two", "counting-bits", "stone-game", "位运算", "数学"]
    ),
    TopologyNodeData(
        id="greedy",
        parent="other-group",
        topic_id="topic-10-dp-math",
        label="Greedy\n贪心算法",
        category="Optimization",
        node_type="normal",
        position={"x": 200, "y": 1000},
        status="learning",
        summary="Prove local optimal choices yield global optimum with no aftermath (e.g. Interval Scheduling, Jump Game, Gas Station).",
        keywords=["greedy", "贪心", "jump-game", "gas-station", "interval", "non-overlapping"]
    ),

    # -------------------------------------------------------------
    # Group 7: Advanced Data Structure Group & Children
    # -------------------------------------------------------------
    TopologyNodeData(
        id="advanced-ds-group",
        topic_id="topic-07-trees-bst",
        label="Advanced Data Structure\n高阶数据结构",
        category="Data Structures",
        node_type="group",
        position={"x": 270, "y": 550},
        status="learning",
        summary="Advanced tree and graph structures: BST invariants, binary heap priority queues, prefix tries, and graph adjacency topologies."
    ),
    TopologyNodeData(
        id="bst",
        parent="advanced-ds-group",
        topic_id="topic-07-trees-bst",
        label="BST\n二叉搜索树",
        category="Data Structures",
        node_type="normal",
        position={"x": 285, "y": 585},
        status="mastered",
        summary="BST invariant (Left < Root < Right) enables logarithmic search, insertion, deletion, and sorted inorder streaming.",
        keywords=["bst", "binary-search-tree", "validate-binary-search-tree", "lowest-common-ancestor", "kth-smallest"]
    ),
    TopologyNodeData(
        id="heap",
        parent="advanced-ds-group",
        topic_id="topic-07-trees-bst",
        label="Heap\n堆与优先队列",
        category="Data Structures",
        node_type="normal",
        position={"x": 420, "y": 585},
        status="mastered",
        summary="Complete binary tree maintaining min/max invariant; swim/sink operations achieve O(log N) priority queue operations.",
        keywords=["heap", "priority-queue", "find-median-from-data-stream", "top-k-frequent", "kth-largest-element", "堆"]
    ),
    TopologyNodeData(
        id="trie",
        parent="advanced-ds-group",
        topic_id="topic-07-trees-bst",
        label="Trie\n前缀字典树",
        category="Data Structures",
        node_type="normal",
        position={"x": 285, "y": 655},
        status="mastered",
        summary="Multi-way tree for high-efficiency prefix matching, string dictionary search, and autocomplete wildcards.",
        keywords=["trie", "prefix-tree", "implement-trie", "word-search-ii", "前缀树", "字典树"]
    ),
    TopologyNodeData(
        id="graph",
        parent="advanced-ds-group",
        topic_id="topic-09-graphs",
        label="Graph\n图论进阶",
        category="Data Structures",
        node_type="normal",
        position={"x": 420, "y": 655},
        status="learning",
        summary="Adjacency list representations, Kahn's topological sort algorithm, bipartite checks, and Union-Find disjoint sets.",
        keywords=["graph", "course-schedule", "is-graph-bipartite", "union-find", "disjoint-set", "图论", "拓扑排序"]
    ),
]

CANONICAL_TOPOLOGY_EDGES: List[TopologyEdgeData] = [
    # Root Branching
    TopologyEdgeData(id="e-data-structure-algorithm-array", source="data-structure-algorithm", target="array", label="Array Branch"),
    TopologyEdgeData(id="e-data-structure-algorithm-linked", source="data-structure-algorithm", target="linked", label="Linked List Branch"),

    # Array Subtree - Operations & Basic DS
    TopologyEdgeData(id="e-array-array-operation-group", source="array", target="array-operation-group"),
    TopologyEdgeData(id="e-array-operation-group-two-pointer-group", source="array-operation-group", target="two-pointer-group"),
    TopologyEdgeData(id="e-array-operation-group-basic-ds-group", source="array-operation-group", target="basic-ds-group"),

    # Linked List & Basic DS / Tree Bridge
    TopologyEdgeData(id="e-linked-basic-ds-group", source="linked", target="basic-ds-group"),
    TopologyEdgeData(id="e-linked-two-pointer-linked", source="linked", target="two-pointer-linked"),
    TopologyEdgeData(id="e-two-pointer-linked-recursion-ops", source="two-pointer-linked", target="recursion-ops"),
    TopologyEdgeData(id="e-recursion-ops-binary-tree", source="recursion-ops", target="binary-tree"),

    # Tree Subtree - Level Order & BFS
    TopologyEdgeData(id="e-binary-tree-level-order-traverse", source="binary-tree", target="level-order-traverse", label="Level-Order"),
    TopologyEdgeData(id="e-level-order-traverse-bfs", source="level-order-traverse", target="bfs"),
    TopologyEdgeData(id="e-bfs-shortest-path", source="bfs", target="shortest-path"),

    # Tree Subtree - Advanced DS Branch
    TopologyEdgeData(id="e-binary-tree-advanced-ds-group", source="binary-tree", target="advanced-ds-group", label="Advanced DS"),

    # Tree Subtree - Recursive Traversal Multi-Branching
    TopologyEdgeData(id="e-binary-tree-recursive-traverse", source="binary-tree", target="recursive-traverse", label="Recursive"),
    TopologyEdgeData(id="e-recursive-traverse-traverse-view-group", source="recursive-traverse", target="traverse-view-group", label="Traversal View"),
    TopologyEdgeData(id="e-recursive-traverse-subproblem-view-group", source="recursive-traverse", target="subproblem-view-group", label="Subproblem View"),
]
