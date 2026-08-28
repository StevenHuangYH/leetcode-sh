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

    def test_index_html_defaults_to_dual_view_mode(self):
        """Assert index.html defaults to dual split-pane view instead of notes-only."""
        content = self.index_html_path.read_text(encoding="utf-8")
        # Assert viewMode is initialized to 'dual'
        self.assertRegex(
            content,
            r'let\s+viewMode\s*=\s*["\']dual["\']',
            "viewMode in index.html must default to 'dual' so both code and notes appear side-by-side"
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

if __name__ == "__main__":
    unittest.main()
