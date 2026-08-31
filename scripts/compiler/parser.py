import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

from .entities import (
    DocumentEntity,
    RoadmapPhase,
    RoadmapTopic,
    RoadmapProblem,
    normalize_slug,
    build_search_blob,
    read_file
)


@dataclass
class TopicConfig:
    """Configuration mapping for curriculum index topics in README.md."""
    key: str
    title: str
    short: str
    pattern: Optional[str] = None


def parse_curriculum_topics(readme_text: str) -> dict:
    """Extracts curriculum topic document items from README.md Section 5."""
    topic_configs = [
        TopicConfig("topic-all", "Problem Index: Complete Catalog", "All 11 Topics Combined", None),
        TopicConfig("topic-01-arrays-sliding-window", "1. Arrays, Strings & Sliding Window", "1. Arrays & Sliding Window", r"### 1\.\s+Arrays"),
        TopicConfig("topic-02-binary-search", "2. Binary Search", "2. Binary Search", r"### 2\.\s+Binary Search"),
        TopicConfig("topic-03-prefix-sum", "3. Prefix Sum & Difference Arrays", "3. Prefix Sum & Difference", r"### 3\.\s+Prefix Sum"),
        TopicConfig("topic-04-intervals", "4. Intervals & In-Place Hashing", "4. Intervals & In-Place Hash", r"### 4\.\s+Intervals"),
        TopicConfig("topic-05-linked-lists", "5. Linked Lists", "5. Linked Lists", r"### 5\.\s+Linked Lists"),
        TopicConfig("topic-06-stacks-queues", "6. Stacks & Queues", "6. Stacks & Queues", r"### 6\.\s+Stacks"),
        TopicConfig("topic-07-trees-bst", "7. Trees & Binary Search Trees (BST)", "7. Trees & BST", r"### 7\.\s+Trees"),
        TopicConfig("topic-08-backtracking", "8. Backtracking & Combinatorics", "8. Backtracking", r"### 8\.\s+Backtracking"),
        TopicConfig("topic-09-graphs", "9. Graph Algorithms", "9. Graph Algorithms", r"### 9\.\s+Graph"),
        TopicConfig("topic-10-dp-math", "10. Dynamic Programming & Math / Game Theory", "10. DP & Game Theory", r"### 10\.\s+Dynamic Programming"),
        TopicConfig("topic-11-oop", "11. OOP & Foundations", "11. OOP & Foundations", r"### 11\.\s+(?:Object-Oriented|OOP)"),
    ]
    
    sec5_match = re.search(r'(## (?:📚 )?Topic-Wise Curriculum & Problem Index.*?)(\n## (?:🖥️ )?Interactive Web Viewer|\n## (?:🚀 )?How to Run|\Z)', readme_text, re.DOTALL)
    sec5_text = sec5_match.group(1) if sec5_match else readme_text

    topic_docs = {}
    for cfg in topic_configs:
        key, title, short, pattern = cfg.key, cfg.title, cfg.short, cfg.pattern
        if key == "topic-all":
            topic_content = f"# Problem Index: Complete Topic-Wise Catalog\n\n{sec5_text}"
        else:
            match = re.search(r'(' + pattern + r'.*?)(?=\n### \d+|\n---|\n## |\Z)', readme_text, re.DOTALL)
            topic_content = f"# Problem Index — {title}\n\n{match.group(1).strip()}" if match else f"# Problem Index — {title}\n\nNo content parsed."

        slug = normalize_slug(title)
        topic_docs[key] = asdict(DocumentEntity(
            key=key, category="Curriculum", category_display="Curriculum", title=title, short=short, slug=slug,
            cn_title="", tags="topic curriculum problem index", lc_num="",
            search_blob=build_search_blob([title, short, slug, "problem index topic curriculum"], topic_content),
            path=f"problem-index/{key}", type="doc", notes=topic_content, diff="All"
        ))
    return topic_docs


def parse_roadmap_data(roadmap_text: str = "", base_dir: Optional[Path] = None) -> list:
    """Dynamically parses phases, topics, and problem links from ROADMAP.md."""
    if not roadmap_text:
        if base_dir is None:
            base_dir = Path(__file__).parent.parent.parent.resolve()
        roadmap_text = read_file(base_dir / "ROADMAP.md")
    if not roadmap_text:
        return []
    
    phases = []
    phase_blocks = re.findall(r'## Phase (\d+):\s*([^\n]+)\n+(.*?)(?=\n## Phase \d+|\n---|\Z)', roadmap_text, re.DOTALL)
    
    for phase_num_str, phase_title, block in phase_blocks:
        phase_num = int(phase_num_str)
        topic_blocks = re.findall(r'### Topic (\d+):\s*([^\n]+)\n+(.*?)(?=\n### Topic \d+|\Z)', block, re.DOTALL)
        topics = []
        
        for topic_num_str, topic_title, topic_body in topic_blocks:
            formula_match = re.search(r'┌─+┐\n│\s*([^\n]+)\n├─+┤\n(.*?)\n└─+┘', topic_body, re.DOTALL)
            formula_summary = formula_match.group(1).strip() if formula_match else f"Topic {topic_num_str} Core Patterns"
            
            problems = []
            for row in re.findall(r'\|\s*\*\*LC\s*(\d+)\*\*\s*\|\s*([^\|]+)\|\s*(Easy|Medium|Hard)\s*\|\s*([^\|]+)\|\s*([^\|]+)\|', topic_body):
                lc_num, name_full, diff, category_name, link_cell = row
                cn_match = re.search(r'\(([\u4e00-\u9fa5A-Za-z0-9\s]+)\)', name_full)
                cn_name = cn_match.group(1) if cn_match else ""
                clean_name = re.sub(r'\(.*?\)', '', name_full).strip()
                
                key_match = re.search(r'\(([^)]+\.py)\)', link_cell)
                key = key_match.group(1) if key_match else f"luffy/{int(lc_num):02d}-lc-{int(lc_num):04d}.py"
                
                problems.append({
                    "num": int(lc_num), "name": clean_name, "cn": cn_name, "diff": diff.capitalize(), "key": key
                })
            
            topics.append({
                "id": f"topic-{topic_num_str}",
                "title": topic_title.split("(")[0].strip(),
                "subtitle": topic_title.split("(")[1].replace(")", "").strip() if "(" in topic_title else topic_title,
                "icon": "layers",
                "formula": formula_summary,
                "problems": problems
            })
            
        phases.append({
            "phase": phase_num,
            "phase_name": f"Phase {phase_num}: {phase_title.strip()}",
            "phase_badge": f"PHASE {phase_num:02d}",
            "phase_desc": f"Master Phase {phase_num} core algorithmic models and problem patterns.",
            "topics": topics
        })
    return phases
