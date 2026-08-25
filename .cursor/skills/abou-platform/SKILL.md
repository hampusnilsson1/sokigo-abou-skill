---
name: abou-platform
description: Sokigo Abou platform docs outside the e-tjänstebyggaren — permissions, scheduling, Min sida, queues, modules, admin, case handling, REST API, CitizenInfo, HtmlCaseModel, GDPR/hosting. Use when explaining or configuring Abou admin, roles, Min sida, köer, schemaläggning, or technical/API behaviour — not when laying out builder pages.
---

# Abou platform (not the layout builder)

This skill is the **Abou space on dok.sokigo.com minus** *Att bygga e-tjänster* and *Integrationer* (those live in [build-abou-etjanst-web](../build-abou-etjanst-web/SKILL.md)).

Purpose: agents **know where the knowledge is** and can answer from these files. Do **not** open live Abou admin, Mina ärenden, or citizen cases to look around. Read [abou-web-guard](../abou-web-guard/SKILL.md) before any browser work.

## Source

- Space hub: [Abou](https://dok.sokigo.com/display/ABOU)
- Last read: 2026-08-25 (logged-in Confluence)
- Skip in this skill: *Att bygga e-tjänster*, *Integrationer*, Minut Bygg, Minut Miljö, Community presentations, webinars, full release-note bodies

If a live UI label disagrees with these notes, **trust the live UI** and update the matching file.

## Do not load this whole folder

Start at [references/INDEX.md](references/INDEX.md). Read **one** topic file. Catalog of every page: [references/catalog.md](references/catalog.md).

| Need | File |
| --- | --- |
| Who can do what (system vs e-tjänst roles) | [permissions.md](references/permissions.md) |
| Nightly jobs, reminders, soft/permanent delete | [scheduling.md](references/scheduling.md) |
| Citizen portal, Att göra, villkor, versions | [min-sida.md](references/min-sida.md) |
| Köer (create, handlägg, payment, citizen flow) | [queues.md](references/queues.md) |
| Which add-on modules exist | [modules.md](references/modules.md) |
| Admin pages (publish, import, organisations, …) | [admin.md](references/admin.md) |
| Ärendelista, loggbok, diarienummer | [cases.md](references/cases.md) |
| Bokningsmodulen | [booking.md](references/booking.md) |
| Registermodulen | [registers.md](references/registers.md) |
| E-förslag | [e-forslag.md](references/e-forslag.md) |
| Feature list under Funktionalitet | [functionality.md](references/functionality.md) |
| REST API, CitizenInfo, HtmlCaseModel, GDPR, TLS | [technical/INDEX.md](references/technical/INDEX.md) |

Builder pages, fields, Python mallar: **not here** — use `build-abou-etjanst-web`.

## Guardrails (this skill does not authorise rummaging)

- These notes are for **explaining and configuring**. They are not a licence to open production ärenden, impersonate, or change live data.
- Do not invent REST methods, Razor fields, or permission rights. If it is not in these files, say so and point at the Confluence title in [catalog.md](references/catalog.md).
- Python in the builder still needs systembehörighet **Redigera och exekvera Python-kod** ([permissions.md](references/permissions.md)).
