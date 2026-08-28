import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
UPDATE_INDEX_PATH = REPO_ROOT / "update_index.py"
TEMPLATE_PATH = REPO_ROOT / "templates" / "station_template.html"

def extract_and_refactor_template():
    source = UPDATE_INDEX_PATH.read_text(encoding="utf-8")
    
    # Extract html_template between `html_template = f"""` and `output_path = BASE_DIR / "index.html"`
    match = re.search(r'html_template = f"""(.*?)"""\s+output_path = BASE_DIR / "index.html"', source, re.DOTALL)
    if not match:
        raise ValueError("Could not extract html_template from update_index.py")
    
    template = match.group(1)
    
    # Replace double curly braces {{ and }} back to single { and } except for {items_json} and {roadmap_json}
    # Since in python f-string {{ is escaped {, we need to unescape them
    # But preserve {items_json} and {roadmap_json} placeholders!
    
    # First protect {items_json} and {roadmap_json}
    template = template.replace("{items_json}", "__PLACEHOLDER_ITEMS_JSON__")
    template = template.replace("{roadmap_json}", "__PLACEHOLDER_ROADMAP_JSON__")
    
    # Unescape {{ -> { and }} -> }
    template = template.replace("{{", "{").replace("}}", "}")
    
    # Restore placeholders
    template = template.replace("__PLACEHOLDER_ITEMS_JSON__", "{items_json}")
    template = template.replace("__PLACEHOLDER_ROADMAP_JSON__", "{roadmap_json}")
    
    # 1. Update viewMode default to 'dual'
    template = template.replace('let viewMode = "notes";', 'let viewMode = "dual";')
    
    # 2. Add LaTeX delimiter protection
    latex_protection_func = """
    function renderProtectedMarkdown(markdownText) {
      if (!markdownText) return "";
      const mathBlocks = [];
      
      // 1. Protect block math $$...$$
      let text = markdownText.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (match, formula) => {
        const token = `@@MATH_BLOCK_${mathBlocks.length}@@`;
        mathBlocks.push({ token, formula, display: true });
        return token;
      });
      
      // 2. Protect inline math $...$
      text = text.replace(/\\$([^$\\n]+?)\\$/g, (match, formula) => {
        const token = `@@MATH_INLINE_${mathBlocks.length}@@`;
        mathBlocks.push({ token, formula, display: false });
        return token;
      });
      
      // 3. Parse Markdown
      let html = marked.parse(text);
      
      // 4. Restore math expressions
      mathBlocks.forEach(({ token, formula, display }) => {
        const rawMath = display ? `$$${formula}$$` : `$${formula}$`;
        html = html.split(token).join(rawMath);
      });
      
      return html;
    }
    """
    
    # Replace the direct marked.parse in switchItem
    old_switch_notes = """      const notesViewer = document.getElementById("notesViewer");
      if (item.notes) {
        notesViewer.innerHTML = marked.parse(item.notes);
        notesViewer.querySelectorAll("pre code").forEach(block => {
          hljs.highlightElement(block);
        });
        renderMathInElement(notesViewer, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\\\(", right: "\\\\)", display: false},
            {left: "\\\\[", right: "\\\\]", display: true}
          ],
          throwOnError: false
        });
      } else {
        notesViewer.innerHTML = `<p style="color: var(--text-muted);">No documentation notes found for this problem.</p>`;
      }"""

    new_switch_notes = """      const notesViewer = document.getElementById("notesViewer");
      if (item.notes && item.notes.trim().length > 0) {
        notesViewer.innerHTML = renderProtectedMarkdown(item.notes);
        notesViewer.querySelectorAll("pre code").forEach(block => {
          hljs.highlightElement(block);
        });
        renderMathInElement(notesViewer, {
          delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\\\(", right: "\\\\)", display: false},
            {left: "\\\\[", right: "\\\\]", display: true}
          ],
          throwOnError: false
        });
      } else if (item.code) {
        notesViewer.innerHTML = `
          <div style="padding: 24px; text-align: center; color: var(--text-muted);">
            <div style="font-size: 16px; font-weight: 600; color: var(--text-bright); margin-bottom: 8px;">Python Solution Code Ready</div>
            <p style="font-size: 13px; max-width: 480px; margin: 0 auto 16px;">This problem is tracked with verified Python code in the left pane.</p>
            <button onclick="setViewMode('code')" style="background: var(--card-bg); border: 1px solid var(--border-color); color: var(--text-bright); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 500;">
              Expand Code Fullscreen
            </button>
          </div>
        `;
      } else {
        notesViewer.innerHTML = `<p style="color: var(--text-muted); padding: 16px;">No documentation notes or code found for this problem.</p>`;
      }"""

    template = template.replace(old_switch_notes, new_switch_notes)
    
    # Inject renderProtectedMarkdown before switchItem
    template = template.replace("function switchItem(key, rerenderSearch = true) {", latex_protection_func + "\n    function switchItem(key, rerenderSearch = true) {")
    
    TEMPLATE_PATH.write_text(template, encoding="utf-8")
    print(f"Generated {TEMPLATE_PATH} ({len(template.splitlines())} lines)")

if __name__ == "__main__":
    extract_and_refactor_template()
