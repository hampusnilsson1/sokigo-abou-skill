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

Razor object in the mall is **HtmlCaseModel** (`@Model`). Changing organisation on a service switches to that org’s PDF mall, else kund/standard.

These PDFs are **not** the same thing as **meddelandemallar** (e-post/SMS). A notifiering can *attach* the ärende-PDF or beslut-PDF. The HTML/Razor below is what Abou turns into those PDFs.

## Two PDF jobs (the ones customers edit most)

| Mall | When Abou generates it | Typical attach-on |
| --- | --- | --- |
| **Ärende-mall** (Medborgare/Företag) | When the case is created (after submit / after last medsökande sign) | Inkommet-mail, Min sida, Admin |
| **Beslutsmall** (Medborgare/Företag) | When handläggare **Godkänn** or **Avslå** | Beslutsmail, Min sida “ta del av beslut” |

Same editor, same `@Model`, different body: ärende-mallen is a **sammanfattning of answers**; beslutsmallen leads with **the decision** then usually repeats the answers.

Both are a full HTML document: `<style>` in `<head>`, Razor in `<body>` inside `@{ … }`. CSS is customer-owned (font, left margin, zebra `bgcolor="efefef"`, table ~80% wide, `th.table-key` ~45%). Use `<caption class="sr-only">` when a table has no visible heading. Screen-reader captions and `scope="row"` on the question cell are the a11y pattern.

Do **not** hard-code a municipality name, logo path, or inbox in the shared kund-mall if organisation mallar should differ — put those in sidhuvud/sidfot or org-level mall.

### Ärende-PDF — what the mall must do

1. **Title of the case** — `@Model.Service.DisplayName` (h1).
2. **Ärende meta** — at least `@Model.UniqueId` and `@Model.Submitted` (`ToString("yyyy-MM-dd HH:mm")`). If `@Model.FirstSignedByAll.HasValue`, show that timestamp as signed-time (nullable — guard it).
3. **Answers** — only pages that have data: `foreach (var page in Model.Pages)` + `if (page.HasAnyValues)`. Page title = `@page.DisplayName` (h2). Then `foreach (var block in page.Blocks)`. On a block page (`page.IsBlockPage`) the block header is a table `<caption>` when not empty.
4. **Fields** — `block.Fields`; skip empty with `Model.HasValue(FriendlyFieldId)`.
   - If the answer is itself a table (`Answer.Contains("<table ")`), print question as a full-width header and `@field.Answer` as HTML (do not escape).
   - Otherwise two columns: question | answer, zebra rows (`j++ % 2`).
5. **Payments** (optional) — `Model.Payments` with culture `sv-SE`: amount (`ToString("C")`), `OrderId`, `Date`. Skip the block if the list is null/empty.
6. **Signing**
   - **Alternativ signering** (`Model.IsSignedAlternatively`): empty lines for Datum/Ort and Underskrift (paper sign after print).
   - Else **sökande**: `Model.ApplicantSignature` — Submitted, `SignedBy.FirstName` + `LastName`, `SignedBy.SocialSecurityNumber`, `Issuer`, `Signed`.
   - **Medsökande**: `Model.SortedRecentCoApplicantSignatures` (same columns, loop).
   - **Attestanter**: `Model.SortedRecentAttestSignatures` plus `SignatureAttest.AnswerString` (Bevilja/Avslå), `Comment`, optional `Attachment.FileName`.
7. **Kompletteringar** — `Model.Supplements`: Title, DateRequested, DateCompleted, OriginalFileNamesJoined, CitizenComment. Skip empty strings.

Older mallar loop `page.Fields` instead of `page.Blocks` / `block.Fields`. New kund-mallar should use **blocks** so layout matches the builder.

`HasValue` vs printing every field: ärende-PDF that should hide unanswered questions uses `HasValue`. Editerbar PDF mallar sometimes print all fields as inputs instead.

### Beslut-PDF — what the mall must do

1. **Service name** + caption **Beslutat**.
2. **Decision block first** — `@Model.Decision.DecisionText` (Godkänt / Avslaget), `@Model.Decision.Date`, handläggare, `@Model.Decision.Comment`. The property for the caseworker name on Decision is spelled **`Adminstrator`** in the template model (no “i”). Null-check `Model.Decision` if a mall can render before a decision exists.
3. **Same answer dump as the ärende-PDF** (pages → blocks → HasValue fields).
4. **Signing on the decision PDF** is usually gated with `Model.Service.RequiresEid`. Then either the paper-sign blanks (`IsSignedAlternatively`) or the applicant row from `Model.Signatures.FirstOrDefault(s => s.SignatureType == …SignatureType.Applicant)`.
5. Leave room after the decision for **överklagandehänvisning** (CSS hook `.overklaga` is common). Different Godkänt vs Avslaget wording belongs in this mall (or in sidhuvud/beslutstext), not in the e-tjänst layout.

### Razor pitfalls in dokumentmallar

- Guard nulls (`FirstSignedByAll`, `ApplicantSignature`, `Payments`, `Decision`, attest attachment).
- Table-valued answers must be detected before you wrap them in a two-column `<td>` or the nested table breaks the PDF.
- Field answers that contain a raw `@` without `@Model["fältid"]` can break PDF generation.
- Date format in Swedish PDFs: `yyyy-MM-dd HH:mm`.
- Money: `CultureInfo.CreateSpecificCulture("sv-SE")` + currency format.
- Alternativ signering and e-leg blocks are mutually exclusive in a well-written mall (`IsSignedAlternatively`).

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
- Signing block: Sokigo can require it on all blanketter or only e-leg services. In the **Ärendeblankett** mall, wrap “Sökandes underskrift” in `if (Model.RequireId) { … }` so unsigned services omit it
- Unique layout from 3.26 = this editor (customer-editable)

Publish as menygrupp type **Blankett genererad från e-tjänst**, or generate from Admin. Role **Skicka in ärende** can generate PDF. The blankett is **not** a fillable computer form — print, fill by hand, post.
