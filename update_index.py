#!/usr/bin/env python3
"""
update_index.py — Thin CLI entry point for LeetCode Study Station Compiler.

Backed by deep modules in scripts.compiler and scripts.validator.
"""

import sys
import argparse
import subprocess
from pathlib import Path

# Deep module imports
from scripts.compiler import (
    DocumentEntity,
    BuildResult,
    collect_workspace_documents,
    parse_curriculum_topics,
    parse_roadmap_data,
    compile_study_station,
)
from scripts.validator import audit_notes_directory

BASE_DIR = Path(__file__).parent.resolve()
TEMPLATE_PATH = BASE_DIR / "templates" / "station_template.html"

def build_index_html(output_path: Path = None, use_cache: bool = True) -> Path:
    """Compiles the single-page index.html file."""
    result = compile_study_station(BASE_DIR, output_path, use_cache=use_cache)
    if not result.success:
        print(f"❌ [Error] Failed to build study station: {result.error_message}", file=sys.stderr)
        sys.exit(1)
    cache_msg = " [Cached]" if use_cache else " [Clean Rebuild]"
    print(f"✨ [Success] Built {result.output_path.name} ({result.total_entities} problem entities & curriculum tracks){cache_msg}.")
    return result.output_path

def run_lint_check():
    """Audits all companion markdown notes across tracks."""
    tracks = ["top-100", "daily-practice", "luffy"]
    total_audited = 0
    total_invalid = 0

    print("🔍 Auditing companion note active recall structures...")
    for track in tracks:
        track_dir = BASE_DIR / track
        if not track_dir.exists():
            continue
        results = audit_notes_directory(track_dir)
        for name, res in results.items():
            total_audited += 1
            if not res.is_valid:
                total_invalid += 1
                print(f"  ⚠️  [{track}] {name}: {', '.join(res.errors)}")

    if total_invalid == 0:
        print(f"✅ [Pass] All {total_audited} companion notes adhere to the standard 7-section format.")
    else:
        print(f"⚠️  [Notice] {total_invalid}/{total_audited} notes have structural anomalies.")

def main():
    parser = argparse.ArgumentParser(description="Auto-update index.html for LeetCode workspace.")
    parser.add_argument("--open", action="store_true", help="Build and open index.html in browser")
    parser.add_argument("--lint", action="store_true", help="Audit companion notes 7-section structure")
    parser.add_argument("--watch", action="store_true", help="Continuously watch workspace and rebuild on change")
    parser.add_argument("--clean", "--force", action="store_true", dest="clean", help="Force full rebuild bypassing manifest cache")
    args = parser.parse_args()

    if args.lint:
        run_lint_check()

    build_index_html(use_cache=not args.clean)

    if args.open:
        cmd_exe = Path("/mnt/c/WINDOWS/System32/cmd.exe")
        if cmd_exe.exists():
            subprocess.run([str(cmd_exe), "/c", "start", "", "C:\\Users\\steve\\iCloudDrive\\desktop\\leetcode-sh\\index.html"])

if __name__ == "__main__":
    main()
