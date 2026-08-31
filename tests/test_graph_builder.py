import unittest
import json
from pathlib import Path
from scripts.compiler.graph_builder import build_topology_graph, TopologyNodeData, TopologyEdgeData
from scripts.compiler.collector import collect_workspace_documents
from scripts.compiler.engine import compile_study_station

REPO_ROOT = Path(__file__).parent.parent

class TestGraphBuilder(unittest.TestCase):

    def test_topology_graph_structure_integrity(self):
        """Assert topology graph contains standard 38 nodes, 7 groups, 16 edges, valid attributes, and DAG connectivity."""
        graph = build_topology_graph()
        self.assertIn("nodes", graph)
        self.assertIn("edges", graph)

        self.assertEqual(len(graph["nodes"]), 38, "Must contain exactly 38 nodes")
        self.assertEqual(len(graph["edges"]), 16, "Must contain exactly 16 backbone edges")

        node_ids = set()
        group_ids = set()
        for node in graph["nodes"]:
            data = node["data"]
            node_id = data["id"]
            node_ids.add(node_id)
            if data.get("node_type") == "group":
                group_ids.add(node_id)
            self.assertTrue(len(data.get("label", "")) > 0, f"Node {node_id} must have non-empty label")
            self.assertTrue(len(data.get("category", "")) > 0, f"Node {node_id} must have non-empty category")
            self.assertTrue(len(data.get("topic_id", "")) > 0, f"Node {node_id} must have non-empty topic_id")

            # Check valid positions
            if "position" in node:
                self.assertIn("x", node["position"])
                self.assertIn("y", node["position"])

            # Check valid parent references for compound children
            parent = data.get("parent")
            if parent:
                self.assertIn(parent, group_ids | {"array-operation-group", "basic-ds-group", "two-pointer-group", "advanced-ds-group", "traverse-view-group", "subproblem-view-group", "other-group"})

        self.assertEqual(len(group_ids), 7, "Must contain exactly 7 group nodes")
        self.assertIn("data-structure-algorithm", node_ids)
        self.assertIn("array", node_ids)
        self.assertIn("linked", node_ids)
        self.assertIn("binary-tree", node_ids)
        self.assertIn("backtracking", node_ids)
        self.assertIn("dp", node_ids)
        self.assertIn("diff-array", node_ids)
        self.assertIn("sliding-window", node_ids)

        # Check edge consistency
        for edge in graph["edges"]:
            edge_data = edge["data"]
            source = edge_data["source"]
            target = edge_data["target"]
            self.assertIn(source, node_ids, f"Edge source {source} must exist in node_ids")
            self.assertIn(target, node_ids, f"Edge target {target} must exist in node_ids")
            self.assertNotEqual(source, target, f"Edge cannot be a self-loop: {edge_data['id']}")

    def test_problem_counting_enrichment(self):
        """Assert build_topology_graph enriches nodes with problem counts from items."""
        items = collect_workspace_documents(REPO_ROOT)
        graph = build_topology_graph(items)

        nodes_by_id = {node["data"]["id"]: node["data"] for node in graph["nodes"]}
        
        # Check that nodes have positive problem counts
        self.assertGreaterEqual(nodes_by_id["prefix-sum"]["problem_count"], 1)
        self.assertGreaterEqual(nodes_by_id["binary-search"]["problem_count"], 1)
        self.assertGreaterEqual(nodes_by_id["sliding-window"]["problem_count"], 1)
        self.assertGreaterEqual(nodes_by_id["data-structure-algorithm"]["problem_count"], 150)

    def test_document_entity_domain_methods(self):
        """Assert DocumentEntity matches_keywords and to_topology_summary encapsulation."""
        from scripts.compiler.entities import DocumentEntity
        entity = DocumentEntity.create_problem(
            key="daily-practice/lc-0216-combination-sum-3.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 216 · Combination Sum III (组合总和 III)",
            short="LC 216 Combination Sum III",
            slug="lc-0216-combination-sum-3 combination-sum-iii",
            cn_title="组合总和 III",
            en_title="Combination Sum III",
            tags="backtracking recursion dfs combinatorics",
            lc_num="LC 216",
            path="daily-practice/lc-0216-combination-sum-3",
            diff="Medium"
        )
        self.assertTrue(entity.matches_keywords(["backtracking"]))
        self.assertTrue(entity.matches_keywords(["0216"]))
        self.assertTrue(entity.matches_keywords(["lc-0216"]))
        self.assertTrue(entity.matches_keywords(["combination-sum"]))
        self.assertTrue(entity.matches_keywords(["组合"]))
        self.assertFalse(entity.matches_keywords(["linked-list"]))

        summary = entity.to_topology_summary()
        self.assertEqual(summary["key"], "daily-practice/lc-0216-combination-sum-3.py")
        self.assertEqual(summary["lc_num"], "LC 216")
        self.assertEqual(summary["diff"], "Medium")

    def test_tokenized_keyword_matching_exact_and_collision_rejection(self):
        """Assert exact token matches work and substring collisions are strictly rejected."""
        from scripts.compiler.entities import DocumentEntity

        # 1. Exact token match: backtracking, binary-tree, lc-0216
        entity_bt = DocumentEntity.create_problem(
            key="daily-practice/lc-0216-combination-sum-3.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 216 · Combination Sum III (组合总和 III)",
            short="LC 216 Combination Sum III",
            slug="lc-0216-combination-sum-3 combination-sum-iii",
            cn_title="组合总和 III",
            en_title="Combination Sum III",
            tags="backtracking recursion dfs combinatorics",
            lc_num="LC 216",
            path="daily-practice/lc-0216-combination-sum-3",
            diff="Medium"
        )
        self.assertTrue(entity_bt.matches_keywords(["backtracking"]))
        self.assertTrue(entity_bt.matches_keywords(["lc-0216"]))
        self.assertTrue(entity_bt.matches_keywords(["0216"]))
        self.assertTrue(entity_bt.matches_keywords(["216"]))
        self.assertTrue(entity_bt.matches_keywords(["combination-sum"]))

        entity_tree = DocumentEntity.create_problem(
            key="top-100/lc-0104-maximum-depth-of-binary-tree.py",
            category="Top 100 Liked Track",
            category_display="Top 100",
            title="LC 104 · Maximum Depth of Binary Tree (二叉树的最大深度)",
            short="LC 104 Maximum Depth of Binary Tree",
            slug="lc-0104-maximum-depth-of-binary-tree maximum-depth-of-binary-tree",
            cn_title="二叉树的最大深度",
            en_title="Maximum Depth of Binary Tree",
            tags="binary-tree tree dfs",
            lc_num="LC 104",
            path="top-100/lc-0104-maximum-depth-of-binary-tree",
            diff="Easy"
        )
        self.assertTrue(entity_tree.matches_keywords(["binary-tree"]))
        self.assertTrue(entity_tree.matches_keywords(["tree"]))
        self.assertTrue(entity_tree.matches_keywords(["二叉树"]))
        self.assertTrue(entity_tree.matches_keywords(["lc-0104"]))
        self.assertTrue(entity_tree.matches_keywords(["0104"]))

        # 2. Substring collisions rejected:
        # "tree" must NOT match "street"
        entity_street = DocumentEntity.create_problem(
            key="daily-practice/lc-9999-easy-street.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 9999 · Easy Street Problem (简单街道)",
            short="LC 9999 Easy Street Problem",
            slug="lc-9999-easy-street easy-street",
            cn_title="简单街道",
            en_title="Easy Street Problem",
            tags="array easy",
            lc_num="LC 9999",
            path="daily-practice/lc-9999-easy-street",
            diff="Easy"
        )
        self.assertFalse(entity_street.matches_keywords(["tree"]))
        self.assertTrue(entity_street.matches_keywords(["street"]))
        self.assertTrue(entity_street.matches_keywords(["easy-street"]))

        # "diff" must NOT match "difficult"
        entity_diff = DocumentEntity.create_problem(
            key="daily-practice/lc-9998-difficult-sum.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 9998 · Difficult Sum (困难求和)",
            short="LC 9998 Difficult Sum",
            slug="lc-9998-difficult-sum difficult-sum",
            cn_title="困难求和",
            en_title="Difficult Sum",
            tags="dp math",
            lc_num="LC 9998",
            path="daily-practice/lc-9998-difficult-sum",
            diff="Hard"
        )
        self.assertFalse(entity_diff.matches_keywords(["diff"]))
        self.assertTrue(entity_diff.matches_keywords(["difficult"]))
        self.assertTrue(entity_diff.matches_keywords(["difficult-sum"]))

        # "path" must NOT match "empathy"
        entity_path = DocumentEntity.create_problem(
            key="daily-practice/lc-9997-empathy-score.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 9997 · Empathy Score (同理心分数)",
            short="LC 9997 Empathy Score",
            slug="lc-9997-empathy-score empathy-score",
            cn_title="同理心分数",
            en_title="Empathy Score",
            tags="greedy",
            lc_num="LC 9997",
            path="daily-practice/lc-9997-empathy-score",
            diff="Medium"
        )
        self.assertFalse(entity_path.matches_keywords(["path"]))
        self.assertTrue(entity_path.matches_keywords(["empathy"]))

    def test_backtracking_node_contains_lc_77_and_lc_216(self):
        """Assert backtracking topology node contains LC 77 and LC 216."""
        items = collect_workspace_documents(REPO_ROOT)
        graph = build_topology_graph(items)
        nodes_by_id = {node["data"]["id"]: node["data"] for node in graph["nodes"]}
        
        backtracking_problems = nodes_by_id["backtracking"]["problems"]
        prob_keys = [p["key"] for p in backtracking_problems]
        self.assertTrue(any("0077" in k for k in prob_keys), "LC 77 should be in backtracking node")
        self.assertTrue(any("0216" in k for k in prob_keys), "LC 216 should be in backtracking node")


if __name__ == "__main__":
    unittest.main()


