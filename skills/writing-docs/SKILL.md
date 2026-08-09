---
name: writing-docs
description: How to write well-structured documentation using the Diataxis framework — classify every doc into exactly one quadrant (tutorial, how-to, reference, explanation), keep the quadrant boundaries, match voice to quadrant, and draft in plain language. Covers repo docs (READMEs, how-tos, architecture, reference), team docs (onboarding, runbooks) and Obsidian vault notes (summaries, decision records); a status update stays with writing-style even when saved to the vault. WHEN writing, reviewing or restructuring a README, how-to, tutorial, reference page, architecture doc, runbook, onboarding guide, troubleshooting guide, ADR or vault note.
kind: procedure
inputs:
- the subject matter (code, system, decision, procedure) and its intended reader
outputs:
- a doc classified into one Diataxis quadrant, written in that quadrant's form and voice
guardrails:
- classify the doc into exactly one quadrant before writing a word of it
- never mix quadrants in one doc — split into separate docs and link between them (README excepted, see the type map)
- never invent numbers, behaviour or claims to sound authoritative; stop where evidence ends
- never state that code runs, or that output appears, unless you verified it or the user confirmed it
definition_of_done:
- the doc sits in exactly one quadrant, chosen before drafting
- no quadrant mixing — a how-to that grew an explanation section is split, with a link
- every code example was executed, confirmed by the user, or explicitly marked unverified; examples use real filenames, paths, ports and values
- headings state outcomes, not topics, in task docs
- each file reread against the sentence-craft rules and anti-patterns.md; violations deleted
---

# Writing Docs

## Overview

Classify before you write. Every doc serves one of four purposes, and mixing them produces docs that serve no reader well — too slow for practitioners, too thin for learners, too noisy for lookup. This skill covers repo docs, team-facing docs and Obsidian vault notes.

## Classify first

Ask two questions about the reader:

1. **Studying or working?** Studying → left column. Working (mid-task, at the keyboard) → right column.
2. **Practical steps or understanding?** Steps → top row. Knowledge → bottom row.

|                   | Studying        | Working       |
| ----------------- | --------------- | ------------- |
| **Steps**         | Tutorial        | How-to guide  |
| **Knowledge**     | Explanation     | Reference     |

- **Tutorial** — a lesson. The reader builds one concrete thing and gains skill. Answers "teach me".
- **How-to guide** — steps to a goal. The reader already knows the basics. Answers "how do I X?".
- **Reference** — austere description of what exists. Answers "what is X?".
- **Explanation** — discussion of why. Answers "why is it this way?".

Map common types before writing:

| Doc type | Quadrant | Note |
| --- | --- | --- |
| README | Compound (exception) | Landing page: reference-voice description plus an embedded quickstart, linking out for the rest; the one sanctioned multi-quadrant doc — keep each section in one quadrant's voice |
| Quickstart | How-to | Fastest path to a working result |
| Onboarding guide | Tutorial | A new teammate is a learner |
| Runbook | How-to | Symptom → exact commands → verification |
| Troubleshooting guide | How-to | Organise by symptom, not by cause |
| Architecture doc | Explanation | Design and trade-offs; no steps |
| ADR / vault decision note | Explanation | Context, decision, consequences |
| Vault summary note | Record (exception) | Outside the quadrant map; apply the sentence-craft rules only |

## Boundary rules

1. **One purpose per doc.** A doc that needs two quadrants is two docs. Split, then cross-link.
2. **Tutorials are lessons, not how-tos.** The tutorial reader is a student; the how-to reader is a practitioner with a goal. The difference is study versus work, not basic versus advanced.
3. **Reference describes.** It never instructs ("first do X"), explains ("because Y") or persuades ("we recommend Z"). Link out for those.
4. **Explanation discusses.** Numbered steps in an explanation mean you are writing a how-to — move the steps out and link.
5. **Lead with outcomes, not features.** Title task docs after what the reader achieves: "Move data to the warehouse", not "The Pipeline API".
6. **Show, don't tell.** Every concept gets a concrete example — code, output, a diagram. The showing often replaces the telling.

## Voice by quadrant

| Quadrant | Person | Tone | Patterns | Never |
| --- | --- | --- | --- | --- |
| Tutorial | "we" | Encouraging, patient | "First, do X. You should see..."; one path, no choices | Alternatives, theory paragraphs, "you will learn" |
| How-to | "you" | Direct; assumes competence | Conditional imperatives: "If you need X, do Y" | Teaching basics, narrating the UI |
| Reference | Third person | Austere, factual, no personality | "Returns a list of...", "Defaults to `usd`" | Instruction, opinion, narrative |
| Explanation | "we"/"I", conversational | Thoughtful; opinion allowed | "We chose X because...; the trade-off is..." | Steps, parameter listings |

Word rules, all quadrants: cut "simply", "easy", "just" and "please"; write descriptive link text, never "click here"; write "use", not "leverage" or "utilize"; name the section you mean, never "above" or "below".

## Sentence craft

- **Kill filler.** Delete on sight: "It's important to note that", "In order to", "Basically", "As mentioned earlier". Say the thing.
- **One purpose per sentence.** Break long sentences at each new action or dependency.
- **Back claims with code or numbers.** "Reduced image load time from 320ms to 120ms", not "much faster". Delete "powerful", "robust" and "seamless" — replace with the specific.
- **Hedge once, deliberately.** Cut reflexive hedges ("seems", "appears", "might") on claims you verified; where uncertainty is real, name it once explicitly instead of hedging every sentence. Cut "always", "never" and "completely" — stop where evidence ends.
- **Real examples.** Real filenames, paths, ports and values: `docker run -p 8080:8080 myapp:latest`, not `hello-world`; `ada@example.com`, not `foo`.
- **Banned phrases.** For the full taxonomy, see `../writing-style/references/banned-phrases.md`.

## Drafting workflow

1. **Classify.** One quadrant, using the two questions. Record it.
2. **Outline the sections.** In task docs, phrase headings as outcomes ("Restore the database from backup"), not topics ("Backups").
3. **Bullet each section.** One atomic claim per line. No prose yet.
4. **Convert each bullet into exactly one simple sentence.** One — a bullet allowed to become two sentences re-inflates into a paragraph.
5. **Merge and vary.** Combine trivially related bullets; vary sentence length so the result reads as prose, not a transcript.
6. **Keep genuine lists as lists.** Reference tables, prerequisite lists and step sequences stay structured — Diataxis reference form beats forced prose.
7. **Review.** Check the draft against `references/anti-patterns.md` and the `definition_of_done` in this skill's frontmatter. Delete violations; do not soften them.

## References

- `references/templates.md` — copy-paste skeletons for tutorial, how-to, reference page, explanation, README, runbook and ADR.
- `references/anti-patterns.md` — review checklist of docs smells. Run it before calling any doc done.

---

Adapted from anivar/developer-docs-framework (MIT) and Xamfonos/technical-writing-best-practices (MIT); Diataxis by Daniele Procida (diataxis.fr).
