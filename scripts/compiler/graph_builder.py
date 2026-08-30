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
    """Constructs the canonical directed algorithm roadmap graph in English, enriched with workspace problem counts."""
    raw_nodes = [
        # Root Node
        TopologyNodeData(
            id="root",
            topic_id="topic-all",
            label="Data Structures & Algorithms\nDSA Mastery",
            category="Root Paradigm",
            status="mastered",
            summary="Programs = Data Structures + Algorithms. Comprehensive mastery across linear buffers, tree/graph topologies, and advanced optimization paradigms.",
            keywords=["overview", "all"]
        ),
        # First-Level Split
        TopologyNodeData(
            id="array_root",
            topic_id="topic-01-arrays-sliding-window",
            label="Array",
            category="Linear Structures",
            status="mastered",
            summary="Contiguous memory with O(1) random access. Focus on in-place mutations, range operations, and pointer movements.",
            keywords=["array", "数组"]
        ),
        TopologyNodeData(
            id="linked_list_root",
            topic_id="topic-05-linked-lists",
            label="Linked List",
            category="Linear Structures",
            status="mastered",
            summary="Pointer-linked dynamic nodes. Core techniques: Dummy Head, Fast & Slow Pointers, and In-Place Reversal.",
            keywords=["linked-list", "链表", "linked_list"]
        ),
        # Array Subtree - Operations Pipeline
        TopologyNodeData(
            id="arr_ops",
            topic_id="topic-01-arrays-sliding-window",
            label="Array Operations",
            category="Array Basics",
            status="mastered",
            summary="In-place element removal, moving zeroes, cyclic rotation, and matrix indexing.",
            keywords=["remove-element", "move-zeroes", "rotate-array"]
        ),
        TopologyNodeData(
            id="prefix_sum",
            topic_id="topic-03-prefix-sum",
            label="Prefix Sum",
            category="Array Techniques",
            status="mastered",
            summary="O(N) precomputation enables O(1) static range sum queries; combine with hash maps for Subarray Sum = K.",
            keywords=["prefix-sum", "prefix_sum", "前缀和", "subarray-sum", "range-sum"]
        ),
        TopologyNodeData(
            id="diff_array",
            topic_id="topic-03-prefix-sum",
            label="Difference Array",
            category="Array Techniques",
            status="learning",
            summary="Optimize frequent range updates [i, j] += val from O(N) down to O(1) boundary increments.",
            keywords=["difference-array", "差分", "corporate-flight", "car-pooling"]
        ),
        TopologyNodeData(
            id="matrix_2d",
            topic_id="topic-04-intervals",
            label="2D Matrix",
            category="Array Techniques",
            status="learning",
            summary="2D prefix sums, in-place clockwise matrix rotation, spiral traversal, and diagonal reflections.",
            keywords=["matrix", "rotate-image", "spiral-matrix", "set-matrix-zeroes"]
        ),
        # Array Subtree - Two Pointers Pipeline
        TopologyNodeData(
            id="two_pointers_tech",
            topic_id="topic-01-arrays-sliding-window",
            label="Two Pointers Technique",
            category="Two Pointers",
            status="mastered",
            summary="Fast/slow pointers, collision pointers, and sliding bounds to reduce brute-force complexity by monotonicity.",
            keywords=["two-pointers", "双指针"]
        ),
        TopologyNodeData(
            id="arr_two_pointers",
            topic_id="topic-01-arrays-sliding-window",
            label="Array Two Pointers",
            category="Two Pointers",
            status="mastered",
            summary="Opposite collision pointers, Two Sum on sorted arrays, and Trapping Rain Water volumetric computation.",
            keywords=["container-with-most-water", "3sum", "two-sum-ii", "trapping-rain-water"]
        ),
        TopologyNodeData(
            id="sliding_window",
            topic_id="topic-01-arrays-sliding-window",
            label="Sliding Window",
            category="Two Pointers",
            status="mastered",
            summary="Maintain dynamic closed bounds [left, right] with monotonic expansion and shrink conditions.",
            keywords=["sliding-window", "滑动窗口", "longest-substring", "min-window"]
        ),
        TopologyNodeData(
            id="binary_search",
            topic_id="topic-02-binary-search",
            label="Binary Search",
            category="Searching",
            status="mastered",
            summary="Halve search spaces by monotonicity. Covers standard closed intervals, left/right bounds, and search by answer.",
            keywords=["binary-search", "二分", "search-in-rotated", "find-first-and-last"]
        ),
        TopologyNodeData(
            id="random_algo",
            topic_id="topic-02-binary-search",
            label="Randomized Algorithms",
            category="Searching",
            status="unvisited",
            summary="Reservoir Sampling for stream processing and Fisher-Yates in-place array shuffling.",
            keywords=["random", "shuffle", "reservoir"]
        ),
        # Array Subtree - Data Structures Pipeline
        TopologyNodeData(
            id="basic_ds",
            topic_id="topic-06-stacks-queues",
            label="Basic Data Structures\n(Circular Array / Stack / Queue / Hash / LRU)",
            category="Data Structures",
            status="mastered",
            summary="Circular queues, monotonic stacks, monotonic queues, hash collisions, and LRU/LFU cache eviction design.",
            keywords=["stack", "queue", "lru", "lfu", "min-stack", "daily-temperatures"]
        ),
        TopologyNodeData(
            id="adv_ds",
            topic_id="topic-07-trees-bst",
            label="Advanced Data Structures\n(BST / Heap / Trie / Graph)",
            category="Data Structures",
            status="learning",
            summary="BST properties and balanced trees, priority queues/heaps, prefix tries, and adjacency graph representations.",
            keywords=["bst", "heap", "trie", "priority-queue", "kth-largest"]
        ),
        # Linked List & Tree Subtree - Bridge
        TopologyNodeData(
            id="ll_two_pointers",
            topic_id="topic-05-linked-lists",
            label="Linked List Two Pointers",
            category="Linked List",
            status="mastered",
            summary="Find middle nodes, detect cycles using Floyd's Tortoise and Hare, and merge K sorted lists.",
            keywords=["linked-list-cycle", "reverse-linked-list", "middle-of-the-linked-list", "merge-two-sorted-lists"]
        ),
        TopologyNodeData(
            id="recursion_tree",
            topic_id="topic-07-trees-bst",
            label="Recursion Foundations",
            category="Recursive Mindset",
            status="mastered",
            summary="Mathematical induction and call stack fundamentals: base cases, single-level contracts, and return values.",
            keywords=["recursion", "递归"]
        ),
        TopologyNodeData(
            id="binary_tree_root",
            topic_id="topic-07-trees-bst",
            label="Binary Tree",
            category="Tree Hierarchies",
            status="mastered",
            summary="Foundational hierarchy for advanced search and dynamic programming. Branches into level-order and recursive traversals.",
            keywords=["binary-tree", "二叉树", "tree"]
        ),
        # Tree Subtree - Level Order Pipeline
        TopologyNodeData(
            id="level_order",
            topic_id="topic-07-trees-bst",
            label="Level-Order Traversal",
            category="Tree Traversal",
            status="mastered",
            summary="Queue-driven top-to-bottom breadth scanning and layered tree exploration.",
            keywords=["level-order", "层序", "binary-tree-level-order"]
        ),
        TopologyNodeData(
            id="bfs_search",
            topic_id="topic-09-graphs",
            label="Breadth-First Search (BFS)",
            category="Search Algorithms",
            status="mastered",
            summary="Wavefront expansion model for finding global shortest paths and minimum transitions in unweighted state graphs.",
            keywords=["bfs", "word-ladder", "open-the-lock"]
        ),
        TopologyNodeData(
            id="shortest_path",
            topic_id="topic-09-graphs",
            label="Shortest Path",
            category="Search Algorithms",
            status="learning",
            summary="Dijkstra's weighted shortest paths, bidirectional BFS branch pruning, and 0-1 BFS with deques.",
            keywords=["dijkstra", "shortest-path", "network-delay-time"]
        ),
        # Tree Subtree - Recursive Traversal Multi-Branching
        TopologyNodeData(
            id="recursive_traversal",
            topic_id="topic-07-trees-bst",
            label="Recursive Traversal",
            category="Tree Paradigms",
            status="mastered",
            summary="Preorder, Inorder, and Postorder traversals — the theoretical origin of Backtracking and Divide & Conquer.",
            keywords=["inorder", "preorder", "postorder", "max-depth", "invert-binary-tree"]
        ),
        # Traversal Perspective: Backtracking -> DFS
        TopologyNodeData(
            id="backtracking",
            topic_id="topic-08-backtracking",
            label="Backtracking",
            category="Exhaustive Search",
            status="mastered",
            summary="State-space decision trees: Choose -> Explore -> Unchoose pattern for permutations, subsets, and N-Queens.",
            keywords=["backtracking", "回溯", "subsets", "permutations", "combination-sum", "n-queens"]
        ),
        TopologyNodeData(
            id="dfs_search",
            topic_id="topic-09-graphs",
            label="Depth-First Search (DFS)",
            category="Exhaustive Search",
            status="mastered",
            summary="Connected components, island flooding algorithms, topological sorting, and deep recursion exploration.",
            keywords=["dfs", "number-of-islands", "surrounded-regions", "pacific-atlantic"]
        ),
        # Subproblem Perspective: Divide & Conquer -> DP
        TopologyNodeData(
            id="divide_and_conquer",
            topic_id="topic-07-trees-bst",
            label="Divide & Conquer",
            category="Subproblems",
            status="mastered",
            summary="Deconstruct problems into disjoint subproblems, solve independently, and merge results (e.g. Merge Sort).",
            keywords=["divide-and-conquer", "分治", "merge-sort", "quick-sort"]
        ),
        TopologyNodeData(
            id="dynamic_programming",
            topic_id="topic-10-dp-math",
            label="Dynamic Programming (DP)",
            category="Optimization",
            status="learning",
            summary="Overlapping subproblems, optimal substructure, and state transition tables (memoization vs tabulation).",
            keywords=["dynamic-programming", "dp", "coin-change", "climbing-stairs", "longest-increasing-subsequence"]
        ),
        # Miscellaneous: Math -> Greedy
        TopologyNodeData(
            id="math_algo",
            topic_id="topic-10-dp-math",
            label="Math & Bit Manipulation",
            category="Discrete Math",
            status="mastered",
            summary="Bit manipulation tricks, binary exponentiation, Euclidean GCD algorithm, and prime number sieves.",
            keywords=["math", "bit-manipulation", "power-of-two", "single-number", "gcd"]
        ),
        TopologyNodeData(
            id="greedy_algo",
            topic_id="topic-10-dp-math",
            label="Greedy Algorithms",
            category="Optimization",
            status="learning",
            summary="Prove local optimal choices yield global optimum with no aftermath (e.g. Interval Scheduling, Jump Game).",
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
                    if node.id == "root":
                        count += 1
                        continue
                    slug = entity.get("slug", "").lower()
                    tags = entity.get("tags", "").lower()
                    title = entity.get("title", "").lower()
                    cn_title = entity.get("cn_title", "").lower()
                    key = entity.get("key", "").lower()
                    search_target = f"{slug} {tags} {title} {cn_title} {key}"
                    if any(kw.lower() in search_target for kw in keywords):
                        count += 1
            node_dict["problem_count"] = count
        nodes.append({"data": node_dict})

    raw_edges = [
        # Root Branching
        TopologyEdgeData(id="e-root-arr", source="root", target="array_root", label="Array Branch"),
        TopologyEdgeData(id="e-root-ll", source="root", target="linked_list_root", label="Linked List Branch"),

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
        TopologyEdgeData(id="e-bt-lo", source="binary_tree_root", target="level_order", label="Level-Order"),
        TopologyEdgeData(id="e-lo-bfs", source="level_order", target="bfs_search"),
        TopologyEdgeData(id="e-bfs-sp", source="bfs_search", target="shortest_path"),

        # Tree Subtree - Recursive Traversal Multi-Branching
        TopologyEdgeData(id="e-bt-rec", source="binary_tree_root", target="recursive_traversal", label="Recursive"),
        # Traversal Perspective
        TopologyEdgeData(id="e-rec-btk", source="recursive_traversal", target="backtracking", label="Traversal"),
        TopologyEdgeData(id="e-btk-dfs", source="backtracking", target="dfs_search"),
        # Subproblem Perspective
        TopologyEdgeData(id="e-rec-dc", source="recursive_traversal", target="divide_and_conquer", label="Subproblems"),
        TopologyEdgeData(id="e-dc-dp", source="divide_and_conquer", target="dynamic_programming"),
        # Miscellaneous
        TopologyEdgeData(id="e-rec-math", source="recursive_traversal", target="math_algo", label="Other Paradigms"),
        TopologyEdgeData(id="e-math-greedy", source="math_algo", target="greedy_algo"),
    ]

    edges = [{"data": asdict(edge)} for edge in raw_edges]

    return {
        "nodes": nodes,
        "edges": edges
    }
