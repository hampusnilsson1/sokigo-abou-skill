# Dokumentmallar och PDF

From version **3.26**. Tab **Dokumentmallar** in Admin. Right: **Skapa och redigera dokumentmallar**.

Older sites laid out PDFs in the database. The editor replaces that.

## What you edit

| Part | Typical use |
| --- | --- |
| Sidhuvud | Logo, heading |
| Sidfot | Contact, address |
| Ärende-mall Medborgare/Företag | PDF when a case is created |
| Beslutsmall Medborgare/Företag | PDF when handläggare fattar beslut — different text for Godkänt vs Avslaget |
| Ärendeblankett-mall | PDF from **Generera blankett**. Needs the customer mall’s special code |

Recommended: duplicate the complete **kund-mall**, then small changes per organisation or e-tjänst.

## Priority (content is taken from the first level that has a mall)

1. E-tjänst
2. Organisation (only if there is **no** e-tjänst mall coupled to that organisation)
3. Kund
4. Standard

Changes do **not** rewrite old PDFs already generated.

Editor actions: search (visible text / e-tjänst / organisation), filter malltyp, sort, add, **couple to e-tjänst or organisation**, duplicate, delete.

Razor object in the mall: [technical/htmlcasemodel.md](technical/htmlcasemodel.md). Changing organisation on a service switches to that org’s PDF mall, else kund/standard ([admin.md](admin.md)).

## Hantera dokument (file library)

Tab **Dokument**: upload then link as `/FileStorageArea/Documents/FILNAMN.ext`. Images on text pages must be uploaded here first. Select + **Ta bort** to delete.

## Editerbar pdf-mall (builder tree)

For **internal** services: text fields in the case PDF stay editable in a PDF reader after submit (`data-pdf-form-field="true"`). Text fields only. Demo: Provrummet `PDFtest`.

In **Dokumentmallar** → tab **Medborgare**, replace the lower two `Answer` outputs (not all three) with an `<input data-pdf-form-field="true" …>` bound to `FriendlyFieldId`. Full loops: Confluence *Editerbar Pdf-Mall* (example 1 = all fields, example 2 = filled fields / `Model.Pages` + `HasAnyValues`).

## Blankettgeneratorn

The e-tjänst **is** the blankett. **Ladda hem blankett** / **Generera blankett** (E-tjänster → Allmänt) always uses the current service. Pages become sections; choice fields two columns; help texts can print at the end (service **Inställningar**). Manual page breaks: page **Inställningar** or field **Avancerat**. Header/footer follow ärende-PDF. Signing block on the blankett is a Sokigo config (all vs e-leg services only). Unique layout from 3.26 = this editor.

Publish as menygrupp blankett type **Blankett genererad från e-tjänst**, or generate from Admin. Role **Skicka in ärende** can generate PDF.
