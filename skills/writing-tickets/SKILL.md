---
name: writing-tickets
description: How to write and refine a Jira epic or story — the Context/Outcomes/Scope/Acceptance-criteria structure, stating business value honestly, the epic-versus-story split, and the challenges to raise against a weak draft. WHEN drafting, reviewing or refining the wording of a Jira epic or story, or turning a request into ticket text.
kind: procedure
inputs:
- a request, problem statement or draft ticket
- the requester, available to answer questions
outputs:
- a story with Context, Outcomes, In scope, Out of scope, Acceptance criteria, Notes
- or an epic with Context, Outcomes, In scope, Out of scope, Condition of satisfaction, Notes
- a list of challenges raised and how they were resolved
guardrails:
- never put an outcome in the ticket that the requester did not state or confirm.
  proposing a candidate outcome in conversation is expected; writing it in is not
- mark every proposal as a proposal until the requester confirms it
- an outcome that fails the opposite test is rewritten, not softened
- render the complete ticket on screen and obtain approval before creating or editing
  anything in Jira. a summary of changes is not the ticket
- show the exact command that will run, and wait, before running it
definition_of_done:
- every gate 1 check passes (see Validation); gate 2 cold read is run for epics and
  large stories
- blocking challenges are resolved or consciously accepted by the requester
- the full ticket was rendered and approved before anything was written to Jira
---

# Writing Tickets

## Overview

Turn a request into an epic or story someone can pick up months later without asking a
question. This is not a form to fill in. Your job is to draw the real outcome out of
the requester, propose what they have not thought of, and challenge what does not hold
up. A ticket that passes the template but states nothing checkable is a failure.

## When to use

Writing a new epic or story; improving someone else's draft; turning a conversation,
bug report or message into tracked work; splitting an item that is too big.

For creating the item in Jira once written, use the `acli-jira` skill.

## Repo context

Atlassian details for a repository live in `.atlassian.yaml` at its root. Read it before
naming a project key or writing about the organisation. Never hardcode a project key, site
URL or organisation name in this skill or in your working notes.

Look in the repository root only — `git rev-parse --show-toplevel` when inside a git
repository, otherwise the current directory. Do not search parent directories.

**Present.** Use its values: `jira_base_url` as the site, `default_project` for a new item
unless the requester names another, `projects[].use_for` to choose between projects, and
`organisation` wherever this skill's text says "the organisation". Where two projects could
both fit, ask rather than guess.

**Absent.** Say the repository has no `.atlassian.yaml`, then ask for the project key and
site URL and work from the answers for the rest of the session. Offer once to write the
file. Never write it unasked, and never in a repository that has nothing to do with
Atlassian. Schema and scaffold: [../acli-jira/ATLASSIAN-YAML.md](../acli-jira/ATLASSIAN-YAML.md).

**Malformed or incomplete.** Name the key that is missing or would not parse, then continue
as though the file were absent. Do not repair it silently.

Where these templates say "the organisation", use the `organisation` value from
`.atlassian.yaml` when the repository has one.

## Structure

Two canonical schemas. Use these section names exactly.

| Section | Epic | Story |
| --- | --- | --- |
| Context | The situation and why it needs to change | The same, narrowed to this slice |
| Outcomes | What changes for whom, and why it matters | Same, smaller claim |
| Expected state at the end of this epic | Only when the epic deliberately stops short of the full ambition | Not used |
| In scope | Broad areas of work | Specific work items |
| Out of scope | What this explicitly does not cover | What this leaves to others |
| Condition of satisfaction | Required. One paragraph: what must be true to close | Not used |
| Acceptance criteria | Not used | Required. Specific and checkable |
| Notes | References, provenance, decisions taken | Same |

Where this skill says "acceptance criteria" unqualified, read it as "criteria for a
story, condition of satisfaction for an epic".

The Jira summary is a field, not a body section. Rules for it are in WRITING-RULES.md.

**Value is not a separate section.** It lives inside Outcomes. An outcome that does not
say why anyone should care is not finished.

Templates and worked examples: [TEMPLATES.md](TEMPLATES.md)
Plain-language and vocabulary rules: [WRITING-RULES.md](WRITING-RULES.md)

## Epic or story

An epic is not a large story. The test is **combined effect**: an epic describes a
change no single story within it delivers alone. If one story could deliver the epic's
outcome, it was never an epic.

An epic must be closeable. If you cannot write "after this epic, [someone] can [do
something they cannot today]", it is a bucket and will never close.

Epics lean to business outcomes; stories balance outcomes with actionable detail and
testable criteria. Both always carry Context.

## The loop

1. **Read what you were given.** Do not start drafting.
2. **Ask before assuming.** Smallest number of questions that gets a real outcome,
   usually two or three.
3. **Draft, marking inferences** — "I have assumed X, confirm or correct".
4. **Challenge your own draft**, not just what you were given.
5. **Raise blocking challenges** before proceeding. Lower tiers: state once, move on.
6. **Validate.** Do not skip because the draft feels good.
7. **Render the full ticket and get approval.** Not a summary, not a diff.
8. **Show the command, then run it.** Only after both approvals.

A small story may collapse steps 2 and 5 into one question. An epic needs a real
conversation. Do not turn a five-minute ticket into an interrogation.

## Elicitation questions

Highest-yield first.

1. "If this works, who is better off, and what can they do that they cannot today?"
2. "What happens if we do not do this?" — surfaces real cost, sometimes reveals the
   work is not worth doing.
3. "How would we know it worked?" — produces criteria directly.
4. "What is deliberately not included?" — fastest defence against scope creep.
5. "Who has to be told, or change what they do, for this to land?"
6. "What do you already know will be awkward?"

When the requester describes a solution, ask what problem it solves before accepting it.

## Context

Open in business terms. Someone outside the delivery team should understand the first
paragraph without knowing the codebase.

Order: **what the business has or needs → what is wrong today → what this ticket does
→ technical detail.** Technical vocabulary is not banned, it just cannot go first.
Repository names, paths, libraries and tool names belong later, or in Notes.

| Opens badly | Opens well |
| --- | --- |
| "The reporting toolchain — packages/extractor plus its four reader libraries — lives in a single workspace venv." | "The organisation has one reliable record of how its systems connect, and it exists only inside a proof of concept." |
| "Replace the Jenkins freestyle job with a reusable workflow." | "Releases currently need a named individual to run them by hand." |

Two checks: could a stakeholder outside the team say what problem is being solved from
the opening? Does the first sentence name a system, path or tool? If so, it starts too
deep.

**Say how you know.** A reader outside the team cannot tell whether your stated facts
are true, so they can only accept them. Where a claim carries real weight, say what it
rests on.

| Bare assertion | With its basis |
| --- | --- |
| "AI coding agents get its commands wrong." | "Two public guides were checked against the version we run; both contained commands that do not work." |
| "The service catalogue is unreliable." | "Three of its twelve entries name owners who have left, and nothing refreshes it automatically." |

Not every sentence — that makes Context unreadable. Do it for the claims the
justification rests on. If you cannot say how you know, discover that before raising
the ticket.

## Outcomes

Each outcome names **who** is better off and **what observably changes**. Not every
outcome can carry a number; demanding one produces invented numbers. Identify the tier
and apply its discipline.

| Tier | Description | Required |
| --- | --- | --- |
| Measurable | A number checkable in normal operations | State the number and the baseline |
| Observable | A specific event you would witness | "We will know this is achieved when …" |
| Arguable | A reasoning chain, not observable in this timescale | Say "we believe", name a leading indicator |

Most enablement work — tooling, CI, extraction, ways of working — is Tier 3. That is
legitimate. Making it legitimate is what stops people faking Tier 1.

For indirect value, show the chain rather than asserting the benefit:

> This enables [actor] to [changed behaviour], which removes [specific friction],
> which matters because [organisational reason].

If the chain does not hold when written out, the benefit is overstated. Say so.

Sentence patterns: [TEMPLATES.md](TEMPLATES.md).

## Acceptance criteria

A criterion is checkable by someone who was not in the conversation. Prefer a
declarative checklist; use Given/When/Then only where behaviour genuinely depends on a
starting state.

At least one criterion must test the **stated outcome**, not just delivery. "The file
exists" proves a file exists, not that anyone is better off.

Ban criteria depending on unrecorded opinion — "the team agrees it is good" — and
hedges that cannot fail: "appropriate", "reasonable", "properly", "as needed".

**One criterion tests one thing.** Do not combine a format check and an outcome test;
when it fails you will not know which half failed.

**Do not restate scope.** If a criterion repeats something in In scope, delete it.
Scope says what we will build; criteria say how we know it worked. "The plugin exists
at `path/x/`" tests a decision already recorded, and turns a design choice into a
contract you must renegotiate to change.

**Write criteria as if agreed before the work started.** Ask: *would we have agreed
this before we knew how we would build it?* If it could only have been written after
seeing the solution, it describes the implementation. Rewrite it as the requirement the
implementation was chosen to satisfy.

| Retrospective | Agreed in advance |
| --- | --- |
| "The reference records the tool version it was generated against" | "A reader can tell whether the guidance has gone out of date" |
| "Creates an ADF-formatted work item" | "The ticket renders readably in Jira — headings and lists, not flat text" |
| "An agent can do X without consulting `--help`" | "An agent creates the item without having to correct the commands" |

**Keep criteria readable by someone outside the build.** Expand an abbreviation on
first use or keep it out. Tool names, formats and version numbers usually belong in
Notes.

Judge jargon against the *intended audience*, not a general reader. Terms the team and
its stakeholders use daily — the company name, the tracker, the database, the domain
products — are not jargon, and expanding them makes the ticket worse. The test: would a
competent colleague on an adjacent team know it? Build-specific abbreviations, internal
nicknames and tool flags fail; established domain vocabulary does not.

## Challenges

Raise these against any draft, including your own. Tiers matter: a skill that
challenges everything gets ignored.

- **Blocking** — do not proceed until resolved or consciously accepted.
- **Should address** — raise once, accept the answer, move on.
- **Informational** — mention, do not press.

| Signal | Tier | Challenge |
| --- | --- | --- |
| Outcome restates the title or the work | Blocking | "This restates what will be built, not what changes for someone. Complete: 'After this work, [someone] can [do what they cannot today].'" |
| Unfalsifiable phrase — "improves productivity", "increases agility", "reduces technical debt" | Blocking | "'[phrase]' is not checkable. What would a person notice, or what number would move?" |
| Story with no criteria, or epic with no condition of satisfaction | Blocking | "There is no definition of done. What checkable conditions confirm this is complete?" |
| Criteria could all pass while the outcome is unachieved | Blocking | "If every criterion passed, would we know '[outcome]' had happened? What would confirm the outcome itself?" |
| A story spanning more than one sprint, or several distinct capabilities | Blocking | "This looks like more than one story. Which thin slice delivers value alone? That becomes the first; the rest become siblings." |
| Context references a meeting, decision or fact not explained | Blocking | "This assumes context the reader will not have. Add two sentences summarising it." |
| Criteria restate scope or read as a task list | Blocking | "These list what we will build, which In scope already records. What would we check to know it worked? Rewrite at least one as an outcome test." |
| Criterion could only have been written after seeing the solution | Should address | "Would we have agreed this before we knew how we were building it? If not, state the requirement and move the detail to Notes." |
| Unexplained abbreviation or tool name in a criterion | Should address | "A reviewer outside the build will not know '[term]'. Expand on first use or move to Notes." |
| Context opens with technical detail | Should address | "The opening names [system/path/tool] before the business problem. Lead with what the organisation has or needs and what is wrong with it today." |
| No named beneficiary | Should address | "Who specifically is better off — which team or role? Naming them makes the outcome checkable." |
| Out of scope empty despite adjacent concerns | Should address | "Nothing is excluded. Given this touches [area], is that in or out? One exclusion prevents drift." |
| Business benefit claimed for enabling work, chain not shown | Should address | "The link between [deliverable] and [benefit] is not shown. Fill in: enables [actor] to [behaviour], removing [friction], which matters because [reason]." |
| OKR linkage names an objective, not a key result | Informational | "Objectives are directions; key results are measurable. Which key result does this move?" |
| Arguable outcome with no stated confidence | Informational | "This relies on reasoning rather than observation. Add 'we believe' and name the leading indicator." |

## Validation

Gate 1 every time. Gate 2 for epics, stories with more than about five criteria, and
anything contentious.

### Gate 1 — mechanical, always, do it yourself

Deterministic, so dispatching an agent is slower and adds nothing.

- [ ] Sections present and named exactly as the two schemas define.
- [ ] Correct closing section for the type — criteria on a story, condition of
      satisfaction on an epic. Never both.
- [ ] Context opens with the business situation, not a system, path or tool.
- [ ] Every outcome names who is better off and what observably changes.
- [ ] Every outcome passes the opposite test.
- [ ] No banned vocabulary in Outcomes or criteria.
- [ ] Out of scope states at least one explicit exclusion.
- [ ] Every blocking challenge resolved or consciously accepted, and recorded.

Stories also: no criterion restates In scope; one criterion tests one thing; at least
one tests the outcome rather than delivery.

### Gate 2 — cold read, by subagent

Run for epics, stories with more than about five criteria, and anything contentious.
Two subagents in parallel: one reads the ticket cold, one audits it against this skill.

Full procedure and prompts: [VALIDATION.md](VALIDATION.md)

## Approval before Jira

Nothing reaches Jira until the requester has seen it in full and said yes. Two separate
approvals: the content, then the command.

**Render the ticket in full.** Every section, formatted as it will appear. Then stop.

- A summary is not the ticket. "I tightened the outcomes" tells the requester nothing
  they can check. Nobody can approve wording they have not read.
- For an edit, show the whole new version, not a diff — a ticket is judged as a whole,
  and a diff hides a section that now contradicts one you did not touch.
- Reworking several tickets means rendering each in full, not one batched summary.
- If the text is long, render it anyway. Length is not a reason to approve unseen.

**Then show the command.** State exactly what will run and what it changes, naming
every work item key. Prefer explicit keys over JQL; where JQL is unavoidable, run the
search first and show what matched. Say what is *not* changing — status, assignee,
parent, summary — so an unintended edit is visible. Then wait; do not run it in the
same turn as proposing it.

**Not approval:** approval of a summary when the full text was never shown; silence or
moving on; approval of an earlier version when content has changed since; your own
judgement that the change is small.

## Suggesting without inventing

You are expected to propose — candidate outcomes, likely criteria, obvious exclusions,
risks not mentioned. You may not invent requirements and present them as the
requester's.

- Mark proposals "Proposed — confirm or correct", once at the top of the unconfirmed
  section, not on every bullet. Remove the marker on confirmation; anything still
  unconfirmed at Jira time belongs in Notes as an open question.
- State the inference: "You said X, so I assumed Y."
- A blank Outcomes section with a question beats a fabricated one.
- Where you are guessing at scope, say which parts you are least sure about.

## Do not agree by default

Agreement is not helpfulness. When a draft is weak, say what is wrong and why before
offering a fix.

- Do not open with praise. Open with the problem.
- If the requester rejects a blocking challenge, record the decision in Notes rather
  than silently dropping it.
- If you cannot find anything wrong, say so plainly. Do not invent a challenge to
  appear rigorous.
- If a proposed outcome fails the opposite test, softening the wording is not a fix.
  Say it carries no information and ask for the real one.
