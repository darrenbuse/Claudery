# Writing rules

Companion to [SKILL.md](SKILL.md). Apply these to ticket prose. Hard rules always
apply. Heuristics apply unless there is a reason not to.

## The opposite test

**Negate the claim. If the negation is something nobody would ever write as an
intended outcome, the original carries no information and must be rewritten.**

The test is established practice — Intercom use it on product principles: flip a
statement to its opposite, and if the opposite is not at least plausible, the
original is a truism rather than a position.

| Claim | Negation | Verdict |
| --- | --- | --- |
| Improves developer productivity | Worsens developer productivity | Absurd. Empty claim. Rewrite. |
| Drives efficiency | Reduces efficiency | Absurd. Empty claim. Rewrite. |
| Makes the repo easier and safer to work in | Makes it harder and less safe | Absurd. Empty claim. Rewrite. |
| Removes the manual handoff for data-source onboarding | Keeps the manual handoff | Plausible. Carries information. Keep. |
| Reduces median build time from 22 to 8 minutes | Increases it from 22 to 8 | Plausible. Carries information. Keep. |

Two supporting tests:

- **So what?** After each outcome, ask "so what?" If the answer is another vague
  sentence, go again. Stop when you reach a concrete consequence for a named person.
- **Specificity.** Can you attach a number, a named system, a named actor or a named
  process? If not, it is still abstract.

## Rewriting a weak claim

| Move | Do this |
| --- | --- |
| Unfalsifiable claim | Replace with an observable change |
| Comparative with no baseline — "faster", "better" | State current state and target state |
| No actor — "teams will be empowered" | Name the role or team |
| Abstract noun — "the provisioning process" | Describe the actual steps removed or automated |
| Vague scope — "across the estate" | How many services, repos, teams? If unknown, say so |
| Assertion with no mechanism | Add "because …" and state why it follows |
| Estimated value | Say "we expect X, based on Y" |

## Banned in Outcomes

Each of these fails the opposite test or hides the actor.

| Phrase | Why | Instead |
| --- | --- | --- |
| Unlocks value | Metaphor, no literal meaning | What was blocked, and what it now allows |
| Drives efficiency | No actor, process or measure | Name the process and the change |
| Empowers teams / engineers | Empty — every tool extends capability | What they can now do that they could not |
| Enables synergies | Corporate placeholder | The specific cross-team interaction |
| Accelerates delivery | Faster than what? | Baseline and target |
| Improves developer experience | Only acceptable with specifics | Add "by [mechanism], removing [friction]" |
| Seamless | Undefined, universally aspirational | Delete. Describe the actual journey |
| Robust | Undefined degree | Name the failure mode it prevents |
| Best-in-class, world-class, cutting-edge, game-changing | Marketing | Delete |
| Very, really, extremely, incredibly | Empty intensifiers | Delete |

## Banned in acceptance criteria

Words that make a criterion unfalsifiable: *appropriate*, *as appropriate*,
*reasonable*, *reasonably fast*, *properly*, *correctly handled*, *as needed*,
*where applicable*, *sufficient*, *robust*, *user-friendly*.

Also banned: criteria that depend on unrecorded opinion — "the team agrees",
"reviewed and found acceptable" — unless the record itself is the criterion
("the decision is recorded in Notes").

## Honest hedging

Where value is genuinely uncertain, say so rather than overclaiming or writing
something so hedged it says nothing.

- "We expect [effect], based on [evidence]."
- "We believe [chain]. This is an assumption; the leading indicator is [X]."
- "This may not hold if [condition]. We will know by [checkpoint]."

Avoid stacked hedges — "we think it may possibly help somewhat" — which state
nothing while appearing cautious.

## Mechanics

Following the GDS writing standard, which mandates plain English.

**Hard rules**

1. Split sentences over 25 words.
2. No more than 5 sentences in a paragraph.
3. Active voice. "The extractor writes the file", not "the file is written".
4. Never hide the actor in the passive — "it was decided" must name who decided.
5. Spell out an abbreviation on first use.
6. Write "for example", "that is", "such as" — not "eg", "ie", "etc".
7. Define internal shorthand, or do not use it.
8. No ambiguous "it" or "this" at the start of a sentence — name the thing.

**Heuristics**

9. Prefer the short word: *buy* not *purchase*, *help* not *assist*, *about* not
   *approximately*, *use* not *utilise*.
10. Cut nominalisations — words ending *-ion*, *-ment*. "Make a decision" becomes
    "decide"; "provide clarification" becomes "clarify".
11. Cut "there is", "there are" where the sentence works without them.
12. Cut "in order to" — "to" is enough.
13. Cut redundant pairs — "each and every", "first and foremost".
14. State the point first. Do not build up to it.
15. One idea per paragraph.
16. Use a list when items are genuinely parallel. Use prose when the connection
    between points is the substance — bullets fragment reasoning.

## Summaries

- Say what the work is, not how important it is.
- No trailing full stop.
- Avoid "Improve X" and "Update Y" alone — they say nothing. Name the change.
- Length: aim for under 12 words. If it will not fit, the item may be too big.

Good: "Extract the parser components from the prototype repo into the platform repo"
Weak: "Repo improvements"
Weak: "Improve repository engineering standards and pull request safeguards"

## Anti-patterns

| Pattern | Example | Fix |
| --- | --- | --- |
| Context-free | "Fix the thing" | State the situation and the problem |
| Assumes a conversation | "As discussed, do the migration" | Summarise the discussion in Context |
| Undefined shorthand | "Wire up the IP contract via the CLI seam" | Expand on first use |
| Ambiguous pronoun | "This needs to happen before it breaks" | Name both |
| Actor hidden by passive | "It was agreed the schema would change" | Who agreed? |
| Weasel criteria | "Should be reasonably fast" | State the threshold |
| Solution stated as problem | "We need a Kafka topic" | What problem does it solve? |
