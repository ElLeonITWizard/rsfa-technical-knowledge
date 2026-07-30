# CLAUDE.md

## What this file contains

This file defines how Claude Code must work inside the RSFA technical knowledge repository.

It does not document individual automations in detail. Instead, it establishes the permanent operating rules Claude must follow when reading, creating, updating and validating repository content.

## Objective

The objective of this file is to ensure Claude:

- Understands the purpose of the repository.
- Understands the technical context of RSFA.
- Knows where each type of information belongs.
- Distinguishes verified facts from assumptions.
- Does not invent missing information.
- Protects sensitive information.
- Works carefully before proposing production changes.
- Maintains consistency across documentation and registries.
- Uses agents, skills and connected tools safely.

---

# RSFA Technical Knowledge Repository

## 1. Repository purpose

This repository is the canonical technical knowledge base for RSFA's systems, automations, integrations, incidents, operational procedures and technical decisions.

It is intended to help RSFA:

- Understand how its technical ecosystem works.
- Investigate support requests and incidents.
- Maintain existing automations.
- Design new automations safely.
- Identify dependencies between systems.
- Document changes and decisions.
- Reduce the need to reconstruct historical context from Slack messages, screenshots or old conversations.
- Preserve technical knowledge independently from any individual developer.

This repository is not a storage location for client records, credentials or other sensitive business data.

---

## 2. RSFA context

RSFA is a New Zealand financial-advice business.

Rod Schubert is a financial adviser and owner of RSFA.

Kathleen Schubert also works at RSFA and is more strongly involved in insurance-related work.

RSFA's technical ecosystem includes:

- Make.com automations.
- Power Automate flows.
- Monday.com boards and workflows.
- SharePoint and Microsoft 365 integrations.
- Jotform questionnaires.
- Aircall integrations.
- Slack communication and technical ticket management.
- Document-generation processes.
- Technical documentation and system maintenance.

RSFA prioritises functionality and has little tolerance for errors.

Technical work for RSFA must therefore favour:

1. Reliability.
2. Verification.
3. Clear evidence.
4. Controlled testing.
5. Reversible changes.
6. Accurate communication.

Do not trade safety or correctness for speed.

---

## 3. Primary users

The primary users of this repository are RSFA developers, technical consultants and authorised staff responsible for maintaining RSFA systems.

The repository should help them:

- Quickly understand unfamiliar parts of the system.
- Identify which automation is related to a ticket.
- Locate the relevant board, flow, scenario or document.
- Understand how systems are connected.
- Investigate failures without relying only on memory.
- Prepare safe implementation plans.
- Communicate findings clearly to RSFA stakeholders.
- Continue maintenance work even when the original developer is unavailable.

---

## 4. Canonical repository structure

### `knowledge/`

Contains reusable, platform-independent knowledge about RSFA.

### `knowledge/systems/`

Documents individual platforms and systems, including:

- Monday.com
- Make.com
- Power Automate
- SharePoint
- Microsoft 365
- Slack
- Aircall
- Jotform

System documents describe:

- The role of each platform in RSFA.
- Ownership.
- Connections.
- Naming conventions.
- Limitations.
- Security considerations.
- Related automations.
- Known operational dependencies.

### `knowledge/automations/`

Contains the canonical documentation for each RSFA automation.

Each active automation should have one main document.

Do not create separate versions of the same automation document for ChatGPT, Claude or another AI platform.

### `knowledge/documents/`

Contains summaries, indexes and references for important source documents.

Original PDFs and sensitive source files should normally remain in their approved storage location, such as SharePoint.

### `knowledge/playbooks/`

Contains repeatable operational procedures, such as:

- Investigating a failed automation.
- Processing a Slack ticket.
- Testing a Make.com scenario.
- Recovering from a missing output.
- Preparing and validating a production change.
- Reviewing an incident.
- Updating technical documentation.

### `knowledge/incidents/`

Contains records of important technical incidents and their investigation.

Incident files must be sanitised and must not contain unnecessary client data.

### `knowledge/decisions/`

Contains technical and architectural decisions.

Use these files when a decision affects how future work should be performed.

### `knowledge/schemas/`

Contains structured technical information such as:

- Monday board schemas.
- Monday column IDs.
- Make scenario structures.
- Power Automate flow structures.
- Important data mappings.
- Trigger conditions.
- Routing logic.
- Output structures.

### `knowledge/glossary/`

Contains RSFA-specific terms, abbreviations and naming conventions.

### `templates/`

Contains approved templates for creating new documentation.

Always use the relevant template before creating a new canonical document.

### `exports/`

Contains controlled technical exports such as:

- Make.com blueprints.
- Power Automate definitions.
- Monday schema exports.

Do not place unreviewed exports containing sensitive data in this folder.

### `.claude/`

Contains Claude-specific configuration, agents and skills.

Claude-specific instructions belong here or in this `CLAUDE.md` file.

Platform-independent RSFA facts must not be stored only inside `.claude/`.

---

## 5. Source-of-truth rules

A technical fact should be documented once in the canonical knowledge base.

Do not create competing copies of the same knowledge in different folders.

Use evidence in the following order when investigating a current technical question:

1. Live information from the relevant system.
2. Current canonical documentation in this repository.
3. Current source documentation stored in SharePoint or another approved system.
4. Recent Slack discussions and ticket threads.
5. Historical incident records.
6. Explicitly labelled inference.

A Slack message may represent a new request or decision, but it does not automatically replace existing technical documentation.

When live-system behaviour conflicts with documentation:

1. Do not silently choose one.
2. Clearly identify the discrepancy.
3. Treat the live system as evidence of current behaviour.
4. Investigate whether the behaviour is intended.
5. Update the documentation only after verification.

---

## 6. Evidence classification

Always classify important information as one of the following.

### Confirmed from live system

Information directly verified using a current system, connected tool, API, export or approved interface.

### Confirmed from documentation

Information found in a current canonical document or verified source document.

### Historical information

Information that was true at a previous point in time but may no longer describe the current system.

### Inference

A conclusion derived from available evidence but not directly verified.

### Unknown

Information that could not yet be confirmed.

Never present an inference as a confirmed fact.

When information is missing, write:

```text
TODO: verify
Do not invent a value to complete a document.

---

## 7. Working procedure

Before answering a technical question or recommending a change:

1. Identify the affected business process.
2. Identify the related automation.
3. Read the current automation document.
4. Read the related system and schema documents.
5. Check relevant incidents and technical decisions.
6. Retrieve live information when approved tools are available.
7. Identify dependencies and downstream effects.
8. Separate confirmed facts from assumptions.
9. Assess the operational risk.
10. Prepare a validation approach.

Before modifying documentation:

1. Read the existing file completely.
2. Read directly related files.
3. Check the relevant registry.
4. Preserve existing confirmed information.
5. Preserve source references and technical IDs.
6. Add missing information only when supported by evidence.
7. Update the change history.
8. Update related registries where required.

---

## 8. Production-change requirements

Before recommending or implementing a production change, define:

- The problem being solved.
- The expected outcome.
- The affected systems.
- The affected automation or workflow.
- Dependencies.
- Possible side effects.
- Test cases.
- Expected test results.
- Post-change validation.
- Rollback procedure.
- Required stakeholder approval.

Do not recommend editing production based only on:

- An isolated Slack message.
- An unverified assumption.
- An outdated screenshot.
- Historical documentation.
- A partial automation export.
- A remembered implementation detail.

Where possible, inspect the current production configuration first.

---

## 9. Testing expectations

RSFA has little tolerance for dysfunctional deliverables.

Testing should cover, where applicable:

- Successful standard processing.
- Missing optional information.
- Missing required information.
- Duplicate processing.
- Empty values.
- Incorrect mappings.
- Unavailable external services.
- Failed API requests.
- Invalid linked Monday items.
- Missing SharePoint folders.
- Missing files or templates.
- Partial completion.
- Reprocessing after failure.
- Downstream automation impact.

Do not describe a change as tested unless the test was actually performed.

Use the following terminology:

- `Planned`: the test has been designed but not executed.
- `Passed`: the expected result was confirmed.
- `Failed`: the result did not match expectations.
- `Partially verified`: only part of the process was confirmed.
- `Not testable`: the test could not be safely performed.

---

## 10. Documentation rules

All canonical documentation should be:

- Precise.
- Operational.
- Easy to scan.
- Explicit about dependencies.
- Clear about current status.
- Clear about verification dates.
- Written without vague references.

Prefer:

```text
The `Mortgage App` board triggers `AUTO-MORTGAGE-001`, which creates an item in `Masterboard End Forms`.
```

Avoid:

```text
The first board sends the information to the other board.
```

Whenever known, include:

- Internal document ID.
- Platform-specific ID.
- Exact system name.
- Exact board name.
- Exact column name and ID.
- Exact scenario or flow name.
- Current status.
- Last verification date.
- Related documents.
- Source reference.

Use ISO dates:

```text
YYYY-MM-DD
```

Documentation should normally be written in English because RSFA operates in English.

Another language may be used when explicitly required.

---

## 11. Document maintenance rules

When modifying a document:

- Update `last_modified`.
- Update `last_verified` only if real verification occurred.
- Add an entry to the change history.
- Preserve the internal ID.
- Update related document references.
- Update the relevant registry when required.

A document must not be marked as current solely because it was recently edited.

The verification date must reflect when the documented behaviour was actually checked.

When an automation is replaced:

1. Do not delete its historical documentation.
2. Mark the old automation as deprecated or replaced.
3. Link it to the replacement.
4. Update the Automation Registry.
5. Explain migration or compatibility considerations.

---

## 12. Registry maintenance

The main registry files are:

- `knowledge/02_SYSTEMS_REGISTRY.md`
- `knowledge/03_AUTOMATION_REGISTRY.md`
- `knowledge/04_MONDAY_BOARDS_REGISTRY.md`
- `knowledge/09_DOCUMENT_REGISTRY.md`

When creating a new system, automation, board or source document:

1. Create the canonical file.
2. Assign an internal ID.
3. Add it to the relevant registry.
4. Add relationships to related files.
5. Confirm that links and paths are correct.

Do not create undocumented orphan files.

---

## 13. Security and sensitive information

RSFA handles financial, insurance and personal client information.

Never commit:

- Passwords.
- API keys.
- OAuth client secrets.
- Access tokens.
- Refresh tokens.
- Private keys.
- Authentication cookies.
- Real mortgage application data.
- Client financial information.
- Identification documents.
- Medical or insurance records.
- Full client email contents.
- Full call recordings.
- Unredacted client call transcripts.
- Real client information used as test data.

Credentials may only be referenced by:

- System.
- Approved password manager vault.
- Credential item name.
- Purpose.
- Account owner.

Never include the secret value.

Use sanitised or fictional examples in documentation.

---

## 14. Tool and connector usage

When approved tools or MCP connections are available, use them to retrieve current information.

Possible live sources may include:

- Monday.com
- Slack
- SharePoint
- Microsoft 365
- Make.com
- Power Automate
- Aircall
- Jotform

Use tools only for the scope required by the task.

Prefer read and search operations before write operations.

Before any action that modifies an external system:

1. Explain the proposed action.
2. Identify the exact target.
3. Explain the expected outcome.
4. Explain possible risks.
5. Request explicit approval unless the user already clearly authorised the exact action.

Never perform destructive, bulk or irreversible actions without explicit approval.

---

## 15. Slack ticket investigation

When investigating a request from Rod or another RSFA team member:

1. Retrieve the full Slack thread when available.
2. Identify the original request.
3. Identify later clarifications.
4. Extract dates, links, filenames and system references.
5. Identify the affected automation.
6. Retrieve live-system evidence.
7. Review related documentation.
8. List confirmed facts.
9. List unverified information.
10. Develop likely causes.
11. Propose investigation steps.
12. Recommend a solution only when sufficiently supported.
13. Prepare a concise response for the relevant RSFA stakeholder.
14. Identify documentation updates required.

Do not treat a short Slack message as complete technical requirements when the thread contains additional context.

---

## 16. Communication with RSFA stakeholders

Responses prepared for RSFA stakeholders should be:

- Clear.
- Concise.
- Professional.
- Direct about limitations.
- Explicit about what was confirmed.
- Explicit about what could not be confirmed.
- Focused on the recommended next step.

Do not overstate confidence.

Do not claim a problem is resolved until the expected outcome has been validated.

When a limitation prevents full investigation, explain:

- What was checked.
- What was confirmed.
- What could not be accessed.
- Why it could not be accessed.
- What should be changed to improve future investigations.

---

## 17. Git workflow

Before changing multiple canonical files:

1. Review the current Git status.
2. Consider using a dedicated branch.
3. Keep changes focused on one purpose.
4. Review the final diff.
5. Confirm no sensitive data is included.
6. Use a clear commit message.

Do not:

- Force-push.
- Rewrite shared history.
- Delete documentation without preserving required history.
- Commit generated or sensitive files accidentally.

Recommended commit examples:

```text
docs: add Aircall transcription automation documentation
docs: update Mortgage App column mappings
fix: correct Monday board registry references
docs: record missing attachment incident findings
```

---

## 18. Claude agents and skills

Use specialised agents and skills when they match the task.

Expected agent responsibilities include:

- RSFA ticket investigation.
- Make.com scenario auditing.
- Power Automate debugging.
- Monday.com schema analysis.
- Documentation maintenance.

Expected skills include:

- Processing an RSFA ticket.
- Documenting an automation.
- Comparing Monday schemas.
- Preparing a production change plan.

Agents and skills must follow this file and may not override its safety, evidence or documentation rules.

---

## 19. Initial documentation priorities

Prioritise documentation in this order:

1. Aircall Transcriptions and AI Summaries.
2. Mortgage Application to Masterboard mapping.
3. Client Email Filing.
4. Overflow Email Processing.
5. Branded Mortgage SOP Generation.
6. Jotform Mortgage Questionnaire.
7. Monday.com board schemas.
8. SharePoint document and folder structure.
9. Make.com scenario registry.
10. Power Automate flow registry.

Prefer a partially complete but accurate document over a complete-looking document containing assumptions.

---

## 20. Final quality check

Before completing a task, confirm:

- Was the correct system or automation identified?
- Were related files reviewed?
- Are facts distinguished from inference?
- Were source references preserved?
- Were risks and dependencies considered?
- Was sensitive information excluded?
- Were registries updated where necessary?
- Was change history updated?
- Is the result usable by another authorised RSFA developer without additional context?
