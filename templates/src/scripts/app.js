const items = {items_json};
    const configuredTracks = {tracks_json};
    const roadmapData = {roadmap_json};

    let mainMode = localStorage.getItem("mainMode") || "roadmap";
    let roadmapGraphInstance = null;
    let currentKey = "README.md";
    let viewMode = "notes"; // 'notes', 'dual', 'code'
    let mobileTab = "notes"; // 'notes', 'code'
    let workspaceSplitRatio = parseFloat(localStorage.getItem("workspaceSplitRatio") || "50");
    const collapsedFolders = JSON.parse(localStorage.getItem("treeCollapsedFolders") || "{}");
    let isInternalUrlUpdate = false;
    let lastHandledHash = (typeof window !== "undefined" && window.location && window.location.hash) ? window.location.hash : "";

    // Check initial URL hash
    let initialAnchor = "";
    if (window.location.hash && window.location.hash.length > 1) {
      const initialRoute = resolveInitialRoute(window.location.hash);
      mainMode = initialRoute.mode;
      currentKey = initialRoute.key;
      initialAnchor = initialRoute.anchor;
    }

    // Tree folder structure definitions matching README.md repo structure
    const staticFolders = [
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
      }
    ];

    const dynamicTrackFolders = (Array.isArray(configuredTracks) ? configuredTracks : []).map(t => ({
      id: t.id,
      name: `${t.dir_path}/`,
      label: t.display_label,
      filter: k => k.startsWith(`${t.dir_path}/`) || k.startsWith(`${t.id}/`)
    }));

    const treeStructure = [
      ...staticFolders,
      ...dynamicTrackFolders
    ];

    function updateProgressBadge() {
      const problemKeys = Object.keys(items).filter(k => items[k].type === "problem");
      document.getElementById("progressStats").innerText = `${problemKeys.length} Problems`;
    }

    function applyWorkspaceSplit(ratio) {
      const leftPane = document.getElementById("left-pane");
      const rightPane = document.getElementById("right-pane");
      if (!leftPane || !rightPane) return;
      if (viewMode === "dual" && window.innerWidth > 768) {
        const clamped = Math.max(15, Math.min(85, ratio));
        leftPane.style.width = `calc(${clamped}% - 2.5px)`;
        leftPane.style.flex = "none";
        rightPane.style.width = `calc(${100 - clamped}% - 2.5px)`;
        rightPane.style.flex = "none";
      } else {
        leftPane.style.width = "";
        leftPane.style.flex = "";
        rightPane.style.width = "";
        rightPane.style.flex = "";
      }
    }

    function setMobileTab(tab) {
      mobileTab = tab;
      applyWorkspaceSplit(50);
      const tabNotes = document.getElementById("mobileTabNotes");
      const tabCode = document.getElementById("mobileTabCode");
      if (tabNotes) tabNotes.classList.toggle("active", tab === "notes");
      if (tabCode) tabCode.classList.toggle("active", tab === "code");

      const workspace = document.getElementById("workspace");
      if (workspace) {
        workspace.classList.toggle("tab-notes", tab === "notes");
        workspace.classList.toggle("tab-code", tab === "code");
      }
    }

    function setViewMode(mode) {
      viewMode = mode;
      const workspace = document.getElementById("workspace");

      document.getElementById("btnDual").classList.toggle("active", mode === "dual");
      document.getElementById("btnNotes").classList.toggle("active", mode === "notes");
      document.getElementById("btnCode").classList.toggle("active", mode === "code");

      if (window.innerWidth <= 768) {
        setMobileTab(mode === "code" ? "code" : "notes");
        return;
      }

      if (workspace) {
        workspace.classList.remove("mode-dual", "mode-notes", "mode-code");
        workspace.classList.add(`mode-${mode}`);
      }

      if (mode === "dual") {
        applyWorkspaceSplit(workspaceSplitRatio);
      } else {
        applyWorkspaceSplit(50);
      }
    }

    function syncResponsiveLayout() {
      if (window.innerWidth <= 768) {
        setMobileTab(mobileTab);
      } else {
        setViewMode(viewMode);
      }
    }

    function setMainMode(mode, triggerSwitch = true, options = {}) {
      mainMode = mode;
      localStorage.setItem("mainMode", mode);

      const btnRoadmap = document.getElementById("btnModeRoadmap");
      const btnWorkspace = document.getElementById("btnModeWorkspace");
      const roadmapView = document.getElementById("roadmap-view");
      const workspaceView = document.getElementById("workspace");
      const mainContainer = document.getElementById("main-container");
      const copyBtn = document.getElementById("copyBtn");
      const breadcrumb = document.getElementById("itemBreadcrumb");
      const mobileNav = document.getElementById("mobileBottomNav");

      if (mode === "roadmap") {
        if (btnRoadmap) btnRoadmap.classList.add("active");
        if (btnWorkspace) btnWorkspace.classList.remove("active");
        if (roadmapView) roadmapView.classList.add("active");
        if (workspaceView) workspaceView.classList.add("hidden-view");
        if (mainContainer) mainContainer.classList.add("is-roadmap-mode");
        if (mobileNav) mobileNav.classList.add("hidden");
        if (breadcrumb) {
          breadcrumb.innerHTML = `
            <span class="breadcrumb-folder">Curriculum</span>
            <span class="breadcrumb-sep">/</span>
            <span class="breadcrumb-file" title="Interactive Topology Graph">Interactive Topology Graph</span>
          `;
        }
        updateUrlHash("#roadmap", { replace: Boolean(options && (options.replaceHistory || options.replace)) });
        setTimeout(() => {
          if (!roadmapGraphInstance) {
            initRoadmapGraph();
          } else if (roadmapGraphInstance.cy) {
            roadmapGraphInstance.cy.resize();
            roadmapGraphInstance.cy.fit(undefined, 35);
          }
        }, 50);
      } else {
        if (btnRoadmap) btnRoadmap.classList.remove("active");
        if (btnWorkspace) btnWorkspace.classList.add("active");
        if (roadmapView) roadmapView.classList.remove("active");
        if (workspaceView) workspaceView.classList.remove("hidden-view");
        if (mainContainer) mainContainer.classList.remove("is-roadmap-mode");
        if (copyBtn) copyBtn.classList.toggle("is-hidden", !items[currentKey]?.code);
        if (mobileNav) mobileNav.classList.remove("hidden");
        syncResponsiveLayout();
        if (triggerSwitch) {
          switchItem(currentKey, false, true, options);
        }
      }
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

    function buildSearchMatcher(query) {
      if (!query) return () => true;
      const clean = query.trim().toLowerCase();
      if (!clean) return () => true;
      const tokens = clean.split(/\s+/);
      const isAllNumeric = tokens.every(t => /^\d+$/.test(t));
      const matchers = tokens.map(token => {
        if (/^\d+$/.test(token)) {
          const targetNum = parseInt(token, 10);
          const boundaryRegex = new RegExp(`\\b0*${token}\\b`, "i");
          return (item) => {
            if (item.type !== "problem") {
              return !isAllNumeric && item.search_blob.includes(token);
            }
            if (item.lc_num) {
              const numOnly = item.lc_num.replace(/\D/g, "");
              if (numOnly && parseInt(numOnly, 10) === targetNum) return true;
            }
            // Strip leading curriculum batch sequence prefix (e.g. 01-lc-2235 -> lc-2235)
            const cleanSlug = (item.slug || "").replace(/^\d+-/, "");
            const cleanKey = (item.key || "").replace(/^[^/]+\/\d+-/, "");
            const idBlob = `${cleanKey} ${cleanSlug} ${item.title || ""} ${item.en_title || ""}`.toLowerCase();
            return boundaryRegex.test(idBlob);
          };
        }
        return (item) => item.search_blob.includes(token);
      });
      return (item) => matchers.every(m => m(item));
    }

    function renderTree(query = "") {
      const root = document.getElementById("treeRoot");
      if (!root) return;

      const isSearching = Boolean(query && query.trim().length > 0);
      const searchMatcher = buildSearchMatcher(query);
      let html = "";
      let totalVisible = 0;

      treeStructure.forEach(folder => {
        if (folder.isLeaf) {
          const matchingKey = Object.keys(items).find(k => folder.filter(k));
          if (!matchingKey) return;
          const item = items[matchingKey];
          if (isSearching && !searchMatcher(item)) return;

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
          ? folderKeys.filter(k => searchMatcher(items[k]))
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

          let numBadge = "";
          let mainTitle = item.title;
          let enSubtitle = "";

          const isProblem = item.type === "problem";
          const problemClass = isProblem ? "problem-item" : "";

          if (isProblem) {
            if (item.lc_num) {
              const numOnly = item.lc_num.replace(/^LC\s*/, '');
              numBadge = `<span class="tree-prob-num">${numOnly}</span>`;
            }
            mainTitle = item.en_title || item.title;
            if (item.cn_title && item.en_title && item.cn_title !== item.en_title) {
              enSubtitle = `<span class="tree-prob-en">${item.cn_title}</span>`;
            }
          } else {
            mainTitle = item.title || item.cn_title;
          }

          html += `
            <div class="nav-item ${problemClass} ${isActive ? 'active' : ''}" data-key="${itemKey}" onclick="switchItem('${itemKey}')" title="${item.title}">
              ${numBadge}
              <div class="tree-title-group">
                <span class="tree-main-title">${mainTitle}</span>
                ${enSubtitle}
              </div>
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

    let searchDebounceTimer = null;
    function handleSearch(query) {
      const clearBtn = document.getElementById("searchClear");
      if (query.trim().length > 0) {
        clearBtn.classList.add("visible");
      } else {
        clearBtn.classList.remove("visible");
      }
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(() => {
        renderTree(query);
        if (roadmapGraphInstance) {
          roadmapGraphInstance.highlightNodes(query);
        }
      }, 75);
    }

    function clearSearch() {
      const input = document.getElementById("search");
      input.value = "";
      document.getElementById("searchClear").classList.remove("visible");
      clearTimeout(searchDebounceTimer);
      renderTree("");
      if (roadmapGraphInstance) {
        roadmapGraphInstance.highlightNodes("");
      }
      const activeItem = document.querySelector("#treeRoot .nav-item.active");
      if (activeItem) {
        activeItem.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
      input.focus();
    }

    function renderProtectedMarkdown(markdownText) {
      if (!markdownText) return "";
      const mathBlocks = [];
      
      // 1. Protect dollar and backslash-delimited block math.
      let text = markdownText.replace(/\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]/g, (match, dollarFormula, bracketFormula) => {
        const formula = dollarFormula ?? bracketFormula;
        const token = `@@MATH_BLOCK_${mathBlocks.length}@@`;
        mathBlocks.push({ token, formula, display: true });
        return token;
      });
      
      // 2. Protect dollar and backslash-delimited inline math.
      text = text.replace(/\$([^$\n]+?)\$|\\\(([\s\S]*?)\\\)/g, (match, dollarFormula, bracketFormula) => {
        const formula = dollarFormula ?? bracketFormula;
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
    
    function switchItem(key, rerenderSearch = true, syncHash = true, options = {}) {
      let shouldRerender = rerenderSearch;
      let shouldSyncHash = syncHash;
      let opts = options || {};

      if (typeof rerenderSearch === "object" && rerenderSearch !== null) {
        opts = rerenderSearch;
        shouldRerender = true;
        shouldSyncHash = true;
      } else if (typeof syncHash === "object" && syncHash !== null) {
        opts = syncHash;
        shouldSyncHash = true;
      }

      if (!items[key]) return;
      currentKey = key;
      const item = items[key];

      setMainMode("workspace", false);

      if (shouldSyncHash) {
        updateUrlHash(key, { replace: Boolean(opts && (opts.replaceHistory || opts.replace)) });
      }

      treeStructure.forEach(folder => {
        if (folder.filter && folder.filter(key) && collapsedFolders[folder.id]) {
          collapsedFolders[folder.id] = false;
          localStorage.setItem("treeCollapsedFolders", JSON.stringify(collapsedFolders));
        }
      });

      if (shouldRerender) {
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
      let folderLabel = item.category_display || item.category || "Workspace";
      let diffHtml = item.diff && item.diff !== "All" ? `<span class="diff-badge ${item.diff}">${item.diff}</span>` : "";

      breadcrumb.innerHTML = `
        <span class="breadcrumb-folder">${folderLabel}</span>
        <span class="breadcrumb-sep">/</span>
        <span class="breadcrumb-file" title="${item.title}">${item.title}</span>
        ${diffHtml}
      `;

      const codeViewer = document.getElementById("codeViewer");
      if (item.code) {
        if (typeof hljs !== "undefined" && hljs.highlight) {
          try {
            codeViewer.innerHTML = hljs.highlight(item.code, { language: "python", ignoreIllegals: true }).value;
          } catch (e) {
            codeViewer.textContent = item.code;
            delete codeViewer.dataset.highlighted;
            hljs.highlightElement(codeViewer);
          }
        } else {
          codeViewer.textContent = item.code;
        }
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
          const hasMath = item.notes && (item.notes.includes("$") || item.notes.includes("\\(") || item.notes.includes("\\["));
          if (hasMath && typeof renderMathInElement === "function") {
            renderMathInElement(notesViewer, {
              delimiters: [
                {left: "$$", right: "$$", display: true},
                {left: "$", right: "$", display: false},
                {left: "\\(", right: "\\)", display: false},
                {left: "\\[", right: "\\]", display: true}
              ],
              throwOnError: false
            });
          }
        } catch (e) {
          console.warn("KaTeX error:", e);
        }
      } else if (item.code) {
        notesViewer.innerHTML = `<p style="color: var(--text-muted); padding: 16px;">Python solution displayed in code pane. Switch to Dual or Code view to inspect implementation.</p>`;
      } else {
        notesViewer.innerHTML = `<p style="color: var(--text-muted); padding: 16px;">No documentation notes or code found for this problem.</p>`;
      }

      const copyBtn = document.getElementById("copyBtn");
      if (copyBtn) {
        copyBtn.classList.toggle("is-hidden", !item.code);
      }

      document.getElementById("left-pane").scrollTop = 0;
      document.getElementById("right-pane").scrollTop = 0;
    }

    const DOM_RENDER_DELAY_MS = 60;

    /**
     * EntityReferenceResolver: Resolves relative file paths, stems, LC numbers, or slugs
     * to a registered DocumentEntity key in the in-memory items manifest.
     */
    function resolveEntityReference(rawHref, activeDocKey = null) {
      if (!rawHref) return null;

      let href = rawHref.trim();
      try {
        href = decodeURIComponent(href);
      } catch (_) {}
      if (!href) return null;

      // Handle leading '#' prefix for standalone anchors or fragment-based routing
      if (href.startsWith("#")) {
        const candidate = href.replace(/^#+/, "").trim();
        if (!candidate) return null;

        // Composite #doc#anchor reference
        if (candidate.includes("#")) {
          const subHashIdx = candidate.indexOf("#");
          const docPart = candidate.substring(0, subHashIdx);
          const anchorPart = candidate.substring(subHashIdx + 1);
          const resolvedDoc = resolveEntityReference(docPart, activeDocKey);
          if (resolvedDoc && resolvedDoc.key && typeof items !== "undefined" && items[resolvedDoc.key]) {
            return { key: resolvedDoc.key, anchor: anchorPart };
          }
          return null;
        }

        // Direct entity key or problem slug match
        const targetEntity = resolveEntityReference(candidate, activeDocKey);
        if (targetEntity && targetEntity.key && typeof items !== "undefined" && items[targetEntity.key]) {
          return targetEntity;
        }

        // Unindexed paths containing '/' or '.py'/'.md'
        const isUnindexedPath = candidate.includes("/") || candidate.endsWith(".py") || candidate.endsWith(".md");
        if (isUnindexedPath) {
          return null;
        }

        // Generic standalone anchor bound to active document
        return { key: activeDocKey || null, anchor: candidate, isAnchorOnly: true };
      }

      let anchor = "";
      const hashIndex = href.indexOf("#");
      if (hashIndex !== -1) {
        anchor = href.substring(hashIndex + 1);
        href = href.substring(0, hashIndex);
      }
      const queryIndex = href.indexOf("?");
      if (queryIndex !== -1) {
        href = href.substring(0, queryIndex);
      }

      let cleanPath = href.replace(/^(\.\/|\/|\.\.\/)+/, "").trim();
      if (!cleanPath && anchor) {
        return { key: activeDocKey || null, anchor: anchor, isAnchorOnly: true };
      }
      if (!cleanPath) return null;

      // 1. Exact Match in items
      if (items[cleanPath]) {
        return { key: cleanPath, anchor };
      }

      // 2. Companion note link conversion (.md -> .py)
      if (cleanPath.endsWith(".md")) {
        const pyKey = cleanPath.replace(/\.md$/, ".py");
        if (items[pyKey]) return { key: pyKey, anchor };
      }

      // 3. Problem index / topic docs match
      if (items[`problem-index/${cleanPath}`]) {
        return { key: `problem-index/${cleanPath}`, anchor };
      }
      if (cleanPath.startsWith("topic-") && items[cleanPath]) {
        return { key: cleanPath, anchor };
      }
      if (Array.isArray(configuredTracks)) {
        for (const t of configuredTracks) {
          if (t.id && cleanPath.startsWith(`${t.id}/`)) {
            const canonicalCandidate = `${t.dir_path}/${cleanPath.slice(t.id.length + 1)}`;
            if (items[canonicalCandidate]) return { key: canonicalCandidate, anchor };
            if (cleanPath.endsWith(".md")) {
              const pyKey = canonicalCandidate.replace(/\.md$/, ".py");
              if (items[pyKey]) return { key: pyKey, anchor };
            }
          }
        }
      }

      // 4. Track prefix fallback & Stem matching
      const stem = cleanPath.split("/").pop().replace(/\.(py|md)$/, "").toLowerCase();
      const searchTracks = [];
      if (Array.isArray(configuredTracks)) {
        for (const t of configuredTracks) {
          if (t.dir_path && !searchTracks.includes(t.dir_path)) searchTracks.push(t.dir_path);
        }
      }
      for (const track of searchTracks) {
        const tryPy = `${track}/${stem}.py`;
        const tryMd = `${track}/${stem}.md`;
        if (items[tryPy]) return { key: tryPy, anchor };
        if (items[tryMd]) return { key: tryMd, anchor };
      }

      // 5. LC Number & exact slug matching
      const lcNumMatch = stem.match(/(?:^|\b)(?:lc-?)(\d+)/i) || stem.match(/(?:^|\b)(\d+)\b/);
      const targetLcNum = lcNumMatch ? parseInt(lcNumMatch[1], 10) : null;

      for (const k in items) {
        const item = items[k];
        if (item.type === "problem") {
          if (targetLcNum !== null && item.lc_num) {
            const itemNum = parseInt(item.lc_num.replace(/\D/g, ""), 10);
            if (itemNum === targetLcNum) {
              return { key: k, anchor };
            }
          }
          if (item.slug && item.slug === stem) {
            return { key: k, anchor };
          }
          if (item.path && item.path.toLowerCase().endsWith(`/${stem}`)) {
            return { key: k, anchor };
          }
        }
      }

      return null;
    }

    /**
     * Resolves an initial URL hash to a structured route target ({ mode, key, anchor }).
     * Delegates entity resolution directly to resolveEntityReference while preserving
     * standalone anchor targets and user view mode.
     */
    function resolveInitialRoute(rawHash, activeDocumentKey = null) {
      const fallbackKey = activeDocumentKey || ((typeof currentKey !== "undefined" && currentKey) ? currentKey : "README.md");
      const DEFAULT_ROUTE = { mode: "workspace", key: "README.md", anchor: "" };
      const fallbackRoute = (typeof mainMode !== "undefined" && mainMode)
        ? { ...DEFAULT_ROUTE, mode: mainMode }
        : DEFAULT_ROUTE;

      if (!rawHash) {
        return fallbackRoute;
      }
      const cleanHash = rawHash.replace(/^#/, "").trim();
      if (!cleanHash) {
        return fallbackRoute;
      }
      if (cleanHash === "roadmap") {
        return { mode: "roadmap", key: "README.md", anchor: "" };
      }

      const resolved = resolveEntityReference(rawHash, activeDocumentKey);
      if (resolved) {
        if (resolved.isAnchorOnly) {
          return { mode: "workspace", key: fallbackKey, anchor: resolved.anchor };
        }
        if (resolved.key && items[resolved.key]) {
          return { mode: "workspace", key: resolved.key, anchor: resolved.anchor || "" };
        }
      }

      return { ...fallbackRoute, isFallback: true };
    }

    /**
     * Finds a heading DOM element strictly within a container matching an anchor id or slug.
     */
    function findHeadingElement(container, anchorId) {
      if (!container || !anchorId) return null;
      const cleanAnchor = anchorId.toLowerCase();
      const direct = container.querySelector(`[id="${anchorId}"], [name="${anchorId}"], h1[id="${anchorId}"], h2[id="${anchorId}"], h3[id="${anchorId}"], h4[id="${anchorId}"], h5[id="${anchorId}"], h6[id="${anchorId}"]`);
      if (direct) return direct;
      return Array.from(container.querySelectorAll("h1, h2, h3, h4, h5, h6")).find(h => {
        const cleanHeading = h.textContent.trim().toLowerCase();
        const slug1 = cleanHeading.replace(/[^\w\s-]/g, "").trim().replace(/\s+/g, "-");
        const slug2 = cleanHeading.replace(/[^\w\s-]/g, " ").trim().replace(/\s+/g, "-");
        return slug1 === cleanAnchor || slug2 === cleanAnchor || cleanHeading === cleanAnchor;
      }) || null;
    }

    /**
     * Scrolls the notes viewer to a target heading matching the anchor.
     * Optionally waits for delay ms (e.g. DOM_RENDER_DELAY_MS) before scrolling.
     */
    function scrollToAnchor(anchor, delay = 0) {
      if (!anchor) return;
      const doScroll = () => {
        const notesViewer = document.getElementById("notesViewer");
        if (!notesViewer) return;
        const targetEl = findHeadingElement(notesViewer, anchor);
        if (targetEl) {
          targetEl.scrollIntoView({ behavior: "smooth", block: "start" });
        }
      };
      if (delay > 0) {
        setTimeout(doScroll, delay);
      } else {
        doScroll();
      }
    }

    /**
     * Updates the window URL hash while protecting against recursive hashchange loops.
     * Supports options: { replace = false }.
     * When options.replace is true, calls history.replaceState.
     * When options.replace is false, calls history.pushState.
     */
    function updateUrlHash(hashKey, { replace = false } = {}) {
      if (!hashKey) return;
      const targetHash = hashKey.startsWith("#") ? hashKey : "#" + hashKey;
      if (typeof window !== "undefined" && window.location && window.location.hash === targetHash) {
        lastHandledHash = targetHash;
        return;
      }
      isInternalUrlUpdate = true;
      lastHandledHash = targetHash;
      try {
        if (typeof history !== "undefined") {
          if (replace && typeof history.replaceState === "function") {
            history.replaceState(null, "", targetHash);
          } else if (!replace && typeof history.pushState === "function") {
            history.pushState(null, "", targetHash);
          } else if (typeof history.replaceState === "function") {
            history.replaceState(null, "", targetHash);
          } else if (typeof window !== "undefined" && window.location) {
            window.location.hash = targetHash;
          }
        } else if (typeof window !== "undefined" && window.location) {
          window.location.hash = targetHash;
        }
      } catch (err) {
        try {
          if (typeof window !== "undefined" && window.location) {
            window.location.hash = targetHash;
          }
        } catch (_) {}
      } finally {
        setTimeout(() => {
          isInternalUrlUpdate = false;
        }, 0);
      }
    }

    /**
     * Handles in-session window hashchange events, dispatching route updates,
     * view mode transitions, and deep anchor scrolling without page reloads.
     */
    function handleHashChange() {
      if (isInternalUrlUpdate) return;
      const currentHash = window.location.hash;
      if (currentHash === lastHandledHash) return;
      lastHandledHash = currentHash;

      const route = resolveInitialRoute(window.location.hash);
      if (route && route.isFallback) {
        updateUrlHash(route.key, { replace: true });
      }

      const { mode, key, anchor } = route;
      if (mode !== mainMode) {
        setMainMode(mode, false, { replaceHistory: true });
      }

      if (mode === "workspace") {
        const itemChanged = (key !== currentKey);
        if (itemChanged && items[key]) {
          switchItem(key, true, false, { replaceHistory: true });
        }
        if (anchor) {
          scrollToAnchor(anchor, itemChanged ? DOM_RENDER_DELAY_MS : 0);
        }
      }
    }

    /**
     * Enforces Notes-First view mode across desktop and mobile breakpoints.
     */
    function enforceNotesView() {
      if (window.innerWidth <= 768) {
        setMobileTab("notes");
      } else {
        setViewMode("notes");
      }
    }

    /**
     * InternalNavigationInterceptor: Intercepts link clicks within workspace & notes
     * to route internal files, in-page anchors, and external links without triggering page downloads.
     */
    /**
     * Formats a canonical URL hash for deep anchor navigation.
     */
    function formatAnchorHash(docKey, anchor) {
      return docKey === "README.md" ? `#${anchor}` : `#${docKey}#${anchor}`;
    }

    function initLinkInterceptor() {
      document.addEventListener("click", (e) => {
        const link = e.target.closest("a");
        if (!link) return;

        const rawHref = link.getAttribute("href");
        if (!rawHref) return;

        // 1. External URLs (http, https, mailto, etc.)
        if (/^(https?:|\/\/|mailto:)/i.test(rawHref)) {
          link.setAttribute("target", "_blank");
          link.setAttribute("rel", "noopener noreferrer");
          return;
        }

        // 2. Pure in-page anchor (#heading)
        if (rawHref.startsWith("#")) {
          e.preventDefault();
          const anchorId = rawHref.substring(1);
          if (items[anchorId]) {
            enforceNotesView();
            switchItem(anchorId, true, true, { replaceHistory: false });
            return;
          }
          scrollToAnchor(anchorId);
          const targetHash = formatAnchorHash(currentKey, anchorId);
          updateUrlHash(targetHash, { replace: false });
          return;
        }

        // 3. Relative File / Entity Reference
        const isRelativeDocLink = rawHref.endsWith(".py") || rawHref.endsWith(".md") || rawHref.startsWith("./") || rawHref.startsWith("../") || rawHref.startsWith("problem-index/") || rawHref.startsWith("topic-");
        const resolved = resolveEntityReference(rawHref, currentKey);
        if (resolved && resolved.key && items[resolved.key]) {
          e.preventDefault();
          const targetKey = resolved.key;

          enforceNotesView();
          if (resolved.anchor) {
            switchItem(targetKey, true, false, { replaceHistory: false });
            scrollToAnchor(resolved.anchor, DOM_RENDER_DELAY_MS);
            const targetHash = formatAnchorHash(targetKey, resolved.anchor);
            updateUrlHash(targetHash, { replace: false });
          } else {
            switchItem(targetKey, true, true, { replaceHistory: false });
          }
          return;
        } else if (isRelativeDocLink) {
          // Prevent browser from triggering a 404 or file download for unindexed relative references
          e.preventDefault();
          console.warn("[InternalNavigationInterceptor] Unindexed relative link reference:", rawHref);
        }
      });
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
        syncResponsiveLayout();
      }
    });

    // Keyboard Shortcuts
    const searchEl = document.getElementById("search");
    if (searchEl) {
      searchEl.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
          e.preventDefault();
          const firstMatchElement = document.querySelector("#treeRoot .problem-item") || document.querySelector("#treeRoot .nav-item[data-key]");
          if (firstMatchElement) {
            const key = firstMatchElement.getAttribute("data-key");
            if (key && items[key]) {
              switchItem(key, false, true, { replaceHistory: false });
              firstMatchElement.scrollIntoView({ behavior: "smooth", block: "nearest" });
              const notesViewer = document.getElementById("notesViewer");
              if (notesViewer) {
                notesViewer.focus();
              }
            }
          }
        }
      });
    }

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
    window.addEventListener("hashchange", handleHashChange);
    initLinkInterceptor();
    renderTree();
    updateProgressBadge();

    if (mainMode === "roadmap") {
      setMainMode("roadmap", true, { replaceHistory: true });
    } else {
      setMainMode("workspace", false);
      switchItem(currentKey, true, !initialAnchor, { replaceHistory: true });
      if (initialAnchor) {
        scrollToAnchor(initialAnchor, DOM_RENDER_DELAY_MS);
      }
    }
