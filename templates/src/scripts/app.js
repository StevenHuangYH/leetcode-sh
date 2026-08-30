const items = {items_json};
    const roadmapData = {roadmap_json};

    let mainMode = localStorage.getItem("mainMode") || "roadmap";
    let currentKey = "README.md";
    let viewMode = "dual"; // 'dual', 'notes', 'code'
    let mobileTab = "notes"; // 'notes', 'code'
    let workspaceSplitRatio = parseFloat(localStorage.getItem("workspaceSplitRatio") || "50");
    const collapsedFolders = JSON.parse(localStorage.getItem("treeCollapsedFolders") || "{}");

    // Check initial URL hash
    if (window.location.hash && window.location.hash.length > 1) {
      const hashKey = decodeURIComponent(window.location.hash.substring(1));
      if (hashKey === "roadmap") {
        mainMode = "roadmap";
      } else if (items[hashKey]) {
        currentKey = hashKey;
        mainMode = "workspace";
      }
    }

    // Tree folder structure definitions matching README.md repo structure
    const treeStructure = [
      {
        id: "roadmap-doc",
        name: "ROADMAP.md",
        label: "Master Roadmap",
        isLeaf: true,
        filter: k => k === "ROADMAP.md"
      },
      {
        id: "overview",
        name: "README.md",
        label: "Overview",
        isLeaf: true,
        filter: k => k === "README.md"
      },
      {
        id: "problem-index",
        name: "problem-index/",
        label: "Curriculum Index",
        filter: k => k.startsWith("topic-")
      },
      {
        id: "top-100",
        name: "top-100/",
        label: "Top 100 Liked",
        filter: k => k.startsWith("top-100/")
      },
      {
        id: "daily-practice",
        name: "daily-practice/",
        label: "Daily Practice",
        filter: k => k.startsWith("daily-practice/")
      },
      {
        id: "luffy",
        name: "luffy/",
        label: "Curriculum (01-42)",
        filter: k => k.startsWith("luffy/")
      }
    ];

    function updateProgressBadge() {
      const problemKeys = Object.keys(items).filter(k => items[k].type === "problem");
      document.getElementById("progressStats").innerText = `${problemKeys.length} Problems`;
    }

    function applyWorkspaceSplit(ratio) {
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      if (!leftPane || !rightPane) return;
      if (viewMode === "dual") {
        const clamped = Math.max(15, Math.min(85, ratio));
        leftPane.style.width = `calc(${clamped}% - 2.5px)`;
        leftPane.style.flex = "none";
        rightPane.style.width = `calc(${100 - clamped}% - 2.5px)`;
        rightPane.style.flex = "none";
      }
    }

    function setMobileTab(tab) {
      mobileTab = tab;
      const tabNotes = document.getElementById("mobileTabNotes");
      const tabCode = document.getElementById("mobileTabCode");
      if (tabNotes) tabNotes.classList.toggle("active", tab === "notes");
      if (tabCode) tabCode.classList.toggle("active", tab === "code");

      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      const resizer = document.getElementById("workspace-resizer");

      if (window.innerWidth <= 768) {
        if (resizer) resizer.style.display = "none";
        if (tab === "code") {
          if (leftPane) {
            leftPane.style.display = "flex";
            leftPane.style.width = "100%";
            leftPane.style.flex = "1";
          }
          if (rightPane) rightPane.style.display = "none";
        } else {
          if (leftPane) leftPane.style.display = "none";
          if (rightPane) {
            rightPane.style.display = "flex";
            rightPane.style.width = "100%";
            rightPane.style.flex = "1";
          }
        }
      }
    }

    function setViewMode(mode) {
      viewMode = mode;
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      const resizer = document.getElementById("workspace-resizer");

      document.getElementById("btnDual").classList.toggle("active", mode === "dual");
      document.getElementById("btnNotes").classList.toggle("active", mode === "notes");
      document.getElementById("btnCode").classList.toggle("active", mode === "code");

      if (window.innerWidth <= 768) {
        setMobileTab(mode === "code" ? "code" : "notes");
        return;
      }

      if (mode === "dual") {
        leftPane.style.display = "flex";
        rightPane.style.display = "flex";
        resizer.style.display = "block";
        applyWorkspaceSplit(workspaceSplitRatio);
      } else if (mode === "code") {
        leftPane.style.display = "flex";
        leftPane.style.width = "100%";
        leftPane.style.flex = "1";
        rightPane.style.display = "none";
        resizer.style.display = "none";
      } else { // notes only
        leftPane.style.display = "none";
        rightPane.style.display = "flex";
        rightPane.style.width = "100%";
        rightPane.style.flex = "1";
        resizer.style.display = "none";
      }
    }

    function setMainMode(mode, triggerSwitch = true) {
      mainMode = mode;
      localStorage.setItem("mainMode", mode);

      const btnRoadmap = document.getElementById("btnModeRoadmap");
      const btnWorkspace = document.getElementById("btnModeWorkspace");
      const roadmapView = document.getElementById("roadmap-view");
      const workspaceView = document.getElementById("workspace");
      const viewSwitcher = document.getElementById("viewSwitcher");
      const copyBtn = document.getElementById("copyBtn");
      const breadcrumb = document.getElementById("itemBreadcrumb");
      const mobileNav = document.getElementById("mobileBottomNav");

      if (mode === "roadmap") {
        if (btnRoadmap) btnRoadmap.classList.add("active");
        if (btnWorkspace) btnWorkspace.classList.remove("active");
        if (roadmapView) roadmapView.classList.add("active");
        if (workspaceView) workspaceView.classList.add("hidden-view");
        if (viewSwitcher) viewSwitcher.style.display = "none";
        if (copyBtn) copyBtn.style.display = "none";
        if (mobileNav) mobileNav.classList.add("hidden");
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
        if (viewSwitcher) viewSwitcher.style.display = window.innerWidth <= 768 ? "none" : "inline-flex";
        if (copyBtn) copyBtn.style.display = items[currentKey]?.code ? "inline-flex" : "none";
        if (mobileNav) mobileNav.classList.remove("hidden");
        if (window.innerWidth <= 768) {
          setMobileTab(mobileTab);
        } else {
          setViewMode(viewMode);
        }
        if (triggerSwitch) {
          switchItem(currentKey, false);
        }
      }
    }

    function renderRoadmap(selectedPhase = 'all') {
      const root = document.getElementById("roadmapPhasesRoot");
      if (!root) return;

      const diffColorMap = {
        "Easy": "var(--diff-easy)",
        "Medium": "var(--diff-medium)",
        "Hard": "var(--diff-hard)",
      };

      let html = "";
      roadmapData.forEach(p => {
        if (selectedPhase !== 'all' && p.phase !== parseInt(selectedPhase)) return;

        let totalProblemsInPhase = 0;
        p.topics.forEach(t => totalProblemsInPhase += t.problems.length);

        html += `
          <section class="phase-section" id="phase-sec-${p.phase}">
            <div class="phase-header">
              <div class="phase-title-group">
                <span class="phase-badge-pill">${p.phase_badge}</span>
                <h2 class="phase-title-text">${p.phase_name}</h2>
              </div>
              <span class="topic-card-count">${p.topics.length} 专题 · ${totalProblemsInPhase} 题解</span>
            </div>
            <p class="phase-desc">${p.phase_desc}</p>
            <div class="phase-topics-grid">
        `;

        p.topics.forEach(t => {
          html += `
            <div class="topic-card">
              <div class="topic-card-top">
                <div>
                  <h3 class="topic-card-title">${t.title}</h3>
                  <div class="topic-card-subtitle">${t.subtitle}</div>
                </div>
                <span class="topic-card-count">${t.problems.length} 题</span>
              </div>
              <div class="topic-formula-badge" title="Core Mental Model / Formula">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                <span>${t.formula}</span>
              </div>
              <div class="topic-pills-container">
          `;

          t.problems.forEach(prob => {
            const dotColor = diffColorMap[prob.diff] || "var(--diff-medium)";
            html += `
              <div class="topic-problem-pill" onclick="openProblemFromRoadmap('${prob.key}')" title="${prob.name} (${prob.cn})">
                <span class="pill-diff-dot" style="background-color: ${dotColor};"></span>
                <span>LC ${prob.num} ${prob.cn || prob.name}</span>
              </div>
            `;
          });

          html += `
              </div>
            </div>
          `;
        });

        html += `
            </div>
          </section>
        `;
      });

      root.innerHTML = html;
    }

    function filterRoadmapPhase(phase, btnEl) {
      document.querySelectorAll(".phase-filter-btn").forEach(b => b.classList.remove("active"));
      if (btnEl) btnEl.classList.add("active");
      renderRoadmap(phase);
    }

    function openProblemFromRoadmap(key) {
      setMainMode("workspace", false);
      switchItem(key);
    }

    function getCategoryIcon(catId) {
      switch(catId) {
        case "roadmap-doc":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon><line x1="9" y1="3" x2="9" y2="18"></line><line x1="15" y1="6" x2="15" y2="21"></line></svg>`;
        case "overview":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>`;
        case "problem-index":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>`;
        case "top-100":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>`;
        case "daily-practice":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`;
        case "luffy":
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>`;
        default:
          return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>`;
      }
    }

    function toggleFolder(folderId) {
      collapsedFolders[folderId] = !collapsedFolders[folderId];
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree(document.getElementById("search").value);
    }

    function setAllFoldersCollapsed(collapsed) {
      treeStructure.forEach(folder => {
        if (!folder.isLeaf) {
          collapsedFolders[folder.id] = collapsed;
        }
      });
      localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
      renderTree(document.getElementById("search").value);
    }

    function matchesSearchQuery(item, query) {
      if (!query) return true;
      const clean = query.trim().toLowerCase();
      if (!clean) return true;
      const tokens = clean.split(/\\s+/);
      return tokens.every(token => item.search_blob.includes(token));
    }

    function renderTree(query = "") {
      const root = document.getElementById("treeRoot");
      if (!root) return;

      const isSearching = Boolean(query && query.trim().length > 0);
      let html = "";
      let totalVisible = 0;

      treeStructure.forEach(folder => {
        if (folder.isLeaf) {
          const matchingKey = Object.keys(items).find(k => folder.filter(k));
          if (!matchingKey) return;
          const item = items[matchingKey];
          if (isSearching && !matchesSearchQuery(item, query)) return;

          const isActive = matchingKey === currentKey && mainMode === "workspace";
          const iconSvg = getCategoryIcon(folder.id);

          html += `
            <div class="nav-item root-leaf ${isActive ? 'active' : ''}" data-key="${matchingKey}" onclick="switchItem('${matchingKey}')" title="${item.title}">
              <span class="folder-icon" style="margin-right: 2px;">${iconSvg}</span>
              <span class="tree-title">${folder.name}</span>
            </div>
          `;
          totalVisible++;
          return;
        }

        const folderKeys = Object.keys(items).filter(k => folder.filter(k));
        const matchingKeys = isSearching 
          ? folderKeys.filter(k => matchesSearchQuery(items[k], query))
          : folderKeys;

        if (matchingKeys.length === 0) return;
        totalVisible += matchingKeys.length;

        const isCollapsed = isSearching ? false : Boolean(collapsedFolders[folder.id]);
        const folderIconSvg = getCategoryIcon(folder.id);

        html += `
          <div class="tree-folder ${isCollapsed ? 'collapsed' : ''}" id="folder-${folder.id}">
            <div class="tree-folder-header" onclick="toggleFolder('${folder.id}')">
              <span class="folder-arrow">
                <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </span>
              <span class="folder-icon">${folderIconSvg}</span>
              <span class="folder-name">${folder.label}</span>
              <span class="folder-count">${matchingKeys.length}</span>
            </div>
            <div class="tree-children">
        `;

        matchingKeys.forEach(itemKey => {
          const item = items[itemKey];
          const isActive = itemKey === currentKey && mainMode === "workspace";
          const diffClass = `diff-${item.diff}`;

          let displayTitle = item.title;
          if (item.category.includes("Luffy")) {
            displayTitle = item.title.replace(/^LC \\d+\\s*/, "");
          }

          html += `
            <div class="nav-item ${isActive ? 'active' : ''}" data-key="${itemKey}" onclick="switchItem('${itemKey}')" title="${item.title}">
              <span class="tree-title">${displayTitle}</span>
              <span class="tree-diff-dot ${diffClass}"></span>
            </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      if (totalVisible === 0) {
        html = `
          <div class="tree-no-results">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <span>No matching problems found</span>
          </div>
        `;
      }

      root.innerHTML = html;
    }

    function handleSearch(query) {
      const clearBtn = document.getElementById("searchClear");
      if (query.trim().length > 0) {
        clearBtn.classList.add("visible");
      } else {
        clearBtn.classList.remove("visible");
      }
      renderTree(query);
    }

    function clearSearch() {
      const input = document.getElementById("search");
      input.value = "";
      document.getElementById("searchClear").classList.remove("visible");
      renderTree("");
      input.focus();
    }

    
    function renderProtectedMarkdown(markdownText) {
      if (!markdownText) return "";
      const mathBlocks = [];
      
      // 1. Protect block math $$...$$
      let text = markdownText.replace(/\$\$([\s\S]*?)\$\$/g, (match, formula) => {
        const token = `@@MATH_BLOCK_${mathBlocks.length}@@`;
        mathBlocks.push({ token, formula, display: true });
        return token;
      });
      
      // 2. Protect inline math $...$
      text = text.replace(/\$([^$\n]+?)\$/g, (match, formula) => {
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
    
    function switchItem(key, rerenderSearch = true) {
      if (!items[key]) return;
      currentKey = key;
      const item = items[key];

      setMainMode("workspace", false);

      if (history.replaceState) {
        history.replaceState(null, null, "#" + key);
      } else {
        window.location.hash = "#" + key;
      }

      treeStructure.forEach(folder => {
        if (folder.filter && folder.filter(key) && collapsedFolders[folder.id]) {
          collapsedFolders[folder.id] = false;
          localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
        }
      });

      if (rerenderSearch) {
        renderTree(document.getElementById("search").value);
      } else {
        document.querySelectorAll(".nav-item").forEach(el => {
          if (el.getAttribute("data-key") === key) {
            el.classList.add("active");
          } else {
            el.classList.remove("active");
          }
        });
      }

      if (window.innerWidth <= 768) {
        toggleSidebar(false);
        setMobileTab(mobileTab);
      }

      const breadcrumb = document.getElementById("itemBreadcrumb");
      let folderLabel = item.category;
      let diffHtml = item.diff !== "All" ? `<span class="diff-badge ${item.diff}">${item.diff}</span>` : "";

      breadcrumb.innerHTML = `
        <span class="breadcrumb-folder">${folderLabel}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-file">${item.short || item.title}</span>
        ${diffHtml}
      `;

      const codeViewer = document.getElementById("codeViewer");
      if (item.code) {
        codeViewer.textContent = item.code;
        hljs.highlightElement(codeViewer);
      } else {
        codeViewer.textContent = "# No python solution source available for this item.";
      }

            const notesViewer = document.getElementById("notesViewer");
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
                {left: "\(", right: "\)", display: false},
                {left: "\[", right: "\]", display: true}
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
      }

      const copyBtn = document.getElementById("copyBtn");
      copyBtn.style.display = item.code ? "inline-flex" : "none";

      document.getElementById("left-pane").scrollTop = 0;
      document.getElementById("right-pane").scrollTop = 0;
    }

    function copyActiveCode() {
      const item = items[currentKey];
      if (!item || !item.code) return;

      navigator.clipboard.writeText(item.code).then(() => {
        const label = document.getElementById("copyBtnLabel");
        const originalText = label.innerText;
        label.innerText = "Copied!";
        setTimeout(() => {
          label.innerText = originalText;
        }, 1800);
      }).catch(err => {
        console.error("Failed to copy code: ", err);
      });
    }

    function toggleSidebar(forceState = null) {
      const sidebar = document.getElementById("sidebar");
      const backdrop = document.getElementById("sidebar-backdrop");
      const isMobile = window.innerWidth <= 768;

      if (isMobile) {
        const willOpen = forceState !== null ? forceState : !sidebar.classList.contains("mobile-open");
        sidebar.classList.toggle("mobile-open", willOpen);
        backdrop.classList.toggle("active", willOpen);
      } else {
        const isCollapsed = forceState !== null ? !forceState : !sidebar.classList.contains("collapsed");
        sidebar.classList.toggle("collapsed", isCollapsed);
      }
    }

    // Sidebar Resizer Dragging
    const resizer = document.getElementById("resizer");
    const sidebar = document.getElementById("sidebar");
    let isResizingSidebar = false;

    resizer.addEventListener("mousedown", (e) => {
      isResizingSidebar = true;
      resizer.classList.add("dragging");
      document.body.style.cursor = "col-resize";
      document.body.style.userSelect = "none";
    });

    // Workspace Split Resizer Dragging
    const workspaceResizer = document.getElementById("workspace-resizer");
    let isResizingWorkspace = false;

    workspaceResizer.addEventListener("mousedown", (e) => {
      isResizingWorkspace = true;
      workspaceResizer.classList.add("dragging");
      document.body.style.cursor = "col-resize";
      document.body.style.userSelect = "none";
    });

    workspaceResizer.addEventListener("dblclick", () => {
      workspaceSplitRatio = 50;
      localStorage.setItem("workspaceSplitRatio", "50");
      applyWorkspaceSplit(50);
    });

    window.addEventListener("mousemove", (e) => {
      if (isResizingSidebar) {
        const newWidth = Math.max(220, Math.min(650, e.clientX));
        sidebar.style.width = `${newWidth}px`;
        document.documentElement.style.setProperty("--sidebar-width", `${newWidth}px`);
      } else if (isResizingWorkspace) {
        const workspace = document.getElementById("workspace");
        const rect = workspace.getBoundingClientRect();
        const offsetX = e.clientX - rect.left;
        const totalWidth = rect.width;
        const ratio = (offsetX / totalWidth) * 100;
        workspaceSplitRatio = Math.max(15, Math.min(85, ratio));
        applyWorkspaceSplit(workspaceSplitRatio);
      }
    });

    window.addEventListener("mouseup", () => {
      if (isResizingSidebar) {
        isResizingSidebar = false;
        resizer.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
      }
      if (isResizingWorkspace) {
        isResizingWorkspace = false;
        workspaceResizer.classList.remove("dragging");
        document.body.style.cursor = "";
        document.body.style.userSelect = "";
        localStorage.setItem("workspaceSplitRatio", workspaceSplitRatio.toString());
      }
    });

    // Handle Window Resize Responsiveness
    window.addEventListener("resize", () => {
      if (mainMode === "workspace") {
        if (window.innerWidth <= 768) {
          setMobileTab(mobileTab);
        } else {
          setViewMode(viewMode);
        }
      }
    });

    // Keyboard Shortcuts
    window.addEventListener("keydown", (e) => {
      if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") {
        e.preventDefault();
        const searchInput = document.getElementById("search");
        if (sidebar.classList.contains("collapsed")) {
          toggleSidebar(true);
        }
        searchInput.focus();
        searchInput.select();
      } else if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "b") {
        e.preventDefault();
        toggleSidebar();
      } else if (e.key === "Escape") {
        const searchInput = document.getElementById("search");
        if (document.activeElement === searchInput) {
          clearSearch();
          searchInput.blur();
        }
      }
    });

    // Initialize SPA
    renderTree();
    updateProgressBadge();
    renderRoadmap('all');

    if (mainMode === "roadmap") {
      setMainMode("roadmap");
    } else {
      setMainMode("workspace", false);
      switchItem(currentKey);
    }
