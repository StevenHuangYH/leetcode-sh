import re
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple

from scripts.compiler.track_definitions import TrackRegistry

REPO_ROOT = Path(__file__).parent.parent
TRACKS = TrackRegistry.get_track_paths()

def get_disk_problems(repo_root: Path = REPO_ROOT) -> Dict[str, Set[str]]:
    disk_manifest: Dict[str, Set[str]] = {}
    for track in TRACKS:
        track_dir = repo_root / track
        if not track_dir.exists():
            disk_manifest[track] = set()
            continue
        
        stems = set()
        for file in track_dir.iterdir():
            if file.is_file() and (file.name.endswith(".py") or file.name.endswith(".md")):
                stems.add(file.stem)
        disk_manifest[track] = stems
    return disk_manifest

def get_readme_tracked_problems(repo_root: Path = REPO_ROOT) -> Tuple[Dict[str, Set[str]], List[str]]:
    readme_path = repo_root / "README.md"
    track_paths = TrackRegistry.get_track_paths()
    if not readme_path.exists():
        return {track: set() for track in track_paths}, []
    
    readme_text = readme_path.read_text(encoding="utf-8")
    
    tracked_manifest: Dict[str, Set[str]] = {}
    for track in track_paths:
        pattern = rf"{re.escape(track)}/([a-zA-Z0-9\-]+)\.(?:py|md)"
        tracked_manifest[track] = set(re.findall(pattern, readme_text))
    
    # Extract all relative file links pointing to repository tracks
    tracks_regex = "|".join(re.escape(track) for track in track_paths)
    links = re.findall(rf"\[.*?\]\(((?:{tracks_regex})/[^)]+)\)", readme_text)
    return tracked_manifest, links


class TestTrackingIntegrity(unittest.TestCase):
    def test_all_readme_links_point_to_valid_files(self):
        _, links = get_readme_tracked_problems(REPO_ROOT)
        self.assertTrue(len(links) > 0, "README.md should contain track file links")
        
        broken_links = []
        for rel_link in links:
            # Strip anchors if any
            clean_path = rel_link.split("#")[0]
            target = REPO_ROOT / clean_path
            if not target.exists():
                broken_links.append(rel_link)
        
        self.assertEqual(
            broken_links,
            [],
            f"Found {len(broken_links)} broken link(s) in README.md: {broken_links}"
        )

    def test_audit_manifest_structure(self):
        disk_manifest = get_disk_problems(REPO_ROOT)
        total_problems = sum(len(stems) for stems in disk_manifest.values())
        
        self.assertGreater(total_problems, 100, "Repository should contain > 100 problems")
        top_100 = TrackRegistry.get_track_by_id("top-100")
        daily = TrackRegistry.get_track_by_id("daily-practice")
        luffy = TrackRegistry.get_track_by_id("luffy")
        self.assertIsNotNone(top_100)
        self.assertIsNotNone(daily)
        self.assertIsNotNone(luffy)
        self.assertGreater(len(disk_manifest[top_100.dir_path]), 80, "Top 100 track should have > 80 problems")
        self.assertGreater(len(disk_manifest[daily.dir_path]), 10, "Daily track should have > 10 problems")
        self.assertGreater(len(disk_manifest[luffy.dir_path]), 40, "Luffy track should have > 40 problems")

    def test_all_disk_problems_tracked_in_readme(self):
        disk_manifest = get_disk_problems(REPO_ROOT)
        tracked_manifest, _ = get_readme_tracked_problems(REPO_ROOT)
        
        untracked = {}
        for track in TRACKS:
            diff = disk_manifest[track] - tracked_manifest[track]
            if diff:
                untracked[track] = sorted(list(diff))
        
        self.assertEqual(
            untracked,
            {},
            f"Found untracked problems in README.md:\n" +
            "\n".join(f"  {k}: {len(v)} missing -> {v[:5]}..." for k, v in untracked.items())
        )

if __name__ == "__main__":
    unittest.main()
