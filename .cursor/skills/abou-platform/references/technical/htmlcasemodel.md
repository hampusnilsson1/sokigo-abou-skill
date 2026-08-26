# HtmlCaseModel (Razor)

Source: *HtmlCaseModel*. Read 2026-08-25.

Used in **dokumentmallar**, **e-postmallar**, and thank-you text when the page type is **ThankYouAdvanced**.

This is **not** the Python `PageNode` case object. In e-tjänst logik, use PageNode helpers, not these entities.

Access with `@`:

```
@Model.UniqueId
```

Razor (C#). WYSIWYG for mail / ThankYouAdvanced: prefer short expressions, not raw HTML control flow:

```
@(Model.Decision != null ? Model.Decision.DecisionText : "Beslut ej fattat")
```

Dokumentmallar may use `@if`.

Nullables: never dereference when null.

## Model / Case

`Model` is `HtmlTemplate.Case`.

| Name | Type | Meaning |
| --- | --- | --- |
| Id | int | DB id (internal) |
| UniqueId | string | Ärendenummer |
| DiaryNumber | string | Diarienummer (handläggare, e-tjänst, or API) |
| State | string | Status (Inkommet, Registrerat, Avslutat, …) |
| SentInAs | CitizenRole | Submitter role |
| Administrator | Administrator | Assigned caseworker |
| Submitted | DateTime | Submit time |
| Applicant | Citizen | Submitter |
| CoApplicants | Citizen enumerable | Medsökande |
| HasBeenSignedByAll | bool | All co-signers signed |
| Service | Service | E-tjänst |
| Payments | List of Payment | Payments |
| IsSignedAlternatively | bool | Print-and-post |
| HasMultipleSigning | bool | Multipelsignering or Attestlista med sök |
| SentInByOmbudsman | bool | Ombud |
| Proposal | Proposal | E-förslag if configured |
| Decision | Decision | Latest decision |
| Fields | List of Field | All fields |
| Signatures | List of Signature | Signatures |
| ApplicantSignature | Signature | Applicant |
| SortedRecentCoApplicantSignatures | List | Co-signers by name |
| SortedRecentAttestSignatures | List of SignatureAttest | Attest |
| FirstSignedByAll | DateTime? | When all required signatures existed; use `.HasValue` before `.Value` |
| Pages | enumerable | Layout pages for the PDF dump |
| Supplements | enumerable | Requested kompletteringar |
| `Model[friendlyId]` | Field | Lookup by FriendlyFieldId |
| HasValue(friendlyId) | bool | True when that field should print |

### Page / Block (dokumentmall)

| Name | Meaning |
| --- | --- |
| page.DisplayName | Page title in the PDF |
| page.HasAnyValues | Skip empty pages |
| page.IsBlockPage | Blocks have their own headers |
| page.Blocks | Blocks on the page |
| block.Header | Caption when IsBlockPage |
| block.Fields | Fields to loop (prefer this over `page.Fields` in new mallar) |

`Model.HasValue(field.FriendlyFieldId)` — skip unanswered questions on the PDF.

Table-like answers: `field.Answer.Contains("<table ")` (substring, including the space). Then print Answer as HTML, not as a plain cell.

### Administrator

UserName, FirstName (actually **full name**), Email — empty string if unassigned / unknown.

### Citizen (template)

Id, SocialSecurityNumber (personnummer or AD identity), FirstName, LastName, Email, PhoneNumber, MobilePhoneNumber, Address, City, PostalCode, MunicipalityKey, metadata dictionary.

### Decision

Date, Comment, DecisionText (**Avslaget** or **Godkänt**), **Adminstrator** (spelling in the model — full name, else username, else empty / API).

### Service

RequiresEid / RequiresAuthentication / RequiresSignature / RequiresMultipleSignatures, DisplayName, Name, ShortName, ServiceNr (stable across versions).

### Field

| Name | Meaning |
| --- | --- |
| Answer | Display answer (string or HTML) |
| Question | Rubrik e-tjänst |
| FriendlyFieldId | Id for `@Model["x.1"]` |
| RawAnswer | Original (sometimes JSON) |
| PostFieldHtml / PreFieldHtml | Text under/above field |
| SummaryQuestion | Rubrik ärende |
| TypeOfField | Internal (e.g. `EGovTextField`) — not citizen-facing |
| IncludeEmptyAnswer | Show empty on summary |
| HasAnswer | True if answered (empty counts if IncludeEmptyAnswer) |

### Payment

Amount (provider units may differ), OrderId, Date, PayedBy (Citizen; docs note it “borde heta PaidBy”), PaymentType, TransactionId.

## Signatures

`ApplicantSignature` — the sökande. `SortedRecentCoApplicantSignatures` — medsökande. `SortedRecentAttestSignatures` — attest; extra `SignatureAttest.AnswerString`, `.Comment`, `.Attachment` (FileName). `Signatures` — full list; filter with `SignatureType.Applicant` (namespace `Abou.Calamare.Framework.HtmlTemplate`).

Each signature: `Signed` (DateTime), `Issuer`, `SignedBy` (FirstName, LastName, SocialSecurityNumber, DisplayName).

```
@Model.ApplicantSignature.SignedBy.DisplayName
@foreach (var signature in Model.SortedRecentCoApplicantSignatures){@(signature.SignedBy.DisplayName + "\n")}
```

## Supplements

Title, DateRequested, DateCompleted, OriginalFileNamesJoined, CitizenComment. Loop `Model.Supplements`.

## Enums (UPPRÄKNINGAR)

**CitizenRole:** Unknown, Citizen, Company, Organisation.

**PaymentType:** Applicant, CoApplicant.

**ProposalFilterType** (e-förslag list filters): *Inväntar publicering*, *Röstning pågår*, *Inväntar ställningstagande*, plus decided statuses *Godkänt* / *Avslaget* / *Besvarat* / *Avslutad*. URL example: `/Citizen/Proposal?status=Godkänt&status=Avslaget` (space as `%20`).

Substitution tokens `$name$` are listed under meddelandemallar / tokens.
