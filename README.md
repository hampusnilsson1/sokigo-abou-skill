# sokigo-abou-skill

Cursor **Agent Skill** that builds a Sokigo [Abou](https://sokigo.com/produkter/abou/) e-tjänst as a zip Abou can import.

Abou e-tjänster are normally built in the web builder. Municipalities also export/import services as a zip (used when copying a service between environments or from [Provrummet](https://abou-provrummet.sokigohosting.com/)). This repo teaches an agent that zip format.

This is **Abou / Calamare**, not Open ePlatform.

## Use in Cursor

The skill lives at `.cursor/skills/create-abou-etjanst/`. Cursor loads it automatically in this repo. In another project, copy that folder or add this repository as a project skill.

Ask the agent to create an e-tjänst (or invoke `/create-abou-etjanst`). It will:

1. Collect name, pages, and questions
2. Write a JSON definition
3. Run `scripts/package_etjanst.py` to emit `Service/Service` + `Service/Content` inside a zip
4. Validate the zip

Do not keep complete e-tjänst exports in this repo. Format knowledge lives in `.cursor/skills/create-abou-etjanst/references/`. The agent builds only the service the user asked for.

## Zip format

Abou names the download `{kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export.zip`, for example `KOMPOST-150-2026-08-20-export.zip`. Inside:

```text
KOMPOST-150-2026-08-20-export.zip
└── Service/
    ├── Service    # UTF-8 XML, no .xml suffix
    └── Content    # UTF-8 XML, no .xml suffix
```

Details: `.cursor/skills/create-abou-etjanst/references/zip-and-import.md`.

## Package from JSON

```bash
python .cursor/skills/create-abou-etjanst/scripts/package_etjanst.py definition.json

python .cursor/skills/create-abou-etjanst/scripts/validate_etjanst.py \
  {kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export.zip
```

Authoring keys: `.cursor/skills/create-abou-etjanst/assets/schema.json`, `assets/definition.template.json`, and `references/json-definition.md`.

## References

| File | Contents |
| --- | --- |
| `references/field-types.md` | Builder palette → `TypeOfField` |
| `references/pages-and-flow.md` | Page URLs, LayoutAreas, payment |
| `references/xml-conventions.md` | Service vs Content XML |
| `references/zip-and-import.md` | Zip layout and import |
| `references/json-definition.md` | JSON for the packager |
| `references/validators-and-rules.md` | `requiredWhen`, ActivationRule |
| `references/ironpython-pagenode.md` | PageNode / integrations |
| `references/emails-booking-queue.md` | Mail, booking, kö |

These are format references. They are not e-tjänster.

## Public sources

- [Sokigo Abou product](https://sokigo.com/produkter/abou/) — builder, registers, booking, payment, e-ID
- [Abou e-tjänstebyggande courses](https://sokigo.com/kurser/abou-e-tjanstebyggande-steg-1/) — pages, fields, validation, emails, publish
- [Nacka on importing Abou services](https://www.nacka.se/medarbetare/digitalisering/sa-driver-vi-digitalisering/e-tjanster/)
- [Provrummet](https://abou-provrummet.sokigohosting.com/DELAETJANST) — shared catalog; no legacy fältsidor

Sokigo does not publish the Service/Content XSD. The XML layout in this skill is reverse-engineered from Abou exports. After import, always preview in Abou before publishing.
