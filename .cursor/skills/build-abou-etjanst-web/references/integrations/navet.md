# Skatteverkets Navet (registerslagning)

Docs: [page 58524277](https://dok.sokigo.com/pages/viewpage.action?pageId=58524277) under Integrationer. Read 2026-08-21.

This is the page for **fetching person data from personnummer**. It is **not** a Python library catalog. Sokigo does not list `CitizenServiceProxy` methods here.

## What Navet does in Abou

Two Skatteverket services:

1. **PersonPost** — lookup by personnummer. Used to prefill e-tjänster.
2. **NamnSökning** — search by name/postcode etc., max 100 hits. Needs a **separate** Skatteverket subscription.

What PersonPost actually returns is limited by the municipality’s **avtal with Skatteverket**.

## Three ways to use PersonPost in an e-tjänst

1. **Integrerade personfält** (simplest). Common properties marked `*` below are stored in Abou’s database. Login recommended.
2. **Fördjupad Navetslagning** — relations (children, other guardians). Those people are **not** stored in the DB. Builder mallar: [navet-dropdown.md](../logic-templates/navet-dropdown.md) / [navet-table.md](../logic-templates/navet-table.md).
3. **Python from the session** — any PersonPost property from the last Navet call, session-only, not stored.

## PersonPost properties (docs list)

Stored via integrated fields when marked `*`: Personnummer*, Förnamn*, Efternamn*, Utdelningsadress 2*, Postnummer*, Postort*.

Also available (session / fördjupad): PersonID, Sekretessmarkering, Skyddad folkbokföring, Avregistreringsorsak, namn/tilltalsnamn, Mellannamn, folkbokföringsdatum, län/kommun/församling, fastighetsbeteckning, Care of, Utdelningsadress 1, särskild postadress, utlandsadress, civilstånd, födelse, invandring, **Relationer** (typ, datum, vårdnad, RelationID, personnummer), medborgarskap.

NamnSökning returns a shorter person+address set including samordningsnummer and sekretessmarkering.

## Skyddade personuppgifter

- **Skyddad folkbokföring** (stronger): no street address, only särskild postadress. Integrated address fields stay **empty**. Caseworker sees the flag.
- **Sekretessmarkering** (weaker): Navet still sends data with a flag. Integrated fields **prefill as usual**. Caseworker sees the flag. Reports can hide these cases.

**Multipelsignering + fördjupad slagning:** you must adapt Python yourself — whether to prefill medsökande personnummer/name/address depends on these flags.

## How to use Navet in logic

This page is **how the integration is used**, not a SDK dump. Types and calls:

| Need | Library | Docs |
| --- | --- | --- |
| Prefill from login (stored fields) | Integrerade personfält — no Python | Builder |
| Session PersonPost (GDPR bypass on `self.Citizen`) | `GetCitizenInfoLookUp` | [pagenode-api.md](../logic-templates/pagenode-api.md) |
| Children + other vårdnadshavare (`VF`) | `CitizenServiceProxy` / `ProxyRequest` | [navet-dropdown.md](../logic-templates/navet-dropdown.md), [navet-table.md](../logic-templates/navet-table.md) |
| Full PersonPost JSON, reuse in `Session` | `ICitizenServicePluginFactory.GetCitizenAsJson` | [extended-citizen.md](../logic-templates/extended-citizen.md) |

Map of all extra types: [libraries.md](../logic-templates/libraries.md). Clone from a working service on the same site if the mall needs adapting (certificates, avtal).

## KIR

The integration **sammanställning** also lists **KIR (Kommuninvånarregister)** as a registerslagning. There is **no** child page under Integrationer for KIR. Combined Navet+KIR+KID is documented as not supported without new development (TEIS page).
