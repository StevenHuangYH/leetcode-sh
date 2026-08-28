# 04: Template Extraction and Generator Modularization

**What to build:** Decouple the frontend template (HTML/CSS/JS) into a dedicated template file, dynamically parse topic hierarchies from `ROADMAP.md` eliminating hardcoded dictionary bloat, and refactor `update_index.py` from 2,339 lines into a concise compiler under 250 lines.

**Blocked by:** 01: Preview and Generator Test Harness, 02: SPA Dual View and Fallback, 03: KaTeX Formula Protection

**Status:** done

- [x] Extract monolithic inline HTML/CSS/JS from `update_index.py` into `templates/station_template.html`
- [x] Implement dynamic Markdown parser for `ROADMAP.md` extracting phases, topics, formulas, and problem keys
- [x] Refactor `update_index.py` into a single-responsibility compiler under 250 lines
- [x] Verify `python3 update_index.py` generates identical or improved `index.html`
