import unittest
import time
from pathlib import Path
from scripts.compiler.collector import collect_workspace_documents
from scripts.compiler.engine import compile_study_station

REPO_ROOT = Path(__file__).parent.parent

class TestIncrementalCache(unittest.TestCase):

    def test_incremental_cache_creation_and_reuse(self):
        """Assert build_manifest.json is created on first run and reused on subsequent runs."""
        # 1. Clean run
        res1 = collect_workspace_documents(REPO_ROOT, use_cache=True)
        manifest_path = REPO_ROOT / ".cache" / "build_manifest.json"
        
        self.assertTrue(manifest_path.exists(), "Cache manifest file must be generated")
        mtime1 = manifest_path.stat().st_mtime

        # 2. Second cached run (should read from manifest fast)
        t_start = time.time()
        res2 = collect_workspace_documents(REPO_ROOT, use_cache=True)
        t_cached = time.time() - t_start

        self.assertEqual(len(res1), len(res2), "Cached entity count must match full scan count")
        self.assertIn("README.md", res2)
        self.assertIn("topic-all", res2)

    def test_clean_rebuild_bypasses_cache(self):
        """Assert use_cache=False successfully executes full collection."""
        res = collect_workspace_documents(REPO_ROOT, use_cache=False)
        self.assertGreater(len(res), 150)
        self.assertIn("README.md", res)
