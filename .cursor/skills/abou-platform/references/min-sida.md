# Min sida

Citizen portal. Module from **3.40**. Later hubs: *Min sida 2021.2 och 2024.2*. Login with e-leg.

Sokigo can hide undersidor from the menu (they still exist): **Köplatser och bokningar**, **Direktmeddelanden**, **Mina uppgifter**, **Mina ärenden**.

## Att göra (top of Min sida)

Each row is a button to the action; it disappears when done.

| Activity | When it appears |
| --- | --- |
| Väntande betalning | Unpaid case → payment page |
| Väntar på medsökandes signatur | Logged-in person is medsökande |
| Kompletteringsbegäran | Caseworker asked for supplement |
| Beslut ej tagits del av | Decision PDF not downloaded yet (counts when they open the PDF link) |
| Sparade ärenden | Draft resume / delete |
| Sparat ärende där e-tjänsten ändrats | Restart or delete |
| Erbjudande om plats i kö | Status Erbjuden → ja/nej |
| Olästa direktmeddelanden | Open the thread |
| Egenkonfigurerade villkor | Municipality rules, often from a verksamhetssystem (e.g. ByggR: unread decision, grannhörning) |

## Händelser (bottom)

Subset of case history: status changes on cases and köplatser; booking created/cancelled. **Visa** opens the case.

## Direct messages

Two-way messages with an e-leg-authenticated citizen. Caseworker knows sender/recipient is the logged-in person.

## Publicering och villkorsstyrning

Min sida content is driven by the logged-in person (age, parent, children’s age, fastighet, VA/avfall subscriptions, …) plus favourited e-tjänster.

## Versions

**2020.11 and earlier:** tabs like Min sida, Köplatser och bokningar, Direktmeddelanden, Mina ärenden, Mina uppgifter.

**Funktioner som stöds** (pageId `58524170`) on Min sida:

- Signera som medsökande
- Ångra ärende not yet signed by medsökande
- Komplettera (when allowed / when requested)
- Tacka ja/nej till köerbjudande
- Betala årlig köavgift
- Avboka bokning
- Ta del av beslut
- Ta del av handläggarbilagor
- Svara på direktmeddelanden

**2024.2:** organisation with **pages as top level** (custom navigation / grouping). Details: Confluence *Min sida efter 2024.2, med sidor som översta nivå*.

**Min sida Plus:** enhanced Min sida (Sokigo product variant). Do not invent widget lists; if the live site and this file disagree, trust the live site.
