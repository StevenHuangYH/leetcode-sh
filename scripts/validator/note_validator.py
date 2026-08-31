import re
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    is_valid: bool
    missing_sections: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    note_path: Optional[str] = None

    def summary(self) -> str:
        if self.is_valid:
            return f"VALID: {self.note_path or 'Note'}"
        err_str = "; ".join(self.errors)
        return f"INVALID ({len(self.errors)} error(s)): {self.note_path or 'Note'} -> {err_str}"


def get_canonical_topology_keywords() -> List[str]:

    """Dynamically extracts all canonical topology taxonomy keywords and node IDs from the registry."""
    keywords = set()
    try:
        from scripts.compiler.topology_definitions import CANONICAL_TOPOLOGY_NODES
        for node in CANONICAL_TOPOLOGY_NODES:
            keywords.add(node.id.lower())
            for kw in node.keywords:
                if len(kw) > 1:
                    keywords.add(kw.lower())
    except Exception:
        pass
    if not keywords:
        keywords = {
            "array", "linked-list", "linked", "diff", "difference", "matrix", "prefix",
            "stack", "queue", "hash", "design", "pointer", "sliding-window", "binary-search",
            "search", "random", "recursion", "recursive", "tree", "level-order", "bfs",
            "shortest-path", "dijkstra", "dfs", "backtracking", "divide", "conquer",
            "dp", "dynamic", "math", "greedy", "bst", "heap", "trie", "graph", "bit",
            "palindrome", "fast-slow", "sentinel", "string", "combinatorics"
        }
    return sorted(keywords)

class NoteStructureValidator:
    """Validator enforcing the 7 Active Recall components mandated by AGENTS.md."""


    def validate(self, markdown_content: str, note_path: Optional[str] = None) -> ValidationResult:
        """Validates a markdown note's adherence to the 7-component active recall standard."""
        errors: List[str] = []
        missing_sections: List[str] = []

        if not markdown_content or not markdown_content.strip():
            return ValidationResult(
                is_valid=False,
                missing_sections=["All components (empty note)"],
                errors=["Markdown content is empty."],
                note_path=note_path
            )

        # 1. Component 1: Header & File Links (Title + Metadata or Explicit Section)
        has_title = bool(re.search(r'#\s+.*?(?:LeetCode|LC|\d+)', markdown_content, re.IGNORECASE))
        has_meta = bool(
            re.search(r'\*\*(?:Difficulty|Tags|Solution File|Corresponding Python File|LeetCode ID)', markdown_content, re.IGNORECASE) or
            re.search(r'##\s*\d*\.?\s*Header\s*&', markdown_content, re.IGNORECASE) or
            re.search(r'(?:Problem Link|Companion Source|Solution File)', markdown_content, re.IGNORECASE)
        )
        if not (has_title and has_meta):
            missing_sections.append("Component 1: Header & File Links")
            errors.append("Missing required Component 1: Header & File Links metadata.")
        else:
            # Verify topology taxonomy keyword alignment
            topology_keywords = get_canonical_topology_keywords()
            tag_match = re.search(r'(?:Tags|标签)\s*[:：*]+\s*([^\n\r]+)', markdown_content, re.IGNORECASE)
            if tag_match:
                tag_text = tag_match.group(1).lower()
                has_valid_topo_keyword = any(kw in tag_text for kw in topology_keywords)
                if not has_valid_topo_keyword:
                    errors.append("Component 1 Tags must include at least one canonical topology taxonomy keyword.")

        # 2. Component 2: Problem Statement & Constraints (Bilingual [EN] and [CN])
        has_problem_stmt = bool(re.search(r'##\s*\d*\.?\s*Problem\s*Statement', markdown_content, re.IGNORECASE))
        if not has_problem_stmt:
            missing_sections.append("Component 2: Problem Statement & Constraints")
            errors.append("Missing required Problem Statement section.")
        else:
            has_en = bool(re.search(r'\[EN\]', markdown_content))
            has_cn = bool(re.search(r'\[CN\]', markdown_content))
            if not (has_en and has_cn):
                errors.append("Problem Statement is missing bilingual [EN] or [CN] tags.")

        # 3. Component 3: Core Idea, Mental Model & Pattern Lineage
        s3_match = re.search(r'##\s*\d*\.?\s*(?:Core\s*Idea|Problem\s*Blueprint|Mental\s*Model|Pattern\s*Lineage)[^\n]*\n(.*?)(?=\n##\s*\d*\.|\Z)', markdown_content, re.DOTALL | re.IGNORECASE)
        if not s3_match:
            missing_sections.append("Component 3: Core Idea & Mental Model")
            errors.append("Missing required Component 3: Core Idea, Mental Model & Pattern Lineage.")
        else:
            s3_body = s3_match.group(1)
            has_lineage_or_model = bool(
                re.search(r'(?:Topology\s*Node|Pattern\s*Lineage|思维演化|演化树|演化图|决策树|状态转移|```)', s3_body, re.IGNORECASE)
            )
            if not has_lineage_or_model:
                errors.append("Component 3 is missing Topology Anchor or Pattern Lineage ASCII diagram.")




        # 4. Component 4: Step-by-Step Code Walkthrough
        has_walkthrough = bool(re.search(r'##\s*\d*\.?\s*Step-by-Step\s*Code\s*Walkthrough', markdown_content, re.IGNORECASE))
        if not has_walkthrough:
            missing_sections.append("Component 4: Step-by-Step Code Walkthrough")
            errors.append("Missing required Component 4: Step-by-Step Code Walkthrough.")

        # 5. Component 5: Interview Simulation
        has_interview = bool(re.search(r'##\s*\d*\.?\s*Interview\s*Simulation', markdown_content, re.IGNORECASE))
        if not has_interview:
            missing_sections.append("Component 5: Interview Simulation")
            errors.append("Missing required Component 5: Interview Simulation.")

        # 6. Component 6: The Error Log & Complete Dry-Run
        has_error_log = bool(re.search(r'##\s*\d*\.?\s*(?:The\s*Error\s*Log|Error\s*Log|Anti-Patterns)', markdown_content, re.IGNORECASE))
        if not has_error_log:
            missing_sections.append("Component 6: The Error Log & Complete Dry-Run")
            errors.append("Missing required Component 6: The Error Log & Complete Dry-Run.")
        else:
            has_error_table = bool(re.search(
                r'\|[^|\n]*(?:Buggy Pattern|Anti-Patterns?|Traps|典型错误|常见陷阱)[^|\n]*\|[^|\n]*(?:Symptom|Fail Case|触发场景|典型报错|错误现象)[^|\n]*\|[^|\n]*(?:Root Cause|根因|根本原因)[^|\n]*\|[^|\n]*(?:Defensive Fix|Invariant|防御性修复)[^|\n]*',
                markdown_content,
                re.IGNORECASE
            ))
            if not has_error_table:
                errors.append("Component 6 is missing standard 4-column Error Log table schema.")

        # 7. Component 7: Complexity Analysis
        has_complexity = bool(re.search(r'##\s*\d*\.?\s*Complexity\s*Analysis', markdown_content, re.IGNORECASE))
        if not has_complexity:
            missing_sections.append("Component 7: Complexity Analysis")
            errors.append("Missing required Component 7: Complexity Analysis.")
        else:
            has_complexity_table = bool(re.search(
                r'(?:Time\s*Complexity|时间复杂度).*?(?:Space\s*Complexity|空间复杂度)',
                markdown_content,
                re.DOTALL | re.IGNORECASE
            ))
            if not has_complexity_table:
                errors.append("Component 7 is missing Time / Space Complexity analysis table.")

        return ValidationResult(
            is_valid=len(errors) == 0,
            missing_sections=missing_sections,
            errors=errors,
            note_path=note_path
        )

def validate_note(markdown_content: str, note_path: Optional[str] = None) -> ValidationResult:
    """Convenience function for validating note structure."""
    validator = NoteStructureValidator()
    return validator.validate(markdown_content, note_path)

def audit_notes_directory(dir_path: Path) -> Dict[str, ValidationResult]:
    """Audits all companion markdown notes within a directory."""
    validator = NoteStructureValidator()
    results: Dict[str, ValidationResult] = {}
    for md_file in sorted(dir_path.glob("*.md")):
        if re.search(r'(?:^\d{2}-)?lc-', md_file.name):
            content = md_file.read_text(encoding="utf-8", errors="ignore")
            results[md_file.name] = validator.validate(content, str(md_file))
    return results

