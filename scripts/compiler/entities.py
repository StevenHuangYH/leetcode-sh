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
    en_title: str = ""
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

def read_file(path: Path) -> str:
    """Safely reads a text file."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    except Exception as e:
        return f"Error reading file: {e}"

@dataclass
class FormattedTitle:
    """Structured representation of normalized problem title metadata."""
    lc_num: str
    en_title: str
    cn_title: str
    full_title: str

    def __iter__(self):
        """Allows unpacking as a 4-tuple: lc_num, en_title, cn_title, full_title."""
        return iter((self.lc_num, self.en_title, self.cn_title, self.full_title))


class ProblemTitleFormatter:
    """Domain model responsible for normalizing problem titles across tracks."""

    KNOWN_ACRONYMS = frozenset({"oop", "bst", "dfs", "bfs", "dp", "lca", "lru", "lfu"})
    ROMAN_NUMERALS = frozenset({"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"})

    @classmethod
    def format(cls, stem: str, md_content: str = "") -> FormattedTitle:
        """
        Extracts and normalizes (lc_num, en_title, cn_title, full_title) from a filename stem and markdown content.
        Handles standard problems, curriculum prefixed problems, and non-LC tutorials.
        """
        # 1. Match LeetCode 4-digit problem number in stem
        match_lc = re.search(r'(?:^|\D)(?:lc-)?(\d{4})(?:-|$)', stem)
        if match_lc:
            num_int = int(match_lc.group(1))
            lc_num = f"LC {num_int}"
            raw_slug = re.sub(r'^(?:\d{2}-)?(?:lc-)?\d{4}-?', '', stem)
        else:
            match_range = re.search(r'^(\d{2}-\d{2})-(.+)$', stem)
            if match_range:
                lc_num = match_range.group(1)
                raw_slug = match_range.group(2)
            else:
                lc_num = ""
                raw_slug = re.sub(r'^\d{2}-', '', stem)

        # 2. Extract Chinese Title from Markdown H1 header (# LC ... | 中文标题)
        cn_title = ""
        if md_content:
            match_cn = re.search(r'# .*?\|\s*([\u4e00-\u9fa5A-Za-z0-9\s\(\)·\-—]+)', md_content)
            if match_cn:
                cn_title = match_cn.group(1).strip()

        # 3. Clean and title-case English title with acronym/Roman numeral preservation
        raw_slug = raw_slug.strip("-")
        words = [w for w in raw_slug.split("-") if w]
        cased_words = []
        for word in words:
            word_lower = word.lower()
            if word_lower in cls.KNOWN_ACRONYMS or word_lower in cls.ROMAN_NUMERALS:
                cased_words.append(word.upper())
            else:
                cased_words.append(word.capitalize())
        en_title = " ".join(cased_words)

        # 4. Construct canonical full title
        clean_fallback = en_title or raw_slug.replace("-", " ").title() or stem
        if lc_num:
            if en_title and cn_title:
                full_title = f"{lc_num} · {en_title} ({cn_title})"
            elif en_title:
                full_title = f"{lc_num} · {en_title}"
            elif cn_title:
                full_title = f"{lc_num} · {cn_title}"
            else:
                full_title = f"{lc_num} · {clean_fallback}" if clean_fallback else lc_num
        else:
            if en_title and cn_title:
                full_title = f"{en_title} ({cn_title})"
            elif en_title:
                full_title = en_title
            elif cn_title:
                full_title = cn_title
            else:
                full_title = clean_fallback

        return FormattedTitle(lc_num=lc_num, en_title=en_title, cn_title=cn_title, full_title=full_title)


# Direct functional alias for backward compatibility
format_problem_title = ProblemTitleFormatter.format
