# Ticket 04: Workspace Rebuild & E2E Verification

**Spec**: `specs/19-browser-history-push-state-navigation-and-generic-anchor-resolution-hardening.md`
**Status**: Blocked
**Blocked By**: `03-compiler-test-harness-consolidation-and-high-seam-tests.md`

---

## Description
Perform a clean rebuild of the Single Page Application artifact `index.html`, run the full test suite and validation audits, and verify end-to-end workspace integrity.

## Requirements
1. Run clean build: `python3 update_index.py --clean`.
2. Run test discovery: `python3 -m unittest discover tests`.
3. Verify note validation: `python3 -m unittest tests/test_note_structure.py`.
4. Ensure zero problem `.py` files modified per Core Rule 1.
5. Verify clean git working tree.
