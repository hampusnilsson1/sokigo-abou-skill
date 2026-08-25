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

## Editerbar pdf-mall

From builder tree *Editerbar Pdf-Mall*. For **internal** services: after submit, text fields in the case PDF stay editable in a PDF reader (`data-pdf-form-field="true"`). **Text fields only.** Typical flow: beställare fills page 1–2 → sends → mottagare edits in a PDF app → forwards internally (utförare/ekonomi) or back with quote details. Citizen/beställare can also edit and send the PDF on.

Demo on Provrummet: `/PDFtest`. Customer can do this themselves (~1 hour Sokigo help for the stock example).

### How to wire it

1. Tab **Dokumentmallar** — clone an existing mall or create new.
2. Tab **Medborgare** — edit the PDF mall look and behaviour.
3. Find the existing `Answer` output. There are **three** `Answer` sites; change only the **lower two**.
4. Replace:

```html
<td>@page.Fields[i].Answer</td>
```

with:

```html
<td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
```

5. Save and couple the mall to one or more e-tjänster.

Table cells with `AnswerContains("table")` stay as ordinary `@page.Fields[i].Answer` (not inputs). Alternate row colour: `bgcolor="efefef"` when `i++ % 2 == 0`.

### Kodexempel 1 — print every field (editable)

Intent: loop all pages and fields; non-table answers become PDF form inputs.

```
foreach (var page in Model.Pages) { var j = 0;
<table>
  <caption>@page.DisplayName</caption>
  <tbody> @for (int i = 0; i < page.Fields.Count(); i++) {
    if (@page.Fields[i].AnswerContains("table")) {
      <tr bgcolor="efefef">
        <td colspan="2">@page.Fields[i].Question</td>
      </tr>
      <tr>
        <td colspan="2">@page.Fields[i].Answer</td>
      </tr>
    } else {
      if (i++ % 2 == 0) {
      <tr bgcolor="efefef">
        <td>@page.Fields[i].Question</td>
        <td>
          <input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/>
        </td>
      </tr>
      } else {
      <tr>
        <td>@page.Fields[i].Question</td>
        <td>
          <input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/>
        </td>
      </tr>
      }
    }
  }
  </tbody>
</table> }
```

### Kodexempel 2 — only pages that have values

Wiki heading: only fields the citizen filled. Outer guard is `page.HasAnyValues`. Inner `if (!Model.HasValue(...))` is **as on the Confluence snippet** — if a test mall skips the wrong rows, drop the `!` or the `HasValue` check. Nested `<tr>` under the table-answer branch is also as on the wiki.

```
foreach (var page in Model.Pages)
{
    if (page.HasAnyValues)
    {
        var j = 0;
        <table>
            <caption>@page.DisplayName</caption>
            <tbody>
                @for (int i = 0; i < page.Fields.Count(); i++)
                {
                    if (!Model.HasValue(@page.Fields[i].FriendlyFieldId))
                    {
                        if (@page.Fields[i].AnswerContains("table"))
                        {
                            <tr bgcolor="efefef">
                                <td colspan="2">@page.Fields[i].Question</td>
                            </tr>
                            <tr>
                                <td colspan="2">@page.Fields[i].Answer</td>
                            </tr>
                        }
                        else
                        {
                            if (i++ % 2 == 0)
                            {
                                <tr bgcolor="efefef">
                                    <td>@page.Fields[i].Question</td>
                                    <td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
                                </tr>
                            }
                            else
                            {
                                <tr>
                                    <td>@page.Fields[i].Question</td>
                                    <td><input data-pdf-form-field="true" type="text" name=@page.Fields[i].FriendlyFieldId value="@System.Web.HttpUtility.HtmlAttributeEncode(page.Fields[i].Answer ?? string.Empty)"/></td>
                                </tr>
                            }
                        }
                    }
                }
            </tbody>
        </table>
    }
}
```

## Blankettgeneratorn

The e-tjänst **is** the blankett. Every **Ladda hem blankett** / **Generera blankett** (E-tjänster → Allmänt) uses the current service, so the paper form cannot go stale.

- Pages become sections; choice fields in two columns; list objects with prefix
- Help texts can print at the end: service **Inställningar → Visa hjälptexter i genererad blankett**
- Manual page breaks: page **Inställningar** or field **Avancerat**
- Header/footer follow ärende-PDF
- Signing block: Sokigo can require it on all blanketter or only e-leg services. In the **Ärendeblankett** mall, wrap “Sökandes underskrift” in `if (Model.RequireId) { … }` so unsigned services omit it ([faq.md](faq.md))
- Unique layout from 3.26 = this editor (customer-editable)

Publish as menygrupp type **Blankett genererad från e-tjänst**, or generate from Admin. Role **Skicka in ärende** can generate PDF. The blankett is **not** a fillable computer form — print, fill by hand, post.
