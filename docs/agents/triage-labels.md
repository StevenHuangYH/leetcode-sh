# Triage labels

Map canonical skill roles to these GitHub labels:

| Canonical role | Tracker label | Meaning |
| --- | --- | --- |
| `needs-triage` | `needs-triage` | Maintainer needs to evaluate the issue |
| `needs-info` | `needs-info` | Waiting on the reporter for more information |
| `ready-for-agent` | `ready-for-agent` | Fully specified and ready for an agent |
| `ready-for-human` | `ready-for-human` | Requires human implementation |
| `wontfix` | `wontfix` | Will not be actioned |

Before applying a label, check `gh label list --limit 100`. Create missing labels when running an authorized triage workflow; preserve existing labels. Edit the tracker-label column if the repository adopts different names.
