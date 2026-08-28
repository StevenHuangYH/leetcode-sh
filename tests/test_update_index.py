import unittest
from update_index import collect_workspace_documents

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

if __name__ == "__main__":
    unittest.main()
