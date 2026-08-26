# Kömodulen

Add-on. Sokigo switches it on (no new deploy). Hub pageId `58525141`.

Citizen joins via an **e-tjänst with a köfält**. Case appears both in **ärendelistan** and under top menu **Köplatser**. Position = **registreringsdatum** (submit time); new cases go last. Removing a place renumbers. Status **Tilldelad** drops that place’s number so the rest move up.

## Prerequisites (Komma igång)

Builder must include:

- **Köfält** (required)
- **Integrerat personnummerfält** or login **before** the köfält (so the citizen can follow the place)

Then a kö-admin creates the queue(s).

| Task | Rights |
| --- | --- |
| Handlägga köer | System **Handlägga köer** + at least **Statusuppdaterare** on coupled services |
| Administrera köer | System **Skapa och redigera köer** + **Redaktör** or at least Statusuppdaterare on the service |

Optional: yearly digital payment (Swedbank Pay) via Min sida; extra columns; block duplicate places; Sokigo **köfilter** if column values come from service fields.

Payment amount in the e-tjänst **cannot** vary by which/how many queues the citizen picks.

If you delete a köplats, also update the **case** status in the ärendelista.

## Create queue

On the service: left **Köer** → **Skapa ny kö** → **Namn** (shown in the service if several queues, on Min sida, and to handläggare).

Settings:

| Setting | Effect |
| --- | --- |
| Tillåt flera köplatser per person | Same person may join again |
| Tillåt handläggare att ändra information i en köplats | Edit place info — only if the case was submitted **as ombud** |
| Tillåt handläggare att byta köplats | Move to an **existing** place; others shift |
| Tillåt handläggare att uppdatera registreringsdatum | Also updates case submitted date |
| Manuell betalning | Record a year paid outside Abou (invoice, etc.) |
| Status efter nekat erbjudande | Status if citizen says no |
| Erbjudandetext | Shown when status → **Erbjuden** |
| Maximalt antal platser | Integer; queue deactivates at that many **Erbjuden** or **Står i kö**. Empty = unlimited |
| Sista ansökningsdag | Deactivates after date |
| Specialkolumn 1–2 | Extra handläggare columns. Values from the e-tjänst need a Sokigo **köfilter** |
| Beskrivning | Admin only, not citizen |

## Handläggning (top menu **Köplatser**)

Search: personnummer, namn, adress, betalår, ombud vs invånare. Filter status. Excel export. Activate/deactivate queue. Link **Gå till kö** for settings (needs Skapa och redigera köer).

### Begära digital betalning

Needs yearly payment config, payment integration (Swedbank Pay), and the case **administreras av invånaren**.

- Whole queue: **Begär digital betalning** → all places without this year’s payment, citizen-administered, with a place number.
- One place: open place → same button.
- Reminders: button for everyone with an unpaid requested payment this year. Count shown in admin and on Min sida. Mall when: **Vid påminnelse-Betalningsbegäran** on the service tab for kömeddelanden.

Citizen pays from Min sida / Mina ärenden.

### Other actions

- Add person: **Skicka in som ombud** (same e-tjänst).
- Byt köplats / uppdatera registreringsdatum / ändra info: only if those flags are on.
- Status examples used in docs: **Står i kö**, **Erbjuden**, **Tilldelad**, **Nekad**, **Borttagen**. Confirm labels in the live UI.

## Kömeddelanden tokens

`$Comment$`, `$QueuePosition$`, `$QueueName$`.
