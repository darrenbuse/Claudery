# Anti-patterns

Review checklist. Run it before calling a doc done; fix every box you cannot tick.

## Structure

- [ ] **Kitchen sink page** — tutorial steps, reference tables and explanation on one page. Split per quadrant; cross-link.
- [ ] **Empty scaffold** — four empty quadrant folders. Improve existing docs one at a time instead.
- [ ] **Dead end** — no prerequisites at the top, no next steps or related links at the bottom.
- [ ] **Feature mirror** — task docs organised by API surface, not reader goals.

## Content

- [ ] **Lecture tutorial** — theory paragraphs between steps. Cut to one sentence; link to explanation.
- [ ] **Disguised how-to** — labelled "tutorial" but assumes prior knowledge. Relabel.
- [ ] **Opinionated reference** — "we recommend..." in parameter tables. Move opinion to explanation, instruction to how-to.
- [ ] **Explanation with steps** — "Understanding X" that ends with "now do this". Move the steps to a how-to; link.
- [ ] **Abstract description** — what something "can do", no example. Show code, output or a diagram.
- [ ] **Choices buffet** — a tutorial offering multiple languages or paths. Pick one; guide it completely.
- [ ] **"You will learn" promise** — describe what the reader will *build*.
- [ ] **Feature announcement voice** — "We've added X!" Frame as what the reader can now do.

## Style and sentences

- [ ] **Passive maze (task docs)** — "the file should be edited". Write "edit the file". Reference may use natural passive description.
- [ ] **Thesaurus trap** — "workspace", "project", "environment" for one thing. One term per concept.
- [ ] **Idiom minefield** — "out of the box", "hit the ground running". Plain language; global audience.
- [ ] **Admonition avalanche** — max 2-3 callouts per page; Warning only for data loss or security, Note only for surprising information.
- [ ] **Mismatched tone** — reference written as "Let's learn...", tutorial in austere API prose. Match tone to quadrant.
- [ ] **UI narrator** — "Click Deploy to deploy". Document the judgement, not the button.
- [ ] **Filler openers** — "In this guide, we will...", "It is important to note that...". Say the thing.
- [ ] **"Simply" / "just" / "easily"** — condescending to anyone struggling. Delete.
- [ ] **Hedging** — "seems", "appears", "might". State what you verified; stop where evidence ends.
- [ ] **Vague absolutes** — "always", "never", "completely". Make the measured claim.
- [ ] **Vague adjectives** — "powerful", "robust", "seamless". Replace with numbers or behaviour.

## Code examples

- [ ] **Broken example** — missing imports, undefined variables. Every example runs as written, or is explicitly marked unverified.
- [ ] **hello-world values** — `foo`, `bar`, toy commands. Use real filenames, ports and context.
- [ ] **Wall-of-text code block** — comment every non-obvious line: the why, not the what.
- [ ] **Marathon quickstart** — an hour of setup before the first result. Strip to install, one command, one visible result.

---

Adapted from anivar/developer-docs-framework (MIT) and Xamfonos/technical-writing-best-practices (MIT); Diataxis by Daniele Procida (diataxis.fr).
