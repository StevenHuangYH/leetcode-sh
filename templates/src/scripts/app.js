const items = {items_json};
    const roadmapData = {roadmap_json};

    let mainMode = localStorage.getItem("mainMode") || "roadmap";
    let currentRoadmapSubview = localStorage.getItem("roadmapSubview") || "graph";
    let roadmapGraphInstance = null;
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
            <span class="breadcrumb-file">Interactive Topology Graph</span>
          `;
        }
        if (history.replaceState) {
          history.replaceState(null, null, "#roadmap");
        }
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

    const ROADMAP_GRAPH_DATA = {
      nodes: [
        // 根节点
        { data: { id: "root", topic_id: "topic-all", label: "数据结构与算法\nDSA Master", category: "Root Paradigm", status: "mastered", summary: "程序 = 数据结构 + 算法。涵盖核心线性结构、树图非线性拓扑与高级搜索/动规范式。" } },
        
        // 第一层分流
        { data: { id: "array_root", topic_id: "topic-01-arrays-sliding-window", label: "数组 (Array)", category: "Linear Structures", status: "mastered", summary: "连续内存分配，O(1) 随机访问。重点考察区间操作、原地修改与指针移动。" } },
        { data: { id: "linked_list_root", topic_id: "topic-05-linked-lists", label: "链表 (Linked List)", category: "Linear Structures", status: "mastered", summary: "离散内存指针连接。核心技巧：虚拟头节点 (Dummy Node)、快慢指针与反转操作。" } },

        // 数组分支 1: 数组操作流水线
        { data: { id: "arr_ops", topic_id: "topic-01-arrays-sliding-window", label: "数组操作", category: "Array Basics", status: "mastered", summary: "原地删除元素、移动零、区间覆盖与基础数组重排。" } },
        { data: { id: "prefix_sum", topic_id: "topic-03-prefix-sum", label: "前缀和 (Prefix Sum)", category: "Array Techniques", status: "mastered", summary: "预处理 O(N) 实现静态区间查询 O(1)，结合哈希表快速求解子数组和为 K 问题。" } },
        { data: { id: "diff_array", topic_id: "topic-03-prefix-sum", label: "差分数组 (Diff Array)", category: "Array Techniques", status: "learning", summary: "频繁对区间 [i, j] 进行 +val 更新时，借助差分数组将区间修改从 O(N) 降至 O(1)。" } },
        { data: { id: "matrix_2d", topic_id: "topic-04-intervals", label: "二维数组 (2D Matrix)", category: "Array Techniques", status: "learning", summary: "二维前缀和、顺时针旋转矩阵、螺旋遍历与对角线对称折叠技巧。" } },

        // 数组分支 2: 双指针流水线
        { data: { id: "two_pointers_tech", topic_id: "topic-01-arrays-sliding-window", label: "双指针技巧", category: "Two Pointers", status: "mastered", summary: "快慢指针、左右对撞指针与首尾滑动指针，用单调性减少暴力搜索维度。" } },
        { data: { id: "arr_two_pointers", topic_id: "topic-01-arrays-sliding-window", label: "数组双指针", category: "Two Pointers", status: "mastered", summary: "左右对撞双指针、有序数组两数之和、接雨水体积计算。" } },
        { data: { id: "sliding_window", topic_id: "topic-01-arrays-sliding-window", label: "滑动窗口 (Sliding Window)", category: "Two Pointers", status: "mastered", summary: "维护左右动态闭区间窗口，通过扩张与收缩寻找极值或可行解。" } },
        { data: { id: "binary_search", topic_id: "topic-02-binary-search", label: "二分搜索 (Binary Search)", category: "Searching", status: "mastered", summary: "利用单调性每次将搜索空间减半。涵盖闭区间模版、红蓝染色法与二分答案法。" } },
        { data: { id: "random_algo", topic_id: "topic-02-binary-search", label: "随机算法 (Randomized)", category: "Searching", status: "unvisited", summary: "蓄水池抽样算法 (Reservoir Sampling)、Fisher-Yates 原地随机洗牌算法。" } },

        // 数组分支 3: 数据结构流水线
        { data: { id: "basic_ds", topic_id: "topic-06-stacks-queues", label: "基础数据结构\n(循环数组/栈与队列/哈希/设计)", category: "Data Structures", status: "mastered", summary: "循环队列、单调栈/单调队列、哈希表冲突处理与 LRU/LFU 缓存机制设计。" } },
        { data: { id: "adv_ds", topic_id: "topic-07-trees-bst", label: "高级数据结构\n(二叉搜索树/堆/字典树/图论)", category: "Data Structures", status: "learning", summary: "二叉搜索树性质与平衡、大顶堆/小顶堆优先队列、Trie 前缀树与图论邻接表。" } },

        // 链表与树分支 1: 穿针引线到二叉树
        { data: { id: "ll_two_pointers", topic_id: "topic-05-linked-lists", label: "链表双指针", category: "Linked List", status: "mastered", summary: "寻找链表中点、Floyd 判圈算法检测环形链表、合并 K 个有序链表。" } },
        { data: { id: "recursion_tree", topic_id: "topic-07-trees-bst", label: "递归 (Recursion)", category: "Recursive Mindset", status: "mastered", summary: "数学归纳法与调用栈本原：明确递归基、单层处理逻辑与返回值契约。" } },
        { data: { id: "binary_tree_root", topic_id: "topic-07-trees-bst", label: "二叉树 (Binary Tree)", category: "Tree Hierarchies", status: "mastered", summary: "所有高级搜索与动态规划的母体结构。分为层序遍历视角与递归遍历视角。" } },

        // 二叉树 -> 层序遍历 & BFS 路线
        { data: { id: "level_order", topic_id: "topic-07-trees-bst", label: "层序遍历 (Level-order)", category: "Tree Traversal", status: "mastered", summary: "基于队列 Queue 实现自顶向下的逐层扫描与树的广度探索。" } },
        { data: { id: "bfs_search", topic_id: "topic-09-graphs", label: "广度优先搜索 (BFS)", category: "Search Algorithms", status: "mastered", summary: "水波纹扩散模型，求解无权图中的全局最短步数与路径。" } },
        { data: { id: "shortest_path", topic_id: "topic-09-graphs", label: "最短路径 (Shortest Path)", category: "Search Algorithms", status: "learning", summary: "Dijkstra 带权最短路、双向 BFS 搜索剪枝与 0-1 BFS 双端队列。" } },

        // 二叉树 -> 递归遍历分流
        { data: { id: "recursive_traversal", topic_id: "topic-07-trees-bst", label: "递归遍历 (Recursive Traversal)", category: "Tree Paradigms", status: "mastered", summary: "前序/中序/后序遍历，是回溯搜索与分治降维的算法理论源泉。" } },

        // 遍历视角：回溯 -> DFS
        { data: { id: "backtracking", topic_id: "topic-08-backtracking", label: "回溯算法 (Backtracking)", category: "Exhaustive Search", status: "mastered", summary: "在多叉决策树上做选择、递归深入、撤销选择 (Choose -> Explore -> Unchoose)。" } },
        { data: { id: "dfs_search", topic_id: "topic-09-graphs", label: "深度优先搜索 (DFS)", category: "Exhaustive Search", status: "mastered", summary: "连通分量计数、网格岛屿沉没、拓扑排序与状态空间深度穷举。" } },

        // 子问题视角：分治 -> DP
        { data: { id: "divide_and_conquer", topic_id: "topic-07-trees-bst", label: "分治算法 (Divide & Conquer)", category: "Subproblems", status: "mastered", summary: "大问题拆解为互不相交的子问题，分别求解后归并（如归并排序、快速排序）。" } },
        { data: { id: "dynamic_programming", topic_id: "topic-10-dp-math", label: "动态规划 (DP)", category: "Optimization", status: "learning", summary: "重叠子问题、最优子结构与状态转移方程。分为自顶向下带备忘录与自底向上递推表格。" } },

        // 其他算法：数学 -> 贪心
        { data: { id: "math_algo", topic_id: "topic-10-dp-math", label: "数学 (Math)", category: "Discrete Math", status: "mastered", summary: "位运算 (Bit Manipulation)、快速幂、辗转相除法 GCD 与素数筛法。" } },
        { data: { id: "greedy_algo", topic_id: "topic-10-dp-math", label: "贪心算法 (Greedy)", category: "Optimization", status: "learning", summary: "局部最优解能推导至全局最优解，需严格证明无后效性（如区间调度、跳跃游戏）。" } }
      ],
      edges: [
        // 根节点分流
        { data: { id: "e-root-arr", source: "root", target: "array_root", label: "数组分支" } },
        { data: { id: "e-root-ll", source: "root", target: "linked_list_root", label: "链表分支" } },

        // 数组分支 1: 数组操作流水线
        { data: { id: "e-arr-ops", source: "array_root", target: "arr_ops" } },
        { data: { id: "e-ops-prefix", source: "arr_ops", target: "prefix_sum" } },
        { data: { id: "e-prefix-diff", source: "prefix_sum", target: "diff_array" } },
        { data: { id: "e-diff-2d", source: "diff_array", target: "matrix_2d" } },

        // 数组分支 2: 双指针流水线
        { data: { id: "e-arr-tp", source: "array_root", target: "two_pointers_tech" } },
        { data: { id: "e-tp-arrtp", source: "two_pointers_tech", target: "arr_two_pointers" } },
        { data: { id: "e-arrtp-sw", source: "arr_two_pointers", target: "sliding_window" } },
        { data: { id: "e-sw-bs", source: "sliding_window", target: "binary_search" } },
        { data: { id: "e-bs-rand", source: "binary_search", target: "random_algo" } },

        // 数组分支 3: 数据结构流水线
        { data: { id: "e-arr-bds", source: "array_root", target: "basic_ds" } },
        { data: { id: "e-bds-ads", source: "basic_ds", target: "adv_ds" } },

        // 链表与树分支: Bridge (链表 -> 链表双指针 -> 递归 -> 二叉树)
        { data: { id: "e-ll-tp", source: "linked_list_root", target: "ll_two_pointers" } },
        { data: { id: "e-tp-rec", source: "ll_two_pointers", target: "recursion_tree" } },
        { data: { id: "e-rec-bt", source: "recursion_tree", target: "binary_tree_root" } },

        // 二叉树 -> 层序遍历 -> BFS -> 最短路径
        { data: { id: "e-bt-lo", source: "binary_tree_root", target: "level_order", label: "层序遍历" } },
        { data: { id: "e-lo-bfs", source: "level_order", target: "bfs_search" } },
        { data: { id: "e-bfs-sp", source: "bfs_search", target: "shortest_path" } },

        // 二叉树 -> 递归遍历，并分流为三路
        { data: { id: "e-bt-rec", source: "binary_tree_root", target: "recursive_traversal", label: "递归遍历" } },

        // 遍历视角：回溯算法 -> 深度优先搜索 (DFS)
        { data: { id: "e-rec-btk", source: "recursive_traversal", target: "backtracking", label: "遍历视角" } },
        { data: { id: "e-btk-dfs", source: "backtracking", target: "dfs_search" } },

        // 子问题视角：分治算法 -> 动态规划 (DP)
        { data: { id: "e-rec-dc", source: "recursive_traversal", target: "divide_and_conquer", label: "子问题视角" } },
        { data: { id: "e-dc-dp", source: "divide_and_conquer", target: "dynamic_programming" } },

        // 其他算法：数学 -> 贪心算法
        { data: { id: "e-rec-math", source: "recursive_traversal", target: "math_algo", label: "其他算法" } },
        { data: { id: "e-math-greedy", source: "math_algo", target: "greedy_algo" } }
      ]
    };

    function loadNoteByTopicId(topicId) {
      hideNodePopover();
      if (!topicId) return;
      if (items[topicId]) {
        setMainMode("workspace");
        switchItem(topicId);
        return;
      }
      const match = Object.keys(items).find(k => k === topicId || k.startsWith(topicId) || k.includes(topicId));
      if (match) {
        setMainMode("workspace");
        switchItem(match);
      } else {
        setMainMode("workspace");
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

      let posX = renderedPos.x + 15;
      let posY = renderedPos.y + 15;
      if (posX + 300 > containerRect.width) {
        posX = Math.max(10, renderedPos.x - 305);
      }
      if (posY + 260 > containerRect.height) {
        posY = Math.max(10, renderedPos.y - 250);
      }

      const currentStatus = nodeData.status || "unvisited";
      const title = (nodeData.label || "").replace(/\n/g, " ");

      popover.innerHTML = `
        <div class="popover-header">
          <div>
            <div class="popover-category">${nodeData.category || "DSA Topic"}</div>
            <div class="popover-title">${title}</div>
          </div>
          <button class="popover-close-btn" onclick="hideNodePopover()">✕</button>
        </div>
        <div class="popover-summary">
          ${nodeData.summary || "核心数据结构与算法解题心法，掌握对应递归基、状态转移与时间空间最优边界。"}
        </div>
        <div class="popover-status-row">
          <span class="popover-status-label">掌握状态:</span>
          <div class="status-pill-group">
            <button class="status-opt-btn mastered ${currentStatus === 'mastered' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'mastered')">● 已掌握</button>
            <button class="status-opt-btn learning ${currentStatus === 'learning' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'learning')">● 学习中</button>
            <button class="status-opt-btn unvisited ${currentStatus === 'unvisited' ? 'active' : ''}" onclick="updateGraphNodeStatus('${nodeData.id}', 'unvisited')">● 未开始</button>
          </div>
        </div>
        <button class="popover-action-btn" onclick="loadNoteByTopicId('${nodeData.topic_id}')">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
          <span>查看题解与源码</span>
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
            selector: 'node',
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
              'text-max-width': '140px',
              'font-size': '11px',
              'font-family': 'Consolas, -apple-system, sans-serif',
              'line-height': 1.35,
              'padding': '10px',
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
            selector: 'node#root',
            style: {
              'background-color': '#21262d',
              'border-color': '#2dd4bf',
              'border-width': 2.5,
              'font-weight': 'bold',
              'font-size': '12px'
            }
          },
          {
            selector: 'node:hover, node:selected',
            style: {
              'border-color': '#2dd4bf',
              'border-width': 2.5,
              'shadow-blur': 12,
              'shadow-color': 'rgba(45, 212, 191, 0.4)',
              'shadow-opacity': 0.8
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
              'arrow-scale': 1.1,
              'transition-property': 'line-color, opacity',
              'transition-duration': '0.2s'
            }
          },
          {
            selector: 'edge[label]',
            style: {
              'label': 'data(label)',
              'font-size': '9.5px',
              'font-weight': '600',
              'font-family': 'ui-monospace, Consolas, -apple-system, sans-serif',
              'color': '#2dd4bf',
              'text-background-color': '#0d1117',
              'text-background-opacity': 0.92,
              'text-background-padding': '3px 5px',
              'text-background-shape': 'roundrectangle',
              'text-border-color': '#30363d',
              'text-border-width': 1,
              'text-border-opacity': 0.8,
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
          name: 'dagre',
          rankDir: 'TB',
          nodeSep: 40,
          rankSep: 65,
          padding: 35
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
          cy.animate({ fit: { eles: cy.elements(), padding: 30 }, duration: 400 });
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
            cy.nodes().forEach(n => {
              const label = (n.data('label') || "").toLowerCase();
              const cat = (n.data('category') || "").toLowerCase();
              const tid = (n.data('topic_id') || "").toLowerCase();
              if (label.includes(q) || cat.includes(q) || tid.includes(q)) {
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
          const hasMath = item.notes && (item.notes.includes("$") || item.notes.includes("\(") || item.notes.includes("\["));
          if (hasMath && typeof renderMathInElement === "function") {
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

    if (mainMode === "roadmap") {
      setMainMode("roadmap");
    } else {
      setMainMode("workspace", false);
      switchItem(currentKey);
    }
