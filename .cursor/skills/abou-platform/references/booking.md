# Bokningsmodulen

Add-on. Confluence children: Beskrivning; Handläggning; Skapa nytt bokningstillfälle; Återkommande tillfällen; Boka om och avboka; Konfigurera bokningar; Bokningsmeddelanden.

Facts already confirmed elsewhere (do not invent slot-UI details):

- Builder: bokningsfält + optional Python `SlotFilter` (`build-abou-etjanst-web` mall *booking-filter*).
- E-tjänst roles that may add/edit/delete **unreserved** slots: Verksamhetsadmin, Beslutsfattare, Statusuppdaterare, Redaktör.
- Scheduled **bokningspåminnelse**: hours before start ([scheduling.md](scheduling.md)).
- Min sida: avboka; Händelser lists booked/cancelled.
- Message tokens: `$ReservationDate$` (single booking), `$ReservationSpots$`, `$ReservationUTCStart$`, `$ReservationUTCEnd$`. Razor `@this.Model["fältId"]` lists booked occasions. [message-tokens.md](message-tokens.md).

For create-slot steps, read the Confluence child or the live **Bokningar** admin — not invented here.
