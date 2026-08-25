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
