# Ticket 03: Compiler Test Harness Consolidation & High-Seam Tests

**Spec**: `specs/19-browser-history-push-state-navigation-and-generic-anchor-resolution-hardening.md`
**Status**: Complete
**Blocked By**: `01-generic-syntax-anchor-resolution-and-allowlist-elimination.md`, `02-browser-history-push-state-navigation.md`

---

## Description
In `tests/test_update_index.py`, Node executable discovery is duplicated across multiple test methods. Furthermore, integration tests need to assert generic standalone anchor resolution (without static allowlists) and verify that `updateUrlHash` supports both push and replace behaviors.

## Requirements
1. Extract a shared helper method `_get_node_binary(self)` in `TestUpdateIndex`:
   - Checks `os.environ.get("NODE_BIN")`.
   - Checks `shutil.which("node")` and `shutil.which("nodejs")`.
   - Checks user fallback candidates (e.g. `Path.home().glob(".local/share/fnm/node-versions/*/installation/bin/node")`).
   - Deduplicate all call sites in `tests/test_update_index.py`.
2. Expand high-seam tests:
   - Verify that arbitrary custom anchor fragments (e.g. `#my-custom-proof-section`) resolve accurately to `isAnchorOnly: true` with the correct anchor slug and target document.
   - Verify that `updateUrlHash` contains both `pushState` and `replaceState` logic based on options.
   - Verify that `STANDALONE_SECTION_ANCHORS` is no longer present in compiled client code.
   - Verify that all unit tests pass.
