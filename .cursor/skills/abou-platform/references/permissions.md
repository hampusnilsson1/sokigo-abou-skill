# Behörigheter

Source: *Behörighetsnivåer* (hub pageId `58524271`). Read 2026-08-25.

Three layers:

1. **Sysadmin** — Sokigo / hosting. Not assigned in the municipality UI.
2. **Systembehörigheter** — what the user may do in Admin (across services).
3. **E-tjänstebehörighet** — per e-tjänst.

Highest of individual + group wins. Without **AD**, users must exist as individuals even when rights are on a group: create users → create group and set rights → attach users to the group.

A user **cannot** grant themselves e-tjänst rights that expose case data in production (Läsbehörighet, Statusuppdaterare, Verksamhetsadministrator). That lock can be relaxed in **test**. They **can** give themselves **Redaktör** in production.

Import in **test** grants **Redaktör**. Editing the service in test also needs systembehörighet **Skapa och redigera e-tjänster**.

## Systembehörigheter

PageId `58524275` (continuation `58524215`).

| Behörighet | What it allows |
| --- | --- |
| Administrera behörigheter | Create/change/delete users; assign system and e-tjänst rights |
| Administrera vanliga frågor | FAQ under **Frågor och svar**; couple Q/A to a service or page |
| Publicera e-tjänster och blanketter (Menygrupper) | Menygrupper; publish services/blanketter into a group; reorder |
| Uppdatera vanliga texter | Citizen pages (Om e-legitimation, Så här funkar det, FAQ, Kontakta oss) and handläggarstöd text |
| Statistik och rapporter | Excel export (all services without case rows, or one service with case data — needs matching e-tjänst right); användningsmodul reports; kö/bokning Excel if those modules exist |
| Importera och exportera e-tjänster | Test ↔ prod. Export also needs e-tjänst right |
| Skapa och redigera e-tjänster | New services, edit (also needs at least **Redaktör**), linked services |
| Skapa och redigera köer | Create/change/delete queues; couple queues to services |
| Handlägga köer | Queue cases; needs kö module + e-tjänst right |
| Skicka in ärenden som ombud | Run a service as ombud; needs matching e-tjänst right **Skicka in ärende** |
| Skapa och redigera dokumentmallar | Document mallar |
| Administrera systemet | Tab **Administration**: organisations |
| **Redigera och exekvera Python-kod** | Create/edit Python in services. Trusted staff only — can alter data |
| Handlägga förslag | E-förslag module |
| Konfigurera schemaläggning | Create/change/delete scheduled jobs |

## E-tjänstebehörigheter (per service)

Handläggare pickable for tilldelning = users with **Statusuppdaterare** on that service.

| Right | Verksamhetsadmin | Beslutsfattare | Statusuppdaterare | Läs | Skicka in ärende | Redaktör |
| --- | --- | --- | --- | --- | --- | --- |
| See case list + PDF | yes | yes | yes | yes | | |
| Change status | yes | yes | yes | | | |
| Soft-delete case | yes | | | | | |
| Diarienummer, komplettering, tilldela | yes | tilldela + status | tilldela + status | | | |
| Beslut (Godkänn/Avslå) | | yes (service setting **Beslut**) | | | | |
| Loggbok read | yes | yes | yes | yes | | |
| Loggbok write/admin headings | yes | yes | yes | | | |
| Skicka meddelande | yes | yes | yes | | | |
| Booking slots (unreserved) | yes | yes | yes | | | yes |
| FAQ couple to service | yes | | | | | yes |
| Meddelandemallar + koppla notifiering | yes | | | | | yes |
| Upload docs/images for the service | yes | | | | | yes |
| Edit citizen-facing texts (name, pages, blocks, field help) | yes | | | | | yes |
| Grant others rights on this service | yes | | | | | |
| Generate blankett PDF | | | | | yes | |
| Ombud submit (also needs system **Skicka in ärenden som ombud**) | | | | | yes | |

**Redaktör** does **not** see cases. **Läsbehörighet** does not change anything.

Text editing includes: e-tjänstens namn, uppskattad handläggningstid (flik **Handläggningstider** / **Så funkar det** — not every graphic theme), handläggningsinformation, hjälptext on menygrupp, page name/body/right column, block rubrik/beskrivning, svarsalternativ (if enabled in builder), field help, text above/below field.

Cannot delete a meddelandemall that is still coupled to a service.
