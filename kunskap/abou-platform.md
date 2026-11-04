# Abou-plattform — kunskapsbas

All kunskap utanför byggaren: behörigheter, admin, ärenden, Min sida, köer, bokning, register, e-förslag, schemaläggning, dokumentmallar, FAQ, Funktionalitet, REST API 2.4.4 (metoder, payload, entiteter, C#), CitizenInfo, HtmlCaseModel, GDPR/TLS.

Detta är en **självständig kunskapsfil för RAG**. Svara från den här texten. Hitta inte på API:er, behörigheter eller fält som inte står här. Svenska UI-namn från Abou gäller. Referera inte till interna dokumentationsfiler.

---

# Abou space catalog (outside builder + integrations)

Ingested 2026-08-25 from Confluence space Abou.

**Already covered with the builder notes:** *Att bygga e-tjänster* and *Integrationer*. Do not duplicate those here.

**Not ingested (intentionally):** Release-note bodies, Community presentations, Webinar videos, Minut Bygg, Minut Miljö. On-prem hosting PDFs (headings only in compliance). Testpersoner personnummer (never copy into git).

**Abou REST API v2.4.4** (Sokigo PDF, 55 pages) is ingested in full, including notes on errors in the original (full text, method map).

## Abou (main hub)

### Administrationsidorna
Administrera Organisationer; Administrera Text Och Bild I Abou; Aktivera/Inaktivera E-Tjänst; Ange Öppettider För En E-Tjänst; Forcera Ärenden (Signera Som Ombud); Frågor Och Svar; Hantera Behörigheter; Hantera Dokument; Importera Och Exportera E-Tjänster; Integrationslogg; Menygrupper; Permanent Borttagning Av Ärenden; Publicera E-Tjänst Och/Eller Blankett; Skicka In Ärende Som Ombud; Statistik Och Rapporter; Systemhändelser; Sök Och Ta Bort Invånare (Personpost); Ta Bort E-Tjänst I Admin; Ändra Organisation För En E-Tjänst; Ändra Texter I E-Tjänster.

Notes. PDF/dokumentmallar.

### Ärendehantering
Ärendelistan Och Ärendedetaljvy; Ärendets Diarienummer; Handlägga Ärenden; Loggboken.

Notes.

### Behörighetsnivåer
Introduktion Behörigheter; Systembehörigheter; Systemadministrator; E-Tjänstebehörighet: Verksamhetsadministrator; Beslutsfattare; Statusuppdaterare; Läsbehörighet; Skicka In Ärende; Redaktör; Behörighet På Individ-Eller Gruppnivå.

Notes.

### Bokningsmodulen
Beskrivning; Handläggning Av Bokningar; Skapa Nytt Bokningstillfälle; Återkommande Bokningstillfällen; Boka Om Och Avboka; Konfigurera Bokningar; Bokningsmeddelanden.

Notes.

### Dela e-tjänster med andra
Notes.

### E-Förslag
Beskrivning; Skapa E-Tjänst För Att Lämna Förslag; Inställningar; Handlägga Förslag; Handlägga Kommentarer; Rösta Som Ombud; Läsa, Rösta, Dela Och Kommentera; Texter I Invånarvy; E-Förslagsmeddelanden.

Notes.

### FAQ
All Q&A pairs.

### Funktionalitet
Feature pages.

### Kömodulen
Beskrivning; Komma Igång; Skapa Ny Kö; Konfigurera En Kö; Handlägga Köer (+ byt köplats, digital betalning, lägg till manuellt, ta bort, uppdatera kontakt, uppdatera registreringsdatum, uppdatera status); Köbetalning; Köer: Hur Gör Invånaren; Köfilter; Kömeddelanden.

Notes.

### Meddelandemallar
Exempel; Exempel (multipelsignering); Koppla Meddelandemall Till E-Tjänst; Skapa/Redigera/Ta Bort; Statusnotifieringar; Värden I Meddelandemallar.

Builder-adjacent. Tokens. Razor model.

### Min sida
Att Göra; Beskrivning (2020.11 och tidigare); Direktmeddelanden; Händelser; Köplatser Och Bokningar; Publicering Och Villkorsstyrning; Tjänster.

### Min sida 2021.2 och 2024.2
Funktioner Som Stöds; Övergripande Beskrivning Min Sida Och Min Sida Plus; Video; Min sida efter 2024.2, med sidor som översta nivå.

Notes.

### Moduler
Schemaläggningsmodul; E-Förslagsmodulen; Betalningsfunktion; Min Sida; Användningsmodulen; Kömodulen; Bokningsmodulen; Register.

Notes.

### Projektdokument, Checklistor Och Processer
Kundservice/Support; Deployprocess; Checklista: Driftsättning Av E-Tjänst.

Notes.

### Registermodulen
Fokuswebinar; Beskrivning; Import Och Export; Redigera Register; Koppla Register Och E-Tjänst; Behörigheter För Register; Text/Värdeseparering.

Notes.

### Release notes
V26; 2025.11 … back through 2021 and earlier. **Not copied** into the skill (too large / version-specific). Ask Sokigo or the live wiki for a named version.

### Schemaläggning
Beskrivning; Ärendepåminnelser; Bokningspåminnelser; Köplatspåminnelser; Notifiering Vid Röstningsperiodens Slut; Signeringspåminnelse; Skapa Fil; Synkronisera Personuppgifter; Ta Bort Ärenden Mjukt; Ta Bort Ärenden Permanent; Uppdatera Status På Ärende.

Notes. From version **2018.2**.

### Teknisk Information & Dokumentation
Abou REST API; Ansvarsfördelning vid drift On Prem; CitizenInfo; HtmlCaseModel; Information Om GDPR; Penetrationstester Av Abou; Teknisk Kravspecifikation - Abou Intern Hosting; Testpersoner I Abou; Tillgänglighetsredogörelse; Vad Är EIDAS; Vilka Protokoll Stödjer Abou; Vilka Webbläsare Stödjer Abou.

Notes.

## Other top-level in the space

- **Community** — användarträffar, webinars (not ingested).
- **Minut Bygg / Minut Miljö** — other Sokigo products; do not open.

---

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

## API-användare (REST)

Not in the wiki tables above. Abou REST API 2.4.4: flik **API-användare** under **Behörigheter** (användarnamn, API-nyckel, **Kräv tokenbaserad anslutning**). Case calls use the e-tjänst rights **Statusuppdaterare**, **Enbart läsbehörighet** (Läs), or **Beslutsfattare**. System rights named only in that PDF: **Hämta ärendestatistik**, **Hämta e-tjänster**, **Importera register**. Map and payloads: REST API.

---

# Schemaläggning

Hub pageId `58524530`. Module from **2018.2**. Needs systembehörighet **Konfigurera schemaläggning**. Jobs are **per e-tjänst**. Menu: **Schemaläggning**. Add via **Lägg till schemalagd uppgift**. Tick **Aktiv** to run; untick to pause. **Spara ändringar** persists all jobs on the page.

Reminders need a meddelandemall coupled on the service with **När ska meddelandet skickas?** = the matching when (usually **Vid påminnelse** or **Signeringspåminnelse**). Recipients are the usual ones (sökande, handläggare, funktionsbrevlåda, e-post/SMS field).

Most reminder/file jobs run **once per day at 01:00**. Permanent delete runs **once per hour**.

## Job types

| Dropdown name | What it does |
| --- | --- |
| Skicka bokningspåminnelse | Hours before a booking |
| Skicka köplatspåminnelse | Days a köplats has had a given status (e.g. Erbjuden 3 days) |
| Skicka ärendepåminnelse | Days a case has had a given status |
| Skicka notifiering vid röstningsperiodens slut (e-förslag) | End of voting on an e-förslag service |
| Skicka Signeringspåminnelse | Unsigned medsökande / attest only (not those who already signed). Recurring or one-shot |
| Uppdatera status på ärende | Change status after N days in a status, or one-shot batch |
| Ta bort ärenden | **Soft** delete (flag; hidden in Abou) after status+time |
| Ta bort ärenden permanent | Hard-delete rows already soft-deleted. Sokigo must enable. Not for big one-off batches — use Admin **Permanent borttagning** |
| Skapa fil | File of cases or payments. Needs **CreateFilePlugin** (XML/FI, ordered separately). Types from site config (e.g. `.sie`) |
| Synkronisera personuppgifter | Refresh person data from configured register (usually Navet) for one service or all |

## Ärendepåminnelse parameters

Name; e-tjänst; **status**; **days in that status**; Aktiv.

Several jobs on the **same** service share the **same** reminder mall. The mail goes only for cases at **exactly** that day count — older cases are skipped.

Example: status *Väntar på medsökandes signatur* since 23 March → reminder 2 April 01:00 if days = 10.

## Signeringspåminnelse

Couple mall with when = **Signeringspåminnelse**. Job type **Signeringspåminnelse**, recurring or **Engångsjobb**.

## Skapa fil parameters

Name; e-tjänst; **Avser betalningar**; optional **status**; **För x dagar sen** or a fixed date; filtyp; Aktiv.

- Payments tick: include by payment day.
- Status only: include by status-change day.
- Both: payment date for that status.
- Neither: submit date.

## Synkronisera personuppgifter

Name; **Kör endast en gång** (else nightly); e-tjänst (empty = all persons with case relations); **Antal dagar sedan senaste synkronisering**; Aktiv.

Does **not** rewrite fältsvar. Dead / skyddade uppgifter show on **köplatser** after sync. Navet lookups cost money if the set is large.

## Soft / permanent delete

Soft: flag in DB; then permanent job (or Admin batch) erases. Permanent **cannot be undone**. Permanent job: name + e-tjänst + Aktiv.

## Status update

Name; one-shot vs recurring; e-tjänst; current status → new status; days since last status change.

---

# Min sida

Citizen portal. Module from **3.40**. Later hubs: *Min sida 2021.2 och 2024.2*. Login with e-leg.

Sokigo can hide undersidor from the menu (they still exist): **Köplatser och bokningar**, **Direktmeddelanden**, **Mina uppgifter**, **Mina ärenden**.

## Att göra (top of Min sida)

Built-in rows are buttons; each disappears when done.

| Activity | When it appears |
| --- | --- |
| Väntande betalning | Unpaid case → payment page |
| Väntar på medsökandes signatur / attestera | Logged-in person is medsökande or attestant (resurstext) |
| Kompletteringsbegäran | Caseworker asked for supplement |
| Beslut ej tagits del av | Decision PDF not downloaded yet (counts when they open the PDF link) |
| Sparade ärenden | Draft resume / delete |
| Sparat ärende där e-tjänsten ändrats | Restart or delete |
| Erbjudande om plats i kö | Status Erbjuden → ja/nej |
| Olästa direktmeddelanden | Open the thread |
| Egenkonfigurerade villkor | Extra e-tjänster published under Att göra (see villkor below) |

## Händelser (bottom)

Subset of case history: status changes on cases and köplatser; booking created/cancelled. **Visa** opens the case.

## Direktmeddelanden

Two-way thread in **logged-in** mode (e-leg). Needs the Min sida module. Caseworker always knows sender/recipient is the logged-in person.

- Handläggare can **always** start a thread from a case: case → tab **Direktmeddelande** → write → **Skicka meddelande**. Optional notifiering so the citizen logs in to Min sida.
- Citizen can start a thread only if the service setting **Tillåt invånaren att starta Direktmeddelanden** is on (**from 3.48**). Otherwise they can only reply in an existing thread.
- Ärendelista: **blue** speech bubble = unread; **grey** = thread exists, already read.
- Unread threads also appear under **Att göra**. Permanent case delete drops the messages .

## Publicering och villkorsstyrning

A service is **not** on Min sida until you publish it there. Admin top menu **Publicering → Min sida**.

Villkor is **code that returns True or False**. Input is the logged-in **citizen** object (personuppgifter). You can also key off dates. Pick a mall, then edit freely. **Testa**: type a personnummer/identitet in the box to the right — returns whether that person would see the item. **Do not copy real personnummer into git.**

### Under Tjänster

1. **Lägg till**
2. Choose e-tjänst
3. Display name (the Min sida link text)
4. Villkor mall for **Tjänster** → edit so it returns True/False
5. **Testa** if needed
6. **Spara**
7. Order: **Sortera** (alpha) or drag the list — matching services show in that order. **Ta bort** then pick another mall to switch template.

Typical villkor: age, parent/guardian, children’s age, fastighet, VA/avfall, always-visible, date window.

### Under Att göra

Built-in Att göra rows (pay, co-sign, …) appear automatically. Extra rows are e-tjänster that call a **verksamhetssystem**. Example: ByggR komplettering — villkor looks up ByggR; if the person has a pending komplettering the row shows (“Din bygglovsansökan behöver kompletteras”). **The villkor must become False after they complete the service**, or the row never leaves Att göra.

Same Lägg till / namn / mall / Testa / Spara / Sortera flow as Tjänster, but the mall list is the **Att göra** set.

## Versions

**2020.11 and earlier:** tabs like Min sida, Köplatser och bokningar, Direktmeddelanden, Mina ärenden, Mina uppgifter.

**Funktioner som stöds** on Min sida (2021.2 list):

- Signera som medsökande / attestera
- Ångra ärende not yet signed by medsökande
- Komplettera where the service allows it
- Komplettera when handläggare begärt komplettering
- Tacka ja/nej till köerbjudande
- Betala årlig köavgift
- Avboka bokning
- Ta del av beslut
- Ta del av handläggarbilagor
- Svara på direktmeddelanden

## Min sida efter 2024.2 (sidor som översta nivå)

From **2024.2** the top level is **sidor** (they appear in the toppmeny). Previously the top level was kategorier. A sida is text + **komponenter**. Two component types today (more may come):

| Komponent | What it is |
| --- | --- |
| **Inbäddad kategori** | Inline list (e.g. things to do, started applications) |
| **Bildkortsmeny** | Image you click to reveal the content |

Treat sidor as **permanent** menu entries so Min sida feels familiar. Show/hide **inside** the page (components and their content), do not hide the whole sida.

A sida is the CMS-like entry point for the **logged-in** person.

### Standard Min sida (not editable layout)

Two sidor:

1. **Att göra** — two inbäddade kategorier: **Att göra** and **Påbörjade ansökningar**
2. **Mina ärenden** — two bildkortsmenyer: **Pågående ärenden** and **Avslutade ärenden**

### Min sida Plus

Customers with Plus can arrange sidor and komponenter themselves. External content from other systems is often put on **own sidor**. Do not invent extra widget types; if the live site disagrees, trust the live site.

---

# Kömodulen

Add-on. Sokigo switches it on (no new deploy). Hub pageId `58525141`.

Citizen joins via an **e-tjänst with a köfält**. Case appears both in **ärendelistan** and under top menu **Köplatser**. Position = **registreringsdatum** (submit time); new cases go last. Removing a place renumbers. Status **Tilldelad** drops that place’s number so the rest move up.

## Prerequisites (Komma igång)

Builder must include:

- **Köfält** (required)
- **Integrerat personnummerfält** or login **before** the köfält (so the citizen can follow the place)

Then a kö-admin creates the queue(s).

| Task | Rights |
| --- | --- |
| Handlägga köer | System **Handlägga köer** + at least **Statusuppdaterare** on coupled services |
| Administrera köer | System **Skapa och redigera köer** + **Redaktör** or at least Statusuppdaterare on the service |

Optional: yearly digital payment (Swedbank Pay) via Min sida; extra columns; block duplicate places; Sokigo **köfilter** if column values come from service fields.

Payment amount in the e-tjänst **cannot** vary by which/how many queues the citizen picks.

If you delete a köplats, also update the **case** status in the ärendelista.

## Create queue

On the service: left **Köer** → **Skapa ny kö** → **Namn** (shown in the service if several queues, on Min sida, and to handläggare).

Settings:

| Setting | Effect |
| --- | --- |
| Tillåt flera köplatser per person | Same person may join again |
| Tillåt handläggare att ändra information i en köplats | Edit place info — only if the case was submitted **as ombud** |
| Tillåt handläggare att byta köplats | Move to an **existing** place; others shift |
| Tillåt handläggare att uppdatera registreringsdatum | Also updates case submitted date |
| Manuell betalning | Record a year paid outside Abou (invoice, etc.) |
| Status efter nekat erbjudande | Status if citizen says no |
| Erbjudandetext | Shown when status → **Erbjuden** |
| Maximalt antal platser | Integer; queue deactivates at that many **Erbjuden** or **Står i kö**. Empty = unlimited |
| Sista ansökningsdag | Deactivates after date |
| Specialkolumn 1–2 | Extra handläggare columns. Values from the e-tjänst need a Sokigo **köfilter** |
| Beskrivning | Admin only, not citizen |

## Handläggning (top menu **Köplatser**)

Search: personnummer, namn, adress, betalår, ombud vs invånare. Filter status. Excel export. Activate/deactivate queue. Link **Gå till kö** for settings (needs Skapa och redigera köer).

### Begära digital betalning

Needs yearly payment config, payment integration (Swedbank Pay), and the case **administreras av invånaren**.

- Whole queue: **Begär digital betalning** → all places without this year’s payment, citizen-administered, with a place number.
- One place: open place → same button.
- Reminders: button for everyone with an unpaid requested payment this year. Count shown in admin and on Min sida. Mall when: **Vid påminnelse-Betalningsbegäran** on the service tab for kömeddelanden.

Citizen pays from Min sida / Mina ärenden.

### Other actions

- Add person: **Skicka in som ombud** (same e-tjänst).
- Byt köplats / uppdatera registreringsdatum / ändra info: only if those flags are on.
- Status examples used in docs: **Står i kö**, **Erbjuden**, **Tilldelad**, **Nekad**, **Borttagen**. Confirm labels in the live UI.

## Kömeddelanden tokens

`$Comment$`, `$QueuePosition$`, `$QueueName$`.

---

# Moduler

Sokigo enables add-ons (often without a new deploy). Do not assume a site has a module.

| Module | What it is | Notes in this skill |
| --- | --- | --- |
| Schemaläggningsmodul | Nightly/hourly jobs | |
| Kömodulen | Waiting lists + köfält | |
| Bokningsmodulen | Slots / appointments | |
| Min sida (modul) | Citizen portal | |
| E-förslagsmodulen | Suggestions + voting | |
| Betalningsfunktion | Swedbank Pay (and others per integrations) | Builder: payment page; kö yearly fee in |
| Användningsmodulen | Usage stats / reports | Needs system **Statistik och rapporter** |
| Register | Lists for dropdowns / mapping | |

Hub: *Abou → Moduler*. Each child is a short product page pointing at the detailed section.

---

# Dokumentmallar och PDF

From version **3.26**. Tab **Dokumentmallar** in Admin. Right: **Skapa och redigera dokumentmallar**.

Older sites laid out PDFs in the database. The editor replaces that.

## What you edit

| Part | Typical use |
| --- | --- |
| Sidhuvud | Logo, heading |
| Sidfot | Contact, address |
| Ärende-mall Medborgare/Företag | PDF when a case is created |
| Beslutsmall Medborgare/Företag | PDF when handläggare fattar beslut — different text for Godkänt vs Avslaget |
| Ärendeblankett-mall | PDF from **Generera blankett**. Needs the customer mall’s special code |

Recommended: duplicate the complete **kund-mall**, then small changes per organisation or e-tjänst.

## Priority (content is taken from the first level that has a mall)

1. E-tjänst
2. Organisation (only if there is **no** e-tjänst mall coupled to that organisation)
3. Kund
4. Standard

Changes do **not** rewrite old PDFs already generated.

Editor actions: search (visible text / e-tjänst / organisation), filter malltyp, sort, add, **couple to e-tjänst or organisation**, duplicate, delete.

Razor object in the mall is **HtmlCaseModel** (`@Model`). Changing organisation on a service switches to that org’s PDF mall, else kund/standard.

These PDFs are **not** the same thing as **meddelandemallar** (e-post/SMS). A notifiering can *attach* the ärende-PDF or beslut-PDF. The HTML/Razor below is what Abou turns into those PDFs.

## Two PDF jobs (the ones customers edit most)

| Mall | When Abou generates it | Typical attach-on |
| --- | --- | --- |
| **Ärende-mall** (Medborgare/Företag) | When the case is created (after submit / after last medsökande sign) | Inkommet-mail, Min sida, Admin |
| **Beslutsmall** (Medborgare/Företag) | When handläggare **Godkänn** or **Avslå** | Beslutsmail, Min sida “ta del av beslut” |

Same editor, same `@Model`, different body: ärende-mallen is a **sammanfattning of answers**; beslutsmallen leads with **the decision** then usually repeats the answers.

Both are a full HTML document: `<style>` in `<head>`, Razor in `<body>` inside `@{ … }`. CSS is customer-owned (font, left margin, zebra `bgcolor="efefef"`, table ~80% wide, `th.table-key` ~45%). Use `<caption class="sr-only">` when a table has no visible heading. Screen-reader captions and `scope="row"` on the question cell are the a11y pattern.

Do **not** hard-code a municipality name, logo path, or inbox in the shared kund-mall if organisation mallar should differ — put those in sidhuvud/sidfot or org-level mall.

### Ärende-PDF — what the mall must do

1. **Title of the case** — `@Model.Service.DisplayName` (h1).
2. **Ärende meta** — at least `@Model.UniqueId` and `@Model.Submitted` (`ToString("yyyy-MM-dd HH:mm")`). If `@Model.FirstSignedByAll.HasValue`, show that timestamp as signed-time (nullable — guard it).
3. **Answers** — only pages that have data: `foreach (var page in Model.Pages)` + `if (page.HasAnyValues)`. Page title = `@page.DisplayName` (h2). Then `foreach (var block in page.Blocks)`. On a block page (`page.IsBlockPage`) the block header is a table `<caption>` when not empty.
4. **Fields** — `block.Fields`; skip empty with `Model.HasValue(FriendlyFieldId)`.
 - If the answer is itself a table (`Answer.Contains("<table ")`), print question as a full-width header and `@field.Answer` as HTML (do not escape).
 - Otherwise two columns: question | answer, zebra rows (`j++ % 2`).
5. **Payments** (optional) — `Model.Payments` with culture `sv-SE`: amount (`ToString("C")`), `OrderId`, `Date`. Skip the block if the list is null/empty.
6. **Signing**
 - **Alternativ signering** (`Model.IsSignedAlternatively`): empty lines for Datum/Ort and Underskrift (paper sign after print).
 - Else **sökande**: `Model.ApplicantSignature` — Submitted, `SignedBy.FirstName` + `LastName`, `SignedBy.SocialSecurityNumber`, `Issuer`, `Signed`.
 - **Medsökande**: `Model.SortedRecentCoApplicantSignatures` (same columns, loop).
 - **Attestanter**: `Model.SortedRecentAttestSignatures` plus `SignatureAttest.AnswerString` (Bevilja/Avslå), `Comment`, optional `Attachment.FileName`.
7. **Kompletteringar** — `Model.Supplements`: Title, DateRequested, DateCompleted, OriginalFileNamesJoined, CitizenComment. Skip empty strings.

Older mallar loop `page.Fields` instead of `page.Blocks` / `block.Fields`. New kund-mallar should use **blocks** so layout matches the builder.

`HasValue` vs printing every field: ärende-PDF that should hide unanswered questions uses `HasValue`. Editerbar PDF mallar sometimes print all fields as inputs instead.

### Beslut-PDF — what the mall must do

1. **Service name** + caption **Beslutat**.
2. **Decision block first** — `@Model.Decision.DecisionText` (Godkänt / Avslaget), `@Model.Decision.Date`, handläggare, `@Model.Decision.Comment`. The property for the caseworker name on Decision is spelled **`Adminstrator`** in the template model (no “i”). Null-check `Model.Decision` if a mall can render before a decision exists.
3. **Same answer dump as the ärende-PDF** (pages → blocks → HasValue fields).
4. **Signing on the decision PDF** is usually gated with `Model.Service.RequiresEid`. Then either the paper-sign blanks (`IsSignedAlternatively`) or the applicant row from `Model.Signatures.FirstOrDefault(s => s.SignatureType == …SignatureType.Applicant)`.
5. Leave room after the decision for **överklagandehänvisning** (CSS hook `.overklaga` is common). Different Godkänt vs Avslaget wording belongs in this mall (or in sidhuvud/beslutstext), not in the e-tjänst layout.

### Razor pitfalls in dokumentmallar

- Guard nulls (`FirstSignedByAll`, `ApplicantSignature`, `Payments`, `Decision`, attest attachment).
- Table-valued answers must be detected before you wrap them in a two-column `<td>` or the nested table breaks the PDF.
- Field answers that contain a raw `@` without `@Model["fältid"]` can break PDF generation.
- Date format in Swedish PDFs: `yyyy-MM-dd HH:mm`.
- Money: `CultureInfo.CreateSpecificCulture("sv-SE")` + currency format.
- Alternativ signering and e-leg blocks are mutually exclusive in a well-written mall (`IsSignedAlternatively`).

## Hantera dokument (file library)

Tab **Dokument**: upload then link as `/FileStorageArea/Documents/FILNAMN.ext`. Images on text pages must be uploaded here first. Select + **Ta bort** to delete.

## Editerbar pdf-mall

From builder tree *Editerbar Pdf-Mall*. For **internal** services: after submit, text fields in the case PDF stay editable in a PDF reader (`data-pdf-form-field="true"`). **Text fields only.** Typical flow: beställare fills page 1–2 → sends → mottagare edits in a PDF app → forwards internally (utförare/ekonomi) or back with quote details. Citizen/beställare can also edit and send the PDF on.

Demo on Provrummet: `/PDFtest`. Customer can do this themselves (~1 hour Sokigo help for the stock example).

### How to wire it

1. Tab **Dokumentmallar** — clone an existing mall or create new.
2. Tab **Medborgare** — edit the PDF mall look and behaviour.
3. Find the existing `Answer` output. There are **three** `Answer` sites; change only the **lower two**.
4. Replace:

```html
<td>@page.Fields[i].Answer</td>
```

with:

```html
<td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
```

5. Save and couple the mall to one or more e-tjänster.

Table cells with `AnswerContains("table")` stay as ordinary `@page.Fields[i].Answer` (not inputs). Alternate row colour: `bgcolor="efefef"` when `i++ % 2 == 0`.

### Kodexempel 1 — print every field (editable)

Intent: loop all pages and fields; non-table answers become PDF form inputs.

```
foreach (var page in Model.Pages) { var j = 0;
<table>
 <caption>@page.DisplayName</caption>
 <tbody> @for (int i = 0; i < page.Fields.Count; i++) {
 if (@page.Fields[i].AnswerContains("table")) {
 <tr bgcolor="efefef">
 <td colspan="2">@page.Fields[i].Question</td>
 </tr>
 <tr>
 <td colspan="2">@page.Fields[i].Answer</td>
 </tr>
 } else {
 if (i++ % 2 == 0) {
 <tr bgcolor="efefef">
 <td>@page.Fields[i].Question</td>
 <td>
 <input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/>
 </td>
 </tr>
 } else {
 <tr>
 <td>@page.Fields[i].Question</td>
 <td>
 <input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/>
 </td>
 </tr>
 }
 }
 }
 </tbody>
</table> }
```

### Kodexempel 2 — only pages that have values

Wiki heading: only fields the citizen filled. Outer guard is `page.HasAnyValues`. Inner `if (!Model.HasValue(...))` is **as on the Confluence snippet** — if a test mall skips the wrong rows, drop the `!` or the `HasValue` check. Nested `<tr>` under the table-answer branch is also as on the wiki.

```
foreach (var page in Model.Pages)
{
 if (page.HasAnyValues)
 {
 var j = 0;
 <table>
 <caption>@page.DisplayName</caption>
 <tbody>
 @for (int i = 0; i < page.Fields.Count; i++)
 {
 if (!Model.HasValue(@page.Fields[i].FriendlyFieldId))
 {
 if (@page.Fields[i].AnswerContains("table"))
 {
 <tr bgcolor="efefef">
 <td colspan="2">@page.Fields[i].Question</td>
 </tr>
 <tr>
 <td colspan="2">@page.Fields[i].Answer</td>
 </tr>
 }
 else
 {
 if (i++ % 2 == 0)
 {
 <tr bgcolor="efefef">
 <td>@page.Fields[i].Question</td>
 <td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
 </tr>
 }
 else
 {
 <tr>
 <td>@page.Fields[i].Question</td>
 <td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
 </tr>
 }
 }
 }
 }
 </tbody>
 </table>
 }
}
```

## Blankettgeneratorn

The e-tjänst **is** the blankett. Every **Ladda hem blankett** / **Generera blankett** (E-tjänster → Allmänt) uses the current service, so the paper form cannot go stale.

- Pages become sections; choice fields in two columns; list objects with prefix
- Help texts can print at the end: service **Inställningar → Visa hjälptexter i genererad blankett**
- Manual page breaks: page **Inställningar** or field **Avancerat**
- Header/footer follow ärende-PDF
- Signing block: Sokigo can require it on all blanketter or only e-leg services. In the **Ärendeblankett** mall, wrap “Sökandes underskrift” in `if (Model.RequireId) { … }` so unsigned services omit it
- Unique layout from 3.26 = this editor (customer-editable)

Publish as menygrupp type **Blankett genererad från e-tjänst**, or generate from Admin. Role **Skicka in ärende** can generate PDF. The blankett is **not** a fillable computer form — print, fill by hand, post.

---

# Administrationsidorna

How-to for Admin screens. Do **not** open live cases unless the user asked. Rights.

## Organisationer (from 3.36)

Flik **Administration → Organisationer**. **Skapa ny organisation**. Pencil = rename. Cross = delete only if no services (move them first). Changing a service’s org (**Allmänt → Ändra organisation**) also switches its PDF mall.

## Texter och bild

System **Uppdatera vanliga texter**. Flik **Texter**. Citizen pages + **Handläggarstöd**. Not sammanfattning/tacksida in the e-tjänst help column. **Välj roll**: only infotext + rubrik, not body. Images: upload under **Dokument** first . Generic theme: **Visa i meny**, **Ordning i menyn**; infobox above body. Tab **Lavinmeddelande**: banner on every external page . Sysadmin **Uppdatera innehåll** can set one banner for **all nodes**.

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

Menu **Behörigheter**. First login: username = password, then change. Per-choice rights: *Behörighet givet val*. LDAP: **Grupper → Synkronisera användare** .

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

---

# Ärendehantering

Menu **Ärenden**. Rights.

## Ärendelistan

Filters: statuses (all on by default), **Dina ärenden**, **Dölja avslutade**. Search: submit date, ärendetyp (only services you may see), status, diarienummer, ärendenummer, handläggare username or full name. Optional extra columns = chosen fältsvar. Click headers to sort.

## Detalj — actions

Default statuses (change under service **Inställningar**): Inkommet, Registrerat, Under handläggning, Avslutad.

| Action | Notes |
| --- | --- |
| Uppdatera status | Status list from the service |
| Ange diarienummer | Free text (letters/digits/symbols). Shown on Min sida and tacksida **instead of** ärendenummer unless hidden in service settings. List sort is **string** order (`1,10,11,2…`) |
| Begära komplettering | **From 2021.2: files only** (which files, explanation, optional instruction file, types, multiple). Notify with standard message when status **Väntar på komplettering**. Older: pick fields **Komplettera fält** then begär. **Ångra komplettering** exists. After supplement, multi-sign cases return to **Väntar på medsökandes signatur** |
| Tilldela handläggare | Selectable users = **Statusuppdaterare**. Optional personal text + attachments if tilldelning-mail is coupled |
| Ladda upp bilaga | Citizen sees on Min sida if linked. Optional **läskvitto**. Same allowed types/signature check as filuppladdning. Cannot delete ärende-PDF or beslut; other files are permanent delete |
| Godkänn / Avslå | Service setting **Beslut** + **Beslutsfattare** + person link. Comment and/or file; system builds beslut-PDF; download = läskvitto. Statusnotifiering Godkänd/Avslagen |
| Forcera / ombud sign | |
| Skicka meddelande | Needs login, integrated personnummer, or configured email field — builder |
| Ta bort | Soft delete |
| Loggbok | Headings defined **on the e-tjänst**. Same headings for all cases of that service. Cannot delete a heading that has entries; can close a heading for new entries. Deleted entries are struck through (who/when) and omitted from Excel. Read: Läs+; write: Statusuppdaterare+ |

**Läsbehörighet:** view + open attachments only.

## Diarienummer vs REST

UI **Ange diarienummer**, or REST `UpdateDiaryNumber` (PUT, **Statusuppdaterare**). Message when **När diarienummer sätts**. Payload: REST API.

---

# Bokningsmodulen

Sokigo add-on. Builder: **bokningsfält** + optional Python `SlotFilter`. Handläggare who create slots: at least **Statusuppdaterare**. Min sida avbokning needs login or integrated personnummer.

Use cases: personal meetings, rooms, group events with a seat cap. Combine with payment. Citizen: green days in a calendar, then times; optional pick handläggare; one or many slots. **Reservation** holds the slot for N minutes while they finish the flow.

## Admin tab **Bokningar**

Filter: handläggare, date range, Alla / Bokade / Helt obokade / Med lediga platser. Search visible text. Excel export = **booked** slots only. Unbooked → **Ta bort**. Booked → **Avboka** or **Boka om** (old time frees). Cannot edit date/time in place — delete and recreate (except seats).

### Create slot

Pick a service that has a booking field → **Skapa nytt bokningstillfälle**: date, start/end (end from **standardlängd**), optional handläggare (if **Använd handläggare för bokningar**), fritext (shown with the time), **antal platser**, **antal platser per bokning**.

Handläggare on the slot auto-assigns the **case** on book. Changing caseworker on the case does not change the slot; changing the slot later does not rewrite **existing** bookings. Multiple slots in one case → caseworker from the **first** selected slot. Unticking “använd handläggare” clears slot–user links.

### Recurring

Tick **Återkommande**, weekdays, interval, end date (default **6 months** if empty), exception dates. First occurrence is the **first matching weekday that week**, not necessarily the day you clicked — create that day as a single slot and start the series the week after. A series is one row in the list.

### Avboka / boka om

Admin: confirm avbokning (slot free again; avbokning-mail if configured). Boka om: pick a new free slot (avbokning + new booking mails). Citizen avboks from Mina ärenden until **deadline för avbokning** hours before start (`0` = until start). Admin is not limited by that deadline.

## Field arguments (bokningsfält)

| Argument | Effect |
| --- | --- |
| Tillåter flera bokningar | Several slots in the field |
| Max antal bokningar | Cap (with several) |
| Visar handläggare | Print name |
| Visar sluttid | `8:00-9:00` vs duration text |
| Tillåter multipla val | Several times the **same day** (with flera bokningar) |

## Service settings (Bokningar → Inställningar)

1. **Använd handläggare för bokningar** — required on create; auto-assign case
2. **Inkludera kalenderbokning** — `.ics` on the case; attach via bokningsmeddelande
3. **Standardlängd** — minutes
4. **Tid för reservation** — minutes held after pick (from 3.46; older = 20)
5. **Deadline för avbokning** — hours before start for the citizen

## Bokningsmeddelanden

Service **Redigera meddelanden → Bokningsmeddelanden → Lägg till ny**. When: **Bokning** (citizen book or admin rebook), **Avbokning** (citizen or admin), **Vid påminnelse** (scheduled). Prefer **Bokning** over “ärendet inkommit” as confirmation — inkommit does not mean a slot was booked. One mall per recipient (invånare / funktionsbrevlåda / handläggare). Tokens. Reminders.

---

# Registermodulen

Paid add-on. Tab **Register**. Shared choice lists (e.g. skolor) instead of duplicating rullistor or Python. Min sida display of registers was **not built yet** when the page was written.

## Create / import

**Visningsnamn** (required, editable, not unique), **systemnamn/kortnamn** (required, unique, **immutable**, same rules as e-tjänst kortnamn), beskrivning optional.

- **Skapa Register** — add rows in Admin
- **Importera register** — `.csv` (save Excel as CSV). Re-import **same kortnamn** **overwrites** the register. No sort/filter in Admin — edit in Excel then re-import.
- Delete only if **not** coupled (button grey).

Edits apply to running services without republishing. A resumed draft sees the new rows.

## Couple to e-tjänst

Builder **Inställningar → Koppla register**. One service can use many registers; one field uses **one** register (**Fältdetaljer / Svarsalternativ**). Register view lists coupled services.

Must exist in the **same environment**. Export service to prod → export register too unless kortnamn already exists there (**case sensitive**). Missing register → **import of the e-tjänst fails** with that systemnamn in the error.

## Rights

Anyone in Admin can **see** registers and coupling. Editors can couple. Create/update/import/export/delete in the UI needs system **Administrera Register**.

REST `ImportRegister` (`PUT /api/v2/registers/ImportRegister`) is a different entry. The API PDF names systembehörighet **Importera register**. It creates a register or overwrites one with the same SystemName and can couple it to e-tjänster. Payload: REST API reference.

## Text/värde

In a row: `visningstext:::värde` (three colons). Hidden value for fältregler / logikhopp.

---

# E-förslag

Module. Sokigo flags the submit e-tjänst in sysadmin so submit **creates a proposal linked to the case**. Right **Handlägga förslag**. Citizen list: `/Citizen/Proposal`. Filter via `?status=Godkänt&status=Avslaget` (space as `%20`).

## Map fields (integrationsargument `proposal`)

| Argument value | Meaning | Required |
| --- | --- | --- |
| Title | Rubrik | yes |
| Text | Brödtext | yes |
| File | Filuppladdning | no |
| SentBy | Inskickad av | no |
| Email | E-post | no |

Builder: field → **Integration → Nytt integrationsargument** → `proposal` / value. Extra fields stay on the **case** only. Prefer image-only uploads (files are public). Optional login + **kommunintillhörighet** (Navet) so only residents submit.

## Inställningar (Admin → E-förslag → Inställningar)

1. Cookie-only voting (IP stored; same browser cannot vote twice) **or** require personuppgifter (still cookies)
2. **Kräv inloggning för röstning** + **Kräv kommunintillhörighet** (needs Navet)
3. ReCaptcha keys (Sokigo per site) — graphic captcha is **not** recommended for a11y
4. **Tillåt kommentarer** / **Publicera kommentarer automatiskt**
5. Facebook share + delningsbeskrivning
6. **Livslängd (dagar)** — first vote day = publish day; last = publish + N − 1. Existing proposals unchanged if you edit the default
7. **Minst antal röster för beslut** → status **Inväntar ställningstagande** else **Avslutad**. Per-proposal override possible

## Handläggning statuses

**Inväntar publicering** (hidden) → edit title/text (logged in case history), optional public comment, tick **Publicerad** (shows period), or delete from e-förslag view (case remains). Link to case. Override vote threshold.

**Röstning pågår** — optional message **När antal röster uppnåtts**.

**Inväntar ställningstagande** — **Skapa beslutsunderlag** regenerates case PDF (tokens for vote count). Then Godkänt / Avslaget / Besvarat + motivering + optional file (replaceable later).

Comments: blue bubble = new; publish / publicera ej; can reverse.

**Rösta som ombud:** on the proposal; if login-voting, personnummer + name + legitimering; no duplicate SSN; kommun check if configured.

## Messages (e-tjänst → E-förslagsmeddelanden)

When: **Vid publicering**; **Vid förberedande för ställningstagande** (beslutsunderlag — typical funktionsbrevlåda + PDF); **Vid ställningstagande**; **Vid röstningsperiodens slut** (must combine with scheduled job **Skicka notifiering vid röstningsperiodens slut**); **När minst antal röster har uppnåtts**.

Citizen texts: resource strings on list + proposal page (button, empty list, vote/comment help).

---

# Funktionalitet

How Abou behaves after the builder. Builder how-to (pages, fields, Python mallar) stays in . FAQ. These notes are the knowledge — do not send the user to Confluence.

## Dokumentmallar / blankett / editerbar PDF

## Behörighet givet val i e-tjänsten

One choice field on the service (**Redigera e-tjänst → Inställningar → Behörighet per svarsalternativ**). Lets one e-tjänst serve several schools/förvaltningar: only some handläggare see cases with e.g. “Solbergaskolan”.

- Only **one field** per service; only kryssrutor / radioknappar / rullistor.
- Same **behörighetsnivå** even if several alternatives; works for Verksamhetsadmin, Statusuppdaterare, Läsbehöriga.
- If no per-alternative grants: everyone with the service right sees every choice.
- Also filters Excel: Exportera ärenden (one service), Exportera betalning, Exportera bokning.

**Grant:** Behörigheter → E-tjänster → service → **Ändra** beside **Behörighet per svarsalternativ** → tick alternatives → save. Case list then only shows matching cases.

**Watch:**

- Optional field left empty → everyone with the service right sees the case.
- **Alla behörigheter** = all alternatives including ones added later (so someone still sees new choices you forgot to grant).
- New alternative → grant it and save; consider a new notifieringsmall for that choice.
- Verksamhetsadmin can change **their own** per-alternative rights unless Sokigo enabled the behörighetsspärr.
- Existing cases are **not** retrofitted when you turn the function on later.

**Stale alternatives:** users still see old cases; if the same label comes back they regain it automatically. To strip stale grants: remove the service right entirely, save, re-grant. To grant a stale label the user never had: temporarily add the alternative in Redigera texter / Redigera e-tjänst, grant it, then remove it from the service again if it should stay unselectable.

**With “redaktör kan uppdatera svarsalternativ”:** warning in Redigera texter and Redigera e-tjänst (test and prod) if logic/integrations/behörighet can break.

**With “handläggare kan ändra svarsalternativ på inskickat ärende”:** dialog warns that the field drives rights; picking an alternative they do not have makes the case unavailable to them.

## Alternativ signering

Citizen can **Logga in och underteckna** (e-leg) or **Skriv ut och underteckna** (print, sign, post). Raises access for people without e-leg.

To get the case PDF without e-leg: integrated personnummer (Mina ärenden) **or** tacksida **PdfLinkThankYou.aspx** (from 3.26 without login). Admin shows the case as not signed with e-legitimation (signeringsinformation). When the paper PDF arrives, handlägg as usual.

## Förfylla från tidigare inskickat ärende

Same or another e-tjänst. Needs e-leg + **ärendeväljarfält** early + sidlogik (builder mall *Förifyll värden med Ärendeväljarfältet*).

## Komplettering med bilaga via Min sida

After submit. Login or integrated personnummer. **One file at a time** (each gets its own description) → Relaterade filer. Works even if the service has no filuppladdningsfält. Optional notifiering to handläggare / funktionsbrevlåda / invånare. Handläggare file-komplettering from 2021.2.

## Spara och återuppta ärende

Sokigo enables **system-wide**. Needs e-leg or integrated personnummer. **Spara** → **Mina sparade ärenden** (resume or delete). Resume restarts the flow from the beginning with answers prefilled (so they can change them). Only the **latest** save. Hide **Spara** per service Inställningar. If the service definition changed: they must fill again (info page). If inactivated: blocked. No time limit except gallring.

## Tilldelningsmall vid tilldelning av handläggare

Mail on **Tilldela handläggare** (including assigning yourself). Default on; disable per service **Redigera meddelanden → Skicka vid handläggartilldelning**. Optional extra personal text + attachments if the mall is coupled.

## Länkad e-tjänst

System **Skapa och redigera e-tjänster**. Create: tick **Länkad e-tjänst**, URL (incl. `http://`), optional iframe (height/width `%` or `px`, margins px; example 800px / 100% / 0 / 5 / 0 / 0), optional introduktionssida (**Redigera texter**). If not iframe, systemnamn is set automatically. Edit iframe later: **Redigera länkad e-tjänst**.

## Visa svar i ärendelistan (Admin)

One or more field answers in parentheses after the name, e.g. `Felanmälan (Vinterunderhåll)`. **Cannot** filter or search on them. Sokigo or customer config (videoguide on wiki).

## Visa svar i ärendelistan på Min sida

Field **Fältdetaljer → Visa under ärenden på Min sida**. Use when one person has many cases of the same type (e.g. child name on skolskjuts).

## Användningsmodulen

Add-on. Stats in a **Sokigo cloud store**, not the customer DB. From the moment Sokigo enables it. Cached **last night**. All service versions used at least once in the last year. No persons/cases (anonymous CaseId). No blankett/file stats. Multisite: also shows which kommun. Internal sites: not automatic.

Right: **Statistik och rapporter** → tab **Användning**.

Questions it answers: which services are used most/least; time to complete; where users abort; which pages; which validation errors; month-over-month %.

Three views: overview (optional **Ange egen översiktsrapport** for one service/node/date range); per service (only pages actually visited — logic-skip matters; compare versions that have data); per page (validation messages × field).

Stored (avpersonifierat): Date, InstanceId/Name, CustomerId/Name, Action (`Started` 0, `Cancelled` 1, `Published` 2, `Saved` 3, `Resumed` 4, `PageEntered` 5, `PageExited` 6, `ValidationFailed` 7), anonymous CaseId, ServiceShortName/DisplayName/Version, PageName/DisplayName, FieldName, FriendlyFieldId, TypeOfField, IsRequired, Question, ValidationMessage.

## Inloggning och signering

Login: any **SAML2** IdP. Methods: Mobilt BankID, Freja, Freja eID+, eIDAS.

Signing providers (avtal + Sokigo config): Twoday (f.d. Visma Sirius), CGI, Svensk e-identitet, Signport/KnowIT (fd Cybercom).

## Betalning via e-tjänst

Needs payment integration. Sysadmin: which service, amount, which page after **Avbryt** at the provider (Abou treats Avbryt as fail / felsida unless that return page is set). Pay now vs invoice = logikhopp. Variable amount = Python on Payment.aspx (builder mall). Tacksida **PaymentThankYou** shows payment info; currency label default `SEK`. No kvitto/faktura from Abou. Case details show amount, transaction id, datetime. Card/Swish etc. depend on the provider contract.

## Betalning via Min sida

Same integration. Use when payment in the service is optional, or for **årlig köavgift** (mail → log in → pay). List of unpaid cases; **Tillbaka** = fail → error page with link back to the payment overview. .

## Ombud / forcera signering

## Multipelsignering

Builder. FAQ for one vs two guardians. Field **Attestlista med sök** is **internal** attest (AD), not citizen guardians — see Attestering below.

## Ångra ett ärende som inte har signerats av medsökande

Service Inställningar **Tillåt sökande att ångra ärendet under Min sida** (off by default). While status is **Väntar på medsökandes signatur**, the applicant on Min sida can **Ångra ärende**. The case returns to **utkast** (spara/återuppta): they can change answers and submit again. Related setting **Tillåt sökande att ändra ärendet under Min sida** (builder / ) is the same family of “revert while waiting for co-sign”.

## Attestering

Variant of multipelsignering: one or more **attestanter** must answer (with e-sign) before the case is Inkommet and can be handlagd. Needs **inloggning**. Signing from the sökande is usual but **not** a technical requirement.

### Attestlista med sök

Searchable dropdown. Alternatives: `Efternamn|Förnamn|UID|E-postadress` (all four, pipe-separated). UID = personnummer **or** AD short name, depending how the site identifies users. Or Python `SetOptions`. Optional 5th help segment with `{1}` `{2}`. Common: AD lookup of the user’s chef (`InternalWebSearch`). Builder.

### Notifiering

Same as multi-sign: **När sökande har signerat (medsökande finns)** → **Till fält för invånare (E-post)** = the attest field id. Point them at Min sida.

### Flow

1. Sökande completes the service (optional own sign).
2. Status **Väntar på medsökandes signatur** (resurstext — often renamed **Väntar på attest**).
3. That “när sökande har signerat” mail goes out.
4. Attestant on Min sida **Att göra** sees **Signera som medsökande** (resurstext — often **Attestera ärende**).
5. Opens **Ärendesammanfattning**, picks an answer, optional comment/file.
6. From **V26** default answers are **Bevilja** and **Avslå**. Older **Besvara** is config-only (also in Admin ärendevy).
7. **Attestera** → signing provider → back to Min sida.
8. When all attestants have answered: status **Inkommet** — **regardless of Bevilja vs Avslå**. Then “när ärendet inkommit” mails; RestWrapper / ThankYou **PythonPlugin** can change status from the attest answers.

### Ombud / byt attestant

Like multi-sign: handläggare **Hantera attest** on the case — answer as ombud and/or change attestant.

## Värden som parametrar till e-tjänst (from 2019.2)

Query string `?namn=värde` (`&` between pairs) lands in `self.Service.SessionParameters` (string dict, **case sensitive**). Use to know *where* the service was started or to prefill. Builder mall: *Starta e-tjänst med parametrar i url och sedan använda dom* . Check `in` before indexing.

Example: `https://service.kommunnamn.se/GRUSK?skola=Lyckoskolan&årskurs=3` then Python can prefill school/year or skip pages.

## Mina meddelanden (DIGG)

Encrypted digital mailbox (Kivra, Min myndighetspost, Bring Digimail). Full product notes: builder .

- Citizen must have joined Mina meddelanden **and** chosen this kommun.
- Service needs **login or integrated personnummer** (lookup is on personnummer). Mallar must be coupled. Sokigo plugin + customer avtal.
- Separate body for e-post vs Mina meddelanden (falls back to e-post body). Same for företag → else invånare body.
- Only the **ärende-PDF** can be attached differently vs ordinary e-post. Other case files follow the notifiering tick (go to both).
- On **beslut**, case files **including the decision file** always go with the MM send.
- Does **not** replace SMS (SMS has its own mall).

## Redaktör kan uppdatera svarsalternativ i produktion (from 3.15)

**Redigera texter** in prod. Typical: seasonal stipend choices. Someone with **Skapa och redigera e-tjänster** must first tick the service Inställningar flag **in test**, then **import** to prod. Can break logic, integrations, and behörighet-per-alternativ — warnings when those are on.

## Handläggare kan redigera svarsalternativ på ett inskickat ärende

On **rullistor, kryssrutor, radioknappar**: field argument **Svar redigerbart av handläggare** = `True`. After submit, handläggare change that answer on the **ärendedetaljvy**.

Typical: felanmälan where the citizen picked the wrong förvaltning — change the choice so the case routes internally. If **Meddelande per svarsalternativ** is on, a **new** funktionsbrevlåda mail goes out for the new choice (builder ).

Combined with behörighet-per-alternativ: dialog warns that the field drives rights; picking an alternative they do not have makes the case unavailable to them.

## Synkronisera användare med AD

Only with **LDAP** AD login (not IdP). Rights live on **Abou groups that match AD groups**; users need not be created by hand. For mail, Abou still needs the user’s e-post — that is what sync fills.

**Behörigheter → Grupper → Synkronisera användare**: syncs every AD user who sits in an AD group that exists in Abou. Updates name/email; **creates** missing users. **Does not delete** a user who left the AD group (remove in Abou by hand). Synced users **cannot** be edited in Abou and **cannot** get individual e-tjänst or system rights — all via the group.

Import/create service: Redaktör is **not** auto-granted to the synced user; they pick **which group(s)** get the right.

**Sluta synkronisera** on the user: then edit rights in Abou (or inactivate to remove).

Lookups also run at login, on the rights UI, and when showing assigned handläggare. LDAP vs IdP product: builder .

## Krypterad e-post (tilläggsbeställning, from 3.28)

S/MIME on **standardmeddelanden**, aimed at funktionsbrevlådor. Needs cert on the server: encryption cert public `.crt`/`.cer` **and** signing cert private `.pfx`. Recipients need the matching private key to read. Price: kundansvarig.

Tick on the service: **Redigera meddelanden → Standardmeddelanden → Kryptera e-post**. Mall must **not** attach PDF / PDF to Mina meddelanden. **No attachments** on encrypted mail. Extra field content in the body = Razor mall.

## Lavinmeddelande

Banner on **all pages of the external UI** (maintenance, outage). Admin **Texter → Lavinmeddelande**. Right **Uppdatera vanliga texter** = this node. Sysadmin **Uppdatera innehåll** = all nodes in the install.

## Meddelanden per svarsalternativ

Funktionsbrevlåda to different addresses from choice fields. Several such fields allowed on one service. Full builder steps. One address per alternative; optional default address/mall/attachments when an alternative has no override.

## Skapa ett nytt ärende baserat på ett befintligt (from 2019.11)

Not “edit the old case”. A **kompletteringstjänst** maps fields onto a **ursprungstjänst** via integrationsargument. Sokigo enables **CaseServicePlugin**: on submit of the kompletteringstjänst it builds a **new** case from the original + new answers (version history kept). Original case can be closed or left unchanged. Sokigo also wires the two services. Use when a long-lived case must be updated without replaying the whole original e-tjänst (which may have changed).

## Skicka e-postmeddelande vid fel i Abou

Sysadmin mail to a fixed mailbox on failures, including: Paynova/payment, file upload, save case, update status, REST API in/out, menygrupp page load, menygrupp save in Admin, e-leg login, e-leg signing, outbound mail, Navet, SMS, other integrations.

Example: `Abou.Security.Eid.EidProvider.Logout` with Sirius — logout abort; citizen sees no error page, but ops still get mail.

## Stöd för olika typer av e-tjänster

| Type | Login/sign | Follow case | Extra |
| --- | --- | --- | --- |
| Ingen inloggning/signering | none | no Mina ärenden | |
| Koppling via integrerat personnummer | none | yes | optional file-komplettering (Inställningar) |
| E-leg | login + sign | yes | Navet/KIR prefill; field-komplettering handläggaren begär; optional file-komplettering |
| E-leg + multipelsignering | all sökande sign | all sökande | cannot handlägg until all signed |
| Med beslut | e-leg **or** integrated personnummer | yes | download of beslut = läskvitto (who/when) |

## Responsiv anpassning

Abou **always** ships a responsive citizen UI (phone / tablet / desktop). Wiki browser matrix is historical (iOS 5–9, Android 4.3–6, old Firefox/IE/Chrome/Edge) — do not treat as current support; browsers.

---

# FAQ (Abou Confluence)

Operational answers from the Abou space FAQ. Read 2026-08-25. Builder-only FAQ (Excel vs txt, several addresses on meddelande per svarsalternativ).

Do **not** invent extra Q&A. If the live product disagrees, trust the live UI.

## Ärende-PDF i mailnotifieringar

Attach the case PDF on the message mall (videoguide on the wiki). Coupling/attachments: builder .

## Fler taggar för sökfunktionen

**Publicering** → open the e-tjänst → field **Nyckelord att söka på** (right side, further down). Several words, comma-separated. Each tag must be **at least 3 characters** or it does not appear in search.

## Inga mail i testmiljön

Most test environments use a **generic mailbox** (e.g. a shared Gmail). Configured Abou mail in test goes there, not to the address you typed. Ask the Abou system owner which address receives test mail. Changing mail/password in test often also never arrives at the real user.

## Enbart Redaktör vid import

After the 2014 rights review, import grants **Redaktör** only so the importer does not automatically see incoming cases (personal data). Users **cannot raise their own** e-tjänst role even with system right **Administrera behörigheter**.

## Oracle istället för SQL

**No.** Abou does not support Oracle. Dual data stores would be a large product + customer cost.

## Vad kostar en Navet-slagning?

Wiki figures **from April 2016** (confirm current Skatteverket tariffs before quoting a price):

| Item | Wiki figure |
| --- | --- |
| Daily ändringsavisering | 1000 kr / quarter |
| Weekly ändringsavisering | 500 kr / quarter |
| Web service ePersondata (fixed) | 500 kr |
| Per personpost (ePersondata) | 0,03 kr |
| Per namnsökning | 0,50 kr |
| SHS/e-transport per post | 0,03 kr |
| Load/urval ≤ 2 000 000 posts | 0,03 kr / post |
| Load/urval > 2 000 000 posts | 0,01 kr / post |

More: Skatteverket. What data Navet can return: builder .

## Enkel vs avancerad grafisk anpassning

**Simple (typical Sokigo “enkel” package):** header, footer, font family/size for H1–H3 and body, up to **two** theme colours.

**Advanced:** three or more theme colours, fonts for ingress etc., content-driven formatting, custom icons, pixel tweaks, third-party search (e.g. SiteSeeker).

## Första inloggning — lösenord

New Abou user: **username as password** the first time, then change password. Same as .

## Dela e-tjänster med andra kommuner

There is a service on **Provrummet** used for this: *Dela e-tjänster med andra*. Details.

## Blankettgeneratorn

The generated blankett is **not** a fillable computer form. It is for people who print, fill by hand, and post. The e-tjänst is the source of truth: change the service → next generate uses the new layout. No separate blankett archive object is published; generation happens when the citizen (or handläggare) clicks blankett.

**Signing block on the blankett:** in the **Ärendeblankett** dokumentmall, wrap the “Sökandes underskrift” table in:

```
if (Model.RequireId)
{
 <label class="signLabel signLabelFirst">Sökandes underskrift</label>
 <table class="signTable">
 <tr><td><strong>Ort och datum</strong></td></tr>
 <tr><td><strong>Underskrift</strong></td></tr>
 </table>
}
```

If the e-tjänst does not require e-leg, that block is omitted.

**Publish a blankett link:**

1. Admin → **Publicering**
2. **Publicera ny e-tjänst/blankett**
3. Choose the service, tick **Blankett genereras från e-tjänst**
4. Save

The portal can then show **Till e-tjänst** and/or **Blankett**. The module must be enabled. Full behaviour.

## När görs AD-uppslag?

- User logs in
- Someone with rights admin opens the rights UI (update user / add user)
- Assigned handläggare is loaded/shown in the case list and on case details

Product: builder . Sync users.

## Handläggare notifierad när något hänt på dennes ärende

Configure a **statusmeddelande** to the assigned caseworker. Triggers:

- Citizen supplemented with a file
- Citizen supplemented one or more fields
- Another caseworker updated status (even just **Spara**)

## Funktionsbrevlåda till olika adresser beroende på val

Yes. Field **ServiceRequestEmail**: alternatives in a dropdown; each alternative maps to **one** email (same address may be reused). Mapping is **database configuration** (Sokigo). Typical: felanmälan by förvaltning, school services by school.

Builder also has **Meddelande per svarsalternativ** on choice fields — that is the self-serve field argument, not this ServiceRequestEmail DB map.

## Filtrera/söka i ärendelistan (Admin)

Date submitted, ärendetyp (only services you may see), status, diarienummer, ärendenummer, handläggare username. Optional extra columns = chosen fältsvar — **cannot** filter/search on those. .

## Vilka SQL-databaser?

Wiki list (historical): SQL 2012, SQL 2008 R2, SQL 2008; recommendation at the time was SQL 2012. **Do not treat as current hosting matrix** — ask Sokigo for the version you run.

## Visa/dölja fält direkt på sidan

Yes: **klientlogik** or **fältregler**. Builder and client mallar.

## Ibland en, ibland två signaturer (vårdnadshavare)

Build **multipelsignering**. The extra page has the second guardian’s fields plus a radio: sole guardian or not. If sole guardian, the other fields are not required (and vice versa).

Sokigo can also wire a **Skatteverket** check of one vs two guardians. Builder: *Multipelsignering*.

## Vilka data från Navet?

Among others: personnummer, namn, adress, civilstånd, födelseort. Full property list: builder .

## Roller (invånare, företag, förening)

**Removed in Abou 2022.5** — cannot enable on new services. Sokigo recommends turning roles off on old services; new product work does not support it.

Historically: system-wide “Välj roll” before the service (names configured globally). Service must have login. If the service is configured for only one role, that role is auto-selected. Could also use field **Integrerat fält för att välja roll** instead of the global page. **Content cannot follow the role by itself** — use Python on the field answer.

## Sparas medborgarens personuppgifter?

If the citizen uses a service **with e-legitimation**, personuppgifter are stored for the next e-leg service.

## Kan kunden editera sidor (text och bild)?

Yes: ordinary pages (Kontakta oss, FAQ, Handläggningstider, …) in Admin. E-tjänst editorial (help, tacksida) too. Links and images: upload under **Dokument** first. .

## Kan ärendet skrivas ut?

Yes — the case PDFs (logo, per-step answers). Handläggare: Admin or functional-mailbox attachment. Citizen: Mina ärenden; optional PDF on thank-you mail / tacksida. Decisions also become PDFs.

## Följa var i processen ärendet är

1. Mina ärenden (case must be tied to the user)
2. Statusmeddelande on status change (e-post, SMS, historically Facebook) — same coupling
3. Optional SLA / estimated handläggningstider in the theme

## Hindra inklistring av e-post (ange två gånger)

Field type **E-postfält (EGovEmailField)** → validator **E-post (EmailValidator)** → argument **`verify`**. Extra field **Verifiera e-post**: no cut-and-paste, must match.

## Format på ärendenummer

`ÅÅMMDD-KORTNAMN-xxxx` e.g. `130925-BVL-GY09` (date submitted, service short name, two random letters + two digits). Sokigo can configure **unidentifiable** numbers for sensitive services.

## Hjälptexter på enskilda fält

1. Help button beside the field, or
2. Hover tooltip

Builder: field help text.

## E-legitimationsleverantörer (FAQ list)

Wiki FAQ names: CGI (fd Logica), Visma Sirius, BankID, Nordic Edge, Svensk e-identitet, Medborgarkonto from Svensk e-identitet.

**Current signing providers** on the Funktionalitet page (prefer this): Twoday (f.d. Visma Sirius), CGI, Svensk e-identitet, Signport/KnowIT (fd Cybercom). Login: any SAML2 IdP; methods Mobilt BankID, Freja, Freja eID+, eIDAS. Avtal + Sokigo config. .

## AD — vad är det?

Microsoft Active Directory for **internal** login (LDAP or IdP). Full product notes: builder . When lookups run: section above.

---

# Dela e-tjänster med andra

**Provrummet** is Sokigo’s shared catalog of e-tjänster that customers have built in Abou. You can **test** those services there and **export** them, then **import** into your own Abou.

To publish one of yours into Provrummet, Sokigo provides an e-tjänst on Provrummet named **Dela e-tjänster med andra**. That is not the same as Admin zip export between your own test/prod.

After import: only **Redaktör** is granted (, ). Booking slots do not import; Python `SlotFilter` code does. Rights and editorial texts follow the usual import rules .

---

# Checklista och deploy

## Checklista: driftsättning av e-tjänst

### First time (service not in prod yet)

1. Export in **test**
2. Import in **prod** (grants **Redaktör** only — , )
3. Tell Sokigo if the service needs **database wiring** they own (payment, bokning, …) and **when** you will go live
4. Set handläggare/redaktör rights — **rights do not travel with the import**
5. Submit a **test case** in prod: logic, texts, messages, PDF. Warn whoever owns the funktionsbrevlåda
6. Publish under the menygrupp(er) citizens should use
7. Put the link on the municipal website: `https://<host>/<kortnamn>` (example pattern `https://eservice.engelholm.se/ABOU01`)

### Change to a service that already exists in prod

1. Export **prod**
2. Import that zip into **test** (so test matches live)
3. Edit in **test**
4. Export **test**
5. Import into **prod** — normally **do not** take editorial texts with the import
6. Submit a test case again; warn the funktionsbrevlåda owners

Also: publishing ≠ activating; empty menygrupper stay hidden; blankett is a separate publish tick; Python needs **Redigera och exekvera Python-kod**; ThankYou Python plugin may need app-pool recycle (builder ); test mail often hits a generic mailbox ; do not delete a production e-tjänst until cases/köer/bokningar are gone .

## Deployprocess (Sokigo platform release)

Customer-facing process for a **new Abou version** (not the same as importing one e-tjänst — that is the checklist above). Sokigo usually books a **full day** (deploy + their tests).

### Cadence

1. Deploy to **test**
2. Customer has **2–3 weeks** to test and feed back
3. Sokigo adjusts
4. Deploy to **prod** (usually faster than test)

### What Sokigo does on each environment

**Test:** systemtest + funktionstest after deploy. Kundansvarig reports results (often same afternoon or next day). During deploy they **lock** the platform; visitors see a maintenance text (standard texts exist; customer can choose wording, e.g. estimated date/time).

**Prod:** same tests, same lock, results usually **the same day**.

### After go-live

- Support: `kundservice@sokigo.com`
- The site is on the **latest** Abou version; new features/fixes are listed per release (not copied into this skill)
- Cost of a deploy: ask kundansvarig

Do not invent IIS slots or who clicks the actual deploy.

---

# Tokens in meddelandemallar

Source: *Värden i meddelandemallar* (pageId `60096729`) plus builder messages notes. Read 2026-08-25.

Always `$name$` (case-sensitive: `$serviceName$` not `$ServiceName$`). Field answers: Razor `@this.Model["AVB.2"]` (FriendlyFieldId). Razor **does not** work in **scheduled reminder** mallar or in SMS.

If you write a field id with a raw `@` in the answer and skip `@Model[]`, PDF generation can fail.

How to write status/kö mail and couple attachments: see meddelandemallar (when/to/attachments). HtmlCaseModel is the Razor object in dokumentmall and in e-post that uses `@Model`.

## General

| Token | Meaning |
| --- | --- |
| `$uniqueID$` | Ärendenummer |
| `$registrationNumber$` | Diarienummer |
| `$serviceName$` | E-tjänstens namn |
| `$administrator$` | Assigned caseworker username |
| `$administratorName$` | Assigned caseworker full name |
| `$caseID$` | Internal case id |
| `$customerName$` | Municipality / node name |
| `$customerUrl$` | Abou base URL |
| `$dateSubmitted$` | Submit date |
| `$dateSubmitted6$` | Submit timestamp |

Min sida case URL pattern (builder docs): `…/Citizen/MyPage2#/cases/$uniqueID$`.

## Citizen (needs login or integrated personnummer)

`$citizenName$`, `$citizenFirstName$`, `$citizenLastName$`, `$citizenMobileNumber$`, `$citizenHomePhoneNumber$`.

## Kö status notices

`$Comment$` (manual status comment), `$QueuePosition$`, `$QueueName$`.

## Bookings

`$ReservationDate$` (single booking only), `$ReservationSpots$`, `$ReservationUTCStart$`, `$ReservationUTCEnd$` (e.g. `2022-12-14T09:00:00`). All occasions: `@this.Model["fältId"]`.

## Payments (Razor)

`@Model.ApplicantPayment.Amount`, `.TransactionId`, `.PayedBy`.

---

# Technical documentation

Hub: *Teknisk Information & Dokumentation*. Read 2026-08-25.

| Need | File |
| --- | --- |
| REST API v2.4.4 — auth, methods, then the full PDF text | method map, full text |
| `self.Citizen`, Citizen vs CitizenInfo, Navet/KIR mapping | |
| `@Model` Razor in dokumentmall, e-post, ThankYouAdvanced | |
| GDPR, eIDAS, TLS, browsers, WCAG, pentest, hosting | |

**Testpersoner i Abou:** official Sokigo test identities (including sekretess / avliden). Use that Confluence page for numbers — do not copy personnummer into git.

**Ansvarsfördelning vid drift On Prem** and **Teknisk kravspecifikation - Abou Intern Hosting** are PDFs on Confluence; not transcribed here.

**Abou REST API v2.4.4** is transcribed in full (Sokigo PDF *Abou REST API v2_4_4*, 55 pages) in the full REST reference. Start at the method map (when to call, token vs API key, method table). A 2026-08-25 note called the PDF version 2.5.2 and omitted schemas; that version label is not in the verified document. Ask Sokigo support for the real host and test credentials — do not tell the user to log into the wiki.

---

# Abou REST API

External systems call **Abou REST API V2**. This file is the method map. Payloads, entities, C# samples, version history, and notes that mark errors in Sokigo's original PDF are in the full REST reference. Copy URLs, verbs, and property names from that file. Do not invent methods or fields.

Source: Sokigo *Abou REST API v2.4.4* (original file *Abou REST API v2_4_4*, 55 pages; created 2025-02-18, modified 2025-03-07). A Confluence ingest on 2026-08-25 labeled a PDF "version 2.5.2" and stored only method names. That version label is **not** in the verified document. Do not add methods from it.

Not this API:

- Python **Adapter REST** / `IRestWrapperServiceFactory` (named sysadmin config inside an e-tjänst) — Adapter REST.
- `self.Citizen` / CitizenInfo, and Razor `@Model` / HtmlCaseModel.

Example host `https://abou.sokigo.com/api` is fictional. Ask Sokigo support for the real base URL and test credentials. Do not send the user to the wiki.

## When to use it

Use it when an external system must read or change Abou data: case lists and detail, status, diarienummer, handläggare, invånare, files, create a case, direktmeddelande, komplettering, beslut, fältsvar, API version, ärendestatistik, published e-tjänster, or register import.

Read methods need e-tjänst right **Enbart läsbehörighet** (the Läs column under Behörigheter). Updates need **Statusuppdaterare**. Decisions need **Beslutsfattare**. Three system rights are named in the PDF and are not in the wiki systembehörighet table: **Hämta ärendestatistik**, **Hämta e-tjänster**, **Importera register**.

## Auth

From Abou **2021.8** there are two options. Sokigo recommends the token.

API users are administered under **Behörigheter → API-användare** (användarnamn, API-nyckel, checkbox **Kräv tokenbaserad anslutning**).

### Token (preferred)

1. `GET /api/authenticate` or `GET /api/authenticate/{ServiceShortName}`.
2. Header: `Authorization: Basic ` + Base64(`UserName:ApiKey`).
3. The body of HTTP 200 is a JWT. 401 = unauthorized, 500 = server error.
4. Send `Authorization: Bearer <token>` on every later call.
5. If the later call includes `ServiceShortName`, fetch the token **with** that short name.

Token mode requires **Kräv tokenbaserad anslutning** on the API user.

### API key (older)

`username` and `apikey` as query parameters in clear text, for example `.../cases/UpdateStatus?username=userName&apikey=apiKey`. Turn **off** **Kräv tokenbaserad anslutning** for that user.

## Methods

28 methods plus Authenticate. `{serviceShortName}` is the e-tjänst kortnamn. Most case methods are under `/api/v2/services/{serviceShortName}/cases/`.

| Method | Verb | Path | Right |
| --- | --- | --- | --- |
| Authenticate | GET | `/api/authenticate` or `/api/authenticate/{ServiceShortName}` | Basic (UserName:ApiKey) |
| UpdateStatus | PUT | `.../cases/UpdateStatus` | Statusuppdaterare |
| UpdateDiaryNumber | PUT | `.../cases/UpdateDiaryNumber` | Statusuppdaterare |
| UpdateAdministrator | PUT | `.../cases/UpdateAdministrator` | Statusuppdaterare |
| AddCitizens | PUT | `.../cases/AddCitizens` | Statusuppdaterare |
| FileUpload | POST | `.../cases/FileUpload` | Statusuppdaterare |
| GetByDateAndState | POST | `.../cases/GetByDateAndState` | Enbart läsbehörighet |
| GetByDate | POST | `.../cases/GetByDate` | Enbart läsbehörighet |
| GetByState | POST | `.../cases/GetByState` | Enbart läsbehörighet |
| GetByDateTimeAndState | POST | `.../cases/GetByDateTimeAndState` | Enbart läsbehörighet |
| GetDetailed | POST | `.../cases/GetDetailed` | Enbart läsbehörighet |
| CasePdfDownload | POST | `.../cases/CasePdfDownload` | Enbart läsbehörighet |
| DecisionPdfDownload | POST | `.../cases/DecisionPdfDownload` | Enbart läsbehörighet |
| AttachmentDownload | POST | `.../cases/AttachmentDownload` | Enbart läsbehörighet |
| CreateCase | POST | `.../cases/CreateCase` | Statusuppdaterare |
| NewDirectMessage | PUT | `.../cases/NewDirectMessage` | Statusuppdaterare |
| GetCaseListFromUserIdentity | GET | `.../cases/GetCaseListFromUserIdentity?userIdentity={userIdentity}` | Enbart läsbehörighet |
| RequestSupplementExistingCase | POST | `.../cases/RequestSupplementExistingCase` | Statusuppdaterare |
| RequestSupplementNewCase | POST | `.../cases/RequestSupplementNewCase` | Statusuppdaterare |
| CancelSupplement | POST | `.../cases/CancelSupplement` | Statusuppdaterare |
| CancelAllSupplements | POST | `.../cases/CancelAllSupplements` (URL example in the PDF: `CancelAllSupplement`) | Statusuppdaterare |
| DecisionOnExistingCase | POST | `.../cases/DecisionOnExistingCase` | Beslutsfattare |
| DecisionToNewCase | POST | `.../cases/DecisionToNewCase` | Beslutsfattare |
| UpdateFieldAnswers | PUT | `.../cases/UpdateFieldAnswers` | Statusuppdaterare |
| GetVersion | GET | `/api/v2/services/cases/GetVersion` | (none stated) |
| GetCaseStatistics | GET | `.../cases/GetCaseStatistics` | System: Hämta ärendestatistik |
| SearchServices | GET | `/api/v2/services/SearchServices?Searchstring={query}` | (none stated) |
| GetServices | POST | `/api/v2/services/GetServices` | System: Hämta e-tjänster |
| ImportRegister | PUT | `/api/v2/registers/ImportRegister` | System: Importera register |

`...` means `/api/v2/services/{serviceShortName}`.

Case lists return ärendenummer. **GetDetailed** returns the case as XML (or JSON if `Accept: application/json`). Attachment **Content is empty** in that response; use CasePdfDownload, DecisionPdfDownload, or AttachmentDownload (SystemFileName from GetDetailed). **FileUpload** is multipart (`CaseBaseRequest` plus one part per file), not a single JSON body. **ImportRegister** creates a register or overwrites one with the same SystemName and can couple it to e-tjänster. UI CSV import is a separate path and uses systembehörighet **Administrera Register**.

Komplettering and beslut can pass Arguments (`ConfigurationDataKey`, `ServicePurpose`, optional `IncludeCaseParameters`) so **RestwrapperPlugin** calls another system when the citizen completes the supplement or downloads the decision the first time. The plugin and its configuration must already exist.

## Entities

Property tables are only in the reference: RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse.

`*` in the Obl column means strictly required. `-` means required only in the case the description states.

## Errors kept from the original PDF

The reference quotes the PDF and marks mistakes. Do not "correct" them when copying an example. The ones that change a call:

- **CancelAllSupplements.** The URL example ends with `CancelAllSupplement` (no final s). Version history: new in API 2.4.4, Abou **2025.3**. The method table says Abou release **2023.2.0.0**.
- **AttachmentDownload.** The method path is `.../cases/AttachmentDownload`. The C# sample calls `.../cases/CaseAttachmentDownload`.
- **UpdateFieldAnswers** sample JSON is missing commas after `Comment` and `Answer`.
- **GetServices** result sample uses `=` instead of `:`. **SearchServices** result sample has a trailing comma.
- **GetDetailed** contents list says attachments include Content; the method text says they do not. In the data block, OmitXmlDeclaration is marked `(5` and described by footnote 6. Property name in the PDF: `IncludeAllAttachements`.
- **CreateCase** repeats the sentence "När man hämtar ett detaljerat ärende…".
- **DoPublishPdf** on CaseUpdateFieldAnswersRequest stops mid-sentence ("…genereras på nytt för att").
- Title-page footer says **2.4.3**; the title says **2.4.4**.
- C# samples keep original typos (`URI.EscapeDataString`, doubled parentheses, `stringContents` in GetByDateAndState).

## C# and testing

The reference has .NET `HttpClient` + Newtonsoft.Json samples (token, FileUpload, the read/update methods, CreateCase). The PDF says to try calls with Postman or the Chrome extension YARC. Bearer examples use the token from Authenticate.

---

# Abou REST API 2.4.4

Dokumentation från Sokigo AB (Addnode Group) av Abous REST API V2, version 2.4.4. Titelsidan har rubriken ”Abous REST API 2.4.4” och visar Sokigos logotyp (SOKIGO, ADDNODE GROUP). Sidfoten på titelsidan anger ”Abou REST API 2.4.3” samt ”Sokigo AB sokigo.com/vara-produkter/abou info@sokigo.com”.

## Innehåll

- Versionering
- Inledning
- Autentisering (Tokenbaserad autentisering, Hämta token Authenticate, Autentisering med API-nyckel)
- Snabböversikt över API-metoder
- UpdateStatus – Uppdatera status för ett ärende
- UpdateDiaryNumber – Uppdatera diarienummer för ett ärende
- UpdateAdministrator – Uppdatera handläggare för ett ärende
- AddCitizens – Uppdatera ärende med invånare
- FileUpload – Bifoga filer till ett ärende
- GetByDateAndState – Hämta ärendenummer inom ett datumintervall och status
- GetByDate – Hämta ärendenummer inom ett datumintervall
- GetByState – Hämta ärendenummer för ett eller flera status
- GetByDateTimeAndState – Hämta ärendenummer med statusuppdatering inom ett datumintervall med klockslag och status
- GetDetailed – Hämta ett detaljerat ärende (inkl. Bilagor och dess innehåll, Content)
- CasePdfDownload – Hämta ärende-PDF
- DecisionPdfDownload – Hämta ett ärendes besluts-PDF
- AttachmentDownload – Hämta en specifik bilaga från ett ärende
- CreateCase – Skapa nytt ärende
- NewDirectMessage – Skapa direktmeddelande
- GetCaseListFromUserIdentity – Hämta en lista av ärendenummer för ett personnummer
- Begäran om komplettering (RequestSupplementExistingCase, RequestSupplementNewCase, CancelSupplement, CancelAllSupplements)
- Delgivning av beslut (DecisionOnExistingCase, DecisionToNewCase)
- UpdateFieldAnswers – Uppdatera fältsvar på ett befintligt ärende
- GetVersion – Hämta befintlig version av Abou API
- GetCaseStatistics – Hämta ärendestatistik för en specifik e-tjänst
- SearchServices – Söka bland publicerade e-tjänster
- GetServices – Hämta information för en specifik e-tjänst
- ImportRegister – Import register
- Entiteter (RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse)
- Kodexempel för att anropa Abous REST API.Net C#
- Testa REST API
- Att använda RestwrapperPluginet via REST-API

## Versionering (versionshistorik för Abou REST API)

Versionshistorik för Abou REST API från version 2.1 till 2.4.4, med release av Abou som ändringen gäller från och ansvarig person.

| Händelse | Version av API | Förändring | Fr.o.m. rel. av Abou | Ansvarig |
|---|---|---|---|---|
| Upprättat | 2.1 | API’t utökat med följande metoder: AddCitizens, GetByDateAndState, GetByDate, GetByState, GetDetailed, CasePdfDownload, DecisionPdfDownload, AttachmentDownload, CreateCase samt GetCaseListFromUserIdentity. | 3.26.1541.0 | Jonas von Geijer |
| Justering | 2.1.1 | Metod CreateCase utökad med parameter för att kunna ange att publicering till integration-plugins skall ske. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.1 | Beskrivning av FileUpload korrigerad i denna dokumentation. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.1 | Produktnamnet Automaten ersatt med Abou och företagsnamnet Abou ersatt med Sokigo i denna dokumentation. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.2 | Notifiering sker via NotifyByWhenToSendEmail vilken även tar hänsyn till eventuell typ av kontakt användaren gjort i ärendet mha kontaktfältet | 2018.6.0 | Jonas von Geijer |
| Justering | 2.1.3 | Unescaping på filnamnet i FileUpload för att hantera ovanliga tecken | 2019.2.0 | Arnar Gardarsson |
| Justering | 2.1.4 | GetByDate, GetByState och GetByDateAndState supporterar filter för fältsvar | 2019.2.6 | Jonas von Geijer |
| Justering | 2.1.5 | Utökat attribut, FileDescription, i payload till FileUpload. Hämta version av API | 2019.5.0 | Jonas von Geijer |
| Utökning | 2.2.0 | Begäran om komplettering och Delgivning av beslut | 2019.8.0 | Jonas von Geijer |
| Utökning | 2.2.1 | Begäran om komplettering utökad med Subject.<br>Begäran om komplettering och Delgivning av beslut utökad med Kontakttyp | 2019.8.4 | Jonas von Geijer |
| Dok.rev. | 2.2.1 A | Förtydligande angående bilagors innehåll i GetDetailed | NA | Jonas von Geijer |
| Dok.rev. | 2.2.1 B | Förtydligande angående Entiteter och obligatoriska argument | NA | Jonas von Geijer |
| Utökning | 2.2.2 | Ny metod för att uppdatera fältsvar | 2020.2.16 | Jonas von Geijer |
| Justering | 2.2.3 | Begäran om komplettering refaktoriserad för att hantera ny funktionalitet för kompletteringsbegäran | 2021.2.0 | Jonas von Geijer |
| Justering | 2.2.3 | FileUpload kan nu sätta filtyp, filbeskrivning och läskvitto per fil | 2021.2.0 | Tom Ilestrand |
| Utökning | 2.2.4 | Hämta ärendestatistik för en specifik e-tjänst | 2021.5.0 | Tom Ilestrand |
| Justering | 2.2.5 | Begäran om komplettering kan nu ta emot en instruktionsbilaga | 2021.5.0 | Nicklas Nordahl |
| Justering | 2.2.5 | Söka publicerade e-tjänster och statistik för e-tjänster | 2021.5.0 | Tom Ilestrand |
| Utökning | 2.3.0 | Tokenbaserad autentisering | 2021.8.0 | Jonas von Geijer |
| Justering | 2.3.1 | IntegrationObjectResponse tillagt i metoder det används i och under modeller | 2022.2.0 | Tom Ilestrand |
| Dok. rev. | 2.3.1.A | Dokumentation av den befintliga metoden NewDirectMessage | 2022.3.0 | Dan Hoatson |
| Utökning | 2.3.2 | Ny metod ImportRegister | 2022.8 | Tom Ilestrand |
| Utökning | 2.4.0 | Ny metod CancelSupplement | 2023.2 | Tom Ilestrand |
| Utökning | 2.4.1 | Ny metod GetByDateTimeAndState | 2023.5 | Tom Ilestrand |
| Justering | 2.4.2 | FileUpload skickar nu meddelande för ”När handläggare bifogar fil” | 2024.2 | Tom Ilestrand |
| Justering | 2.4.3 | GetDetailed tar nu emot ett till argument (generatePdf) | 2024.11 | Adam Norman |
| Utökning | 2.4.4 | Ny metod CancelAllSupplements | 2025.3 | Adam Norman |

## Inledning

Detta dokument beskriver möjligheten att integrera med Abou via dess REST API V2.

## Autentisering i Abou REST API

Abou REST API erbjuder fr.o.m. Abou rel. 2021.8 två varianter av autentisering, tokenbaserad eller API-nyckel. Sokigos rekommendation är att använda tokenbaserad autentisering framför API-nyckel.

### Tokenbaserad autentisering (Bearer-token, JWT)

För att kunna anropa Abou API krävs API-användare vilka administreras i Abou Admingränssnitt Behörigheter. (Redan befintliga API-användare behöver inställning ”Kräv tokenbaserad anslutning”.)

Tokenbaserad autentisering innebär att man innan faktiska API-anrop behöver hämta en tidsbegränsad token (krypterad ”nyckel” som baseras på JWT, Json Web Token) som sedan måste skickas med till varje API-anrop i form av en Bearer Authorization Header.

### GET /api/authenticate – Hämta token (Authenticate)

Authenticate hämtar en tidsbegränsad Bearer-token (JWT) för tokenbaserad autentisering mot Abou REST API. Två varianter av sökväg:

```text
…/api/authenticate
…/api/authenticate/ServiceShortName
```

Om vidare API-anrop som ska göras kräver ServiceShortName måste token hämtas med alternativet …/api/authenticate/ServiceShortName.

#### Authenticate – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/authenticate/AAA
```

Authenticate kräver Basic Authorization Header vilken består av UserName (registrerat användarnamn för aktuell API-användare i Abou) och ApiKey (registrerad API-nyckel för aktuell API-användare i Abou). Själva värdet för Basic Authorization Header skapas enligt:

```text
"Basic " + Base64Encoded(UserName:ApiKey)
```

#### Authenticate – Verb och headers vid anrop

| | |
|---|---|
| Verb | GET |
| Header | Authorization: Basic … |

#### Authenticate – Svar (response)

Svar från Authenticate (GET /api/authenticate): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 401 | Unauthorized (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError |

Exempel på token i response (i originalet visas tokenens header-del i fetstil och resten i rött):

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJc3MiOiJhYm91IiwiRXhwIjoiMjAyMS0wOC0yM1QwODowMjo0NC41NTA4MTQ3WiIsIlNlcnZpY2VTaG9ydE5hbWUiOiJBQk9VMTIzIiwiU3lzdGVtUGVybWlzc2lvbiI6MjQsIlNlcnZpY2VQZXJtaXNzaW9uIjoyNTQsIkN1c29tZXJJZCI6MTAwMn0.xb3NP-WebwIzU5Aa8QM3RTiZtL1k_LsvSp5eDt8bU0I
```

### Autentisering med API-nyckel (username och apikey som URL-parametrar)

Ursprunglig autentisering i Abou REST API är m.h.a. API-nyckel vilket innebär att API-användares användarnamn och nyckel skickas med som url-parametrar i klartext vid anrop. Eftersom tokenbaserad autentisering är säkrare än API-nyckel är Sokigos rekommendation att byta ut autentisering med API-nyckel till tokenbaserad autentisering fr.o.m. Abou rel. 2021.8.

#### Autentisering med API-nyckel – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateStatus?username=userName&apikey=apiKey
```

För att kunna anropa Abou API krävs API-användare vilka administreras i Abou Admingränssnitt Behörigheter. För att använda autentisering m.h.a. API-nyckel behöver man inaktivera inställning ”Kräv tokenbaserad anslutning” för aktuell API-användare.

#### Bild: Behörigheter – inställningen ”Kräv tokenbaserad anslutning” för en API-användare

Skärmbild från Abou Admingränssnitt med rubriken **”Behörigheter - abou”**. Flikar överst: *Användare*, *Grupper*, *API-användare* (vald), *E-tjänster*. Knappar: *Tillbaka*, *Spara*, *Ta bort*. Underflikar: *Användaruppgifter* (vald), *Systembehörigheter*, *E-tjänstebehörigheter*. Formulärfält: *Användarnamn* = ”abou” (ej redigerbart), *Namn* = ”Abous Api-användare”, *Api-nyckel* (maskerat värde, med knapp för att generera ny nyckel), samt kryssrutan **”Kräv tokenbaserad anslutning”** (ikryssad, med hjälpikon), som är inringad med en streckad orange markering.

## Snabböversikt över API-metoder i Abou REST API 2.4.4

Sammanställning av samtliga metoder i dokumentet (verb, sökväg, lägsta behörighet och, där det anges, release av Abou). Basadress i exemplen: `https://abou.sokigo.com/api` (fiktiv URL).

| Metod | Verb | Sökväg | Behörighet | Abou release |
|---|---|---|---|---|
| Authenticate | GET | /api/authenticate respektive /api/authenticate/{ServiceShortName} | Basic Authorization (UserName:ApiKey) | fr.o.m. 2021.8 |
| UpdateStatus | PUT | /api/v2/services/{serviceShortName}/cases/UpdateStatus | Statusuppdaterare | |
| UpdateDiaryNumber | PUT | /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber | Statusuppdaterare | |
| UpdateAdministrator | PUT | /api/v2/services/{serviceShortName}/cases/UpdateAdministrator | Statusuppdaterare | |
| AddCitizens | PUT | /api/v2/services/{serviceShortName}/cases/AddCitizens | Statusuppdaterare | |
| FileUpload | POST | /api/v2/services/{serviceShortName}/cases/FileUpload | Statusuppdaterare | |
| GetByDateAndState | POST | /api/v2/services/{serviceShortName}/cases/GetByDateAndState | ”Enbart läsbehörighet” | |
| GetByDate | POST | /api/v2/services/{serviceShortName}/cases/GetByDate | ”Enbart läsbehörighet” | |
| GetByState | POST | /api/v2/services/{serviceShortName}/cases/GetByState | ”Enbart läsbehörighet” | |
| GetByDateTimeAndState | POST | /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState | ”Enbart läsbehörighet” | |
| GetDetailed | POST | /api/v2/services/{serviceShortName}/cases/GetDetailed | ”Enbart läsbehörighet” | |
| CasePdfDownload | POST | /api/v2/services/{serviceShortName}/cases/CasePdfDownload | ”Enbart läsbehörighet” | |
| DecisionPdfDownload | POST | /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload | ”Enbart läsbehörighet” | |
| AttachmentDownload | POST | /api/v2/services/{serviceShortName}/cases/AttachmentDownload | ”Enbart läsbehörighet” | |
| CreateCase | POST | /api/v2/services/{serviceShortName}/cases/CreateCase | Statusuppdaterare | |
| NewDirectMessage | PUT | /api/v2/services/{serviceShortName}/cases/NewDirectMessage | Statusuppdaterare | |
| GetCaseListFromUserIdentity | GET | /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity?userIdentity={userIdentity} | ”Enbart läsbehörighet” | |
| RequestSupplementExistingCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementExistingCase | Statusuppdaterare | 2021.2.0.0 |
| RequestSupplementNewCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementNewCase | Statusuppdaterare | 2021.2.0.0 |
| CancelSupplement | POST | /api/v2/services/{SERVICESHORTNAME}/cases/CancelSupplement | Statusuppdaterare | 2023.2.0.0 |
| CancelAllSupplements | POST | /api/v2/services/{SERVICESHORTNAME}/cases/CancelAllSupplement (så skrivet i URL-exemplet) | Statusuppdaterare | 2023.2.0.0 enligt metodtabellen (versionshistoriken anger 2025.3) |
| DecisionOnExistingCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/DecisionOnExistingCase | Beslutsfattare | 2019.8.0.0 |
| DecisionToNewCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/DecisionToNewCase | Beslutsfattare | 2019.8.0.0 |
| UpdateFieldAnswers | PUT | /api/v2/services/{SERVICESHORTNAME}/cases/UpdateFieldAnswers | Statusuppdaterare | 2020.2.16.0 |
| GetVersion | GET | /api/v2/services/cases/GetVersion | (ingen angiven) | 2019.5.0.0 |
| GetCaseStatistics | GET | /api/v2/services/{ServiceShortName}/cases/GetCaseStatistics | Systembehörighet: Hämta ärendestatistik | 2021.5.0.0 |
| SearchServices | GET | /api/v2/services/SearchServices?Searchstring={query} | (ingen angiven) | 2021.5.0.0 |
| GetServices | POST | /api/v2/services/GetServices | Systembehörighet: Hämta e-tjänster | 2021.5.0.0 |
| ImportRegister | PUT | /api/v2/registers/ImportRegister | Systembehörighet: Importera register | 2022.8.0.0 |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus – Uppdatera status för ett ärende (UpdateStatus)

UpdateStatus sätter en ny status på ett ärende i Abou, identifierat med UniqueId eller DiaryNumber, och kan skicka notifiering till invånaren.

### UpdateStatus – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateStatus
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateStatus – Verb, headers och parametrar vid anrop

Anrop till UpdateStatus (PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus).
När man uppdaterar status måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "State": "Status på ärendet som ska sättas" (3,
 "DisableSendNotification": true/false (4
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `State`.

Fotnoter till datablocket för UpdateStatus:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Obligatorisk.
4. Boolean, anger om Abou skall skicka notifiering till invånaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### UpdateStatus – Svar (response)

Svar från UpdateStatus (PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber – Uppdatera diarienummer för ett ärende (UpdateDiaryNumber)

UpdateDiaryNumber sätter anropande systems diarienummer (DiaryNumber) på ett ärende i Abou. (Meningen om Comment i fotnot 2 står två gånger i originalet.)

### UpdateDiaryNumber – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateDiaryNumber
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateDiaryNumber – Verb, headers och parametrar vid anrop

Anrop till UpdateDiaryNumber (PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber).
När man uppdaterar diarienummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "DisableSendNotification": true/false (3,
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för UpdateDiaryNumber:

1. Obligatorisk.
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Boolean, anger om Abou skall skicka notifiering till invånaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### UpdateDiaryNumber – Svar (response)

Svar från UpdateDiaryNumber (PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator – Uppdatera handläggare för ett ärende (UpdateAdministrator)

UpdateAdministrator sätter ny handläggare (Administrator) på ett ärende i Abou och kan notifiera den nya handläggaren, valfritt med ärendets bifogade filer.

### UpdateAdministrator – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateAdministrator
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateAdministrator – Verb, headers och parametrar vid anrop

Anrop till UpdateAdministrator (PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator).
När man uppdaterar handläggare måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "Administrator": "Handläggare på ärendet som ska sättas" (3,
 "DisableSendNotification": true/false (4,
 "IncludeCaseAttachmentsInNotification": true/false (5
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för UpdateAdministrator:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Obligatorisk.
4. Boolean, anger om Abou skall skicka notifiering till nya handläggaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.
5. Boolean, anger om ärendets bifogade filer skall ingå i notifiering till nya handläggaren.

### UpdateAdministrator – Svar (response)

Svar från UpdateAdministrator (PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/AddCitizens – Uppdatera ärende med invånare (AddCitizens)

AddCitizens lägger till invånare (Citizen-objekt med UserIdentity, FirstName, LastName, Email) på ett befintligt ärende i Abou.

### AddCitizens – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/AddCitizens
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### AddCitizens – Verb, headers och parametrar vid anrop

Anrop till AddCitizens (PUT /api/v2/services/{serviceShortName}/cases/AddCitizens).
När man uppdaterar invånare måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Citizens": Lista med Citizen-objekt (2,
 "OmitSocialSecurityNumberValidation": true/false (3,
 "UpdateExisting": true/false (4,
 "Actor": "Anropande systems namn" (5,
 "Comment": "Kommentar" (5,
 "DisableSendNotification": true/false (6
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Citizens`, `Actor`, `Comment`.

Fotnoter till datablocket för AddCitizens:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk lista enligt:<br>`[{"UserIdentity":"Personnummer eller annan unik identifierare", "FirstName":"Förnamn","LastName":"Efternamn", "Email":"E-postadress"},{…}]`.
3. Boolean, anger om personnummervalidering skall utföras på UserIdentity för varje Citizen.
4. Boolean, anger om redan befintlig Citizen’s värden skall uppdateras.
5. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
6. Boolean, anger om Abou skall skicka notifiering till nya handläggaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### AddCitizens – Svar (response)

Svar från AddCitizens (PUT /api/v2/services/{serviceShortName}/cases/AddCitizens): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## POST /api/v2/services/{serviceShortName}/cases/FileUpload – Bifoga filer till ett ärende (FileUpload)

FileUpload bifogar en eller flera filer till ett ärende i Abou via multipart-anrop. Ärendeinformationen skickas som en JSON-del (i kodexemplet med namnet CaseBaseRequest) och varje fil som en del med namnet file.

### FileUpload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/FileUpload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### FileUpload – Verb, headers och parametrar vid anrop

Anrop till FileUpload (POST /api/v2/services/{serviceShortName}/cases/FileUpload).
När man bifogar fil till ett ärende måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Multi Part Content (3 |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
 "FileDescription": "Eventuell beskrivning av filen",
 "DisableSendNotification": true/false (4
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `FileDescription`.

Fotnoter till datablocket för FileUpload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Filtyp, fildefinition och läskvitto sätts genom att sätta header fileDefinition, fileDescription respektive useReceipt under filens Content-Disposition. För läskvittot används värdet true. Se kodexempel för mer information (avsnittet ”Kodexempel C# – FileUpload med Bearer Token”).
4. Boolean, anger om Abou skall skicka notifiering för händelse ”När handläggare bifogar fil” om sådan finns konfigurerad i e-tjänsten.

### FileUpload – Svar (response)

Svar från FileUpload (POST /api/v2/services/{serviceShortName}/cases/FileUpload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 400 | Bad Request (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 415 | Unsupported Media Type (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState – Hämta ärendenummer inom ett datumintervall och status (GetByDateAndState)

GetByDateAndState returnerar Abous unika ärendenummer för ärenden inskickade inom ett datumintervall och med angivna statusar, valfritt filtrerat på fältsvar.

### GetByDateAndState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDateAndState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDateAndState – Verb, headers och parametrar vid anrop

Anrop till GetByDateAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum" (1,
 "ToDate": "Till och med datum" (2,
 "States": Lista med strängar (3,
 "ExcludeCasesWithDiaryNumber": true/false (4,
 "Field": Ett Field-objekt (5
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`, `States`.

Fotnoter till datablocket för GetByDateAndState:

1. Obligatorisk. Ärenden inskickade fr.o.m. datum omfattas.
2. Obligatorisk. Ärenden inskickade t.o.m. omfattas.
3. Obligatorisk. Ärendestatusar som ska omfattas.<br>`"States": ["status1", "status2"]`
4. Om diarieförda ärenden skall uteslutas.
5. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDateAndState – Svar (response)

Svar från GetByDateAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByDate – Hämta ärendenummer inom ett datumintervall (GetByDate)

GetByDate returnerar Abous unika ärendenummer för ärenden inskickade inom ett datumintervall, valfritt filtrerat på fältsvar.

### GetByDate – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDate
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDate – Verb, headers och parametrar vid anrop

Anrop till GetByDate (POST /api/v2/services/{serviceShortName}/cases/GetByDate).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum" (1,
 "ToDate": "Till och med datum" (2,
 "ExcludeCasesWithDiaryNumber": true/false (3,
 "Field": Ett Field-objekt (4
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`.

Fotnoter till datablocket för GetByDate:

1. Obligatorisk. Ärenden inskickade fr.o.m. datum omfattas.
2. Obligatorisk. Ärenden inskickade t.o.m. omfattas.
3. Om diarieförda ärenden skall uteslutas.
4. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDate – Svar (response)

Svar från GetByDate (POST /api/v2/services/{serviceShortName}/cases/GetByDate): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150810-AAA-WM56","150810-AAA-PI19","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByState – Hämta ärendenummer för ett eller flera status (GetByState)

GetByState returnerar Abous unika ärendenummer för ärenden med en eller flera angivna statusar, valfritt filtrerat på fältsvar.

### GetByState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByState – Verb, headers och parametrar vid anrop

Anrop till GetByState (POST /api/v2/services/{serviceShortName}/cases/GetByState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "States": Lista med strängar (1,
 "ExcludeCasesWithDiaryNumber": true/false (2,
 "Field": Ett Field-objekt (3
}
```

I originalet är följande fältnamn fetmarkerade: `States`.

Fotnoter till datablocket för GetByState:

1. Obligatorisk. Ärendestatusar som ska omfattas.<br>`"States": ["status1", "status2"]`
2. Om diarieförda ärenden skall uteslutas.
3. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByState – Svar (response)

Svar från GetByState (POST /api/v2/services/{serviceShortName}/cases/GetByState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150810-AAA-WM56","150810-AAA-PI19","150907-AAA-UL67"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState – Hämta ärendenummer med statusuppdatering inom ett datumintervall med klockslag och status (GetByDateTimeAndState)

GetByDateTimeAndState returnerar ärendenummer för ärenden vars status uppdaterats inom ett intervall med datum och klockslag. Här är States inte obligatorisk (saknas/null/tom = ingen statusfiltrering). Ny metod i API 2.4.1 (Abou 2023.5).

### GetByDateTimeAndState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDateTimeAndState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDateTimeAndState – Verb, headers och parametrar vid anrop

Anrop till GetByDateTimeAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum med klockslag" (1,
 "ToDate": "Till och med datum med klockslag" (2,
 "States": Lista med strängar (3,
 "ExcludeCasesWithDiaryNumber": true/false (4,
 "Field": Ett Field-objekt (5
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`.

Fotnoter till datablocket för GetByDateTimeAndState:

1. Obligatorisk. Ärenden med uppdaterad status fr.o.m. datum med klockslag omfattas.
2. Obligatorisk. Ärenden med uppdaterad status t.o.m. datum med klockslag omfattas.<br>`”ToDate”:” 2023-04-21 14:03:09”`
3. Ärendestatusar som ska omfattas. Om listan saknas, är null eller tom kommer ingen filtrering på status att ske.<br>`"States": ["status1", "status2"]`
4. Om diarieförda ärenden skall uteslutas.
5. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDateTimeAndState – Svar (response)

Svar från GetByDateTimeAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetDetailed – Hämta ett detaljerat ärende (GetDetailed)

GetDetailed hämtar ett komplett ärende (fält, bilagors metadata, statusar m.m.) som XML eller JSON; bilagornas innehåll levereras inte. I originalets datablock är OmitXmlDeclaration märkt `(5` men beskrivs av fotnot 6. Argumentet GeneratePdf tillkom i API 2.4.3.

### GetDetailed – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetDetailed
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetDetailed – Verb, headers och parametrar vid anrop

Anrop till GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed).
När man hämtar ett detaljerat ärende måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "IncludeAllFields": true/false (3,
 "IncludeAllAttachements": true/false (4,
 "XmlGeneratorType": "Typ av XML" (5,
 "OmitXmlDeclaration": true/false (5,
 "GeneratePdf":true/false(7
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `XmlGeneratorType`.

Fotnoter till datablocket för GetDetailed:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Boolean, om alla fält skall omfattas eller endast fält angivna för integration.
4. Boolean, om alla bifogade filler skall omfattas eller endast bifogade i fält angivna för integration.
5. Obligatorisk. Vilken typ av XML ärendet genereras som,<br>`Abou.Calamare.Framework.Integration.Xml.Default.DefaultXmlCaseGenerator` eller<br>`Abou.Calamare.Framework.Integration.Xml.ByggRGenerator.ByggRXmlCaseGenerator`.
6. Boolean, om xml-deklaration skall infogas initialt i xml’en.
7. Boolean, Styr om ärendepdf ska genereras och metadata om ärendepdfen ska hämtas. Default false.

### GetDetailed – Svar (response)

Svar från GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

### GetDetailed – Bilagor och dess innehåll, Content

Gäller svaret från GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed).

GetDetailed leverar inte bilagornas innehåll i svaret, dvs

```xml
<Case><Attachments><Attachment><Content /></Attachment></Attachments></Case>
```

För att hämta bilagors innehåll se CasePdfDownload, DecisionPdfDownload och AttachmentDownload.

Data:

- Content type: application/xml (om “Accept: application/json” anges i request header svaret som json)
- Content: String. T.ex. (i originalet en sammanhängande XML-sträng; här indenterad för läsbarhet):

```xml
<Case xmlns="urn:abou:documents:ka:Case">
  <Id>160309-FFS-LF53</Id>
  <DiaryNumber>74271</DiaryNumber>
  <DateSubmitted>2016-03-09T07:58:42.8770000</DateSubmitted>
  <SentInAs>Citizen</SentInAs>
  <RequiresMultipleSignatures>false</RequiresMultipleSignatures>
  <Status>Pågående</Status>
  <ServiceId>FFS</ServiceId>
  <ServiceName>Felanmälan</ServiceName>
  <ServiceVersion>22</ServiceVersion>
  <ServiceStatuses>
    <ServiceStatus>Inkommet</ServiceStatus>
    <ServiceStatus>Under handläggning</ServiceStatus>
    <ServiceStatus>Avslutat</ServiceStatus>
  </ServiceStatuses>
  <Citizens/>
  <Signatures/>
  <Payments/>
  <QueueItems/>
  <Fields>
    <Field>
      <Id>U.37.2.3</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[vattenläcka?trädgårdsvägen /
Moränvägen]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.6</Id>
      <TypeOfField>EGovDateChooserField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[2016-03-09 07:59:23]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.2</Id>
      <TypeOfField>EGovDropDownField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[Gatuunderhåll]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.9</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[59,4567348;18,0408177]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.4</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[Trädgårdsvägen1]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.7</Id>
      <TypeOfField>EGovFileUploadField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[image1.png]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.10</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[<a target="_blank" href="http://maps.google.se/maps?q=59.4567348,18.0408177&z=17&ll=59.4567348,18.0408177">Visa på karta</a>]]></Answer>
      <Arguments/>
    </Field>
  </Fields>
  <Attachments>
    <Attachment>
      <Type>CasePdf</Type>
      <FileName>160309-FFS-LF53.pdf</FileName>
      <SystemFileName/>
      <FileType>application/pdf</FileType>
      <FileDescription>Ärendebilaga</FileDescription>
      <DateUploaded>2016-03-09T07:58:42.8770000</DateUploaded>
      <FileSize>63361</FileSize>
      <Content/>
      <FieldId/>
      <Arguments/>
    </Attachment>
    <Attachment>
      <Type>Attachment</Type>
      <FileName>image1.png</FileName>
      <SystemFileName>160309-FFS-LF53_Bifoga_bild.png</SystemFileName>
      <FileType>image/jpeg</FileType>
      <FileDescription>Bifoga bild</FileDescription>
      <DateUploaded>2016-03-09T07:58:42.0000000</DateUploaded>
      <FileSize>790094</FileSize>
      <Content/>
      <FieldId/>
      <Arguments/>
    </Attachment>
  </Attachments>
  <Supplements/>
</Case>
```

## POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload – Hämta ärende-PDF (CasePdfDownload)

CasePdfDownload hämtar ärendets PDF (ärende-PDF) som binärdata.

### CasePdfDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/CasePdfDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### CasePdfDownload – Verb, headers och parametrar vid anrop

Anrop till CasePdfDownload (POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload).
När man hämtar en ärende-PDF måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för CasePdfDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).

### CasePdfDownload – Svar (response)

Svar från CasePdfDownload (POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload – Hämta ett ärendes besluts-PDF (DecisionPdfDownload)

DecisionPdfDownload hämtar ett ärendes besluts-PDF som binärdata.

### DecisionPdfDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/DecisionPdfDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### DecisionPdfDownload – Verb, headers och parametrar vid anrop

Anrop till DecisionPdfDownload (POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload).
När man hämtar en besluts-PDF-bilaga måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för DecisionPdfDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).

### DecisionPdfDownload – Svar (response)

Svar från DecisionPdfDownload (POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload – Hämta en specifik bilaga från ett ärende (AttachmentDownload)

AttachmentDownload hämtar en specifik bilaga från ett ärende som binärdata. Bilagan anges med SystemFileName (finns i GetDetailed-svaret). Observera att kodexemplet i dokumentet anropar sökvägen …/cases/CaseAttachmentDownload.

### AttachmentDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/AttachmentDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### AttachmentDownload – Verb, headers och parametrar vid anrop

Anrop till AttachmentDownload (POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload).
När man hämtar en bilaga måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "SystemFileName": "Specifikt filnamn" (3
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `SystemFileName`.

Fotnoter till datablocket för AttachmentDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Obligatorisk. Bilagans specifika filnamn i Abou.

### AttachmentDownload – Svar (response)

Svar från AttachmentDownload (POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/CreateCase – Skapa nytt ärende (CreateCase)

CreateCase skapar ett nytt ärende i en e-tjänst i Abou. Fältsvar kopplas till fält via fältens integrationsargument (Name/Value). Giltiga värden för SentInAs: Citizen, Company, Organisation (övriga hanteras som Unknown).

### CreateCase – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/CreateCase
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.
- Kräver att aktuella fält i e-tjänsten har konfigurerats med Integrationsargument.

### CreateCase – Verb, headers och parametrar vid anrop

Anrop till CreateCase (POST /api/v2/services/{serviceShortName}/cases/CreateCase).
När man hämtar ett detaljerat ärende måste man skicka med information som JSON. (Så formulerat i originalet, trots att avsnittet gäller CreateCase.)

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "Fields": Lista med Field-objekt (1,
 "Citizen": "Citizenobjekt" (2,
 "OmitSocialSecurityNumberValidation": true/false (3,
 "UpdateExistingCitizen": true/false (4,
 "SentInAs": "Typ av invånare" (5,
 "SignatureData": "Signeringsdata" (6,
 "SignatureIssuer": "Utgivare av signering" (7,
 "Actor": "Anropande systems namn" (8,
 "Comment": "Kommentar" (8,
 "EnablePublishToPlugin": true/false (9
}
```

I originalet är följande fältnamn fetmarkerade: `Fields`, `Citizen`, `SentInAs`, `SignatureData`, `SignatureIssuer`, `Actor`, `Comment`.

Fotnoter till datablocket för CreateCase:

1. Obligatorisk lista enligt:<br>`[{"Answer":"Fältsvar", "Arguments":[{"Name":"Fältets specifika argumentnamn", "Value":" Fältets specifika argumentvärde"}, {…}]}, {…}]`
2. Obligatorisk **om** aktuell e-tjänst kräver inloggning/signering, Citizen:<br>`{"UserIdentity":"Personnummer eller annan unik identifierare", "FirstName":"Förnamn","LastName":"Efternamn", "Email":"E-postadress"}`.
3. Boolean, anger om personnummervalidering skall utföras på UserIdentity för Citizen.
4. Boolean, anger om redan befintlig Citizen’s värden skall uppdateras.
5. Obligatorisk **om** aktuell e-tjänst kräver inloggning/signering, använd någon av följande typer: ”Citizen”, ”Company” eller ”Organisation” (andra värden kommer att hanteras som ”Unknown”).
6. Obligatorisk **om** aktuell e-tjänst kräver signering.
7. Obligatorisk **om** aktuell e-tjänst kräver signering.
8. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).
9. Boolean, anger om publicering till integration-plugins skall ske (fr.o.m. rel. 3.30.1607.1)

### CreateCase – Svar (response)

Svar från CreateCase (POST /api/v2/services/{serviceShortName}/cases/CreateCase): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: String (JSON objekt) med Abous unika ärendenummer för det nya ärendet, t.ex:

```text
”150810-AAA-WM56”
```

## PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage – Skapa direktmeddelande (NewDirectMessage)

NewDirectMessage skapar ett direktmeddelande i ett ärende i Abou, i namn av en administratör (AdministratorIdentity = UserName för en AdminUser i Abou). Metoden dokumenterades i dokumentrevision 2.3.1.A.

### NewDirectMessage – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/NewDirectMessage
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### NewDirectMessage – Verb, headers och parametrar vid anrop

Anrop till NewDirectMessage (PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage).
När man skapar ett direktmeddelande måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "AdministratorIdentity": "Meddelandets administratör" (2,
 "Text": “Själva meddelandet (3”
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `AdministratorIdentity`, `Text`.

Fotnoter till datablocket för NewDirectMessage:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (UserName för någon AdminUser i Abou)
3. Obligatorisk

### NewDirectMessage – Svar (response)

Svar från NewDirectMessage (PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: String (JSON objekt) som bekräftar skickat meddelande för aktuellt ärende, t.ex:

```text
” 220223-AAA-IH39 - New direct message created”
```

## GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity – Hämta en lista av ärendenummer för ett personnummer (GetCaseListFromUserIdentity)

GetCaseListFromUserIdentity returnerar en lista med de senaste ärendenumren för ett person- eller organisationsnummer (query-parametern userIdentity). Ingen request body.

### GetCaseListFromUserIdentity – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetCaseListFromUserIdentity?userIdentity= userIdentity
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| userIdentity | Person- eller organisationsnummer (eller annan identifierare) som man vill hämta en lista av de senaste ärendena för |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetCaseListFromUserIdentity – Verb, headers och parametrar vid anrop

Anrop till GetCaseListFromUserIdentity (GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity).

| | |
|---|---|
| Verb | GET |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

### GetCaseListFromUserIdentity – Svar (response)

Svar från GetCaseListFromUserIdentity (GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/json eller xml
- Content: string[]

## Begäran om komplettering

Metoder för att begära komplettering från sökande (invånare) i Abou: RequestSupplementExistingCase, RequestSupplementNewCase, CancelSupplement och CancelAllSupplements. Kan användas tillsammans med RestwrapperPlugin se Att använda RestwrapperPluginet via REST-API nedan.

### POST /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementExistingCase – Begäran om komplettering på ett befintligt ärende i Abou

RequestSupplementExistingCase skapar en kompletteringsbegäran på ett ärende som redan finns i Abou (ärendet anges med UniqueId).

| RequestSupplementExistingCase | | |
|---|---|---|
| Request | RequestSupplementRequest | Se RequestSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [], "Applicant": "" }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2021.2.0.0 | |

Exempel på url för anrop (RequestSupplementExistingCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/RequestSupplementExistingCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (RequestSupplementExistingCase):

```json
{
  "Title": "Komplettera med markkarta",
  "Instructions": "Vänligen ladda upp ny markkarta med korrekt skala 1:400",
  "Arguments": [{
    "Name": "EventID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "InstructionFile": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  },
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "UniqueId": "190401-INTTESTANSOK-QX47",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "FileTypeCategories": 4
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementNewCase – Begäran om komplettering då ärende saknas i Abou

RequestSupplementNewCase skapar en kompletteringsbegäran när ärendet saknas i Abou; i exemplet refereras ärendet med anropande systems DiaryNumber. Citizen är obligatoriskt när ett nytt ärende ska skapas i Abou.

| RequestSupplementNewCase | | |
|---|---|---|
| Request | RequestSupplementRequest | Se RequestSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [], "Applicant": "" }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2021.2.0.0 | |

Exempel på url för anrop (RequestSupplementNewCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/RequestSupplementNewCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (RequestSupplementNewCase):

```json
{
  "Title": "Komplettera med markkarta",
  "Instructions": "Vänligen ladda upp ny markkarta med korrekt skala 1:400",
  "Arguments": [{
    "Name": "EventID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "InstructionFile": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  },
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "DiaryNumber": "BYGG.2017.32",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "FileTypeCategories": 4
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/CancelSupplement – Ta bort en väntande komplettering

CancelSupplement tar bort (avbryter) en eller flera väntande kompletteringsbegäranden på ett ärende i Abou, angivna med SupplementIds. Ny metod i API 2.4.0.

| CancelSupplement | | |
|---|---|---|
| Request | CancelSupplementRequest | Se CancelSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [] }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2023.2.0.0 | |

Exempel på url för anrop (CancelSupplement):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/CancelSupplement
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (CancelSupplement):

```json
{
"SupplementIds":[4083,4084],
"Comment":"Tid för komplettering har gått ut",
"UniqueId": "190401-INTTESTANSOK-QX47"
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/CancelAllSupplements – Ta bort samtliga väntande kompletteringar

CancelAllSupplements tar bort samtliga väntande kompletteringsbegäranden på ett ärende i Abou. Request-modellen anges som CancelSupplementRequest, men exempel-payloaden innehåller inga SupplementIds. Ny metod i API 2.4.4 (Abou 2025.3 enligt versionshistoriken; metodtabellen anger Abou release 2023.2.0.0).

| CancelAllSupplements | | |
|---|---|---|
| Request | CancelSupplementRequest | Se CancelSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [] }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2023.2.0.0 | |

I originalet slutar URL-exemplet på `CancelAllSupplement` (utan avslutande s; radbrutet som ”CancelAllSupplemen” + ”t”).

Exempel på url för anrop (CancelAllSupplements):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/CancelAllSupplement
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (CancelAllSupplements):

```json
{
"Comment":"Tid för komplettering har gått ut",
"UniqueId": "190401-INTTESTANSOK-QX47"
}
```

## Delgivning av beslut

Metoder för att delge sökande (invånare) ett beslut via Abou: DecisionOnExistingCase och DecisionToNewCase. Kan användas tillsammans med RestwrapperPlugin se Att använda RestwrapperPluginet via REST-API nedan.

### POST /api/v2/services/{SERVICESHORTNAME}/cases/DecisionOnExistingCase – Delgivning av beslut på ett befintligt ärende i Abou

DecisionOnExistingCase delger ett beslut (beslutsdokument som Base64 i DecisionDocument, DecisionType Approved eller Rejected) på ett ärende som redan finns i Abou (anges med UniqueId).

| DecisionOnExistingCase | | |
|---|---|---|
| Request | CaseDecisionRequest | Se CaseDecisionRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "DecisionId": "", "Applicant": "" }` |
| E-service permission | Beslutsfattare | |
| Abou release | 2019.8.0.0 | |

Exempel på url för anrop (DecisionOnExistingCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/DecisionOnExistingCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (DecisionOnExistingCase):

```json
{
  "DecisionType": "Approved",
  "Description": "Här kommer ett beslut",
  "Arguments": [{
    "Name": "castor_CaseID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "UniqueId": "190515-INTTESTANSOK-DU65",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "DecisionDocument": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  }
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/DecisionToNewCase – Delgivning av beslut då ärende saknas i Abou

DecisionToNewCase delger ett beslut när ärendet saknas i Abou; i exemplet refereras ärendet med anropande systems DiaryNumber. Citizen är obligatoriskt när ett nytt ärende ska skapas i Abou.

| DecisionToNewCase | | |
|---|---|---|
| Request | CaseDecisionRequest | Se CaseDecisionRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "DecisionId": "" }` |
| E-service permission | Beslutsfattare | |
| Abou release | 2019.8.0.0 | |

Exempel på url för anrop (DecisionToNewCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/DecisionToNewCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (DecisionToNewCase):

```json
{
  "DecisionType": "Approved",
  "Description": "Här kommer ett beslut",
  "Arguments": [{
    "Name": "castor_CaseID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "DiaryNumber": "BYGG.2017.32",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "DecisionDocument": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  }
}
```

## PUT /api/v2/services/{SERVICESHORTNAME}/cases/UpdateFieldAnswers – Uppdatera fältsvar på ett befintligt ärende (UpdateFieldAnswers)

UpdateFieldAnswers uppdaterar svaret på ett eller flera fält i ett befintligt ärende i Abou. Fältet anges med ett unikt integrationsargument (FieldKeyValue med Name/Value). Med DoPublishPdf kan ärendets PDF genereras på nytt. Ny metod i API 2.2.2.

| UpdateFieldAnswers | | |
|---|---|---|
| Request | CaseUpdateFieldAnswersRequest | Se CaseUpdateFieldAnswersRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse |
| E-service permission | Statusuppdaterare | |
| Abou release | 2020.2.16.0 | |

Exempel på url för anrop (UpdateFieldAnswers):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/UpdateFieldAnswers
```

- Verb: PUT
- Headers: Authorization: Bearer …

Exempel på Payload (UpdateFieldAnswers), återgiven exakt som i originalet. Observera att kommatecken saknas efter `"Comment"` och efter `"Answer"`, så exemplet är inte giltig JSON som det står:

```json
{
   "UniqueId": "200507-MMLA-MS11",
   "DiaryNumber": null,
   "Actor": "System X",
   "Comment": "Uppdatering av fältsvar…"
   "Fields": [
        {
             "Answer": "Nytt svar"
             "FieldKeyValue": {
                  "Name": "abou_an_unique_integrationargument_name",
                  "Value": "some_value"
             }
        }
   ],
   "DoPublishPdf": true
}
```

## GET /api/v2/services/cases/GetVersion – Hämta befintlig version av Abou API (GetVersion)

GetVersion returnerar befintlig version av Abou API. Ingen request-modell och ingen e-tjänstebehörighet anges.

| GetVersion | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse |
| E-service permission | | |
| Abou release | 2019.5.0.0 | |

Exempel på url för anrop (GetVersion):

```text
https://abou.sokigo.com/api/v2/services/cases/GetVersion
```

- Verb: GET

## GET /api/v2/services/{ServiceShortName}/cases/GetCaseStatistics – Hämta ärendestatistik för en specifik e-tjänst (GetCaseStatistics)

GetCaseStatistics returnerar ärendestatistik (påbörjade ärenden, inskickade ärenden, inskickade som ombud) för en e-tjänst. Kräver systembehörigheten ”Hämta ärendestatistik”.

| GetCaseStatistics | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | Hämta ärendestatistik | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för GetCaseStatistics (IntegrationResponse.Result):

```json
{
"ServiceShortName":"",
"StartedCases": 0,
"SubmittedCases": 0,
"SubmittedAsOmbudsman": 0
}
```

Exempel på url för anrop (GetCaseStatistics):

```text
https://abou.sokigo.com/api/v2/services/ServiceShortName/cases/GetCaseStatistics
```

- Verb: GET
- Headers: Authorization: Bearer …

## GET /api/v2/services/SearchServices?Searchstring={query} – Söka bland publicerade e-tjänster (SearchServices)

SearchServices söker bland publicerade e-tjänster med en söksträng (query-parametern Searchstring) och returnerar kortnamn, visningsnamn och URL:er för matchande e-tjänster.

| SearchServices | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för SearchServices (IntegrationResponse.Result), återgiven som i originalet (inklusive avslutande kommatecken efter objektet):

```jsonc
[
{
"ServiceShortName":"",
"DisplayName": "",
"ServiceUrl": "",
"FormUrl": ""
},
]
```

I URL-exemplet är `query` (söksträngen) fetmarkerad.

Exempel på url för anrop (SearchServices):

```text
https://abou.sokigo.com/api/v2/services/SearchServices?Searchstring=query
```

- Verb: GET

## POST /api/v2/services/GetServices – Hämta information för en specifik e-tjänst (GetServices)

GetServices returnerar information om e-tjänster (aktiv/öppen, öppettider, autentisering/signering, beslut, organisation, ärendestatusar), filtrerat enligt ServiceOrganisationRequest. Kräver systembehörigheten ”Hämta e-tjänster”.

| GetServices | | |
|---|---|---|
| Request | ServiceOrganisationRequest | Se ServiceOrganisationRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | Hämta e-tjänster | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för GetServices (IntegrationResponse.Result), återgiven som i originalet (med `=` i stället för `:`):

```text
[{
"ServiceShortName" = "",
"ServiceDisplayName" = "",
"ServiceUrl" = "",
"FormUrl" = "",
"ServiceIsActive" = true/false,
"ServiceIsOpen" = true/false,
"ServiceOpenFrom" = datum/null,
"ServiceOpenTo" = datum/null,
"ServiceWindowFrom" = datum/null,
"ServiceWindowTo" = datum/null,
"ServiceHasAuthentication" = true/false,
"ServiceHasSigning" = true/false,
"ServiceHasMultipleSigning" = true/false,
"ServiceHasAlternativeSigning" = true/false,
"ServiceHasDecision" = true/false,
"ServiceLastUpdated" = datum,
"OrganisationName" = "",
"CaseStatusList" = [""]
}]
```

Exempel på url för anrop (GetServices):

```text
https://abou.sokigo.com/api/v2/services/GetServices
```

- Verb: POST
- Headers: Authorization: Bearer …

## PUT /api/v2/registers/ImportRegister – Import register (ImportRegister)

ImportRegister importerar ett register till Abou (skapar nytt eller skriver över befintligt med samma SystemName) och kan koppla registret till e-tjänster. Kräver systembehörigheten ”Importera register”. Ny metod i API 2.3.2.

| ImportRegister | | |
|---|---|---|
| Request | ImportRegisterRequest | Se ImportRegisterRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Inkluderar Success och Message |
| E-service permission | | |
| Systembehörighet | Importera register | |
| Abou release | 2022.8.0.0 | |

Exempel på url för anrop (ImportRegister):

```text
https://abou.sokigo.com/api/v2/registers/ImportRegister
```

- Verb: PUT
- Headers: Authorization: Bearer …

## Entiteter (request- och response-modeller)

*Kolumnen Obl (obligatorisk) nedan anges som * och – där * innebär att argumentet är strikt obligatoriskt medan – innebär att argumentet är obligatoriskt beroende på vilket ska framgå i beskrivning.*

I tabellerna nedan återges * som `*` och – som `-`; tom cell betyder att inget anges i originalet. Namn och typer är i originalet satta i teckensnitt med fast bredd, och modellnamn i typkolumnen (t.ex. FileData, CitizenRequest, FieldArgument) är länkar till respektive entitet.

### Entitet RequestSupplementRequest

Request-modell för Begäran om komplettering (RequestSupplementExistingCase och RequestSupplementNewCase).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Title` | String | `*` | Rubrik för kompletteringsbegäran. |
| `Instructions` | String | `-` | För sökande vägledande information för att kunna utföra komplettering.<br>Obligatorisk om det saknas ”InstructionFIle” |
| `InstructionFile` | FileData | `-` | För sökande vägledande information för att kunna utföra komplettering.<br>Obligatorisk om det saknas ”Instructions” |
| `DescriptionToAdministrator` | String | | Anledning till begäran om komplettering, lagras i ärendet som ärendehistorik i Abou |
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om begäran om komplettering ska ske i ett redan <u>existerande</u> ärende i Abou |
| `DiaryNumber` | String | | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou |
| `Actor` | String | | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String | | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `Arguments` | List<FieldArgument> | `-` | Lista med Namn/Värde-par som rör kompletteringen. Dessa behövs vid eventuell återkopplande integration till anropande system.<br>Se FieldArgument. |
| `Citizen` | CitizenRequest | `-` | Obligatoriskt när ett nytt ärende ska skapas i Abou.<br>Se CitizenRequest |
| `OmitSocialSecurityNumberValidation` | Bool | | True innebär att personnummervalidering på Citizen.UserIdentity utelämnas |
| `UpdateExistingCitizen` | Bool | | True innebär att Citizen-FirstName, LastName, Email och MobilePhone uppdaterar befintlig invånare I Abou |
| `DisableSendNotification` | Bool | | True innebär att e-tjänstens notifieringar inaktiveras |
| `SentInAs` | String | | Anger vilken roll sökande får i nytt ärende baserad på specifik e-tjänst för komplettering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureData` | String | `-` | Information som ska signeras.<br>Obligatorisk om specifik e-tjänst för komplettering kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureIssuer` | String | `-` | Utgivare av signeringen.<br>Obligatorisk om specifik e-tjänst för komplettering kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `EnablePublishToPlugin` | Bool | | True innebär att nytt ärende baserad på specifik e-tjänst för komplettering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt, triggar händelse för integration |
| `AllowMultipleFiles` | Bool | | True innebär att invånaren kan komplettera med flera filer inom en och samma kompletteringsbegäran |
| `FileTypeCategories` | Int | | De typer av fil invånaren tillåts komplettera med. Giltiga värden är 1, 2 och 4.<br>1 – Bilder (".jpg", ".jpeg", ".png")<br>2 – Office-dokument (".xls", ".xlsx", ".doc", ".docx")<br>4 – PDF-fil (".pdf")<br>Så kallad bit-skiftning (bitwise) kan användas för att kombinera tillåtna typer av filer, t.ex. innebär värdet 5 att Bilder och PDF-fil tillåts.<br>Default (om FileTypeCategories utelämnas) är att Bilder, Office-dokument och PDF-fil tillåts. |

#### RequestSupplementRequest – värden för FileTypeCategories

Enumvärden (bitflaggor som kan kombineras) för fältet FileTypeCategories i RequestSupplementRequest, enligt tabellen ovan:

| Värde | Tillåtna filtyper |
|---|---|
| 1 | Bilder (".jpg", ".jpeg", ".png") |
| 2 | Office-dokument (".xls", ".xlsx", ".doc", ".docx") |
| 4 | PDF-fil (".pdf") |
| 5 (exempel, 1 + 4) | Bilder och PDF-fil |
| utelämnat (default) | Bilder, Office-dokument och PDF-fil |

### Entitet CancelSupplementRequest

Request-modell för CancelSupplement och CancelAllSupplements (ta bort väntande komplettering).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Comment` | String | | Det anropande systemets kommentar för anropet, presenteras i ärendehistorik. |
| `UniqueId` | String | `*` | Identifierare för ett ärende i Abou. |
| `DiaryNumber` | String | `-` | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou. |
| `SupplementIds` | List<int> | `*` | Id för de kompletteringsbegäran som skall avbrytas. Värdet kan vara sparat från när kompletteringsbegärand skapades eller hämtas med GetDetailed. |

### Entitet CaseDecisionRequest

Request-modell för Delgivning av beslut (DecisionOnExistingCase och DecisionToNewCase).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Description` | String | | Kommentar som beskriver beslutet. Ska ses som en kommentar från en handläggare. Visas för sökande i Abou. |
| `DecisionType` | String | `*` | Typ av beslut. Giltiga värden är: Rejected och Approved. |
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om beslut ska tilldelas ett redan <u>existerande</u> ärende i Abou. |
| `DiaryNumber` | String | | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou |
| `Actor` | String | `*` | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String | | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `DecisionDocument` | FileData | `*` | Innehåller information om beslutsdokumentet. Se FileData |
| `Citizen` | CitizenRequest | `-` | Obligatoriskt när ett nytt ärende ska skapas i Abou.<br>Se CitizenRequest |
| `OmitSocialSecurityNumberValidation` | Bool | | True innebär att personnummervalidering på Citizen.UserIdentity utelämnas |
| `UpdateExistingCitizen` | Bool | | True innebär att Citizen-FirstName, LastName, Email och MobilePhone uppdaterar aktuell invånare (sökande) i Abou |
| `DisableSendNotification` | Bool | | True innebär att e-tjänstens notifieringar inaktiveras |
| `SentInAs` | String | | Anger vilken roll sökande får i nytt ärende baserad på specifik e-tjänst för beslut som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt. |
| `SignatureData` | String | `-` | Information som ska signeras.<br>Obligatorisk om specifik e-tjänst för beslut kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureIssuer` | String | `-` | Utgivare av signeringen.<br>Obligatorisk om specifik e-tjänst för beslut kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `Arguments` | List<FieldArgument> | `-` | Lista med Namn/Värde-par som rör beslutet. Dessa behövs vid eventuell återkopplande integration till anropande system.<br>Se FieldArgument. |
| `EnablePublishToPlugin` | Bool | | True invånaren kan välja att komplettera med flera filer i en och samma komplettering |

Anm.: Beskrivningen av `EnablePublishToPlugin` i CaseDecisionRequest är återgiven exakt som i originalet (den liknar beskrivningen av AllowMultipleFiles i RequestSupplementRequest).

Enumvärden för `DecisionType` i CaseDecisionRequest: `Approved`, `Rejected`.

### Entitet CitizenRequest

Modell för invånare/sökande (Citizen) i bl.a. RequestSupplementRequest och CaseDecisionRequest.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `UserIdentity` | String | `*` | Ett giltigt personnummer |
| `FirstName` | String | `*` | Förnamn |
| `LastName` | String | `*` | Efternamn |
| `Email` | String | `*` | En giltig e-post adress |
| `MobilePhone` | String | | Mobiltelefon |
| `SendNotificationType` | String | | Giltiga värden är Email (default) eller Sms |

### Entitet ServiceOrganisationRequest

Request-modell (filter) för GetServices (POST /api/v2/services/GetServices). Tabellen saknar kolumnen Obl i originalet.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Open` | Bool? | Enbart e-tjänster som är öppna(true)/stängda/(false). Null innebär ingen filtrering. |
| `Active` | Bool? | Enbart e-tjänster som är aktiva(true)/inaktiva /(false). Null innebär ingen filtrering. |
| `ServiceShortNames` | String[] | Array med kortnamnen på de e-tjänster som skall hämtas. Null innebär ingen filtrering. |
| `Organisations` | String[] | Array med namnen på de organisationer vars e-tjänster skall hämtas. Null innebär ingen filtrering. |

### Entitet ImportRegisterRequest

Request-modell för ImportRegister (PUT /api/v2/registers/ImportRegister). Tabellen saknar kolumnen Obl i originalet.

| Namn | Typ | Beskrivning |
|---|---|---|
| `SystemName` | String | Systemnamn för det importerade registret. Anges ett existerade systemnamn skrivs det befintliga registret över. |
| `DisplayName` | String | Visningsnamn för det importerade registret. |
| `Description` | String | Beskrivning av det importerade registret. |
| `ServiceShortNames` | String[] | Array med kortnamnen på de nya e-tjänster som ska kopplas till registret. Existerande kopplingar påverkas inte. Om tom eller null utförs ingen koppling. Eventuella dubbletter ignoreras. Samtliga e-tjänster behöver finnas i noden. |
| `Data` | String[] | Array med data som skall finnas i registret. Tomma värden tas bort. Dubbletter ignoreras. Tom lista godkänns inte. |

### Entitet FieldArgument

Namn/värde-par (integrationsargument). Används i Arguments-listor (RequestSupplementRequest, CaseDecisionRequest) och i FieldRequest.FieldKeyValue.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Name` | String | `*` | |
| `Value` | String | `*` | |

### Entitet FileData

Fil som Base64-data. Används i CaseDecisionRequest.DecisionDocument och RequestSupplementRequest.InstructionFile.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `FileName` | String | `*` | Beslutsdokumentets namn |
| `Base64Data` | String | `*` | Fildata i Base64 |

### Entitet CaseUpdateFieldAnswersRequest

Request-modell för UpdateFieldAnswers (uppdatera fältsvar på ett befintligt ärende).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om INTE DiaryNumber används |
| `DiaryNumber` | String | `-` | Att systemets ärendenummer på ett ärende i Abou.<br>Obligatorisk om INTE UniqueId används |
| `Actor` | String | `*` | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String | | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `Fields` | List<FieldRequest> | `*` | Lista med nytt fältsvar samt fältreferens.<br>Se FieldRequest. |
| `DoPublishPdf` | Bool | | True innebär att det aktuella ärendets PDF genereras på nytt för att |

Anm.: Beskrivningen av `DoPublishPdf` slutar abrupt (”…genereras på nytt för att”) i originalet; resten av meningen finns inte i dokumentet.

### Entitet FieldRequest

Modell för ett fältsvar i CaseUpdateFieldAnswersRequest.Fields.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Answer` | String | `*` | Nytt fältsvar |
| `FieldKeyValue` | FieldArgument | `*` | Unik kombination av namn och värde för ett integrationsargument som anger fältet för uppdatering av svar |

### Entitet IntegrationResponse

Response-modell (Result som sträng) för bl.a. Begäran om komplettering, Delgivning av beslut, UpdateFieldAnswers och GetVersion. Tabellen saknar kolumnen Obl.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Success` | Bool | True innebär att anropet utfördes i sin helhet |
| `Message` | String | Felmeddelande vid Success = false |
| `Result` | String | Resultat vid Success = true |
| `Id` | String | Vanligen aktuellt ärendenummer i Abou |

### Entitet IntegrationObjectResponse

Response-modell (Result som objekt) för GetCaseStatistics, SearchServices, GetServices och ImportRegister. Tillagd i API 2.3.1. Tabellen saknar kolumnen Obl.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Success` | Bool | True innebär att anropet utfördes i sin helhet |
| `Message` | String | Felmeddelande vid Success = false |
| `Result` | Object | Resultat vid Success = true |
| `Id` | String | Vanligen aktuellt ärendenummer i Abou |

## Kodexempel för att anropa Abous REST API.Net C#

C#-exempel (HttpClient, Newtonsoft.Json) från dokumentet för att anropa Abou REST API med Bearer-token. Radbrytningar som i PDF:en uppstått mitt i strängliteraler och kommentarer på grund av sidbredden har slagits ihop; i övrigt återges koden som i dokumentet, inklusive eventuella fel (t.ex. `URI.EscapeDataString(filename)`, dubbla parenteser i `NameValueHeaderValue((`, och `stringContents` i GetByDateAndState).

### Kodexempel C# – using-direktiv och konstanter

Gemensamma using-direktiv och konstanter (ApiUrl, ApiUserName, ApiKey, ServiceShortName, CaseUniqueId, DiaryNumber) som används i kodexemplen nedan.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;
using Newtonsoft.Json;

private const string ApiUrl = "https://abou.sokigo.com/api";
private const string ApiUserName = "api user name";
private const string ApiKey = "api user key";
private const string ServiceShortName = "aaa";
private const string CaseUniqueId = "150527-AAA-UI91";
private const string DiaryNumber = "";
```

### Kodexempel C# – Hämta Bearer Token (Authenticate)

Hämtar en Bearer-token via GET {ApiUrl}/authenticate/{ServiceShortName} med Basic Authorization (ApiUserName:ApiKey, Base64-kodat).

```csharp
var httpRequestTokenMessage = new HttpRequestMessage(HttpMethod.Get,
   string.Format("{0}/authenticate/{1}", ApiUrl, ServiceShortName));
var basicAuth =  new AuthenticationHeaderValue("Basic", Convert.ToBase64String(new
   UTF8Encoding().GetBytes(ApiUserName + ":" + ApiKey)));
httpRequestTokenMessage.Headers.Authorization = basicAuth;

var client = new HttpClient();
var request = client.SendAsync(httpRequestTokenMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
var httpResponse = request.Result;
if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
   return;
var bearerToken = httpResponse.Content.ReadAsStringAsync().Result;
```

### Kodexempel C# – FileUpload med Bearer Token

Bifogar filer via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/FileUpload som MultipartFormDataContent: en JSON-del med namnet CaseBaseRequest och en del per fil med namnet file. Per fil kan Content-Disposition-parametrarna useReceipt, fileDescription och fileDefinition anges. Kommentaren `//←` avslutar i originalet blocket som bara behövs för dessa parametrar.

```csharp
var content = new MultipartFormDataContent();

const string ServiceShortName = "kortnamn";
const string CaseUniqueId = "ärendenummer";
const string DiaryNumber = "";
const bool DisableSendNotification = false;

var stringContent = new
StringContent($"{{\"UniqueId\":\"{CaseUniqueId}\",\"DiaryNumber\":\"{DiaryNumber}\",\"Comment\":\"Test av V2api\",\"Actor\":\"ConsoleApp\",\"DisableSendNotification\":\"{DisableSendNotification}\"}}");
stringContent.Headers.Add("Content-Disposition", "form-data; name=\"CaseBaseRequest\"");
content.Add(stringContent);

var files = new[] { @"C:\Temp\Test1.pdf", @"C:\Temp\Test2.pdf" };

foreach (var file in files)
{
   var fileStream = new FileStream(file, FileMode.Open);
   var fileName = Path.GetFileName(file);
   var streamContent = new StreamContent(fileStream);

   //Only needed when we want to use useReceipt, fileDescription or fileDefinition
   streamContent.Headers.Add("Content-Type", "application/octet-stream");
   streamContent.Headers.Add("Content-Disposition", "form-data; name=\"file\"; filename=\"" + URI.EscapeDataString(filename) + "\"");
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("useReceipt", "true"));
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("fileDescription", " beskrivning"));
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("fileDefinition", " typ"));
   //←

   content.Add(streamContent, "file", fileName);
}

var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
   string.Format("{0}/v2/services/{1}/cases/FileUpload", ApiUrl, ServiceShortName));
var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
httpRequestMessage.Headers.Authorization = bearerAuth;
httpRequestMessage.Content = content;

var client = new HttpClient();
request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
httpResponse = request.Result;
if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
   return;
var response = httpResponse.Content.ReadAsStringAsync().Result;
```

### Kodexempel C# – UpdateStatus med Bearer Token

Sätter status (i exemplet ”Makulerat”) via PUT {ApiUrl}/v2/services/{ServiceShortName}/cases/UpdateStatus med JSON-body.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"State\":\"{4}\",
      \"DisableSendNotification\":\"{5}\"}}",
   CaseUniqueId, DiaryNumber, "Test av V2api", "ConsoleApp", "Makulerat", false));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Put,
      string.Format("{0}/v2/services/{1}/cases/UpdateStatus", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

### Kodexempel C# – GetByDateAndState

Söker ärendenummer via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/GetByDateAndState (datumintervall, statusar ”inkommet”/”avslutad” och filter på fältsvar) och itererar över resultatet för att hämta varje ärende med GetDetailed.

```csharp
using (var client = new HttpClient())
{
   var str = "{\"FromDate\":\"2012-01-01\", \"ToDate\":\"2015-12-12\",
      \"Comment\":\"Test av V2api\", \"Actor\":\"ConsolApp\", \"States\":[\"inkommet\",
      \"avslutad\"], \"ExcludeCasesWithDiaryNumber\":false, \"Field\":{\"Answer\":
      \"ett fältsvar\", \"Argument\":{\"Name\":\"integrationsargumentets namn\",
      \"Value\":\"integrationsargumentets värde\"}}}";

   var stringContent = new StringContent(str);
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
   string.Format("{0}/v2/services/{1}/cases/GetByDateAndState", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
      HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;

   var ids = JsonConvert.DeserializeObject<IEnumerable<string>>(stringContents);
   var enumerable = ids as string[] ?? ids.ToArray();

   if (ids == null || !enumerable.Any())
      return;

   foreach (var id in enumerable)
   {
      // Get detailed case via GetDetailed
   }
}
```

### Kodexempel C# – GetDetailed med Bearer Token

Hämtar ett detaljerat ärende via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/GetDetailed med XmlGeneratorType DefaultXmlCaseGenerator och sparar svaret som XML-fil under C:\Temp.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"XmlGeneratorType\":\"{4}\",
      \"IncludeAllFields\":\"{5}\",\"IncludeAllAttachements\":\"{6}\",
      \"OmitXmlDeclaration\":\"{7}\"}}", uniqueId ?? CaseUniqueId, "", "Test av V2api",
      "ConsolApp","Abou.Calamare.Framework.Integration.Xml.Default.DefaultXmlCaseGenerator", true, true, true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/GetDetailed", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;

   var response = httpResponse.Content.ReadAsStringAsync().Result;

   File.WriteAllText(string.Format(@"C:\Temp\{0}.xml", uniqueId ?? CaseUniqueId),
      response);
}
```

### Kodexempel C# – AttachmentDownload med Bearer Token

Hämtar en specifik bilaga (SystemFileName ”150907-AAA-UL67_abou_produktblad.pdf”) och sparar den som fil. Observera att exemplet anropar sökvägen `…/cases/CaseAttachmentDownload`, medan metoden i API-beskrivningen heter AttachmentDownload.

```csharp
const string systemFilename = "150907-AAA-UL67_abou_produktblad.pdf";

using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"SystemFileName\":\"{4}\"}}",
      uniqueId ?? CaseUniqueId, "", "Test av V2api", "ConsolApp", systemFilename));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/CaseAttachmentDownload", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var data = httpResponse.Content.ReadAsByteArrayAsync();

   File.WriteAllBytes(string.Format(@"C:\Temp\{0}", systemFilename), data.Result);
}
```

### Kodexempel C# – AddCitizens med Bearer Token

Lägger till två invånare (Kalle Karlsson och Sven Svensson) på ett ärende via PUT {ApiUrl}/v2/services/{ServiceShortName}/cases/AddCitizens.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Citizens\":" +

      "[{{\"UserIdentity\":\"121212121212\",\"FirstName\":\"Kalle\",\"LastName\":
      \"Karlsson\",\"Email\":\"kalle@karlsson.se\"}}," +

      "{{\"UserIdentity\":\"121312127374\",\"FirstName\":\"Sven\",\"LastName\":
      \"Svensson\",\"Email\":\"sven@svensson.se\"}}]," +

      "\"Comment\":\"{2}\",\"Actor\":\"{3}\",\"UpdateExisting\":false,
      \"OmitSocialSecurityNumberValidation\":false," +

      "\"DisableSendNotification\":\"{4}\"}}", CaseUniqueId, DiaryNumber,
      "Test av V2api", "ConsolApp", true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Put,
      string.Format("{0}/v2/services/{1}/cases/AddCitizens", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

### Kodexempel C# – CreateCase med Bearer Token

Skapar ett nytt ärende via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/CreateCase med två fältsvar (integrationsargument ArgumentName1/ArgumentName2), Citizen, SentInAs ”Citizen” och signeringsdata.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"Fields\":[{{\"Answer\":
      \"Fältsvar förnamn\",\"Arguments\":[{{\"Name\":\"ArgumentName1\",\"Value\":
      \"ArgumentValue1\"}}]}}," +

      "{{\"Answer\":\"Fältsvar efternamn\",\"Arguments\":[{{\"Name\":\"ArgumentName2\",
      \"Value\":\"ArgumentValue2\"}}]}}]," +

      "\"Citizen\":{{\"UserIdentity\":\"121212121212\",\"FirstName\":\"Kalle\",
      \"LastName\":\"Karlsson\",\"Email\":\"kalle@karlsson.se\"}}," +

      "\"Comment\":\"{2}\",\"Actor\":\"{3}\",\"UpdateExistingCitizen\":false,
      \"OmitSocialSecurityNumberValidation\":false," +

      "\"SentInAs\":\"Citizen\",\"SignatureData\":\"signdata\",\"SignatureIssuer\":
      \"signer\"," +

      "\"DisableSendNotification\":\"{4}\"}}", CaseUniqueId, DiaryNumber,
      "Test av V2api", "ConsolApp", true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/CreateCase", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

## Testa REST API (Postman, YARC)

Kan enkelt göras med verktyget Postman eller t.ex. YARC som är ett tillägg till Google Chrome:

### Bild: Test av Authenticate i YARC (Chrome-tillägg)

Skärmbild från YARC som visar ett lyckat anrop till Authenticate (hämta token). Text i bilden:

- **Request Settings**
 - URL: `https://abou.sokigo.com/api/authenticate/AAA`, metod: **GET**
 - Payload: tomt fält med platshållartexten `application/json`
- **Custom Headers** (hopfälld panel)
- **Authentication**: ”Basic Authentication is supported. Enter a username and password and the Authorization Header will be generated and sent with the request.”
 - Authorization: `Basic YWJvdTyAdA91YAda` (avläst från skärmbilden; kan innehålla avläsningsfel). Knapp: *Add Credentials*
- Knapp: *Send Request*
- **Response**
 - Request URL: `https://abou-a3-dev.abou.se/api/authenticate/ABOU123`
 - Request Method: GET
 - Response Time: 0.29 seconds
 - Response Status: 200 - OK (visas även som en stor grön ruta med ”200”)
 - Flikar: *Response Body* (vald), *Response Body (RAW)*, *Response Headers*, *Request Details*
 - Knappar: *Copy Request*, *Copy Response*

Response Body i skärmbilden (JWT-token; header-delen i fetstil, resten i rött). Avläst från skärmbilden: payload-delen är kontrollerad genom Base64-avkodning, signaturdelen (efter sista punkten) kan innehålla avläsningsfel:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJc3MiOiJhYm91IiwiRXhwIjoiMjAyMS0wOC0yM1QwODoyNjozNC44MTkyMTUxWiIsIlNlcnZpY2VTaG9ydE5hbWUiOiJBQk9VMTIzIiwiU3lzdGVtUGVybWlzc2lvbiI6MjQsIlNlcnZpY2VQZXJtaXNzaW9uIjoyNTQsIkN1c29tZXJJZCI6MTAwMn0.c4NOmKFBEfbFnrEsbOO4bDw_1A-SoVLebt30hlKKLnw
```

## Att använda RestwrapperPluginet via REST-API

Gäller metoderna för Begäran om komplettering (RequestSupplementExistingCase, RequestSupplementNewCase) och Delgivning av beslut (DecisionOnExistingCase, DecisionToNewCase).

Följande metoder har stöd för att ta emot argument som gör att RestwrapperPluginet kan skicka ett anrop för att tillexempel skapa ett läskvitto i ett annat system när invånaren tar del av ett beslutsdokument:

- Begäran om komplettering – anrop körs när invånaren utför kompletteringen
- Delgivning av beslut – anrop körs när beslutsdokumentet laddas ned för första gången

För att detta ska kunna användas krävs att man har tillgång till RestwrapperPluginet samt att lämplig konfiguration för anropet har lags in. Utöver detta ska man skicka med följande värden som Name i Arguments

- ConfigurationDataKey – Nyckeln på den konfiguration som skall användas
- ServicePurpose – Grundmodell för hur Restwrappern ska hantera ärendet, t.ex. CaseAsGenericModel
- IncludeCaseParameters – true/false, valfritt. Bestämmer om parametrar för tokens från ärendet ska inkluderas till anropet

Det finns också stöd för att skicka med ytterligare värden som kommer att hanteras som om de vore integrationsargument ifrån ärendet.

---

# CitizenInfo and Citizen

Source: *CitizenInfo*. Read 2026-08-25.

Person data always comes from an **external plugin** (Navet, KIR, PulsenId, TEIS, …). Builder Python: also and mallar.

## CitizenInfo (stored)

On login, Abou looks up the configured service:

1. If a person is found, these are stored: FirstName, LastName, Email, CompanyPhone, HomePhone, MobilePhone, CompanyName, City, AllAddress, MunicipalityKey, ProtectedIdentity.
2. Else only values from the **login** IdP are mapped (name, email, phones, company).
3. A row is inserted/updated in table **CitizenInfo**.

That row is what ties the user to e-tjänster and UI preferences. In page logic it is **`self.Citizen`** (GDPR-stripped — civilstånd, födelse, raw CitizenData often empty). Keep the class small; some fields are no longer maintained unless a setting is on.

Direct lookup **without** saving and **without** GDPR stripping:

```
self.GetCitizenInfoLookup(socialSecurityNumber)
```

(Docs also spell `GetCitizenInfoLookUp`.) Session only.

## Citizen (not stored)

`DefaultCitizenService.GetCitizen(personnummer)` hits the configured person service and maps to **Citizen**. Not written to DB. Unified interface so plugins can change without rewriting mallar. Relatives and civilstånd are examples — **not every plugin has every field**.

`GetCitizenAsJson(personnummer)` returns the source JSON string. **Sekretess / skyddad identitet sits above the PersonPost** and is **not** visible via this method. Same payload may appear as `CitizenData` for Navet and TEIS.

## Field mapping (Kir / Navet / PulsenId / Teis)

| Field | Kir | Navet | PulsenId | Teis |
| --- | --- | --- | --- | --- |
| CitizenData | no | yes | no | yes |
| SocialSecurityNumber, FirstName, LastName | yes | yes | yes | yes |
| MunicipalityKey | yes | yes | yes | no |
| MaritalStatusCode | no | yes | no | yes |
| ProtectedIdentity | yes | yes | no | no |
| ProtectedIdentityCivilRegister | no | yes | no | no |
| Address.PostalAddress / PostalCode | yes | yes | yes | yes |
| Address.CareOf | yes | yes | yes | no |
| BirthPlace (+ CountyCode, Community, OverSea*) | no | yes | no | Teis: BirthPlace yes, subfields empty |
| Relatives | no | yes | yes | yes |
| Relative SSN, TypeOfRelation | no | yes | yes | yes |
| Relative Deregistrated | no | yes | no | no |
| Relative FirstName, LastName | no | no | yes | yes |

Do not log real personnummer.

---

# HtmlCaseModel (Razor)

Source: *HtmlCaseModel*. Read 2026-08-25.

Used in **dokumentmallar**, **e-postmallar**, and thank-you text when the page type is **ThankYouAdvanced**.

This is **not** the Python `PageNode` case object. In e-tjänst logik, use PageNode helpers, not these entities.

Access with `@`:

```
@Model.UniqueId
```

Razor (C#). WYSIWYG for mail / ThankYouAdvanced: prefer short expressions, not raw HTML control flow:

```
@(Model.Decision != null ? Model.Decision.DecisionText : "Beslut ej fattat")
```

Dokumentmallar may use `@if`.

Nullables: never dereference when null.

## Model / Case

`Model` is `HtmlTemplate.Case`.

| Name | Type | Meaning |
| --- | --- | --- |
| Id | int | DB id (internal) |
| UniqueId | string | Ärendenummer |
| DiaryNumber | string | Diarienummer (handläggare, e-tjänst, or API) |
| State | string | Status (Inkommet, Registrerat, Avslutat, …) |
| SentInAs | CitizenRole | Submitter role |
| Administrator | Administrator | Assigned caseworker |
| Submitted | DateTime | Submit time |
| Applicant | Citizen | Submitter |
| CoApplicants | Citizen enumerable | Medsökande |
| HasBeenSignedByAll | bool | All co-signers signed |
| Service | Service | E-tjänst |
| Payments | List of Payment | Payments |
| IsSignedAlternatively | bool | Print-and-post |
| HasMultipleSigning | bool | Multipelsignering or Attestlista med sök |
| SentInByOmbudsman | bool | Ombud |
| Proposal | Proposal | E-förslag if configured |
| Decision | Decision | Latest decision |
| Fields | List of Field | All fields |
| Signatures | List of Signature | Signatures |
| ApplicantSignature | Signature | Applicant |
| SortedRecentCoApplicantSignatures | List | Co-signers by name |
| SortedRecentAttestSignatures | List of SignatureAttest | Attest |
| FirstSignedByAll | DateTime? | When all required signatures existed; use `.HasValue` before `.Value` |
| Pages | enumerable | Layout pages for the PDF dump |
| Supplements | enumerable | Requested kompletteringar |
| `Model[friendlyId]` | Field | Lookup by FriendlyFieldId |
| HasValue(friendlyId) | bool | True when that field should print |

### Page / Block (dokumentmall)

| Name | Meaning |
| --- | --- |
| page.DisplayName | Page title in the PDF |
| page.HasAnyValues | Skip empty pages |
| page.IsBlockPage | Blocks have their own headers |
| page.Blocks | Blocks on the page |
| block.Header | Caption when IsBlockPage |
| block.Fields | Fields to loop (prefer this over `page.Fields` in new mallar) |

`Model.HasValue(field.FriendlyFieldId)` — skip unanswered questions on the PDF.

Table-like answers: `field.Answer.Contains("<table ")` (substring, including the space). Then print Answer as HTML, not as a plain cell.

### Administrator

UserName, FirstName (actually **full name**), Email — empty string if unassigned / unknown.

### Citizen (template)

Id, SocialSecurityNumber (personnummer or AD identity), FirstName, LastName, Email, PhoneNumber, MobilePhoneNumber, Address, City, PostalCode, MunicipalityKey, metadata dictionary.

### Decision

Date, Comment, DecisionText (**Avslaget** or **Godkänt**), **Adminstrator** (spelling in the model — full name, else username, else empty / API).

### Service

RequiresEid / RequiresAuthentication / RequiresSignature / RequiresMultipleSignatures, DisplayName, Name, ShortName, ServiceNr (stable across versions).

### Field

| Name | Meaning |
| --- | --- |
| Answer | Display answer (string or HTML) |
| Question | Rubrik e-tjänst |
| FriendlyFieldId | Id for `@Model["x.1"]` |
| RawAnswer | Original (sometimes JSON) |
| PostFieldHtml / PreFieldHtml | Text under/above field |
| SummaryQuestion | Rubrik ärende |
| TypeOfField | Internal (e.g. `EGovTextField`) — not citizen-facing |
| IncludeEmptyAnswer | Show empty on summary |
| HasAnswer | True if answered (empty counts if IncludeEmptyAnswer) |

### Payment

Amount (provider units may differ), OrderId, Date, PayedBy (Citizen; docs note it “borde heta PaidBy”), PaymentType, TransactionId.

## Signatures

`ApplicantSignature` — the sökande. `SortedRecentCoApplicantSignatures` — medsökande. `SortedRecentAttestSignatures` — attest; extra `SignatureAttest.AnswerString`, `.Comment`, `.Attachment` (FileName). `Signatures` — full list; filter with `SignatureType.Applicant` (namespace `Abou.Calamare.Framework.HtmlTemplate`).

Each signature: `Signed` (DateTime), `Issuer`, `SignedBy` (FirstName, LastName, SocialSecurityNumber, DisplayName).

```
@Model.ApplicantSignature.SignedBy.DisplayName
@foreach (var signature in Model.SortedRecentCoApplicantSignatures){@(signature.SignedBy.DisplayName + "\n")}
```

## Supplements

Title, DateRequested, DateCompleted, OriginalFileNamesJoined, CitizenComment. Loop `Model.Supplements`.

## Enums (UPPRÄKNINGAR)

**CitizenRole:** Unknown, Citizen, Company, Organisation.

**PaymentType:** Applicant, CoApplicant.

**ProposalFilterType** (e-förslag list filters): *Inväntar publicering*, *Röstning pågår*, *Inväntar ställningstagande*, plus decided statuses *Godkänt* / *Avslaget* / *Besvarat* / *Avslutad*. URL example: `/Citizen/Proposal?status=Godkänt&status=Avslaget` (space as `%20`).

Substitution tokens `$name$` are listed under meddelandemallar / tokens.

---

# Compliance, hosting, browsers, eIDAS

Read 2026-08-25. High-level only.

## Protocols (pageId `60096956`)

From **2022.8**, HTTPS to external systems: **TLS 1.3** and **TLS 1.2**. TLS 1.1 / 1.0 not supported. SSL3 not enabled by default.

## Browsers (pageId `60096958`)

Latest **Edge, Firefox, Chrome, Safari**. Older versions only as long as they are not a security hole.

## GDPR (*Information om GDPR*)

Sokigo documents GDPR approach, internal systems, planned work, and customer responsibilities. Person data in Abou is plugin-backed . Do not store extra person fields in Python. Scheduled **Synkronisera personuppgifter** and soft/permanent delete are the operational tools .

## eIDAS (*Vad är EIDAS*, pageId `60096954`)

EU e-ID: foreign e-leg in Swedish public services. Identifier is **not** always a Swedish personnummer — country codes + id. No new Abou version required; municipality talks to their e-leg IdP, Sokigo maps metadata (may patch).

Citizen flow: pick service → IdP → BankID / Mobilt BankID / **eIDAS** → back to Abou.

Per service, the municipality chooses what a foreign-id user may do (info page, English variant, or full flow). **Integrerat personnummerfält** should become **integrerat användarnamnsfält** (or branching logic) if foreign ids must submit. Min sida then works like BankID.

## Accessibility (*Tillgänglighetsredogörelse*, pageId `60096950`)

Law: SFS 2018:1937. Sokigo targets **WCAG 2.1 AA** and **EN 301 549**. Useit reviews. Known remaining deviations (fix in product; also depend on how you build the e-tjänst):

- Maps: not screen-reader/keyboard — always offer address/coordinate input
- **Rullista med sök** not usable with screen readers
- Error messages for radio/checkbox **groups** not correctly associated
- Table layout can confuse some screen readers
- Graphic captcha on e-förslag — **do not use**
- **Lägg till rad** not accessibility-adapted — avoid when a11y is required
- Failed-submit error not presented correctly; after reload focus jumps to top

2019-03-11 Useit findings on the Lyckebo theme were addressed in **2021.2**. Customer content (images, PDFs) is the municipality’s a11y duty.

## Penetration tests

Confluence *Penetrationstester av Abou* records that tests exist. **Do not copy exploit detail into this skill.**

## Hosting PDFs (not transcribed)

- Ansvarsfördelning vid drift On Prem (`161742875`)
- Teknisk kravspecifikation - Abou Intern Hosting

---
