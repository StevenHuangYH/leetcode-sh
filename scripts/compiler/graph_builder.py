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

def _matches_entity_keywords(entity: Any, keywords: List[str]) -> bool:
    if hasattr(entity, "matches_keywords"):
        return entity.matches_keywords(keywords)
    if isinstance(entity, dict):
        search_target = f"{entity.get('search_blob', '')} {entity.get('key', '')} {entity.get('slug', '')} {entity.get('title', '')}".lower()
        return any(kw.lower() in search_target for kw in keywords)
    return False

def _extract_topology_summary(k: str, entity: Any) -> Dict[str, Any]:
    if hasattr(entity, "to_topology_summary"):
        return entity.to_topology_summary()
    if isinstance(entity, dict):
        return {
            "key": k,
            "lc_num": entity.get("lc_num", ""),
            "title": entity.get("title", ""),
            "short": entity.get("short", ""),
            "diff": entity.get("diff", "Medium"),
            "category": entity.get("category_display", "")
        }
    return {"key": k, "title": str(entity)}

def build_topology_graph(items: Optional[Dict[str, Any]] = None) -> Dict[str, List[Dict[str, Any]]]:
    """Constructs the canonical 38-node compound algorithm roadmap graph enriched with workspace problem counts."""
    nodes = []
    for node in CANONICAL_TOPOLOGY_NODES:
        node_dict = asdict(node)
        keywords = node_dict.get("keywords", [])
        if items:
            problem_list = []
            seen_keys = set()
            for k, entity in items.items():
                is_problem = entity.type == "problem" if hasattr(entity, "type") else entity.get("type") == "problem"
                if not is_problem:
                    continue
                if node.id == "data-structure-algorithm":
                    if k not in seen_keys:
                        seen_keys.add(k)
                        problem_list.append(_extract_topology_summary(k, entity))
                    continue
                if _matches_entity_keywords(entity, keywords):
                    if k not in seen_keys:
                        seen_keys.add(k)
                        problem_list.append(_extract_topology_summary(k, entity))
            node_dict["problems"] = problem_list
            node_dict["problem_count"] = len(problem_list)

        element_payload = {"data": node_dict}
        if node.position:
            element_payload["position"] = node.position
        nodes.append(element_payload)

    edges = [{"data": asdict(edge)} for edge in CANONICAL_TOPOLOGY_EDGES]

    return {
        "nodes": nodes,
        "edges": edges
    }
