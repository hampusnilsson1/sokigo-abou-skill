# JSON definition

Authoring format consumed by `scripts/package_etjanst.py`. Schema: `assets/schema.json`. JSON shape: `assets/definition.template.json` (authoring reference, not an e-tjänst).

## Required keys

```json
{
  "shortName": "KORTNAMN",
  "displayName": "Visningsnamn",
  "pages": []
}
```

`shortName` becomes `ServiceName`, `ServiceShortName`, and the prefix of every `FriendlyFieldID`.

## Recommended service keys

| Key | Default | Notes |
| --- | --- | --- |
| `menuDisplayName` | `displayName` | Shorter menu label if needed |
| `organisationName` | `"Organisation"` | Nämnd/förvaltning |
| `availableCitizen` | true | |
| `availableCompany` | false | |
| `requiresAuthentication` | true | |
| `requiresSignature` | true | Adds SignPage |
| `requireEID` | true | |
| `isEnabled` | **false** | Never auto-publish |
| `infoHtml` | — | Creates InfoPage |
| `thankYouHtml` | a short thank-you | ThankYou header |
| `caseStatusList` | Inkommet;Registrerat;Under handläggning;Avslutat | |
| `serviceNr` | auto | Abou `ServiceNr`; middle part of the zip name |
| `exportDate` | today | `YYYY-MM-DD` in the zip name and `LastUpdated` |
| `updatedBy` | `hani001` | Abou username (`<UpdatedBy>`) |
| `updatedByName` | `Hampus Nilsson` | Display name (`<UpdatedByName>`) |

## Pages

```json
{
  "name": "Uppgifter",
  "displayName": "Uppgifter om sökande",
  "showInSummary": true,
  "headerHtml": "<p>Valfri ingress.</p>",
  "fields": []
}
```

`name` must be unique and identifier-like (used in XML and IronPython `GetPage('Name')`).

The packager appends `SummaryPage`, `SignPage` (if signing), and `ThankYou` when missing. It does not add `PaymentPage.aspx` / `PaymentThankYou.aspx`; clone those pages from an export the user supplies when the service takes payment.

## Fields

```json
{
  "id": 10,
  "type": "EGovTextField",
  "question": "Verksamhetens namn",
  "required": true,
  "postFieldHtml": "<p>Hjälptext.</p>"
}
```

Choice field:

```json
{
  "id": 11,
  "type": "EGovRadioButtonField",
  "question": "Anmälan avser",
  "required": true,
  "alternatives": ["Ny anmälan", "Ändring", "Avanmälan"]
}
```

Upload:

```json
{
  "id": 15,
  "type": "FileUploadField2",
  "question": "Egenkontrollprogram",
  "required": true,
  "allowMultiple": true,
  "maxFileSize": 10
}
```

Checkbox / dropdown: `"type": "EGovCheckBoxField"` or `"EGovDropDownField"` with `alternatives`.

Label (no input):

```json
{
  "id": 16,
  "type": "EGovLabelField",
  "question": "",
  "preFieldHtml": "<h3>Uppgifter hämtade från e-legitimation</h3>"
}
```

Add-rows (column count must match the type):

```json
{
  "id": 20,
  "type": "EGovAddRows2ColumnsListField",
  "question": "Vilka kostnader har du?",
  "required": true,
  "columns": [
    { "question": "Typ av kostnad" },
    {
      "question": "Kostnad (kr)",
      "validator": "IntegerValidator",
      "summarizedNumbers": "KORTNAMN.20"
    }
  ]
}
```

Textarea: `"type": "EGovTextField", "textFieldNrOfRows": 5`.

Read-only e-ID name: `"type": "FirstNameField", "enabled": false`.

Several `requiredWhen` answers (OR): pass an array of `{ "field", "answer" }` objects.

## What the packager fills in

- Unique numeric Ids for entities, content rows, and arguments
- System pages
- Default `LayoutAreas` (one field per full-width row)
- Default slot settings and empty email/register collections
- `ExtendedData` attachment settings
- `DirektFeedbackSettings` nils
- Duplicate `Id`/`IsDeleted` pairs
- Matching `Content` document

## Editing an existing export

To tweak a real export instead of generating from JSON:

1. Keep both XML files
2. Change texts/flags carefully
3. Keep Content in sync (page/field content ids and short name)
4. Re-zip as `Service/Service` + `Service/Content`
5. Run `validate_etjanst.py`

Do not mix leftover Content pages from an old version of the service.
