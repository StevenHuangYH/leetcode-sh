import functools
import re
from pathlib import Path
from typing import List, Dict, Optional, Any, Set, Tuple
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


def _normalize_token_aliases(text: str) -> Set[str]:
    """Generates normalized aliases (lower-cased, space/hyphen/underscore variants) for a token."""
    cleaned = text.strip().lower()
    if not cleaned:
        return set()
    aliases = {cleaned}
    if "-" in cleaned:
        aliases.add(cleaned.replace("-", " "))
    if "_" in cleaned:
        aliases.add(cleaned.replace("_", " "))
    return aliases


@functools.lru_cache(maxsize=1)
def _get_canonical_topology_data() -> Tuple[List[str], Set[str]]:
    """Cached internal helper to extract both canonical keywords list and entities set in a single traversal."""
    keywords = set()
    entities = set()
    try:
        from scripts.compiler.topology_definitions import CANONICAL_TOPOLOGY_NODES
    except Exception as e:
        raise RuntimeError(f"Failed to load CANONICAL_TOPOLOGY_NODES from scripts.compiler.topology_definitions: {e}") from e

    if not CANONICAL_TOPOLOGY_NODES:
        raise RuntimeError("CANONICAL_TOPOLOGY_NODES registry is empty or missing.")

    for node in CANONICAL_TOPOLOGY_NODES:
        # 1. Node ID (hyphenated and spaced)
        node_id = node.id.strip().lower()
        keywords.add(node_id)
        entities.update(_normalize_token_aliases(node_id))

        # 2. Node Category
        category = getattr(node, "category", None)
        if category:
            entities.update(_normalize_token_aliases(category))

        # 3. Node Label lines
        label = getattr(node, "label", None)
        if label:
            for line in label.splitlines():
                line_clean = line.strip().lower()
                if line_clean:
                    entities.add(line_clean)
                    for part in re.split(r'[/|&]', line_clean):
                        part_clean = part.strip()
                        if len(part_clean) > 1:
                            entities.update(_normalize_token_aliases(part_clean))

        # 4. Canonical Keywords
        node_keywords = getattr(node, "keywords", None)
        if node_keywords:
            for kw in node_keywords:
                kw_clean = kw.strip().lower()
                if len(kw_clean) > 1:
                    keywords.add(kw_clean)
                    entities.update(_normalize_token_aliases(kw_clean))

    return sorted(keywords), entities


def get_canonical_topology_keywords() -> List[str]:
    """Dynamically extracts all canonical topology taxonomy keywords and node IDs from the registry."""
    return _get_canonical_topology_data()[0]


def get_canonical_topology_entities() -> Set[str]:
    """Dynamically extracts all canonical node IDs, categories, group labels, and keywords from the topology registry."""
    return _get_canonical_topology_data()[1]


def validate_non_problem_document(markdown_content: str, doc_path: Optional[str] = None) -> ValidationResult:
    """Validates non-problem markdown documentation files (guides, curriculum overviews) with structural rules."""
    errors: List[str] = []

    if not markdown_content or not markdown_content.strip():
        return ValidationResult(
            is_valid=False,
            missing_sections=["Non-empty document body"],
            errors=["Markdown content is empty."],
            note_path=doc_path,
        )

    # 1. Top-level markdown H1 title (# Title)
    if not re.search(r'^#\s+[^\n\r]+', markdown_content, re.MULTILINE):
        errors.append("Document is missing a top-level H1 markdown title (# Title).")

    # 2. Balanced code block fences
    if markdown_content.count("```") % 2 != 0:
        errors.append("Document contains unclosed code block fences (odd count of ```).")

    # 3. No empty markdown link targets [text]()
    if re.search(r'\[[^\]]+\]\(\s*\)', markdown_content):
        errors.append("Document contains broken empty markdown link targets [text]().")

    # 4. Relative link disk verification when doc_path is provided
    if doc_path:
        doc_file_path = Path(doc_path)
        doc_dir = doc_file_path.parent if doc_file_path.is_file() or doc_file_path.suffix else doc_file_path
        for match in re.finditer(r'!?\[([^\]]+)\]\(([^)]+)\)', markdown_content):
            target = match.group(2).strip()
            if not target or target.startswith("#"):
                continue
            if re.match(r'^(?:https?|ftp|mailto|tel|javascript|data):', target, re.IGNORECASE):
                continue
            # Extract file part before any anchor or whitespace title
            clean_target = target.split()[0].split("#")[0].strip()
            if not clean_target:
                continue
            target_rel_doc = doc_dir / clean_target
            target_rel_cwd = Path(clean_target)
            if not (target_rel_doc.exists() or target_rel_cwd.exists()):
                errors.append(f"Broken relative link target '{clean_target}' (file not found on disk).")

    # 5. Verify overview structure (presence of # Topic or ## Overview or ## 概述 or introductory text)
    has_overview = bool(
        re.search(r'^#\s+.*Topic', markdown_content, re.MULTILINE | re.IGNORECASE) or
        re.search(r'##\s*(?:Overview|概述)', markdown_content, re.IGNORECASE) or
        re.search(r'^[^#\s\n\r][^\n\r]+', markdown_content, re.MULTILINE) or
        len(markdown_content.strip()) > 30
    )
    if not has_overview:
        errors.append("Document is missing overview structure (# Topic, ## Overview, ## 概述, or introductory body).")

    return ValidationResult(
        is_valid=len(errors) == 0,
        missing_sections=[],
        errors=errors,
        note_path=doc_path,
    )


class NoteStructureValidator:
    """Validator enforcing the 7 Active Recall components mandated by AGENTS.md."""

    validate_non_problem_doc = staticmethod(validate_non_problem_document)

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
        s3_matches = list(re.finditer(
            r'##\s*\d*\.?\s*(?:Core\s*Idea|Problem\s*Blueprint|Mental\s*Model|Pattern\s*Lineage)[^\n]*\n(.*?)(?=\n##\s*\d*\.|\n##\s*(?:Step-by-Step|Interview|The\s*Error|Complexity)|\Z)',
            markdown_content,
            re.DOTALL | re.IGNORECASE
        ))

        if not s3_matches:
            missing_sections.append("Component 3: Core Idea & Mental Model")
            errors.append("Missing required Component 3: Core Idea, Mental Model & Pattern Lineage.")
        else:
            s3_body = "\n".join(m.group(1) for m in s3_matches)

            # Check mandatory Topology Node macro anchor
            topo_match = re.search(r'(?:(?:🗺️\s*)?`?\*?\*?Topology\s*Node\*?\*?\s*[:：]\s*)([^\n\r]+)', s3_body, re.IGNORECASE)
            if not topo_match:
                errors.append("Component 3 is missing required 'Topology Node:' macro anchor.")
            else:
                anchor_raw = topo_match.group(1).strip().strip("`*|# ")
                canonical_entities = get_canonical_topology_entities()
                anchor_lower = anchor_raw.lower()
                has_matching_entity = False
                for entity in canonical_entities:
                    pattern = rf'(?<![a-zA-Z0-9]){re.escape(entity)}(?![a-zA-Z0-9])'
                    if re.search(pattern, anchor_lower):
                        has_matching_entity = True
                        break
                if not has_matching_entity:
                    errors.append(
                        f"Component 3 Topology Node macro anchor '{anchor_raw}' does not match any registered canonical node ID, group category, or taxonomy keyword in CANONICAL_TOPOLOGY_NODES."
                    )

            # Check Pattern Lineage ASCII diagram / mental model
            has_lineage_or_model = bool(
                re.search(r'(?:Pattern\s*Lineage|思维演化|演化树|演化图|决策树|状态转移|```)', s3_body, re.IGNORECASE)
            )
            if not has_lineage_or_model:
                errors.append("Component 3 is missing Pattern Lineage ASCII diagram or mental model.")

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
    """Audits all companion markdown notes and documentation files within a directory."""
    validator = NoteStructureValidator()
    results: Dict[str, ValidationResult] = {}
    if not dir_path.exists() or not dir_path.is_dir():
        return results

    for md_file in sorted(dir_path.glob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            results[md_file.name] = ValidationResult(
                is_valid=False,
                errors=["File contains invalid UTF-8 encoding."],
                note_path=str(md_file)
            )
            continue
        except Exception as e:
            results[md_file.name] = ValidationResult(
                is_valid=False,
                errors=[f"Failed to read file: {e}"],
                note_path=str(md_file)
            )
            continue

        if re.search(r'(?:^\d{2}-)?lc-.*\.md$', md_file.name):
            results[md_file.name] = validator.validate(content, str(md_file))
        else:
            results[md_file.name] = validator.validate_non_problem_doc(content, str(md_file))

    return results

