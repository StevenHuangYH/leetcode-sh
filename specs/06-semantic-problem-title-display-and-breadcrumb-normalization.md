# Spec 06: Semantic Problem Title Display and Breadcrumb Normalization

## Problem Statement

Users navigating problems in the LeetCode Study Station frequently encounter raw filesystem artifacts (e.g. `lc-0153-find-minimum-in-rotated-sorted-array.py`, `01-lc-2235-add-two-integers`, `topic-01-arrays-sliding-window`) in prominent UI surfaces such as the top breadcrumb bar and navigation components. Displaying disk filenames instead of cleanly formatted, bilingual problem titles creates cognitive friction, obscures problem identities, and distracts learners from algorithmic problem solving.

Furthermore, batch curriculum problems with numeric prefixes (such as `luffy/01-lc-2235-add-two-integers.py` or `10-oop-pre-main-practice.py`) fail to strip file-ordering prefixes during metadata aggregation, resulting in mangled titles like `01 Lc 2235 Add Two Integers` rather than standard LeetCode identifiers (`LC 2235 · Add Two Integers`).

## Solution

1. **ProblemTitleFormatter Normalization Engine**: Implement a robust title parsing and normalization engine in the compiler pipeline that strips raw disk prefixes (such as `\d{2}-lc-\d{4}-`, `lc-\d{4}-`, `\d{2}-`), extracts LeetCode problem numbers, and formats standard bilingual titles (`LC {num} · {English Title} ({Chinese Title})`).
2. **Semantic Top Breadcrumb**: Upgrade the top navigation breadcrumb to render clean, semantic folder and problem titles (`Category / LC {num} · {English Title} ({Chinese Title})` or `Curriculum / 1. Arrays, Strings & Sliding Window`) rather than filesystem paths.
3. **Graceful Overflow & Tooltip Protection**: Apply CSS ellipsis truncation (`text-overflow: ellipsis`) to the breadcrumb container to maintain a rigid, compact toolbar height (46px) across all viewports, while retaining the full bilingual title in the HTML `title` attribute for instant hover tooltips.
4. **Fallback & Tutorial Title Synthesis**: Ensure tutorial files without LeetCode numbers (e.g. `10-oop-pre-main-practice.py`) and problems with only `.py` source files synthesize clean, title-cased names (e.g. `OOP Pre Main Practice`).

## User Stories

1. As a learner viewing a problem note, I want the top breadcrumb to display the clean bilingual title (e.g. `Daily Practice / LC 153 · Find Minimum in Rotated Sorted Array (寻找旋转排序数组中的最小值)`), so that I immediately understand the problem context without deciphering a filename.
2. As a user studying curriculum problems in the `luffy/` track, I want batch numbers like `01-lc-2235-` cleaned into standard `LC 2235 · Add Two Integers`, so that the curriculum track looks unified with standard problem tracks.
3. As a user inspecting non-LC tutorial scripts (such as OOP practices or prefix sum examples), I want the title to be neatly formatted (e.g. `OOP Pre Main Practice`), so that non-LC exercises are readable and professional.
4. As a user on a laptop or split screen with limited horizontal space, I want long bilingual titles in the breadcrumb to truncate cleanly with an ellipsis rather than wrapping and breaking the top toolbar height.
5. As a learner using a desktop browser, I want to hover over a truncated breadcrumb to view the full English and Chinese title in a native tooltip.
6. As a student browsing curriculum index topics, I want the breadcrumb to show `Curriculum / 1. Arrays, Strings & Sliding Window` rather than `Problem Index / topic-01-arrays-sliding-window`.
7. As a learner opening the project overview, I want the breadcrumb to read `Overview / LeetCode Self-Practices Overview` rather than `Overview / README.md`.
8. As an AI assistant generating or auditing companion notes, I want title formatting to be automated in `StudyStationCompiler`, ensuring zero manual title sync overhead across markdown files.
9. As a developer running regression tests, I want automated unit tests to verify title parsing rules across `top-100/`, `daily-practice/`, `luffy/`, and `problem-index/`.
10. As a contributor, I want original `.py` filenames on disk to remain strictly immutable while the UI displays clean semantic titles.

## Implementation Decisions

### 1. Title Parsing & Normalization (`ProblemTitleFormatter`)
* In the document collector pipeline:
  * For LeetCode problems matching `(?:lc-)?(\d{4})` or `\d{2}-lc-(\d{4})`: extract standard problem number `LC {int(num)}` and clean slug.
  * Strip all prefix variants: `^lc-\d{4}-`, `^\d{2}-lc-\d{4}-`, `^\d{2}-`.
  * Convert clean slug to title-cased English title: `raw_slug.replace("-", " ").title()`.
  * Extract Chinese title from Markdown H1 header (`# LC ... | {Chinese Title}`).
  * Construct primary title:
    * If both English and Chinese exist: `LC {num} · {English Title} ({Chinese Title})`.
    * If only English exists: `LC {num} · {English Title}`.
    * If neither exists: clean slug title.
  * For non-LC files (e.g. `10-oop-pre-main-practice`): strip `^\d{2}-`, format as `OOP Pre Main Practice`.

### 2. Breadcrumb Rendering & Dynamic Updates
* Breadcrumb template in JavaScript:
  ```html
  <span class="breadcrumb-folder">${folderLabel}</span>
  <span class="breadcrumb-sep">/</span>
  <span class="breadcrumb-file" title="${item.title}">${item.title}</span>
  ${diffBadgeHtml}
  ```
* Top breadcrumb container styles:
  * `overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 100%;`
  * `.breadcrumb-file`: `overflow: hidden; text-overflow: ellipsis; white-space: nowrap;`

### 3. Curriculum & Overview Title Mapping
* `README.md` maps to title `LeetCode Self-Practices Overview`.
* `topic-01` through `topic-11` map to clean topic names (e.g. `1. Arrays, Strings & Sliding Window`).

## Testing Decisions

### Good Test Principles
* Test external document entity contracts and HTML output representations rather than internal regex strings.
* Test diverse filename patterns across all three tracks (`top-100`, `daily-practice`, `luffy`).

### Modules Tested
* `StudyStationCompiler.collector` (`tests/test_update_index.py` & `tests/test_preview_and_generator.py`)
* Curriculum topic parser (`scripts/compiler/parser.py`)

### Prior Art
* Existing test suites in `tests/test_update_index.py` validating curriculum document entity generation.

## Out of Scope

* Renaming `.py` or `.md` source files on the local filesystem (immutable per Core Rule 1).
* Changing problem difficulty rating schemas or tags.
* Modifying algorithm topology graph node connectivity.

## Further Notes

* Documented in `CONTEXT.md` under `ProblemTitleFormatter` and Principle 6 (*Semantic Breadcrumb & Bilingual Title Normalization*).
