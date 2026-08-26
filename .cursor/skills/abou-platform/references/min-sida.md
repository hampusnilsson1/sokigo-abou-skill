# Min sida

Citizen portal. Module from **3.40**. Later hubs: *Min sida 2021.2 och 2024.2*. Login with e-leg.

Sokigo can hide undersidor from the menu (they still exist): **Köplatser och bokningar**, **Direktmeddelanden**, **Mina uppgifter**, **Mina ärenden**.

## Att göra (top of Min sida)

Built-in rows are buttons; each disappears when done.

| Activity | When it appears |
| --- | --- |
| Väntande betalning | Unpaid case → payment page |
| Väntar på medsökandes signatur / attestera | Logged-in person is medsökande or attestant (resurstext) |
| Kompletteringsbegäran | Caseworker asked for supplement |
| Beslut ej tagits del av | Decision PDF not downloaded yet (counts when they open the PDF link) |
| Sparade ärenden | Draft resume / delete |
| Sparat ärende där e-tjänsten ändrats | Restart or delete |
| Erbjudande om plats i kö | Status Erbjuden → ja/nej |
| Olästa direktmeddelanden | Open the thread |
| Egenkonfigurerade villkor | Extra e-tjänster published under Att göra (see villkor below) |

## Händelser (bottom)

Subset of case history: status changes on cases and köplatser; booking created/cancelled. **Visa** opens the case.

## Direktmeddelanden

Two-way thread in **logged-in** mode (e-leg). Needs the Min sida module. Caseworker always knows sender/recipient is the logged-in person.

- Handläggare can **always** start a thread from a case: case → tab **Direktmeddelande** → write → **Skicka meddelande**. Optional notifiering so the citizen logs in to Min sida.
- Citizen can start a thread only if the service setting **Tillåt invånaren att starta Direktmeddelanden** is on (**from 3.48**). Otherwise they can only reply in an existing thread.
- Ärendelista: **blue** speech bubble = unread; **grey** = thread exists, already read.
- Unread threads also appear under **Att göra**. Permanent case delete drops the messages ([admin.md](admin.md)).

## Publicering och villkorsstyrning

A service is **not** on Min sida until you publish it there. Admin top menu **Publicering → Min sida**.

Villkor is **code that returns True or False**. Input is the logged-in **citizen** object (personuppgifter). You can also key off dates. Pick a mall, then edit freely. **Testa**: type a personnummer/identitet in the box to the right — returns whether that person would see the item. **Do not copy real personnummer into git.**

### Under Tjänster

1. **Lägg till**
2. Choose e-tjänst
3. Display name (the Min sida link text)
4. Villkor mall for **Tjänster** → edit so it returns True/False
5. **Testa** if needed
6. **Spara**
7. Order: **Sortera** (alpha) or drag the list — matching services show in that order. **Ta bort** then pick another mall to switch template.

Typical villkor: age, parent/guardian, children’s age, fastighet, VA/avfall, always-visible, date window.

### Under Att göra

Built-in Att göra rows (pay, co-sign, …) appear automatically. Extra rows are e-tjänster that call a **verksamhetssystem**. Example: ByggR komplettering — villkor looks up ByggR; if the person has a pending komplettering the row shows (“Din bygglovsansökan behöver kompletteras”). **The villkor must become False after they complete the service**, or the row never leaves Att göra.

Same Lägg till / namn / mall / Testa / Spara / Sortera flow as Tjänster, but the mall list is the **Att göra** set.

## Versions

**2020.11 and earlier:** tabs like Min sida, Köplatser och bokningar, Direktmeddelanden, Mina ärenden, Mina uppgifter.

**Funktioner som stöds** on Min sida (2021.2 list):

- Signera som medsökande / attestera
- Ångra ärende not yet signed by medsökande ([functionality.md](functionality.md))
- Komplettera where the service allows it
- Komplettera when handläggare begärt komplettering
- Tacka ja/nej till köerbjudande
- Betala årlig köavgift
- Avboka bokning
- Ta del av beslut
- Ta del av handläggarbilagor
- Svara på direktmeddelanden

## Min sida efter 2024.2 (sidor som översta nivå)

From **2024.2** the top level is **sidor** (they appear in the toppmeny). Previously the top level was kategorier. A sida is text + **komponenter**. Two component types today (more may come):

| Komponent | What it is |
| --- | --- |
| **Inbäddad kategori** | Inline list (e.g. things to do, started applications) |
| **Bildkortsmeny** | Image you click to reveal the content |

Treat sidor as **permanent** menu entries so Min sida feels familiar. Show/hide **inside** the page (components and their content), do not hide the whole sida.

A sida is the CMS-like entry point for the **logged-in** person.

### Standard Min sida (not editable layout)

Two sidor:

1. **Att göra** — two inbäddade kategorier: **Att göra** and **Påbörjade ansökningar**
2. **Mina ärenden** — two bildkortsmenyer: **Pågående ärenden** and **Avslutade ärenden**

### Min sida Plus

Customers with Plus can arrange sidor and komponenter themselves. External content from other systems is often put on **own sidor**. Do not invent extra widget types; if the live site disagrees, trust the live site.
