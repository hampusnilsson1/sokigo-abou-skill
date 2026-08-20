# Zip layout and Abou import

## Canonical zip

Abou names the **download** after kortnamn, service number and export date:

```text
KOMPOST-150-2026-08-20-export.zip
```

| Part | Source |
| --- | --- |
| `KOMPOST` | Kortnamn = `ServiceShortName` |
| `150` | `ServiceNr` |
| `2026-08-20` | Export date (today when you export) |
| `export` | Fixed suffix |

The `.zip` extension is the container; Abou’s label is `{kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export`.

Inside the zip the payload is always a `Service` folder with two UTF-8 XML files **without** `.xml` extensions:

```text
KOMPOST-150-2026-08-20-export.zip
└── Service/
    ├── Service
    └── Content
```

Zip entry names must be:

- `Service/Service`
- `Service/Content`

Avoid `./Service/Service`, a wrapping dated folder, or `Service.xml`.

The files are DataContract-style XML (WCF). Encoding is UTF-8 with an XML declaration:

```xml
<?xml version="1.0" encoding="utf-8"?>
```

## What each file is

| File | Root | Role |
| --- | --- | --- |
| `Service` | `<Service>` | Structure: flags, organisation, pages, fields, layout, validators, optional IronPython `PageNode` |
| `Content` | `<Content>` | Localizable/content twins: service texts, page headers, field help HTML, alternatives |

`Content` is not a duplicate of `Service`. Field questions, types, and page URLs live in `Service`. HTML help, display names, and alternative labels are mirrored into `Content` so the importer can attach content rows.

IDs must line up:

- Second `<Id>` on `<Service>` = `<ServiceContent><Id>`
- Second `<Id>` on each `<Page>` = matching `<PageContent><Id>`
- Second `<Id>` on each `<Field>` = matching `<FieldContent><Id>`
- `<Field><PageID>` = first `<Id>` on that page (entity id)

The packager keeps these in sync.

## Import behaviour (observed + municipal practice)

Abou is built so municipalities can copy e-tjänster from each other (Nacka and others describe importing a service another municipality developed; Sokigo hosts **Provrummet** as a shared catalog).

Public docs do not publish an XSD. This skill is reverse-engineered from Abou exports plus Sokigo/Abou product pages.

Practical import notes:

- Numeric database IDs in the zip are source-environment IDs. The target Abou instance remaps them.
- `ServiceShortName` should be unique in the target. Change it in JSON before packaging if the code already exists.
- `Organisation/Id` will not match. Prefer a correct `OrganisationName`; admins re-bind the nämnd after import.
- Leave `IsEnabled` false. Publish from the builder after preview.
- Emails, diaries, PDF templates, linked registers, and FAQ entries are empty in a minimal package. Configure them in the UI.
- Integration pages (Bolagsverket company lookup) need the target site's integration modules. Importing the XML is not enough if the module is missing.
- Provrummet currently rejects services that still use old **fältsidor** (non-block field pages). New services must use `BlockPage.aspx` for form/info pages.

## After import checklist

1. Short name and display name
2. Organisation / nämnd
3. Menu group and visibility (citizen/company)
4. Authentication and signature settings
5. Preview every page, including conditionals and uploads
6. Case statuses and handläggar texts
7. Email messages
8. Integrations and registers
9. Publish

## Packaging command

```bash
python .cursor/skills/create-abou-etjanst/scripts/package_etjanst.py definition.json
# writes KOMPOST-150-2026-08-20-export.zip when shortName=KOMPOST and serviceNr=150

python .cursor/skills/create-abou-etjanst/scripts/validate_etjanst.py KOMPOST-150-2026-08-20-export.zip
```
