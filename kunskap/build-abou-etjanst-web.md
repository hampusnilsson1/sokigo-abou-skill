# Bygg Abou e-tjänst — kunskapsbas

All kunskap för **e-tjänstebyggaren**: sidor, fält, fältregler, validatorer, Python/JS-bibliotek, logikmallar och Integrationer (Navet, REST, betalning, AD, EDP, …).

Detta är en **sammanslagen kunskapsfil** för en AI. All kunskap från skillen `build-abou-etjanst-web` ligger här. Svara från den här filen. Hitta inte på API:er, behörigheter eller fält som inte står här. Svenska UI-namn från Abou gäller.

Källfiler (samma innehåll som under `.cursor/skills/`):

- `SKILL.md`
- `references/catalog.md`
- `references/builder-ui.md`
- `references/create-and-settings.md`
- `references/pages-and-fields.md`
- `references/field-types.md`
- `references/rules-validators.md`
- `references/logic.md`
- `references/messages.md`
- `references/logic-templates/INDEX.md`
- `references/logic-templates/libraries.md`
- `references/logic-templates/pagenode-api.md`
- `references/logic-templates/standard.md`
- `references/logic-templates/url-parameters.md`
- `references/logic-templates/payment.md`
- `references/logic-templates/custom-validation.md`
- `references/logic-templates/booking-filter.md`
- `references/logic-templates/file-upload.md`
- `references/logic-templates/navet-dropdown.md`
- `references/logic-templates/navet-table.md`
- `references/logic-templates/prefill-multisign.md`
- `references/logic-templates/prefill-case-selector.md`
- `references/logic-templates/prefill.md`
- `references/logic-templates/required-when-hidden.md`
- `references/logic-templates/hide-fields-blocks.md`
- `references/logic-templates/ad-lookup.md`
- `references/logic-templates/logging.md`
- `references/logic-templates/page-skip.md`
- `references/logic-templates/calculations.md`
- `references/logic-templates/table-field.md`
- `references/logic-templates/thankyou.md`
- `references/logic-templates/extended-citizen.md`
- `references/logic-templates/client/api.md`
- `references/logic-templates/client/empty.md`
- `references/logic-templates/client/handle-field.md`
- `references/logic-templates/client/handle-many.md`
- `references/logic-templates/client/hide-block-on-value.md`
- `references/integrations/INDEX.md`
- `references/integrations/catalog.md`
- `references/integrations/navet.md`
- `references/integrations/bolagsverket.md`
- `references/integrations/adapter-rest.md`
- `references/integrations/e-legitimation.md`
- `references/integrations/sokigo-fb.md`
- `references/integrations/geo.md`
- `references/integrations/payment.md`
- `references/integrations/sms.md`
- `references/integrations/mina-meddelanden.md`
- `references/integrations/active-directory.md`
- `references/integrations/edp-future.md`
- `references/integrations/verksamhetssystem.md`
- `references/integrations/plattformar.md`
- `references/integrations/arkiv.md`
- `references/integrations/ovrigt.md`

---

## Källa: `SKILL.md`

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


---

## Källa: `references/catalog.md`

# Documentation catalog — Att bygga e-tjänster

Hub: https://dok.sokigo.com/pages/viewpage.action?pageId=56918159  
Space: Abou. Stay on `dok.sokigo.com`. Read 2026-08-21.

Prerequisite noted on the hub: e-tjänstebyggaren must be enabled by Sokigo.

## Tree (56 live child pages)

### Ersätta uppföljningsenkäter från Direkt feedback
- Guide — skapa enkät för kvalitetsuppföljning av e-tjänst

### Fälttyper
- Ärendeinformationsfältet (tidigare Ärenden-fält)
- Ärendeväljarfält
- Attestlista med sök
- Blockeringsfält
- Dolt svarsfält
- Filuppladdningsfält
- Flervalsfält — separera text och värde för svarsalternativ
- Föråldrade fälttyper
- Integrerade fält
- Integrerat fält för att välja roll
- Integrerat kontaktfält
- Kartfält, generellt
- Lägg till rad-fält
- Navigeringsknappsfält
- Personuppgiftsfält/Adressfält
- Rullgardinslista (dropdown) med sök
- Standardfälttyper
- Svarsalternativ
- Tabellfält

### FAQ
- Blir ej Excel-fil utan txt-fil
- Lista flera adresser i Meddelanden per svarsalternativ

### Hur är e-tjänsten uppbyggd?
- Beskrivning av logikmallar i Byggaren
- E-tjänstens sidor och fält
- Exempel på när man kan använda logik i e-tjänster
- Fält: Egenskaper för ett fält (inställningar)
- Fält: Lägga till fält på en sida
- Fält: Lägga till text till ett fält
- Fältargument
- Inloggning och/eller signering
- Inställningar för en e-tjänst
- Konfigurera en e-tjänst med betalning
- Konfigurera en e-tjänst med multipelsignering
- Sidtyper
- Skapa en ny sida
- Skapa en ny sida (Egenskaper)
- Skapa ny e-tjänst
- Skapa ny e-tjänst (Egenskaper)

### Layoutbyggaren
- Fältregler och visningsvillkor
- Förhandsvisa e-tjänst
- Klientlogik
- Konfigurera validatorer
- Kortkommandon
- Pythonlogik
  - Kod på tacksidor — PythonCaseService och PythonPlugin
- Skapa block och fält på layoutsida
- Sök och navigera till fält i layoutbyggaren

### PDF-mallar
- Editerbar pdf-mall

### Videoguider
- Lista över alla videor

## Adjacent Abou pages used while building (same host)

Linked from the hub articles, not children of the hub:

- Koppla meddelandemall till e-tjänst (`60096727`) — co-signer notify
- Exempel på meddelandemallar (multipelsignering) (`60096723`)
- Värden i meddelandemallar (`60096729`)
- Meddelandemallar, Skicka meddelande, Meddelanden per svarsalternativ, statusnotifieringar

## Broken / missing from this tree

- Children-display **Validatorer** (26 articles) on the hub: linked page IDs 404. Use *Konfigurera validatorer*.
- Python/JS beyond builder mallar is “kundens eget ansvar”. See [libraries.md](logic-templates/libraries.md).
- Hub video guides were not transcribed (videos on the pages).


---

## Källa: `references/builder-ui.md`

# Layout builder UI

Source: Sokigo Abou docs, *Layoutbyggaren* (from Abou 2018.11). Read 2026-08-21.

## Blocks and fields on a layout page

The video/guide covers: create layout page; add/configure blocks; rows and columns; add/configure fields; duplicate/move fields and blocks; delete; block colour.

Default: field **rubrik above** the input. Block setting **Fältrubriker bredvid fält** puts labels beside inputs.

That setting does **not** apply (need full width) for:

- Bokningsfält
- Etikettfält
- Filuppladdningsfält
- Kartfält, generellt
- Kryssrutor with 3+ columns
- Läggtillradfält with 2+ columns
- Radioknappar with 3+ columns
- Tabellfält
- Ärendeinformationsfält
- Ärendeväljarfält

Block setting **Dölj i ärende-PDF** hides the whole block from the case PDF (default: blocks with answers are shown).

Search/navigate-to-field is a separate short guide (video).

## Preview

**Förhandsvisa e-tjänsten** in the builder opens the flow in a new tab (like **Testa e-tjänsten**). Stay on the working page, edit in the builder, **Spara**, then refresh the preview tab. Log prints on the page.

Does not re-run the whole flow: no logikhopp, no previous-page `GetNextPage` prefills, no tabellfält. Moving pages breaks the preview.

Do **not** publish from preview. Do not open Mina ärenden or other citizens’ cases.

## Shortcuts (layout pages)

| Keys | Action |
| --- | --- |
| Ctrl+C | Copy field |
| Ctrl+X | Cut field |
| Ctrl+V | Paste into a placeholder |
| Del | Delete field |
| Ctrl+S | Save (whole builder) |
| Escape | Undo last shortcut |


---

## Källa: `references/create-and-settings.md`

# Create service and settings

Source: Sokigo Abou docs under *Hur är e-tjänsten uppbyggd?* (read 2026-08-21).

## Skapa ny e-tjänst

1. Top menu **E-tjänster**
2. **Skapa ny e-tjänst**
3. Fill **Egenskaper**
4. **Skapa**

## Egenskaper (new service)

**E-tjänstenamn** — what the citizen sees, e.g. “Anmälan om sophämtning”.

**Systemnamn** — unique, only in the URL. Usually three characters, e.g. `001`, `AOS`. Allowed: `a-z`, `A-Z`, `0-9`, `_`. Not `åäö`. Cannot be changed later in a useful way (settings page: “kan ej ändras”).

**Organisation** — grouping in admin.

**Skapa e-tjänst efter mall** — copy an existing service with a new systemnamn.

**Länkad e-tjänst** — not built in Abou; only a URL.

Checkboxes when creating:

| Setting | Effect |
| --- | --- |
| **Kräva inloggning** | e-legitimation before the service. Enables Mina ärenden. Requires **integrerade personobjektsfält**. Creates a personuppgiftssida. |
| **Kräva signering** | Citizen must sign before submit. Shown in case PDF and case. **Requires inloggning** (Abou ticks inloggning automatically; cannot sign without login). Creates a signeringssida. |
| **Kräva multipelsignering** | Two or more signers (e.g. guardians). Requires inloggning **and** signering. Creates a multipelsignering page. |
| **Möjliggöra beslut** | Caseworker can send a digital decision. |

Audience: **Medborgare** / **Företag** / **Förening**. With e-legitimation and the municipality “roll” feature, the citizen picks a role at start. Python can show different pages per role.

## Inloggning och signering

- Login only: no signature, e.g. fetch person data from Navet.
- Login + signing: must log in and sign to submit.
- Can be changed later in the builder.
- Ticking signing always ticks login.

## Service settings (after create)

Same ideas plus:

- **Använd denna e-tjänst som mall** — listed first when creating from a template; does not change runtime behaviour.
- **Tillåt sökande att ändra ärendet under Min sida** / **Tillåt sökande att ångra ärendet under Min sida** — with multipelsignering (or attestering). Applicant can revert to utkast while status is **Väntar på medsökandes signatur**. Off by default. [functionality.md](../../abou-platform/references/functionality.md).
- **Tillåt invånaren att komplettera ärendet med bilaga under Mina ärenden**
- **Logga ut invånaren vid start av e-tjänst** — anonymity; case not tied to the logged-in user.
- **Begränsa åtkomst till enbart invånare i kommunen** — Sokigo must set kommunkod; needs login + Navet or KIR.
- **Dölj Spara-knapp**
- **Visa inte diarienummer på Min sida och Tacksidor** (from 2021.2)
- **Statuslista** — statuses shown in Mina ärenden
- **Alternativ signering** — e-legitimation **or** print and post
- **Köfilter** — Sokigo-developed queue rules
- **Visa hjälptexter i genererad blankett**
- **Redaktör kan uppdatera svarsalternativ** — production text edit; can break logic/integrations
- **Behörighet per svarsalternativ** — case visibility by answer
- **Ärenden osynliga för invånaren** — only new submitted cases; saved drafts still show
- **Tillåt invånaren att starta Direktmeddelanden**
- **Maximal sammanlagd storlek för ärendets bilagor i MB** — 0 = unused. Do not use with conditional file fields or skipped pages.
- Felmeddelande for that limit, else resource `Service.FileUploadField2.MaxTotalSizeOfAttachments`

## Default pages by type

If **no signing** (typ 1 and 2): InfoPage, Sammanfattningssida, Tacksida.

If **signing** (typ 3 and 5): InfoPage, **Dina uppgifter** (person fields below), Sammanfattningssida, Sign, Tacksida.

If **signing + multipelsignering** (typ 4): same as signing plus **Multipelsignatur**.

Auto fields on **Dina uppgifter**: Personnummer, Förnamn, Efternamn, Adress, Postnummer, Ort, E-post, Telefon, Mobil (optional), Kontaktfält (optional). Can rename, reorder, add, or remove.

## Multipelsignering

Docs: *Konfigurera en e-tjänst med multipelsignering*.

- After submit, status **Väntar på medsökandes signatur**. Cannot process until signed (or force as ombud / delete).
- Several multipelsigneringsfält allowed → several co-applicants.
- When all have signed: first status (usually **Inkommet**). Last signature time is “signerad”.
- Internal AD / integrated personnummer approval: use **Attestlista med sök**, not multipelsignering.
- If integrations set diarienummer used in messages: send message **När diarienummer sätts**.

Created page **Multipelsignatur**:

1. Field **Krävs flera signaturer** — Ja/Nej, obligatory
2. Field **Multipelsignering** with Personnummer, Förnamn, Efternamn, E-post

Field arguments on Multipelsignering:

- **Fält-id för att kräva signaturer** — field whose answer decides if a co-signer is required
- **Matchar svar** — e.g. `Ja`

With **fördjupad Navet-slagning**: create the child field yourself (dropdown or radio). Put `null` as the dummy answer alternative; citizens do not see the word null.

Always two signers (e.g. växelvis boende):

1. Remove **Krävs flera signaturer**
2. Remove those arguments on Multipelsignering
3. Set Multipelsignering **Obligatoriskt**

Lock name fields, keep email editable: argument **Endast epost är redigerbart** = `True`.

The multipelsigneringsfält **cannot** be configured as never required: either tick **Obligatoriskt**, or keep both “require signatures” arguments.

Notify the co-signer: [messages.md](messages.md) (*Koppla meddelandemall till e-tjänst*).

## Payment

Needs login, at least one answered field, payment page last before thank-you. Sokigo must add the service in system config (kortnamn, amount, error page usually Sammanfattning). Add a page and set sidtyp **Betalningssida**.


---

## Källa: `references/pages-and-fields.md`

# Pages and fields in the builder

Source: Sokigo Abou docs (read 2026-08-21).

## Add a page

1. **Ny sida** — settings open automatically
2. Fill **Egenskaper**
3. Drag the page to the right place

### Page properties

**Systemnamn** — for the system and for Python. Same character rules as service systemnamn. Tip: `HarSkriverJagEttSidnamn`. Citizens do not see it.

**Sidnamn** — heading in the service, admin, and PDF.

**Sidtyp** — default **Layoutsida**. See below.

**Visa på sammanfattningssidan** — uncheck so the page is omitted from summary (typical for info-only pages). User then cannot go back and change that page from summary.

**Förhandsgranska ärendesammanfattning** — on the summary page: draft PDF marked “Utkast”.

**Dölj navigeringsknappar** — hides next/back, step counter, save, cancel.

**Dölj inte tillbaka-knappen** — hide other nav but keep back.

**Sidbryt** — blankettgenerator / PDF page break after last field.

Delete page: red cross.

## Sidtyper

New pages default to **Layoutsida**. Change under the page’s **Inställningar**.

| Sidtyp | Use |
| --- | --- |
| Layoutsida | Normal pages: blocks and fields. Not summary, sign, thank-you. |
| Sammanfattningssida | Created automatically. No extra fields. Every new page is shown here unless you uncheck **Visa på sammanfattningssidan**. |
| Signeringssida | Created if the service requires e-legitimation. Add manually if that was not ticked at create. No extra fields. |
| Betalningssida | Payment; needs no fields. |
| Tacksida: ThankYou | Default thank-you. Hardcoded case number. **Huvudinnehåll** after the case number; may replace the municipality “signatur”. No extra fields. |
| Tacksida: ThankYouSimple | Empty; no hardcoded text (e.g. hide case number). |
| Tacksida: PdfLinkThankYou | Link to case summary (from 2023.11 HTML summary + PDF link). **Huvudinnehåll** at top, replaces part of “Tack för din ansökan/anmälan”. |
| Tacksida: PaymentThankYou | Payment info (from 3.48). |
| Tacksida: ThankYouAdvanced | Razor in **Huvudinnehåll** for dynamic text (case number etc.). Test thoroughly. |
| NoNavigationFieldPage.aspx | Removed in 2020.5 |
| Fältsida | Removed in 2020.5. Convert via Inställningar → Sidtyper. **Re-set validators** after convert. |

## Add a field (classic field tab)

1. Select the page
2. Tab **Fält**
3. **Nytt fält**
4. Fill properties, **Spara**

Prefer layout builder blocks when working on a Layoutsida (see builder-ui.md).

### Field properties

- **Rubrik** — citizen label. Bold via `<br/><strong>Övrigt</strong>`
- **Fälttyp** — dropdown of types (see field-types.md)
- **Svarsalternativ** — where the type needs them
- **Obligatoriskt**
- **Anpassade valideringstexter** — only when format is wrong, not when empty (system texts then). Not for köfält.
- Show answer in admin case list (per version; only new cases). **Redigera** reorders those columns.
- **Viktigt** — highlight for caseworkers
- **Antal rader** — textarea height; for radio/checkbox = number of **columns**
- **Validering** + **Validatorargument**
- **Minsta längd** / **Maxlängd**

### Field texts tab

- **Hjälptext** — i-icon
- **Text ovanför fält** — not for spacing; use **LabelField**
- **Text under fält**
- **Svarsalternativ hjälptexter** — after a choice is selected
- **Muspekartext** — keep short


---

## Källa: `references/field-types.md`

# Field types (builder names)

Source: Sokigo Abou *Fälttyper* (read 2026-08-21). Instruct with **Swedish builder names**.

## Standardfälttyper

| Builder name | Use |
| --- | --- |
| **Textfält** | Free text, one or more rows |
| **Datumfält** | Calendar date picker |
| **Filuppladdning** | One or more files — see below |
| **Etikett** | Heading with no input (e.g. locked personnummer from another system) |
| **Kryssrutor** | One or more fixed choices |
| **Rullista** | Single choice dropdown |
| **Rullista med sök** | Searchable dropdown; can add custom options |
| **Radioknappar** | Single choice |
| **Flervalslista** | Multi-select list |
| **Multipelsigneringsfält** | Extra signer (personnummer, name, email) |
| **Lägg till rad** | Repeatable rows (1–5 column variants) |
| **Personuppgiftsfält** | Person data (see person/address) |

**Svarsalternativ:** on checkboxes, radios, dropdowns — field **Detaljer → Redigera** next to Svarsalternativ → fill → **Stäng**.

**Separera text och värde:** on Flervalslista, Rullgardinslista, Kryssrutor, Radioknappar. Tick **Separera text och värde** so the citizen sees one label and integrations receive another (e.g. display `Karta`, send `Karta - DKK`).

## Multipelsigneringsfält

Cannot be “never required”:

1. **Obligatoriskt** ticked → always required
2. **Obligatoriskt** off → both arguments **Fält-id för att kräva signaturer** and **Matchar svar** must be set (situational)

**Endast epost är redigerbart** — when names/personnummer are filled by script.

## Rullista med sök (from 3.14)

Arguments:

- **Kan skapa alternativ** = `true` — citizen can add options not in the list
- **Standardtext** — placeholder instead of `--- Välj ---` (e.g. `Välj land`)

## Filuppladdningsfält

Do **not** use validator “Filuppladdning”. Use argument **Tillåtna filändelser**.

| Argument | Meaning |
| --- | --- |
| Tillåt multipla filer | True/False |
| Visa miniatyrbild | Thumbnails on summary (Sokigo must enable thumbnails in system config) |
| Maxstorlek (MB) | Per field; if multiple files, **total** size |
| Lägg till pdf i ärende-pdf | Append uploaded PDFs to case PDF |
| Kräver filtyp | Citizen picks a type; types = svarsalternativ (one type auto-applied) |
| Kräver beskrivning | Required free-text per file |
| Valfri beskrivning | Optional description |
| Tillåtna filändelser | e.g. `jpg,png,gif`. Extensions **outside** Sokigo’s approved list skip signature/MIME checks — security risk |
| Max antal sidor i pdf | Block oversize PDFs |
| Generera läskvitto vid nedladdning | Receipt when someone downloads |

Default allowed types: bmp, doc, docx, gif, jpeg, jpg, pdf, pic, pict, png, pps, ppsx, ppt, pptx, rtf, tif, tiff, xls, xlsx, odt, odp, ods, dwg. Upload checks signature, extension, and MIME together.

Python can set types dynamically and require some types when leaving the page.

Service-level max **total** attachment size is a **service setting**, not this field.

## Dolt svarsfält (from 2018.8)

Masks input as `*` in UI, case PDF, and admin details. **Stored in cleartext** in DB and reports. Do not use for passwords.

## Blockeringsfält

Stops a new case if the same person already has an **active** (not Avslutat) case on this service. Needs **Integrerat personnummerfält** on the **same page**. Argument **Meddelande att visa**; default: “Du har redan ett aktivt ärende för denna e-tjänst”.

## Personuppgiftsfält / adressfält

Most are **integrerade**. Integrated personnummer lets the citizen follow the case in Mina ärenden even without e-ID **if** that field was filled. Prefer integrated fields **with login**. Without login, anyone can change person data in Abou’s DB — not recommended.

Without e-ID (docs still list these types): Personnummer, Organisationsnummer, Postnummer, Telefon, E-post. Auto validators can be turned off with **Inaktiverad validering** = `true`. E-post argument **Förhindra inklistring**.

With e-ID / integrated personnummer — builder names like **Integrerat personnummerfält**, **Integrerat förnamnsfält**, … auto-fill from e-ID / Navet / KIR / DB.

**Integrerat kontaktfält** — how the citizen wants status updates (SMS/e-post checkboxes from installed plugins). Login only. Must sit on the **same page** as integrated email and mobile. Validates those fields from the choice. Auto-added on **Dina uppgifter**. Skip the field to force email/SMS via Standardmeddelanden, or omit status messages entirely.

**Integrerat fält för att välja roll** — Invånare / Företag / Förening. Arguments **Text för invånaralternativet** / företags- / förenings-; if only one key is set, that is the only choice.

## Lägg till rad-fält

Five types: 1–5 columns of text. **Every column needs a heading** via arguments **Rubrik för kolumn N**.

- Whole field obligatory: tick **Obligatoriskt**
- Per column: **Obligatoriskt svar i kolumn N** for **all** columns (even optional ones). Cannot combine with beroende-validators
- Column validators via **Validator för svar i kolumn N** = system name (`RegexValidator`, `SocialSecurityNumberValidator`, …). **Case sensitive**. Side-level validators (Beroende, Minst ett, Allt eller inget) go on the field as usual. Simple field-level validators **do not work** on this type
- Without column-required arguments, filling anything makes **all columns** required
- Sum a column: **Fält för summering av kolumn N** = target field id (e.g. `LTR.1`). From 3.36: **Summeringssuffix**, **Antal decimaler** (default 2)

Working column validators include: OlderOrYounger, NumberOfChoices, Regex, SocialSecurityNumber, PostCode, PhoneNumber, Integer, Email, Date. Many others do **not**.

## Tabellfält

**Python only** (mall **Tabellfältet**). Show-only or selectable rows (checkboxes/radios). Arguments **Väljartyp**, **Kolumnindex för hämtning av svar**. Not supported in förhandsvisning.

## Kartfält, generellt

Arguments: **Format på bakgrundsdata** (Tiles / WMS), **Funktion** (`None`, `SetPoint`, `SetPointAutoInitial`, `SetPolygon`, `SetPolyLine`, `SetPointAsString`, `Attefall` — Attefall needs extra Sokigo GEO service), **Url till bakgrundsdata (TilesUrl)**, **Initial zoomnivå och område** (`lat;long;zoom`), **Debug** (test only), **Tillskrivning av rättigheter**, **Kartlager** (WMS), **Inverterad Y-axel (TMS)**, **Max zoom** (default 18), **Zooma automatiskt till aktuell position**. Stored as GeoJSON except SetPointAsString. Sysadmin can share a base map config; then only **Funktion** may be needed.

## Attestlista med sök

Internal services (AD or integrated personnummer), **not** citizen guardian signing. Needs **inloggning**. Sökande signering is usual but not a technical requirement. Searchable dropdown.

Svarsalternativ syntax: `efternamn|förnamn|identitet|e-post` (all four, pipe-separated). Or `SetOptions` in Python; help text as 5th segment with `{1}` `{2}` placeholders.

Email: **Redigera meddelanden** → new message → send **När sökande har signerat (medsökande finns)** → **Till fält för invånare (E-post)** = this field’s id.

Flow, V26 **Bevilja**/**Avslå**, ombud **Hantera attest**: [functionality.md](../../abou-platform/references/functionality.md) *Attestering*. Status becomes **Inkommet** regardless of Bevilja vs Avslå.

## Ärendeinformationsfältet

Shows recent cases in this service (e.g. felanmälan). Always shows **Inskickat**. Arguments for column/expander field ids, headers, photo from a file field (gif/jpg/png, Sokigo config), **Antal ärenden att visa** (default 10), max photo size.

## Ärendeväljarfält

Pick a previous submitted case to prefill later pages. Needs e-legitimation. Put **early** (intro). Prefill Python: mall **Förifyll värden med Ärendeväljarfältet**. Arguments Datumformat, Antal ärenden att visa, Antal tecken att visa från ärendenumret.

## Navigeringsknappsfält

**Obsolete** — removed from builder in **V26**. Existing services keep working. Do not use in new services. Was: custom button text, URL, or **Avbryt e-tjänst**.

## Föråldrade fälttyper (do not use)

Barnomsorgsfält, Barnomsorgsminifält, Beställningsfält, Modersmålsfält, Brandfarlig vara, Heltalssummering, Lånelista, Bygglovsväljare, Anhörigfält, Personallistfält, Textsummering, Dynamiskt funktionsbrevlåde, **Bokningsfält (gammalt)**, **Filuppladdningsfält (gammalt)**, EGovDistanceListField, EGovTextFieldLarge, EGovIframeField.

Current **Bokningsfält** / **Köfält** still exist elsewhere; they cannot use fältregler (see rules-validators.md). Booking field arguments and Admin slot UI: [booking.md](../../abou-platform/references/booking.md). Köfält: [queues.md](../../abou-platform/references/queues.md). Register as svarsalternativ: [registers.md](../../abou-platform/references/registers.md).


---

## Källa: `references/rules-validators.md`

# Field rules, validators, and field arguments

Source: Sokigo Abou docs (read 2026-08-21).

## Prefer UI rules over Python

From version **2020.11**, **fältregler** and **visningsvillkor** can skip pages and show/hide/require fields **without** Python or JavaScript.

Do **not** combine those UI rules with Python/JS that also show/hide fields or skip pages — conflicts. Combining with Python/JS for *other* logic is fine.

**Fältregler** cannot be used on **Bokningsfält** or **Köfält**.

### Fältregler

On the field whose **answer** should drive other fields: tab **Fältregler**.

Can show/hide other fields or **blocks**, and make them obligatory.

### Visningsvillkor

On the **later page**: Inställningar → **Visningsvillkor**. Point at a field on an earlier page, pick a condition, comparison value. If true, the page is in the flow.

### Conditions (fältregler and visningsvillkor)

| Condition | Use |
| --- | --- |
| Equals, NotEqualTo | Single answer only |
| Contains, DoesNotContain | Same, but still true if other answers are selected too |
| In, NotIn | Several answers in one rule, semicolon: `Röd;Gul` |
| GreaterThan, LessThan | Single numeric (or numeric string) |
| GreaterThanOrEquals, LessThanOrEquals | Same |

## Validators (layout builder from 2018.11)

Configured on the field. Hub child-list “Validatorer” (26 pages) did **not** load (404). Use this list from *Konfigurera validatorer*:

| Validator | What it does |
| --- | --- |
| Allt eller inget | All listed fields filled, or none |
| Antal val i ett flervalsfält | Min and/or max number of choices |
| Beroende | This field required when another field has a given answer (e.g. “Annat”) |
| Datum | Date format; optional compare to today, a fixed date, or another field |
| Exakt ett svar | Exactly one of several fields filled (separate empty vs too-many texts) |
| Minst ett svar | At least one of several fields |
| Olika svar | Answers must differ |
| Samma svar | Answers must match |
| Reguljärt uttryck | Custom regex |
| Tal | Integer or decimal; optional min/max |
| Veckodagar | Date falls on given weekdays |
| Äldre än eller yngre än | Age vs personnummer or date; “äldre än” is ≥, “yngre än” is strictly < |

Also mentioned on field properties: **standardvalidering (obligatoriskt fält)** exists as a concept; tick **Obligatoriskt** on the field.

## Common fältargument (friendly names in the UI)

| Argument | Value | Effect |
| --- | --- | --- |
| Tal | True | Text field numeric only |
| Max antal tecken | Positive int | Max length |
| Dold om fältet är tomt | True | Hide when empty |
| Dold | True | Always hidden |
| Aktiverad | False | Read-only (e.g. prefilled) |
| Aktivera meddelande per svarsalternativ | True | Different email recipients per choice |
| Svar redigerbart av handläggare | True | After submit, handläggare can change this choice on the case ([functionality.md](../../abou-platform/references/functionality.md)) |
| Datumformat | e.g. `yyyy-MM-dd HH:mm` | Booking / ärendeväljare |
| Visar sluttid | True/False | Booking interval display |
| Antal ärenden att visa | Positive int | Recent cases |
| Antal tecken att visa från ärendenumret | Positive int | Truncate case number display |
| Endast epost är redigerbart | True | Multipelsignering: lock name/personnummer, keep email |

Arguments are also used to map fields for integrations.


---

## Källa: `references/logic.md`

# Python and client logic

Where to type code in the builder, and how it relates to the **libraries**.

**How the APIs work** (read this when explaining or reviewing, not only when pasting a new file): [logic-templates/libraries.md](logic-templates/libraries.md).

Sokigo supports the **mallar in the builder** plus the listed PageNode / PageLogic methods. Other Python/JS is the municipality’s own risk. Do not invent methods.

Prefer **fältregler / visningsvillkor** ([rules-validators.md](rules-validators.md)) before code.

## Where to write it

- **Logik** tab: IronPython `PageNode`. `Initialize` on enter, `BeforeGetNextPage` before leave, `GetNextPage` must return a page. Class name = IronPythonType = page systemnamn.
- **Klientlogik** tab: JavaScript `PageLogic` on **Layoutsida** only. Runs when answers on **this page** change.
- Thank-you: `Published(self)` → `PublishedResult`. Mall: [logic-templates/thankyou.md](logic-templates/thankyou.md).

Field ids: `'x.1'` = current short name + number.

Method lists: [pagenode-api.md](logic-templates/pagenode-api.md), [client/api.md](logic-templates/client/api.md). Worked examples: [INDEX.md](logic-templates/INDEX.md).

## Thank-you plugin (sysadmin)

Confluence: *Kod på tacksidor - PythonCaseService och PythonPlugin*. Needs app-pool recycle (`Python plugin loaded`).

`IPythonCaseService`: `AddRelationToCase`, `UpdateStateForCase`, `AssignAdministratorToCase`, `RegisterCase`. Normal `GetAnswer` does not work; use published-case helpers in the thank-you mall. See [libraries.md](logic-templates/libraries.md).

## Preview

**Förhandsvisa** reloads **this page only**. No logikhopp, no previous-page `GetNextPage` prefills, no tabellfält. **Visa skriptlogg** shows `Log*`.


---

## Källa: `references/messages.md`

# Messages (email / SMS) while building

Abou pages linked from *Att bygga e-tjänster*, same host. Read 2026-08-21.

## Koppla meddelandemall till e-tjänst

In the service: left menu **Redigera meddelanden**.

Every service has two optional **handläggare** mails (untick to disable):

- Skicka vid statusuppdatering (when someone else changes status)
- Skicka vid handläggartilldelning

Mallar for those: tab **Meddelandemallar**.

**Lägg till ny** on tab **Standardmeddelanden**:

- Från namn / Från adress
- Meddelandemall (preview on the right)
- **När ska meddelandet skickas?**

| When | Meaning |
| --- | --- |
| När ärendet inkommit | After **Slutför**. For funktionsbrevlåda and thank-you to applicant. **Inkommen only after any medsökande has signed.** |
| När sökande har signerat (medsökande finns) | After the applicant signed a multi-sign case — **use this for the co-signer / attest mail** |
| Vid alternativ signering | Print-and-post instead of e-leg |
| När betalning genomförts | Payment via Min sida |
| Vid komplettering | Supplement / attach / edit answers |
| Vid direktmeddelande till invånare / handläggare | Min sida module |
| Vid påminnelse | Manual reminder or scheduled reminder (needs a standard message with this when) |
| När diarienummer sätts | When diary number is set (UI or API). Use this instead of “inkommit” if the confirmation should include diary number in the PDF |
| När handläggare tilldelas | Manual assign in Admin (not auto-assign on booking) |
| Vid statusuppdatering | Status change (e.g. Godkänn). First submit is **not** a status update |
| När handläggare bifogar fil | |
| När fil lästs | First download of a file with läskvitto |

Attachments: all case files, or types (Standard, e-förslag, beslut, iCal, …). Encryption exists but **not with attachments**.

**To:**

- **Till handläggare** — only if a caseworker is assigned
- **Till funktionsbrevlåda** — one address per coupling; several couplings for several addresses. Per-choice routing: see below
- **Till invånarens e-post** — logged-in user’s service or Mina uppgifter address (they can differ)
- **Till fält för invånare (E-post)** — pick the email field. Not läggtillrad, ärendeväljare, tabell, or other multi-value fields. **Exception: Multipelsigneringsfält** — pick `ID.XX: Medsökande` so the co-signer gets mail
- **Till fält för företag (E-post)** — company/club email field
- SMS equivalents: **Till invånarens mobiltelefon**, **Till fält för invånare (SMS)** — SMS **cannot** use Multipelsigneringsfält

## Co-signer notify (multipelsignering)

1. Create malls (see examples below) under **Meddelandemallar** as **Automatiskt meddelande**.
2. On the service **Redigera meddelanden → Lägg till ny**.
3. When: **När sökande har signerat (medsökande finns)**.
4. To: **Till fält för invånare (E-post)** = the multipelsigneringsfält (`…: Medsökande`).
5. Usually attach the case PDF so the co-signer sees the application.

Same “when” is used for **Attestlista med sök**, with To = the attest field id.

**När ärendet inkommit** waits until the co-signer has signed — too late for “please sign”.

## Example malls (multipelsignering)

Paste into the editor with **Klistra in som text**. Tokens: `$serviceName$`, `$uniqueID$`, `$citizenFirstName$`.

Three standard names in the docs:

- Bekräftelse **tvingande** multi-sign, **sökande** — “eventuell medsökandes signatur krävs”
- Bekräftelse **valfri** multi-sign, **sökande** — case can already be processed
- Bekräftelse multi-sign, **medsökande** — “Du har angetts som medsökande… signera under Mina ärenden”

## Tokens in malls

Always `$name$` (case-sensitive). Field answers: Razor `@this.Model["AVB.2"]` (not in SMS / not in scheduled reminders). Skipped pages have no field value → “fält.id not defined”.

Useful: `$uniqueID$`, `$registrationNumber$`, `$serviceName$`, `$citizenFirstName$`, `$dateSubmitted$`, `$customerUrl$`. Min sida case URL pattern: `…/Citizen/MyPage2#/cases/$uniqueID$`.

Full token list (kö, bokning, betalning Razor): [message-tokens.md](../../abou-platform/references/message-tokens.md). Case object for dokumentmall / ThankYouAdvanced: [htmlcasemodel.md](../../abou-platform/references/technical/htmlcasemodel.md).

## Create malls

**Meddelandemallar** in the main menu. Needs permission **Uppdatera texter**. Usage: Automatiskt / Manuellt / Standardmall för statusnotifiering (only one in the system) / handläggare status or tilldelning. Subject can use `$serviceName$` / `$uniqueID$`. Optional case PDF; SMS max 160 characters. Separate body for invånare vs företag; Mina meddelanden has its own editor or falls back to email body.

## Meddelanden per svarsalternativ

Funktionsbrevlåda routed by a choice field (kryssrutor, radioknappar, rullgardin). **Several** such fields on one service are allowed. **One address per alternative.**

1. Create the choice field(s).
2. Fältargument **Aktivera meddelande per svarsalternativ** = `True`. Save.
3. Left menu **Redigera meddelande** → tab **Meddelande per svarsalternativ**.
4. Optional default: name, e-post, mall, and whether case files are attached — used when an alternative has no override. If there is **no** default, every alternative **must** have address + mall.
5. Per field, per alternative: recipient and optional mall; attachment tick can differ per field.
6. Save.

FAQ DB field **ServiceRequestEmail** is a different Sokigo mapping ([faq.md](../../abou-platform/references/faq.md)). Workaround for several addresses on one alternative: hidden field copied from the first.

Encryption tick on standardmeddelanden: [functionality.md](../../abou-platform/references/functionality.md) *Krypterad e-post* — **no attachments**.

## Statusnotifieringar

New **inloggning** services get an automatic status message (not on first submit). Citizen opt-in: **Integrerat kontaktfält**. Without login: add a message later to an email field.

## Manual message from a case

**Skicka meddelande** (from 2023.2 email or SMS). Needs a link to the applicant. Works while **Väntar på medsökandes signatur**. Mallar marked **Manuellt ärendemeddelande**.

## Sökande ändrar / ångrar before co-sign

Service Inställningar (off by default):

- **Tillåt sökande att ändra ärendet under Min sida**
- **Tillåt sökande att ångra ärendet under Min sida**

While status is **Väntar på medsökandes signatur**, the applicant on Min sida can revert the case to **utkast**, change answers, and submit again. [functionality.md](../../abou-platform/references/functionality.md).


---

## Källa: `references/logic-templates/INDEX.md`

# Logic libraries and mallar

This folder documents **how to use Abou’s Python and JavaScript libraries**, and includes the official builder **mallar** as examples.

- **Library (how it works):** [libraries.md](libraries.md), [pagenode-api.md](pagenode-api.md), [client/api.md](client/api.md)
- **Integrations those libraries call:** [../integrations/INDEX.md](../integrations/INDEX.md)
- **Example to adapt:** one mall in the tables below

Read the library files when explaining, reviewing, debugging, or designing — **not only** when you need a new script to paste.

**Do not load this whole folder.** Prefer fältregler/visningsvillkor before code. Prefer listed methods before inventing APIs.

In the builder: tab **Logik** or **Klientlogik**. Replace `ANGEFÄLTID` / `'x.1'` / `BLOCK1`. Python **class name = IronPythonType = page systemnamn** (malls often say `InfoPage` — rename).

## Sidlogik (Python) — `PageNode`

How to use the library: [libraries.md](libraries.md) + [pagenode-api.md](pagenode-api.md).

| Topic | File |
| --- | --- |
| All PageNode helpers | [pagenode-api.md](pagenode-api.md) |
| Empty class | [standard.md](standard.md) |
| URL query → fields (`SessionParameters`) | [url-parameters.md](url-parameters.md) |
| Payment amount / order text | [payment.md](payment.md) |
| Custom validator text + stay on page | [custom-validation.md](custom-validation.md) |
| Booking `SlotFilter` | [booking-filter.md](booking-filter.md) |
| File upload types | [file-upload.md](file-upload.md) |
| Navet children + other guardian (dropdown) | [navet-dropdown.md](navet-dropdown.md) |
| Same with tabellfält | [navet-table.md](navet-table.md) |
| Prefill from multipelsignering JSON | [prefill-multisign.md](prefill-multisign.md) |
| Prefill from ärendeväljare | [prefill-case-selector.md](prefill-case-selector.md) |
| Copy fields, läggtillrad, dynamic lists | [prefill.md](prefill.md) |
| Required field hidden by JS | [required-when-hidden.md](required-when-hidden.md) |
| Hide/disable fields and blocks (server) | [hide-fields-blocks.md](hide-fields-blocks.md) |
| Internal user from AD (`RestWrapper`) | [ad-lookup.md](ad-lookup.md) |
| System log (`LogDebug` …) | [logging.md](logging.md) (builder name **Inloggning**) |
| Skip pages (`GetPage`) | [page-skip.md](page-skip.md) |
| Sums / läggtillrad | [calculations.md](calculations.md) |
| Build tabellfält JSON | [table-field.md](table-field.md) |
| After submit (`Published`) | [thankyou.md](thankyou.md) |
| Full PersonPost JSON | [extended-citizen.md](extended-citizen.md) |

Thank-you **plugin** `IPythonCaseService`: [../logic.md](../logic.md).

## Klientlogik (JavaScript) — `PageLogic`

How to use the library: [libraries.md](libraries.md) + [client/api.md](client/api.md). Only on **Layoutsida**.

| Topic | File |
| --- | --- |
| Empty skeleton | [client/empty.md](client/empty.md) |
| One field (get/set/hide/empty, split text/value) | [client/handle-field.md](client/handle-field.md) |
| Several fields and blocks | [client/handle-many.md](client/handle-many.md) |
| Hide a block when a field matches | [client/hide-block-on-value.md](client/hide-block-on-value.md) |


---

## Källa: `references/logic-templates/libraries.md`

# Abou libraries

This folder is the **documentation of Abou’s supported libraries** (IronPython `PageNode` and extra types, JavaScript `PageLogic`). The mall files are **worked examples** of those libraries.

Read here whenever you need to **know how a method, type, or integration-backed library works** — explaining to the user, reviewing pasted code, designing a flow, debugging, or writing new logic. Do **not** open a mall only when you need a new file to paste.

Sokigo does not publish a separate SDK. **These notes plus the mallar are the library.** Methods not listed here are unsupported (“kundens eget ansvar”).

**Do not load this whole folder.** Start at this file or [INDEX.md](INDEX.md), then one API file and (if you implement) one mall.

## When to read what

| Situation | Read |
| --- | --- |
| What Python can do / which method to call | [pagenode-api.md](pagenode-api.md) |
| What client JS can do / hide-show on the same page | [client/api.md](client/api.md) |
| Navet, REST, payment, AD, EDP, … (product + how it is used) | [../integrations/INDEX.md](../integrations/INDEX.md) then one file |
| Need a working script to adapt | [INDEX.md](INDEX.md) → one mall |
| Field rules instead of code | [../rules-validators.md](../rules-validators.md) |
| Where to type code in the builder | [../logic.md](../logic.md) |

## Layering (use the lowest layer that works)

1. **Fältregler / visningsvillkor / fältargument** — no library. Prefer this for show/hide and page skip.
2. **Klientlogik (`PageLogic`)** — same Layoutsida, instant, browser only. Does not persist hide/require for the next page unless Python agrees.
3. **Sidlogik (`PageNode`)** — on enter (`Initialize`) or leave (`GetNextPage` / `BeforeGetNextPage`). Other pages, validation that stops Nästa, registers, REST, payment amount, thank-you.

Python hide and JS hide are different. A field hidden only in JS can still be **required** on the server — use [required-when-hidden.md](required-when-hidden.md).

## Core library: `PageNode` (every Logik tab)

Import: `from Abou.Calamare.Web import PageNode`. Class name **must** equal IronPythonType **and** the page **systemnamn**.

| You need | Use |
| --- | --- |
| Read/write answers, options, labels | `GetAnswer` / `SetAnswer` / `SetAnswerIfEmpty` / `SetOptions` / `SetQuestionText` |
| Split “text\|value” alternatives | `GetValueFromQuestionAlternative` / `GetAnswerFromQuestionAlternative` |
| Hide, require, disable field or block | `SetHidden` / `SetRequired` / `SetDisabled` / `SetHiddenBlock` / `SetHiddenAndClearBlock` |
| Stop the citizen on this page | `SetValidationText` **and** `return self.Page` |
| Jump to another page | `return self.GetPage('Systemnamn')` |
| Log in preview | `LogDebug` / `LogInfo` / `LogError` (+ `*Object`) |
| JSON as a field answer | `Serialize` / `Deserialize` |
| Other cases / ärendeväljare | `GetAnswerFromCase` / `GetCasesByServiceAndQuestionAnswer` / `GetDetailed` |
| After submit | `GetAnswerFromPublishedCase` / `SetAnswerToPublishedCase` / `GetPublishedCasePdf` / `Published()` |
| Logged-in person (GDPR-stripped) | `self.Citizen` |
| Fuller PersonPost in **session** | `GetCitizenInfoLookUp` — see Navet below |
| Query string `?Smak=sur` | `self.Service.SessionParameters` ([url-parameters.md](url-parameters.md)) |
| Cross-page Python state | `self.Session['key']` (serializable). Do not call Navet again on every page. |

Full method list and mall: [pagenode-api.md](pagenode-api.md).

Lifecycle: `Initialize` → citizen fills → `BeforeGetNextPage` → `GetNextPage` must return a page. Thank-you: `Published(self)` returns `PublishedResult`.

Field ids: `'x.1'` = **this** service short name + number. Other service: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)`.

## Core library: `PageLogic` (Klientlogik)

Only on **Layoutsida**. Always:

```javascript
PageLogic = function() {
    var self = this;
};
```

Runs in the browser when answers **on this page** change. Cannot see other pages, cannot call Navet/REST, cannot stop Nästa by itself.

| You need | Use |
| --- | --- |
| One field | `self.GetField(id)` then `SetAnswer` / `GetAnswer` / `SetHidden` / `EmptyField` |
| Same without instance | `self.SetAnswer(id, v)` / `GetAnswer` / `SetHidden` / `EmptyField` |
| Several fields/blocks | `EmptyFields` / `SetHiddenFields` / `SetHiddenBlocks` |
| React to a value | `field.When("equals"\|"notequals"\|"contains"\|"notcontains", value, fn)` |
| Custom compare | `self.When(fn, value, callback)` |
| Split text/value on change | `field.WhenEvent(fn, "change")` + `GetValueFromQuestionAlternative` |

Full list: [client/api.md](client/api.md). Examples: [handle-field.md](client/handle-field.md), [handle-many.md](client/handle-many.md), [hide-block-on-value.md](client/hide-block-on-value.md).

## Extra types (only with matching integration / field)

These are **not** always available. They need the field type and usually a **sysadmin-enabled** integration. Document the product in `integrations/`, use the type as shown in the mall.

| Type / factory | What it is | Integration / setup | Example |
| --- | --- | --- | --- |
| `CitizenServiceProxy`, `ProxyRequest` | Children / other guardians from Navet (`VF`, skyddad identitet) | [navet.md](../integrations/navet.md) | [navet-dropdown.md](navet-dropdown.md), [navet-table.md](navet-table.md) |
| `ICitizenServicePluginFactory` + `GetCitizenAsJson` | Full PersonPost JSON (Navet / TEST / TEIS shapes differ) | [navet.md](../integrations/navet.md) | [extended-citizen.md](extended-citizen.md) |
| `IRestWrapperServiceFactory` | Named REST config (URL, auth). Python fills `IntegrationHttpRequest.Parameters` | [adapter-rest.md](../integrations/adapter-rest.md) | [ad-lookup.md](ad-lookup.md) (`InternalWebSearch`) |
| `SlotFilter` on booking field | Filter bookable slots (admin, days, text, weekends) | Booking field on the page | [booking-filter.md](booking-filter.md) |
| `TableFieldModel` | Table JSON (headers, widths ≤ 12, rows) | Tabellfält; not in preview | [table-field.md](table-field.md) |
| `AnswersModel.Deserialize` | Läggtillrad cells `Answer1`, `Answer2`, … | [calculations.md](calculations.md) | same |
| Payment hooks on Payment.aspx | `HasPaymentInfo`, `GetPaymentOrderText`, `CalculatePaymentAmount`; read via `GetAnswerFromFieldId` | [payment.md](../integrations/payment.md) | [payment.md](payment.md) |
| `PublishedResult`, published-case helpers | After submit | Thank-you page | [thankyou.md](thankyou.md) |
| `IPythonCaseService` | `AddRelationToCase`, `UpdateStateForCase`, `AssignAdministratorToCase`, `RegisterCase` | Sysadmin plugin; [../logic.md](../logic.md) | thank-you scripts |
| EDP Future Request methods | Invoices, meters, subscriptions | [edp-future.md](../integrations/edp-future.md) | clone a working Future service — no builder mall here |
| `JavaScriptSerializer` | .NET JSON serialize/deserialize | Used inside several mallar | prefill, table, Navet |

How to use an extra type: read the **integration file** (what the product does, avtal, sysadmin) **and** the **mall** (exact imports and calls). Do not invent method names from the integration marketing page.

## GDPR and person data

- `self.Citizen` on a logged-in service is **stripped** (e.g. civilstånd, födelse, raw CitizenData often empty). Mapping table: [citizeninfo.md](../../../abou-platform/references/technical/citizeninfo.md).
- Session lookup: `GetCitizenInfoLookup` / `GetCitizenInfoLookUp` — not stored in DB.
- Relations (barn, other VF): `CitizenServiceProxy` mallar — those people are **not** stored unless you write them into fields.
- Skyddad folkbokföring / sekretessmarkering: [navet.md](../integrations/navet.md). Dropdown mall drops protected children and blocks protected other guardians; table mall does **not** — add that if needed.
- Do not log real personnummer.

## Preview limits (library still runs, but not the whole flow)

**Förhandsvisa** reloads **this page only**. Logikhopp, prefills set in the previous page’s `GetNextPage`, and **tabellfält** are not testable there. **Visa skriptlogg** shows `Log*`.


---

## Källa: `references/logic-templates/pagenode-api.md`

# PageNode API — Dokumentation för hjälpmetoder

This **is** the supported IronPython library (builder mall **Dokumentation för hjälpmetoder**, UI 2026-08-21). Use it to explain and review Python, not only to copy a new class.

How it fits with client JS and integrations: [libraries.md](libraries.md). Worked examples: [INDEX.md](INDEX.md).

Field id: under Fältdetaljer. In code use `'x.1'` where `x` is the current service short name and `1` is the number. Other services: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)` → `"<shortName>.15"`.

Lifecycle: `Initialize` on page load (prefill, hide). `BeforeGetNextPage` before leave. `GetNextPage` must return a page: `PageNode.GetNextPage(self)`, `self.GetPage('Systemnamn')`, or `self.Page` to stay (validation). Thank-you uses `Published(self)` not GetAnswer.

IronPythonType **class name must match**.

## How to use the methods

- **Answers:** `GetAnswer` is one string. Checkboxes and tables need `GetAnswers`. `SetAnswerIfEmpty` lets the citizen keep a changed value.
- **Visibility:** `SetHidden` / `SetHiddenBlock` run on the **server** when the page loads or on Nästa. Same-page instant hide is [client/api.md](client/api.md). Clearing a hidden required field: [required-when-hidden.md](required-when-hidden.md).
- **Validation:** `SetValidationText` does nothing unless you `return self.Page`.
- **Options:** `SetOptions` with `"Text|Value"` when **Separera text och värde** is on. Read with `GetValueFromQuestionAlternative` vs `GetAnswerFromQuestionAlternative`.
- **Citizen:** `self.Citizen` is GDPR-stripped. Fuller PersonPost: `GetCitizenInfoLookUp` (session) or Navet types in [libraries.md](libraries.md).
- **Other cases:** `GetAnswerFromCase` requires the logged-in user to be tied to that case. After submit use `*PublishedCase*`.
- **JSON:** mall comments mention `DeserializeObject`; the hjälpmetoder **code** calls `Deserialize`. Läggtillrad uses `AnswersModel` in [calculations.md](calculations.md), not these helpers.

## Methods (from the mall)

Field id: under Fältdetaljer. In code use `'x.1'` where `x` is the current service short name and `1` is the number. Other services: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)` → `"<shortName>.15"`.

Lifecycle: `Initialize` on page load (prefill, hide). `BeforeGetNextPage` before leave. `GetNextPage` must return a page: `PageNode.GetNextPage(self)`, `self.GetPage('Systemnamn')`, or `self.Page` to stay (validation). Thank-you uses `Published(self)` not GetAnswer.

IronPythonType **class name must match**.

## Methods (from the mall)

| Method | Use |
| --- | --- |
| `GetAnswer('x.1')` | Single answer |
| `GetAnswers('x.1')` | Checkboxes, table — list |
| `GetValueFromQuestionAlternative('x.1')` | Separated **value** (radio/checkbox) |
| `GetAnswerFromQuestionAlternative('x.1')` | Separated **display text** |
| `SetAnswer('x.1', value)` | Set answer |
| `SetAnswerIfEmpty('x.1', value)` | Set only if empty; citizen change wins |
| `SetQuestionText('x.1', 'Rubrik')` | Field label |
| `GetOptions("x.1")` | Current alternatives |
| `SetOptions("x.1", Array[String]([…]))` | Alternatives; with split: `"Text\|Value"` |
| `SetOptionHelpTexts("x.1", Array[str]([…]))` | Per-alternative help |
| `SetDisabled('x.1', True/False)` | Read-only |
| `SetRequired("x.1", True/False)` | Required |
| `SetHidden("x.1", True/False)` | Hide field |
| `SetHiddenBlock("BLOCK1", True/False)` | Hide block |
| `SetHiddenAndClearBlock("BLOCK1", True/False)` | Clear + hide / show |
| `CopyTo(fromId, toId)` | Copy answer (same field kinds) |
| `LogDebug` / `LogInfo` / `LogError` | String → preview **Visa skriptlogg** |
| `LogDebugObject` / `LogInfoObject` / `LogErrorObject` | Object |
| `GetAgeOnDate(pnr, "2026-03-03")` | Age from personnummer + date strings |
| `SetValidationText("x.1", "…")` | Then **`return self.Page`** or the user is not stopped |
| `Serialize(obj)` | Object → JSON string (store as answer) |
| `Deserialize(json)` | JSON → dict/list (mall comment says DeserializeObject; **code uses Deserialize**) |
| `GetJsonDeserializedObjectSibling(obj, "key")` | First nested value for key |
| `GetCasesByServiceAndQuestionAnswer(shortName, Dictionary, whiteList, blackList)` | Case numbers matching field answers/status |
| `GetDetailed(caseId)` | Full case (dates, answers, parties, queue, …) |
| `GetAnswerFromCase(caseId, friendlyId)` | Other case; **logged-in user must be tied to that case** |
| `GetAnswerFromPublishedCase(caseId, friendlyId)` | Submitted case; on thank-you: `self.Service.UniqueCaseId` |
| `GetPublishedCasePdf(customerId, uniqueId, writeToDisk)` | Thank-you: PDF `Name` + `Data` bytes |
| `GetCitizenInfoLookUp(pnr)` | Session Navet lookup; bypasses GDPR-stripped `self.Citizen` fields (not saved to DB) |
| `self.Session['key']` | HttpSession; any serializable value |
| `self.Citizen` | Logged-in person. GDPR: MaritalStatusCode, BirthPlace.*, CitizenData **not** populated unless LookUp |
| `self.Service` | Id, DisplayName, ShortName, Nr, ServiceVersion, UniqueCaseId, RequiresAuthentication/Signature, IsAnonymous, HasAlternativeSigning, IsQueueService, RequiresPayment, CustomerId, Properties, ServiceParameters. URL mall also: **SessionParameters** dict |
| `self.Page` | PageId, DisplayName, PageName, PageIndex, HTML, ClientLogic, HiddenBlocks, ShowInSummary, Layout, ActivationRule, GetBlocksInPage() |
| `self.Service.GetField(id)` | Field object (TypeOfField, Arguments, …) |

Citizen LookUp keys in the mall: ProtectedIdentity, ProtectedIdentityCivilRegister, FirstName, LastName, Adress, Postcode, City, Email, phones, alt address, WantEmailContact, MunicipalityKey, CitizenCaseRelations, …

## Full mall

```python
from Abou.Calamare.Web import PageNode
from System import *
from System.Collections.Generic import *

class InfoPage(PageNode):

	# I den här mallen hittar du korta beskrivningar av våra Pagenode-metoder, tillsammans med exempel.
	
	## FältId ##
	# Varje fält i en e-tjänst har ett unikt id som syns under Fältdetaljer på varje fält.
	# För att nå ett fält från kod, skriv 'x.id', där id är siffran i fält-id:t
	# Exempelvis 'x.1'
	
	## Initialize
	# Initialize körs när sidan laddas och kan användas för att förifylla fält och styra vilka block och fält som ska visas.
	def Initialize(self):
		## GetAnswer ##
		# Hämta svaret från ett fält.
		svar = self.GetAnswer('x.1')
		
		## GetAnswers ##
		# Används för ex. kryssrutor och tabellfält
		# Hämta svar som en lista
		svar = self.GetAnswers('x.1')
		
		## GetValueFromQuestionAlternative ##
		# Används för ex. radioknappar och kryssrutor
		# Få värdet i ett svarsalternativ, där "Separera text och värde" är ikryssat
		svarsvarde = self.GetValueFromQuestionAlternative('x.1')
		
		## GetAnswerFromQuestionAlternative ##
		# Används för ex. radioknappar och kryssrutor
		# Få texten i ett svarsalternativ, där "Separera text och värde" är ikryssat
		svarstext = self.GetAnswerFromQuestionAlternative('x.1')
		
		## SetAnswer ##
		# Sätter svaret i ett fält. Ange först fältet, och sedan det svar du vill sätta.
		self.SetAnswer('x.1', 'Svar')
		
		## SetAnswerIfEmpty ##
		# Sätter svaret i ett fält om det är tomt. Om det redan fanns ett svar, eller om invånaren byter svar, kommer inte den här metoden ändra svaret.
		self.SetAnswerIfEmpty('x.1', 'Svar om tomt')
		
		## SetQuestionText ##
		# Sätter rubriken på ett fält
		self.SetQuestionText('x.1','Fältrubrik')
		
		## GetOptions ##
		# Hämtar tillåtna svarsalternativ för till exempel kryssrute- och radioknappsfält
		svarsalternativ = self.GetOptions("x.1")
		
		## SetOptions ##
		# Används för ex. radioknappar och kryssrutor
		# För ett fält UTAN separerade värden:
		self.SetOptions("x.1", Array[String](["Alternativ A", "Alternativ B", "Alternativ C"]))
		# För ett fält MED separerade värden:
		self.SetOptions("x.2", Array[String]((["Alternativ A|A", "Alternativ B|B", "Alternativ C|C"])))
		# Text och värde separeras med | 
		# Första svarsalternativet har då texten "Alternativ A" och värdet "A"
		
		## SetOptionHelpTexts ##
		# Används för ex. radioknappar och kryssrutor
		# Sätter hjälptext för vardera svarsalternativ
		self.SetOptionHelpTexts("x.1", Array[str](["Hjälptext till Alternativ A", "Hjälptext till Alternativ B", "Hjälptext till Alternativ C"]))

		## SetDisabled ##
		# Sätter att ett fält ska vara inaktiverat eller inte, dvs om fältet ska gå att fylla i eller ej. Default är aktiverat
		# Sätter fältet till inaktiverat
		self.SetDisabled('x.1', True)
		# Sätter fältet till aktiverat
		self.SetDisabled('x.1', False)
		
		## SetRequired ##
		# Sätter att ett fält ska vara obligatoriskt eller inte
		# Sätter fältet till icke-obligatoriskt
		self.SetRequired("x.1", False)
		# Sätter fältet till obligatoriskt
		self.SetRequired("x.1", True)
		
		## SetHidden ##
		# Sätter att ett fält ska vara dolt eller inte.
		# Sätter fältet till dolt
		self.SetHidden("x.1", True)
		# Sätter fältet till icke dolt
		self.SetHidden("x.1", False)
		
		## SetHiddenBlock ##
		# Sätter att ett block ska vara dolt eller inte.
		# Sätter blocket till dolt
		self.SetHiddenBlock("BLOCK1", True)
		# Sätter blocket till icke dolt
		self.SetHiddenBlock("BLOCK1", False)
		
		## SetHiddenAndClearBlock ##
		# Tömmer alla fält i ett block och gömmer dem
		self.SetHiddenAndClearBlock("BLOCK1", True)
		# Visar ett block
		self.SetHiddenAndClearBlock("BLOCK1", False)
		
		## CopyTo ##
		# Kopierar svar mellan två fält. Bör vara samma sorts fält.
		kopieraTillFält = "x.1"
		kopieraFrånFält = "x.2"
		self.CopyTo(kopieraFrånFält, kopieraTillFält)
		
		## Loggmetoder ##
		## Dessa Loggar presenteras i "Visa skriptlogg" under "Förhandsvisa e-tjänst"
		self.LogDebug("Sträng")
		värde = self.GetAnswer('x.1')
		self.LogDebugObject({"Nyckel":värde})
		self.LogInfo("Sträng")
		värde = "Hej"
		self.LogInfoObject({"Nyckel":värde})
		self.LogError("Sträng")
		värde = "Hej"
		self.LogErrorObject({"Nyckel":värde})
		
		## GetAgeOnDate ##
		personnummer = self.Citizen.UserIdentity
		datum = "2026-03-03"
		self.GetAgeOnDate(personnummer, datum)
		
		## GetFriendlyFieldIdFromFieldNumber ##
		friendlyFieldId = self.GetFriendlyFieldIdFromFieldNumber(15)
		
		## SetValidationText ##
		# OBS: sätt alltid return self.Page efter valideringen, annars stoppas inte invånaren från att gå vidare
		self.SetValidationText("x.1", "Fel svar; Vänligen försök igen.")
		
		## Serialize / Deserialize / GetJsonDeserializedObjectSibling ##
		data = {
			"geometry": {
				"type": "Point",
				"coordinates": [18.0649, 59.3326]
			}
		}
		json_string = self.Serialize(data)
		deserialized = self.Deserialize(json_string)
		coordinates = deserialized["geometry"]["coordinates"]
		json_deserialized = self.Deserialize(json_string)
		coordinates = self.GetJsonDeserializedObjectSibling(json_deserialized, "coordinates")
		
		## GetCasesByServiceAndQuestionAnswer
		serviceShortName = "EX_TJANST"
		fieldsAndValues = {"EX_TJANST.3": "Ja"}
		statusWhiteList = []
		statusBlackList = ["Avslutat"]
		results = self.GetCasesByServiceAndQuestionAnswer(serviceShortName, Dictionary[str,str](fieldsAndValues), List[str](statusWhiteList), List[str](statusBlackList))
		
		## GetDetailed
		caseId = "250204-EX_TJANST-KW03"
		case = self.GetDetailed(caseId)
		
		## GetAnswerFromCase / GetAnswerFromPublishedCase / SetAnswerToPublishedCase
		otherCaseAnswer = self.GetAnswerFromCase(caseId, "x.1")
		otherCaseAnswer = self.GetAnswerFromPublishedCase(caseId, "x.1")
		otherCaseAnswer = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId, 'x.1')
		self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', "Ja")
		self.SetAnswerToPublishedCase("201021-ABC-AB12", 'x.1', "Nej")
		
		## GetCitizenInfoLookUp — kringgår GDPR-strip på self.Citizen (session only)
		citizen = self.GetCitizenInfoLookUp(self.Citizen.UserIdentity)
		
		## Service / Page / BLOCK / Field / Session — see mall comments in builder
		self.Session['MyKey'] = "Mitt värde"
		MyValue = self.Session['MyKey']
 
	def BeforeGetNextPage(self):
		pass
		
	def GetNextPage(self):
		return PageNode.GetNextPage(self)
		# return self.GetPage('Sida2')
		# return self.Page
```

Citizen LookUp, Service, Page, Block, and Field property dumps are in the builder mall verbatim; copy from the UI if you need a property not listed above. Do not log real personnummer in production.


---

## Källa: `references/logic-templates/standard.md`

# Standard

Tab: **Logik**. Empty Python skeleton.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        answer = self.GetAnswer('')

    def GetNextPage(self):
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/url-parameters.md`

# Använda url-parametrar

Tab: **Logik**. From **2019.2**. Prefill from query string, stored in `self.Service.SessionParameters` (string dict). Product page: [functionality.md](../../../abou-platform/references/functionality.md) *Värden som parametrar*.

Example URL: `Siteurl/Etjänstenamn?Smak=sur&Frukt=citron` or `…/GRUSK?skola=Lyckoskolan&årskurs=3`. Missing keys throw — check `in` first. Dict keys are **case sensitive** (`Frukt` vs `frukt`).

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        #I det här exemplet antas det att e-tjänsten har startats med parametrar
        #Det betyder att man i anropet till e-tjänsten anget parametrar i urlen
        #I det här exemplet anropas abou med parametrarna 'Smak' och 'Frukt'
        #Urlen ser då ut såhär 'Siteurl/Etjänstenamn?Smak=sur&Frukt=citron'
        #Dessa parametrar lagras i propertyn self.Service.SessionParameters
        #self.Service.SessionParameters är en dictionary med strängar. 
        
        #Exempel på att hämta ut en parameter och förifylla ett fält
        #notera att om Smak inte skulle finnas i dictionaryn kommer detta smälla. 
        #Var noga med att kolla om nycklar finns vid implementation där parameterlistan är okänd innan man försöker hämta ut dom.
        smak = self.Service.SessionParameters['Smak']
        friendlyFieldId = 'x.1'
        self.SetAnswer(friendlyFieldId, smak)
        
        #Ett säkrare sätt att kolla om värdet finns i dictionaryn.
        #Exempel på användning
        
        #Försök hämta värdet för parametern 'Frukt'
        friendlyFieldId2 = 'x.2'
        
        if 'frukt' in self.Service.SessionParameters:
            self.SetAnswer(friendlyFieldId2, self.Service.SessionParameters['frukt'])
        else:
            self.SetAnswer(friendlyFieldId2, 'Värdet finns inte')

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/payment.md`

# Betalning (för PaymentPage.aspx)

Tab: **Logik** on the **Betalningssida**. Amount and order text. Read answers via `GetAnswerFromFieldId(fields, fieldId)`, not `GetAnswer`.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        answer = self.GetAnswer('')

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)

    #För att logiken för betalningen ska fungera som önskat ska fältsvar hämtas via den här metoden istället för den vanliga GetAnswer
    def GetAnswerFromFieldId(self,fields,fieldId):
        return filter(lambda f: f.FieldId == fieldId, fields)[0].Answer

    def HasPaymentInfo(self):
        return True
    
    #Ange ordertext här
    def GetPaymentOrderText(self):
        return 'MIN ORDERTEXT'

    #Ange ev. felsida här
    #def GetPaymentErrorPage(self):
        #return 'felsidan'

    #här beräknas summan
    def CalculatePaymentAmount(self, fields):
        #Definiera konstanter
        baseAmount = 100
        numItemsFieldId='ANGEFÄLTID'
        nameFieldId='ANGEFÄLTID'
        
        #Hämta och parsa fältsvar från fields parametern istället för vanliga GetAnswer
        numItems = int(self.GetAnswerFromFieldId(fields, numItemsFieldId))
        strName = self.GetAnswerFromFieldId(fields, nameFieldId)

        #Beräkna summan
        amount = numItems * baseAmount
        
        if(strName=='emelie'):
            amount = amount * 0.75 # 25% rabatt !!

        return amount
```


---

## Källa: `references/logic-templates/custom-validation.md`

# Egen valideringstext

Tab: **Logik**. Custom check + `SetValidationText` + `return self.Page` so the citizen cannot continue.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def GetNextPage(self):
        #Vid en del användningsfall där validatorer inte täcker upp helt kan man skapa en egen validator med hjälp av Python.
        #Men för att informera användaren om vad som gör att den kommer tillbaka till samma sida kan det vara bra att
        #visa ett valideringsmeddelande på samma sätt som en validator gör. 
        #Detta går att åstakomma med hjälp av: self.SetValidationText

        #Hämta svar från det fält man vill basera valideringen på.
        #I detta exempel antar vi ett radioknappsfält med svarsalternativ "Ja" och "Nej"
        
        fieldId = 'ANGE FÄLTID'

        answer = self.GetAnswer(fieldId)

        #Om man svarar nej i fältet får man inte gå vidare
        if(answer.Contains('Nej')):
            self.SetValidationText(fieldId, 'ANGE FELMEDDELANDE HÄR')
            return self.Page
        
        #Annars går vi vidare till nästa sida
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/booking-filter.md`

# Filtrera bokningsbara tillfällen

Tab: **Logik**. `SlotFilter` on a booking field. Filters stack (AND).

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Contracts.Reservation import SlotFilter

class InfoPage(PageNode):
    def Initialize(self):
        reservationField = self.Service.GetField('Ange Fält-id för bokningsfältet')
        slotFilter = SlotFilter() # Skapa SlotFilter-objekt för alla inställningar som önskas.
        reservationField.SetSlotFilter(slotFilter) # ställ in fältet att använda inställningsobjektet
        
        # Alla inställningar läggs ihop för att utöka filtreringen. Tillfällen som inte matchar angivna filter förkastas.
        # Om inget anges sker ingen filtrering på den inställningen.
        
        # Visa bokningstillfällen som ägs av handläggare med angivna inloggningsnamn.
        slotFilter.Admins = ['adminuser1', 'adminuser2']
        
        # Filtrera på Fritext. Tar bara med tillfällen som innehåller angiven sträng.
        # Följande inställning skulle exempelvis matcha 'Loppis i parken' och 'Loppis på torget'
        slotFilter.ContainsText = 'loppis'
        
        # Följande inställningar bestämmer vilka kalenderdagar från dagens datum som skall visas
        # Med följande inställning kan man aldrig boka ett tillfälle på samma dag, nästföljande dag, eller tillfällen längre fram än fem dagar
        slotFilter.DaysUntilFirst = 2 # visar inte dagens eller nästföljande dags tillfällen
        slotFilter.DaysUntilLast = 5  # visar bara tillfällen fem dagar framåt
        
        # ExcludeWeekend = True gör att lördagar och söndagar inte räknas med vid beräkning av DaysUntilFirst och DaysUntilLast.
        # Varje vardag kommer då att räknas som en sammanhängande serie.
        # Om vi bara har bokningstillfällen på vardagar och har DaysUntilFirst = 2
        # vore det exempelvis inte möjligt att boka ett måndagstillfälle på föregående fredag
        slotFilter.ExcludeWeekend = True # Grundinställning är False
        
        # ExcludeDays kan ses som en utökning av ExcludeWeekend.
        # Här kan man skriva in en lista med datum som ska fungera som helger. Anges i formatet yyyy-MM-dd
        slotFilter.ExcludeDays = ['2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26', '2020-12-31', '2021-01-01']
        
        # En enklare inställning som säkerställer att bokning inte kan göras senare än x antal timmar innan tillfället
        slotFilter.MinimumHoursBeforeTime = 2
        

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/file-upload.md`

# Filuppladdningsfältet

Tab: **Logik**. Needs file field with **AllowMultiple** and **Kräver filtyp**, **Separera text och värde**, empty svarsalternativ (types set in Python). `HasUploadedTypes` checks the **value** after `|`.

```python
### Denna mall fungerar med följande.
# 1. Ett filuppladdningsfält
# 2. AllowMultiple och RequireFileType satt till true
# 3. Inga alternativ under Svarsalternativ, samt true under Separera text och värde
from System import Array
from Abou.Calamare.Web import PageNode

fileUploadFieldId = "x.2"

# Filtyper använder sig av samma gränssnitt som kryssrutefältet
# I det här exemplet kör vi med Separera text och värde, detta görs med tecknet '|'
requiredTypes = ["Nåt vi vet att vi behöver|vi-behover", "Nåt mer vi redan känner till|nat-mer"]

# Obligatoriska filtyper kollas med värdedelen av alternativen, dvs det efter '|'-tecknet
requiredTypeValues =    ["vi-behover"               , "nat-mer"]
requiredTypeDisplayed = ["Nåt vi vet att vi behöver", "Nåt mer vi redan känner till"]
# Om vi inte har separerade värden räcker det att bara jobba med visningsvärdena.

class InfoPage(PageNode):
    # När vi anländer till sidan kan vi dynamiskt ange filtyper för filuppladdningsfältet
    def Initialize(self):
        # Sätt fältrubrik, för att indikera obligatoriska element
        self.SetQuestionText(fileUploadFieldId, "Ladda up bilagor, (obligatoriska typer: " + ", ".join(requiredTypeDisplayed) + ")")
        
        # Vi hämtar alternativ som kan bero på andra system eller logik under e-tjänstekörningen
        integrationTypes = self.GetIntegrationTypes()
        
        ## Vi lägger ihop listorna och sorterar för användarvänligheten
        allTypes = sorted(integrationTypes + requiredTypes)
    
        # Och nu blir alternativen tillgängliga för fältet.
        self.SetOptions(fileUploadFieldId, Array[str](allTypes))

    # Vid navigering till nästa sida kan vi lägga till validering som 
    # verifierar att alla obligatoriska filtyper har blivit uppladdade
    def GetNextPage(self):
        fileUploadField = self.Service.GetField(fileUploadFieldId)
        if (not fileUploadField.HasUploadedTypes(Array[str](requiredTypeValues))):
            self.SetValidationText(fileUploadFieldId, "Det saknas filtyper. Du måste skicka med " + (", ".join(requiredTypeDisplayed)))
            return self.Page
        
        return PageNode.GetNextPage(self)
    
    def GetIntegrationTypes(self):
        integrationTypeSessionKey = "typesFromMyIntegration-" + self.Service.UniqueCaseId
        if (self.Session[integrationTypeSessionKey] == None):
            # Om alternativen ex. behöver hämtas från ett externt api kan det
            # vara bra att spara listan i sessionen istället för skicka nya anrop när vi besöker sidan på nytt.
            self.Session[integrationTypeSessionKey] = ["Bild på registreringsplåt|bild-registreringsplåt", "Bild på stötfångare|bild-stötfångare"]
        return self.Session[integrationTypeSessionKey]
```


---

## Källa: `references/logic-templates/navet-dropdown.md`

# Fördjupad Navet-slagning med enkel lista

Tab: **Logik**. Children in a dropdown (`FetchMyChildren` / `FetchMyChildrenFlatList`), other guardian into multipelsigneringsfält. Relation `VF`. Children/guardians with protected identity are dropped or blocked. JSON for multi-sign: `SocialSecurityNumber`, `FirstName`, `LastName`, `Email`.

Also see [integrations/navet.md](../integrations/navet.md).

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.Integration import CitizenServiceProxy, ProxyRequest
from System.Web.Script.Serialization import JavaScriptSerializer
from System import Array, String

class InfoPage(PageNode):

	# Rullgardingslista
	dropDownFieldId = 'ANGEFÄLTID'
	# Multipelsigneringsfält
	multipleSignatureFieldId = 'ANGEFÄLTID'
	# Radioknapp - krävs flera signaturer?
	radiobuttonFieldId = 'ANGEFÄLTID'

	def Initialize(self):
		# barn innehåller mer information om varje barn, medan barnFlatList innehåller namn och personnummer
		# Barn med skyddad identitet följer inte med
		barn, barnFlatList = self.HamtaBarnFranNavet()

		if barnFlatList:
			self.SetOptions(self.dropDownFieldId, barnFlatList)
		else:
			self.SetOptions(self.dropDownFieldId, Array[String](""))
			self.SetValidationText(self.dropDownFieldId, 'Du är inte vårdnadshavare för något barn.')

	def GetNextPage(self):	
		ssp = CitizenServiceProxy()
		# Hämta ut valt barn ur rullgardingslistan
		valtBarn = ssp.GetIdentityFromFlatListAnswer(self.GetAnswer(self.dropDownFieldId))


		andraVardnadshavare = self.HamtaAndraVardnadshavareFranNavet(valtBarn)
		if andraVardnadshavare:
			if andraVardnadshavare == "Skyddad":
				# Om den andra vårdnadshavaren har skyddad identitet bör dennes uppgifter 
				# inte förifyllas i e-tjänsten. Det kan hanteras t.ex. genom att vårdnadshavaren 
				# utan skyddad identitet inte kan skicka in ärendet och får en instruktion för
				# annan hantering av ärendet.
				self.SetValidationText(self.dropDownFieldId, 'Du kan inte skicka in ett ärende i denna e-tjänst. Hör av dig till kontaktcenter för vidare hjälp med ditt ärende.')
				return self.Page
			else:
				self.SetAnswer(self.multipleSignatureFieldId, andraVardnadshavare)
				self.SetAnswer(self.radiobuttonFieldId, 'Ja')
				return self.GetPage('Multipelsignatur')
			
		# Om det inte finns en andra vårdnadshavare, gå vidare. Skriv in nedan vilken sida, annars går den direkt till nästa
		return PageNode.GetNextPage(self)

	def HamtaBarnFranNavet(self):
		# Barn med skyddad identitet följer inte med
		if(self.Citizen is not None):
			citizen = self.Citizen
			ssp = CitizenServiceProxy()
			
			# Skapa request för att hämta de barn den inloggade användaren är vårdnadshavare för
			request = ProxyRequest()
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True

			# Kontrollera om den inloggade användaren har barn
			if ssp.HasChildren(citizen.UserIdentity, request) == False:
				return None, None

			# Hämta barn från Navet
			children = ssp.FetchMyChildren(citizen.UserIdentity, request)
			children = self.TaBortBarnSkyddadIdentitet(children)
			
			# Hämta barn i kortare format från Navet
			childrenFlatList = ssp.FetchMyChildrenFlatList(citizen.UserIdentity, request)
			childrenFlatList = self.TaBortBarnSkyddadIdentitetFlatList(children, childrenFlatList)

			return children, childrenFlatList
		return None, None

	def HamtaAndraVardnadshavareFranNavet(self, valtBarn):
		ssp = CitizenServiceProxy()
		citizen = self.Citizen
		serializer = JavaScriptSerializer()
		
		# Skapa upp request för att hämta andra vårdnadshavare
		request = ProxyRequest()
		request.IdentityToRemoveInRelations = citizen.UserIdentity
		request.ParentsTypeOfRelationToChild = 'VF'
		request.RemoveDeregistratedRelation = True

		andraVardnadshavare = ssp.FetchMyParents(valtBarn, request)[0]
		if andraVardnadshavare:
			# Kontrollera ifall vårdnadshavare har skyddad identitet
			if andraVardnadshavare["ProtectedIdentity"] == "False" and andraVardnadshavare["ProtectedIdentityCivilRegister"] == "False":
				# Formattera andra vårdnadshavaren till json som kan användas till multipelsigneringsfältet
				andraVardnadshavareDict = dict(SocialSecurityNumber=andraVardnadshavare['SocialSecurityNumber'], FirstName=andraVardnadshavare['FirstName'], LastName=andraVardnadshavare['LastName'], Email='')
				andraVardnadshavarejson = serializer.Serialize(andraVardnadshavareDict)
				return andraVardnadshavarejson
			else:
				return "Skyddad"
		else:
			return None

	def TaBortBarnSkyddadIdentitet(self, children):
		# Kontrollera varje barn för att inte ta med de med skyddad identitet
		kontrolleradLista = []
		if children:
			for child in children:
				if child['ProtectedIdentityCivilRegister'] == "False" and child['ProtectedIdentity'] == "False":
					kontrolleradLista.append(child)
		return kontrolleradLista

	def TaBortBarnSkyddadIdentitetFlatList(self, children, childrenFlatList):
		# Kontrollera varje barn för att inte ta med de med skyddad identitet
		# Returnerar barnen i FlatList-format, dvs ["Förnamn efternamn, personnummer"]
		kontrolleradLista = []
		if children:
			for child in children:			
				if child['ProtectedIdentityCivilRegister'] == "False" and child['ProtectedIdentity'] == "False":
					childWithNoProtectedIdentity = [x for x in childrenFlatList if child['SocialSecurityNumber'] in x]
					childWithNoProtectedIdentity = str.format('{0} {1}, {2}', child['FirstName'], child['LastName'], child['SocialSecurityNumber'])
					kontrolleradLista.append(childWithNoProtectedIdentity)
		return Array[String](kontrolleradLista)
```


---

## Källa: `references/logic-templates/navet-table.md`

# Fördjupad Navet-slagning med tabellfältet

Tab: **Logik**. Same Navet flow using `TableFieldModel` + `SetAnswerIfEmpty`. Selected child identity = `tableAnswerModel.Answers[0]`. Does **not** filter protected identity like the dropdown mall — add that if needed.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.Integration import CitizenServiceProxy, ProxyRequest
from System.Web.Script.Serialization import JavaScriptSerializer
from Abou.Calamare.Web.UI.EGovLib.Fields import TableFieldModel
from System.Collections.Generic import List

class InfoPage(PageNode):
	
	def GetTableFieldModel(self,headers,propertyNames,propertyList,widths):
		# help method to support a dictionary with property names and values
		model = TableFieldModel()
		model.Widths = List[int](widths)
		model.Headers = List[str](headers)
		model.Rows = List[List[str]]()
		for i, val in enumerate(propertyList):
			vals = List[str]()
			for i2, valname in enumerate(propertyNames):
				if(valname in val):
					vals.Add(val[valname])
				else:
					vals.Add('')
			model.Rows.Add(vals)
		return model

	def Initialize(self):		
		if(self.Citizen is not None):
			citizen = self.Citizen
			ssp = CitizenServiceProxy()
			serializer = JavaScriptSerializer()
			
			# define the id for you table field
			tableFieldId = 'ANGEFÄLTID'
			
			# declare request to only get children logged in user is legal guardian for
			request = ProxyRequest()
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True
			children = ssp.FetchMyChildren(citizen.UserIdentity, request)
			
			# define the table here, with column widths and column headers
			model = self.GetTableFieldModel(['Förnamn','Efternamn','Personnummer','Födelseort'],['FirstName','LastName','SocialSecurityNumber','Community','SocialSecurityNumber'],children,[3,3,3,3])
			
			# serialize table
			answer = serializer.Serialize(model)
			
			# write serialized table to table field
			self.SetAnswerIfEmpty(tableFieldId,answer)
			
			# check if logged in user is legal guardian for any child, if not set validation text
			if(ssp.HasChildren(citizen.UserIdentity, request) == False):
				self.SetValidationText(tableFieldId,'Du är inte vårdnadshavare för något barn.')

	def GetNextPage(self):	
		if(self.Citizen is not None):
			citizen = self.Citizen
			serializer = JavaScriptSerializer()
			ssp = CitizenServiceProxy()
			
			# get answer, social security number for choosen child in this case, from table field
			tableFieldId = 'ANGEFÄLTID'
			tableAnswer = self.GetAnswer(tableFieldId)
			tableAnswerModel = serializer.Deserialize[TableFieldModel](tableAnswer)
			currentChildIdentity = tableAnswerModel.Answers[0]
			
			# declare request to only get other legal guardians for choosen child
			request = ProxyRequest()
			request.IdentityToRemoveInRelations = citizen.UserIdentity
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True
			
			radiobuttonFieldId = 'ANGEFÄLTID'
			multipleSignatureFieldId = 'ANGEFÄLTID'

			if(ssp.HasParent(currentChildIdentity, request)):
				# if we have an other legal guardian show page with MultipelSigneringsFältet and set field answers
				otherLegalGuardian = ssp.FetchMyParents(currentChildIdentity, request)[0]
				otherLegalGuardianDict = dict(SocialSecurityNumber=otherLegalGuardian['SocialSecurityNumber'], FirstName=otherLegalGuardian['FirstName'], LastName=otherLegalGuardian['LastName'], Email='')
				otherLegalGuardianjson = serializer.Serialize(otherLegalGuardianDict)
				self.SetAnswer(radiobuttonFieldId, 'Ja')
				self.SetAnswer(multipleSignatureFieldId, otherLegalGuardianjson)
				return self.GetPage('Multipelsignatur')
			else:
				# no other legal guardian, reset field answers in MultipelSigneringsFältet and show summary page
				otherLegalGuardianDict = dict(SocialSecurityNumber='', FirstName='', LastName='', Email='')
				otherLegalGuardianjson = serializer.Serialize(otherLegalGuardianDict)
				self.SetAnswer(radiobuttonFieldId, 'Nej')
				self.SetAnswer(multipleSignatureFieldId, otherLegalGuardianjson)
				return self.GetPage('SummaryPage')
		
		return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/prefill-multisign.md`

# Förifyll från Multipelsigneringsfält

Tab: **Logik**. Multi-sign answer is JSON: `SocialSecurityNumber`, `FirstName`, `LastName`, `Email`.

```python
from System.Web.Script.Serialization import JavaScriptSerializer
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        # Hämtar information från multipelsigneringsfältet
        answer = self.GetAnswer('ANGE FÄLTID')
        # Skapar en Dictionary<string, object> av svaret
        data = JavaScriptSerializer().DeserializeObject(answer)
        # Kopierar personnumret (SocialSecurityNumber) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['SocialSecurityNumber'])
        # Kopierar Förnamnet (FirstName) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['FirstName'])
        # Kopierar Efternamnet (LastName) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['LastName'])
        # Kopierar Epost (Email) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['Email'])
```


---

## Källa: `references/logic-templates/prefill-case-selector.md`

# Förifyll värde med Ärendeväljarfältet

Tab: **Logik** on a page **after** the ärendeväljare. `GetAnswerFromCase` needs login and the user tied to that case.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        
        #hämta ärendenumret från Ärendeväljarfältet
        caseId = self.GetAnswer("ANGEFÄLTID")
        
        #hämta det gamla fältsvaret från ärendet
        answer = self.GetAnswerFromCase(caseId,"FältID för det fält du vill att svaret ska hämtas från")
        
        # skriv in det gamla fältsvaret i ett fält
        self.SetAnswer("ANGEFÄLTID",answer)

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/prefill.md`

# Förifyll värden

Tab: **Logik**. Copy fields, läggtillrad JSON (`Answer1`…), dynamic `SetOptions`, split `"synligt|hemligt"`.

```python
from System import Array
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):

        #Förifyllnad

        #Byta rubrik för fält
        self.SetQuestionText('ANGEFÄLTID', 'ANGE ÖNSKAD RUBRIK')
    
        #Hämta ett fältsvar
        answer = self.GetAnswer("ANGEFÄLTID")

        #Skriv in fältsvaret i ett annat fält om det är tomt
        self.SetAnswerIfEmpty("ANGEFÄLTID", answer)
 
        #Kopiera ett värde från ett fält till ett annat
        self.CopyTo('ANGE_FRÅN_FÄLTID', 'ANGE_TILL_FÄLTID')

    
        #Förifyllnad av Lägg till rad-fält
    
        personuppgifter = '[{"Answer1":"196305011234","Answer2":"Ulla","Answer3":"Andersson","Answer4":"070-1122334","Answer5":"mamma"},{"Answer1":"199010075678","Answer2":"Kalle","Answer3":"Andersson","Answer4":"070-55667788","Answer5":"barn"}]' 
        self.SetAnswer("ANGEFÄLTID",personuppgifter)
    

        #Förifyll dynamiska värden till rullgardinslista-fält
    
        #hämta ett svar med ålder valt
        alder = self.GetAnswer("ANGEFÄLTID")
        #skapa en array-variabel
        kurs= []        
    
        #skriv in värden i arrayen beroende på valet för ålder 
        if alder.Equals("20-25"):
            kurs = ["Balett","Bugg"]
    
        if alder.Equals("26-30"):
            kurs = ["Vals","Hip-hop","Tango"]
    
        if alder.Equals("31-35"):
            kurs=["Salsa","Samba"]
    
        #skriv in valet i ett rullgardinslista-fält
        self.SetOptions("ANGEFÄLTID", Array[str]((kurs)))

        #Hantera hemliga värden i flervalsfält.
        #Använd hemliga värden när det inte är önskvärt att visa det valda värdet för användaren.
        
        #Förifyll ett flervalsfält med "synligt värde|hemligt värde"
        #För användaren visas valen aaa, bbb och cccc.
        self.SetOptions("ANGEFÄLTID",Array[str](["aaa|hemligt1","bbb|hemligt2","cccc|hemligt3"]))

        #Hämta dolt värde från en flervalslista med separerade värden.
        self.GetValueFromQuestionAlternative('ANGEFÄLTID')

        #Hämta synligt värde från en flervalslista med separerade värden.
        self.GetAnswerFromQuestionAlternative('ANGEFÄLTID')


    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/required-when-hidden.md`

# Hantera obligatoriska fält som döljs i klient-logik

Tab: **Logik**. If JS hides a required field, clear required in `BeforeGetNextPage` or validation blocks navigation with no visible error.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        #Ett obligatoriskt fält där logik påverkar om det är obligatoriskt eller inte bör alltid initialt sättas som obligatoriskt:
        self.SetRequired("ANGEFÄLTID", True)

    def BeforeGetNextPage(self):
        #Om ett obligatoriskt fält döljs i klient-logik måste man ange att fältet ej ska vara obligatoriskt
        #för att undvika stoppande och osynlig validering i samband med att sidhopp sker:
        self.SetRequired("ANGEFÄLTID", False)

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/hide-fields-blocks.md`

# Hantera visning av fält och block

Tab: **Logik**. Server-side hide/disable (also after Nästa). For same-page instant hide, use klientlogik.

```python
from Abou.Calamare.Web import PageNode
# Hantera visning av fält och block
class InfoPage(PageNode):
    def Initialize(self):
        friendlyFieldId = 'x.1'
        shouldHide = True
        shouldDisable = True
        # Döljer eller visar ett fält med matchande id
        self.SetHidden(friendlyFieldId, shouldHide)

        # Sätter ett fält inaktivt så att det inte kan redigeras.
        self.SetDisabled(friendlyFieldId, shouldDisable)
        
        blockId = 'BLOCK1'
        # Döljer eller visar ett helt block med matchande ID och gör
        # SetHidden på alla fält som ingår i blocket
        self.SetHiddenBlock(blockId, shouldHide)


    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/ad-lookup.md`

# Hämta uppgifter om inloggad från AD

Tab: **Logik**. Internal node. Needs sysadmin `RestWrapperConfiguration` key **InternalWebSearch**. Class in mall is `page` — rename to the page system name.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Framework.Integration import IntegrationHttpRequest
from Abou.Calamare.Framework.Integration.RestWrapper import IRestWrapperServiceFactory
from System.Collections.Generic import Dictionary, List
from System.Web.Script.Serialization import JavaScriptSerializer

class page(PageNode):
    debugFieldId = 'x.8'
    def Initialize(self):
        #Följande konfiguration behöver finnas i Abou.Calamare.Framework.Integration.RestWrapper.RestWrapperConfiguration i sysadmin
        # "InternalWebSearch": {
        #     "IsEnabled": true,
        #     "IsCaseEventsEnabled": false,
        #     "ServiceType": "Abou.Calamare.Framework.Integration.RestWrapper.V2.RestWrapperServiceV2",
        #     "Url": "{addresstillinternalweb}/api/v1/activedirectoryuser/Search?apiapplication={apiapplication}&apikey={apikey}",
        #     "Password": lösenord,
        #     "UserName": användarnamn,
        #     "ExtendedConfigurationData": {
        #         "integrationHttpRequest.Data": "{'searchString':'{searchString}','searchProperty':'{searchProperty}','resultProperties':{resultProperties}}",
        #     }
        # }
        internalWebSearch = self.Resolve[IRestWrapperServiceFactory]().Create(self.IntegrationContext, "InternalWebSearch")

        request = IntegrationHttpRequest()
        request.Parameters = Dictionary[str,str](
            {
                "integrationHttpRequest.data.searchString":self.Citizen.UserIdentity, #värdet som ska sökas på, här satt till inloggad användares användarnamn. Obligatoriskt
                "integrationHttpRequest.data.searchProperty":"sAMAccountName", #egenskapen i AD:t som skall matcha värdet, här satt till kontonamn ett annat intressant värde kan vara distinguishedname. Obligatoriskt
                "integrationHttpRequest.data.resultProperties":"['sAMAccountName','manager','givenName','sn','mail','telephoneNumber','homePhone','mobile']", #exempel på egenskaper som skall hämtas alla värden som finns på avändaren kan hämtas, förnamn, efternamn, kontonamn och epost är default om ett tomt värde anges
            })

        #Hämta inloggad användare i AD
        try:
            result = internalWebSearch.Post(request)
            
            if (not result is None and not result.Result is None):
                properties = JavaScriptSerializer().Deserialize[Dictionary[str,List[str]]](result.Result)
                self.SetAnswer('x.1', properties['givenName'][0]) #Förnamn
                self.SetAnswer('x.2', properties['sn'][0]) #Efternamn
                self.SetAnswer('x.3', properties['sAMAccountName'][0]) #Användarnamn
                self.SetAnswer('x.4', properties['mail'][0]) #Epost
                self.SetAnswer('x.5', properties['telephoneNumber'][0]) #Telefon
                self.SetAnswer('x.6', properties['mobile'][0]) #Mobil
                self.SetAnswer('x.7', properties['manager'][0]) #Chef
        except:
            self.SetAnswer(self.debugFieldId, 'FEL vid hämtning av inloggad användare i AD')
            return
```


---

## Källa: `references/logic-templates/logging.md`

# Inloggning (loggning)

Tab: **Logik**. Builder mall name **Inloggning**; the code is **system log** examples. Preview: **Visa skriptlogg**.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):

    def Initialize(self):

        #Exempel på loggning till Systemloggen i Abou
        #Du kan logga valfri text, fältsvar, svar från integrationer med mer
        
        #Debug-loggning
        self.LogDebug('DEBUGTEXT');

        #DebugObject-loggning
        self.LogDebugObject(self);

        #Info-loggning
        self.LogInfo('INFOTEXT');

        #InfoObject-loggning
        self.LogInfoObject(self);

        #Fel-loggning
        self.LogError('FELTEXT');

        #FelObject-loggning
        self.LogErrorObject(self);
```


---

## Källa: `references/logic-templates/page-skip.md`

# Logikhopp

Tab: **Logik**. `GetNextPage` must return a page. `GetPage('Systemnamn')` jumps. Only one return path runs — uncomment/adapt a single pattern.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def GetNextPage(self):
        #exempel: logikhopp beroende på val i tjänsten 
        answer = self.GetAnswer('ANGEFÄLTID')
        if answer.Contains('Bil'):
            return self.GetPage('UppgifterBil')
        if answer.Contains('Båt'):
            return self.GetPage('UppgifterBat')
        return self.GetPage('SummaryPage')


        #exempel: logikhopp beroende på flera val i tjänsten 
        answer1 = self.GetAnswer('ANGEFÄLTID')
        answer2 = self.GetAnswer('ANGEFÄLTID')
        if answer1.Contains('Bil') and answer2.Contains('Flygplan'):
            return self.GetPage('UppgifterBil&Flyg')
        return self.GetPage('SummaryPage')

        
        #exempel: logikhopp beroende på om ett val är ifyllt eller inte
        answer = self.GetAnswer('ANGEFÄLTID')
        if not answer:
            return self.GetPage('Fastighetsbeteckning2')
        return self.GetPage('Karta')

        #exempel: logikhopp obereoende av val i e-tjänsten
        return self.GetPage('Kontaktperson')
```


---

## Källa: `references/logic-templates/calculations.md`

# Summeringar och beräkningar

Tab: **Logik**. `int.TryParse` via `GetAnswerAsInt`. Läggtillrad: `AnswersModel.Deserialize`, cells `Answer1`, `Answer2`.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.UI.EGovLib.Fields.Models import AnswersModel

class InfoPage(PageNode):

    #hämtar ett fältsvar och returnerar det konverterat till siffra, 0 returneras om det ej går att konvertera till siffra.
    def GetAnswerAsInt(self, friendlyFieldId):
        answer = self.GetAnswer(friendlyFieldId)
        result = int.TryParse(answer)
        if result[0]:
            return result[1]        
        return 0;

    def Initialize(self):

        #addera flera fältsvar som heltal och skriv in dem i fält 

        #hämta värden som heltal
        arvoden = self.GetAnswerAsInt('ANGEFÄLTID')
        socialaavgifter = self.GetAnswerAsInt('ANGEFÄLTID')
        lokalhyra = self.GetAnswerAsInt('ANGEFÄLTID')

        #summera
        summa = arvoden + socialaavgifter + lokalhyra

        #skriv in summan i ett fält
        self.SetAnswer('ANGEFÄLTID', str(summa))

        #Beräkna med läggtill radfält
        #Läggtillradfälts bryter ur celler som answer1 och answer2 = kolumn 1,2 
        
        #Hämta fältsvar från läggtill-radfält
        pubTot = self.GetAnswer("ANGEFÄLTID")
        
        #deserialisera svaret
        pubTotModels = AnswersModel.Deserialize(pubTot)
        #om det gick att deserialisera, loopa igenom raderna och multiplicera cellerna Answer1 & Answer2
        if pubTotModels is not None:
            sum = 0
            for pubTotModel in pubTotModels:
                Answer1 = int.Parse(pubTotModel.Answer1)
                Answer2 = int.Parse(pubTotModel.Answer2)         
                sum += Answer1 * Answer2                                  
            self.SetAnswer("ANGEFÄLTID",str(sum))
```


---

## Källa: `references/logic-templates/table-field.md`

# Tabellfältet

Tab: **Logik**. Serialize a dict with Widths (sum ≤ 12), Headers, Rows. Extra columns without headers stay hidden; `AnswerIndex` reads them. `SummaryType`: `SelectedRows`, `Table`, or empty = selected answers only. Preview does **not** support this field.

```python
from Abou.Calamare.Web import PageNode
from System.Web.Script.Serialization import JavaScriptSerializer

class InfoPage(PageNode):

    def Initialize(self):        
        #ange fältid för din tabell
        tableFieldId = 'ANGEFÄLTID'
        
        #definera raderna i tabellen
        rowList =   [
                        ['ABC123','Nybyggnad','2015-01-01','0'],
                        ['ABC234','Rivning','2012-05-20','1'],
                        ['ABD567','Utbyggnad','2013-03-10','2'],
                    ]
        
        #observera att kolumner som inte har motsvarande rubriker, kommer bli gömda i tabellen, men kan
        #användas för att få ut värden genom att sätta fältargumentet AnswerIndex till kolumnen.

        #definera tabellen här, med kolumnbredder och kolumnrubriker och rader.
        #summan av bredderna bör inte överskrida 12.
        table = dict(Widths=[4,5,3],Headers=['Diarienummer','Ärendemening','Inkommet'],Rows=rowList)
        
        #här är ett exempel på en tabell med styling
        #table = dict(Widths=[4,5,2,1],Headers=['Diarienummer','Ärendemening','Inkommet','id'],Rows=rowList,
        #HeaderStyle="background-color:#ffffff !important;border:1px solid #000000;color:#000000 !important",
        #RowStyle="background-color:#bbbbbb;border:1px solid #000000;",
        #TableStyle="font-family: 'Times New Roman', Georgia, Serif;font-size:18px;",
        #SummaryType="SelectedRows"
        #)
        #SummaryType styr hur tabellfältet presenteras i ärendepdf, sammanfattningssida och ärendeyv för handläggare
        #SummaryType = "SelectedRows" används för att visa valda rader
        #SummaryType = "Table" används för att visa hela tabellen
        #Lämna SummaryType tom för att endast visa valda svar

        #serialisera tabellen
        serializedTable = JavaScriptSerializer().Serialize(table)
        
        #skriv in den serialiserade tabellen till fältet
        self.SetAnswerIfEmpty(tableFieldId,serializedTable)

    def GetNextPage(self):
        #tableFieldId 'x.1'
        self.LogDebugObject(self.GetAnswers('x.1'))
        
        return PageNode.GetNextPage(self)
```


---

## Källa: `references/logic-templates/thankyou.md`

# Tacksida

Tab: **Logik** on thank-you. Hook is `Published(self)`, not `GetAnswer`. Return `PublishedResult` (`Success`, `Message`). `Success = False` mails via `CalamareErrorNotificationServiceConfiguration` and sets `Cases.FailedIntegration`.

Also: [pagenode-api.md](pagenode-api.md) thank-you methods, Confluence `IPythonCaseService` in `../logic.md`.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Contracts import PublishedResult

class InfoPage(PageNode):
    # Tacksidans python-skript anropas efter att ett ärende har skickats in
    def Published(self):
        ###
        ## PageNode innehåller en referens till ärendets ID (self.Service.UniqueCaseId)
        ## som kan användas till att slå upp eller uppdatera ärendets fältsvar
        ## Men det är möjligt att ange vilket UniqueCaseId som helst
        ## om det hör till ett inlämnat ärende.
        # self.SetAnswerToPublishedCase('101010-kortnamnet-XX00', 'x.1', 'Updated in another case')
        
        ###
        ## Hämta ett fältsvar från det publicerade ärendet.
        answer1 = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1')
        self.LogDebug("self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1') => " + answer1)
        
        ###
        ## Sätta fältsvar på ett publicerat ärende
        self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', 'Nytt värde angivet')
        self.LogDebug("self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', 'Nytt värde angivet')")
        
        answer1 = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1')
        self.LogDebug("self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1') => " + answer1)
        
        ###
        ## Hämta ärende-PDF för ett publicerat ärende (från FileStorageArea om den redan existerar annars som en ny renderad case-PDF) för att skicka ärende-PDF vidare till ett annat system
        ## Metoden GetPublishedCasePdf har parametrar CustomerId (Integer), CaseUniqueId (String) och WriteToFileStorageArea (Bool) returnerar ett objekt som består av egenskaperna Name och Data
        ## Name - String (filnamn för ärende-PDF i Abou)
        ## Data - Byte[] (ärende-PDF innehåll)
        ## Vill man även spara ärende-PDF till FileStorageArea i filsystemet (den kommer inte att ersättas om den redan existerar) anger man True som sista parameter (WriteToFileStorageArea) i anropet
        casePdf = self.GetPublishedCasePdf(self.Service.CustomerId, self.Service.UniqueCaseId, False)
        self.LogDebug(casePdf.Name)
        
        ###
        ## Returtypen är PublishedResult med medlemmarna Success och Message
        result = PublishedResult()
        
        # När Success = False skickas ett felmeddelande till epost enligt inställningar i
        # Abou.Calamare.Framework.Configurations.CalamareErrorNotificationServiceConfiguration
        # (Det samma gäller när skriptkörningen får exekveringsfel)
        # Ange True för att indikera att allt gått bra.
        # Sparas i databasen på kolumn Cases.FailedIntegration
        result.Success = True
        
        # Message kan innehålla info om hur skriptkörningen gått eller annan information
        # Sparas i databasen på kolumn Cases.PluginData
        result.Message = "Tacksidans skript körde utan fel."
        
        return result
```


---

## Källa: `references/logic-templates/extended-citizen.md`

# Utökad invånarinformation

Tab: **Logik**. Full PersonPost JSON via `ICitizenServicePluginFactory` + `GetCitizenAsJson`. Store in `self.Session['personPost']` and reuse on later pages (do not call Navet again). JSON shape differs for Navet vs Abou TEST vs TEIS.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Framework.Configurations import IConfigurationReader
from Abou.Calamare.Framework.CitizenService import ICitizenServicePluginFactory, CitizenServiceConfiguration
from System.Web.Script.Serialization import JavaScriptSerializer

class InfoPage(PageNode):
    def GetNextPage(self):
        # Exempel på hur man kan hämta en fullständig personpost för en invånare

        citizenServicePluginFactory = self.Resolve[ICitizenServicePluginFactory]()
        configReader = self.Resolve[IConfigurationReader]()
        citizenServiceConfiguration = configReader.GetConfiguration[CitizenServiceConfiguration](self.Service.CustomerId)
        citizenService = citizenServicePluginFactory.CreateCitizenServicePlugin(citizenServiceConfiguration.CitizenServicePluginType, self.Service.CustomerId)

        socialSecurityNumber = self.Citizen.UserIdentity.replace('-', '')
        citizenDataJson = citizenService.GetCitizenAsJson(socialSecurityNumber)

        # Deserialisera personposten och lagra som sessionsvariabel
        citizenData = JavaScriptSerializer().DeserializeObject(citizenDataJson)
        self.Session['personPost'] = citizenData
        # OBS: Sessionsvariabeln ska sedan användas i efterkommande sidor istället för att hämta på nytt!

        return PageNode.GetNextPage(self)

        # ------- En efterkommande sida -------

        citizenData = self.Session['personPost']
        if (not citizenData is None):
            self.LogDebug(JavaScriptSerializer().Serialize(citizenData))

            ## Invånarinformation från Navet, ex:
            #if(not citizenData['Namn'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Namn']['Fornamn']))
            #    self.SetAnswer('Field.Id', unicode(citizenData['Namn']['Efternamn']))
            #if(not citizenData['Folkbokforing'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Folkbokforing']['Fastighetsbeteckning']))
            #if (not citizenData['Adresser'] is None and not citizenData['Adresser']['Folkbokforingsadress'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Adresser']['Folkbokforingsadress']['CareOf']))
            #if (not citizenData['Civilstand'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Civilstand']['CivilstandKod']))
            #if (not citizenData['Relationer'] is None and citizenData['Relationer'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relationer'][0]['Relationstyp']))
            #if (not citizenData['Fodelse'] is None and not citizenData['Fodelse']['HemortSverige'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Fodelse']['HemortSverige']['Fodelseforsamling']))

            ## Invånarinformation från Abou TEST, ex:
            #self.SetAnswer('Field.Id', unicode(citizenData['FirstName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['LastName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['MaritalStatusCode']))
            #if (not citizenData['Address'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Address']['CareOf']))
            #if (not citizenData['Relatives'] is None and citizenData['Relatives'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relatives'][0]['TypeOfRelation']))                       
            #if (not citizenData['BirthPlace'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['BirthPlace']['Community']))

            ## Invånarinformation från TEIS, ex:
            #self.SetAnswer('Field.Id', unicode(citizenData['GivenName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['LastName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['CivilStatus']))
            #if (not citizenData['Relations'] is None and citizenData['Relations'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relations'][0]['Relationship']))
```


---

## Källa: `references/logic-templates/client/api.md`

# Klientlogik API (`PageLogic`)

This **is** the supported browser library (from builder mallar, 2026-08-21). Use it to explain and review JavaScript, not only to copy a new `PageLogic`.

How it fits with Python and fältregler: [../libraries.md](../libraries.md).

Only on **Layoutsida**. Runs when answers **on this page** change — no Nästa, no other pages, no Navet/REST.

Wrapper is always:

```javascript
PageLogic = function() {
    var self = this;
    // ...
};
```

`x.1` = current service short name + field number. Block ids like `BLOCK1`.

Hide/show in JS is **only client-side**. Pair with Python [required-when-hidden.md](../required-when-hidden.md) if the field is obligatory. Prefer **fältregler** if the rule is simple and can wait until Nästa.

## How to use

- Get a field instance when you need `When` / `WhenEvent` / split text-value: `var field = self.GetField(ffid)`.
- Batch helpers (`EmptyFields`, `SetHiddenFields`, `SetHiddenBlocks`) take **arrays**. The mall **Hantera flera** uses `ffidMoreInfo` without declaring it — declare that id first.
- `When("contains"|"notcontains", …)` is **case sensitive**. Checkboxes: `"Ja;Nej"` in **alternative order**.
- `self.When(ownFunc, value, callback)` is for a custom `(answer, compareTo) => boolean`.

## `self` (page)

| Method | Meaning |
| --- | --- |
| `GetField(ffid)` | Field instance |
| `SetAnswer(ffid, value)` | Set |
| `SetAnswerIfEmpty(ffid, value)` | Set if empty |
| `GetAnswer(ffid)` | Get |
| `SetHidden(ffid, true/false)` | Hide / show one field |
| `EmptyField(ffid)` | Clear one field |
| `EmptyFields([id, id])` | Clear several |
| `SetHiddenFields([id, id], true/false)` | Hide / show several fields |
| `SetHiddenBlock(blockId, true/false)` | One block |
| `SetHiddenBlocks([id, id], true/false)` | Several blocks |
| `When(fn, value, callback)` | Custom compare: `fn(answer, compareTo)` |

## Field instance (`var field = self.GetField(ffid)`)

| Method | Meaning |
| --- | --- |
| `SetAnswer(value)` / `SetAnswerIfEmpty(value)` | Set |
| `GetAnswer()` | Raw answer |
| `GetValueFromQuestionAlternative()` | Separated **value** |
| `GetAnswerFromQuestionAlternative()` | Separated **display text** |
| `SetHidden(true/false)` | Hide / show |
| `EmptyField()` | Clear |
| `When("equals"\|"notequals"\|"contains"\|"notcontains", value, fn)` | React to answer. Checkboxes: `"Ja;Nej"` in alternative order. contains/notcontains are **case sensitive** |
| `WhenEvent(fn, "change")` | Run on change (e.g. read split text/value) |

Mall files: [empty.md](empty.md), [handle-field.md](handle-field.md), [handle-many.md](handle-many.md), [hide-block-on-value.md](hide-block-on-value.md).


---

## Källa: `references/logic-templates/client/empty.md`

# Tom mall

Tab: **Klientlogik**. Empty skeleton.

```javascript
PageLogic = function() {
    var self = this;

    //infoga kod här

};
```


---

## Källa: `references/logic-templates/client/handle-field.md`

# Hantera fält

Tab: **Klientlogik**. Get/set/hide/empty one field, with or without a field instance. Split text/value on change.

```javascript
PageLogic = function() {
    var self = this;

    //Fältid
    var friendlyfieldid = "x.1";

    //Exempel på fält-logik med fält-instans
    //--------------------------------------

    //Hämta ett fält
    var field = self.GetField(friendlyfieldid);
    //Sätt svar
    //field.SetAnswer("test");

    //Sätt svar om fältet är tomt
    //field.SetAnswerIfEmpty("test");

    //Göm ett fält
    //field.SetHidden(true);

    //Visa ett fält som är dolt via klient-logik
    // field.SetHidden(false);

    //Töm ett fält
    //field.EmptyField();

    //Hämta fältsvar
    //var myanswer = field.GetAnswer();
    //alert(myanswer);

    // Hämta olika typer av fältsvar för kryssrutor och radioknappar med inställningen "Separera text och värde" när fältsvar ändras    
    // field.WhenEvent(function () {
    //     var myanswerFull = field.GetAnswer();
    //     var myanswerValue = field.GetValueFromQuestionAlternative();
    //     var myanswerDisplay = field.GetAnswerFromQuestionAlternative();
    //     self.SetAnswer("test.6", myanswerDisplay)
    // }, "change");

    //Exempel på fält-logik utan fält-instans
    //--------------------------------------
    //Sätt svar
    //self.SetAnswer(friendlyfieldid, "test");

    //Sätt svar om fältet är tomt
    //self.SetAnswerIfEmpty(friendlyfieldid, "test");

    //Göm ett fält
    //self.SetHidden(friendlyfieldid, true);

    //Visa ett fält som är dolt via klient-logik
    //self.SetHidden(friendlyfieldid, false);

    //Töm ett fält
    //self.EmptyField(friendlyfieldid);

    //Hämta fältsvar
    //var myanswer = self.GetAnswer(friendlyfieldid);
    //alert(myanswer);    
};
```


---

## Källa: `references/logic-templates/client/handle-many.md`

# Hantera flera fält och block samtidigt

Tab: **Klientlogik**. Batch empty/hide/show fields and blocks.

The mall as shipped uses `ffidMoreInfo` without declaring it. Declare that id (or reuse `ffidYesno`) before calling `EmptyFields` / `SetHiddenFields`.

```javascript
PageLogic = function() {
    var self = this;

    //Fältids och blockids
    var ffidYesno = "x.3";
    var ffidDropdown = "x.4";
    var block1 = "BLOCK1";
    var block2 = "BLOCK2";
    var block3 = "BLOCK3";

    //Töm flera fält samtidigt
    self.EmptyFields([ffidMoreInfo, ffidDropdown]);

    //Göm flera fält samtidigt
    self.SetHiddenFields([ffidMoreInfo, ffidDropdown], true);
    
    //Visa flera fält  som är dolda via klient-logik samtidigt
    self.SetHiddenFields([ffidMoreInfo, ffidDropdown], false);
    
    //Göm flera block samtidigt
    self.SetHiddenBlocks([block1, block2, block3], true);

    //Visa flera block som är dolda via klient-logik samtidigt
    self.SetHiddenBlocks([block1, block2, block3], false);
};
```


---

## Källa: `references/logic-templates/client/hide-block-on-value.md`

# Göm block när fält får ett visst värde

Tab: **Klientlogik**. `field.When` equals / notequals / contains / notcontains, plus custom compare.

```javascript
PageLogic = function() {
    var self = this;

    //Fältids och blockids
    var ffidYesno = "x.3";
    var bidMoreInfo = "BLOCK1";

    //Hämta ett fält med radioknappar med svarsalternativ Ja och Nej
    var field = self.GetField(ffidYesno);

    //Ange initialt värde
    field.SetAnswer("Ja");

    //När fältsvaret blir Ja, visa blocket
    field.When("equals", "Ja", function() {
        //visa ett block som är dolt via klient-logik
        self.SetHiddenBlock(bidMoreInfo, false);
    });

    //När fältsvaret blir Nej, göm blocket
    field.When("equals", "Nej", function() {
        //dölj blocket
        self.SetHiddenBlock(bidMoreInfo, true);
    });

    //För kryssrutor anges flera svar samtidigt så här (i samma ordning som svarsalternativen):
    //field.When("equals", "Ja;Nej", function(){
    //	self.SetHiddenBlock(bidMoreInfo, false);		
    //});

    //Det går även att göra detta inverterat dvs när svaret skiljer sig från det man jämför med
    //field.When("notequals", "Nej", function() {
        //visa om svaret inte är "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Det går även att kolla om fältets svar innehåller en sträng man jämför med (Obs case sensetive)
    //field.When("contains", "Nej", function() {
        //visa om svaret innehåller "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Det går även att kolla om fältets svar inte innehåller en sträng man jämför med (OBS case sensetive)
    //field.When("notcontains", "Nej", function() {
        //visa om svaret inte innehåller "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Skulle inte ovanstånde jämförelser räcka till kan man skriva en egendefinerad function som tar emot ett svar och ett värde och jämför på ett eget sätt.
    //Definera egen jämförelsefunktion
    //var ownFunc = function (answer, compareTo){
        //här skriver man egen logik, i det här exemplet så blir resultatet samma som att använda 'equals' men man kan alltså skriva vad man vill här och skicka med det till self.When
    //    return answer === compareTo;
    //};
    
    //Skicka med funktionen till self.When
    //self.When(ownFunc, value, function (){
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
};
```


---

## Källa: `references/integrations/INDEX.md`

# Integrations

Hub: [Integrationer](https://dok.sokigo.com/display/ABOU/Integrationer). Read 2026-08-21.

This folder documents **how each integration is used in an e-tjänst** (what it does, avtal/sysadmin, builder vs Python). It is not a dump of marketing pages.

Read the matching file whenever you **explain, choose, configure, or write logic against** that integration — not only when adding a new field. Most products need Sokigo **sysadmin** enablement; do not invent a plugin the site does not have.

**Do not load this whole folder.** Pick one file. Python/JS types that call these products: [../logic-templates/libraries.md](../logic-templates/libraries.md).

## How integrations are used

Typical layers (use what the site actually has):

1. **Builder only** — e.g. integrerade personfält (Navet), e-legitimation on login/sign pages, Betalningssida, GEO/FB fields. No extra library.
2. **Builder + PageNode mall** — e.g. fördjupad Navet (`CitizenServiceProxy`), AD via `RestWrapper`, payment amount on Payment.aspx, booking `SlotFilter`.
3. **Sysadmin named REST** — Adapter REST / `IRestWrapperServiceFactory`. Python names the JSON; sysadmin owns URL and secrets.
4. **Thank-you plugin** — `IPythonCaseService` after submit ([../logic.md](../logic.md)).

The Integrationer Confluence page often describes the **product**, not the Python API. **Method names live in the mallar / EDP Future method list / RestWrapper config**, not in the blurb.

## Pick one

| Need | How it is used | File |
| --- | --- | --- |
| Personuppgifter / barn / vårdnadshavare | Integrerade fält, session LookUp, or `CitizenServiceProxy` mallar | [navet.md](navet.md) |
| Företag / organisationsnummer | SSBTGU/SSBTGO; builder/plugin, not a PageNode mall in this skill | [bolagsverket.md](bolagsverket.md) |
| Valfritt REST-API from Python | `IRestWrapperServiceFactory` + named sysadmin config | [adapter-rest.md](adapter-rest.md) |
| BankID / e-leg (login, sign) | Service settings + signeringsida; not PageLogic | [e-legitimation.md](e-legitimation.md) |
| Fastighet / adress / detaljplan | Sokigo FB fields | [sokigo-fb.md](sokigo-fb.md) |
| Karta in vs GEO ut | GEO fields / publish | [geo.md](geo.md) |
| Betalning | Betalningssida + [payment mall](../logic-templates/payment.md) | [payment.md](payment.md) |
| SMS | Notices / sysadmin | [sms.md](sms.md) |
| DIGG Mina meddelanden | Sysadmin + messages | [mina-meddelanden.md](mina-meddelanden.md) |
| Intern AD-inloggning | LDAP/IdP; lookup mall [ad-lookup.md](../logic-templates/ad-lookup.md) | [active-directory.md](active-directory.md) |
| VA/avfall EDP Future | Published Python method list (clone a working service) | [edp-future.md](edp-future.md) |
| Namngivet verksamhetssystem (ByggR, Ecos, …) | Site-specific; often Adapter REST | [verksamhetssystem.md](verksamhetssystem.md) |
| Mule / TEIS | Platform in front of APIs | [plattformar.md](plattformar.md) |
| Arkiv (Formpipe LTA, AGS) | After case handling | [arkiv.md](arkiv.md) |
| Analytics | Product blurb | [ovrigt.md](ovrigt.md) |
| Full name list | Catalog only | [catalog.md](catalog.md) |


---

## Källa: `references/integrations/catalog.md`

# Integrationer — catalog

Hub: https://dok.sokigo.com/display/ABOU/Integrationer (root id 58524142). Read 2026-08-21.

Sammanställning: page `58524148`. Groups: karta, betalning, SMS, autentisering, registerslagning (Navet, SSBTGU, Sokigo FB, KIR), verksamhetssystem, motorer (TEIS, Mule), Adapter REST.

## Children crawled (45)

Adapter Rest; Artvise; Barium Live; Bolagsverket SSBTGU/SSBTGO; CGI Treserva; Dibs; DIGG Mina meddelanden; E-legitimation; Easit BPS; EDP ByggReda via Mule; EDP Future (+ Anropsmetoder); EDP Vision; Evry Ephorte; Flexeurope Flexite; Formpipe LTA; Generic SMS; Google Analytics; GotaSMS; Gränssnitt för geografisk data; Ida Infront AGS; Ida Infront iipax; Microsoft AD; Paynova P3; Prosona Castor; Pulsen Mule; Sammanställning; Seriline P-Express; Skatteverkets Navet (`58524277`); SMS Teknik; Sokigo AlkT; ByggR; Ecos; Evolution; FB; OL2; Orbit; Skolskjuts; Solarplexus Lex; Solid Park M3; Swedbank Pay; Tele2; Telenor; Tellus Talk; Tieto TEIS.

## Listed on hub/sammanställning but no child page

- KIR (Kommuninvånarregister)
- Bosbec SMS
- Esri GEOSECMA (link on hub, not in child API)
- MMP, Infracontrol Online (names on sammanställning)

## What is *not* in these pages

Full IronPython libraries (except EDP Future methods, ThankYou `IPythonCaseService`, and Navet mallar in the builder). Adapter REST has no method list.


---

## Källa: `references/integrations/navet.md`

# Skatteverkets Navet (registerslagning)

Docs: [page 58524277](https://dok.sokigo.com/pages/viewpage.action?pageId=58524277) under Integrationer. Read 2026-08-21.

This is the page for **fetching person data from personnummer**. It is **not** a Python library catalog. Sokigo does not list `CitizenServiceProxy` methods here.

## What Navet does in Abou

Two Skatteverket services:

1. **PersonPost** — lookup by personnummer. Used to prefill e-tjänster.
2. **NamnSökning** — search by name/postcode etc., max 100 hits. Needs a **separate** Skatteverket subscription.

What PersonPost actually returns is limited by the municipality’s **avtal with Skatteverket**.

## Three ways to use PersonPost in an e-tjänst

1. **Integrerade personfält** (simplest). Common properties marked `*` below are stored in Abou’s database. Login recommended.
2. **Fördjupad Navetslagning** — relations (children, other guardians). Those people are **not** stored in the DB. Builder mallar: [navet-dropdown.md](../logic-templates/navet-dropdown.md) / [navet-table.md](../logic-templates/navet-table.md).
3. **Python from the session** — any PersonPost property from the last Navet call, session-only, not stored.

## PersonPost properties (docs list)

Stored via integrated fields when marked `*`: Personnummer*, Förnamn*, Efternamn*, Utdelningsadress 2*, Postnummer*, Postort*.

Also available (session / fördjupad): PersonID, Sekretessmarkering, Skyddad folkbokföring, Avregistreringsorsak, namn/tilltalsnamn, Mellannamn, folkbokföringsdatum, län/kommun/församling, fastighetsbeteckning, Care of, Utdelningsadress 1, särskild postadress, utlandsadress, civilstånd, födelse, invandring, **Relationer** (typ, datum, vårdnad, RelationID, personnummer), medborgarskap.

NamnSökning returns a shorter person+address set including samordningsnummer and sekretessmarkering.

## Skyddade personuppgifter

- **Skyddad folkbokföring** (stronger): no street address, only särskild postadress. Integrated address fields stay **empty**. Caseworker sees the flag.
- **Sekretessmarkering** (weaker): Navet still sends data with a flag. Integrated fields **prefill as usual**. Caseworker sees the flag. Reports can hide these cases.

**Multipelsignering + fördjupad slagning:** you must adapt Python yourself — whether to prefill medsökande personnummer/name/address depends on these flags.

## How to use Navet in logic

This page is **how the integration is used**, not a SDK dump. Types and calls:

| Need | Library | Docs |
| --- | --- | --- |
| Prefill from login (stored fields) | Integrerade personfält — no Python | Builder |
| Session PersonPost (GDPR bypass on `self.Citizen`) | `GetCitizenInfoLookUp` | [pagenode-api.md](../logic-templates/pagenode-api.md) |
| Children + other vårdnadshavare (`VF`) | `CitizenServiceProxy` / `ProxyRequest` | [navet-dropdown.md](../logic-templates/navet-dropdown.md), [navet-table.md](../logic-templates/navet-table.md) |
| Full PersonPost JSON, reuse in `Session` | `ICitizenServicePluginFactory.GetCitizenAsJson` | [extended-citizen.md](../logic-templates/extended-citizen.md) |

Map of all extra types: [libraries.md](../logic-templates/libraries.md). Clone from a working service on the same site if the mall needs adapting (certificates, avtal).

## KIR

The integration **sammanställning** also lists **KIR (Kommuninvånarregister)** as a registerslagning. There is **no** child page under Integrationer for KIR. Combined Navet+KIR+KID is documented as not supported without new development (TEIS page).


---

## Källa: `references/integrations/bolagsverket.md`

# Bolagsverket — SSBTGU / SSBTGO

Docs: [Bolagsverkets bastjänster](https://dok.sokigo.com/pages/viewpage.action?pageId=58524190). Read 2026-08-21.

Prefill company data for a **logged-in** user: name, addresses, verksamhet, plus **roll i företag** (funktionär / firmatecknare).

## SSBTGU (old)

Abou plugin. Free to fetch for prefilling. Municipality connects with Bolagsverket. Bolagsverket planned shutdown **January 2026**.

## SSBTGO (new, Abou from 2025.2)

- Existing SSBTGU avtal can continue; new users sign SSBTGO.
- Send **two Client IDs** (test + prod) to Sokigo kundservice. Auth is mutual TLS + Client ID (not Client Secret).
- Sokigo configures test/prod (billable). Code change GU→GO in each e-tjänst is extra; Sokigo can drop a **mall-e-tjänst with examples** in test.

Do not write SSBTGU Python for a new service if the site is on SSBTGO. Ask which plugin is live.

Builder: company/role integrated fields + login as **Företag**. Copy Python from the mall-e-tjänst on that site, not from guesses.


---

## Källa: `references/integrations/adapter-rest.md`

# Adapter REST

Docs: [Adapter Rest](https://dok.sokigo.com/display/ABOU/Adapter+Rest). Read 2026-08-21.

Generic adapter toward **one or more REST APIs**.

- **Python in the e-tjänst** names the methods and the request/response JSON.
- The adapter handles **security** and **which endpoints** to call (sysadmin).
- You must know the target API. Examples in docs: Ängelholm → Procapita Education via Mule; Täby → BookIT.

There is **no method list** on this Confluence page. The library in Python is `IRestWrapperServiceFactory` + a **named** sysadmin config (URL, auth, `ExtendedConfigurationData`). Example of how to call it: [ad-lookup.md](../logic-templates/ad-lookup.md) (`InternalWebSearch`). How it fits: [libraries.md](../logic-templates/libraries.md).

Clone a working service on the same site, or get the API contract from the municipality. Do not put API keys in field help text or git.


---

## Källa: `references/integrations/e-legitimation.md`

# E-legitimation (authentication and signing)

Docs: [E-legitimation, flera leverantörer](https://dok.sokigo.com/pages/viewpage.action?pageId=58524202). Read 2026-08-21.

Abou supports login and signing via (docs list): CGI (Logica), Visma Sirius, Svensk e-identitet (Medborgarkonto and E-leg), Mobilt BankID.

Mobile BankID signing (as of that page): Visma Sirius, CGI, Svensk e-identitet.

Sammanställning also names federation/IdP options: CGI, Sirius, Portwise, McAfee, Svensk E-identitet, Microsoft AD, KnowIT (Cybercom/SignPort), SwedenConnect.

**Builder:** tick **Kräva inloggning** / **signering** on the service. Sokigo wires the IdP. You do not pick CGI vs Sirius in the layout builder.

See `../create-and-settings.md` for service checkboxes.


---

## Källa: `references/integrations/sokigo-fb.md`

# Sokigo FB (fastighet och befolkning)

Docs: [Sokigo FB](https://dok.sokigo.com/pages/viewpage.action?pageId=58524286). Read 2026-08-21.

From an e-tjänst, docs say you can:

- Search properties from a **personnummer**
- Autocomplete **fastighetsbeteckning** (with kommun)
- Autocomplete **adress**
- Fetch property data for one property
- Fetch detaljplaner in **Arken** and download them

No Python method names on this page. Sokigo enables the plugin. Clone a working FB e-tjänst on the site for field types and scripts.


---

## Källa: `references/integrations/geo.md`

# Maps and GEO

Read 2026-08-21.

## Inside the e-tjänst (builder)

Field type **Kartfält, generellt** — see `../field-types.md`. Sammanställning: Lantmäteriet WMS, Google Maps, Mapbox tiles URL, OpenStreetMap tiles URL.

Hub listed **Esri GEOSECMA for ArcGIS** as a registerslagning, but that page was **not** a live child of Integrationer when crawled.

## Out from Abou (from 3.52)

[Gränssnitt för geografisk data](https://dok.sokigo.com/pages/viewpage.action?pageId=58524196): publish incoming cases’ map points to another GIS (felanmälan on the municipal web, grävtillstånd for caseworkers). Sokigo configures which services/fields. The GIS must read Abou **spatial views**. Not something you finish with a field argument alone.


---

## Källa: `references/integrations/payment.md`

# Payment

Read 2026-08-21. Builder: `../create-and-settings.md` (Betalningssida). How the **library** on Payment.aspx is used (`HasPaymentInfo`, `GetPaymentOrderText`, `CalculatePaymentAmount`, `GetAnswerFromFieldId`): [payment mall](../logic-templates/payment.md), [libraries.md](../logic-templates/libraries.md).

| Provider | Status in docs |
| --- | --- |
| **Swedbank Pay** | Current. V1 (Swish/card) until 2023.11; **V3.1 from Abou 2024.1** (invoice, Apple/Google Pay, wallets). V1 being shut down. Extra Swedbank Pay avtal for new methods. Sokigo config change (no extra Abou license). |
| **Paynova P3** | Being phased out; no new customers |
| **Dibs** | Being phased out; no new customers (in Abou from 3.48) |

All need provider avtal + Sokigo config. Do not add a payment page unless that stack is live.


---

## Källa: `references/integrations/sms.md`

# SMS notification

Read 2026-08-21. Each vendor page is the same sentence: Abou can send confirmation and status SMS; **Sokigo must configure** it.

Vendors with pages: Generic, GotaSMS, SMS Teknik, Solid Park M3 (formerly Mawell), Tele2, Telenor, Tellus Talk.

Sammanställning also lists **Bosbec** (no child page in the tree).

Builder: **Integrerat kontaktfält** + standardmeddelanden (`../messages.md`). You do not pick Telenor vs Tele2 in the e-tjänst; that is the installed plugin.


---

## Källa: `references/integrations/mina-meddelanden.md`

# DIGG Mina meddelanden

Encrypted digital mailbox (Kivra, Min myndighetspost, Bring Digimail) via FAR + sealing. Sokigo installs the plugin. Do not store cert passwords in the skill or git.

## Prerequisites

- Abou **3.21+**
- **Separate** Steria server cert (not the Navet cert)
- DIGG anslutningsavtal; org.nr, support text/email/URL/phone/logo to Sokigo
- Configured in **produktion**
- Citizen has joined Mina meddelanden **and** chosen this kommun
- Message malls coupled to the e-tjänst
- Service has **inloggning or integrerat personnummerfält** (the integration looks up personnummer)
- Works for privatpersoner and företag

## What it does

If the citizen opted in, **all** Abou message sends to them go to their chosen secure mailbox operator.

- Different body for e-post vs Mina meddelanden: unique MM text if present, else the e-post body. Same fallback for företag → invånare body.
- The only attachment you can treat differently vs ordinary e-post is the **ärende-PDF**.
- Other case-file attachments follow the notifiering tick and then go to **both** e-post and MM.
- On **beslut**, case files **including the decision file** always go with the MM send.
- Does **not** replace SMS (own kortmeddelande mall).

Builder: mall editor has a Mina meddelanden body (or falls back). Coupling: `../messages.md`.


---

## Källa: `references/integrations/active-directory.md`

# Microsoft AD (internal login)

Docs: [AD för inloggning](https://dok.sokigo.com/pages/viewpage.action?pageId=58524264). Read 2026-08-21.

LDAP or IdP. Can cover external admin, internal admin, and **internal citizen node** (internal e-tjänster + Min sida).

- **Abou LDAP:** users sign with AD; signing in the internal citizen view is possible. Rights in Abou users **or** AD groups synced into Abou groups (same names). Highest of user+group wins. **Behörigheter → Grupper → Synkronisera användare** copies name/email into Abou for those group members (creates missing users; does **not** delete leavers). Synced users cannot be edited or given individual rights in Abou — [functionality.md](../../abou-platform/references/functionality.md).
- **IdP:** IdP owns login (can combine SMS 2FA). **No signing** in the citizen view. Cannot drive Abou rights from AD groups.

Builder mall: [ad-lookup.md](../logic-templates/ad-lookup.md) — `IRestWrapperServiceFactory` + sysadmin key **InternalWebSearch**. How RestWrapper is used: [adapter-rest.md](adapter-rest.md), [libraries.md](../logic-templates/libraries.md). Attestlista med sök is the internal multi-approve field (`../field-types.md`).


---

## Källa: `references/integrations/edp-future.md`

# EDP Future (VA / avfall)

Docs: [EDP Future](https://dok.sokigo.com/pages/viewpage.action?pageId=58524206) and [anropsmetoder](https://dok.sokigo.com/display/ABOU/EDP+Future-adapter+Anropsmetoder). Read 2026-08-21.

Abou ↔ EDP Webb. E-tjänster in docs: invoices, subscriptions, water meter history/reading, applications, collection schedule/history, new/change subscription, contacts, reklamation.

Python methods take a **Request** object. Only use if this adapter is on the site. This file **is** the method documentation (Sokigo publishes this list). There is no builder mall — clone a working Future e-tjänst for the exact Python types. How it fits: [libraries.md](../logic-templates/libraries.md).

| Method | Request fields |
| --- | --- |
| GetCustomersByIdentity | UserIdentity |
| GetCustomerContacts | CustomerId |
| GetKundAterbetalningskontoTypList | (none) |
| GetApplicationsByCustomers | CustomerIDs |
| GetApplicationById | ApplicationId |
| GetVAServicesByBuilding | BuildingId, EServiceType |
| GetVAServiceEventsByService | ServiceId, CustomerId |
| GetBuildingsByCustomerIDs | CustomerIDs, EServiceType |
| GetAllServicesByBuildingID | BuildingId (active RH/VA/other) |
| CheckMeterReadingReliability | (meter reading check) |
| GetServicesByBuildingIdForOrder | BuildingId |
| CalculateOrderCost | OrderType (serialized), BuildingId, CustomerId, ServiceId, IncVat (from 2022.11 V2) |
| CalculateOrderRows | same |

Request properties listed: UserIdentity, CustomerId, CustomerIDs[], ApplicationId, BuildingId, ServiceId, MeterId, ReadingValue, ReadingDate, Comment, EServiceType, Parameters, OrderType, EmptyPerYear, Choice, IncVat, BinNumber, FeeCode, FeeChangeDate.

Clone a working Future e-tjänst for the exact Python types.


---

## Källa: `references/integrations/verksamhetssystem.md`

# Named verksamhetssystem

Read 2026-08-21 from Integrationer children. These are **Sokigo-built adapters**, usually “when the e-tjänst completes, send the case”. You do not implement the SOAP/XML yourself. Confirm the plugin is on the site; then copy a working service or ask Sokigo for field mapping.

| Integration | Docs gist |
| --- | --- |
| Artvise Kundtjänst | Direct; Täby felanmälan on complete |
| Barium Live | Starts a Barium process (Lomma felanmälan) |
| CGI Treserva | Ekonomiskt bistånd: fetch stadsdelar/orsaker; send case+PDF |
| Easit BPS | XML files on disk (Lidingö) |
| EDP ByggReda via Mule | Case Abou → Mule → ByggReda (Falkenberg) |
| EDP Vision | XML per Vision XSD on submit (Falkenberg) |
| Evry Ephorte | XML on disk → Lex Talk (Karlskrona) |
| Flexeurope Flexite | One-way felanmälan to contact center (Norrtälje) |
| Ida Infront iipax/Bitsy | One-way PDF+data; not reusable |
| Prosona Castor | Create case in Castor; diary number back to Abou (direct or TEIS) |
| Seriline P-Express | Parking cards; P-Express uses Abou REST (Helsingborg) |
| Sokigo AlkT | Alcohol permits; list/edit serveringspersonal; Min sida lookups (Karlskrona) |
| Sokigo ByggR | MinutBygg / GÄHS: apply, supplement, decision, grannhöran (several kommuner) |
| Sokigo Ecos | MinutMiljö: avlopp, bergvärme, livsmedel, radon |
| Sokigo Evolution | Send case; Min sida; supplements; decisions |
| Sokigo OL2 | Folköl/tobak/e-cig (Karlskrona) |
| Sokigo Orbit | Felanmälan on complete (Huddinge) |
| Sokigo Skolskjuts | Prefill elev; send application; prelim decisions (Trelleborg) |
| Solarplexus Lex | XML on disk → Lex Talk (Upplands Väsby) |

AlkT and ByggR/Ecos are the richest Sokigo ones. No Python method tables except EDP Future ([edp-future.md](edp-future.md)).


---

## Källa: `references/integrations/plattformar.md`

# Integrationsplattformar

Read 2026-08-21.

## Pulsen Mule

Plugin streams XML to a REST API Pulsen built. Needs Abou ≥ 3.16, Pulsen Mule, Sokigo switch-on.

## Tieto TEIS

Generic adapter:

1. **Send case** (answers, files, case PDF) via TEIS UploadWebService after submit. **Waits for medsökande** if multipelsignering.
2. **Status back** into Abou (email if login or integrated personnummer).
3. **Fråga/svar** (first: KID person/fastighet). Cannot mix Navet + QID + KID without new development.

**Not** in first version: other system’s diary/handläggare in Abou, supplements from the other system.

Builder (docs “tänkt lösning”): field arguments map e-tjänst fields → target fields; DB configuration-table by **kortnamn**. Person prefills = ordinary person fields. Other lookups = Sokigo Python method.

Sammanställning: a TEIS adapter still needs a **second** adapter to the real target system.


---

## Källa: `references/integrations/arkiv.md`

# Arkiv

Read 2026-08-21.

**Formpipe Long-Term Archive:** generic searches configured in LTA; e-tjänst picks which query (e.g. logged-in user searches their grade). Örebro, Upplands Väsby, Täby.

**Ida Infront AGS:** enter fastighetsbeteckning, fetch related cases/documents (Norrtälje).


---

## Källa: `references/integrations/ovrigt.md`

# Other

**Google Analytics:** Sokigo puts the municipality tracker in **production** (deploy). Not configured per e-tjänst in the builder.

**Integrationsloggen:** video on the sammanställning page — how to debug calls. Use that in Admin when an integration fails; do not open citizen cases.


---
