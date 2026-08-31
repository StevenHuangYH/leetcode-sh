import unittest
from update_index import collect_workspace_documents
from scripts.compiler.entities import format_problem_title

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
        self.assertIn("luffy/02-lc-0001-two-sum.py", documents)
        self.assertIn("top-100/lc-0015-3sum.py", documents)
        self.assertIn("daily-practice/lc-0025-reverse-nodes-in-k-group.py", documents)

        # 2. Extension swap contract (md file companion lookup)
        top15 = documents.get("top-100/lc-0015-3sum.py")
        self.assertIsNotNone(top15)
        self.assertTrue(top15.get("md_file", "").endswith("lc-0015-3sum.md"))

        # 3. Topic and problem-index keys
        self.assertIn("topic-01-arrays-sliding-window", documents)
        self.assertIn("topic-all", documents)

        # 4. LC number mapping integrity
        lc15_entity = next((v for v in documents.values() if v.get("lc_num") == "LC 15"), None)
        self.assertIsNotNone(lc15_entity)
        self.assertEqual(lc15_entity["key"], "top-100/lc-0015-3sum.py")

        lc1_luffy = documents.get("luffy/02-lc-0001-two-sum.py")
        lc1_top = documents.get("top-100/lc-0001-two-sum.py")
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
            key="daily-practice/lc-0077-combinations.py",
            category="Daily Practice Track",
            category_display="Daily Practice",
            title="LC 77 · Combinations (组合)",
            short="LC 77 Combinations",
            slug="lc-0077-combinations combinations",
            cn_title="组合",
            en_title="Combinations",
            tags="daily-practice medium",
            lc_num="LC 77",
            path="daily-practice/lc-0077-combinations",
            diff="Medium"
        )
        self.assertIn("combinations", entity.search_blob)
        self.assertIn("77", entity.search_blob)

        topic_cfg = TopicConfig("topic-08-backtracking", "8. Backtracking", "8. Backtracking", r"### 8\.")
        self.assertEqual(topic_cfg.key, "topic-08-backtracking")

    def test_sync_readme_dynamic_difficulty_metrics(self):
        """Assert sync_readme does not contain hardcoded difficulty counts and computes them dynamically."""
        from pathlib import Path
        sync_readme_path = Path(__file__).parent.parent / "scripts" / "sync_readme.py"
        content = sync_readme_path.read_text(encoding="utf-8")
        # Ensure hardcoded difficulty table constants are removed
        self.assertNotIn("| **Easy** | 31 | ~31% | 31 |", content)
        self.assertNotIn("| **Medium** | 62 | ~62% | 134 |", content)
        self.assertNotIn("| **Hard** | 7 | ~7% | 9 |", content)
        self.assertNotIn("total_problems = 174", content)


if __name__ == "__main__":
    unittest.main()
