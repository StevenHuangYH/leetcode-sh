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

if __name__ == "__main__":
    unittest.main()
