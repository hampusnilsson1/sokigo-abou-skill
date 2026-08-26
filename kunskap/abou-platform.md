# Abou-plattform — kunskapsbas

All kunskap utanför byggaren: behörigheter, admin, ärenden, Min sida, köer, bokning, register, e-förslag, schemaläggning, dokumentmallar, FAQ, Funktionalitet, REST-metodnamn, CitizenInfo, HtmlCaseModel, GDPR/TLS.

Detta är en **sammanslagen kunskapsfil** för en AI. All kunskap från skillen `abou-platform` ligger här. Svara från den här filen. Hitta inte på API:er, behörigheter eller fält som inte står här. Svenska UI-namn från Abou gäller.

Källfiler (samma innehåll som under `.cursor/skills/`):

- `SKILL.md`
- `references/INDEX.md`
- `references/catalog.md`
- `references/permissions.md`
- `references/scheduling.md`
- `references/min-sida.md`
- `references/queues.md`
- `references/modules.md`
- `references/document-templates.md`
- `references/admin.md`
- `references/cases.md`
- `references/booking.md`
- `references/registers.md`
- `references/e-forslag.md`
- `references/functionality.md`
- `references/faq.md`
- `references/sharing.md`
- `references/operations.md`
- `references/message-tokens.md`
- `references/technical/INDEX.md`
- `references/technical/rest-api.md`
- `references/technical/citizeninfo.md`
- `references/technical/htmlcasemodel.md`
- `references/technical/compliance.md`

---

## Källa: `SKILL.md`

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
| REST API, CitizenInfo, HtmlCaseModel, GDPR, TLS | [technical/INDEX.md](references/technical/INDEX.md) |

Builder pages, fields, Python mallar: **not here** — use `build-abou-etjanst-web`.

## Guardrails

- These notes are for **explaining and configuring**. They are not a licence to open production ärenden, impersonate, or change live data.
- Do not invent REST methods, Razor fields, or permission rights. If it is not in these files, say so. Naming the old wiki title in [catalog.md](references/catalog.md) is for maintainers filling gaps — not something to tell the user to open.
- Python in the builder still needs systembehörighet **Redigera och exekvera Python-kod** ([permissions.md](references/permissions.md)).


---

## Källa: `references/INDEX.md`

# Abou platform — pick one file

These files **are** the documentation. The wiki is behind login; do not send the user there. Read 2026-08-25.

**Do not load this whole folder.** Builder pages/fields/Python: [build-abou-etjanst-web](../../build-abou-etjanst-web/SKILL.md). Page list: [catalog.md](catalog.md).

| Need | File |
| --- | --- |
| Roles: sysadmin, systembehörighet, e-tjänst (redaktör … verksamhetsadmin) | [permissions.md](permissions.md) |
| Schemalagda jobb (påminnelser, status, radering, Navet-sync, fil) | [scheduling.md](scheduling.md) |
| Min sida / Min sida Plus, Att göra, villkor, 2021.2 / 2024.2 | [min-sida.md](min-sida.md) |
| Köfält, skapa kö, handlägg, årsavgift, medborgarflöde | [queues.md](queues.md) |
| Which modules Sokigo switches on | [modules.md](modules.md) |
| Admin: publicera, import/export, organisationer, statistik | [admin.md](admin.md) |
| Ärendelista, loggbok, diarienummer | [cases.md](cases.md) |
| Bokningsmodulen | [booking.md](booking.md) |
| Registermodulen | [registers.md](registers.md) |
| E-förslag | [e-forslag.md](e-forslag.md) |
| Dokumentmallar, blankett, editerbar PDF | [document-templates.md](document-templates.md) |
| Feature pages under Funktionalitet | [functionality.md](functionality.md) |
| FAQ Q&A | [faq.md](faq.md) |
| Dela e-tjänster med andra kommuner | [sharing.md](sharing.md) |
| Checklista driftsättning / deploy | [operations.md](operations.md) |
| `$uniqueID$`, kö/bokning tokens, Razor in mallar | [message-tokens.md](message-tokens.md) |
| REST API method names | [technical/rest-api.md](technical/rest-api.md) |
| `self.Citizen` vs `GetCitizen` vs GetCitizenAsJson | [technical/citizeninfo.md](technical/citizeninfo.md) |
| `@Model` in dokumentmall / ThankYouAdvanced / e-post | [technical/htmlcasemodel.md](technical/htmlcasemodel.md) |
| GDPR, eIDAS, TLS, browsers, WCAG, hosting | [technical/INDEX.md](technical/INDEX.md) |


---

## Källa: `references/catalog.md`

# Abou space catalog (outside builder + integrations)

Ingested 2026-08-25 from Confluence space Abou. **Answer from the notes files**, not from wiki URLs.

**Already in `build-abou-etjanst-web`:** *Att bygga e-tjänster* and *Integrationer*. Do not duplicate those here.

**Not ingested (intentionally):** Release-note bodies, Community presentations, Webinar videos, Minut Bygg, Minut Miljö. REST API request/response schemas (PDF). On-prem hosting PDFs (headings only in compliance). Testpersoner personnummer (never copy into git).

## Abou (main hub)

### Administrationsidorna
Administrera Organisationer; Administrera Text Och Bild I Abou; Aktivera/Inaktivera E-Tjänst; Ange Öppettider För En E-Tjänst; Forcera Ärenden (Signera Som Ombud); Frågor Och Svar; Hantera Behörigheter; Hantera Dokument; Importera Och Exportera E-Tjänster; Integrationslogg; Menygrupper; Permanent Borttagning Av Ärenden; Publicera E-Tjänst Och/Eller Blankett; Skicka In Ärende Som Ombud; Statistik Och Rapporter; Systemhändelser; Sök Och Ta Bort Invånare (Personpost); Ta Bort E-Tjänst I Admin; Ändra Organisation För En E-Tjänst; Ändra Texter I E-Tjänster.

Notes: [admin.md](admin.md). PDF/dokumentmallar: [document-templates.md](document-templates.md).

### Ärendehantering
Ärendelistan Och Ärendedetaljvy; Ärendets Diarienummer; Handlägga Ärenden; Loggboken.

Notes: [cases.md](cases.md).

### Behörighetsnivåer
Introduktion Behörigheter; Systembehörigheter; Systemadministrator; E-Tjänstebehörighet: Verksamhetsadministrator; Beslutsfattare; Statusuppdaterare; Läsbehörighet; Skicka In Ärende; Redaktör; Behörighet På Individ-Eller Gruppnivå.

Notes: [permissions.md](permissions.md).

### Bokningsmodulen
Beskrivning; Handläggning Av Bokningar; Skapa Nytt Bokningstillfälle; Återkommande Bokningstillfällen; Boka Om Och Avboka; Konfigurera Bokningar; Bokningsmeddelanden.

Notes: [booking.md](booking.md).

### Dela e-tjänster med andra
Notes: [sharing.md](sharing.md).

### E-Förslag
Beskrivning; Skapa E-Tjänst För Att Lämna Förslag; Inställningar; Handlägga Förslag; Handlägga Kommentarer; Rösta Som Ombud; Läsa, Rösta, Dela Och Kommentera; Texter I Invånarvy; E-Förslagsmeddelanden.

Notes: [e-forslag.md](e-forslag.md).

### FAQ
All Q&A pairs: [faq.md](faq.md).

### Funktionalitet
Feature pages: [functionality.md](functionality.md).

### Kömodulen
Beskrivning; Komma Igång; Skapa Ny Kö; Konfigurera En Kö; Handlägga Köer (+ byt köplats, digital betalning, lägg till manuellt, ta bort, uppdatera kontakt, uppdatera registreringsdatum, uppdatera status); Köbetalning; Köer: Hur Gör Invånaren; Köfilter; Kömeddelanden.

Notes: [queues.md](queues.md).

### Meddelandemallar
Exempel; Exempel (multipelsignering); Koppla Meddelandemall Till E-Tjänst; Skapa/Redigera/Ta Bort; Statusnotifieringar; Värden I Meddelandemallar.

Builder-adjacent: `build-abou-etjanst-web/references/messages.md`. Tokens: [message-tokens.md](message-tokens.md). Razor model: [technical/htmlcasemodel.md](technical/htmlcasemodel.md).

### Min sida
Att Göra; Beskrivning (2020.11 och tidigare); Direktmeddelanden; Händelser; Köplatser Och Bokningar; Publicering Och Villkorsstyrning; Tjänster.

### Min sida 2021.2 och 2024.2
Funktioner Som Stöds; Övergripande Beskrivning Min Sida Och Min Sida Plus; Video; Min sida efter 2024.2, med sidor som översta nivå.

Notes: [min-sida.md](min-sida.md).

### Moduler
Schemaläggningsmodul; E-Förslagsmodulen; Betalningsfunktion; Min Sida; Användningsmodulen; Kömodulen; Bokningsmodulen; Register.

Notes: [modules.md](modules.md).

### Projektdokument, Checklistor Och Processer
Kundservice/Support; Deployprocess; Checklista: Driftsättning Av E-Tjänst.

Notes: [operations.md](operations.md).

### Registermodulen
Fokuswebinar; Beskrivning; Import Och Export; Redigera Register; Koppla Register Och E-Tjänst; Behörigheter För Register; Text/Värdeseparering.

Notes: [registers.md](registers.md).

### Release notes
V26; 2025.11 … back through 2021 and earlier. **Not copied** into the skill (too large / version-specific). Ask Sokigo or the live wiki for a named version.

### Schemaläggning
Beskrivning; Ärendepåminnelser; Bokningspåminnelser; Köplatspåminnelser; Notifiering Vid Röstningsperiodens Slut; Signeringspåminnelse; Skapa Fil; Synkronisera Personuppgifter; Ta Bort Ärenden Mjukt; Ta Bort Ärenden Permanent; Uppdatera Status På Ärende.

Notes: [scheduling.md](scheduling.md). From version **2018.2**.

### Teknisk Information & Dokumentation
Abou REST API; Ansvarsfördelning vid drift On Prem; CitizenInfo; HtmlCaseModel; Information Om GDPR; Penetrationstester Av Abou; Teknisk Kravspecifikation - Abou Intern Hosting; Testpersoner I Abou; Tillgänglighetsredogörelse; Vad Är EIDAS; Vilka Protokoll Stödjer Abou; Vilka Webbläsare Stödjer Abou.

Notes: [technical/INDEX.md](technical/INDEX.md).

## Other top-level in the space

- **Community** — användarträffar, webinars (not ingested).
- **Minut Bygg / Minut Miljö** — other Sokigo products; do not open.


---

## Källa: `references/permissions.md`

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


---

## Källa: `references/scheduling.md`

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

## Källa: `references/min-sida.md`

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
- Unread threads also appear under **Att göra**. Permanent case delete drops the messages ([admin.md](admin.md)).

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
- Ångra ärende not yet signed by medsökande ([functionality.md](functionality.md))
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

## Källa: `references/queues.md`

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

`$Comment$`, `$QueuePosition$`, `$QueueName$` — [message-tokens.md](message-tokens.md).


---

## Källa: `references/modules.md`

# Moduler

Sokigo enables add-ons (often without a new deploy). Do not assume a site has a module.

| Module | What it is | Notes in this skill |
| --- | --- | --- |
| Schemaläggningsmodul | Nightly/hourly jobs | [scheduling.md](scheduling.md) |
| Kömodulen | Waiting lists + köfält | [queues.md](queues.md) |
| Bokningsmodulen | Slots / appointments | [booking.md](booking.md) |
| Min sida (modul) | Citizen portal | [min-sida.md](min-sida.md) |
| E-förslagsmodulen | Suggestions + voting | [e-forslag.md](e-forslag.md) |
| Betalningsfunktion | Swedbank Pay (and others per integrations) | Builder: payment page; kö yearly fee in [queues.md](queues.md) |
| Användningsmodulen | Usage stats / reports | Needs system **Statistik och rapporter** |
| Register | Lists for dropdowns / mapping | [registers.md](registers.md) |

Hub: *Abou → Moduler*. Each child is a short product page pointing at the detailed section.


---

## Källa: `references/document-templates.md`

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

Razor object in the mall: [technical/htmlcasemodel.md](technical/htmlcasemodel.md). Changing organisation on a service switches to that org’s PDF mall, else kund/standard ([admin.md](admin.md)).

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
  <tbody> @for (int i = 0; i < page.Fields.Count(); i++) {
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
                @for (int i = 0; i < page.Fields.Count(); i++)
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
- Signing block: Sokigo can require it on all blanketter or only e-leg services. In the **Ärendeblankett** mall, wrap “Sökandes underskrift” in `if (Model.RequireId) { … }` so unsigned services omit it ([faq.md](faq.md))
- Unique layout from 3.26 = this editor (customer-editable)

Publish as menygrupp type **Blankett genererad från e-tjänst**, or generate from Admin. Role **Skicka in ärende** can generate PDF. The blankett is **not** a fillable computer form — print, fill by hand, post.


---

## Källa: `references/admin.md`

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


---

## Källa: `references/cases.md`

# Ärendehantering

Menu **Ärenden**. Rights: [permissions.md](permissions.md).

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
| Forcera / ombud sign | [admin.md](admin.md) |
| Skicka meddelande | Needs login, integrated personnummer, or configured email field — builder `messages.md` |
| Ta bort | Soft delete |
| Loggbok | Headings defined **on the e-tjänst**. Same headings for all cases of that service. Cannot delete a heading that has entries; can close a heading for new entries. Deleted entries are struck through (who/when) and omitted from Excel. Read: Läs+; write: Statusuppdaterare+ |

**Läsbehörighet:** view + open attachments only.

## Diarienummer vs REST

UI or API `UpdateDiaryNumber`. Message when **När diarienummer sätts**.


---

## Källa: `references/booking.md`

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

Service **Redigera meddelanden → Bokningsmeddelanden → Lägg till ny**. When: **Bokning** (citizen book or admin rebook), **Avbokning** (citizen or admin), **Vid påminnelse** (scheduled). Prefer **Bokning** over “ärendet inkommit” as confirmation — inkommit does not mean a slot was booked. One mall per recipient (invånare / funktionsbrevlåda / handläggare). Tokens: [message-tokens.md](message-tokens.md). Reminders: [scheduling.md](scheduling.md).


---

## Källa: `references/registers.md`

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

Anyone in Admin can **see** registers and coupling. Editors can couple. Create/update/import/export/delete needs system **Administrera Register**.

## Text/värde

In a row: `visningstext:::värde` (three colons). Hidden value for fältregler / logikhopp.


---

## Källa: `references/e-forslag.md`

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

## Källa: `references/functionality.md`

# Funktionalitet

How Abou behaves after the builder. Builder how-to (pages, fields, Python mallar) stays in `build-abou-etjanst-web`. FAQ: [faq.md](faq.md). These notes are the knowledge — do not send the user to Confluence.

## Dokumentmallar / blankett / editerbar PDF

[document-templates.md](document-templates.md)

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

After submit. Login or integrated personnummer. **One file at a time** (each gets its own description) → Relaterade filer. Works even if the service has no filuppladdningsfält. Optional notifiering to handläggare / funktionsbrevlåda / invånare. Handläggare file-komplettering from 2021.2: [cases.md](cases.md).

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

Same integration. Use when payment in the service is optional, or for **årlig köavgift** (mail → log in → pay). List of unpaid cases; **Tillbaka** = fail → error page with link back to the payment overview. [queues.md](queues.md), [min-sida.md](min-sida.md).

## Ombud / forcera signering

[admin.md](admin.md)

## Multipelsignering

Builder: `create-and-settings.md`. FAQ for one vs two guardians: [faq.md](faq.md). Field **Attestlista med sök** is **internal** attest (AD), not citizen guardians — see Attestering below.

## Ångra ett ärende som inte har signerats av medsökande

Service Inställningar **Tillåt sökande att ångra ärendet under Min sida** (off by default). While status is **Väntar på medsökandes signatur**, the applicant on Min sida can **Ångra ärende**. The case returns to **utkast** (spara/återuppta): they can change answers and submit again. Related setting **Tillåt sökande att ändra ärendet under Min sida** (builder `create-and-settings.md` / `messages.md`) is the same family of “revert while waiting for co-sign”.

## Attestering

Variant of multipelsignering: one or more **attestanter** must answer (with e-sign) before the case is Inkommet and can be handlagd. Needs **inloggning**. Signing from the sökande is usual but **not** a technical requirement.

### Attestlista med sök

Searchable dropdown. Alternatives: `Efternamn|Förnamn|UID|E-postadress` (all four, pipe-separated). UID = personnummer **or** AD short name, depending how the site identifies users. Or Python `SetOptions`. Optional 5th help segment with `{1}` `{2}`. Common: AD lookup of the user’s chef (`InternalWebSearch`). Builder: `field-types.md`.

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

Query string `?namn=värde` (`&` between pairs) lands in `self.Service.SessionParameters` (string dict, **case sensitive**). Use to know *where* the service was started or to prefill. Builder mall: *Starta e-tjänst med parametrar i url och sedan använda dom* (`logic-templates/url-parameters.md`). Check `in` before indexing.

Example: `https://service.kommunnamn.se/GRUSK?skola=Lyckoskolan&årskurs=3` then Python can prefill school/year or skip pages.

## Mina meddelanden (DIGG)

Encrypted digital mailbox (Kivra, Min myndighetspost, Bring Digimail). Full product notes: builder `integrations/mina-meddelanden.md`.

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

Typical: felanmälan where the citizen picked the wrong förvaltning — change the choice so the case routes internally. If **Meddelande per svarsalternativ** is on, a **new** funktionsbrevlåda mail goes out for the new choice (builder `messages.md`).

Combined with behörighet-per-alternativ: dialog warns that the field drives rights; picking an alternative they do not have makes the case unavailable to them.

## Synkronisera användare med AD

Only with **LDAP** AD login (not IdP). Rights live on **Abou groups that match AD groups**; users need not be created by hand. For mail, Abou still needs the user’s e-post — that is what sync fills.

**Behörigheter → Grupper → Synkronisera användare**: syncs every AD user who sits in an AD group that exists in Abou. Updates name/email; **creates** missing users. **Does not delete** a user who left the AD group (remove in Abou by hand). Synced users **cannot** be edited in Abou and **cannot** get individual e-tjänst or system rights — all via the group.

Import/create service: Redaktör is **not** auto-granted to the synced user; they pick **which group(s)** get the right.

**Sluta synkronisera** on the user: then edit rights in Abou (or inactivate to remove).

Lookups also run at login, on the rights UI, and when showing assigned handläggare. LDAP vs IdP product: builder `integrations/active-directory.md`.

## Krypterad e-post (tilläggsbeställning, from 3.28)

S/MIME on **standardmeddelanden**, aimed at funktionsbrevlådor. Needs cert on the server: encryption cert public `.crt`/`.cer` **and** signing cert private `.pfx`. Recipients need the matching private key to read. Price: kundansvarig.

Tick on the service: **Redigera meddelanden → Standardmeddelanden → Kryptera e-post**. Mall must **not** attach PDF / PDF to Mina meddelanden. **No attachments** on encrypted mail. Extra field content in the body = Razor mall.

## Lavinmeddelande

Banner on **all pages of the external UI** (maintenance, outage). Admin **Texter → Lavinmeddelande**. Right **Uppdatera vanliga texter** = this node. Sysadmin **Uppdatera innehåll** = all nodes in the install.

## Meddelanden per svarsalternativ

Funktionsbrevlåda to different addresses from choice fields. Several such fields allowed on one service. Full builder steps: `build-abou-etjanst-web/references/messages.md`. One address per alternative; optional default address/mall/attachments when an alternative has no override.

## Skapa ett nytt ärende baserat på ett befintligt (from 2019.11)

Not “edit the old case”. A **kompletteringstjänst** maps fields onto a **ursprungstjänst** via integrationsargument. Sokigo enables **CaseServicePlugin**: on submit of the kompletteringstjänst it builds a **new** case from the original + new answers (version history kept). Original case can be closed or left unchanged. Sokigo also wires the two services. Use when a long-lived case must be updated without replaying the whole original e-tjänst (which may have changed).

## Skicka e-postmeddelande vid fel i Abou

Sysadmin mail to a fixed mailbox on failures, including: Paynova/payment, file upload, save case, update status, REST API in/out, menygrupp page load, menygrupp save in Admin, e-leg login, e-leg signing, outbound mail, Navet, SMS, other integrations.

Example: `Abou.Security.Eid.EidProvider.Logout()` with Sirius — logout abort; citizen sees no error page, but ops still get mail.

## Stöd för olika typer av e-tjänster

| Type | Login/sign | Follow case | Extra |
| --- | --- | --- | --- |
| Ingen inloggning/signering | none | no Mina ärenden | |
| Koppling via integrerat personnummer | none | yes | optional file-komplettering (Inställningar) |
| E-leg | login + sign | yes | Navet/KIR prefill; field-komplettering handläggaren begär; optional file-komplettering |
| E-leg + multipelsignering | all sökande sign | all sökande | cannot handlägg until all signed |
| Med beslut | e-leg **or** integrated personnummer | yes | download of beslut = läskvitto (who/when) |

## Responsiv anpassning

Abou **always** ships a responsive citizen UI (phone / tablet / desktop). Wiki browser matrix is historical (iOS 5–9, Android 4.3–6, old Firefox/IE/Chrome/Edge) — do not treat as current support; browsers: [technical/compliance.md](technical/compliance.md).


---

## Källa: `references/faq.md`

# FAQ (Abou Confluence)

Operational answers from the Abou space FAQ. Read 2026-08-25. Builder-only FAQ (Excel vs txt, several addresses on meddelande per svarsalternativ): `build-abou-etjanst-web`.

Do **not** invent extra Q&A. If the live product disagrees, trust the live UI.

## Ärende-PDF i mailnotifieringar

Attach the case PDF on the message mall (videoguide on the wiki). Coupling/attachments: builder `messages.md`.

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

More: Skatteverket. What data Navet can return: builder `integrations/navet.md`.

## Enkel vs avancerad grafisk anpassning

**Simple (typical Sokigo “enkel” package):** header, footer, font family/size for H1–H3 and body, up to **two** theme colours.

**Advanced:** three or more theme colours, fonts for ingress etc., content-driven formatting, custom icons, pixel tweaks, third-party search (e.g. SiteSeeker).

## Första inloggning — lösenord

New Abou user: **username as password** the first time, then change password. Same as [admin.md](admin.md).

## Dela e-tjänster med andra kommuner

There is a service on **Provrummet** used for this: *Dela e-tjänster med andra*. Details: [sharing.md](sharing.md).

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

The portal can then show **Till e-tjänst** and/or **Blankett**. The module must be enabled. Full behaviour: [document-templates.md](document-templates.md).

## När görs AD-uppslag?

- User logs in
- Someone with rights admin opens the rights UI (update user / add user)
- Assigned handläggare is loaded/shown in the case list and on case details

Product: builder `integrations/active-directory.md`. Sync users: [functionality.md](functionality.md).

## Handläggare notifierad när något hänt på dennes ärende

Configure a **statusmeddelande** to the assigned caseworker. Triggers:

- Citizen supplemented with a file
- Citizen supplemented one or more fields
- Another caseworker updated status (even just **Spara**)

## Funktionsbrevlåda till olika adresser beroende på val

Yes. Field **ServiceRequestEmail**: alternatives in a dropdown; each alternative maps to **one** email (same address may be reused). Mapping is **database configuration** (Sokigo). Typical: felanmälan by förvaltning, school services by school.

Builder also has **Meddelande per svarsalternativ** on choice fields (`messages.md`) — that is the self-serve field argument, not this ServiceRequestEmail DB map.

## Filtrera/söka i ärendelistan (Admin)

Date submitted, ärendetyp (only services you may see), status, diarienummer, ärendenummer, handläggare username. Optional extra columns = chosen fältsvar — **cannot** filter/search on those. [cases.md](cases.md).

## Vilka SQL-databaser?

Wiki list (historical): SQL 2012, SQL 2008 R2, SQL 2008; recommendation at the time was SQL 2012. **Do not treat as current hosting matrix** — ask Sokigo for the version you run.

## Visa/dölja fält direkt på sidan

Yes: **klientlogik** or **fältregler**. Builder `rules-validators.md` and client mallar.

## Ibland en, ibland två signaturer (vårdnadshavare)

Build **multipelsignering**. The extra page has the second guardian’s fields plus a radio: sole guardian or not. If sole guardian, the other fields are not required (and vice versa).

Sokigo can also wire a **Skatteverket** check of one vs two guardians. Builder: `create-and-settings.md` *Multipelsignering*.

## Vilka data från Navet?

Among others: personnummer, namn, adress, civilstånd, födelseort. Full property list: builder `integrations/navet.md`.

## Roller (invånare, företag, förening)

**Removed in Abou 2022.5** — cannot enable on new services. Sokigo recommends turning roles off on old services; new product work does not support it.

Historically: system-wide “Välj roll” before the service (names configured globally). Service must have login. If the service is configured for only one role, that role is auto-selected. Could also use field **Integrerat fält för att välja roll** instead of the global page. **Content cannot follow the role by itself** — use Python on the field answer.

## Sparas medborgarens personuppgifter?

If the citizen uses a service **with e-legitimation**, personuppgifter are stored for the next e-leg service.

## Kan kunden editera sidor (text och bild)?

Yes: ordinary pages (Kontakta oss, FAQ, Handläggningstider, …) in Admin. E-tjänst editorial (help, tacksida) too. Links and images: upload under **Dokument** first. [admin.md](admin.md).

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

**Current signing providers** on the Funktionalitet page (prefer this): Twoday (f.d. Visma Sirius), CGI, Svensk e-identitet, Signport/KnowIT (fd Cybercom). Login: any SAML2 IdP; methods Mobilt BankID, Freja, Freja eID+, eIDAS. Avtal + Sokigo config. [functionality.md](functionality.md).

## AD — vad är det?

Microsoft Active Directory for **internal** login (LDAP or IdP). Full product notes: builder `integrations/active-directory.md`. When lookups run: section above.


---

## Källa: `references/sharing.md`

# Dela e-tjänster med andra

**Provrummet** is Sokigo’s shared catalog of e-tjänster that customers have built in Abou. You can **test** those services there and **export** them, then **import** into your own Abou.

To publish one of yours into Provrummet, Sokigo provides an e-tjänst on Provrummet named **Dela e-tjänster med andra**. That is not the same as Admin zip export between your own test/prod.

After import: only **Redaktör** is granted ([faq.md](faq.md), [admin.md](admin.md)). Booking slots do not import; Python `SlotFilter` code does. Rights and editorial texts follow the usual import rules ([operations.md](operations.md)).


---

## Källa: `references/operations.md`

# Checklista och deploy

## Checklista: driftsättning av e-tjänst

### First time (service not in prod yet)

1. Export in **test**
2. Import in **prod** (grants **Redaktör** only — [faq.md](faq.md), [admin.md](admin.md))
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

Also: publishing ≠ activating; empty menygrupper stay hidden; blankett is a separate publish tick; Python needs **Redigera och exekvera Python-kod**; ThankYou Python plugin may need app-pool recycle (builder `logic.md`); test mail often hits a generic mailbox ([faq.md](faq.md)); do not delete a production e-tjänst until cases/köer/bokningar are gone ([admin.md](admin.md)).

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

## Källa: `references/message-tokens.md`

# Tokens in meddelandemallar

Source: *Värden i meddelandemallar* (pageId `60096729`) plus builder messages notes. Read 2026-08-25.

Always `$name$` (case-sensitive). Field answers: Razor `@this.Model["AVB.2"]` (FriendlyFieldId). Razor **does not** work in **scheduled reminder** mallar or in SMS.

If you write a field id with a raw `@` in the answer and skip `@Model[]`, PDF generation can fail.

Builder coupling (when/to/attachments): `build-abou-etjanst-web/references/messages.md`. Object model: [technical/htmlcasemodel.md](technical/htmlcasemodel.md).

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

## Källa: `references/technical/INDEX.md`

# Technical documentation

Hub: *Teknisk Information & Dokumentation*. Read 2026-08-25.

| Need | File |
| --- | --- |
| REST methods to update/fetch cases | [rest-api.md](rest-api.md) |
| `self.Citizen`, Citizen vs CitizenInfo, Navet/KIR mapping | [citizeninfo.md](citizeninfo.md) |
| `@Model` Razor in dokumentmall, e-post, ThankYouAdvanced | [htmlcasemodel.md](htmlcasemodel.md) |
| GDPR, eIDAS, TLS, browsers, WCAG, pentest, hosting | [compliance.md](compliance.md) |

**Testpersoner i Abou:** official Sokigo test identities (including sekretess / avliden). Use that Confluence page for numbers — do not copy personnummer into git.

**Ansvarsfördelning vid drift On Prem** and **Teknisk kravspecifikation - Abou Intern Hosting** are PDFs on Confluence; not transcribed here.

**Abou REST API** is a PDF (*Abou REST API version 2.5.2*, 56 pages). Method names: [rest-api.md](rest-api.md). Request/response schemas were not transcribed (too large). Ask Sokigo support for the PDF / test endpoints — do not tell the user to log into the wiki.


---

## Källa: `references/technical/rest-api.md`

# Abou REST API

Source: Confluence *Abou REST API* (PDF **version 2.5.2**). Read 2026-08-25. Contact for test endpoints: Sokigo support.

Auth in the PDF: token (`Authenticate`), API key, Bearer examples (.NET). **Do not invent URLs or payloads** — copy from the PDF.

## Methods (from PDF TOC)

### Auth
- Hämta token / Authenticate
- API-nyckel
- Bearer token

### Update case
| Method | Purpose |
| --- | --- |
| `UpdateStatus` | Status |
| `UpdateDiaryNumber` | Diarienummer |
| `UpdateAdministrator` | Handläggare |
| `AddCitizens` | Medsökande / invånare on the case |
| `FileUpload` | Attach files |
| `CreateCase` | New case |
| `NewDirectMessage` | Direktmeddelande |
| `UpdateFieldAnswers` | Fältsvar on an existing case |

### Read
| Method | Purpose |
| --- | --- |
| `GetByDateAndState` | Case numbers in date range + status |
| `GetByDate` | Date range |
| `GetByState` | One or more statuses |
| `GetByDateTimeAndState` | Status-change window (with clock) + status |
| `GetDetailed` | One detailed case (including attachments/content) |
| `GetCaseListFromUserIdentity` | Case numbers for a personnummer |
| `CasePdfDownload` | Case PDF |
| `DecisionPdfDownload` | Decision PDF |
| `AttachmentDownload` | One attachment |

### Komplettering
| Method | Purpose |
| --- | --- |
| `RequestSupplementExistingCase` | Supplement on a case that exists in Abou |
| `RequestSupplementNewCase` | Supplement when the case is not in Abou |
| `CancelSupplement` | Drop one pending supplement |
| `CancelAllSupplements` | Drop all pending |

### Beslut
| Method | Purpose |
| --- | --- |
| `DecisionOnExistingCase` | Decision on an existing case |
| `DecisionToNewCase` | Decision when the case is not in Abou |

Plus a method to read the current API version.

## Entity names in the PDF (from TOC)

RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse.

Do not invent property lists for these.


---

## Källa: `references/technical/citizeninfo.md`

# CitizenInfo and Citizen

Source: *CitizenInfo*. Read 2026-08-25.

Person data always comes from an **external plugin** (Navet, KIR, PulsenId, TEIS, …). Builder Python: also [navet.md](../../../build-abou-etjanst-web/references/integrations/navet.md) and mallar.

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

## Källa: `references/technical/htmlcasemodel.md`

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
| `Model[friendlyId]` | Field | Lookup by FriendlyFieldId |

### Administrator

UserName, FirstName (actually **full name**), Email — empty string if unassigned / unknown.

### Citizen (template)

Id, SocialSecurityNumber (personnummer or AD identity), FirstName, LastName, Email, PhoneNumber, MobilePhoneNumber, Address, City, PostalCode, MunicipalityKey, metadata dictionary.

### Decision

Date, Comment, DecisionText (**Avslaget** or **Godkänt**), Administrator (full name, else username, else empty / API).

### Service

DisplayName, Name, ShortName, RequiresMultipleSignatures, RequiresAuthentication, RequiresSignature, ServiceNr (stable across versions).

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

Amount (provider units may differ), PayedBy (Citizen; docs note it “borde heta PaidBy”), PaymentType, TransactionId.

## Signatures (examples)

```
@Model.ApplicantSignature.SignedBy.DisplayName
@foreach (var signature in Model.SortedRecentCoApplicantSignatures){@(signature.SignedBy.DisplayName + "\n")}
```

## Enums (UPPRÄKNINGAR)

**CitizenRole:** Unknown, Citizen, Company, Organisation.

**PaymentType:** Applicant, CoApplicant.

**ProposalFilterType** (e-förslag list filters): *Inväntar publicering*, *Röstning pågår*, *Inväntar ställningstagande*, plus decided statuses *Godkänt* / *Avslaget* / *Besvarat* / *Avslutad*. URL example: `/Citizen/Proposal?status=Godkänt&status=Avslaget` (space as `%20`).

Substitution **`$token$`** list: [../message-tokens.md](../message-tokens.md).


---

## Källa: `references/technical/compliance.md`

# Compliance, hosting, browsers, eIDAS

Read 2026-08-25. High-level only.

## Protocols (pageId `60096956`)

From **2022.8**, HTTPS to external systems: **TLS 1.3** and **TLS 1.2**. TLS 1.1 / 1.0 not supported. SSL3 not enabled by default.

## Browsers (pageId `60096958`)

Latest **Edge, Firefox, Chrome, Safari**. Older versions only as long as they are not a security hole.

## GDPR (*Information om GDPR*)

Sokigo documents GDPR approach, internal systems, planned work, and customer responsibilities. Person data in Abou is plugin-backed ([citizeninfo.md](citizeninfo.md)). Do not store extra person fields in Python. Scheduled **Synkronisera personuppgifter** and soft/permanent delete are the operational tools ([../scheduling.md](../scheduling.md)).

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
