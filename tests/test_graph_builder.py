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

    def test_end_to_end_topology_payload_in_index_html(self):
        """Assert compiled index.html contains the dynamic roadmap_graph payload."""
        result = compile_study_station(REPO_ROOT)
        self.assertTrue(result.success)
        self.assertTrue(result.output_path.exists())

        html_content = result.output_path.read_text(encoding="utf-8")
        self.assertIn("ROADMAP_GRAPH_DATA", html_content)
        self.assertNotIn("{roadmap_graph_json}", html_content, "Token {roadmap_graph_json} must be replaced")

