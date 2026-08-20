# Field types

`TypeOfField` is the Abou/Calamare class name. The JSON definition uses the same string.

Map from the Swedish **builder palette** (fältväljaren) to XML. Prefer types verified in Abou exports. Do not invent a class name.

## Builder palette → TypeOfField

| Builder name | TypeOfField | Alternatives | Verified |
| --- | --- | --- | --- |
| Textfält | `EGovTextField` | no | yes |
| Datumfält | `EGovDateChooserField` | no | yes |
| Filuppladdning | `FileUploadField2` | often `AlternativesWithValues` even without labels | yes |
| Etikett | `EGovLabelField` | no | yes |
| Kryssrutor | `EGovCheckBoxField` | **yes** | yes |
| Rullista | `EGovDropDownField` | **yes** | yes |
| Rullista med sök + egna alternativ | *unknown* | yes | **no confirmed class** |
| Radioknappar | `EGovRadioButtonField` | **yes** | yes |
| Flervalslista | *unknown* | yes | **no confirmed class** |
| Multipelsigneringsfält | *unknown* | no | **no confirmed class** (behaviour documented below) |
| Lägg till rad | `EGovAddRows2ColumnsListField` … `EGovAddRows5ColumnsListField` | no | yes |
| Personuppgiftsfält | not a single type — emits identity/address fields | — | yes |

If the importer rejects a type, clone the exact `TypeOfField` from an export the user supplies. Do not guess `EGovCheckBoxListField`, `EGovDropDownListField`, or a searchable-dropdown class name.

## Verified types

### Text, choice, date, upload, label

| TypeOfField | Notes |
| --- | --- |
| `EGovTextField` | Single line, or several lines when `textFieldNrOfRows` is set (e.g. 5) |
| `EGovRadioButtonField` | One choice. `TypeOfFieldAlternative` = `AlternativesWithValues` |
| `EGovCheckBoxField` | One or more choices from a fixed list. Same alternatives XML as radio. May set `TextFieldNrOfRows` |
| `EGovDropDownField` | One choice from a dropdown. Optional arg `notificationByQuestionAlternative=True` |
| `EGovDateChooserField` | Date picker (kalender) |
| `EGovLabelField` | Heading/HTML only. `Question` is often nil; put the text in `PreFieldHtml`. Not an answer field. Do not attach `FieldAnswerDependencyValidator` |
| `FileUploadField2` | One or more attachments. Args below |

### Identity / personuppgifter

The builder “Personuppgiftsfält” is a composite. Emit the individual types, typically on the first personal-data page:

| TypeOfField | Notes |
| --- | --- |
| `FirstNameField` / `LastNameField` | Often `Enabled=false` when filled from e-ID |
| `SocialSecurityNumberField` | Manual personnummer; can `Hide=True` |
| `IntegratedSocialSecurityNumberField` | From e-ID |
| `AddressField` | |
| `PostcodeField` / `IntegratedPostcodeField` | Swedish postcode |
| `CityField` | Ort |
| `PhoneNumberField` / `MobilePhoneField` / `HomePhoneField` | Phone variants |
| `EGovEmailField` / `IntegratedEmailField` | Email |

A company-picker page may also include `TableField` plus locked names and integrated personnummer/email.

### Company / tables / add-rows

| TypeOfField | Notes |
| --- | --- |
| `OrganisationNumberField` | Organisationsnummer |
| `TableField` | Company-picker / display table. Optional args `SelectionMode=Single`, `AnswerIndex`. Alternatives are **not** required |
| `EGovAddRows2ColumnsListField` | Repeatable 2-column row group |
| `EGovAddRows3ColumnsListField` | 3 columns |
| `EGovAddRows4ColumnsListField` | 4 columns |
| `EGovAddRows5ColumnsListField` | 5 columns |

Add-rows column titles are `Question1` … `QuestionN` arguments, **not** `Question` on the field (that can be nil; intro HTML goes in `PreFieldHtml`). Optional per-column:

- `AnswerNValidator` = `IntegerValidator` for numeric cells
- `AnswerNSummarizedNumbers` = friendly field id that receives the sum

Use the **current** short name in that id (`{shortName}.20`). Do not leave a previous service’s short name in the sum target.

JSON shortcut: `"columns": [{"question": "Typ"}, {"question": "Belopp (kr)", "validator": "IntegerValidator", "summarizedNumbers": "KORTNAMN.20"}]` plus the matching `EGovAddRowsNColumnsListField` type.

### Booking / queue

| TypeOfField | Notes |
| --- | --- |
| `ReservationField2` | Booking widget. Needs `SlotSettings` and the booking module |
| `QueueField` | Queue widget. Needs the queue module |

See [emails-booking-queue.md](emails-booking-queue.md).

## Named in validator blacklist (exist in the platform)

These appear in `FieldAnswerDependencyValidator.BlackList`:

- `EGovLabelField`
- `ServiceBlockAccessField`
- `EGovNavigationButtonField`
- `EGovPastCasesDisplayField`

Do not put a dependency validator on them.

## Not yet confirmed in XML

Documented from the builder UI. **Do not invent XML** until an export confirms `TypeOfField` and argument names.

### Rullista med sökfunktionalitet

Dropdown where the user can search alternatives **and add their own**. Class name unknown. Clone from an export that contains this field.

### Flervalslista

List where the user selects one or more fixed alternatives by highlighting rows (not checkboxes). Class name unknown. Do not assume `EGovCheckBoxListField`.

### Multipelsigneringsfält

Field for medsökande / extra signers. A multiple-signature field **cannot be never-required**:

1. **Always required:** builder “Obligatoriskt” is checked (`IsRequired` true).
2. **Situationally required:** “Obligatoriskt” is off, and **both** of these field arguments are set:
   - **Fält-id för att kräva signaturer** — friendly id of the field that decides whether extra signatures are needed
   - **Matchar svar** — if that field’s answer equals this value, the multiple-signature field becomes required

Optional argument **Endast epost är redigerbart**: when checked, Förnamn, Efternamn and Personnummer are filled by logic script and not editable; the e-mail field stays editable.

Service flag `RequiresMultipleSignatures` exists on `<Service>` but is not a substitute for this field. Clone the field XML from an export the user supplies.

## Arguments (`FieldCreateArgument`)

| Name | Typical values | Used on |
| --- | --- | --- |
| `Enabled` | `false` | Lock a field filled by e-ID |
| `Hide` | `True` | Hide but keep in the model |
| `RequireFileDescription` | `False` / `True` | `FileUploadField2` |
| `AllowMultiple` | `True` / `False` | `FileUploadField2` |
| `MaxFileSize` | integer (e.g. `10`) | `FileUploadField2` (MB in the builder) |
| `SelectionMode` | `Single` | `TableField` |
| `AnswerIndex` | integer | `TableField` |
| `Question1` … `Question5` | column title | Add-rows |
| `AnswerNValidator` | `IntegerValidator` | Add-rows numeric column |
| `AnswerNSummarizedNumbers` | friendly field id | Add-rows sum target |
| `notificationByQuestionAlternative` | `True` | `EGovDropDownField` |
| `ShowEndTime` | `True` | `ReservationField2` |
| `MultipleSelect` | `True` | `ReservationField2` |
| `ShowAdminUser` | `True` | `ReservationField2` |
| `MaxNumberOfReservations` | integer | `ReservationField2` |
| `MultipleReservations` | `True` | `ReservationField2` |

JSON shortcuts: `"enabled": false`, `"hide": true`, `"allowMultiple": true`, `"maxFileSize": 10`, `"columns": [...]`.

## Alternatives

Choice fields need all of:

1. `QuestionAlternatives` CDATA: `Ja;Nej` or `Aktiebolag|AB;Handelsbolag|HB`
2. `QuestionAlternativeModels` with one `<Name>` per option
3. `QuestionAlternativesCompability` JSON array
4. `TypeOfFieldAlternative` = `AlternativesWithValues`

Pipe syntax `Label|code` stores the whole string as the answer. Dependency validators must match **that stored string** (`Aktiebolag|AB`, not `Aktiebolag`, when the alternative was defined with a code). If the alternative has no pipe, match the label.

A leading space in an alternative is significant if present.

## HTML around fields

- `PreFieldHtml` — heading/intro before the control (required for `EGovLabelField`)
- `PostFieldHtml` — help under the control
- `InfoButtonText` — info-button HTML
- `MouseOverText` / `SummaryQuestion` — often a copy of `Question`

HTML is stored as XML CDATA, typically TinyMCE snippets (`<p>`, `<ul>`, `<a>`).

## Identity fields vs manual fields

When `RequiresAuthentication` / `RequireEID` is true, prefer integrated types on the first personal-data page and disable names/address if they should be read-only.

A separate manual page is only needed when the flow allows “fill in company/person data yourself”.
