# XML conventions

Abou exports look like .NET `DataContractSerializer` XML: element order is fixed, nulls are `xsi:nil`, strings are often CDATA, and inherited content objects are flattened into the same element (duplicate `Id` / `IsDeleted`).

## Nulls

Empty optional values are nil elements with a local prefix:

```xml
<ExternalURL p2:nil="true" xmlns:p2="http://www.w3.org/2001/XMLSchema-instance" />
```

Prefix numbers follow nesting in the official export (`p2` at service root, `p4` on pages, `p6` on fields, `p8` on alternative help). Matching that pattern is safer than a single root `xmlns:xsi`.

## CDATA

Use CDATA for user-facing strings (names, questions, HTML, alternatives). Nested `]]>` must be split as `]]]]><![CDATA[>`.

PageNode IronPython is CDATA inside CDATA. The export closes the inner CDATA with:

```text
]]]]><![CDATA[></ObjectActivator>
```

See [ironpython-pagenode.md](ironpython-pagenode.md).

## Duplicate Id / IsDeleted

`<Service>`, `<Page>`, and `<Field>` each serialize **two** objects:

| Element | First `Id` | Second `Id` |
| --- | --- | --- |
| `Service` | Service entity | ServiceContent |
| `Page` | Page entity (also `Field/PageID`) | PageContent |
| `Field` | Field entity | FieldContent |

Keep both. The validator checks that the second ids exist in `Content`.

`Content` uses `FriendlyFieldId` (capital I only on Id). `Service` uses `FriendlyFieldID`.

## Service root (required skeleton)

Emit these children in this order (packager does this):

`Version`, `IsAdvancedService`, `AutoDiaryNumbering`, `ServiceName`, `ServiceShortName`, `MenuDisplayName`, `ServiceNr`, audience flags, `IsEnabled`, auth/signature/payment flags, `AvailableYears` (nil), `RequiresMultipleSignatures`, `CaseStatusList`, several nils, audit fields, `Type`, more flags, first `Id`/`IsDeleted`, `ServiceTags`, `Properties` (JSON array string), `SlotSettings` (JSON object string), `RequireEID`, `Organisation`, `Pages`, empty collections (`PdfTemplate`, `Diary`, emails, registers, `Chapters`), display/content fields, second `Id`/`IsDeleted`, `DirektFeedbackSettings`, `ProecessingTime` (sic — this misspelling exists in exports), `ExtendedData`.

Do not “fix” `ProecessingTime`.

Generated packages set audit fields `UpdatedBy` = `hani001` and `UpdatedByName` = `Hampus Nilsson`. Leave the original values when cloning a municipal export.

## Page skeleton

Each `<Page>` includes page-entity fields, then content fields (`DisplayName`, `PageHeaderHTML`, …), then optional `PageNode`, optional `LayoutAreas` (JSON string), `Fields`, `Properties`, `ActivationRule`.

`ActivationRule` and `LayoutAreas` are JSON text, not XML child elements.

## Field skeleton

Order matches the export. Optional `<Arguments>` sits after the first `Id`/`IsDeleted`. Optional `<Validators>` (JSON array string) sits after `QuestionAlternativeModels`.

`QuestionAlternatives` is a semicolon-separated CDATA list. `QuestionAlternativeModels` repeats each name.

## Content root

```xml
<Content>
  <ServiceContents>…</ServiceContents>
  <PageContents>…</PageContents>
  <FieldContents>…</FieldContents>
  <PDFTemplates />
  <ServiceEmails />
  <ServiceRequestEmails />
  <FaqEntries />
  <FaqEntryToServices />
  <FaqEntryToPages />
</Content>
```

`ServiceContent` includes a nil nested `<Service>` and `CustomerName=""`.

Do not leave Content pages that are absent from `Service/Pages`. New packages must stay in sync.
