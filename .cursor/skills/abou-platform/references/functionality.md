# Funktionalitet

Confluence *Funktionalitet*. How Abou behaves after the builder. Builder how-to stays in `build-abou-etjanst-web`.

| Feature | What it does |
| --- | --- |
| Dokumentmallar / blankett / editerbar PDF | [document-templates.md](document-templates.md) |
| Behörighet givet val | One choice field on the service (**Inställningar → Behörighet per svarsalternativ**). Only checkboxes/radios/rullistor. One field per service. Same role level, several alternatives. Applies to Verksamhetsadmin / Statusuppdaterare / Läs. Also filters Excel exports. Empty optional field → everyone with service right sees the case. **Alla behörigheter** = all alternatives including future ones. Existing cases are **not** retrofitted. New alternatives need an explicit grant. Removing stale alternatives: strip service right, save, re-grant. Editor/handläggare who change alternatives get a warning if this is on |
| Alternativ signering | Citizen can **Skriv ut och underteckna** instead of e-leg. Needs integrated personnummer (Min sida) or tacksida **PdfLinkThankYou.aspx** (from 3.26 without login). Admin shows not signed with e-leg |
| Förfylla från tidigare ärende | E-leg service + **ärendeväljarfält** + sidlogik (builder mall) |
| Komplettering med bilaga via Min sida | After submit; login or integrated personnummer; **one file at a time** with description → Relaterade filer. Handläggare file-komplettering from 2021.2: [cases.md](cases.md) |
| Spara och återuppta | Sokigo enables **system-wide**. Needs e-leg or integrated personnummer. **Spara** → Mina sparade ärenden. Resume starts the flow from the beginning with answers prefilled. Only latest save. Hide **Spara** per service Inställningar. If the service changed: restart; if inactivated: blocked. No time limit except gallring |
| Tilldelningsmall | Mail on **Tilldela handläggare** (also if you assign yourself). Disable on service **Redigera meddelanden** (Skicka vid handläggartilldelning) |
| Länkad e-tjänst | System **Skapa och redigera e-tjänster**. Tick **Länkad e-tjänst**, URL, optional iframe (height/width `%` or `px`, margins px) and introduktionssida (**Redigera texter**) |
| Visa svar i ärendelistan (Admin) | One or more field answers in parentheses after the name. **Cannot** filter/search on them. Sokigo or customer config |
| Visa svar på Min sida | Field **Fältdetaljer → Visa under ärenden på Min sida** (e.g. child name on skolskjuts) |
| Användningsmodulen | Sokigo cloud stats store, **not** the customer DB. Cached last night. No persons/cases (anonymous CaseId). Three views: overview, service, page validation. Right **Statistik och rapporter**. Stored actions: Started, Cancelled, Published, Saved, Resumed, PageEntered, PageExited, ValidationFailed |
| Inloggning | Any **SAML2** IdP. Methods: Mobilt BankID, Freja, Freja eID+, eIDAS |
| Signering providers | Twoday (f.d. Visma Sirius), CGI, Svensk e-identitet, Signport/KnowIT (fd Cybercom). Avtal + Sokigo config |
| Betalning i e-tjänst | Sysadmin: which service, amount, **Avbryt** return page. Pay now vs invoice = logikhopp. Variable amount = Python on Payment.aspx (builder mall). Provider: integrations |
| Betalning via Min sida | Yearly kö fee / later pay — [queues.md](queues.md), [min-sida.md](min-sida.md) |
| Ombud / forcera | [admin.md](admin.md) |
| Multipelsignering / meddelanden / URL-parametrar | Builder skill |
| Ångra osignerat ärende | [min-sida.md](min-sida.md) |

Pages still thinner (open Confluence if needed): Attestering (field **Attestlista med sök**), Krypterad e-post, Lämnameddelande, nytt ärende från befintligt, e-post vid fel i Abou, Dela e-tjänster, checklista driftsättning. FAQ answers: catalog titles in [catalog.md](catalog.md) — do not invent Q&A.
