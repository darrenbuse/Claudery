# Gate 2 — cold read validation

Invoked from the Validation section of the `writing-tickets` skill. Run this for epics,
for stories with more than about five acceptance criteria, and for anything contentious.

## Gate 2 — cold read, by subagent

You cannot run this yourself: you know what the ticket means, and that knowledge is the
contamination being tested for. Dispatch two agents **in parallel**; they must not see
each other's output.

**Agent A — cold reader.** Ticket text and *nothing else*. No background, no history,
no explanation. Withholding context is the point. Ask it to do things, not to give an
opinion — "is this a good ticket?" produces flattery.

> 1. In one sentence, what will exist when this is done that does not exist today?
> 2. Who is better off, and how would they notice?
> 3. For each criterion — or an epic's condition of satisfaction — describe the
>    procedure you would follow to check it: what you would run, look at or compare.
>    You are not being asked to carry it out. Answer "I COULD NOT CHECK THIS" only
>    where you cannot describe a procedure at all, and say what is missing.
> 4. What would you have to ask before you could start?

**Agent B — auditor.** Ticket text *plus* this skill, TEMPLATES.md and
WRITING-RULES.md — it cannot audit structure without the templates. Ask for violations
with the specific line, and to say plainly if it finds none.

| Signal | Meaning |
| --- | --- |
| A cannot restate the outcome | Outcomes are not doing their job |
| A answers "I could not check this" | That criterion is not checkable. Rewrite it |
| A asks something the ticket should have answered | Missing context. Add it |
| A and B disagree about what the work is | The ticket is ambiguous |

**Triage; do not auto-apply.** A cold reader flags domain vocabulary it does not know.
If the intended audience knows the term, keep it. Judge each report; the agent's
discomfort is not automatically a defect.

**Never let a subagent rewrite the ticket.** It knows neither the domain nor the
conversation, so it will invent outcomes — the thing the guardrails forbid. It reports;
you fix.
