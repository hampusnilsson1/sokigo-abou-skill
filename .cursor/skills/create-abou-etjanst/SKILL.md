---
name: create-abou-etjanst
description: Create a Sokigo Abou (Calamare) e-tjänst as an importable ZIP with Service/Service and Service/Content XML. Use when building, exporting, packaging, or converting a Swedish municipal e-service for Abou import.
---

# Create an Abou e-tjänst ZIP

Build a Sokigo **Abou** e-tjänst as a zip that can be imported in the Abou admin UI. Do not invent a parallel XML format. Always emit the export layout that Abou already understands.

This skill is for **Abou / Calamare** (namespaces such as `Abou.Calamare.Web`). It is not for Open ePlatform.

Do **not** include or present complete e-tjänst exports (real `Service`/`Content` packages). Format knowledge lives in [references/](references/). Build and return only the service the user asked for.

## When to use

- The user wants a new e-tjänst as a zip for Abou import
- The user has a description, PDF form, or existing export and wants an Abou package
- The user asks about `Service`/`Content` XML, FriendlyFieldID, BlockPage, or Calamare fields

## Output contract

Produce a zip with **exactly** this layout (folder name `Service`, extensionless XML files):

```text
Service/
  Service    # UTF-8 XML, root <Service>
  Content    # UTF-8 XML, root <Content>
```

Do not add a `.xml` suffix. Do not nest extra folders. The zip entries must be `Service/Service` and `Service/Content`.

Name the **zip file** like Abou’s own export download:

```text
{kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export.zip
```

Naming: kortnamn `KOMPOST`, ServiceNr `150`, export date 20 August 2026 → `KOMPOST-150-2026-08-20-export.zip`.

`kortnamn` is `ServiceShortName`. The date is the export day (also written to `LastUpdated` in `Service`). The packager uses that name by default.

Leave `isEnabled` false so import does not publish the service. Abou remaps numeric IDs on import; still emit unique, consistent IDs inside the package.

On generated packages set `UpdatedBy` to `hani001` and `UpdatedByName` to `Hampus Nilsson` (packager defaults). If the user supplies an export to clone, keep that file’s audit fields unless they ask to stamp these values.

## Workflow

1. Collect requirements (see below). Do not guess legal copy, organisation, or integrations.
2. Write a JSON definition matching `assets/schema.json`. Use `assets/definition.template.json` as the JSON shape (it is an authoring reference, not an e-tjänst).
3. Package:

   ```bash
   python .cursor/skills/create-abou-etjanst/scripts/package_etjanst.py path/to/definition.json
   ```

4. Validate:

   ```bash
   python .cursor/skills/create-abou-etjanst/scripts/validate_etjanst.py Out.zip
   ```

5. Give the user that zip plus a short import checklist.

Never hand-write the full Service/Content XML. Use the packager. Hand-editing XML is only for rare PageNode/IronPython cases after packaging.

## Requirements to collect

Ask only for what is missing:

| Topic | Why it matters |
| --- | --- |
| `shortName` | Unique code, prefix of every field id (`{shortName}.10`) |
| Display name | Menu and service title |
| Organisation / nämnd | Stored on the service; importer may remap |
| Audience | Citizen / company / club flags |
| Auth and signing | BankID (`requireEID`), signature page |
| Pages and questions | Labels, required, alternatives, help HTML |
| Conditional fields | `requiredWhen` / visibility |
| Attachments | `FileUploadField2` |
| Integrations | Bolagsverket, SPAR, registers — do not fake these |
| Thank-you / info texts | HTML on InfoPage and ThankYou |

A typical linear flow is: InfoPage → form page(s) → SummaryPage → Sign (`SignEID.aspx`) → ThankYou.

With payment (clone PageNodes from an export the user supplied; do not invent): … → Sign → `PaymentPage.aspx` → `PaymentThankYou.aspx`.

The packager prepends InfoPage when `infoHtml` is set, and always appends SummaryPage, SignPage (if `requiresSignature`), and ThankYou unless those pages already exist. It does not emit payment pages.

## Field IDs

`FriendlyFieldID` / `FriendlyFieldId` is `{shortName}.{n}`.

- Use stable integers in JSON (`id: 10` → `{shortName}.10`)
- Never reuse an id after deleting a field
- Radio/select values are matched as **exact strings** in validators (`Ja`, not `ja`)

## Field types

Prefer types verified from Abou exports. Builder Swedish names and arguments: [references/field-types.md](references/field-types.md).

| Builder name | JSON `type` |
| --- | --- |
| Textfält | `EGovTextField` (`textFieldNrOfRows` for several lines) |
| Datumfält | `EGovDateChooserField` |
| Filuppladdning | `FileUploadField2` (`allowMultiple`, `maxFileSize`) |
| Etikett | `EGovLabelField` (HTML in `preFieldHtml`; no input) |
| Kryssrutor | `EGovCheckBoxField` (`alternatives`) |
| Rullista | `EGovDropDownField` (`alternatives`) |
| Radioknappar | `EGovRadioButtonField` (`alternatives`) |
| Lägg till rad | `EGovAddRows2ColumnsListField` … `EGovAddRows5ColumnsListField` (`columns`) |
| Personuppgiftsfält | composite: `FirstNameField`, `LastNameField`, `IntegratedSocialSecurityNumberField`, address/phone/email types |
| Organisationsnummer | `OrganisationNumberField` |

Do not invent type names. Searchable dropdown, flervalslista, and multipelsigneringsfält have **no confirmed class name** — clone from an export the user supplies, or document the gap.

Do not put leftover Content pages (pages or fields that are missing from `<Pages>`) into a new package.

## JSON definition (authoring format)

Shape:

```json
{
  "shortName": "KORTNAMN",
  "displayName": "Visningsnamn",
  "organisationName": "Nämnd",
  "infoHtml": "<p>Ingress.</p>",
  "pages": [
    {
      "name": "Anmalan",
      "displayName": "Uppgifter",
      "fields": [
        {
          "id": 10,
          "type": "EGovTextField",
          "question": "Fråga",
          "required": true
        }
      ]
    }
  ]
}
```

Conditional required field:

```json
{
  "id": 14,
  "type": "EGovTextField",
  "question": "Följdfråga",
  "requiredWhen": {
    "field": 13,
    "answer": "Ja",
    "errorText": "Fyll i fältet när svaret är Ja"
  }
}
```

Page names should be identifier-like (`Anmalan`, `DinaUppgifter`). Display names are the Swedish labels shown to the user.

## Import in Abou

Exact admin labels vary by version. Typical path:

1. Open Abou administration (e-tjänstebyggaren)
2. Find import/exportera e-tjänst (often used to copy services between municipalities / Provrummet)
3. Upload the zip
4. After import: set organisation, menus, emails, registers, and integrations; preview; then publish (`IsEnabled`)

`Organisation.Id` from the source environment will not match the target. The importer usually keeps the name and assigns a local id.

## What not to do

- Do not emit Open ePlatform, 1177, or generic form XML
- Do not put `.xml` on `Service` / `Content`
- Do not enable the service in the zip
- Do not copy live person data from an export into a new service
- Do not write Bolagsverket/SPAR IronPython unless the user supplied a working export to clone
- Do not add leftover Content pages that are missing from `<Pages>`
- Do not ship or show complete e-tjänst exports; use `references/` for format details

## References (load on demand)

Format references — not e-tjänster. See [references/README.md](references/README.md).

- [references/zip-and-import.md](references/zip-and-import.md) — zip layout, import caveats
- [references/xml-conventions.md](references/xml-conventions.md) — Service vs Content, duplicate Ids, CDATA, xsi:nil
- [references/field-types.md](references/field-types.md) — field catalog and arguments
- [references/pages-and-flow.md](references/pages-and-flow.md) — page URLs, LayoutAreas
- [references/validators-and-rules.md](references/validators-and-rules.md) — requiredWhen, ActivationRule
- [references/json-definition.md](references/json-definition.md) — full JSON authoring guide
- [references/ironpython-pagenode.md](references/ironpython-pagenode.md) — custom page flow
- [references/emails-booking-queue.md](references/emails-booking-queue.md) — ServiceEmail, booking, kö, FAQ

## Scripts

| Script | Purpose |
| --- | --- |
| `scripts/package_etjanst.py` | JSON → zip |
| `scripts/validate_etjanst.py` | Structural checks |
| `scripts/xmlutil.py` | XML helpers used by the packager |

Validate a zip or a Service/Content pair with:

```bash
python .cursor/skills/create-abou-etjanst/scripts/validate_etjanst.py the-export.zip
python .cursor/skills/create-abou-etjanst/scripts/validate_etjanst.py --service Service --content Content
```
