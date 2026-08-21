# Logic libraries and mallar

This folder documents **how to use Abou’s Python and JavaScript libraries**, and includes the official builder **mallar** as examples.

- **Library (how it works):** [libraries.md](libraries.md), [pagenode-api.md](pagenode-api.md), [client/api.md](client/api.md)
- **Integrations those libraries call:** [../integrations/INDEX.md](../integrations/INDEX.md)
- **Example to adapt:** one mall in the tables below

Read the library files when explaining, reviewing, debugging, or designing — **not only** when you need a new script to paste.

**Do not load this whole folder.** Prefer fältregler/visningsvillkor before code. Prefer listed methods before inventing APIs.

In the builder: tab **Logik** or **Klientlogik**. Replace `ANGEFÄLTID` / `'x.1'` / `BLOCK1`. Python **class name = IronPythonType = page systemnamn** (malls often say `InfoPage` — rename).

## Sidlogik (Python) — `PageNode`

How to use the library: [libraries.md](libraries.md) + [pagenode-api.md](pagenode-api.md).

| Topic | File |
| --- | --- |
| All PageNode helpers | [pagenode-api.md](pagenode-api.md) |
| Empty class | [standard.md](standard.md) |
| URL query → fields (`SessionParameters`) | [url-parameters.md](url-parameters.md) |
| Payment amount / order text | [payment.md](payment.md) |
| Custom validator text + stay on page | [custom-validation.md](custom-validation.md) |
| Booking `SlotFilter` | [booking-filter.md](booking-filter.md) |
| File upload types | [file-upload.md](file-upload.md) |
| Navet children + other guardian (dropdown) | [navet-dropdown.md](navet-dropdown.md) |
| Same with tabellfält | [navet-table.md](navet-table.md) |
| Prefill from multipelsignering JSON | [prefill-multisign.md](prefill-multisign.md) |
| Prefill from ärendeväljare | [prefill-case-selector.md](prefill-case-selector.md) |
| Copy fields, läggtillrad, dynamic lists | [prefill.md](prefill.md) |
| Required field hidden by JS | [required-when-hidden.md](required-when-hidden.md) |
| Hide/disable fields and blocks (server) | [hide-fields-blocks.md](hide-fields-blocks.md) |
| Internal user from AD (`RestWrapper`) | [ad-lookup.md](ad-lookup.md) |
| System log (`LogDebug` …) | [logging.md](logging.md) (builder name **Inloggning**) |
| Skip pages (`GetPage`) | [page-skip.md](page-skip.md) |
| Sums / läggtillrad | [calculations.md](calculations.md) |
| Build tabellfält JSON | [table-field.md](table-field.md) |
| After submit (`Published`) | [thankyou.md](thankyou.md) |
| Full PersonPost JSON | [extended-citizen.md](extended-citizen.md) |

Thank-you **plugin** `IPythonCaseService`: [../logic.md](../logic.md).

## Klientlogik (JavaScript) — `PageLogic`

How to use the library: [libraries.md](libraries.md) + [client/api.md](client/api.md). Only on **Layoutsida**.

| Topic | File |
| --- | --- |
| Empty skeleton | [client/empty.md](client/empty.md) |
| One field (get/set/hide/empty, split text/value) | [client/handle-field.md](client/handle-field.md) |
| Several fields and blocks | [client/handle-many.md](client/handle-many.md) |
| Hide a block when a field matches | [client/hide-block-on-value.md](client/hide-block-on-value.md) |
