# RSFA Technical Knowledge Repository

Canonical technical knowledge base for RSFA's systems, automations, integrations, incidents, operational procedures and technical decisions.

See `CLAUDE.md` for the full operating rules this repository follows.

## Start here

- `knowledge/00_PROJECT_GUIDE.md` — how this repository should be used.
- `knowledge/01_RSFA_SYSTEM_MAP.md` — high-level map of RSFA's systems and data flows.
- `knowledge/02_SYSTEMS_REGISTRY.md` — master registry of platforms and systems.
- `knowledge/03_AUTOMATION_REGISTRY.md` — master registry of automations (Make.com, Power Automate, Monday Workflows).
- `knowledge/04_MONDAY_BOARDS_REGISTRY.md` — Monday.com board registry.

## Structure

```text
knowledge/            — canonical, platform-independent documentation (systems, automations, playbooks, incidents, decisions, schemas, glossary)
exports/               — controlled technical exports (Make.com blueprints, Power Automate Solutions, Monday schemas)
source-material/        — earlier walkthrough notes used as evidence when drafting canonical documents
templates/             — approved templates for new canonical documents
.claude/               — Claude-specific agents and skills
```

## Power Automate Solution exports

`exports/power-automate/` contains exported Power Automate Solution packages, kept as read-only, point-in-time evidence:

- `exports/power-automate/solution-inventory.md` — index of every exported Solution and its flows, with mappings to canonical automations.
- `exports/power-automate/solutions/<solution>/manifest.md` — per-Solution identity, flow list, connection references, and security review.
- `exports/power-automate/README.md` — full explanation of the folder's structure and rules.

These exports are evidence, not working files: they must not be edited, and they are not proof of current live-production state. Proposed or modified Power Automate Solution files belong in the separate `rsfa-automation-development` repository, under `projects/<project-slug>/power-automate/` — never inside `exports/`.

## Working rules

Read `CLAUDE.md` before making any change to this repository. It defines evidence classification, documentation rules, registry maintenance, security handling, and the Git workflow this repository follows.
