# Field rules, validators, and field arguments

Source: Sokigo Abou docs (read 2026-08-21).

## Prefer UI rules over Python

From version **2020.11**, **fältregler** and **visningsvillkor** can skip pages and show/hide/require fields **without** Python or JavaScript.

Do **not** combine those UI rules with Python/JS that also show/hide fields or skip pages — conflicts. Combining with Python/JS for *other* logic is fine.

**Fältregler** cannot be used on **Bokningsfält** or **Köfält**.

### Fältregler

On the field whose **answer** should drive other fields: tab **Fältregler**.

Can show/hide other fields or **blocks**, and make them obligatory.

### Visningsvillkor

On the **later page**: Inställningar → **Visningsvillkor**. Point at a field on an earlier page, pick a condition, comparison value. If true, the page is in the flow.

### Conditions (fältregler and visningsvillkor)

| Condition | Use |
| --- | --- |
| Equals, NotEqualTo | Single answer only |
| Contains, DoesNotContain | Same, but still true if other answers are selected too |
| In, NotIn | Several answers in one rule, semicolon: `Röd;Gul` |
| GreaterThan, LessThan | Single numeric (or numeric string) |
| GreaterThanOrEquals, LessThanOrEquals | Same |

## Validators (layout builder from 2018.11)

Configured on the field. Hub child-list “Validatorer” (26 pages) did **not** load (404). Use this list from *Konfigurera validatorer*:

| Validator | What it does |
| --- | --- |
| Allt eller inget | All listed fields filled, or none |
| Antal val i ett flervalsfält | Min and/or max number of choices |
| Beroende | This field required when another field has a given answer (e.g. “Annat”) |
| Datum | Date format; optional compare to today, a fixed date, or another field |
| Exakt ett svar | Exactly one of several fields filled (separate empty vs too-many texts) |
| Minst ett svar | At least one of several fields |
| Olika svar | Answers must differ |
| Samma svar | Answers must match |
| Reguljärt uttryck | Custom regex |
| Tal | Integer or decimal; optional min/max |
| Veckodagar | Date falls on given weekdays |
| Äldre än eller yngre än | Age vs personnummer or date; “äldre än” is ≥, “yngre än” is strictly < |

Also mentioned on field properties: **standardvalidering (obligatoriskt fält)** exists as a concept; tick **Obligatoriskt** on the field.

## Common fältargument (friendly names in the UI)

| Argument | Value | Effect |
| --- | --- | --- |
| Tal | True | Text field numeric only |
| Max antal tecken | Positive int | Max length |
| Dold om fältet är tomt | True | Hide when empty |
| Dold | True | Always hidden |
| Aktiverad | False | Read-only (e.g. prefilled) |
| Aktivera meddelande per svarsalternativ | True | Different email recipients per choice |
| Svar redigerbart av handläggare | True | After submit, handläggare can change this choice on the case ([functionality.md](../../abou-platform/references/functionality.md)) |
| Datumformat | e.g. `yyyy-MM-dd HH:mm` | Booking / ärendeväljare |
| Visar sluttid | True/False | Booking interval display |
| Antal ärenden att visa | Positive int | Recent cases |
| Antal tecken att visa från ärendenumret | Positive int | Truncate case number display |
| Endast epost är redigerbart | True | Multipelsignering: lock name/personnummer, keep email |

Arguments are also used to map fields for integrations.
