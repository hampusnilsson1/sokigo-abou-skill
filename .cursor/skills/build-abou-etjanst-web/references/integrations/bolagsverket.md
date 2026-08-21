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
