# 03: KaTeX Formula Protection

**What to build:** Implement LaTeX delimiter protection in the markdown rendering pipeline so mathematical formulas with underscores and asterisks are preserved and rendered accurately by KaTeX without being corrupted into HTML italics tags.

**Blocked by:** 01: Preview and Generator Test Harness

**Status:** done

- [x] Implement math token replacement before invoking Markdown parsing
- [x] Restore raw LaTeX expressions before invoking `renderMathInElement`
- [x] Verify complex formulas (e.g. `O(\log n)`, `\sum_{i=0}^n`, modular arithmetic) render cleanly
