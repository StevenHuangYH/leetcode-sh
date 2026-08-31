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
    compile_study_station,
)

from scripts.validator import audit_notes_directory

BASE_DIR = Path(__file__).parent.resolve()

def build_index_html(output_path: Path = None, use_cache: bool = True) -> Path:
    """Compiles the single-page index.html file."""
    result = compile_study_station(BASE_DIR, output_path, use_cache=use_cache)
    if not result.success:
        print(f"❌ [Error] Failed to build study station: {result.error_message}", file=sys.stderr)
        sys.exit(1)
    cache_msg = " [Cached]" if use_cache else " [Clean Rebuild]"
    print(f"✨ [Success] Built {result.output_path.name} ({result.total_entities} problem entities & curriculum tracks){cache_msg}.")
    return result.output_path

def watch_mode():
    """Watches tracks, ROADMAP.md, README.md, and templates/src/ for changes and auto-rebuilds."""
    import time
    print("👀 [Watch Mode] Monitoring tracks and templates/src/ for changes... (Ctrl+C to stop)")
    watch_dirs = [
        BASE_DIR / "top-100",
        BASE_DIR / "daily-practice",
        BASE_DIR / "luffy",
        BASE_DIR / "templates" / "src",
    ]
    watch_files = [
        BASE_DIR / "README.md",
    ]

    def get_snapshot() -> dict:
        snapshot = {}
        for d in watch_dirs:
            if d.exists():
                for p in d.rglob("*"):
                    if p.is_file() and not p.name.startswith("."):
                        try:
                            snapshot[str(p)] = p.stat().st_mtime
                        except OSError:
                            pass
        for f in watch_files:
            if f.exists():
                try:
                    snapshot[str(f)] = f.stat().st_mtime
                except OSError:
                    pass
        return snapshot

    last_snapshot = get_snapshot()
    try:
        while True:
            time.sleep(0.5)
            curr = get_snapshot()
            if curr != last_snapshot:
                last_snapshot = curr
                print("\n🔄 [Change Detected] Rebuilding index.html...")
                build_index_html(use_cache=True)
    except KeyboardInterrupt:
        print("\n👋 [Watch Mode] Stopped.")

def run_lint_check(strict: bool = False) -> bool:
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
        return True
    else:
        print(f"⚠️  [Notice] {total_invalid}/{total_audited} notes have structural anomalies.")
        if strict:
            print("❌ [Strict Failure] Lint errors detected under strict mode.", file=sys.stderr)
            sys.exit(1)
        return False

def main():
    parser = argparse.ArgumentParser(description="Auto-update index.html for LeetCode workspace.")
    parser.add_argument("--open", action="store_true", help="Build and open index.html in browser")
    parser.add_argument("--lint", action="store_true", help="Audit companion notes 7-section structure")
    parser.add_argument("--strict", action="store_true", help="Fail with non-zero exit code if lint errors are detected")
    parser.add_argument("--watch", action="store_true", help="Continuously watch workspace and rebuild on change")
    parser.add_argument("--clean", "--force", action="store_true", dest="clean", help="Force full rebuild bypassing manifest cache")
    args = parser.parse_args()

    if args.lint:
        run_lint_check(strict=args.strict)

    build_index_html(use_cache=not args.clean)

    if args.watch:
        watch_mode()

    if args.open:
        index_file = BASE_DIR / "index.html"
        try:
            import webbrowser
            webbrowser.open(index_file.as_uri())
        except Exception:
            cmd_exe = Path("/mnt/c/WINDOWS/System32/cmd.exe")
            if cmd_exe.exists():
                subprocess.run([str(cmd_exe), "/c", "start", "", str(index_file)])

if __name__ == "__main__":
    main()
