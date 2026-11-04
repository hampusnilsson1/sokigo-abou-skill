---
name: abou-platform
description: Sokigo Abou platform docs outside the e-tjänstebyggaren — permissions, scheduling, Min sida, queues, modules, admin, case handling, REST API, CitizenInfo, HtmlCaseModel, GDPR/hosting. Use when explaining or configuring Abou admin, roles, Min sida, köer, schemaläggning, or technical/API behaviour — not when laying out builder pages.
---

# Abou platform (not the layout builder)

This skill **is** the Abou space on dok.sokigo.com minus *Att bygga e-tjänster* and *Integrationer* (those live in [build-abou-etjanst-web](../build-abou-etjanst-web/SKILL.md)).

The wiki is behind login. Agents **cannot** open it. Answer from these files. Do not send the user a Confluence URL as the answer. Do **not** open live Abou admin, Mina ärenden, or citizen cases to look around. Read [abou-web-guard](../abou-web-guard/SKILL.md) before any browser work.

## Source

- Ingested from logged-in Confluence space Abou (last bulk read 2026-08-25).
- Skip in this skill: Minut Bygg, Minut Miljö, Community presentations, webinar videos, full release-note bodies.

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
| Dokumentmallar, blankett-PDF, editerbar PDF | [document-templates.md](references/document-templates.md) |
| Admin pages (publish, import, organisations, …) | [admin.md](references/admin.md) |
| Ärendelista, loggbok, diarienummer | [cases.md](references/cases.md) |
| Bokningsmodulen | [booking.md](references/booking.md) |
| Registermodulen | [registers.md](references/registers.md) |
| E-förslag | [e-forslag.md](references/e-forslag.md) |
| Feature pages under Funktionalitet | [functionality.md](references/functionality.md) |
| FAQ (Q&A from the wiki) | [faq.md](references/faq.md) |
| Dela e-tjänster | [sharing.md](references/sharing.md) |
| Driftsättning / deploy notes | [operations.md](references/operations.md) |
| REST API (auth, methods, payloads) | [technical/rest-api.md](references/technical/rest-api.md) |
| CitizenInfo, HtmlCaseModel, GDPR, TLS | [technical/INDEX.md](references/technical/INDEX.md) |

Builder pages, fields, Python mallar: **not here** — use `build-abou-etjanst-web`. Adapter REST inside an e-tjänst is not this API.

## REST API (v2.4.4)

Use it when an **external system** reads or updates Abou: ärenden, komplettering, beslut, fältsvar, statistik, e-tjänster, register. Open [technical/rest-api.md](references/technical/rest-api.md) before naming a verb or path. Payloads, entities, and C# samples: [technical/abou-rest-api-v2.4.4.md](references/technical/abou-rest-api-v2.4.4.md) (Swedish; notes in that file mark errors in Sokigo's PDF — keep them, do not silently fix examples).

**Auth.** Sokigo recommends a token (Abou 2021.8+). `GET /api/authenticate` or `GET /api/authenticate/{ServiceShortName}` with `Authorization: Basic` + Base64(`UserName:ApiKey`). The body is a JWT; later calls send `Authorization: Bearer`. If the call has a service short name, fetch the token with that name. API user: **Behörigheter → API-användare**, checkbox **Kräv tokenbaserad anslutning**. Older option: `username` and `apikey` on the query string (checkbox off). Example host `https://abou.sokigo.com/api` is fictional.

**Calls.** 28 methods, mostly `/api/v2/services/{serviceShortName}/cases/{Method}`. Write/update (UpdateStatus, UpdateDiaryNumber, UpdateAdministrator, AddCitizens, FileUpload, CreateCase, NewDirectMessage, RequestSupplement*, CancelSupplement, CancelAllSupplements, UpdateFieldAnswers): **Statusuppdaterare**. Read (GetByDate*, GetByState, GetDetailed, *PdfDownload, AttachmentDownload, GetCaseListFromUserIdentity): **Enbart läsbehörighet**. DecisionOnExistingCase / DecisionToNewCase: **Beslutsfattare**. Outside that prefix: GetVersion, SearchServices, GetServices, ImportRegister (`PUT /api/v2/registers/ImportRegister`). GetDetailed does not return attachment bytes.

## Guardrails

- These notes are for **explaining and configuring**. They are not a licence to open production ärenden, impersonate, or change live data.
- Do not invent REST methods, Razor fields, or permission rights. If it is not in these files, say so. Naming the old wiki title in [catalog.md](references/catalog.md) is for maintainers filling gaps — not something to tell the user to open.
- Python in the builder still needs systembehörighet **Redigera och exekvera Python-kod** ([permissions.md](references/permissions.md)).
