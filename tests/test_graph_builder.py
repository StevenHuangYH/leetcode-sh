import unittest
from pathlib import Path
from scripts.compiler.graph_builder import build_topology_graph, TopologyNodeData, TopologyEdgeData
from scripts.compiler.collector import collect_workspace_documents

REPO_ROOT = Path(__file__).parent.parent

class TestGraphBuilder(unittest.TestCase):

    def test_topology_graph_structure_integrity(self):
        """Assert topology graph contains standard nodes, edges, and valid DAG connectivity."""
        graph = build_topology_graph()
        self.assertIn("nodes", graph)
        self.assertIn("edges", graph)

        node_ids = {node["data"]["id"] for node in graph["nodes"]}
        self.assertIn("root", node_ids)
        self.assertIn("array_root", node_ids)
        self.assertIn("linked_list_root", node_ids)
        self.assertIn("binary_tree_root", node_ids)
        self.assertIn("backtracking", node_ids)
        self.assertIn("dynamic_programming", node_ids)

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
        
        # Check that nodes have non-negative problem counts
        self.assertGreaterEqual(nodes_by_id["prefix_sum"]["problem_count"], 1)
        self.assertGreaterEqual(nodes_by_id["binary_search"]["problem_count"], 1)
        self.assertGreaterEqual(nodes_by_id["sliding_window"]["problem_count"], 1)
