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

## How to write a meddelandemall

**Meddelandemallar** are e-post / SMS / Mina meddelanden — not the PDF editor. Couple them under **Redigera meddelanden**. Subject and body may use `$token$` (case-sensitive). A mall has a **name** (internal) and a **subject** (what the citizen sees). SMS max 160 characters; no Razor in SMS or scheduled reminders.

### What every citizen mail should contain

1. **What happened** in plain language (status changed, you are in a queue, please sign, decision taken, …).
2. **Which case** — `$uniqueID$` (and `$serviceName$` if the person has several services).
3. **What they should do next** if anything (open Min sida with e-leg, wait for a second mail, sign as medsökande).
4. **That they cannot reply** to the technical sender (point to a real kontaktväg in the closing).
5. **Closing** — organisation name + how to reach the municipality (e-post/phone). Put the closing in sidfot-equivalent text in the mall, not as a one-off in a single service if many services share a kund-mall.

Do not paste live inbox addresses into shared notes; each customer fills their own closing.

### Statusnotifiering (e-post or SMS)

Trigger: **Vid statusuppdatering** (not the first submit). Body pattern: status has changed → identify the case with `$uniqueID$` → follow the case on **Min sida** (e-leg login) → no-reply + closing.

SMS: same facts, shortened to 160 characters (`$uniqueID$` still).

### Köbekräftelse

Trigger: when the citizen is placed in a queue (kö-mail coupled on the service/kö). Subject often includes `$serviceName$`. Body pattern: thanks for the anmälan → they are **in the queue** → a further confirmation of plats/deltagande will follow → which queue `$QueueName$` and which number `$QueuePosition$` → closing.

`$Comment$` is the handläggarens kö-status comment when that is what you are notifying.

### Tokens vs Razor

- Tokens: `$uniqueID$`, `$serviceName$`, `$QueueName$`, `$QueuePosition$`, `$citizenFirstName$`, … — work in subject, e-post, SMS.
- `$ServiceName$` (capital S) is **not** the documented token; `$serviceName$` is. Wrong casing is left as literal text.
- Field answers and richer PDF-like blocks: Razor `@this.Model["Fält.Id"]` or `@Model.…` in **e-post** mallar only.
- Attach the **ärende-PDF** or **beslut-PDF** on the coupling (attachments), rather than duplicating the whole Razor PDF inside the mail body.

## Statusnotifieringar

New **inloggning** services get an automatic status message (not on first submit). Citizen opt-in: **Integrerat kontaktfält**. Without login: add a message later to an email field.

## Manual message from a case

**Skicka meddelande** (from 2023.2 email or SMS). Needs a link to the applicant. Works while **Väntar på medsökandes signatur**. Mallar marked **Manuellt ärendemeddelande**.

## Sökande ändrar / ångrar before co-sign

Service Inställningar (off by default):

- **Tillåt sökande att ändra ärendet under Min sida**
- **Tillåt sökande att ångra ärendet under Min sida**

While status is **Väntar på medsökandes signatur**, the applicant on Min sida can revert the case to **utkast**, change answers, and submit again. [functionality.md](../../abou-platform/references/functionality.md).
