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

## Deployprocess

Sokigo’s own hosting/deploy pipeline is a separate wiki page. Until that page is copied here: do not invent IIS slots or who clicks deploy. Kundservice/Support process is not in this skill.
