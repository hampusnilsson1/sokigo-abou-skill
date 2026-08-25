# Registermodulen

Paid add-on. Tab **Register**. Shared choice lists (e.g. skolor) instead of duplicating rullistor or Python. Min sida display of registers was **not built yet** when the page was written.

## Create / import

**Visningsnamn** (required, editable, not unique), **systemnamn/kortnamn** (required, unique, **immutable**, same rules as e-tjänst kortnamn), beskrivning optional.

- **Skapa Register** — add rows in Admin
- **Importera register** — `.csv` (save Excel as CSV). Re-import **same kortnamn** **overwrites** the register. No sort/filter in Admin — edit in Excel then re-import.
- Delete only if **not** coupled (button grey).

Edits apply to running services without republishing. A resumed draft sees the new rows.

## Couple to e-tjänst

Builder **Inställningar → Koppla register**. One service can use many registers; one field uses **one** register (**Fältdetaljer / Svarsalternativ**). Register view lists coupled services.

Must exist in the **same environment**. Export service to prod → export register too unless kortnamn already exists there (**case sensitive**). Missing register → **import of the e-tjänst fails** with that systemnamn in the error.

## Rights

Anyone in Admin can **see** registers and coupling. Editors can couple. Create/update/import/export/delete needs system **Administrera Register**.

## Text/värde

In a row: `visningstext:::värde` (three colons). Hidden value for fältregler / logikhopp.
