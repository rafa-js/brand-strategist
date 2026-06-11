# Brand Strategy: A Claude Skill

> _Brainstorm your brand strategy_

This skill turns your agent into brand strategist grounded in brand strategy playbooks:
- *Positioning*
- *The 22 Immutable Laws of Marketing*
- *The Origin of Brands*
- *The Fall of Advertising and the Rise of PR*
- *Visual Hammer*

It also draws on Jonah Berger's *Contagious: Why Things Catch On* to make PR stories travel by word of mouth.

Instead of generic marketing advice, the skill runs a disciplined methodology: it interviews you first (product, competition, current position, business goal), picks the right deliverable, and produces complete strategy documents from battle-tested templates. Every recommendation names the specific law it's grounded in and cites a real brand that proved it.

It's packaged as an [Agent Skill](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): a folder of instructions, framework references, and templates that Claude loads on demand. It works in Claude Code out of the box and in any agent that supports the skills format.

## Why This Skill?

Ask a bare LLM for brand advice and you get the average of everything ever written about marketing: agreeable, additive, and contradictory. This skill exists to prevent exactly that.

- **It has opinions.** Line extensions get challenged by default. Convergence plays get flagged. "Better advertising" is never the answer to a positioning problem. The skill will tell you your brand name is wrong, which a people-pleasing chatbot won't.
- **One coherent methodology, not a blend.** Six books that share a single worldview (the battle is for the mind, focus beats breadth, credibility precedes awareness), with a fixed hierarchy for when they conflict. You get a consistent strategic posture, not a different framework every session.
- **Accountable recommendations.** Every prescription names the law it stands on and a real brand that proved it or died ignoring it. You can check the reasoning, not just trust the vibes.
- **Documents, not chat fragments.** Discovery questions first, then complete deliverables from templates with quality-gate checklists. The output is a strategy package you can hand to a designer, a PR firm, or an investor.
- **Subtractive by design.** Most brand advice adds: more features, more audiences, more channels. This methodology cuts until what remains is ownable. The prescriptions that survive are the ones you can actually execute.

If you want a brainstorming partner that says yes to everything, this is the wrong skill. If you want a strategist that argues back, install it.

## What It Generates

**Launching a new brand (or repositioning one)?** You get a five-document strategy package, produced in order, each locking decisions the next inherits:

| # | Document | What It Locks |
|---|----------|---------------|
| 1 | **Market Research** | The evidence base: why the incumbent framework fails, competitive landscape with per-competitor deep dives, market trends, all converging on the strategic gap your brand will claim |
| 2 | **Brand Strategy** | The hub: brand name, category to create, the one word to own, product-through-the-strategy, naming rationale, strategic guardrails, decisions log |
| 3 | **Positioning** | Positioning statement, tagline (with evolution path), elevator pitch, positioning tests, competitive repositioning map, language discipline (always say / never say) |
| 4 | **Visual Identity** | The visual hammer: symbol, color (chosen by category contrast), typography, app icon, design language, every choice anchored to the verbal position |
| 5 | **PR Narrative** | The launch: core story, three-act narrative, ranked media angles, STEPPS shareability check, outlet tiers, influencer strategy, week-by-week sequencing. PR before advertising, always |

**Diagnosing a struggling brand?** You get an audit report: a sweep of which of the 22 Laws are being violated (with evidence and severity), position assessment, visual-verbal alignment check, advertising-vs-credibility check, root-cause synthesis, and ranked prescriptions that subtract rather than add.

**Making a single decision** (name X vs. Y, extend the brand or not, media mix)? You get a decision recommendation: options scored against one lens (clearer? more focused? more ownable in the mind?), adjudicated by the laws, with mandatory line-extension and convergence gates.

Every template carries `{{placeholders}}`, authoring guidance, and a completion checklist that acts as a quality gate, so the output is consistent whether a human or an agent fills it.

## Installation

<details open>
<summary><b><code>npx skills</code> (recommended)</b></summary>

Installs via the open [agent skills CLI](https://github.com/vercel-labs/skills), which works with Claude Code and 60+ other agents:

```bash
npx skills add rjseibane/brand-strategy-skill
```

To target Claude Code explicitly:

```bash
npx skills add rjseibane/brand-strategy-skill -a claude-code
```

</details>

<details>
<summary><b>Copy and paste</b></summary>

Clone the repo and copy the skill folder into your skills directory:

```bash
git clone https://github.com/rjseibane/brand-strategy-skill.git

# personal install (all your projects)
cp -r brand-strategy-skill/brand-strategy ~/.claude/skills/

# or project install (committed, shared with collaborators)
cp -r brand-strategy-skill/brand-strategy your-repo/.claude/skills/
```

</details>

<details>
<summary><b>From the <code>.skill</code> file</b></summary>

Grab [`brand-strategy.skill`](brand-strategy.skill) (a zip of the skill folder):

- **Claude apps that accept skill uploads** (Claude.ai / Claude Desktop, where available): upload it via Settings → Capabilities/Skills.
- **Manually, anywhere:**
  ```bash
  unzip brand-strategy.skill -d ~/.claude/skills/
  ```

</details>

### Verify

Open a new Claude Code session and type `/brand-strategy`, or just ask something like *"Help me position a new coffee brand against Starbucks."* The skill is working when Claude starts with the four discovery questions instead of generic advice.

## Usage

Invoke explicitly:

```
/brand-strategy I'm launching a meal-prep app for busy parents
```

Or just ask. The skill triggers on brand questions automatically:

- *"Audit my DTC coffee brand. Sales are flat and we're up to four product lines."*
- *"Should we launch the new energy drink under our existing brand name or a new one?"*
- *"I need a positioning statement and tagline for an AI note-taking tool competing with Notion."*
- *"Design a visual identity brief for my fintech startup."*

Expect to be interviewed before you get strategy: the methodology requires four discovery answers (product, competition, current position, business goal) before any recommendation. That's a feature, not friction.

## The Methodology

- **One lens for every decision:** does this make the brand clearer, more focused, and more ownable in the mind of the prospect?
- **Law-grounded:** every recommendation names its principle and cites a brand that executed it (or died ignoring it). The full framework references (all 22 Laws, the positioning concepts, divergence, PR-first sequencing, visual hammer criteria, the STEPPS shareability levers) are bundled in the skill, so it works standalone.
- **Opinionated guardrails:** line extensions are challenged by default; convergence plays get flagged; advertising is never prescribed to fix a positioning problem; claims must survive an adversarial expert interview.
- **When frameworks conflict**, they resolve in a fixed hierarchy: Positioning → 22 Laws → Origin of Brands → PR before advertising → Visual Hammer → Contagious (shareability serves the story).
