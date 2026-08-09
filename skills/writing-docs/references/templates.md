# Templates

Copy the skeleton for the doc type, replace the `[bracketed]` slots, delete sections that do not apply.

## Tutorial

```markdown
# Build [a concrete thing] with [tool]

## What you'll build
[1-2 sentences describing the end result — what they build, not what they "learn"]

## Before you begin
- [Prerequisite, with link — do not explain it here]
**Time**: [estimate]

## Step 1: [Action verb + what this step accomplishes]
[1 sentence of context]
[code]
You should see:
[exact expected output — every step produces a visible result]

## Step N: [...]
[same pattern]

## What you've built
[What now works, and the skills used along the way]

## Next steps
- [Link to how-to, explanation and reference docs]
```

## How-to guide

```markdown
# How to [accomplish specific goal]

[1 sentence: what this does and when you'd need it]

## Prerequisites
- [What must already be in place]

## Steps
### 1. [Action step]
[instruction + code]
### N. [...]

## Verify
[Command or check that confirms it worked, with expected output]

## Related
- [Links to reference, troubleshooting, adjacent guides]
```

## Reference page

```markdown
# [Component / command / endpoint name]

[1 sentence: what it does — describe, never instruct or recommend]

## Parameters / Options
| Name | Type | Required | Default | Description |
| [name] | [type] | [yes/no] | [default] | [constraints, valid values] |

## Example
[complete request or invocation with realistic values]
[example response or output]

## Errors
| Code | Meaning | Fix |
```

## Explanation

```markdown
# Understanding [concept]

## Overview
[2-3 sentences: why this matters and what the reader will understand]

## [Core concept]
[Discuss with examples and analogies — no steps, no parameter listings]

## Design decisions
[What was chosen and why; "Why not [alternative]?" with the reasoning]

## Trade-offs
| Choice | Benefit | Cost |

## Further reading
- [Related explanation, how-to for practical application]
```

## README

```markdown
# [Project name]

[1-2 sentences: what this is and who it's for]

## Quickstart
[Shortest path to a working result — install, configure, run, expected output]

## Usage
[The most common operations, each with a real example]

## Configuration
[Table of the options that matter, or link to the full reference]

## Docs
- [Links to tutorials, how-tos, architecture docs]

## Contributing / License
[Link or one line each]
```

## Runbook

```markdown
# [Service] runbook

**Owner**: [team] | **Last verified**: [date] | **Escalation**: [contact/channel]

## Access
| System | How to access |
| [dashboard / logs / metrics] | [URL + instructions] |

## Scenarios
### [Symptom: what you observe]
**Impact**: [what's affected]
**Resolution**:
1. [Exact command]
2. [Verification step with expected output]
**Escalation**: If unresolved after [time], escalate to [who].

## Post-incident
- [ ] Update this runbook with what you learned
```

## ADR / decision note

```markdown
# ADR-[number]: [Decision title]

**Status**: [Proposed | Accepted | Superseded by ADR-X] | **Date**: [date]

## Context
[The situation forcing a decision — the problem, not the solution]

## Decision
[What was decided, in one or two sentences]

## Consequences
- [What gets better]
- [What gets worse or harder]

## Alternatives considered
- [Alternative]: [why rejected]
```

---

Adapted from anivar/developer-docs-framework (MIT) and Xamfonos/technical-writing-best-practices (MIT); Diataxis by Daniele Procida (diataxis.fr).
