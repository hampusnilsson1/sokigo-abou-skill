# Administrationsidorna

How-to for Admin screens. Do **not** open live cases unless the user asked. Rights: [permissions.md](permissions.md).

## Organisationer (from 3.36)

Flik **Administration → Organisationer**. **Skapa ny organisation**. Pencil = rename. Cross = delete only if no services (move them first). Changing a service’s org (**Allmänt → Ändra organisation**) also switches its PDF mall.

## Texter och bild

System **Uppdatera vanliga texter**. Flik **Texter**. Citizen pages + **Handläggarstöd**. Not sammanfattning/tacksida in the e-tjänst help column. **Välj roll**: only infotext + rubrik, not body. Images: upload under **Dokument** first ([document-templates.md](document-templates.md)). Generic theme: **Visa i meny**, **Ordning i menyn**; infobox above body. Tab **Lavinmeddelande**: banner on every external page ([functionality.md](functionality.md)). Sysadmin **Uppdatera innehåll** can set one banner for **all nodes**.

E-tjänst texts: left **Redigera texter** (needs **Redaktör** or **Verksamhetsadministrator**). Tabs **Sidtexter** (sidnamn, huvudrubrik, infobox) and **Block och fält** (hjälp, text ovan/under, sometimes svarsalternativ).

## Aktivera / inaktivera / öppettider

Production **E-tjänster → Allmänt → Aktivera/Inaktivera**. Active ≠ published. From **2019.5**: datetime when it becomes active; **öppettider** (needs **Skapa och redigera e-tjänster**). Seasonal: inactivate instead of delete.

## Publicering och menygrupper

System **Publicera e-tjänster och blanketter** → menu **Publicering**. Empty groups stay hidden even if activated. Header image 700×300 if the theme supports it.

Blankett on publish: none; generated from e-tjänst; URL/link (incl. `/FileStorageArea/…`); uploaded file (replace by uploading again). Optional **öppna i nytt fönster**. Unpublish: red cross.

## Import / export

System **Importera och exportera e-tjänster**. **Allmänt → Exportera tjänsten** → zip (short name + date). Import: **Importera e-tjänst**. Same kortnamn → overwrite or create new. Import grants **Redaktör**. Default statuses: Inkommet, Registrerat, Under handläggning, Avslutad. **Booking slots do not import**; Python `SlotFilter` code does.

## Ombud / forcera signering

**Skicka in som ombud:** system right + at least **Läsbehörighet** on the service. E-tjänster → open service → **Starta e-tjänst**. If login required: personnummer + **Invånaren har legitimerat sig**. From **2019.2** Sokigo can skip the sign step for ombud (logged as auto-signed).

**Forcera ärenden:** Sokigo enables. **Statusuppdaterare** can sign stuck **Väntar på medsökandes signatur** as ombud so handläggning can start.

## FAQ (Frågor och svar)

System **Administrera vanliga frågor**. Menu **Frågor och svar → Ny fråga**. Types: general; whole e-tjänst (citizen FAQ page); one page in the service. Linked e-tjänst: couple to the service, not to a page (pages are not in Abou).

## Behörigheter UI

Menu **Behörigheter**. First login: username = password, then change. Per-choice rights: [functionality.md](functionality.md) *Behörighet givet val*. LDAP: **Grupper → Synkronisera användare** ([functionality.md](functionality.md)).

## Integrationslogg

**Administration → Integrationslogg**. Needs **Administrera integrationsloggen** + **Administrera systemet**. Retry failed calls. From **2025.8**, cases under gallring that sit in the log are only **soft**-deleted and stay in the log; usually retry without restore.

## Permanent delete

From **2018.2**. **Administration → Ta bort ärenden permanent**. Must already be soft-deleted. Right **Permanent borttagning av ärenden**. Only the **current page** of the list is deleted; keep batches **&lt; 500**. Logged in **Systemhändelser**. Irreversible: relations, bookings, register links, signatures, files, PDFs, direct messages, loggbok. Nightly job then drops orphan citizens. E-förslag cases: from **2018.4**. Filters: status, e-tjänst, soft-delete date.

## Sök och ta bort invånare (from 2018.4)

Right **Ta bort invånare**. Counts engagements (cases, köplatser, future bookings, other region nodes) — **not** which sensitive services. Cannot delete while active case/köplats/future booking. Region: all nodes must be finished. Deletes the **personpost** only; fältsvar on finished cases remain until those cases are permanently deleted. Re-login recreates a personpost. Case-list personnummer search is a different index (fields vs personpost).

Do not copy example personnummer from the wiki into answers.

## Ta bort e-tjänst

**Allmänt → Radera e-tjänst**. Test: removes service + objects. Prod: must remove cases/köer/bokningar first.

## Statistik och rapporter

Right **Statistik och rapporter** (+ at least Läs on the service for case export).

- **Exportera ärenden:** one service = field answers; all services = no field content. Options: loggbok, invert axes, skip empty rows, include sekretess field answers (else “Sekretessmarkerade personuppgifter”).
- Payments / bookings / kö / e-förslag: need the matching module. Kö export includes special columns. Payments without case = failed checkout (refunds).
- **Antal ärenden:** month or year; e-tjänst vs app; optional blankett counts per month.
- **Användning:** cached overnight; all versions used in the last year. Custom range via **Ange egen översiktsrapport**.

## Systemhändelser

Sokigo enables; sysadmin **Felsökning**. Filter by type/time: deploys, config, deletes (case/service/Min sida/menygrupp/kö/integration/person), saves, admin login, users, rights, scheduled jobs, import, API users, email settings, document upload/delete.
