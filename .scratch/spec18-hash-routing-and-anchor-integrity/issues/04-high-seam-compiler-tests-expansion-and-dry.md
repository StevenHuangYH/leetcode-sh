# 04: High-Seam Compiler Tests Expansion and Test Assertion DRYing

**What to build:**
In `tests/test_update_index.py`:
- Refactor repetitive `assertNotIn` statements for forbidden prefixes into parameterized loops over tested function strings.
- Add assertions verifying zero `.replace(/\.py$/, ".md")` in `resolver_fn` and `router_fn`.
- In the high-seam Node.js test harness:
  - Add test case verifying standalone anchor resolution:
    `resolveInitialRoute("#complexity")` resolves to `{ mode: "workspace", key: "README.md", anchor: "complexity" }`.
  - Add test case verifying static document resolution:
    `resolveEntityReference("README.md")` resolves to `{ key: "README.md", anchor: "" }`.
  - Add test case verifying invalid hash fallback preserves safety without crashing:
    `resolveInitialRoute("#nonexistent-slug-xyz")` returns `{ mode: "workspace", key: "README.md", anchor: "" }`.
  - Verify that `window.addEventListener("hashchange", ...)` is bound in compiled JavaScript output.

**Blocked by:** 01-standalone-anchor-preservation-and-route-fallback.md, 02-reactive-in-session-hash-navigation.md, 03-eliminate-residual-dead-extension-swapping.md

**Status:** todo

- [ ] Parameterize repetitive `assertNotIn` checks
- [ ] Add assertions checking zero dead `.replace(/\.py$/, ".md")` in resolver/router functions
- [ ] Add high-seam test case for standalone anchor resolution (`#complexity`)
- [ ] Add high-seam test case for static document resolution (`README.md`)
- [ ] Add high-seam assertion for `hashchange` listener registration
