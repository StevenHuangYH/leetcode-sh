import os
import re
import json
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from dataclasses import asdict

from .entities import (
    DocumentEntity,
    normalize_slug,
    build_search_blob,
    read_file,
    format_problem_title
)
from .parser import parse_curriculum_topics


MANIFEST_VERSION = "2.1"


def _get_file_stat(file_path: Optional[Path]) -> Tuple[float, int]:
    """Returns (mtime, size) for incremental cache invalidation checks."""
    if file_path and file_path.is_file():
        try:
            stat = file_path.stat()
            return stat.st_mtime, stat.st_size
        except OSError:
            pass
    return 0.0, 0


def collect_workspace_documents(base_dir: Optional[Path] = None, use_cache: bool = True) -> Dict[str, Any]:
    """Scans repository folders and aggregates structured problem entities with incremental manifest caching."""
    if base_dir is None:
        base_dir = Path(__file__).parent.parent.parent.resolve()

    cache_dir = base_dir / ".cache"
    manifest_file = cache_dir / "build_manifest.json"
    cached_manifest = {}

    if use_cache and manifest_file.exists():
        try:
            loaded = json.loads(manifest_file.read_text(encoding="utf-8"))
            if loaded.get("__version__") == MANIFEST_VERSION:
                cached_manifest = loaded
        except Exception:
            cached_manifest = {}

    new_manifest = {"__version__": MANIFEST_VERSION}

    # 1. Overview & Curriculum Docs
    readme_path = base_dir / "README.md"
    readme_stat = _get_file_stat(readme_path)
    readme_cache_key = "__readme__"

    if (
        use_cache
        and readme_cache_key in cached_manifest
        and cached_manifest[readme_cache_key].get("stat") == list(readme_stat)
    ):
        overview_docs = cached_manifest[readme_cache_key].get("overview_docs", {})
        topic_docs = cached_manifest[readme_cache_key].get("topic_docs", {})
        new_manifest[readme_cache_key] = cached_manifest[readme_cache_key]
    else:
        readme_text = read_file(readme_path)
        topic_docs = parse_curriculum_topics(readme_text)
        overview_docs = {
            "README.md": asdict(DocumentEntity(
                key="README.md", category="Overview", title="LeetCode Self-Practices Overview",
                short="README.md", slug="readme overview", cn_title="项目总览", tags="readme overview index",
                lc_num="", search_blob=build_search_blob(["README.md", "overview", "项目总览", "leetcode self practices overview"], readme_text),
                path="README.md", type="doc", notes=readme_text, diff="All"
            ))
        }
        new_manifest[readme_cache_key] = {
            "stat": list(readme_stat),
            "overview_docs": overview_docs,
            "topic_docs": topic_docs
        }

    # 2. Problem Documents across Tracks
    problems = {}
    tracks = [
        ("top-100", "Top 100 Liked Track"),
        ("daily-practice", "Daily Practice Track"),
        ("luffy", "Luffy Curriculum (01-42)")
    ]

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
            py_path = track_dir / py_file if py_file else None
            md_path = track_dir / md_file if md_file else None

            py_stat = _get_file_stat(py_path)
            md_stat = _get_file_stat(md_path)
            primary_key = f"{dir_name}/{py_file if py_file else md_file}"

            # Check cache match
            cached_problem = cached_manifest.get(primary_key)
            if (
                use_cache
                and cached_problem
                and cached_problem.get("py_stat") == list(py_stat)
                and cached_problem.get("md_stat") == list(md_stat)
                and "entity" in cached_problem
            ):
                entity_dict = cached_problem["entity"]
            else:
                py_content = read_file(py_path) if py_path else ""
                md_content = read_file(md_path) if md_path else ""

                lc_num, en_title, cn_title, title = format_problem_title(stem, md_content)

                diff_match = re.search(r'\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)', md_content, re.IGNORECASE) if md_content else None
                diff = diff_match.group(1).capitalize() if diff_match else "Medium"

                short_display = f"{lc_num} {en_title or cn_title}".strip()

                clean_slug = normalize_slug(f"{stem} {en_title} {cn_title}")
                search_blob = build_search_blob([stem, title, en_title, cn_title, lc_num, diff, dir_name], f"{md_content}\n{py_content}")

                entity_dict = asdict(DocumentEntity(
                    key=primary_key, category=cat_title, title=title, short=short_display or (py_file if py_file else md_file),
                    slug=clean_slug, cn_title=cn_title, en_title=en_title, tags=f"{dir_name} {diff.lower()}", lc_num=lc_num,
                    search_blob=search_blob, path=f"{dir_name}/{stem}", type="problem", notes=md_content,
                    code=py_content, diff=diff, py_file=f"{dir_name}/{py_file}" if py_file else "",
                    md_file=f"{dir_name}/{md_file}" if md_file else ""
                ))

            problems[primary_key] = entity_dict
            new_manifest[primary_key] = {
                "py_stat": list(py_stat),
                "md_stat": list(md_stat),
                "entity": entity_dict
            }

    # Save manifest cache
    if use_cache:
        try:
            cache_dir.mkdir(parents=True, exist_ok=True)
            manifest_file.write_text(json.dumps(new_manifest, separators=(',', ':'), ensure_ascii=False), encoding="utf-8")
        except Exception:
            pass

    return {**overview_docs, **topic_docs, **problems}
