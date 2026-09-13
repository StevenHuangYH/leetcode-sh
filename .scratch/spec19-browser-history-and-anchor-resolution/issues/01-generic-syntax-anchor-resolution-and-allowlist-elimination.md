# Ticket 01: Generic Syntax-Based Anchor Resolution & Elimination of Hardcoded Allowlist

**Spec**: `specs/19-browser-history-push-state-navigation-and-generic-anchor-resolution-hardening.md`
**Status**: Ready
**Blocked By**: None

---

## Description
In `templates/src/scripts/app.js`, `resolveInitialRoute` prematurely strips the leading `#` from the hash input before calling `resolveEntityReference`. Because `resolveEntityReference` uses `normalized.startsWith("#")` to detect standalone anchor references targeting the active document, this premature stripping causes it to treat the anchor as an unindexed document path. To bypass this, a hardcoded 17-item `STANDALONE_SECTION_ANCHORS` Set was introduced in Spec 18.

## Requirements
1. Remove `STANDALONE_SECTION_ANCHORS` completely from `templates/src/scripts/app.js`.
2. In `resolveInitialRoute(hashKey, activeDocumentKey)`:
   - Pass `hashKey` (or normalized query retaining `#` for anchors) directly to `resolveEntityReference(hashKey, activeDocumentKey)`.
   - Remove manual delimiter splitting (`cleanHash.includes("#")`) in `resolveInitialRoute`; rely entirely on the structured `{ key, item, anchor, isAnchorOnly }` returned by `resolveEntityReference`.
3. In `resolveEntityReference(rawRef, activeDocKey)`:
   - Ensure any input with a leading `#` (e.g. `#any-custom-anchor`) is recognized as `isAnchorOnly: true`, using `activeDocKey` as the document key and extracting the trimmed slug after `#` as `anchor`.
   - For composite references like `lc-0001#custom-section`, return the resolved document entity key and the extracted anchor.
4. Ensure standalone anchors gracefully fall back to the default document (`README.md`) if no active document is present.
