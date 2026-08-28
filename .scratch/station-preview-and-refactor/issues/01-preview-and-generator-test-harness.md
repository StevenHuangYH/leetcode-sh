# 01: Preview and Generator Test Harness

**What to build:** An automated test harness in `tests/test_preview_and_generator.py` asserting that `index.html` defaults to dual split-pane view, provides valid previews for problem entities without companion notes, protects KaTeX mathematical expressions from Markdown italics corruption, and enforces that the generator script is modular and under 350 lines.

**Blocked by:** None (can start immediately)

**Status:** done

- [x] Add unit test asserting `index.html` initial view mode is `"dual"`
- [x] Add unit test verifying problem entities without markdown notes render their Python solution code prominently
- [x] Add unit test asserting LaTeX math delimiters (`$O(\log n)$`, subscripts) are protected from `<em>` tag corruption
- [x] Add unit test asserting `update_index.py` code length is under 350 lines
