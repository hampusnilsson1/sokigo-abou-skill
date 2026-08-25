# Schemaläggning

Hub pageId `58524530`. Module from **2018.2**. Needs systembehörighet **Konfigurera schemaläggning**. Jobs are **per e-tjänst**. Menu: **Schemaläggning**. Add via **Lägg till schemalagd uppgift**. Tick **Aktiv** to run; untick to pause. **Spara ändringar** persists all jobs on the page.

Reminders need a meddelandemall coupled on the service with **När ska meddelandet skickas?** = the matching when (usually **Vid påminnelse** or **Signeringspåminnelse**). Recipients are the usual ones (sökande, handläggare, funktionsbrevlåda, e-post/SMS field).

Most reminder/file jobs run **once per day at 01:00**. Permanent delete runs **once per hour**.

## Job types

| Dropdown name | What it does |
| --- | --- |
| Skicka bokningspåminnelse | Hours before a booking |
| Skicka köplatspåminnelse | Days a köplats has had a given status (e.g. Erbjuden 3 days) |
| Skicka ärendepåminnelse | Days a case has had a given status |
| Skicka notifiering vid röstningsperiodens slut (e-förslag) | End of voting on an e-förslag service |
| Skicka Signeringspåminnelse | Unsigned medsökande / attest only (not those who already signed). Recurring or one-shot |
| Uppdatera status på ärende | Change status after N days in a status, or one-shot batch |
| Ta bort ärenden | **Soft** delete (flag; hidden in Abou) after status+time |
| Ta bort ärenden permanent | Hard-delete rows already soft-deleted. Sokigo must enable. Not for big one-off batches — use Admin **Permanent borttagning** |
| Skapa fil | File of cases or payments. Needs **CreateFilePlugin** (XML/FI, ordered separately). Types from site config (e.g. `.sie`) |
| Synkronisera personuppgifter | Refresh person data from configured register (usually Navet) for one service or all |

## Ärendepåminnelse parameters

Name; e-tjänst; **status**; **days in that status**; Aktiv.

Several jobs on the **same** service share the **same** reminder mall. The mail goes only for cases at **exactly** that day count — older cases are skipped.

Example: status *Väntar på medsökandes signatur* since 23 March → reminder 2 April 01:00 if days = 10.

## Signeringspåminnelse

Couple mall with when = **Signeringspåminnelse**. Job type **Signeringspåminnelse**, recurring or **Engångsjobb**.

## Skapa fil parameters

Name; e-tjänst; **Avser betalningar**; optional **status**; **För x dagar sen** or a fixed date; filtyp; Aktiv.

- Payments tick: include by payment day.
- Status only: include by status-change day.
- Both: payment date for that status.
- Neither: submit date.

## Synkronisera personuppgifter

Name; **Kör endast en gång** (else nightly); e-tjänst (empty = all persons with case relations); **Antal dagar sedan senaste synkronisering**; Aktiv.

Does **not** rewrite fältsvar. Dead / skyddade uppgifter show on **köplatser** after sync. Navet lookups cost money if the set is large.

## Soft / permanent delete

Soft: flag in DB; then permanent job (or Admin batch) erases. Permanent **cannot be undone**. Permanent job: name + e-tjänst + Aktiv.

## Status update

Name; one-shot vs recurring; e-tjänst; current status → new status; days since last status change.
