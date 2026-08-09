---
name: session-summary
description: How to summarise a working session at a high level — what was achieved and what remains, as themed bullets with sub-bullets, splitting open items into blocked-on-the-user versus future backlog. WHEN asked to summarise or recap what was done in a session, wrap up a piece of work, hand off to someone else, or report progress at a high level.
kind: procedure
guardrails:
- never claim an outcome that was not verified in the session; if a step was skipped or failed, it belongs in an open section, not a hedge
- report artifacts by their real identifiers — PR numbers, commit hashes, file paths — never "the PR" or "the changes"
definition_of_done:
- every achieved bullet states an outcome, not an activity
- every open item sits in exactly one of the two open sections
- nothing done in the session is silently omitted from either list
---

# Session Summary

## Structure

Three top-level sections, in this order:

```markdown
**Achieved**

- **Workstream name**
  - Outcome with its artifact (PR #, commit, path, URL)
  - Outcome
- **Another workstream**
  - Outcome

**Open — needs you**

- Action only the user can take (merge, rotate, log in, decide)

**Open — future work**

- **Grouping where helpful**
  - Known gap or natural next step nobody owns yet
```

## Rules

1. **Group by workstream, not chronology.** The reader wants what happened to each
   thread of work, not the order events occurred.
2. **Outcomes, not activities.** "Built the parser skill" earns a bullet; "explored the
   codebase" does not — unless the finding was the deliverable, in which case state the
   finding.
3. **Every bullet carries its artifact.** A merged change names its commit; an open
   change names its PR; a new file names its path. The summary is a map back to the work.
4. **Split the open items by owner.** "Needs you" holds only actions the user must take
   themselves — merges, credentials, decisions. Everything else — known gaps, deferred
   fixes, natural next steps — is "future work". A reader scans "needs you" as a to-do
   list; mixing in backlog buries it.
5. **Be honest in the open sections.** Skipped steps, failed attempts and discovered
   risks are outcomes of the session too. Name them plainly; the achieved list earns
   trust only if the open list is complete.
6. **Two levels maximum.** Bold theme headers, one level of sub-bullets. If a theme needs
   a third level, it is two themes.
7. **Scale to the session.** A short session may not need themed groupings or the
   future-work section; keep the achieved/needs-you split always.

Prose inside bullets follows the writing-style skill: specific, positive form, no filler.
