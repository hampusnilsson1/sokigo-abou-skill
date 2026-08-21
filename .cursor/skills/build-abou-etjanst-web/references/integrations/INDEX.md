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
