import os
import re
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import asdict

from .entities import (
    DocumentEntity,
    normalize_slug,
    build_search_blob,
    read_file
)
from .parser import parse_curriculum_topics


def collect_workspace_documents(base_dir: Optional[Path] = None) -> Dict[str, Any]:
    if base_dir is None:
        base_dir = Path(__file__).parent.parent.parent.resolve()
    """Scans repository folders and aggregates structured problem entities."""
    readme_text = read_file(base_dir / "README.md")
    
    topic_docs = parse_curriculum_topics(readme_text)
    overview_docs = {
        "README.md": asdict(DocumentEntity(
            key="README.md", category="Overview", title="LeetCode Self-Practices Overview (README)",
            short="README.md", slug="readme overview", cn_title="项目总览", tags="readme overview index",
            lc_num="", search_blob=build_search_blob(["README.md", "overview", "项目总览"], readme_text),
            path="README.md", type="doc", notes=readme_text, diff="All"
        ))
    }

    problems = {}
    tracks = [("top-100", "Top 100 Liked Track"), ("daily-practice", "Daily Practice Track"), ("luffy", "Luffy Curriculum (01-42)")]

    for dir_name, cat_title in tracks:
        track_dir = base_dir / dir_name
        if not track_dir.exists():
            continue

        files = sorted(os.listdir(track_dir))
        stem_groups = {}
        for f in files:
            if f.startswith("__") or f.endswith(".pyc") or f == "file_topics.txt":
                continue
            stem = f[:-3] if f.endswith(".py") or f.endswith(".md") else f
            if stem not in stem_groups:
                stem_groups[stem] = {"py": None, "md": None}
            if f.endswith(".py"):
                stem_groups[stem]["py"] = f
            elif f.endswith(".md"):
                stem_groups[stem]["md"] = f

        for stem, pair in stem_groups.items():
            py_file, md_file = pair["py"], pair["md"]
            py_content = read_file(track_dir / py_file) if py_file else ""
            md_content = read_file(track_dir / md_file) if md_file else ""

            m_num = re.search(r'(?:lc-)?(\d{4})', stem)
            lc_num = f"LC {int(m_num.group(1))}" if m_num else ""
            title = f"{lc_num} {stem}" if lc_num else stem.replace("-", " ").title()
            
            cn_match = re.search(r'# .*?\| ([\u4e00-\u9fa5A-Za-z0-9\s\(\)]+)', md_content) if md_content else None
            cn_title = cn_match.group(1).strip() if cn_match else ""
            
            diff_match = re.search(r'\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)', md_content, re.IGNORECASE) if md_content else None
            diff = diff_match.group(1).capitalize() if diff_match else "Medium"
            
            clean_slug = normalize_slug(f"{stem} {cn_title}")
            search_blob = build_search_blob([stem, title, cn_title, lc_num, diff, dir_name], f"{md_content}\n{py_content}")
            primary_key = f"{dir_name}/{py_file if py_file else md_file}"
            
            problems[primary_key] = asdict(DocumentEntity(
                key=primary_key, category=cat_title, title=title, short=py_file if py_file else md_file,
                slug=clean_slug, cn_title=cn_title, tags=f"{dir_name} {diff.lower()}", lc_num=lc_num,
                search_blob=search_blob, path=f"{dir_name}/{stem}", type="problem", notes=md_content,
                code=py_content, diff=diff, py_file=f"{dir_name}/{py_file}" if py_file else "",
                md_file=f"{dir_name}/{md_file}" if md_file else ""
            ))

    return {**overview_docs, **topic_docs, **problems}
