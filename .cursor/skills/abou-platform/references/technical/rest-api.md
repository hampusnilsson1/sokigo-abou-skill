# Abou REST API

External systems call **Abou REST API V2**. This file is the method map. Payloads, entities, C# samples, version history, and notes that mark errors in Sokigo's original PDF are in the [full REST reference](abou-rest-api-v2.4.4.md). Copy URLs, verbs, and property names from that file. Do not invent methods or fields.

Source: Sokigo *Abou REST API v2.4.4* (original file *Abou REST API v2_4_4*, 55 pages; created 2025-02-18, modified 2025-03-07). A Confluence ingest on 2026-08-25 labeled a PDF "version 2.5.2" and stored only method names. That version label is **not** in the verified document. Do not add methods from it.

Not this API:

- Python **Adapter REST** / `IRestWrapperServiceFactory` (named sysadmin config inside an e-tjänst) — [Adapter REST](../../../build-abou-etjanst-web/references/integrations/adapter-rest.md).
- `self.Citizen` / [CitizenInfo](citizeninfo.md), and Razor `@Model` / [HtmlCaseModel](htmlcasemodel.md).

Example host `https://abou.sokigo.com/api` is fictional. Ask Sokigo support for the real base URL and test credentials. Do not send the user to the wiki.

## When to use it

Use it when an external system must read or change Abou data: case lists and detail, status, diarienummer, handläggare, invånare, files, create a case, direktmeddelande, komplettering, beslut, fältsvar, API version, ärendestatistik, published e-tjänster, or register import.

Read methods need e-tjänst right **Enbart läsbehörighet** (the Läs column under Behörigheter). Updates need **Statusuppdaterare**. Decisions need **Beslutsfattare**. Three system rights are named in the PDF and are not in the wiki systembehörighet table: **Hämta ärendestatistik**, **Hämta e-tjänster**, **Importera register**.

## Auth

From Abou **2021.8** there are two options. Sokigo recommends the token.

API users are administered under **Behörigheter → API-användare** (användarnamn, API-nyckel, checkbox **Kräv tokenbaserad anslutning**).

### Token (preferred)

1. `GET /api/authenticate` or `GET /api/authenticate/{ServiceShortName}`.
2. Header: `Authorization: Basic ` + Base64(`UserName:ApiKey`).
3. The body of HTTP 200 is a JWT. 401 = unauthorized, 500 = server error.
4. Send `Authorization: Bearer <token>` on every later call.
5. If the later call includes `ServiceShortName`, fetch the token **with** that short name.

Token mode requires **Kräv tokenbaserad anslutning** on the API user.

### API key (older)

`username` and `apikey` as query parameters in clear text, for example `.../cases/UpdateStatus?username=userName&apikey=apiKey`. Turn **off** **Kräv tokenbaserad anslutning** for that user.

## Methods

28 methods plus Authenticate. `{serviceShortName}` is the e-tjänst kortnamn. Most case methods are under `/api/v2/services/{serviceShortName}/cases/`.

| Method | Verb | Path | Right |
| --- | --- | --- | --- |
| Authenticate | GET | `/api/authenticate` or `/api/authenticate/{ServiceShortName}` | Basic (UserName:ApiKey) |
| UpdateStatus | PUT | `.../cases/UpdateStatus` | Statusuppdaterare |
| UpdateDiaryNumber | PUT | `.../cases/UpdateDiaryNumber` | Statusuppdaterare |
| UpdateAdministrator | PUT | `.../cases/UpdateAdministrator` | Statusuppdaterare |
| AddCitizens | PUT | `.../cases/AddCitizens` | Statusuppdaterare |
| FileUpload | POST | `.../cases/FileUpload` | Statusuppdaterare |
| GetByDateAndState | POST | `.../cases/GetByDateAndState` | Enbart läsbehörighet |
| GetByDate | POST | `.../cases/GetByDate` | Enbart läsbehörighet |
| GetByState | POST | `.../cases/GetByState` | Enbart läsbehörighet |
| GetByDateTimeAndState | POST | `.../cases/GetByDateTimeAndState` | Enbart läsbehörighet |
| GetDetailed | POST | `.../cases/GetDetailed` | Enbart läsbehörighet |
| CasePdfDownload | POST | `.../cases/CasePdfDownload` | Enbart läsbehörighet |
| DecisionPdfDownload | POST | `.../cases/DecisionPdfDownload` | Enbart läsbehörighet |
| AttachmentDownload | POST | `.../cases/AttachmentDownload` | Enbart läsbehörighet |
| CreateCase | POST | `.../cases/CreateCase` | Statusuppdaterare |
| NewDirectMessage | PUT | `.../cases/NewDirectMessage` | Statusuppdaterare |
| GetCaseListFromUserIdentity | GET | `.../cases/GetCaseListFromUserIdentity?userIdentity={userIdentity}` | Enbart läsbehörighet |
| RequestSupplementExistingCase | POST | `.../cases/RequestSupplementExistingCase` | Statusuppdaterare |
| RequestSupplementNewCase | POST | `.../cases/RequestSupplementNewCase` | Statusuppdaterare |
| CancelSupplement | POST | `.../cases/CancelSupplement` | Statusuppdaterare |
| CancelAllSupplements | POST | `.../cases/CancelAllSupplements` (URL example in the PDF: `CancelAllSupplement`) | Statusuppdaterare |
| DecisionOnExistingCase | POST | `.../cases/DecisionOnExistingCase` | Beslutsfattare |
| DecisionToNewCase | POST | `.../cases/DecisionToNewCase` | Beslutsfattare |
| UpdateFieldAnswers | PUT | `.../cases/UpdateFieldAnswers` | Statusuppdaterare |
| GetVersion | GET | `/api/v2/services/cases/GetVersion` | (none stated) |
| GetCaseStatistics | GET | `.../cases/GetCaseStatistics` | System: Hämta ärendestatistik |
| SearchServices | GET | `/api/v2/services/SearchServices?Searchstring={query}` | (none stated) |
| GetServices | POST | `/api/v2/services/GetServices` | System: Hämta e-tjänster |
| ImportRegister | PUT | `/api/v2/registers/ImportRegister` | System: Importera register |

`...` means `/api/v2/services/{serviceShortName}`.

Case lists return ärendenummer. **GetDetailed** returns the case as XML (or JSON if `Accept: application/json`). Attachment **Content is empty** in that response; use CasePdfDownload, DecisionPdfDownload, or AttachmentDownload (SystemFileName from GetDetailed). **FileUpload** is multipart (`CaseBaseRequest` plus one part per file), not a single JSON body. **ImportRegister** creates a register or overwrites one with the same SystemName and can couple it to e-tjänster. UI CSV import is a separate path and uses systembehörighet **Administrera Register**.

Komplettering and beslut can pass Arguments (`ConfigurationDataKey`, `ServicePurpose`, optional `IncludeCaseParameters`) so **RestwrapperPlugin** calls another system when the citizen completes the supplement or downloads the decision the first time. The plugin and its configuration must already exist.

## Entities

Property tables are only in the reference: RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse.

`*` in the Obl column means strictly required. `-` means required only in the case the description states.

## Errors kept from the original PDF

The reference quotes the PDF and marks mistakes. Do not "correct" them when copying an example. The ones that change a call:

- **CancelAllSupplements.** The URL example ends with `CancelAllSupplement` (no final s). Version history: new in API 2.4.4, Abou **2025.3**. The method table says Abou release **2023.2.0.0**.
- **AttachmentDownload.** The method path is `.../cases/AttachmentDownload`. The C# sample calls `.../cases/CaseAttachmentDownload`.
- **UpdateFieldAnswers** sample JSON is missing commas after `Comment` and `Answer`.
- **GetServices** result sample uses `=` instead of `:`. **SearchServices** result sample has a trailing comma.
- **GetDetailed** contents list says attachments include Content; the method text says they do not. In the data block, OmitXmlDeclaration is marked `(5` and described by footnote 6. Property name in the PDF: `IncludeAllAttachements`.
- **CreateCase** repeats the sentence "När man hämtar ett detaljerat ärende…".
- **DoPublishPdf** on CaseUpdateFieldAnswersRequest stops mid-sentence ("…genereras på nytt för att").
- Title-page footer says **2.4.3**; the title says **2.4.4**.
- C# samples keep original typos (`URI.EscapeDataString`, doubled parentheses, `stringContents` in GetByDateAndState).

## C# and testing

The reference has .NET `HttpClient` + Newtonsoft.Json samples (token, FileUpload, the read/update methods, CreateCase). The PDF says to try calls with Postman or the Chrome extension YARC. Bearer examples use the token from Authenticate.
