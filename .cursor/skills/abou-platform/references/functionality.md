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

## Ångra osignerat ärende

On Min sida: undo a case not yet signed by medsökande. Supported functions list: [min-sida.md](min-sida.md).

## Attestering (Attestlista med sök)

Internal multi-approve, **not** vårdnadshavare. Needs **inloggning and signering**. Searchable dropdown. Svarsalternativ: `efternamn|förnamn|identitet|e-post` (all four) or Python `SetOptions`; optional 5th help segment with `{1}` `{2}`.

Mail: **Redigera meddelanden** → send **När sökande har signerat (medsökande finns)** → **Till fält för invånare (E-post)** = this field’s id.

Flow: pick chef → **Väntar på medsökandes signatur** → chef **Attestera** on Min sida → **Inkommet**.

Builder field notes: `build-abou-etjanst-web/references/field-types.md`.

## Värden som parametrar (URL)

Prefill from query string into `self.Service.SessionParameters` (string dict, **case sensitive**). Check `in` before indexing. Builder mall: `logic-templates/url-parameters.md`. Example: `Siteurl/Etjänstenamn?Smak=sur&Frukt=citron`.

## Mina meddelanden (DIGG)

Encrypted digital mailbox (Kivra, Min myndighetspost, Bring Digimail). Builder: `integrations/mina-meddelanden.md`. Message malls can target Mina meddelanden.

## Redaktör kan uppdatera svarsalternativ

Service Inställningar. Lets Redaktör change choice labels in **produktion** via Redigera texter. Can break logic, integrations, and behörighet-per-alternativ — warnings when those are on.

## AD-uppslag / synka användare

Lookups: login, rights admin UI, assigned handläggare in list/details. LDAP vs IdP: builder `integrations/active-directory.md`. Group names in AD can map to Abou groups (LDAP path).

## Pages still being filled from wiki into this folder

Krypterad e-post; Lämnameddelande; skapa nytt ärende från befintligt; e-post vid fel i Abou; handläggare ändrar svarsalternativ på inskickat ärende; responsiv anpassning; stöd för olika typer av e-tjänster. Until those sections exist here, say the skill does not have that page yet — do not invent behaviour.
