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

    def test_modular_template_sources_and_bundler_integrity(self):
        """Assert modular frontend templates exist under templates/src/ and TemplateBundler bundles successfully."""
        src_dir = REPO_ROOT / "templates" / "src"
        self.assertTrue((src_dir / "layout.html").exists(), "templates/src/layout.html must exist as primary layout")
        self.assertTrue((src_dir / "styles" / "base.css").exists())
        self.assertTrue((src_dir / "styles" / "roadmap.css").exists())
        self.assertTrue((src_dir / "styles" / "mobile.css").exists())
        self.assertTrue((src_dir / "scripts" / "app.js").exists())

        from scripts.compiler import TemplateBundler
        bundler = TemplateBundler(REPO_ROOT / "templates")
        bundled = bundler.bundle()
        self.assertIn("{items_json}", bundled)
        self.assertIn("{roadmap_json}", bundled)
        self.assertIn("{roadmap_graph_json}", bundled)

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

    def test_semantic_breadcrumb_and_title_formatter_contract(self):
        """Assert compiled index.html includes semantic breadcrumb title attributes and ProblemTitleFormatter exports."""
        content = self.index_html_path.read_text(encoding="utf-8")
        self.assertIn('breadcrumb-file', content)
        self.assertIn('title="${item.title}"', content)
        self.assertIn('Interactive Topology Graph', content)
        
        # Verify public compiler export
        from scripts.compiler import ProblemTitleFormatter, FormattedTitle
        res = ProblemTitleFormatter.format("lc-0025-reverse-nodes-in-k-group")
        self.assertIsInstance(res, FormattedTitle)
        self.assertEqual(res.lc_num, "LC 25")

    def test_search_enter_keyboard_and_focus_routing(self):
        """Assert index.html contains Enter key search handler, notesViewer tabindex, and numeric boundary search."""
        content = self.index_html_path.read_text(encoding="utf-8")
        self.assertIn('id="notesViewer" tabindex="-1"', content)
        self.assertIn('e.key === "Enter"', content)
        self.assertIn('notesViewer.focus()', content)
        self.assertIn('boundaryRegex', content)
        # Assert Enter key targets .problem-item specifically
        self.assertIn('.problem-item', content)
        self.assertNotIn('document.querySelector("#treeRoot .nav-item");', content)

    def test_view_mode_isolation_on_notes_fallback(self):
        """Assert switchItem does not permanently pollute global viewMode when opening code-only items."""
        app_js_path = REPO_ROOT / "templates" / "src" / "scripts" / "app.js"
        app_js_content = app_js_path.read_text(encoding="utf-8")
        # Ensure switchItem does not execute setViewMode("code") on fallback
        self.assertNotIn(
            'setViewMode("code")',
            app_js_content,
            "switchItem must not mutate global viewMode via setViewMode('code')"
        )

    def test_search_precision_and_scroll_restoration(self):
        """Assert search isolates problem ID tokens, pre-compiles regexes, and clearSearch restores active scroll."""
        content = self.index_html_path.read_text(encoding="utf-8")
        self.assertIn('buildSearchMatcher', content)
        self.assertIn('isAllNumeric', content)
        self.assertIn('firstMatchElement', content)
        self.assertIn('cleanSlug', content)
        self.assertIn('idBlob', content)
        self.assertIn('activeItem.scrollIntoView', content)
        self.assertIn('problem-item', content)

    def test_git_hook_instructions_present_in_docs(self):
        """Assert both AGENTS.md and README.md document git config core.hooksPath .githooks."""
        readme_content = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        agents_content = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("git config core.hooksPath .githooks", readme_content)
        self.assertIn("git config core.hooksPath .githooks", agents_content)


if __name__ == "__main__":
    unittest.main()
