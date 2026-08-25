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

Combined with behörighet-per-alternativ: dialog warns that the field drives rights; picking an alternative they do not have makes the case unavailable to them. Standalone page steps: [catalog.md](catalog.md) title *Handläggare kan redigera svarsalternativ för ett inskickat ärende* — do not invent extra UI.

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

