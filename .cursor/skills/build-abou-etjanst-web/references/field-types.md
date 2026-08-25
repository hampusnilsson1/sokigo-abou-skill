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

Internal services (AD or integrated personnummer), **not** citizen guardian signing. Needs **inloggning and signering**. Searchable dropdown.

Svarsalternativ syntax: `efternamn|förnamn|identitet|e-post` (all four, pipe-separated). Or `SetOptions` in Python; help text as 5th segment with `{1}` `{2}` placeholders.

Email: **Redigera meddelanden** → new message → send **När sökande har signerat (medsökande finns)** → **Till fält för invånare (E-post)** = this field’s id.

Flow: pick chef → status **Väntar på medsökandes signatur** → chef **Attestera** on Min sida → **Inkommet**.

## Ärendeinformationsfältet

Shows recent cases in this service (e.g. felanmälan). Always shows **Inskickat**. Arguments for column/expander field ids, headers, photo from a file field (gif/jpg/png, Sokigo config), **Antal ärenden att visa** (default 10), max photo size.

## Ärendeväljarfält

Pick a previous submitted case to prefill later pages. Needs e-legitimation. Put **early** (intro). Prefill Python: mall **Förifyll värden med Ärendeväljarfältet**. Arguments Datumformat, Antal ärenden att visa, Antal tecken att visa från ärendenumret.

## Navigeringsknappsfält

**Obsolete** — removed from builder in **V26**. Existing services keep working. Do not use in new services. Was: custom button text, URL, or **Avbryt e-tjänst**.

## Föråldrade fälttyper (do not use)

Barnomsorgsfält, Barnomsorgsminifält, Beställningsfält, Modersmålsfält, Brandfarlig vara, Heltalssummering, Lånelista, Bygglovsväljare, Anhörigfält, Personallistfält, Textsummering, Dynamiskt funktionsbrevlåde, **Bokningsfält (gammalt)**, **Filuppladdningsfält (gammalt)**, EGovDistanceListField, EGovTextFieldLarge, EGovIframeField.

Current **Bokningsfält** / **Köfält** still exist elsewhere; they cannot use fältregler (see rules-validators.md). Booking field arguments and Admin slot UI: [booking.md](../../abou-platform/references/booking.md). Köfält: [queues.md](../../abou-platform/references/queues.md). Register as svarsalternativ: [registers.md](../../abou-platform/references/registers.md).
