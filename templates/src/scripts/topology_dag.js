/**
 * Topology DAG Interactive Module
 * Manages Cytoscape graph lifecycle, node popovers, mastery status updates,
 * and seamless navigation hooks into problem workspace.
 */

const ROADMAP_GRAPH_DATA = {roadmap_graph_json};

    function openWorkspaceForNode(nodeId, topicId, labelText) {
      hideNodePopover();
      setMainMode("workspace");

      const searchInput = document.getElementById("search");
      const cleanLabel = (labelText || "").split("\n")[0].trim();
      const nodeKeywords = [nodeId, cleanLabel].filter(Boolean);

      // Search for matching problem items
      let matchedKey = null;
      for (const k in items) {
        const item = items[k];
        if (item.type === "problem") {
          const blob = (item.search_blob || "").toLowerCase();
          const target = `${item.slug || ''} ${item.tags || ''} ${item.title || ''} ${item.cn_title || ''} ${item.key || ''}`.toLowerCase();
          if (nodeKeywords.some(kw => blob.includes(kw.toLowerCase()) || target.includes(kw.toLowerCase()))) {
            matchedKey = k;
            break;
          }
        }
      }

      if (matchedKey) {
        if (searchInput) {
          searchInput.value = cleanLabel;
          handleSearch(cleanLabel);
        }
        switchItem(matchedKey);
        return;
      }

      // Fallback to topic curriculum documentation
      if (topicId && items[topicId]) {
        switchItem(topicId);
        return;
      }
      const match = Object.keys(items).find(k => k === topicId || k.startsWith(topicId) || k.includes(topicId));
      if (match) {
        switchItem(match);
      } else {
        switchItem("README.md");
      }
    }

    function showNodePopover(node) {
      const popover = document.getElementById("cy-node-popover");
      if (!popover) return;

      const nodeData = node.data();
      const renderedPos = node.renderedPosition();
      const container = document.getElementById("roadmap-view");
      const containerRect = container.getBoundingClientRect();

      const problems = nodeData.problems || [];
      const hasProblems = problems.length > 0;

      let posX = renderedPos.x + 15;
      let posY = renderedPos.y + 15;
      if (posX + 350 > containerRect.width) {
        posX = Math.max(10, renderedPos.x - 345);
      }
      if (posY + (hasProblems ? 360 : 270) > containerRect.height) {
        posY = Math.max(10, renderedPos.y - (hasProblems ? 350 : 260));
      }

      const currentStatus = nodeData.status || "unvisited";
      const rawLabel = nodeData.label || "";
      const labelParts = rawLabel.split("\n");
      const titleEn = labelParts[0] || nodeData.id;
      const titleCn = labelParts[1] || "";
      const displayTitle = titleCn ? `${titleEn} · ${titleCn}` : titleEn;
      const count = nodeData.problem_count || 0;
      const countBadge = count > 0 ? `<span class="popover-count-badge">${count} Problems</span>` : '<span class="popover-count-badge" style="opacity:0.65;">Topic Concept</span>';

      let problemsHtml = "";
      if (hasProblems) {
        const problemItems = problems.map(p => {
          const numOnly = (p.lc_num || "").replace(/\D/g, "");
          const numBadge = numOnly ? `<span class="popover-prob-num">${numOnly}</span>` : "";
          const diffClass = `diff-${(p.diff || "medium").toLowerCase()}`;
          const cleanTitle = p.short || p.title || p.key;
          return `
            <div class="popover-prob-item" onclick="switchItem('${p.key}')" title="${p.title || cleanTitle}">
              ${numBadge}
              <span class="popover-prob-title">${cleanTitle}</span>
              <span class="popover-prob-diff ${diffClass}"></span>
            </div>
          `;
        }).join("");

        problemsHtml = `
          <div class="popover-problem-section">
            <div class="popover-problem-header">
              <span>Linked Problems (${problems.length})</span>
            </div>
            <div class="popover-problem-list">
              ${problemItems}
            </div>
          </div>
        `;
      }

      popover.innerHTML = `
        <div class="popover-header">
          <div>
            <div style="display: flex; align-items: center; gap: 6px;">
              <span class="popover-category">${nodeData.category || "DSA Topic"}</span>
              ${countBadge}
            </div>
            <div class="popover-title">${displayTitle}</div>
          </div>
          <button class="popover-close-btn" onclick="hideNodePopover()">✕</button>
        </div>
        <div class="popover-summary">
          ${nodeData.summary || "Core data structure & algorithm paradigms with time/space complexity invariants and recursion contracts."}
        </div>
        ${problemsHtml}
        <div class="popover-status-row">
          <span class="popover-status-label">Mastery Status:</span>
          <div class="status-pill-group">
            <button class="status-opt-btn mastered ${currentStatus === 'mastered' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'mastered')">● Mastered</button>
            <button class="status-opt-btn learning ${currentStatus === 'learning' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'learning')">● In Progress</button>
            <button class="status-opt-btn unvisited ${currentStatus === 'unvisited' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'unvisited')">● Unvisited</button>
          </div>
        </div>
        <button class="popover-action-btn" onclick="openWorkspaceForNode('${nodeData.id}', '${nodeData.topic_id || ''}', '${titleEn.replace(/'/g, "\\'")}')">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
          <span>${count > 0 ? `Filter All in Workspace` : 'Open Curriculum Topic'}</span>
        </button>
      `;

      popover.style.left = `${posX}px`;
      popover.style.top = `${posY}px`;
      popover.style.display = "flex";
    }

    function hideNodePopover() {
      const popover = document.getElementById("cy-node-popover");
      if (popover) popover.style.display = "none";
    }

    function updateGraphNodeStatus(nodeId, newStatus) {
      const savedStatusMap = JSON.parse(localStorage.getItem("leetcodeRoadmapStatusMap") || "{}");
      savedStatusMap[nodeId] = newStatus;
      localStorage.setItem("leetcodeRoadmapStatusMap", JSON.stringify(savedStatusMap));

      if (roadmapGraphInstance && roadmapGraphInstance.cy) {
        const node = roadmapGraphInstance.cy.getElementById(nodeId);
        if (node) {
          node.data('status', newStatus);
          showNodePopover(node);
        }
      }
    }

    function initRoadmapGraph() {
      const container = document.getElementById("cy-roadmap");
      if (!container || typeof cytoscape === "undefined") return;

      if (typeof cytoscapeDagre !== "undefined") {
        cytoscape.use(cytoscapeDagre);
      }

      // Load saved statuses from localStorage
      const savedStatusMap = JSON.parse(localStorage.getItem("leetcodeRoadmapStatusMap") || "{}");
      ROADMAP_GRAPH_DATA.nodes.forEach(n => {
        if (savedStatusMap[n.data.id]) {
          n.data.status = savedStatusMap[n.data.id];
        }
      });

      const cy = cytoscape({
        container: container,
        elements: [...ROADMAP_GRAPH_DATA.nodes, ...ROADMAP_GRAPH_DATA.edges],
        boxSelectionEnabled: false,
        autounselectify: false,
        style: [
          {
            selector: 'node[node_type = "group"]',
            style: {
              'shape': 'round-rectangle',
              'background-color': '#11161d',
              'background-opacity': 0.65,
              'border-width': 1.5,
              'border-style': 'dashed',
              'border-color': '#30363d',
              'color': '#8b949e',
              'label': 'data(label)',
              'text-valign': 'top',
              'text-halign': 'center',
              'text-margin-y': 10,
              'text-wrap': 'wrap',
              'text-max-width': '180px',
              'font-size': '11.5px',
              'font-weight': '600',
              'font-family': '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", sans-serif',
              'padding': '16px'
            }
          },
          {
            selector: 'node[node_type = "normal"]',
            style: {
              'shape': 'round-rectangle',
              'background-color': '#161b22',
              'border-width': 1.5,
              'border-color': '#30363d',
              'color': '#f0f6fc',
              'label': 'data(label)',
              'text-valign': 'center',
              'text-halign': 'center',
              'text-wrap': 'wrap',
              'text-max-width': '145px',
              'font-size': '12px',
              'font-weight': '500',
              'font-family': '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif',
              'line-height': 1.35,
              'padding': '10px 14px',
              'width': 'label',
              'height': 'label',
              'transition-property': 'background-color, border-color, opacity, border-width, shadow-blur',
              'transition-duration': '0.2s'
            }
          },
          {
            selector: 'node[status = "mastered"]',
            style: { 'border-color': '#238636', 'border-width': 2 }
          },
          {
            selector: 'node[status = "learning"]',
            style: { 'border-color': '#d29922', 'border-width': 2 }
          },
          {
            selector: 'node[status = "unvisited"]',
            style: { 'border-color': '#30363d' }
          },
          {
            selector: 'node#data-structure-algorithm',
            style: {
              'background-color': '#1c2128',
              'border-color': '#52c41a',
              'border-width': 2.5,
              'font-weight': 'bold',
              'font-size': '13px'
            }
          },
          {
            selector: 'node:hover, node:selected',
            style: {
              'border-color': '#2dd4bf',
              'border-width': 2.5,
              'shadow-blur': 14,
              'shadow-color': 'rgba(45, 212, 191, 0.45)',
              'shadow-opacity': 0.85
            }
          },
          {
            selector: 'edge',
            style: {
              'width': 2,
              'line-color': '#30363d',
              'target-arrow-color': '#2dd4bf',
              'target-arrow-shape': 'triangle',
              'curve-style': 'bezier',
              'arrow-scale': 1.15,
              'transition-property': 'line-color, opacity',
              'transition-duration': '0.2s'
            }
          },
          {
            selector: 'edge[label]',
            style: {
              'label': 'data(label)',
              'font-size': '10.5px',
              'font-weight': '600',
              'font-family': '-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", sans-serif',
              'color': '#2dd4bf',
              'text-background-color': '#0d1117',
              'text-background-opacity': 0.95,
              'text-background-padding': '3px 6px',
              'text-background-shape': 'roundrectangle',
              'text-border-color': '#30363d',
              'text-border-width': 1,
              'text-border-opacity': 0.85,
              'text-rotation': 'autorotate'
            }
          },
          {
            selector: '.highlighted',
            style: {
              'border-color': '#2dd4bf',
              'border-width': 3,
              'shadow-blur': 18,
              'shadow-color': 'rgba(45, 212, 191, 0.7)',
              'shadow-opacity': 1,
              'opacity': 1
            }
          },
          {
            selector: '.dimmed',
            style: {
              'opacity': 0.2
            }
          }
        ],
        layout: {
          name: 'preset',
          padding: 45,
          fit: true
        }
      });

      cy.on('tap', 'node', (evt) => {
        showNodePopover(evt.target);
      });

      cy.on('tap', (evt) => {
        if (evt.target === cy) {
          hideNodePopover();
        }
      });

      cy.on('pan zoom', () => {
        hideNodePopover();
      });

      roadmapGraphInstance = {
        cy: cy,
        fitView: () => {
          hideNodePopover();
          cy.animate({ fit: { eles: cy.elements(), padding: 35 }, duration: 400 });
        },
        zoomIn: () => {
          hideNodePopover();
          cy.zoom({ level: cy.zoom() * 1.25, renderedPosition: { x: container.clientWidth / 2, y: container.clientHeight / 2 } });
        },
        zoomOut: () => {
          hideNodePopover();
          cy.zoom({ level: cy.zoom() * 0.8, renderedPosition: { x: container.clientWidth / 2, y: container.clientHeight / 2 } });
        },
        highlightNodes: (query) => {
          hideNodePopover();
          const q = (query || "").trim().toLowerCase();
          cy.batch(() => {
            if (!q) {
              cy.elements().removeClass('dimmed highlighted');
              return;
            }
            let firstMatch = null;
            const isNumeric = /^\d+$/.test(q);
            const targetNum = isNumeric ? parseInt(q, 10) : null;

            cy.nodes().forEach(n => {
              const label = (n.data('label') || "").toLowerCase();
              const cat = (n.data('category') || "").toLowerCase();
              const tid = (n.data('topic_id') || "").toLowerCase();
              const summary = (n.data('summary') || "").toLowerCase();
              const keywords = (n.data('keywords') || []).map(k => String(k).toLowerCase());
              const problems = n.data('problems') || [];

              const matchesMeta = label.includes(q) || cat.includes(q) || tid.includes(q) || summary.includes(q) || keywords.some(k => k.includes(q));
              const matchesProblem = problems.some(p => {
                if (isNumeric && p.lc_num) {
                  const pNum = parseInt(String(p.lc_num).replace(/\D/g, ""), 10);
                  if (pNum === targetNum) return true;
                }
                const pText = `${p.key || ''} ${p.title || ''} ${p.short || ''}`.toLowerCase();
                return pText.includes(q);
              });

              if (matchesMeta || matchesProblem) {
                n.removeClass('dimmed').addClass('highlighted');
                if (!firstMatch) firstMatch = n;
              } else {
                n.removeClass('highlighted').addClass('dimmed');
              }
            });
            cy.edges().addClass('dimmed');
            if (firstMatch) {
              cy.animate({
                center: { eles: firstMatch },
                zoom: 1.15,
                duration: 500
              });
            }
          });
        }
      };
    }
