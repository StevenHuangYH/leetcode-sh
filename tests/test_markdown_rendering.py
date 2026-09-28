import subprocess
import unittest
from pathlib import Path

from test_update_index import _get_node_binary


class TestMarkdownRendering(unittest.TestCase):
    def run_rendering_check(self, assertions):
        node = _get_node_binary()
        if not node:
            self.skipTest("Node.js is required for renderer behavior checks")
        source = (Path(__file__).parent.parent / "templates/src/scripts/app.js").read_text(encoding="utf-8")
        rendering = source[source.index("function renderProtectedMarkdown"):source.index("const DOM_RENDER_DELAY_MS")]
        harness = r"""
const assert = require('node:assert/strict');
const elements = new Map();
const document = {
  getElementById(id) {
    if (!elements.has(id)) elements.set(id, {
      innerHTML: '', textContent: '', dataset: {}, scrollTop: 0,
      classList: { toggle() {} }, querySelectorAll() { return []; }
    });
    return elements.get(id);
  },
  querySelectorAll() { return []; }
};
const window = { innerWidth: 1200 };
const items = { fixture: { title: 'Rendering fixture', notes: '', code: '' } };
const treeStructure = [];
const collapsedFolders = {};
let currentKey = '';
function setMainMode() {}
const markdownInputs = [];
const marked = { parse(text) { markdownInputs.push(text); return text; } };
const mathCalls = [];
function renderMathInElement(element, options) {
  mathCalls.push({ html: element.innerHTML, ...options });
}
function openNotes(notes) {
  items.fixture.notes = notes;
  switchItem('fixture', false, false);
}
"""
        result = subprocess.run(
            [node, "-e", harness + rendering + assertions],
            capture_output=True, text=True, encoding="utf-8", timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_plain_language_markers_do_not_trigger_math_rendering(self):
        self.run_rendering_check(r"""
openNotes('### [EN] English Description\n### [CN] 中文描述\n(ASCII Pattern Lineage Map)');
assert.equal(mathCalls.length, 0, 'Plain brackets and parentheses are prose, not formulas');
""")

    def test_math_notes_keep_plain_brackets_out_of_the_delimiter_set(self):
        self.run_rendering_check(r"""
openNotes('### [EN] English Description\nRuntime: $O(n)$ (linear time).');
assert.equal(mathCalls.length, 1);
assert.deepEqual(mathCalls[0].delimiters.map(d => [d.left, d.right]), [
  ['$$', '$$'], ['$', '$'], ['\\(', '\\)'], ['\\[', '\\]']
]);
assert.ok(mathCalls[0].html.includes('[EN]'));
""")

    def test_backslash_formulas_are_protected_before_markdown_parsing(self):
        self.run_rendering_check(r"""
openNotes(String.raw`Inline \(a_*b\) and display \[c_*d\].`);
assert.equal(mathCalls.length, 1);
assert.ok(!markdownInputs[0].includes('a_*b'), 'Inline formula reached Markdown unprotected');
assert.ok(!markdownInputs[0].includes('c_*d'), 'Display formula reached Markdown unprotected');
assert.ok(mathCalls[0].html.includes('a_*b'), 'Inline formula was lost');
assert.ok(mathCalls[0].html.includes('c_*d'), 'Display formula was lost');
""")
