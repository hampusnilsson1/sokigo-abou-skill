# Create service and settings

Source: Sokigo Abou docs under *Hur är e-tjänsten uppbyggd?* (read 2026-08-21).

## Skapa ny e-tjänst

1. Top menu **E-tjänster**
2. **Skapa ny e-tjänst**
3. Fill **Egenskaper**
4. **Skapa**

## Egenskaper (new service)

**E-tjänstenamn** — what the citizen sees, e.g. “Anmälan om sophämtning”.

**Systemnamn** — unique, only in the URL. Usually three characters, e.g. `001`, `AOS`. Allowed: `a-z`, `A-Z`, `0-9`, `_`. Not `åäö`. Cannot be changed later in a useful way (settings page: “kan ej ändras”).

**Organisation** — grouping in admin.

**Skapa e-tjänst efter mall** — copy an existing service with a new systemnamn.

**Länkad e-tjänst** — not built in Abou; only a URL.

Checkboxes when creating:

| Setting | Effect |
| --- | --- |
| **Kräva inloggning** | e-legitimation before the service. Enables Mina ärenden. Requires **integrerade personobjektsfält**. Creates a personuppgiftssida. |
| **Kräva signering** | Citizen must sign before submit. Shown in case PDF and case. **Requires inloggning** (Abou ticks inloggning automatically; cannot sign without login). Creates a signeringssida. |
| **Kräva multipelsignering** | Two or more signers (e.g. guardians). Requires inloggning **and** signering. Creates a multipelsignering page. |
| **Möjliggöra beslut** | Caseworker can send a digital decision. |

Audience: **Medborgare** / **Företag** / **Förening**. With e-legitimation and the municipality “roll” feature, the citizen picks a role at start. Python can show different pages per role.

## Inloggning och signering

- Login only: no signature, e.g. fetch person data from Navet.
- Login + signing: must log in and sign to submit.
- Can be changed later in the builder.
- Ticking signing always ticks login.

## Service settings (after create)

Same ideas plus:

- **Använd denna e-tjänst som mall** — listed first when creating from a template; does not change runtime behaviour.
- **Tillåt sökande att ändra ärendet under Min sida** — only with multipelsignering. Applicant can change while status is “Väntar på medsökandes signatur” and the service definition has not changed after submit.
- **Tillåt invånaren att komplettera ärendet med bilaga under Mina ärenden**
- **Logga ut invånaren vid start av e-tjänst** — anonymity; case not tied to the logged-in user.
- **Begränsa åtkomst till enbart invånare i kommunen** — Sokigo must set kommunkod; needs login + Navet or KIR.
- **Dölj Spara-knapp**
- **Visa inte diarienummer på Min sida och Tacksidor** (from 2021.2)
- **Statuslista** — statuses shown in Mina ärenden
- **Alternativ signering** — e-legitimation **or** print and post
- **Köfilter** — Sokigo-developed queue rules
- **Visa hjälptexter i genererad blankett**
- **Redaktör kan uppdatera svarsalternativ** — production text edit; can break logic/integrations
- **Behörighet per svarsalternativ** — case visibility by answer
- **Ärenden osynliga för invånaren** — only new submitted cases; saved drafts still show
- **Tillåt invånaren att starta Direktmeddelanden**
- **Maximal sammanlagd storlek för ärendets bilagor i MB** — 0 = unused. Do not use with conditional file fields or skipped pages.
- Felmeddelande for that limit, else resource `Service.FileUploadField2.MaxTotalSizeOfAttachments`

## Default pages by type

If **no signing** (typ 1 and 2): InfoPage, Sammanfattningssida, Tacksida.

If **signing** (typ 3 and 5): InfoPage, **Dina uppgifter** (person fields below), Sammanfattningssida, Sign, Tacksida.

If **signing + multipelsignering** (typ 4): same as signing plus **Multipelsignatur**.

Auto fields on **Dina uppgifter**: Personnummer, Förnamn, Efternamn, Adress, Postnummer, Ort, E-post, Telefon, Mobil (optional), Kontaktfält (optional). Can rename, reorder, add, or remove.

## Multipelsignering

Docs: *Konfigurera en e-tjänst med multipelsignering*.

- After submit, status **Väntar på medsökandes signatur**. Cannot process until signed (or force as ombud / delete).
- Several multipelsigneringsfält allowed → several co-applicants.
- When all have signed: first status (usually **Inkommet**). Last signature time is “signerad”.
- Internal AD / integrated personnummer approval: use **Attestlista med sök**, not multipelsignering.
- If integrations set diarienummer used in messages: send message **När diarienummer sätts**.

Created page **Multipelsignatur**:

1. Field **Krävs flera signaturer** — Ja/Nej, obligatory
2. Field **Multipelsignering** with Personnummer, Förnamn, Efternamn, E-post

Field arguments on Multipelsignering:

- **Fält-id för att kräva signaturer** — field whose answer decides if a co-signer is required
- **Matchar svar** — e.g. `Ja`

With **fördjupad Navet-slagning**: create the child field yourself (dropdown or radio). Put `null` as the dummy answer alternative; citizens do not see the word null.

Always two signers (e.g. växelvis boende):

1. Remove **Krävs flera signaturer**
2. Remove those arguments on Multipelsignering
3. Set Multipelsignering **Obligatoriskt**

Lock name fields, keep email editable: argument **Endast epost är redigerbart** = `True`.

The multipelsigneringsfält **cannot** be configured as never required: either tick **Obligatoriskt**, or keep both “require signatures” arguments.

Notify the co-signer: [messages.md](messages.md) (*Koppla meddelandemall till e-tjänst*).

## Payment

Needs login, at least one answered field, payment page last before thank-you. Sokigo must add the service in system config (kortnamn, amount, error page usually Sammanfattning). Add a page and set sidtyp **Betalningssida**.
