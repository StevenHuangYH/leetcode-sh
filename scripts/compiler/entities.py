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
    category_display: str = ""
    notes: str = ""
    code: str = ""
    diff: str = "All"
    py_file: str = ""
    md_file: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def matches_keywords(self, keywords: List[str]) -> bool:
        """Determines whether this entity matches any of the canonical topology keywords using tokenized word-boundary matching."""
        if not keywords:
            return False

        # Gather metadata fields for token extraction and phrase matching
        raw_parts = [
            self.slug or "",
            self.tags or "",
            self.title or "",
            self.category or "",
            self.category_display or "",
            self.short or "",
            self.lc_num or "",
            self.en_title or "",
            self.cn_title or "",
            self.key or "",
            self.path or ""
        ]
        raw_text = " ".join(raw_parts).lower()

        # Clean punctuation except hyphens, underscores, word characters and CJK
        cleaned_text = re.sub(r"[^\w\-\u4e00-\u9fff]+", " ", raw_text)
        word_sequence = [w for w in re.split(r"[-_\s]+", cleaned_text) if w]
        word_seq_len = len(word_sequence)

        # Build token set with individual words and preserved hyphenated/underscore chunks
        token_set = set(word_sequence)
        for chunk in cleaned_text.split():
            clean_chunk = chunk.strip("-_")
            if clean_chunk:
                token_set.add(clean_chunk)
                if "_" in clean_chunk:
                    token_set.add(clean_chunk.replace("_", "-"))

        # Extract LC problem number variations
        lc_sources = [self.lc_num, self.key, self.slug, self.path]
        for src in lc_sources:
            if not src:
                continue
            for m in re.finditer(r'(?:lc-?|\b)(\d{1,4})\b', str(src).lower()):
                try:
                    num_int = int(m.group(1))
                    if num_int > 0:
                        raw_num = str(num_int)
                        padded = f"{num_int:04d}"
                        token_set.update({
                            raw_num,
                            padded,
                            f"lc-{raw_num}",
                            f"lc-{padded}",
                            f"lc{raw_num}",
                            f"lc{padded}"
                        })
                except ValueError:
                    pass

        # Evaluate candidate keywords
        for kw in keywords:
            if not kw:
                continue
            kw_clean = kw.strip().lower()
            if not kw_clean:
                continue

            # CJK characters matching
            if re.search(r'[\u4e00-\u9fff]', kw_clean):
                if kw_clean in raw_text:
                    return True
                continue

            # Split keyword on hyphens, underscores, and whitespace
            kw_words = [w for w in re.split(r"[-_\s]+", kw_clean) if w]
            if not kw_words:
                continue

            if len(kw_words) == 1:
                # Single word token: exact membership check in token_set
                if kw_words[0] in token_set or kw_clean in token_set:
                    return True
            else:
                # Multi-word phrase or hyphenated token
                hyphenated_kw = "-".join(kw_words)
                if hyphenated_kw in token_set or kw_clean in token_set:
                    return True
                k_len = len(kw_words)
                for i in range(word_seq_len - k_len + 1):
                    if word_sequence[i:i + k_len] == kw_words:
                        return True

        return False

    def to_topology_summary(self) -> Dict[str, Any]:
        """Returns a normalized problem projection dictionary for the topology graph."""
        return {
            "key": self.key,
            "lc_num": self.lc_num,
            "title": self.title,
            "short": self.short,
            "diff": self.diff or "Medium",
            "category": self.category_display
        }


    @classmethod
    def create_problem(
        cls,
        key: str,
        category: str,
        category_display: str,
        title: str,
        short: str,
        slug: str,
        cn_title: str,
        en_title: str,
        tags: str,
        lc_num: str,
        path: str,
        diff: str = "Medium",
        notes: str = "",
        code: str = "",
        py_file: str = "",
        md_file: str = ""
    ) -> "DocumentEntity":
        """Constructs a problem entity and automatically computes its encapsulated search blob."""
        search_blob = build_search_blob(
            [slug, tags, title, en_title, cn_title, lc_num, diff, key, path],
            f"{notes}\n{code}"
        )
        return cls(
            key=key,
            category=category,
            category_display=category_display,
            title=title,
            short=short,
            slug=slug,
            cn_title=cn_title,
            en_title=en_title,
            tags=tags,
            lc_num=lc_num,
            search_blob=search_blob,
            path=path,
            type="problem",
            notes=notes,
            code=code,
            diff=diff,
            py_file=py_file,
            md_file=md_file
        )

@dataclass
class BuildResult:
    output_path: Path
    total_entities: int
    total_phases: int = 0
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
        # 1. Match LeetCode 4-digit problem number in stem symmetrically anchored at start
        match_lc = re.search(r'^(?:\d{2}-)?(?:lc-)?(\d{4})(?:-|$)', stem)
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
                match_meta_lc = re.search(r'(?:\*\*LeetCode ID\*\*:\s*|#\s*)LC\s*(\d+)', md_content, re.IGNORECASE) if md_content else None
                if match_meta_lc and int(match_meta_lc.group(1)) > 0:
                    num_int = int(match_meta_lc.group(1))
                    lc_num = f"LC {num_int}"
                else:
                    lc_num = ""
                raw_slug = re.sub(r'^\d{2}-', '', stem)

        # 2. Extract Chinese Title from Markdown H1 header (# LC ... | 中文标题)
        cn_title = ""
        if md_content:
            match_cn = re.search(r'# .*?\|\s*([^\r\n]+)', md_content)
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
