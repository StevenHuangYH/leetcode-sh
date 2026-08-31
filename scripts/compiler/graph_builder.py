"""
Graph Builder: Generates the structured Cytoscape.js directed acyclic graph (DAG)
for the algorithm curriculum topology, automatically enriched with problem counts from workspace items.

Backed by declarative static entities in topology_definitions.py.
"""
from dataclasses import asdict
from typing import Dict, List, Any, Optional

from .topology_definitions import (
    TopologyNodePosition,
    TopologyNodeData,
    TopologyEdgeData,
    CANONICAL_TOPOLOGY_NODES,
    CANONICAL_TOPOLOGY_EDGES
)

def build_topology_graph(items: Optional[Dict[str, Any]] = None) -> Dict[str, List[Dict[str, Any]]]:
    """Constructs the canonical 38-node compound algorithm roadmap graph enriched with workspace problem counts."""
    nodes = []
    for node in CANONICAL_TOPOLOGY_NODES:
        node_dict = asdict(node)
        keywords = node_dict.pop("keywords", [])
        if items:
            count = 0
            for k, entity in items.items():
                if entity.get("type") == "problem":
                    if node.id == "data-structure-algorithm":
                        count += 1
                        continue
                    search_target = f"{entity.get('search_blob', '')} {entity.get('key', '')}".lower()
                    if any(kw.lower() in search_target for kw in keywords):
                        count += 1
            node_dict["problem_count"] = count

        element_payload = {"data": node_dict}
        if node.position:
            element_payload["position"] = node.position
        nodes.append(element_payload)

    edges = [{"data": asdict(edge)} for edge in CANONICAL_TOPOLOGY_EDGES]

    return {
        "nodes": nodes,
        "edges": edges
    }
