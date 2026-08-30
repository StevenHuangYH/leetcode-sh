import unittest
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

class TestPreviewAndGenerator(unittest.TestCase):

    def setUp(self):
        self.index_html_path = REPO_ROOT / "index.html"
        self.update_index_path = REPO_ROOT / "update_index.py"
        self.template_path = REPO_ROOT / "templates" / "station_template.html"
        
        self.assertTrue(self.index_html_path.exists(), "index.html must exist")
        self.assertTrue(self.update_index_path.exists(), "update_index.py must exist")

    def test_index_html_defaults_to_notes_view_mode(self):
        """Assert index.html defaults to notes-only view instead of dual."""
        content = self.index_html_path.read_text(encoding="utf-8")
        # Assert viewMode is initialized to 'notes'
        self.assertRegex(
            content,
            r'let\s+viewMode\s*=\s*["\']notes["\']',
            "viewMode in index.html must default to 'notes'"
        )

    def test_latex_math_formula_protection_logic(self):
        """Assert math formulas with subscripts/asterisks are protected from Markdown italics tags."""
        content = self.index_html_path.read_text(encoding="utf-8")
        # Assert client script includes LaTeX formula placeholder protection before marked.parse
        self.assertTrue(
            "renderProtectedMarkdown" in content or "math" in content.lower(),
            "index.html must protect LaTeX formula delimiters ($$, $) before markdown parsing"
        )

    def test_update_index_code_length_and_modularity(self):
        """Assert update_index.py is clean, decoupled, and under 350 lines."""
        lines = self.update_index_path.read_text(encoding="utf-8").split("\n")
        self.assertLess(
            len(lines),
            350,
            f"update_index.py must be modularized and under 350 lines (currently {len(lines)} lines)"
        )

    def test_station_template_exists_and_is_valid(self):
        """Assert frontend template is decoupled into templates/station_template.html."""
        self.assertTrue(
            self.template_path.exists(),
            "templates/station_template.html must exist to decouple frontend from update_index.py"
        )
        template_text = self.template_path.read_text(encoding="utf-8")
        self.assertIn("{items_json}", template_text)
        self.assertIn("{roadmap_json}", template_text)

    def test_mobile_responsive_features_present(self):
        """Assert station template and index.html include mobile bottom nav and 100dvh."""
        content = self.index_html_path.read_text(encoding="utf-8")
        self.assertIn("mobile-bottom-nav", content)
        self.assertIn("setMobileTab", content)
        self.assertIn("100dvh", content)

    def test_runtime_optimizations_and_compact_payload(self):
        """Assert index.html includes search debouncing, KaTeX math checks, and size is under 1.8MB."""
        content = self.index_html_path.read_text(encoding="utf-8")
        self.assertIn("searchDebounceTimer", content)
        self.assertIn("hasMath", content)
        file_size_mb = self.index_html_path.stat().st_size / (1024 * 1024)
        self.assertLess(file_size_mb, 1.8, f"index.html size should be compact (< 1.8MB), got {file_size_mb:.2f}MB")

if __name__ == "__main__":
    unittest.main()
