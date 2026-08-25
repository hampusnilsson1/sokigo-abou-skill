# Abou REST API

Source: Confluence *Abou REST API* (PDF **version 2.5.2**). Read 2026-08-25. Contact for test endpoints: Sokigo support.

Auth in the PDF: token (`Authenticate`), API key, Bearer examples (.NET). **Do not invent URLs or payloads** — copy from the PDF.

## Methods (from PDF TOC)

### Auth
- Hämta token / Authenticate
- API-nyckel
- Bearer token

### Update case
| Method | Purpose |
| --- | --- |
| `UpdateStatus` | Status |
| `UpdateDiaryNumber` | Diarienummer |
| `UpdateAdministrator` | Handläggare |
| `AddCitizens` | Medsökande / invånare on the case |
| `FileUpload` | Attach files |
| `CreateCase` | New case |
| `NewDirectMessage` | Direktmeddelande |
| `UpdateFieldAnswers` | Fältsvar on an existing case |

### Read
| Method | Purpose |
| --- | --- |
| `GetByDateAndState` | Case numbers in date range + status |
| `GetByDate` | Date range |
| `GetByState` | One or more statuses |
| `GetByDateTimeAndState` | Status-change window (with clock) + status |
| `GetDetailed` | One detailed case (including attachments/content) |
| `GetCaseListFromUserIdentity` | Case numbers for a personnummer |
| `CasePdfDownload` | Case PDF |
| `DecisionPdfDownload` | Decision PDF |
| `AttachmentDownload` | One attachment |

### Komplettering
| Method | Purpose |
| --- | --- |
| `RequestSupplementExistingCase` | Supplement on a case that exists in Abou |
| `RequestSupplementNewCase` | Supplement when the case is not in Abou |
| `CancelSupplement` | Drop one pending supplement |
| `CancelAllSupplements` | Drop all pending |

### Beslut
| Method | Purpose |
| --- | --- |
| `DecisionOnExistingCase` | Decision on an existing case |
| `DecisionToNewCase` | Decision when the case is not in Abou |

Plus a method to read the current API version.

## Entity names in the PDF (from TOC)

RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse.

Do not invent property lists for these.
