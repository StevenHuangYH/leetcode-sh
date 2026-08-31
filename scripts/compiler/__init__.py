"""
scripts.compiler — Deep modular compiler pipeline for leetcode-sh SPA.
"""

from .entities import (
    DocumentEntity,
    RoadmapPhase,
    RoadmapTopic,
    RoadmapProblem,
    BuildResult,
    FormattedTitle,
    ProblemTitleFormatter,
    format_problem_title,
    normalize_slug,
    build_search_blob,
    read_file,
)
from .topology_definitions import (
    TopologyNodeData,
    TopologyEdgeData,
    TopologyNodePosition,
    CANONICAL_TOPOLOGY_NODES,
    CANONICAL_TOPOLOGY_EDGES,
)
from .graph_builder import build_topology_graph
from .collector import collect_workspace_documents
from .parser import parse_curriculum_topics, parse_roadmap_data
from .bundler import TemplateBundler
from .engine import StudyStationCompiler, compile_study_station

__all__ = [
    "DocumentEntity",
    "RoadmapPhase",
    "RoadmapTopic",
    "RoadmapProblem",
    "BuildResult",
    "FormattedTitle",
    "ProblemTitleFormatter",
    "format_problem_title",
    "normalize_slug",
    "build_search_blob",
    "read_file",
    "TopologyNodeData",
    "TopologyEdgeData",
    "TopologyNodePosition",
    "CANONICAL_TOPOLOGY_NODES",
    "CANONICAL_TOPOLOGY_EDGES",
    "build_topology_graph",
    "collect_workspace_documents",
    "parse_curriculum_topics",
    "parse_roadmap_data",
    "TemplateBundler",
    "StudyStationCompiler",
    "compile_study_station",
]
