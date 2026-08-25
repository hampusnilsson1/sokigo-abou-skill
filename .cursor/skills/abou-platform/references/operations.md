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
