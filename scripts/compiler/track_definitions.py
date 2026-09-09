from dataclasses import dataclass
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path

@dataclass(frozen=True)
class TrackConfig:
    """Domain model defining a problem track configuration."""
    id: str
    dir_path: str
    display_label: str
    category_name: str

    def to_client_descriptor(self) -> Dict[str, Any]:
        """Converts track configuration to JSON-serializable descriptor for client runtime."""
        return {
            "id": self.id,
            "dir_path": self.dir_path,
            "display_label": self.display_label,
            "category_name": self.category_name,
        }


CANONICAL_TRACKS: List[TrackConfig] = [
    TrackConfig(
        id="top-100",
        dir_path="problems/top-100",
        display_label="Top 100 Liked",
        category_name="Top 100 Liked Track",
    ),
    TrackConfig(
        id="daily-practice",
        dir_path="problems/daily-practice",
        display_label="Daily Practice",
        category_name="Daily Practice Track",
    ),
    TrackConfig(
        id="luffy",
        dir_path="problems/luffy",
        display_label="Curriculum (01-42)",
        category_name="Luffy Curriculum (01-42)",
    )
]


class TrackRegistry:
    """Central registry and lookup helper for canonical repository tracks."""

    @classmethod
    def get_all_tracks(cls) -> List[TrackConfig]:
        """Returns all configured canonical tracks."""
        return list(CANONICAL_TRACKS)

    @classmethod
    def get_track_paths(cls) -> List[str]:
        """Returns list of relative directory paths for all configured tracks."""
        return [t.dir_path for t in CANONICAL_TRACKS]

    @classmethod
    def get_collector_tuples(cls) -> List[Tuple[str, str]]:
        """Returns (dir_path, category_name) tuples for ProblemCollector."""
        return [(t.dir_path, t.category_name) for t in CANONICAL_TRACKS]

    @classmethod
    def get_track_by_id(cls, track_id: str) -> Optional[TrackConfig]:
        """Finds track configuration by track ID."""
        for t in CANONICAL_TRACKS:
            if t.id == track_id:
                return t
        return None

    @classmethod
    def to_client_json_payload(cls) -> List[Dict[str, Any]]:
        """Generates JSON-serializable list of client descriptors."""
        return [t.to_client_descriptor() for t in CANONICAL_TRACKS]
