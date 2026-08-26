# Bokningsmodulen

Sokigo add-on. Builder: **bokningsfält** + optional Python `SlotFilter`. Handläggare who create slots: at least **Statusuppdaterare**. Min sida avbokning needs login or integrated personnummer.

Use cases: personal meetings, rooms, group events with a seat cap. Combine with payment. Citizen: green days in a calendar, then times; optional pick handläggare; one or many slots. **Reservation** holds the slot for N minutes while they finish the flow.

## Admin tab **Bokningar**

Filter: handläggare, date range, Alla / Bokade / Helt obokade / Med lediga platser. Search visible text. Excel export = **booked** slots only. Unbooked → **Ta bort**. Booked → **Avboka** or **Boka om** (old time frees). Cannot edit date/time in place — delete and recreate (except seats).

### Create slot

Pick a service that has a booking field → **Skapa nytt bokningstillfälle**: date, start/end (end from **standardlängd**), optional handläggare (if **Använd handläggare för bokningar**), fritext (shown with the time), **antal platser**, **antal platser per bokning**.

Handläggare on the slot auto-assigns the **case** on book. Changing caseworker on the case does not change the slot; changing the slot later does not rewrite **existing** bookings. Multiple slots in one case → caseworker from the **first** selected slot. Unticking “använd handläggare” clears slot–user links.

### Recurring

Tick **Återkommande**, weekdays, interval, end date (default **6 months** if empty), exception dates. First occurrence is the **first matching weekday that week**, not necessarily the day you clicked — create that day as a single slot and start the series the week after. A series is one row in the list.

### Avboka / boka om

Admin: confirm avbokning (slot free again; avbokning-mail if configured). Boka om: pick a new free slot (avbokning + new booking mails). Citizen avboks from Mina ärenden until **deadline för avbokning** hours before start (`0` = until start). Admin is not limited by that deadline.

## Field arguments (bokningsfält)

| Argument | Effect |
| --- | --- |
| Tillåter flera bokningar | Several slots in the field |
| Max antal bokningar | Cap (with several) |
| Visar handläggare | Print name |
| Visar sluttid | `8:00-9:00` vs duration text |
| Tillåter multipla val | Several times the **same day** (with flera bokningar) |

## Service settings (Bokningar → Inställningar)

1. **Använd handläggare för bokningar** — required on create; auto-assign case
2. **Inkludera kalenderbokning** — `.ics` on the case; attach via bokningsmeddelande
3. **Standardlängd** — minutes
4. **Tid för reservation** — minutes held after pick (from 3.46; older = 20)
5. **Deadline för avbokning** — hours before start for the citizen

## Bokningsmeddelanden

Service **Redigera meddelanden → Bokningsmeddelanden → Lägg till ny**. When: **Bokning** (citizen book or admin rebook), **Avbokning** (citizen or admin), **Vid påminnelse** (scheduled). Prefer **Bokning** over “ärendet inkommit” as confirmation — inkommit does not mean a slot was booked. One mall per recipient (invånare / funktionsbrevlåda / handläggare). Tokens: [message-tokens.md](message-tokens.md). Reminders: [scheduling.md](scheduling.md).
