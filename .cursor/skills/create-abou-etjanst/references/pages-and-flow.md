# Pages and flow

## Page kinds

| PageName (conventional) | PageURL | IsBlockPage | Fields |
| --- | --- | --- | --- |
| `InfoPage` | `BlockPage.aspx` | true | none; HTML in `PageHeaderHTML` |
| form pages | `BlockPage.aspx` | true | yes |
| `SummaryPage` | `Summary.aspx` | false | none |
| `SignPage` or `Sign` | `SignEID.aspx` | false | none |
| `payment` | `PaymentPage.aspx` | false | none (PageNode) |
| `ThankYou` | `ThankYou.aspx` or `PaymentThankYou.aspx` | false | none |

`PageType` is `Common`.

**New packages must use `BlockPage.aspx`** (`IsBlockPage` true) for info/form pages. Older **fältsidor** (`FieldPage.aspx`, `IsBlockPage` false) are rejected by Provrummet. Keep `FieldPage.aspx` only when cloning an old export that must stay as-is.

If `RequiresSignature` is false, omit the sign page. The sign page may be named `Sign` or `SignPage`; both are valid as long as `PageURL` is `SignEID.aspx`. The packager default is `SignPage`.

## Payment pages

A payment step is **pages + PageNodes**, not only `RequiresPayment`.

A payment flow uses `payment` → `PaymentPage.aspx` and `ThankYou` → `PaymentThankYou.aspx`. `<RequiresPayment>` can still be **false**. After a payment flow, thank-you is `PaymentThankYou.aspx`, not `ThankYou.aspx`.

Those PageNodes contain environment-specific HTTP/JSON IronPython. Clone them from an export the user supplies. Do not invent payment scripts, and do not set `RequiresPayment` true unless the user’s target site expects that flag.

The packager does **not** emit payment pages. Add them only when cloning.

## Version

`<Version>` on `<Service>` varies across Abou sites. For new JSON packages keep packager default `1` unless you are cloning a specific export (then copy that export’s Version).

## Order

`PageOrder` is 0-based and must match the intended wizard order. Linear services walk this list. Branching uses `PageNode` IronPython `GetNextPage()` (see [ironpython-pagenode.md](ironpython-pagenode.md)).

`ShowInSummary` should be true for pages whose answers belong on `Summary.aspx`.

## LayoutAreas

Block pages with fields store a JSON array in `<LayoutAreas>`. Each area is a visual block:

```json
{
  "BlockId": "BLOCK1",
  "Header": null,
  "Color": "#F5F5F5",
  "HideInPdf": false,
  "HorizontalFieldQuestion": false,
  "UsingCustomColor": false,
  "ColumnWidths": [[{ "Xs": 12, "S": 12, "M": 12, "L": 12 }]],
  "FieldLayout": [{ "Id": "KORTNAMN.10", "Row": 0, "Col": 0 }],
  "Description": null,
  "ActivationRule": {
    "enabled": false,
    "field": null,
    "answer": "",
    "condition": "Equals",
    "setsVisibility": false,
    "setsMandatory": false
  }
}
```

Column widths use a 12-column grid (`Xs`/`S`/`M`/`L`). The packager lays out one field per row at full width. That is the safe default; tighter grids and extra blocks (with `Header` / HTML `Description`) can be copied from an export after import.

Info/summary/sign/thank-you/payment pages omit `LayoutAreas`.

## Standard flags on form pages

- `IsEnabled`: true
- `IsServicePage`: true
- `UseDefaultContent`: false
- `ShowInMenu`: false (wizard, not a public menu of pages)
- `GeneratedServicePdfPageBreak`: false unless requested

## Service-level flow flags

| Flag | Meaning |
| --- | --- |
| `RequiresAuthentication` | Log in before the form |
| `RequireEID` | e-legitimation (BankID etc.) |
| `RequiresSignature` | Include `SignEID.aspx` |
| `RequiresPayment` | Payment **module flag**. Can be false even when `PaymentPage.aspx` exists |
| `RequiresMultipleSignatures` | Service-level multi-sign flag; the builder field is separate (see [field-types.md](field-types.md)) |
| `IsAnonymous` | No login |
| `AvailableCitizen` / `AvailableCompany` / `AvailableClub` | Audiences |
| `CaseStatusList` | Semicolon-separated handläggar statuses |

Default case statuses: `Inkommet;Registrerat;Under handläggning;Avslutat`.

`Type` is `Internal` (Abou’s classification of the service record, not “internal-only staff service”).
