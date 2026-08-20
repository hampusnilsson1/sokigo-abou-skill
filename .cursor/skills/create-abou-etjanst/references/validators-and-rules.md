# Validators and rules

## Required checkbox

`IsRequired` on the field is the simple required flag. Use it when the field is always mandatory.

## Conditional required (`requiredWhen`)

Abou stores this as a JSON array in `<Validators>` named `FieldAnswerDependencyValidator`.

JSON authoring:

```json
"requiredWhen": {
  "field": 13,
  "answer": "Ja",
  "errorText": "Ange webbplats när distansförsäljning sker"
}
```

The packager expands that to the export-shaped validator:

- `FieldOnPage` = friendly id of the controlling field
- `FieldAnswer` = exact stored answer (`Ja`, not `true`). If alternatives use `Label|code`, match the **whole** stored string (`Aktiebolag|AB`), unless that export’s validators use the label only
- `ErrorText` = message shown to the user

One field may have **several** dependency validators (OR of answers). In JSON, `requiredWhen` may be an object or an array of objects.

The controlling field is **not** made hidden by this validator. It only toggles mandatory. Visibility is a separate `ActivationRule`.

Do not put this validator on `EGovLabelField`, `ServiceBlockAccessField`, `EGovNavigationButtonField`, or `EGovPastCasesDisplayField`.

## ActivationRule

JSON object on both pages and fields:

```json
{
  "enabled": false,
  "field": null,
  "answer": "",
  "condition": "Equals",
  "setsVisibility": false,
  "setsMandatory": false
}
```

To hide a field unless another answer matches, set `enabled` true, `field` to a friendly id, `answer` to the expected value, `setsVisibility` true.

Most form pages leave `ActivationRule` disabled and use `FieldAnswerDependencyValidator` plus IronPython `GetNextPage` for branching.

## Page branching vs field rules

| Need | Mechanism |
| --- | --- |
| Field becomes required | `requiredWhen` / `FieldAnswerDependencyValidator` |
| Field hidden/shown | `ActivationRule` on the field (and/or LayoutAreas) |
| Skip a whole page | `PageNode` `GetNextPage()` |
| Default an answer | `PageNode` `Initialize` `SetAnswer` |

## Other validators

Exports mainly use `FieldAnswerDependencyValidator`. Add-rows numeric columns use the field argument `AnswerNValidator=IntegerValidator` (not the `<Validators>` JSON). Older fields also have empty `ValidatorName` / `ValidatorArgument` (legacy single-validator slots). Leave those nil unless cloning an export that fills them.

If the user asks for Swedish personnummer/email/postcode checks, prefer the dedicated field types (`SocialSecurityNumberField`, `EGovEmailField`, `PostcodeField`) instead of inventing validator JSON.

A multipelsigneringsfält that is not always required uses its own arguments (“Fält-id för att kräva signaturer” + “Matchar svar”), not `FieldAnswerDependencyValidator`. See [field-types.md](field-types.md).
