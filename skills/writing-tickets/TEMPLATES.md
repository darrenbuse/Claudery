# Ticket templates and worked examples

Companion to [SKILL.md](SKILL.md). Copy a template, then apply the challenges.

Where these templates say "the organisation", use the `organisation` value from the
repository's `.atlassian.yaml` when it has one.

---

## Epic template

```markdown
## Context

[Open in business terms. First paragraph: what the organisation has or needs, and what is wrong
with that today. A stakeholder outside the delivery team must understand it without
knowing the codebase. Do not open with a repository, module path or tool name.

Then the specific, checkable facts — not "things are inconsistent" but what is
inconsistent and where. Technical detail goes in these later paragraphs, not the
first. Someone reading this in six months, who was in none of the conversations, must
understand why this epic exists.]

## Outcomes

[3-5 outcomes. Each names who is better off and what observably changes. Value lives
here — an outcome that does not say why anyone should care is not finished. Use the
sentence patterns below.]

## Expected state at the end of this epic

[Optional but recommended. What is deliberately still rough. Epics that promise a
finished product tend not to close. State what follow-on work is expected.]

## In scope

[The broad areas of work. Not a task list — that is what the stories are for.]

## Out of scope

[What this epic explicitly does not cover, especially the adjacent things a reader
would reasonably assume were included.]

## Condition of satisfaction

[One sentence describing what is true when this epic is done, in the form: "After
this epic, [who] can [what], which they cannot do today." If you cannot write it,
this is a bucket, not an epic, and it will not close.]

## Notes

[References, standards being followed, provenance, decisions taken and why.
Once OKRs are in place, name the specific key result this epic moves.]
```

An epic does not need acceptance criteria. It needs a **condition of satisfaction**:
one sentence describing what is true when it is done. If you cannot write it, the
epic is a bucket and will not close.

---

## Story template

```markdown
## Context

[The situation, narrowed to this slice. Still opens in business terms — a story is
read by the same people as the epic. If this story sits under an epic, do not repeat
the epic: say what is specific to this piece and why it is being done now. Technical
detail follows the business framing rather than leading it.]

## Outcomes

[2-3 outcomes. Smaller claims than the epic's. Still name who is better off.]

## In scope

[The specific work. Concrete enough that someone could start.]

## Out of scope

[At least one explicit exclusion. If nothing is excluded, the scope is not yet
understood.]

## Acceptance criteria

[Numbered. Each checkable by someone who was not in the conversation. At least one
must test the stated outcome, not just delivery.]

## Notes

[References, known gaps, decisions taken, assumptions that were confirmed.]
```

---

## Outcome sentence patterns

Pick the pattern that matches the kind of work. Do not force a number where there
is not one.

**Direct value — someone can do something new**

> [Named beneficiary] can [specific capability], which they currently cannot do
> [at all / without friction / reliably]. We will know this is achieved when
> [observable or measurable condition].

**Indirect value — enablement work (most of this team's work)**

> This work enables [named actor or team] to [changed behaviour], which removes
> [the specific current friction or dependency], which matters because [connection
> to a team goal or organisational need].

**Maintenance, hygiene, risk reduction**

> This work prevents [specific degradation or risk] from affecting [named
> beneficiary]. Without it, [consequence]. The outcome is that [the system or
> process] continues to work correctly in [the specific respect addressed].

**Long-horizon, arguable outcome**

> We believe [deliverable] will enable [actor] to [changed behaviour], leading
> eventually to [organisational effect]. This is an assumption. The leading
> indicator we will track is [specific observable]. We will assess whether it holds
> by [method or checkpoint].

**Epic-level outcome**

> After this epic, [named beneficiary group] can [capability]. They currently
> [constraint that is removed]. This describes the combined effect of the whole
> epic, not any single story within it.

---

## Worked example

**This is an excerpt, not a complete ticket.** It shows Context and Outcomes only, so
that the before and after sit side by side. A real epic also needs In scope, Out of
scope, Condition of satisfaction and Notes. Do not use the shape of this example as
the schema — use the templates above.

Taken from a real baseline. The first version was written without guidance.

### Before

> **Summary:** Improve repository engineering standards and pull request safeguards
>
> The repository was created from a company template and filled in quickly during
> delivery, leaving important engineering practices undocumented or unenforced. We
> need to make the repo easier and safer to work in by adding basic CI checks,
> replacing placeholder contribution guidance, and documenting how the project is
> structured and maintained.
>
> **Acceptance criteria**
> - Pull requests run automated checks before merge.
> - `CONTRIBUTING.md` has no remaining template TODO placeholders.
> - The team has reviewed and agreed the guidance is accurate.

### What is wrong

| Problem | Why it matters |
| --- | --- |
| No Outcomes section | Value is implied, never stated. Nobody knows who benefits. |
| "easier and safer to work in" | Fails the opposite test — nobody would ever set out to make a repo harder and less safe. The sentence carries no information. |
| No beneficiary named | Easier for whom? A new joiner, the on-call engineer, the original authors? Each implies different work. |
| No Out of scope | Nothing excluded, so the epic will absorb release automation, quality gates and anything else adjacent. |
| "The team has reviewed and agreed" | Depends on unrecorded opinion. Not checkable later. |
| Criteria prove delivery, not outcome | "No remaining TODO placeholders" is satisfied by deleting the TODOs without writing anything useful. |
| Context describes the fix, not the problem | Opens with what will be done, so the reader cannot judge whether it is the right thing to do. |

### After

> **Summary:** Establish technical ways of working for the repository
>
> **Context**
> How this team works is currently held in people's heads. Someone joining has to ask
> a colleague how to set up, build, test and contribute, and there is no automatic
> check that what they produce meets the standard the organisation expects of a repository. That
> slows people down and puts the quality of the work on the reviewer rather than on
> the process.
>
> Concretely: `docs/CONTRIBUTING.md` still carries template TODOs for coding
> conventions, installation, build, test and release. Each is an explicit MUST in the
> organisation's repository standard. There are no CI workflows, so nothing verifies a
> pull request. CONTRIBUTING directs contributors to GitHub Issues while the backlog
> is the Jira PROJ project. Increasingly the people following these conventions are
> agents, which have nothing authoritative to read.
>
> **Outcomes**
> - Anyone joining the repository — person or agent — can learn how we work from the
>   repository itself rather than by asking someone who was there.
> - Whoever picks up a question about why a change was made can trace it end to end,
>   because the ticket, the commits and the pull request are linked.
> - Maintainers can show the repository meets the organisation's repository standard, so
>   it can move toward a production lifecycle without rework.
> - Reviewers spend their time on design rather than catching mechanical problems,
>   because those are checked automatically before merge.
>
> **Out of scope**
> Release, packaging and distribution pipelines; deployment and infrastructure;
> code-quality gates and coverage thresholds; service-catalogue lifecycle promotion.

### What changed

- Context opens with what is hard for people today, then gives the specifics — named
  files, a named standard, a named contradiction — instead of a general impression.
- Every outcome names a beneficiary and something observable.
- "Easier and safer" is gone, replaced by what specifically becomes possible.
- Exclusions are stated, so the epic has an edge.
- The unrecorded-opinion criterion is gone.

---

## OKR linkage

If your organisation uses OKRs, add to an epic's Notes:

> Contributes to [specific key result]. This epic moves [which part of it], partially
> — [what else is needed].

Link to a key result, not an objective. Objectives are directions and every epic can
claim to serve them; key results are measurable, so the claim can be checked. An epic
that contributes partially should say so rather than implying it delivers the whole.
