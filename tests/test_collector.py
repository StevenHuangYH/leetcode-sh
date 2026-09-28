import tempfile
import unittest
from pathlib import Path

from scripts.compiler.collector import collect_workspace_documents
from scripts.compiler.track_definitions import TrackRegistry


class TestCollectorFileDiscovery(unittest.TestCase):
    def test_unrelated_files_do_not_change_catalog(self):
        for track in TrackRegistry.get_all_tracks():
            with self.subTest(track=track.id), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                track_dir = root / track.dir_path
                track_dir.mkdir(parents=True)
                (track_dir / "lc-0001-two-sum.py").write_text("pass\n", encoding="utf-8")
                (track_dir / "lc-0001-two-sum.md").write_text("# Two Sum\n", encoding="utf-8")
                (track_dir / "lc-0002-add-two-numbers.py").write_text("pass\n", encoding="utf-8")
                (track_dir / "lc-0003-longest-substring.md").write_text("# Notes\n", encoding="utf-8")
                expected = collect_workspace_documents(root, use_cache=True)
                problem_keys = {key for key in expected if key.startswith(track.dir_path + "/")}
                self.assertEqual(len(problem_keys), 3)

                for name in (".DS_Store", "image.png", "notes.txt", "backup.py.bak"):
                    with self.subTest(file=name):
                        (track_dir / name).write_bytes(b"unrelated file")
                        for use_cache in (False, True):
                            with self.subTest(use_cache=use_cache):
                                self.assertEqual(
                                    collect_workspace_documents(root, use_cache=use_cache),
                                    expected,
                                    "Non-problem files must not add or overwrite catalog entities",
                                )
                        (track_dir / name).unlink()

    def test_directories_with_problem_extensions_are_ignored(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            track_dir = root / TrackRegistry.get_all_tracks()[0].dir_path
            track_dir.mkdir(parents=True)
            expected = collect_workspace_documents(root, use_cache=True)

            for name in ("lc-0001-two-sum.py", "lc-0002-add-two-numbers.md"):
                (track_dir / name).mkdir()
            for use_cache in (False, True):
                with self.subTest(use_cache=use_cache):
                    self.assertEqual(
                        collect_workspace_documents(root, use_cache=use_cache), expected
                    )
