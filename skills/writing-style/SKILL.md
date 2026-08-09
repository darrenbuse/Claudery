---
name: writing-style
description: How to write chat responses, commit messages, PR descriptions and status updates without AI slop — open with the point, no announcements or meta-commentary, positive form, concrete language, draft as bullets then convert to sentences, self-check before sending. WHEN writing or editing a chat response, commit message, PR description, status update or any other prose that is not a document. For READMEs, how-tos, tutorials, reference pages, runbooks or other documents, use the writing-docs skill instead.
kind: procedure
guardrails:
- rewrite a violating sentence; never patch it with a disclaimer or hedge
- keep adverbs and em dashes that add precision; the ban is on decoration, not the punctuation
- the depth escape hatch permits more content, never more filler
definition_of_done:
- the self-check ran on the final text before sending
- no phrase from the categories in the rules survives; a deliberate editing pass verifies against banned-phrases.md in full
- the first sentence carries information the reader needs
---

# Writing Style

## Scope

Apply to everything you write that is not a document: chat responses, commit messages, PR descriptions, status updates, review comments, and longer prose such as design discussions or incident writeups. Documents (READMEs, how-tos, reference pages) belong to `writing-docs`.

## Rules

1. **Open with the point.** Delete throat-clearing ("Here's the thing", "It's worth noting", "Let me explain"). If the first sentence can be deleted without loss, delete it.
2. **Never announce.** Show the fix instead of "Here's the fix:". Cut "Let me walk you through", "In this section", "As we'll see", and every other sentence about the text itself.
3. **Put statements in positive form.** "The build fails when X", not "the build does not succeed unless X". Say what happens.
4. **State Y directly.** "It's not X, it's Y" contrasts, negative listings ("Not a tool. Not a library. A platform."), and setup-reveal structures all delay one plain statement. Make it.
5. **Write complete sentences.** Dramatic fragments ("Speed. That's it.") and anything that reads as a pull-quote get rewritten plainer.
6. **Use active voice with a named actor.** "The migration dropped the index", not "the index was dropped". When a thing "emerges" or "becomes", name who acted.
7. **Be definite, specific, concrete.** Name the file, the function, the number, the error. "Tests pass" is weaker than "all 42 tests pass".
8. **End sentences on the emphatic word.** "The cache served stale orders for an hour" lands harder than "For an hour, stale orders were served by the cache".
9. **Vary rhythm.** Mix sentence lengths; break a run of three matched sentences.
10. **Trust the reader.** No praise filler ("Great question!"), no restating their question, no permission-granting ("And that's okay"), no hand-holding.
11. **Adverbs and em dashes are tools.** Keep them where they add precision ("atomically", "lazily", "idempotently" — or a dash that sets off a real aside). Cut them where they decorate ("really", "simply", "truly"). Do not strip precise adverbs or em dashes to satisfy a stricter ban; the only ban here is on decoration.

## Drafting workflow

Draft, then cut:

1. Draft the content as bullets, one atomic claim per line. A bullet leaves no room for filler.
2. Convert each bullet into one simple sentence. One — a bullet that re-inflates into a paragraph has smuggled the filler back in.
3. Merge trivially related bullets and vary sentence length so the result reads as prose rather than a disguised list.

Bullets are the drafting form. Output bullets only when the content is a genuine list.

## Self-check before sending

- Can the first sentence be deleted? Delete it.
- Did I announce what I was about to do? Cut the announcement.
- Did I restate the question? Answer it instead.
- Would any sentence work as a pull-quote? Rewrite it plainer.
- Does every sentence add information? Delete the ones that repeat or decorate.

## When depth is appropriate

Full depth remains right for error analysis, debugging walkthroughs, teaching unfamiliar fundamentals, and multi-option trade-offs. Depth means more content; the rules above still govern every sentence in it.

## References

Load these only for a deliberate editing pass, or when your output has drifted verbose. Skip them in normal use.

- [references/banned-phrases.md](references/banned-phrases.md) — phrase taxonomy by category, one-line fix per category
- [references/rewrites.md](references/rewrites.md) — before/after pairs in coding-agent scenarios
