# Brand Strategy Skill (development repo)

## What this project is

This repository develops, packages, and distributes the `brand-strategy` Agent Skill. The deliverable is the skill itself, not brand strategy work. When working here, your job is skill authoring: editing instructions, templates, and framework references, and re-packaging.

If the user actually wants brand strategy help (positioning a product, auditing a brand), that is the installed skill's job, not this file's. Apply the skill normally in that case.

## Repository layout

| Path | Role |
|------|------|
| `brand-strategy/` | The installable skill: `SKILL.md` plus `references/` (framework docs + document templates). This folder is what gets shipped. |
| `brand-strategy/SKILL.md` | Skill entry point. The frontmatter `description` is the trigger surface; the body defines workflow, deliverable selection, dependency chain, and conventions. |
| `brand-strategy/references/` | **Canonical, edited in place.** `frameworks.md` at the root is the always-read index and compact distillation; `frameworks/` holds the 6 full framework references; `templates/` holds the 7 document templates. |
| `brand-strategy.skill` | Packaged zip of `brand-strategy/`, committed for direct download. Rebuild after any skill change. |
| `README.md` | GitHub-facing: purpose, what the skill generates, installation, usage. |

## Sources of truth and packaging

Everything the skill ships lives in `brand-strategy/` and is edited in place. There are no derived copies to sync.

1. **Framework references**: when a `references/<framework>.md` file changes substantively, update its compact section and the index table in `frameworks.md` (also canonical, hand-maintained) so the two stay consistent.
2. **Repackage** after any change inside `brand-strategy/`:
   ```bash
   rm brand-strategy.skill && zip -r brand-strategy.skill brand-strategy
   ```
3. **Reinstall locally** to test: `cp -r brand-strategy ~/.claude/skills/`

**Distribution constraint: exactly one skill.** Never add a `SKILL.md` anywhere outside `brand-strategy/` (including `.claude/skills/`). The `npx skills` CLI scans the whole repo for `SKILL.md` files, and this repo must offer users exactly one installable skill.

A change is not done until the edited file, the `.skill` zip, and (if templates or document flow changed) the README's "What It Generates" section all agree.

## Skill authoring conventions

- **Progressive disclosure.** `SKILL.md` stays lean and routes to `frameworks.md` for the compact framework summary, and from there to the full per-framework references. Don't inline framework content into `SKILL.md`.
- **The `description` frontmatter is the trigger.** It must enumerate the user phrasings that should activate the skill (brand strategy, positioning, naming, taglines, audits, visual identity, media mix, line extension). Edits here change when the skill fires; treat them as behavior changes and test them.
- **Templates are contracts.** Keep the conventions stable: `{{placeholder}}` markers, `> 📋` authoring-instruction blockquotes (deleted in finished documents), completion checklists as quality gates, and fixed-criteria tables whose rows are never removed. Documents 1 through 5 form a dependency chain; if you change what a document locks, update the downstream templates and the dependency chain in `SKILL.md`.
- **No em dashes in any shipped prose** (README, SKILL.md, templates, references). Use a colon, comma, period, parentheses, or restructure the sentence.
- **Concrete over abstract.** The methodology's voice is direct and example-heavy. Preserve named brand examples and law citations when editing; they are load-bearing, not decoration.

## Methodology rules (editing invariants)

Every template enforces these nine rules; edits must not weaken them. They are stated in shipped form across `SKILL.md` (workflow, guardrails, How to Recommend) and the templates themselves; this list is the maintainer's checklist.

1. **Discovery before strategy.** No template gets filled until the four discovery questions are answered. The launch path records them in doc 1's Discovery block; the standalone audit and decision templates carry their own Discovery Snapshot because they skip doc 1.
2. **One word.** Every decision traces back to the single word the brand owns. A section that can't name the word it serves gets cut.
3. **Name the law.** Every recommendation cites its principle and a real brand example.
4. **Default against line extension.** A new offering gets a new brand unless a compelling case overrides.
5. **Flag convergence.** Combining categories requires an explicit risk flag with mitigation.
6. **PR before advertising.** No ad spend in any plan until earned media establishes the claim.
7. **Nail before hammer.** No visual decision without the locked verbal nail.
8. **Honesty test.** Every external claim survives an adversarial expert interview.
9. **Lead with the conclusion.** Every document opens with the strategic conclusion; rationale follows.

## Testing changes

1. Repackage and reinstall (commands above).
2. Open a fresh Claude Code session and verify the skill triggers on a plain brand question without being named, and that it starts with the four discovery questions.
3. For template changes, generate the affected document end to end and check the completion checklist is satisfiable.
4. For `description` changes, also verify the skill does NOT fire on adjacent-but-out-of-scope prompts (e.g., generic copywriting).

The `anthropic-skills:skill-creator` skill can run evals and benchmark trigger accuracy when a deeper check is warranted.
