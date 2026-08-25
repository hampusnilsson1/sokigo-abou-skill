# sokigo-abou-skill

Cursor skills for Sokigo [Abou](https://sokigo.com/produkter/abou/) e-tjänster (**Abou / Calamare**, not Open ePlatform).

Notes come from logged-in Sokigo Confluence (space Abou). Browser work is limited by `.cursor/skills/abou-web-guard/`.

## Skills

| Skill | Use when |
| --- | --- |
| `.cursor/skills/build-abou-etjanst-web/` | Build in **e-tjänstebyggaren**: pages, fields, fältregler, Python/JS mallar, Integrationer |
| `.cursor/skills/abou-platform/` | Everything else in the Abou space: behörighet, schemaläggning, Min sida, köer, moduler, admin, REST API, CitizenInfo, HtmlCaseModel, GDPR/eIDAS |
| `.cursor/skills/abou-web-guard/` | Before any browser call to dok.sokigo.com or a builder host |

Agents should open **one** reference file from the matching skill (`references/INDEX.md`), not the whole tree.

## Use in Cursor

Ask the agent to help **build an e-tjänst in the web builder**, or to explain roles, Min sida, köer, scheduled jobs, or the REST API. It should use Swedish UI names (Layoutsida, Fältregler, Verksamhetsadministrator, Köplatser, …).

## Builder docs

`.cursor/skills/build-abou-etjanst-web/references/` — builder behaviour, **library docs** (`logic-templates/libraries.md` for PageNode/PageLogic), **integration how-to** (`integrations/`), and mallar as examples.

## Platform docs

`.cursor/skills/abou-platform/references/` — start at `INDEX.md`. Catalog of Confluence pages outside the builder: `catalog.md`.

## Public sources

- [Sokigo Abou product](https://sokigo.com/produkter/abou/) — builder, registers, booking, payment, e-ID
- [Abou e-tjänstebyggande courses](https://sokigo.com/kurser/abou-e-tjanstebyggande-steg-1/) — pages, fields, validation, emails, publish
- [Provrummet](https://abou-provrummet.sokigohosting.com/DELAETJANST) — shared catalog; no legacy fältsidor
