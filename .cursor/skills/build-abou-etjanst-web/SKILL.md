---
name: build-abou-etjanst-web
description: Build Sokigo Abou e-tjänster in the web builder. Documents PageNode/PageLogic libraries, integrations, and builder mallar. Use when creating, configuring, explaining, or reviewing Abou e-services — pages, fields, validators, Python, client JS, Navet, REST, payment, AD, EDP.
---

# Build an Abou e-tjänst in the web builder

Sokigo **Abou** e-tjänster are built in the **e-tjänstebyggaren** (layout builder). Sokigo must have enabled the builder. This skill is for **click-and-configure in the UI**, using Swedish builder names from Sokigo documentation.

Read [abou-web-guard](../abou-web-guard/SKILL.md) before any browser work. Stay on the docs or builder URL the user gave.

## Source

Official docs were ingested from logged-in Confluence (space Abou). **These skill files are the documentation** — the wiki is behind login and is not available to the agent.

- Builder + integrations: this folder (`references/`). Last read 2026-08-21.
- Platform (roles, Min sida, köer, REST, CitizenInfo, HtmlCaseModel, FAQ): [abou-platform](../abou-platform/SKILL.md). Last bulk read 2026-08-25.
- Do not send the user a dok.sokigo.com URL as the answer.

If a UI label in the live builder disagrees with these notes, **trust the live builder** and update the matching reference.

## These references are the documentation

`references/` is how agents **learn and explain** Abou — libraries, integrations, and builder behaviour — not a folder of files to open only when pasting a new script.

Read the matching file when you:

- Explain what Python, JavaScript, or an integration can do
- Choose between fältregler, klientlogik, and sidlogik
- Review or debug logic the user pasted
- Design a flow that uses Navet, REST, payment, AD, EDP, …
- Write or adapt Logik / Klientlogik

| Need | Documentation |
| --- | --- |
| PageNode / PageLogic / extra types | [logic-templates/libraries.md](references/logic-templates/libraries.md) then the API file |
| Official mall as a worked example | [logic-templates/INDEX.md](references/logic-templates/INDEX.md) — one mall |
| How an integration is used | [integrations/INDEX.md](references/integrations/INDEX.md) — one product file |
| Show/hide without code | [rules-validators.md](references/rules-validators.md) |
| Who may edit Python / see cases / publish | [abou-platform permissions](../abou-platform/references/permissions.md) |
| `self.Citizen` / GetCitizen / PersonPost JSON | [CitizenInfo](../abou-platform/references/technical/citizeninfo.md) |
| `@Model` in dokumentmall / ThankYouAdvanced | [HtmlCaseModel](../abou-platform/references/technical/htmlcasemodel.md) |
| External REST against cases | [Abou REST API](../abou-platform/references/technical/rest-api.md) |

Do not invent PageNode, `PageLogic`, or adapter methods. If it is not in the library or integration notes, say so.

## Workflow when the user wants a new e-tjänst

Ask only for what is missing, then give **builder steps**:

1. **E-tjänster → Skapa ny e-tjänst** and fill **Egenskaper** ([create-and-settings.md](references/create-and-settings.md)).
2. Add **layoutsidor**, blocks, and fields ([pages-and-fields.md](references/pages-and-fields.md), [field-types.md](references/field-types.md)).
3. Set **fältregler / visningsvillkor** before writing Python for show/hide or page skip ([rules-validators.md](references/rules-validators.md)).
4. Use **Pythonlogik** or **Klientlogik** only when the UI cannot do it. Read [libraries.md](references/logic-templates/libraries.md) for how the APIs work, then one mall from [INDEX.md](references/logic-templates/INDEX.md) if you implement.
5. If the service needs a register or backend (Navet, Bolagsverket, ByggR, REST, …), read **only** the matching file under [integrations/INDEX.md](references/integrations/INDEX.md) (how that integration is used). Do not load the whole integrations folder.
6. **Förhandsvisa e-tjänsten** on the page you are editing. Do not publish to production unless the user asked in this message.

Paste-here: if you cannot click the builder, describe the exact tab, field, and value. Ask the user to paste screenshots or confirm labels.

## Builder vocabulary (Swedish UI names)

Use these names when talking to the user:

| Builder name | Meaning |
| --- | --- |
| E-tjänstenamn | Citizen-facing title |
| Systemnamn | Unique code in the URL; a-z A-Z 0-9 `_` only; not åäö |
| Layoutsida | Normal page with blocks and fields |
| Sammanfattningssida | Summary before submit; no extra fields |
| Signeringssida / Sign | Sign with e-legitimation |
| Tacksida | After submit (`ThankYou` and variants) |
| Multipelsignering | Several signers (e.g. two guardians) |
| Fältregler | Show/hide/require other fields from a field’s answer |
| Visningsvillkor | Show a whole later page from an earlier field |
| Fältargument | Extra settings on a field (Hidden, Enabled, etc.) |
| Logik | IronPython on a page (`Initialize` / `GetNextPage`) |
| Klientlogik | JavaScript on a Layoutsida |

## Gaps (not in this docs tree)

These were **not** a complete IronPython or JS SDK on *Att bygga e-tjänster*:

- Python: library docs in [libraries.md](references/logic-templates/libraries.md) and [pagenode-api.md](references/logic-templates/pagenode-api.md); mallar are examples. ThankYou `IPythonCaseService` is extra sysadmin. Other Python is “kundens eget ansvar”
- JavaScript: [client/api.md](references/logic-templates/client/api.md). Other JS is “kundens eget ansvar”
- Navet **library** for barn/vårdnadshavare is documented in [navet.md](references/integrations/navet.md) plus mallar [navet-dropdown.md](references/logic-templates/navet-dropdown.md) / [navet-table.md](references/logic-templates/navet-table.md).
- The children-macro **Validatorer** (26 articles) on the hub did not resolve to live pages (404). Use [rules-validators.md](references/rules-validators.md) (*Konfigurera validatorer*).
- Navet integration page (`58524277`) describes PersonPost/NamnSökning and properties, **not** a `CitizenServiceProxy` API. Relation lookup is the builder mallar; method names in [navet.md](references/integrations/navet.md) are from those mallar.
- Most other integrations are product blurbs + Sokigo config. Only **EDP Future** publishes a Python method list.

## References

- [create-and-settings.md](references/create-and-settings.md) — new service, login, signing, service settings
- [pages-and-fields.md](references/pages-and-fields.md) — page types, default pages, adding fields
- [field-types.md](references/field-types.md) — builder field-type names
- [rules-validators.md](references/rules-validators.md) — field rules, page conditions, validators, field arguments
- [logic.md](references/logic.md) — where to write logic in the builder
- [logic-templates/libraries.md](references/logic-templates/libraries.md) — how PageNode, PageLogic, and extra types are used
- [logic-templates/INDEX.md](references/logic-templates/INDEX.md) — mallar as examples (pick one)
- [integrations/INDEX.md](references/integrations/INDEX.md) — how each integration is used (pick one)
- [document-templates.md](references/document-templates.md) — Dokumentmallar, blankett, editerbar PDF
- [builder-ui.md](references/builder-ui.md) — layout builder, preview, shortcuts
- [messages.md](references/messages.md) — emails, status notices, co-signer notify
- [catalog.md](references/catalog.md) — full article list under Att bygga e-tjänster
