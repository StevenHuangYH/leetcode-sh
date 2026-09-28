# Issue tracker: GitHub

Issues and new specs live in [GitHub Issues](https://github.com/StevenHuangYH/leetcode-sh/issues). Use the `gh` CLI from this clone; outside it, pass `--repo StevenHuangYH/leetcode-sh`.

## Conventions

- Create an issue: `gh issue create --title "..." --body-file <path>`.
- Read an issue: `gh issue view <number> --comments`. For structured requirements, labels, and comments, use `gh issue view <number> --json number,title,body,labels,comments,url`.
- List issues: `gh issue list --state open --limit 100 --json number,title,body,labels,comments`. Use `--label` and `--state` to narrow the queue; raise the limit or paginate when completeness matters.
- Comment: `gh issue comment <number> --body-file <path>`.
- Update an issue body: `gh issue edit <number> --body-file <path>`.
- Apply or remove labels: `gh issue edit <number> --add-label "..."` or `--remove-label "..."`. Resolve canonical triage roles through [triage-labels.md](triage-labels.md).
- Close an issue: `gh issue close <number>`. Post any resolution comment first.

Write multiline bodies to UTF-8 files and pass `--body-file` to preserve formatting and avoid shell interpolation.

## Spec lookup and publication

When a skill says "publish to the issue tracker", create a GitHub issue. When it says "fetch the relevant ticket", read the issue body, labels, and comments with the commands above.

GitHub issues and PRs share a number space. For an ambiguous commit reference such as `#42`, try `gh pr view 42 --json number,title,body,labels,comments,url`; if it is an issue, use `gh issue view 42` instead. Report authentication or network failures separately from a missing reference.

Historical local specs remain under `docs/archive/specs/`. When commits have no issue reference, look there for a matching feature before asking for its spec.

## Pull requests as a triage surface

**PRs as a request surface: no.**

Set this flag to `yes` if external PRs should enter the triage queue. When enabled, use `gh pr` equivalents and include only external authors with association `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE`. This flag does not prevent reading PRs to find review requirements.

## Wayfinding operations

- Keep the map in one issue labelled `wayfinder:map`, with Notes, Decisions-so-far, and Fog sections.
- Link child tickets through GitHub sub-issues; if unavailable, use a task list in the map and `Part of #<map>` in each child. Use `wayfinder:<type>` labels for research, prototype, grilling, and task tickets.
- Record blockers with native issue dependencies. Add an edge using `gh api --method POST repos/StevenHuangYH/leetcode-sh/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`. Obtain the database ID with `gh api repos/StevenHuangYH/leetcode-sh/issues/<blocker> --jq .id`.
- If dependencies are unavailable, record `Blocked by: #<n>, #<n>` at the top of the child body. A ticket is unblocked when all blockers are closed.
- Select the first open, unassigned child in map order with no open blockers. Claim it with `gh issue edit <number> --add-assignee @me`.
- Resolve by posting the answer, closing the child, and adding a short decision plus its issue link to the map.
