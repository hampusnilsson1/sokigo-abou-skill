# Abou libraries

This folder is the **documentation of Abou’s supported libraries** (IronPython `PageNode` and extra types, JavaScript `PageLogic`). The mall files are **worked examples** of those libraries.

Read here whenever you need to **know how a method, type, or integration-backed library works** — explaining to the user, reviewing pasted code, designing a flow, debugging, or writing new logic. Do **not** open a mall only when you need a new file to paste.

Sokigo does not publish a separate SDK. **These notes plus the mallar are the library.** Methods not listed here are unsupported (“kundens eget ansvar”).

**Do not load this whole folder.** Start at this file or [INDEX.md](INDEX.md), then one API file and (if you implement) one mall.

## When to read what

| Situation | Read |
| --- | --- |
| What Python can do / which method to call | [pagenode-api.md](pagenode-api.md) |
| What client JS can do / hide-show on the same page | [client/api.md](client/api.md) |
| Navet, REST, payment, AD, EDP, … (product + how it is used) | [../integrations/INDEX.md](../integrations/INDEX.md) then one file |
| Need a working script to adapt | [INDEX.md](INDEX.md) → one mall |
| Field rules instead of code | [../rules-validators.md](../rules-validators.md) |
| Where to type code in the builder | [../logic.md](../logic.md) |

## Layering (use the lowest layer that works)

1. **Fältregler / visningsvillkor / fältargument** — no library. Prefer this for show/hide and page skip.
2. **Klientlogik (`PageLogic`)** — same Layoutsida, instant, browser only. Does not persist hide/require for the next page unless Python agrees.
3. **Sidlogik (`PageNode`)** — on enter (`Initialize`) or leave (`GetNextPage` / `BeforeGetNextPage`). Other pages, validation that stops Nästa, registers, REST, payment amount, thank-you.

Python hide and JS hide are different. A field hidden only in JS can still be **required** on the server — use [required-when-hidden.md](required-when-hidden.md).

## Core library: `PageNode` (every Logik tab)

Import: `from Abou.Calamare.Web import PageNode`. Class name **must** equal IronPythonType **and** the page **systemnamn**.

| You need | Use |
| --- | --- |
| Read/write answers, options, labels | `GetAnswer` / `SetAnswer` / `SetAnswerIfEmpty` / `SetOptions` / `SetQuestionText` |
| Split “text\|value” alternatives | `GetValueFromQuestionAlternative` / `GetAnswerFromQuestionAlternative` |
| Hide, require, disable field or block | `SetHidden` / `SetRequired` / `SetDisabled` / `SetHiddenBlock` / `SetHiddenAndClearBlock` |
| Stop the citizen on this page | `SetValidationText` **and** `return self.Page` |
| Jump to another page | `return self.GetPage('Systemnamn')` |
| Log in preview | `LogDebug` / `LogInfo` / `LogError` (+ `*Object`) |
| JSON as a field answer | `Serialize` / `Deserialize` |
| Other cases / ärendeväljare | `GetAnswerFromCase` / `GetCasesByServiceAndQuestionAnswer` / `GetDetailed` |
| After submit | `GetAnswerFromPublishedCase` / `SetAnswerToPublishedCase` / `GetPublishedCasePdf` / `Published()` |
| Logged-in person (GDPR-stripped) | `self.Citizen` |
| Fuller PersonPost in **session** | `GetCitizenInfoLookUp` — see Navet below |
| Query string `?Smak=sur` | `self.Service.SessionParameters` ([url-parameters.md](url-parameters.md)) |
| Cross-page Python state | `self.Session['key']` (serializable). Do not call Navet again on every page. |

Full method list and mall: [pagenode-api.md](pagenode-api.md).

Lifecycle: `Initialize` → citizen fills → `BeforeGetNextPage` → `GetNextPage` must return a page. Thank-you: `Published(self)` returns `PublishedResult`.

Field ids: `'x.1'` = **this** service short name + number. Other service: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)`.

## Core library: `PageLogic` (Klientlogik)

Only on **Layoutsida**. Always:

```javascript
PageLogic = function() {
    var self = this;
};
```

Runs in the browser when answers **on this page** change. Cannot see other pages, cannot call Navet/REST, cannot stop Nästa by itself.

| You need | Use |
| --- | --- |
| One field | `self.GetField(id)` then `SetAnswer` / `GetAnswer` / `SetHidden` / `EmptyField` |
| Same without instance | `self.SetAnswer(id, v)` / `GetAnswer` / `SetHidden` / `EmptyField` |
| Several fields/blocks | `EmptyFields` / `SetHiddenFields` / `SetHiddenBlocks` |
| React to a value | `field.When("equals"\|"notequals"\|"contains"\|"notcontains", value, fn)` |
| Custom compare | `self.When(fn, value, callback)` |
| Split text/value on change | `field.WhenEvent(fn, "change")` + `GetValueFromQuestionAlternative` |

Full list: [client/api.md](client/api.md). Examples: [handle-field.md](client/handle-field.md), [handle-many.md](client/handle-many.md), [hide-block-on-value.md](client/hide-block-on-value.md).

## Extra types (only with matching integration / field)

These are **not** always available. They need the field type and usually a **sysadmin-enabled** integration. Document the product in `integrations/`, use the type as shown in the mall.

| Type / factory | What it is | Integration / setup | Example |
| --- | --- | --- | --- |
| `CitizenServiceProxy`, `ProxyRequest` | Children / other guardians from Navet (`VF`, skyddad identitet) | [navet.md](../integrations/navet.md) | [navet-dropdown.md](navet-dropdown.md), [navet-table.md](navet-table.md) |
| `ICitizenServicePluginFactory` + `GetCitizenAsJson` | Full PersonPost JSON (Navet / TEST / TEIS shapes differ) | [navet.md](../integrations/navet.md) | [extended-citizen.md](extended-citizen.md) |
| `IRestWrapperServiceFactory` | Named REST config (URL, auth). Python fills `IntegrationHttpRequest.Parameters` | [adapter-rest.md](../integrations/adapter-rest.md) | [ad-lookup.md](ad-lookup.md) (`InternalWebSearch`) |
| `SlotFilter` on booking field | Filter bookable slots (admin, days, text, weekends) | Booking field on the page | [booking-filter.md](booking-filter.md) |
| `TableFieldModel` | Table JSON (headers, widths ≤ 12, rows) | Tabellfält; not in preview | [table-field.md](table-field.md) |
| `AnswersModel.Deserialize` | Läggtillrad cells `Answer1`, `Answer2`, … | [calculations.md](calculations.md) | same |
| Payment hooks on Payment.aspx | `HasPaymentInfo`, `GetPaymentOrderText`, `CalculatePaymentAmount`; read via `GetAnswerFromFieldId` | [payment.md](../integrations/payment.md) | [payment.md](payment.md) |
| `PublishedResult`, published-case helpers | After submit | Thank-you page | [thankyou.md](thankyou.md) |
| `IPythonCaseService` | `AddRelationToCase`, `UpdateStateForCase`, `AssignAdministratorToCase`, `RegisterCase` | Sysadmin plugin; [../logic.md](../logic.md) | thank-you scripts |
| EDP Future Request methods | Invoices, meters, subscriptions | [edp-future.md](../integrations/edp-future.md) | clone a working Future service — no builder mall here |
| `JavaScriptSerializer` | .NET JSON serialize/deserialize | Used inside several mallar | prefill, table, Navet |

How to use an extra type: read the **integration file** (what the product does, avtal, sysadmin) **and** the **mall** (exact imports and calls). Do not invent method names from the integration marketing page.

## GDPR and person data

- `self.Citizen` on a logged-in service is **stripped** (e.g. civilstånd, födelse, raw CitizenData often empty).
- Session lookup: `GetCitizenInfoLookUp` — not stored in DB.
- Relations (barn, other VF): `CitizenServiceProxy` mallar — those people are **not** stored unless you write them into fields.
- Skyddad folkbokföring / sekretessmarkering: [navet.md](../integrations/navet.md). Dropdown mall drops protected children and blocks protected other guardians; table mall does **not** — add that if needed.
- Do not log real personnummer.

## Preview limits (library still runs, but not the whole flow)

**Förhandsvisa** reloads **this page only**. Logikhopp, prefills set in the previous page’s `GetNextPage`, and **tabellfält** are not testable there. **Visa skriptlogg** shows `Log*`.
