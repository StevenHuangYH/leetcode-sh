import re
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Dict, List, Optional, Any

@dataclass
class DocumentEntity:
    key: str
    category: str
    title: str
    short: str
    slug: str
    cn_title: str
    tags: str
    lc_num: str
    search_blob: str
    path: str
    type: str = "problem"
    notes: str = ""
    code: str = ""
    diff: str = "All"
    py_file: str = ""
    md_file: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class RoadmapProblem:
    num: int
    name: str
    cn: str
    diff: str
    key: str

@dataclass
class RoadmapTopic:
    id: str
    title: str
    subtitle: str
    icon: str
    formula: str
    problems: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class RoadmapPhase:
    phase: int
    phase_name: str
    phase_badge: str
    phase_desc: str
    topics: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class BuildResult:
    output_path: Path
    total_entities: int
    total_phases: int
    success: bool = True
    error_message: Optional[str] = None

def normalize_slug(text: str) -> str:
    """Normalizes problem title to a clean slug for searching."""
    text = re.sub(r"[\(\)\[\]\{\}\.,:;!\?`'\"]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()

def build_search_blob(tokens: List[str], text_content: str = "") -> str:
    """Builds a normalized, space-separated searchable string with deduplicated tokens."""
    token_str = normalize_slug(" ".join(tokens))
    seen = set(token_str.split())
    if text_content:
        clean_text = re.sub(r"[\r\n\t]+", " ", text_content)
        clean_text = re.sub(r"[#\*`_\[\]\(\)\{\}\.,:;!\?'\"/\\<>=~^$|&%@+-]", " ", clean_text)
        words = clean_text.lower().split()
        for w in words[:300]:
            if len(w) > 1 and w not in seen:
                seen.add(w)
    return " ".join(sorted(seen))

def read_file(path: Path) -> str:
    """Safely reads a text file."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    except Exception as e:
        return f"Error reading file: {e}"
