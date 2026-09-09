import unittest
from pathlib import Path
from update_index import collect_workspace_documents
from scripts.compiler.entities import format_problem_title

REPO_ROOT = Path(__file__).parent.parent

class TestUpdateIndexParser(unittest.TestCase):
    def test_all_11_topics_curriculum_are_parsed_without_empty_content(self):
        documents = collect_workspace_documents()
        
        expected_topic_keys = [
            "topic-all",
            "topic-01-arrays-sliding-window",
            "topic-02-binary-search",
            "topic-03-prefix-sum",
            "topic-04-intervals",
            "topic-05-linked-lists",
            "topic-06-stacks-queues",
            "topic-07-trees-bst",
            "topic-08-backtracking",
            "topic-09-graphs",
            "topic-10-dp-math",
            "topic-11-oop",
        ]
        
        for key in expected_topic_keys:
            with self.subTest(topic_key=key):
                self.assertIn(key, documents, f"Key {key} missing from documents")
                doc = documents[key]
                self.assertNotIn(
                    "No content parsed.",
                    doc["notes"],
                    f"Topic '{key}' failed to parse content from README.md"
                )
                self.assertTrue(len(doc["notes"].strip()) > 50, f"Topic '{key}' content is too short")
                self.assertEqual(doc["category"], "Curriculum")

    def test_format_problem_title_extraction(self):
        # 1. Standard problem with markdown
        lc_num, en, cn, full = format_problem_title(
            "lc-0153-find-minimum-in-rotated-sorted-array",
            "# LC 0153: Find Minimum in Rotated Sorted Array | 寻找旋转排序数组中的最小值\n\n**Difficulty:** Medium"
        )
        self.assertEqual(lc_num, "LC 153")
        self.assertEqual(en, "Find Minimum In Rotated Sorted Array")
        self.assertEqual(cn, "寻找旋转排序数组中的最小值")
        self.assertEqual(full, "LC 153 · Find Minimum In Rotated Sorted Array (寻找旋转排序数组中的最小值)")

        # 2. Luffy curriculum problem with batch prefix
        lc_num, en, cn, full = format_problem_title(
            "01-lc-2235-add-two-integers",
            "# LC 2235: Add Two Integers | 两整数相加\n\n**Difficulty:** Easy"
        )
        self.assertEqual(lc_num, "LC 2235")
        self.assertEqual(en, "Add Two Integers")
        self.assertEqual(cn, "两整数相加")
        self.assertEqual(full, "LC 2235 · Add Two Integers (两整数相加)")

        # 3. Non-LC tutorial script without markdown
        lc_num, en, cn, full = format_problem_title("10-oop-pre-main-practice", "")
        self.assertEqual(lc_num, "")
        self.assertEqual(en, "OOP Pre Main Practice")
        self.assertEqual(cn, "")
        self.assertEqual(full, "OOP Pre Main Practice")

        # 4. Roman numerals and acronym preservation
        lc_num, en, cn, full = format_problem_title("09-lc-0059-spiral-matrix-ii-alt", "")
        self.assertEqual(lc_num, "LC 59")
        self.assertEqual(en, "Spiral Matrix II Alt")
        self.assertEqual(full, "LC 59 · Spiral Matrix II Alt")

        # 5. FormattedTitle dataclass attributes
        from scripts.compiler.entities import ProblemTitleFormatter, FormattedTitle
        formatted = ProblemTitleFormatter.format("lc-0153-find-minimum-in-rotated-sorted-array")
        self.assertIsInstance(formatted, FormattedTitle)
        self.assertEqual(formatted.lc_num, "LC 153")
        self.assertEqual(formatted.en_title, "Find Minimum In Rotated Sorted Array")

    def test_overview_document_semantic_title(self):
        documents = collect_workspace_documents()
        self.assertIn("README.md", documents)
        readme_doc = documents["README.md"]
        self.assertEqual(readme_doc["title"], "LeetCode Self-Practices Overview")
        self.assertEqual(readme_doc["category"], "Overview")

    def test_navigation_interceptor_bundled(self):
        from scripts.compiler.bundler import TemplateBundler
        bundler = TemplateBundler()
        bundled_html = bundler.bundle(minify=False)
        self.assertIn("function initRoadmapGraph", bundled_html)
        self.assertIn("function openWorkspaceForNode", bundled_html)
        self.assertIn("function showNodePopover", bundled_html)
        self.assertIn("function enforceNotesView", bundled_html)
        self.assertIn("const DOM_RENDER_DELAY_MS = 60;", bundled_html)
        self.assertIn("function resolveEntityReference", bundled_html)
        self.assertIn("function findHeadingElement", bundled_html)
        self.assertIn("function initLinkInterceptor", bundled_html)
        self.assertIn("initLinkInterceptor();", bundled_html)

    def test_entity_resolution_contracts(self):
        documents = collect_workspace_documents()
        
        # 1. Exact path resolution
        self.assertIn("problems/luffy/02-lc-0001-two-sum.py", documents)
        self.assertIn("problems/top-100/lc-0015-3sum.py", documents)
        self.assertIn("problems/daily-practice/lc-0025-reverse-nodes-in-k-group.py", documents)

        # 2. Extension swap contract (md file companion lookup)
        top15 = documents.get("problems/top-100/lc-0015-3sum.py")
        self.assertIsNotNone(top15)
        self.assertTrue(top15.get("md_file", "").endswith("lc-0015-3sum.md"))

        # 3. Topic and problem-index keys
        self.assertIn("topic-01-arrays-sliding-window", documents)
        self.assertIn("topic-all", documents)

        # 4. LC number mapping integrity
        lc15_entity = next((v for v in documents.values() if v.get("lc_num") == "LC 15"), None)
        self.assertIsNotNone(lc15_entity)
        self.assertEqual(lc15_entity["key"], "problems/top-100/lc-0015-3sum.py")

        lc1_luffy = documents.get("problems/luffy/02-lc-0001-two-sum.py")
        lc1_top = documents.get("problems/top-100/lc-0001-two-sum.py")
        self.assertIsNotNone(lc1_luffy)
        self.assertIsNotNone(lc1_top)
        self.assertEqual(lc1_luffy["lc_num"], "LC 1")
        self.assertEqual(lc1_top["lc_num"], "LC 1")

    def test_compiler_domain_entities_and_pairing_structures(self):
        """Assert DocumentEntity, FilePairing, and ProblemCollector domain models."""
        from scripts.compiler.collector import ProblemCollector, FilePairing
        from scripts.compiler.entities import DocumentEntity
        from scripts.compiler.parser import TopicConfig

        pairing = FilePairing(stem="lc-0077-combinations", py_file="lc-0077-combinations.py", md_file="lc-0077-combinations.md")
        self.assertEqual(pairing.stem, "lc-0077-combinations")

        entity = DocumentEntity.create_problem(
            key="problems/daily-practice/lc-0077-combinations.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 77 · Combinations (组合)",
            short="LC 77 Combinations",
            slug="lc-0077-combinations combinations",
            cn_title="组合",
            en_title="Combinations",
            tags="problems/daily-practice medium",
            lc_num="LC 77",
            path="problems/daily-practice/lc-0077-combinations",
            diff="Medium"
        )
        self.assertIn("combinations", entity.search_blob)
        self.assertIn("77", entity.search_blob)

        topic_cfg = TopicConfig("topic-08-backtracking", "8. Backtracking", "8. Backtracking", r"### 8\.")
        self.assertEqual(topic_cfg.key, "topic-08-backtracking")

    def test_format_markdown_link_helper(self):
        """Assert format_markdown_link helper produces consistent, properly formatted markdown links."""
        from scripts.sync_readme import format_markdown_link
        self.assertEqual(
            format_markdown_link("problems/top-100/lc-0022-generate-parentheses.py"),
            "[`problems/top-100/lc-0022-generate-parentheses.py`](problems/top-100/lc-0022-generate-parentheses.py)"
        )
        self.assertEqual(
            format_markdown_link("problems/daily-practice/lc-0077-combinations.md"),
            "[`problems/daily-practice/lc-0077-combinations.md`](problems/daily-practice/lc-0077-combinations.md)"
        )

    def test_sync_readme_dynamic_difficulty_metrics(self):
        """Assert sync_readme does not contain hardcoded difficulty counts and computes them dynamically."""
        from pathlib import Path
        sync_readme_path = Path(__file__).parent.parent / "scripts" / "sync_readme.py"
        content = sync_readme_path.read_text(encoding="utf-8")
        # Ensure hardcoded difficulty table constants and replacement tuples are removed
        self.assertNotIn("| **Easy** | 31 | ~31% | 31 |", content)
        self.assertNotIn("| **Medium** | 62 | ~62% | 134 |", content)
        self.assertNotIn("| **Hard** | 7 | ~7% | 9 |", content)
        self.assertNotIn("total_problems = 174", content)
        self.assertNotIn("LUFFY_TRACK_REPLACEMENTS", content)
        self.assertNotIn("EXTRA_PROBLEM_MAPPINGS", content)
        self.assertIn("format_markdown_link", content)
        self.assertIn("sync_multi_track_solutions", content)
        self.assertIn("build_problem_files_index(collector_items)", content)

    def test_multi_track_solution_and_note_indexing(self):
        """Assert build_problem_files_index aggregates both .py and .md files for multi-track problems."""
        from scripts.sync_readme import build_problem_files_index
        from scripts.compiler.collector import ProblemCollector
        
        collector_items = ProblemCollector.collect(REPO_ROOT, use_cache=False)
        file_map = build_problem_files_index(collector_items)
        
        # Verify LC 77 contains both daily-practice py/md and luffy py
        self.assertIn(77, file_map)
        lc_77_links = file_map[77]
        self.assertTrue(any("problems/daily-practice/lc-0077-combinations.py" in l for l in lc_77_links))
        self.assertTrue(any("problems/daily-practice/lc-0077-combinations.md" in l for l in lc_77_links))
        self.assertTrue(any("problems/luffy/31-lc-0077-combinations.py" in l for l in lc_77_links))

        # Verify LC 131 contains both daily-practice py/md and luffy py
        self.assertIn(131, file_map)
        lc_131_links = file_map[131]
        self.assertTrue(any("problems/daily-practice/lc-0131-palindrome-partitioning.py" in l for l in lc_131_links))
        self.assertTrue(any("problems/daily-practice/lc-0131-palindrome-partitioning.md" in l for l in lc_131_links))
        self.assertTrue(any("problems/luffy/36-lc-0131-palindrome-partitioning.py" in l for l in lc_131_links))

        # Verify all 10 core multi-track problems exist in file_map with >1 link
        multi_track_ids = [77, 78, 131, 167, 3, 209, 59, 303, 20, 98]
        for prob_id in multi_track_ids:
            with self.subTest(prob_id=prob_id):
                self.assertIn(prob_id, file_map)
                self.assertGreater(len(file_map[prob_id]), 1, f"Problem {prob_id} should have multiple track links")

    def test_section_5_multi_track_readme_preservation(self):
        """Assert Section 5 in README.md retains both .py and .md companion links for multi-track problems."""
        from scripts.sync_readme import update_readme
        update_readme()
        
        readme_text = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        
        # Verify Section 5 rows include both code and companion notes across tracks
        self.assertIn("[`problems/daily-practice/lc-0077-combinations.md`](problems/daily-practice/lc-0077-combinations.md)", readme_text)
        self.assertIn("[`problems/daily-practice/lc-0131-palindrome-partitioning.md`](problems/daily-practice/lc-0131-palindrome-partitioning.md)", readme_text)
        self.assertIn("[`problems/top-100/lc-0003-longest-substring-without-repeating-characters.md`](problems/top-100/lc-0003-longest-substring-without-repeating-characters.md)", readme_text)
        self.assertIn("[`problems/top-100/lc-0209-minimum-size-subarray-sum.md`](problems/top-100/lc-0209-minimum-size-subarray-sum.md)", readme_text)
        self.assertIn("[`problems/luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py`](problems/luffy/03-lc-0167-two-sum-ii-input-array-is-sorted.py)", readme_text)
        self.assertIn("[`problems/luffy/19-lc-0020-valid-parentheses.py`](problems/luffy/19-lc-0020-valid-parentheses.py)", readme_text)

    def test_pre_commit_quality_gate_contracts(self):
        """Assert .githooks/pre-commit enforces strict linting and unit test execution."""
        hook_path = REPO_ROOT / ".githooks" / "pre-commit"
        self.assertTrue(hook_path.exists(), "Pre-commit hook must exist")
        content = hook_path.read_text(encoding="utf-8")
        self.assertIn("--lint --strict", content, "Pre-commit hook must enforce --strict linting")
        self.assertIn("python3 -m unittest discover tests", content, "Pre-commit hook must run test discovery")
        self.assertIn("python3 update_index.py", content, "Pre-commit hook must compile index.html")

    def test_dead_roadmap_parser_removal(self):
        """Assert obsolete parse_roadmap_data and Roadmap classes are completely removed from compiler pipeline."""
        import scripts.compiler.parser as parser_module
        import scripts.compiler.entities as entities_module
        self.assertFalse(hasattr(parser_module, "parse_roadmap_data"), "parse_roadmap_data should be removed")
        self.assertFalse(hasattr(entities_module, "RoadmapPhase"), "RoadmapPhase should be removed")
        self.assertFalse(hasattr(entities_module, "RoadmapTopic"), "RoadmapTopic should be removed")
        self.assertFalse(hasattr(entities_module, "RoadmapProblem"), "RoadmapProblem should be removed")

    def test_strict_lint_across_entire_repository(self):
        """Assert python3 update_index.py --lint --strict succeeds across the entire repository with 0 errors."""
        from update_index import run_lint_check
        self.assertTrue(run_lint_check(strict=True))

    def test_track_registry_domain_model(self):
        """Assert TrackRegistry encapsulates canonical track paths and client payloads."""
        from scripts.compiler.track_definitions import TrackRegistry, CANONICAL_TRACKS
        
        tracks = TrackRegistry.get_all_tracks()
        self.assertEqual(len(tracks), 3)
        self.assertEqual([t.id for t in tracks], ["top-100", "daily-practice", "luffy"])
        
        paths = TrackRegistry.get_track_paths()
        self.assertEqual(paths, ["problems/top-100", "problems/daily-practice", "problems/luffy"])
        
        tuples = TrackRegistry.get_collector_tuples()
        self.assertEqual(tuples, [
            ("problems/top-100", "Top 100 Liked Track"),
            ("problems/daily-practice", "Daily Practice Track"),
            ("problems/luffy", "Luffy Curriculum (01-42)")
        ])
        
        top100 = TrackRegistry.get_track_by_id("top-100")
        self.assertIsNotNone(top100)
        self.assertEqual(top100.dir_path, "problems/top-100")
        self.assertFalse(hasattr(top100, "legacy_prefix"))
        
        payload = TrackRegistry.to_client_json_payload()
        self.assertEqual(len(payload), 3)
        self.assertEqual(payload[0]["id"], "top-100")
        self.assertEqual(payload[0]["dir_path"], "problems/top-100")
        self.assertEqual(payload[0]["display_label"], "Top 100 Liked")
        self.assertEqual(payload[0]["category_name"], "Top 100 Liked Track")
        self.assertNotIn("legacy_prefix", payload[0])
        self.assertEqual(set(payload[0].keys()), {"id", "dir_path", "display_label", "category_name"})

    def test_study_station_compiler_injects_tracks_payload(self):
        """Assert StudyStationCompiler generates index.html containing valid tracks JSON and no unreplaced placeholders."""
        from scripts.compiler.engine import compile_study_station
        import tempfile
        
        with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            result = compile_study_station(REPO_ROOT, tmp_path, use_cache=True)
            self.assertTrue(result.success)
            html_text = tmp_path.read_text(encoding="utf-8")
            self.assertNotIn("{tracks_json}", html_text)
            self.assertNotIn("{items_json}", html_text)
            self.assertNotIn("{roadmap_graph_json}", html_text)
            self.assertIn('"dir_path":"problems/top-100"', html_text)
            self.assertIn('"dir_path":"problems/daily-practice"', html_text)
            self.assertIn('"dir_path":"problems/luffy"', html_text)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()


if __name__ == "__main__":
    unittest.main()


