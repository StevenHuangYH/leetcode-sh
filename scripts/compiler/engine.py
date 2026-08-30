import json
from pathlib import Path
from typing import Optional, Dict, Any

from .entities import BuildResult, read_file
from .collector import collect_workspace_documents
from .parser import parse_roadmap_data
from .bundler import TemplateBundler

class StudyStationCompiler:
    """Deep engine module for compiling the leetcode-sh study station SPA."""

    def __init__(self, repo_root: Optional[Path] = None):
        if repo_root is None:
            self.repo_root = Path(__file__).parent.parent.parent.resolve()
        else:
            self.repo_root = Path(repo_root).resolve()

    def compile(self, output_path: Optional[Path] = None) -> BuildResult:
        """Executes the end-to-end compilation pipeline."""
        try:
            if output_path is None:
                output_path = self.repo_root / "index.html"
            else:
                output_path = Path(output_path).resolve()

            # 1. Collect all documents
            all_items = collect_workspace_documents(self.repo_root)

            # 2. Parse roadmap topology
            roadmap_data = parse_roadmap_data(base_dir=self.repo_root)

            # 3. Bundle template assets in-memory
            bundler = TemplateBundler(self.repo_root / "templates")
            template = bundler.bundle()

            if not template:
                return BuildResult(
                    output_path=output_path,
                    total_entities=len(all_items),
                    total_phases=len(roadmap_data),
                    success=False,
                    error_message="Template content was empty."
                )

            # 4. Inject payload into template
            compact_items_json = json.dumps(all_items, separators=(',', ':'), ensure_ascii=False)
            compact_roadmap_json = json.dumps(roadmap_data, separators=(',', ':'), ensure_ascii=False)

            html_content = template.replace(
                "{items_json}", compact_items_json
            ).replace(
                "{roadmap_json}", compact_roadmap_json
            )

            # 5. Write index.html artifact
            output_path.write_text(html_content, encoding="utf-8")

            # 6. Keep station_template.html in sync for backward compatibility
            fallback_template = self.repo_root / "templates" / "station_template.html"
            if fallback_template.exists():
                fallback_template.write_text(template, encoding="utf-8")

            return BuildResult(
                output_path=output_path,
                total_entities=len(all_items),
                total_phases=len(roadmap_data),
                success=True
            )
        except Exception as e:
            return BuildResult(
                output_path=output_path or self.repo_root / "index.html",
                total_entities=0,
                total_phases=0,
                success=False,
                error_message=str(e)
            )

def compile_study_station(repo_root: Optional[Path] = None, output_path: Optional[Path] = None) -> BuildResult:
    """Convenience functional interface for compiling the study station SPA."""
    compiler = StudyStationCompiler(repo_root)
    return compiler.compile(output_path)
