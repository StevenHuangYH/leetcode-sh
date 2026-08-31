import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TEMPLATE_PATH = REPO_ROOT / "templates" / "station_template.html"

def fix():
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    
    # 1. Fix setMainMode recursion
    old_set_main_mode = """    function setMainMode(mode) {
      mainMode = mode;
      localStorage.setItem("mainMode", mode);

      const btnRoadmap = document.getElementById("btnModeRoadmap");
      const btnWorkspace = document.getElementById("btnModeWorkspace");
      const roadmapView = document.getElementById("roadmap-view");
      const workspaceView = document.getElementById("workspace");
      const viewSwitcher = document.getElementById("viewSwitcher");
      const copyBtn = document.getElementById("copyBtn");
      const breadcrumb = document.getElementById("itemBreadcrumb");

      if (mode === "roadmap") {
        btnRoadmap.classList.add("active");
        btnWorkspace.classList.remove("active");
        roadmapView.classList.add("active");
        workspaceView.classList.add("hidden-view");
        viewSwitcher.style.display = "none";
        copyBtn.style.display = "none";
        breadcrumb.innerHTML = `
          <span class="breadcrumb-folder">Curriculum</span>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-file">Algorithm Master Roadmap</span>
        `;
        if (history.replaceState) {
          history.replaceState(null, null, "#roadmap");
        }
      } else {
        btnRoadmap.classList.remove("active");
        btnWorkspace.classList.add("active");
        roadmapView.classList.remove("active");
        workspaceView.classList.remove("hidden-view");
        viewSwitcher.style.display = "inline-flex";
        copyBtn.style.display = items[currentKey]?.code ? "inline-flex" : "none";
        switchItem(currentKey, false);
      }
    }"""

    new_set_main_mode = """    function setMainMode(mode, triggerSwitch = true) {
      mainMode = mode;
      localStorage.setItem("mainMode", mode);

      const btnRoadmap = document.getElementById("btnModeRoadmap");
      const btnWorkspace = document.getElementById("btnModeWorkspace");
      const roadmapView = document.getElementById("roadmap-view");
      const workspaceView = document.getElementById("workspace");
      const viewSwitcher = document.getElementById("viewSwitcher");
      const copyBtn = document.getElementById("copyBtn");
      const breadcrumb = document.getElementById("itemBreadcrumb");

      if (mode === "roadmap") {
        if (btnRoadmap) btnRoadmap.classList.add("active");
        if (btnWorkspace) btnWorkspace.classList.remove("active");
        if (roadmapView) roadmapView.classList.add("active");
        if (workspaceView) workspaceView.classList.add("hidden-view");
        if (viewSwitcher) viewSwitcher.style.display = "none";
        if (copyBtn) copyBtn.style.display = "none";
        if (breadcrumb) {
          breadcrumb.innerHTML = `
            <span class="breadcrumb-folder">Curriculum</span>
            <span class="breadcrumb-sep">/</span>
            <span class="breadcrumb-file">Algorithm Master Roadmap</span>
          `;
        }
        if (history.replaceState) {
          history.replaceState(null, null, "#roadmap");
        }
      } else {
        if (btnRoadmap) btnRoadmap.classList.remove("active");
        if (btnWorkspace) btnWorkspace.classList.add("active");
        if (roadmapView) roadmapView.classList.remove("active");
        if (workspaceView) workspaceView.classList.remove("hidden-view");
        if (viewSwitcher) viewSwitcher.style.display = "inline-flex";
        if (copyBtn) copyBtn.style.display = items[currentKey]?.code ? "inline-flex" : "none";
        if (triggerSwitch) {
          switchItem(currentKey, false);
        }
      }
    }"""

    if old_set_main_mode in text:
        text = text.replace(old_set_main_mode, new_set_main_mode)
    else:
        # Replace function signature and switchItem call
        text = re.sub(
            r'function setMainMode\(mode\)\s*\{',
            r'function setMainMode(mode, triggerSwitch = true) {',
            text
        )
        text = text.replace('switchItem(currentKey, false);', 'if (triggerSwitch) { switchItem(currentKey, false); }')

    # 2. Fix switchItem call to setMainMode
    text = text.replace('setMainMode("workspace");', 'setMainMode("workspace", false);')

    # 3. Add defensive try-catch in switchItem
    old_switch = """      const notesViewer = document.getElementById("notesViewer");
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

    robust_switch = """      const notesViewer = document.getElementById("notesViewer");
      if (item.notes && item.notes.trim().length > 0) {
        try {
          if (typeof renderProtectedMarkdown === "function") {
            notesViewer.innerHTML = renderProtectedMarkdown(item.notes);
          } else if (typeof marked !== "undefined" && marked.parse) {
            notesViewer.innerHTML = marked.parse(item.notes);
          } else {
            notesViewer.innerHTML = `<pre style="white-space: pre-wrap; font-family: inherit;">${item.notes}</pre>`;
          }
        } catch (err) {
          console.error("Markdown parse error:", err);
          notesViewer.innerHTML = `<pre style="white-space: pre-wrap; font-family: inherit;">${item.notes}</pre>`;
        }

        try {
          if (typeof hljs !== "undefined") {
            notesViewer.querySelectorAll("pre code").forEach(block => {
              hljs.highlightElement(block);
            });
          }
        } catch (e) {
          console.warn("hljs error:", e);
        }

        try {
          if (typeof renderMathInElement === "function") {
            renderMathInElement(notesViewer, {
              delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false},
                {left: "\\\\(", right: "\\\\)", display: false},
                {left: "\\\\[", right: "\\\\]", display: true}
              ],
              throwOnError: false
            });
          }
        } catch (e) {
          console.warn("KaTeX error:", e);
        }
      } else if (item.code) {
        notesViewer.innerHTML = `
          <div style="padding: 28px; text-align: center; color: var(--text-muted);">
            <div style="font-size: 15px; font-weight: 600; color: var(--text-bright); margin-bottom: 8px;">Python Solution Code Available</div>
            <p style="font-size: 13px; max-width: 460px; margin: 0 auto 16px;">This problem is tracked with verified Python code in the left pane.</p>
            <button onclick="setViewMode('code')" style="background: var(--card-bg); border: 1px solid var(--border-color); color: var(--text-bright); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: 500;">
              Expand Code Fullscreen
            </button>
          </div>
        `;
      } else {
        notesViewer.innerHTML = `<p style="color: var(--text-muted); padding: 16px;">No documentation notes or code found for this problem.</p>`;
      }"""

    if old_switch in text:
        text = text.replace(old_switch, robust_switch)
    else:
        # Replace if existing variant
        text = re.sub(r'const notesViewer = document\.getElementById\("notesViewer"\);.*?(?=const copyBtn =)', robust_switch + "\n\n      ", text, flags=re.DOTALL)

    TEMPLATE_PATH.write_text(text, encoding="utf-8")
    print("Fixed station_template.html")

if __name__ == "__main__":
    fix()
