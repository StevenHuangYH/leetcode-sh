# Spec 17: Client Router Architectural Consolidation, Dynamic Directory Mapping, and Routing Seam Unification

**Triage Label**: `ready-for-agent`

---

## Problem Statement

When learners and maintainers navigate the `leetcode-sh` Study Station via direct URL bookmarks, legacy track routes, or markdown cross-references, URL routing and entity reference resolution suffer from architectural friction and code smells uncovered during post-Spec 16 code review:

1. **Hardcoded Directory Assumption (`problems/` String Literal)**:
   Legacy route resolution and direct path matching in the client runtime script construct canonical paths by prepending a hardcoded `'problems/'` string literal (`'problems/' + path`). If a track is configured with a directory outside of `problems/` or a custom directory mapping in the centralized track registry, legacy redirection and internal cross-references fail. The client router violates the single source of truth principle by ignoring the track's configured directory path property.

2. **Duplicated Routing and Resolution Logic**:
   The client application startup hash router contains an inline cascade of path matching, track prefix iteration, and extension swapping that duplicates the domain responsibilities of the `EntityReferenceResolver`. When routing logic needs enhancement, developers face shotgun surgery across multiple script blocks in the client application bundle.

3. **Speculative Generality and Dead Code in Extension Swapping**:
   The client router contains dead defensive branches checking for `.md` keys converted from `.py` problem files. Because problem entities in the Study Station are keyed strictly by their `.py` source paths (with markdown companion notes rendered as attached content rather than separate item entries), querying the items collection with `.replace(/\.py$/, ".md")` is unreachable dead code. Furthermore, unrestricted bidirectional extension swapping on arbitrary non-legacy URLs introduces unrequested scope creep.

4. **Test Harness Reimplementation and Seam Drift**:
   Compiler integration tests duplicate client routing logic inside synthetic test strings rather than evaluating the actual production routing functions extracted directly from the compiled single-page application artifact. This introduces divergence risk between test assertions and real browser execution.

---

## Solution

1. **Dynamic Track Directory Mapping**:
   Eliminate all hardcoded `'problems/'` string literals in client-side routing. Legacy route resolution must dynamically replace the matched track identifier prefix (`${track.id}/`) with the track's canonical directory path (`${track.dir_path}/`) derived strictly from the compiler-injected track configuration.

2. **Architectural Router Delegation to Entity Reference Resolver**:
   Consolidate URL hash initialization and route handling by delegating path resolution directly to the `EntityReferenceResolver`. When the application initializes or the URL hash changes, the router queries the resolver to normalize the path, perform dynamic legacy track translation, handle `.md` to `.py` problem source alignment, and return target keys through a single cohesive pipeline.

3. **Elimination of Dead Code and Strict Key Normalization**:
   Remove all dead reverse `.py` $\rightarrow$ `.md` entity lookups from the client runtime. Constrain problem entity resolution strictly to canonical `.py` problem keys and static markdown documentation (overview and problem index topics).

4. **Single High-Seam Behavioral Testing**:
   Unify test coverage at the highest architectural seam: extracting and executing the actual production router and resolution functions from the compiled single-page application artifact via Node.js, ensuring zero test harness duplication and verifying dynamic track directory translation against real and synthetic fixtures.

---

## User Stories

1. As a learner following an external link or bookmark formatted with a legacy track prefix, I want the client router to seamlessly redirect to the canonical problem entity without manual URL modification, so that my study session is uninterrupted.
2. As a platform maintainer configuring a problem track with an arbitrary directory path, I want the client router to resolve legacy routes using the configured directory attribute rather than a hardcoded folder prefix, so that track restructuring does not break URL resolution.
3. As a developer maintaining the client application runtime, I want URL hash initialization to delegate directly to the domain entity reference resolver, so that routing logic is centralized in one authoritative location.
4. As a code reviewer inspecting future frontend changes, I want zero duplicated route resolution branches in the client script, so that the codebase remains free of divergent change smells.
5. As a software architect, I want dead extension swapping branches removed from entity lookup, so that the client bundle honors YAGNI and avoids unreachable conditional execution.
6. As a learner clicking markdown cross-references between companion notes, I want `.md` problem links to resolve deterministically to their corresponding `.py` problem entities, so that companion walkthroughs load instantly in Notes-First view.
7. As a QA engineer running automated test suites, I want compiler integration tests to execute the actual production client resolution routines extracted from the compiled artifact, so that tests verify true browser runtime behavior.
8. As a test engineer, I want the test harness to avoid synthetic reimplementations of routing functions, so that tests never suffer from implementation drift against production scripts.
9. As a documentation author linking to curriculum topics and problem index catalogs, I want non-problem markdown files to resolve cleanly without unexpected extension stripping, so that documentation navigation remains reliable.
10. As a mobile learner using in-app anchor links, I want hash route changes to extract and preserve anchor targets during entity resolution, so that deep page scrolling remains accurate.
11. As an AI assistant authoring compiler and client updates, I want unambiguous domain interfaces with zero hardcoded track assumptions, so that future refactoring adheres to repository standards.
12. As a repository contributor, I want all route resolution behavior protected by automated high-seam tests, so that regressions in link handling are caught before merging to main.

---

## Implementation Decisions

### 1. Dynamic Directory Prefix Replacement
- In the client entity reference resolution engine, legacy track prefix handling will match the configured track identifier followed by a slash.
- When a match is detected, the resolver will strip the track identifier prefix and prepend the track's configured directory path property, dynamically constructing the canonical candidate path.
- Hardcoded directory string literals representing container directories will be completely eliminated from the client runtime.

### 2. Startup Hash Router Delegation
- The startup hash routing cascade will be streamlined to delegate entity resolution directly to the entity reference resolver.
- The router will evaluate special navigation commands (such as the interactive roadmap view), and for all entity references, pass the decoded hash string to the entity reference resolver.
- If the resolver identifies a valid entity key present in the compiled dataset, the application will activate that entity and enter the workspace mode. If an anchor is present in the hash, it will be preserved for DOM scrolling.
- This eliminates duplicated path checking, duplicate track iteration, and redundant regex operations in the startup script.

### 3. Key Normalization and Dead Code Removal
- Remove all conditional checks attempting to swap `.py` extensions to `.md` against the problem items collection, as problem entities are indexed exclusively by `.py` paths.
- Preserve unidirectional `.md` to `.py` normalization when resolving problem references, ensuring that companion note links seamlessly target their paired problem entity.
- Preserve exact key matching for non-problem entities, such as the overview document and curriculum topic catalogs.

### 4. High-Seam Test Harness Consolidation
- Refactor compiler integration tests to extract the production route resolution functions directly from the compiled HTML artifact using regular expressions.
- Execute the extracted production functions within a Node.js runtime environment against synthetic and production fixtures, verifying:
  - Dynamic canonical path resolution from legacy track prefixes with non-standard directory structures.
  - Correct delegation of hash routing to the entity reference resolver.
  - Handling of `.md` to `.py` extension normalization for problem links.
  - Preservation of static document paths without unintended modification.
- Eliminate synthetic duplicated routing functions in the test file.

---

## Testing Decisions

### What Makes a Good Test
- Tests must assert external observable behavior at the highest possible architectural seam rather than verifying internal helper variables or private implementation mechanics.
- Tests must evaluate the exact compiled script artifact generated by the compiler to prevent divergence between source templates, build outputs, and test expectations.
- Tests must verify both positive resolution paths and negative boundary cases (such as unmatched routes or cross-track prefix collisions).

### Modules Tested
- **Client Application Runtime**: Evaluated via headless Node.js execution on the compiled single-page application artifact.
- **StudyStationCompiler**: Integration tests in the compiler test suite verifying that compiled output contains zero hardcoded directory literals and clean runtime functions.

### Prior Art
- Existing high-seam tests in `tests/test_update_index.py` that extract compiled script blocks and assert runtime behavior via Node.js subprocesses.

---

## Out of Scope

- Modifying original Python problem solutions (`problems/**/*.py`), which remain strictly immutable per Core Rule 1.
- Modifying the centralized track registry schema or Python dataclasses, which were already streamlined in Spec 16.
- Altering the visual design, theme colors, or CSS layout of the single-page application.
- Introducing external client-side routing libraries or Node.js runtime dependencies into the production bundle.

---

## Further Notes

- This specification completes the architectural refinement initiated in Spec 15 and Spec 16, fully closing the remaining code smells identified during post-implementation review.
- Aligns with `CONTEXT.md` Architectural Seam 7 (*Zero-Download In-App Navigation & Notes-First Routing*) and Seam 1 (*Depth over Shallowness*).
- All changes remain 100% backward-compatible with existing URLs, external bookmarks, and internal documentation links.
