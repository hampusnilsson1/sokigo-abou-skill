---
title: "Abou REST API 2.4.4"
source_file: "source.pdf"
original_document: "Abou REST API v2_4_4.docx"
version: "2.4.4"
vendor: "Sokigo AB"
product: "Abou"
document_type: "REST API-dokumentation"
language: "sv"
created: "2025-02-18"
modified: "2025-03-07"
authors: ["Jonas von Geijer", "tom.ilestrand@sokigo.com"]
---

# Abou REST API 2.4.4

Dokumentation från Sokigo AB (Addnode Group) av Abous REST API V2, version 2.4.4. Titelsidan har rubriken ”Abous REST API 2.4.4” och visar Sokigos logotyp (SOKIGO, ADDNODE GROUP). Sidfoten på titelsidan anger ”Abou REST API 2.4.3” samt ”Sokigo AB sokigo.com/vara-produkter/abou info@sokigo.com”.

## Innehåll

- Versionering
- Inledning
- Autentisering (Tokenbaserad autentisering, Hämta token Authenticate, Autentisering med API-nyckel)
- Snabböversikt över API-metoder
- UpdateStatus – Uppdatera status för ett ärende
- UpdateDiaryNumber – Uppdatera diarienummer för ett ärende
- UpdateAdministrator – Uppdatera handläggare för ett ärende
- AddCitizens – Uppdatera ärende med invånare
- FileUpload – Bifoga filer till ett ärende
- GetByDateAndState – Hämta ärendenummer inom ett datumintervall och status
- GetByDate – Hämta ärendenummer inom ett datumintervall
- GetByState – Hämta ärendenummer för ett eller flera status
- GetByDateTimeAndState – Hämta ärendenummer med statusuppdatering inom ett datumintervall med klockslag och status
- GetDetailed – Hämta ett detaljerat ärende (inkl. Bilagor och dess innehåll, Content)
- CasePdfDownload – Hämta ärende-PDF
- DecisionPdfDownload – Hämta ett ärendes besluts-PDF
- AttachmentDownload – Hämta en specifik bilaga från ett ärende
- CreateCase – Skapa nytt ärende
- NewDirectMessage – Skapa direktmeddelande
- GetCaseListFromUserIdentity – Hämta en lista av ärendenummer för ett personnummer
- Begäran om komplettering (RequestSupplementExistingCase, RequestSupplementNewCase, CancelSupplement, CancelAllSupplements)
- Delgivning av beslut (DecisionOnExistingCase, DecisionToNewCase)
- UpdateFieldAnswers – Uppdatera fältsvar på ett befintligt ärende
- GetVersion – Hämta befintlig version av Abou API
- GetCaseStatistics – Hämta ärendestatistik för en specifik e-tjänst
- SearchServices – Söka bland publicerade e-tjänster
- GetServices – Hämta information för en specifik e-tjänst
- ImportRegister – Import register
- Entiteter (RequestSupplementRequest, CancelSupplementRequest, CaseDecisionRequest, CitizenRequest, ServiceOrganisationRequest, ImportRegisterRequest, FieldArgument, FileData, CaseUpdateFieldAnswersRequest, FieldRequest, IntegrationResponse, IntegrationObjectResponse)
- Kodexempel för att anropa Abous REST API, .Net C#
- Testa REST API
- Att använda RestwrapperPluginet via REST-API

## Versionering (versionshistorik för Abou REST API)

Versionshistorik för Abou REST API från version 2.1 till 2.4.4, med release av Abou som ändringen gäller från och ansvarig person.

| Händelse | Version av API | Förändring | Fr.o.m. rel. av Abou | Ansvarig |
|---|---|---|---|---|
| Upprättat | 2.1 | API’t utökat med följande metoder: AddCitizens, GetByDateAndState, GetByDate, GetByState, GetDetailed, CasePdfDownload, DecisionPdfDownload, AttachmentDownload, CreateCase samt GetCaseListFromUserIdentity. | 3.26.1541.0 | Jonas von Geijer |
| Justering | 2.1.1 | Metod CreateCase utökad med parameter för att kunna ange att publicering till integration-plugins skall ske. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.1 | Beskrivning av FileUpload korrigerad i denna dokumentation. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.1 | Produktnamnet Automaten ersatt med Abou och företagsnamnet Abou ersatt med Sokigo i denna dokumentation. | 3.30.1607.1 | Jonas von Geijer |
| Justering | 2.1.2 | Notifiering sker via NotifyByWhenToSendEmail vilken även tar hänsyn till eventuell typ av kontakt användaren gjort i ärendet mha kontaktfältet | 2018.6.0 | Jonas von Geijer |
| Justering | 2.1.3 | Unescaping på filnamnet i FileUpload för att hantera ovanliga tecken | 2019.2.0 | Arnar Gardarsson |
| Justering | 2.1.4 | GetByDate, GetByState och GetByDateAndState supporterar filter för fältsvar | 2019.2.6 | Jonas von Geijer |
| Justering | 2.1.5 | Utökat attribut, FileDescription, i payload till FileUpload. Hämta version av API | 2019.5.0 | Jonas von Geijer |
| Utökning | 2.2.0 | Begäran om komplettering och Delgivning av beslut | 2019.8.0 | Jonas von Geijer |
| Utökning | 2.2.1 | Begäran om komplettering utökad med Subject.<br>Begäran om komplettering och Delgivning av beslut utökad med Kontakttyp | 2019.8.4 | Jonas von Geijer |
| Dok.rev. | 2.2.1 A | Förtydligande angående bilagors innehåll i GetDetailed | NA | Jonas von Geijer |
| Dok.rev. | 2.2.1 B | Förtydligande angående Entiteter och obligatoriska argument | NA | Jonas von Geijer |
| Utökning | 2.2.2 | Ny metod för att uppdatera fältsvar | 2020.2.16 | Jonas von Geijer |
| Justering | 2.2.3 | Begäran om komplettering refaktoriserad för att hantera ny funktionalitet för kompletteringsbegäran | 2021.2.0 | Jonas von Geijer |
| Justering | 2.2.3 | FileUpload kan nu sätta filtyp, filbeskrivning och läskvitto per fil | 2021.2.0 | Tom Ilestrand |
| Utökning | 2.2.4 | Hämta ärendestatistik för en specifik e-tjänst | 2021.5.0 | Tom Ilestrand |
| Justering | 2.2.5 | Begäran om komplettering kan nu ta emot en instruktionsbilaga | 2021.5.0 | Nicklas Nordahl |
| Justering | 2.2.5 | Söka publicerade e-tjänster och statistik för e-tjänster | 2021.5.0 | Tom Ilestrand |
| Utökning | 2.3.0 | Tokenbaserad autentisering | 2021.8.0 | Jonas von Geijer |
| Justering | 2.3.1 | IntegrationObjectResponse tillagt i metoder det används i och under modeller | 2022.2.0 | Tom Ilestrand |
| Dok. rev. | 2.3.1.A | Dokumentation av den befintliga metoden NewDirectMessage | 2022.3.0 | Dan Hoatson |
| Utökning | 2.3.2 | Ny metod ImportRegister | 2022.8 | Tom Ilestrand |
| Utökning | 2.4.0 | Ny metod CancelSupplement | 2023.2 | Tom Ilestrand |
| Utökning | 2.4.1 | Ny metod GetByDateTimeAndState | 2023.5 | Tom Ilestrand |
| Justering | 2.4.2 | FileUpload skickar nu meddelande för ”När handläggare bifogar fil” | 2024.2 | Tom Ilestrand |
| Justering | 2.4.3 | GetDetailed tar nu emot ett till argument (generatePdf) | 2024.11 | Adam Norman |
| Utökning | 2.4.4 | Ny metod CancelAllSupplements | 2025.3 | Adam Norman |

## Inledning

Detta dokument beskriver möjligheten att integrera med Abou via dess REST API V2.

## Autentisering i Abou REST API

Abou REST API erbjuder fr.o.m. Abou rel. 2021.8 två varianter av autentisering, tokenbaserad eller API-nyckel. Sokigos rekommendation är att använda tokenbaserad autentisering framför API-nyckel.

### Tokenbaserad autentisering (Bearer-token, JWT)

För att kunna anropa Abou API krävs API-användare vilka administreras i Abou Admingränssnitt Behörigheter. (Redan befintliga API-användare behöver inställning ”Kräv tokenbaserad anslutning”.)

Tokenbaserad autentisering innebär att man innan faktiska API-anrop behöver hämta en tidsbegränsad token (krypterad ”nyckel” som baseras på JWT, Json Web Token) som sedan måste skickas med till varje API-anrop i form av en Bearer Authorization Header.

### GET /api/authenticate – Hämta token (Authenticate)

Authenticate hämtar en tidsbegränsad Bearer-token (JWT) för tokenbaserad autentisering mot Abou REST API. Två varianter av sökväg:

```text
…/api/authenticate
…/api/authenticate/ServiceShortName
```

Om vidare API-anrop som ska göras kräver ServiceShortName måste token hämtas med alternativet …/api/authenticate/ServiceShortName.

#### Authenticate – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/authenticate/AAA
```

Authenticate kräver Basic Authorization Header vilken består av UserName (registrerat användarnamn för aktuell API-användare i Abou) och ApiKey (registrerad API-nyckel för aktuell API-användare i Abou). Själva värdet för Basic Authorization Header skapas enligt:

```text
"Basic " + Base64Encoded(UserName:ApiKey)
```

#### Authenticate – Verb och headers vid anrop

| | |
|---|---|
| Verb | GET |
| Header | Authorization: Basic … |

#### Authenticate – Svar (response)

Svar från Authenticate (GET /api/authenticate): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 401 | Unauthorized (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError |

Exempel på token i response (i originalet visas tokenens header-del i fetstil och resten i rött):

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJc3MiOiJhYm91IiwiRXhwIjoiMjAyMS0wOC0yM1QwODowMjo0NC41NTA4MTQ3WiIsIlNlcnZpY2VTaG9ydE5hbWUiOiJBQk9VMTIzIiwiU3lzdGVtUGVybWlzc2lvbiI6MjQsIlNlcnZpY2VQZXJtaXNzaW9uIjoyNTQsIkN1c29tZXJJZCI6MTAwMn0.xb3NP-WebwIzU5Aa8QM3RTiZtL1k_LsvSp5eDt8bU0I
```

### Autentisering med API-nyckel (username och apikey som URL-parametrar)

Ursprunglig autentisering i Abou REST API är m.h.a. API-nyckel vilket innebär att API-användares användarnamn och nyckel skickas med som url-parametrar i klartext vid anrop. Eftersom tokenbaserad autentisering är säkrare än API-nyckel är Sokigos rekommendation att byta ut autentisering med API-nyckel till tokenbaserad autentisering fr.o.m. Abou rel. 2021.8.

#### Autentisering med API-nyckel – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateStatus?username=userName&apikey=apiKey
```

För att kunna anropa Abou API krävs API-användare vilka administreras i Abou Admingränssnitt Behörigheter. För att använda autentisering m.h.a. API-nyckel behöver man inaktivera inställning ”Kräv tokenbaserad anslutning” för aktuell API-användare.

#### Bild: Behörigheter – inställningen ”Kräv tokenbaserad anslutning” för en API-användare

Skärmbild från Abou Admingränssnitt med rubriken **”Behörigheter - abou”**. Flikar överst: *Användare*, *Grupper*, *API-användare* (vald), *E-tjänster*. Knappar: *Tillbaka*, *Spara*, *Ta bort*. Underflikar: *Användaruppgifter* (vald), *Systembehörigheter*, *E-tjänstebehörigheter*. Formulärfält: *Användarnamn* = ”abou” (ej redigerbart), *Namn* = ”Abous Api-användare”, *Api-nyckel* (maskerat värde, med knapp för att generera ny nyckel), samt kryssrutan **”Kräv tokenbaserad anslutning”** (ikryssad, med hjälpikon), som är inringad med en streckad orange markering.

## Snabböversikt över API-metoder i Abou REST API 2.4.4

Sammanställning av samtliga metoder i dokumentet (verb, sökväg, lägsta behörighet och, där det anges, release av Abou). Basadress i exemplen: `https://abou.sokigo.com/api` (fiktiv URL).

| Metod | Verb | Sökväg | Behörighet | Abou release |
|---|---|---|---|---|
| Authenticate | GET | /api/authenticate respektive /api/authenticate/{ServiceShortName} | Basic Authorization (UserName:ApiKey) | fr.o.m. 2021.8 |
| UpdateStatus | PUT | /api/v2/services/{serviceShortName}/cases/UpdateStatus | Statusuppdaterare |  |
| UpdateDiaryNumber | PUT | /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber | Statusuppdaterare |  |
| UpdateAdministrator | PUT | /api/v2/services/{serviceShortName}/cases/UpdateAdministrator | Statusuppdaterare |  |
| AddCitizens | PUT | /api/v2/services/{serviceShortName}/cases/AddCitizens | Statusuppdaterare |  |
| FileUpload | POST | /api/v2/services/{serviceShortName}/cases/FileUpload | Statusuppdaterare |  |
| GetByDateAndState | POST | /api/v2/services/{serviceShortName}/cases/GetByDateAndState | ”Enbart läsbehörighet” |  |
| GetByDate | POST | /api/v2/services/{serviceShortName}/cases/GetByDate | ”Enbart läsbehörighet” |  |
| GetByState | POST | /api/v2/services/{serviceShortName}/cases/GetByState | ”Enbart läsbehörighet” |  |
| GetByDateTimeAndState | POST | /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState | ”Enbart läsbehörighet” |  |
| GetDetailed | POST | /api/v2/services/{serviceShortName}/cases/GetDetailed | ”Enbart läsbehörighet” |  |
| CasePdfDownload | POST | /api/v2/services/{serviceShortName}/cases/CasePdfDownload | ”Enbart läsbehörighet” |  |
| DecisionPdfDownload | POST | /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload | ”Enbart läsbehörighet” |  |
| AttachmentDownload | POST | /api/v2/services/{serviceShortName}/cases/AttachmentDownload | ”Enbart läsbehörighet” |  |
| CreateCase | POST | /api/v2/services/{serviceShortName}/cases/CreateCase | Statusuppdaterare |  |
| NewDirectMessage | PUT | /api/v2/services/{serviceShortName}/cases/NewDirectMessage | Statusuppdaterare |  |
| GetCaseListFromUserIdentity | GET | /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity?userIdentity={userIdentity} | ”Enbart läsbehörighet” |  |
| RequestSupplementExistingCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementExistingCase | Statusuppdaterare | 2021.2.0.0 |
| RequestSupplementNewCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementNewCase | Statusuppdaterare | 2021.2.0.0 |
| CancelSupplement | POST | /api/v2/services/{SERVICESHORTNAME}/cases/CancelSupplement | Statusuppdaterare | 2023.2.0.0 |
| CancelAllSupplements | POST | /api/v2/services/{SERVICESHORTNAME}/cases/CancelAllSupplement (så skrivet i URL-exemplet) | Statusuppdaterare | 2023.2.0.0 enligt metodtabellen (versionshistoriken anger 2025.3) |
| DecisionOnExistingCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/DecisionOnExistingCase | Beslutsfattare | 2019.8.0.0 |
| DecisionToNewCase | POST | /api/v2/services/{SERVICESHORTNAME}/cases/DecisionToNewCase | Beslutsfattare | 2019.8.0.0 |
| UpdateFieldAnswers | PUT | /api/v2/services/{SERVICESHORTNAME}/cases/UpdateFieldAnswers | Statusuppdaterare | 2020.2.16.0 |
| GetVersion | GET | /api/v2/services/cases/GetVersion | (ingen angiven) | 2019.5.0.0 |
| GetCaseStatistics | GET | /api/v2/services/{ServiceShortName}/cases/GetCaseStatistics | Systembehörighet: Hämta ärendestatistik | 2021.5.0.0 |
| SearchServices | GET | /api/v2/services/SearchServices?Searchstring={query} | (ingen angiven) | 2021.5.0.0 |
| GetServices | POST | /api/v2/services/GetServices | Systembehörighet: Hämta e-tjänster | 2021.5.0.0 |
| ImportRegister | PUT | /api/v2/registers/ImportRegister | Systembehörighet: Importera register | 2022.8.0.0 |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus – Uppdatera status för ett ärende (UpdateStatus)

UpdateStatus sätter en ny status på ett ärende i Abou, identifierat med UniqueId eller DiaryNumber, och kan skicka notifiering till invånaren.

### UpdateStatus – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateStatus
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateStatus – Verb, headers och parametrar vid anrop

Anrop till UpdateStatus (PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus).
När man uppdaterar status måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "State": "Status på ärendet som ska sättas" (3,
 "DisableSendNotification": true/false (4
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `State`.

Fotnoter till datablocket för UpdateStatus:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Obligatorisk.
4. Boolean, anger om Abou skall skicka notifiering till invånaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### UpdateStatus – Svar (response)

Svar från UpdateStatus (PUT /api/v2/services/{serviceShortName}/cases/UpdateStatus): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber – Uppdatera diarienummer för ett ärende (UpdateDiaryNumber)

UpdateDiaryNumber sätter anropande systems diarienummer (DiaryNumber) på ett ärende i Abou. (Meningen om Comment i fotnot 2 står två gånger i originalet.)

### UpdateDiaryNumber – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateDiaryNumber
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateDiaryNumber – Verb, headers och parametrar vid anrop

Anrop till UpdateDiaryNumber (PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber).
När man uppdaterar diarienummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "DisableSendNotification": true/false (3,
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för UpdateDiaryNumber:

1. Obligatorisk.
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Boolean, anger om Abou skall skicka notifiering till invånaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### UpdateDiaryNumber – Svar (response)

Svar från UpdateDiaryNumber (PUT /api/v2/services/{serviceShortName}/cases/UpdateDiaryNumber): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator – Uppdatera handläggare för ett ärende (UpdateAdministrator)

UpdateAdministrator sätter ny handläggare (Administrator) på ett ärende i Abou och kan notifiera den nya handläggaren, valfritt med ärendets bifogade filer.

### UpdateAdministrator – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/UpdateAdministrator
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### UpdateAdministrator – Verb, headers och parametrar vid anrop

Anrop till UpdateAdministrator (PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator).
När man uppdaterar handläggare måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "Administrator": "Handläggare på ärendet som ska sättas" (3,
 "DisableSendNotification": true/false (4,
 "IncludeCaseAttachmentsInNotification": true/false (5
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för UpdateAdministrator:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
3. Obligatorisk.
4. Boolean, anger om Abou skall skicka notifiering till nya handläggaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.
5. Boolean, anger om ärendets bifogade filer skall ingå i notifiering till nya handläggaren.

### UpdateAdministrator – Svar (response)

Svar från UpdateAdministrator (PUT /api/v2/services/{serviceShortName}/cases/UpdateAdministrator): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## PUT /api/v2/services/{serviceShortName}/cases/AddCitizens – Uppdatera ärende med invånare (AddCitizens)

AddCitizens lägger till invånare (Citizen-objekt med UserIdentity, FirstName, LastName, Email) på ett befintligt ärende i Abou.

### AddCitizens – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/AddCitizens
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### AddCitizens – Verb, headers och parametrar vid anrop

Anrop till AddCitizens (PUT /api/v2/services/{serviceShortName}/cases/AddCitizens).
När man uppdaterar invånare måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Citizens": Lista med Citizen-objekt (2,
 "OmitSocialSecurityNumberValidation": true/false (3,
 "UpdateExisting": true/false (4,
 "Actor": "Anropande systems namn" (5,
 "Comment": "Kommentar" (5,
 "DisableSendNotification": true/false (6
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Citizens`, `Actor`, `Comment`.

Fotnoter till datablocket för AddCitizens:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk lista enligt:<br>`[{"UserIdentity":"Personnummer eller annan unik identifierare", "FirstName":"Förnamn","LastName":"Efternamn", "Email":"E-postadress"},{…}]`.
3. Boolean, anger om personnummervalidering skall utföras på UserIdentity för varje Citizen.
4. Boolean, anger om redan befintlig Citizen’s värden skall uppdateras.
5. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).<br>Vill man att Comment ska ingå i notifiering måsta meddelandemallen innehålla token (värde) Comment.
6. Boolean, anger om Abou skall skicka notifiering till nya handläggaren.<br>Anges en i e-tjänsten okänd status skickas <u>ingen</u> notifiering.

### AddCitizens – Svar (response)

Svar från AddCitizens (PUT /api/v2/services/{serviceShortName}/cases/AddCitizens): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## POST /api/v2/services/{serviceShortName}/cases/FileUpload – Bifoga filer till ett ärende (FileUpload)

FileUpload bifogar en eller flera filer till ett ärende i Abou via multipart-anrop. Ärendeinformationen skickas som en JSON-del (i kodexemplet med namnet CaseBaseRequest) och varje fil som en del med namnet file.

### FileUpload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/FileUpload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### FileUpload – Verb, headers och parametrar vid anrop

Anrop till FileUpload (POST /api/v2/services/{serviceShortName}/cases/FileUpload).
När man bifogar fil till ett ärende måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Multi Part Content (3 |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
 "FileDescription": "Eventuell beskrivning av filen",
 "DisableSendNotification": true/false (4
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `FileDescription`.

Fotnoter till datablocket för FileUpload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Filtyp, fildefinition och läskvitto sätts genom att sätta header fileDefinition, fileDescription respektive useReceipt under filens Content-Disposition. För läskvittot används värdet true. Se kodexempel för mer information (avsnittet ”Kodexempel C# – FileUpload med Bearer Token”).
4. Boolean, anger om Abou skall skicka notifiering för händelse ”När handläggare bifogar fil” om sådan finns konfigurerad i e-tjänsten.

### FileUpload – Svar (response)

Svar från FileUpload (POST /api/v2/services/{serviceShortName}/cases/FileUpload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 400 | Bad Request (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 415 | Unsupported Media Type (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

## POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState – Hämta ärendenummer inom ett datumintervall och status (GetByDateAndState)

GetByDateAndState returnerar Abous unika ärendenummer för ärenden inskickade inom ett datumintervall och med angivna statusar, valfritt filtrerat på fältsvar.

### GetByDateAndState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDateAndState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDateAndState – Verb, headers och parametrar vid anrop

Anrop till GetByDateAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum" (1,
 "ToDate": "Till och med datum" (2,
 "States": Lista med strängar (3,
 "ExcludeCasesWithDiaryNumber": true/false (4,
 "Field": Ett Field-objekt (5
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`, `States`.

Fotnoter till datablocket för GetByDateAndState:

1. Obligatorisk. Ärenden inskickade fr.o.m. datum omfattas.
2. Obligatorisk. Ärenden inskickade t.o.m. omfattas.
3. Obligatorisk. Ärendestatusar som ska omfattas.<br>`"States": ["status1", "status2"]`
4. Om diarieförda ärenden skall uteslutas.
5. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDateAndState – Svar (response)

Svar från GetByDateAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateAndState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByDate – Hämta ärendenummer inom ett datumintervall (GetByDate)

GetByDate returnerar Abous unika ärendenummer för ärenden inskickade inom ett datumintervall, valfritt filtrerat på fältsvar.

### GetByDate – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDate
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDate – Verb, headers och parametrar vid anrop

Anrop till GetByDate (POST /api/v2/services/{serviceShortName}/cases/GetByDate).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum" (1,
 "ToDate": "Till och med datum" (2,
 "ExcludeCasesWithDiaryNumber": true/false (3,
 "Field": Ett Field-objekt (4
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`.

Fotnoter till datablocket för GetByDate:

1. Obligatorisk. Ärenden inskickade fr.o.m. datum omfattas.
2. Obligatorisk. Ärenden inskickade t.o.m. omfattas.
3. Om diarieförda ärenden skall uteslutas.
4. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDate – Svar (response)

Svar från GetByDate (POST /api/v2/services/{serviceShortName}/cases/GetByDate): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150810-AAA-WM56","150810-AAA-PI19","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByState – Hämta ärendenummer för ett eller flera status (GetByState)

GetByState returnerar Abous unika ärendenummer för ärenden med en eller flera angivna statusar, valfritt filtrerat på fältsvar.

### GetByState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByState – Verb, headers och parametrar vid anrop

Anrop till GetByState (POST /api/v2/services/{serviceShortName}/cases/GetByState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "States": Lista med strängar (1,
 "ExcludeCasesWithDiaryNumber": true/false (2,
 "Field": Ett Field-objekt (3
}
```

I originalet är följande fältnamn fetmarkerade: `States`.

Fotnoter till datablocket för GetByState:

1. Obligatorisk. Ärendestatusar som ska omfattas.<br>`"States": ["status1", "status2"]`
2. Om diarieförda ärenden skall uteslutas.
3. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByState – Svar (response)

Svar från GetByState (POST /api/v2/services/{serviceShortName}/cases/GetByState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150810-AAA-WM56","150810-AAA-PI19","150907-AAA-UL67"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState – Hämta ärendenummer med statusuppdatering inom ett datumintervall med klockslag och status (GetByDateTimeAndState)

GetByDateTimeAndState returnerar ärendenummer för ärenden vars status uppdaterats inom ett intervall med datum och klockslag. Här är States inte obligatorisk (saknas/null/tom = ingen statusfiltrering). Ny metod i API 2.4.1 (Abou 2023.5).

### GetByDateTimeAndState – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetByDateTimeAndState
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetByDateTimeAndState – Verb, headers och parametrar vid anrop

Anrop till GetByDateTimeAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState).
När man hämtar (söker) ärendenummer måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "FromDate": "Från och med datum med klockslag" (1,
 "ToDate": "Till och med datum med klockslag" (2,
 "States": Lista med strängar (3,
 "ExcludeCasesWithDiaryNumber": true/false (4,
 "Field": Ett Field-objekt (5
}
```

I originalet är följande fältnamn fetmarkerade: `FromDate`, `ToDate`.

Fotnoter till datablocket för GetByDateTimeAndState:

1. Obligatorisk. Ärenden med uppdaterad status fr.o.m. datum med klockslag omfattas.
2. Obligatorisk. Ärenden med uppdaterad status t.o.m. datum med klockslag omfattas.<br>`”ToDate”:” 2023-04-21 14:03:09”`
3. Ärendestatusar som ska omfattas. Om listan saknas, är null eller tom kommer ingen filtrering på status att ske.<br>`"States": ["status1", "status2"]`
4. Om diarieförda ärenden skall uteslutas.
5. Inkludera även filtrering på fältsvar:<br>`"Field": { "Answer": "fältets svar", "Argument": { "Name": "integrationsargumentets namn för fältet", "Value": "integrationsargumentets värde för fältet " } }`

### GetByDateTimeAndState – Svar (response)

Svar från GetByDateTimeAndState (POST /api/v2/services/{serviceShortName}/cases/GetByDateTimeAndState): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: IEnumerable<string> (JSON objekt) med Abous unika ärendenummer, t.ex:

```json
["150527-AAA-UI91","150907-AAA-LJ11"]
```

## POST /api/v2/services/{serviceShortName}/cases/GetDetailed – Hämta ett detaljerat ärende (GetDetailed)

GetDetailed hämtar ett komplett ärende (fält, bilagors metadata, statusar m.m.) som XML eller JSON; bilagornas innehåll levereras inte. I originalets datablock är OmitXmlDeclaration märkt `(5` men beskrivs av fotnot 6. Argumentet GeneratePdf tillkom i API 2.4.3.

### GetDetailed – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetDetailed
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetDetailed – Verb, headers och parametrar vid anrop

Anrop till GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed).
När man hämtar ett detaljerat ärende måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "IncludeAllFields": true/false (3,
 "IncludeAllAttachements": true/false (4,
 "XmlGeneratorType": "Typ av XML" (5,
 "OmitXmlDeclaration": true/false (5,
 "GeneratePdf":true/false(7
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `XmlGeneratorType`.

Fotnoter till datablocket för GetDetailed:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Boolean, om alla fält skall omfattas eller endast fält angivna för integration.
4. Boolean, om alla bifogade filler skall omfattas eller endast bifogade i fält angivna för integration.
5. Obligatorisk. Vilken typ av XML ärendet genereras som,<br>`Abou.Calamare.Framework.Integration.Xml.Default.DefaultXmlCaseGenerator` eller<br>`Abou.Calamare.Framework.Integration.Xml.ByggRGenerator.ByggRXmlCaseGenerator`.
6. Boolean, om xml-deklaration skall infogas initialt i xml’en.
7. Boolean, Styr om ärendepdf ska genereras och metadata om ärendepdfen ska hämtas. Default false.

### GetDetailed – Svar (response)

Svar från GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

### GetDetailed – Bilagor och dess innehåll, Content

Gäller svaret från GetDetailed (POST /api/v2/services/{serviceShortName}/cases/GetDetailed).

GetDetailed leverar inte bilagornas innehåll i svaret, dvs

```xml
<Case><Attachments><Attachment><Content /></Attachment></Attachments></Case>
```

För att hämta bilagors innehåll se CasePdfDownload, DecisionPdfDownload och AttachmentDownload.

Data:

- Content type: application/xml (om “Accept: application/json” anges i request header svaret som json)
- Content: String. T.ex. (i originalet en sammanhängande XML-sträng; här indenterad för läsbarhet):

```xml
<Case xmlns="urn:abou:documents:ka:Case">
  <Id>160309-FFS-LF53</Id>
  <DiaryNumber>74271</DiaryNumber>
  <DateSubmitted>2016-03-09T07:58:42.8770000</DateSubmitted>
  <SentInAs>Citizen</SentInAs>
  <RequiresMultipleSignatures>false</RequiresMultipleSignatures>
  <Status>Pågående</Status>
  <ServiceId>FFS</ServiceId>
  <ServiceName>Felanmälan</ServiceName>
  <ServiceVersion>22</ServiceVersion>
  <ServiceStatuses>
    <ServiceStatus>Inkommet</ServiceStatus>
    <ServiceStatus>Under handläggning</ServiceStatus>
    <ServiceStatus>Avslutat</ServiceStatus>
  </ServiceStatuses>
  <Citizens/>
  <Signatures/>
  <Payments/>
  <QueueItems/>
  <Fields>
    <Field>
      <Id>U.37.2.3</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[vattenläcka?trädgårdsvägen /
Moränvägen]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.6</Id>
      <TypeOfField>EGovDateChooserField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[2016-03-09 07:59:23]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.2</Id>
      <TypeOfField>EGovDropDownField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[Gatuunderhåll]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.9</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[59,4567348;18,0408177]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.4</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[Trädgårdsvägen1]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.7</Id>
      <TypeOfField>EGovFileUploadField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[image1.png]]></Answer>
      <Arguments/>
    </Field>
    <Field>
      <Id>U.37.2.10</Id>
      <TypeOfField>EGovTextField</TypeOfField>
      <Question><![CDATA[]]></Question>
      <Answer><![CDATA[<a target="_blank" href="http://maps.google.se/maps?q=59.4567348,18.0408177&z=17&ll=59.4567348,18.0408177">Visa på karta</a>]]></Answer>
      <Arguments/>
    </Field>
  </Fields>
  <Attachments>
    <Attachment>
      <Type>CasePdf</Type>
      <FileName>160309-FFS-LF53.pdf</FileName>
      <SystemFileName/>
      <FileType>application/pdf</FileType>
      <FileDescription>Ärendebilaga</FileDescription>
      <DateUploaded>2016-03-09T07:58:42.8770000</DateUploaded>
      <FileSize>63361</FileSize>
      <Content/>
      <FieldId/>
      <Arguments/>
    </Attachment>
    <Attachment>
      <Type>Attachment</Type>
      <FileName>image1.png</FileName>
      <SystemFileName>160309-FFS-LF53_Bifoga_bild.png</SystemFileName>
      <FileType>image/jpeg</FileType>
      <FileDescription>Bifoga bild</FileDescription>
      <DateUploaded>2016-03-09T07:58:42.0000000</DateUploaded>
      <FileSize>790094</FileSize>
      <Content/>
      <FieldId/>
      <Arguments/>
    </Attachment>
  </Attachments>
  <Supplements/>
</Case>
```

## POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload – Hämta ärende-PDF (CasePdfDownload)

CasePdfDownload hämtar ärendets PDF (ärende-PDF) som binärdata.

### CasePdfDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/CasePdfDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### CasePdfDownload – Verb, headers och parametrar vid anrop

Anrop till CasePdfDownload (POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload).
När man hämtar en ärende-PDF måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för CasePdfDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).

### CasePdfDownload – Svar (response)

Svar från CasePdfDownload (POST /api/v2/services/{serviceShortName}/cases/CasePdfDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload – Hämta ett ärendes besluts-PDF (DecisionPdfDownload)

DecisionPdfDownload hämtar ett ärendes besluts-PDF som binärdata.

### DecisionPdfDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/DecisionPdfDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### DecisionPdfDownload – Verb, headers och parametrar vid anrop

Anrop till DecisionPdfDownload (POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload).
När man hämtar en besluts-PDF-bilaga måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`.

Fotnoter till datablocket för DecisionPdfDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).

### DecisionPdfDownload – Svar (response)

Svar från DecisionPdfDownload (POST /api/v2/services/{serviceShortName}/cases/DecisionPdfDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload – Hämta en specifik bilaga från ett ärende (AttachmentDownload)

AttachmentDownload hämtar en specifik bilaga från ett ärende som binärdata. Bilagan anges med SystemFileName (finns i GetDetailed-svaret). Observera att kodexemplet i dokumentet anropar sökvägen …/cases/CaseAttachmentDownload.

### AttachmentDownload – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/AttachmentDownload
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### AttachmentDownload – Verb, headers och parametrar vid anrop

Anrop till AttachmentDownload (POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload).
När man hämtar en bilaga måste man skicka med information som JSON.

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "Actor": "Anropande systems namn" (2,
 "Comment": "Kommentar" (2,
 "SystemFileName": "Specifikt filnamn" (3
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `Actor`, `Comment`, `SystemFileName`.

Fotnoter till datablocket för AttachmentDownload:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk. (Actor och Comment kommer att skrivas till ärendets historik i Abou).
3. Obligatorisk. Bilagans specifika filnamn i Abou.

### AttachmentDownload – Svar (response)

Svar från AttachmentDownload (POST /api/v2/services/{serviceShortName}/cases/AttachmentDownload): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/octet-stream
- Content: Byte[]

## POST /api/v2/services/{serviceShortName}/cases/CreateCase – Skapa nytt ärende (CreateCase)

CreateCase skapar ett nytt ärende i en e-tjänst i Abou. Fältsvar kopplas till fält via fältens integrationsargument (Name/Value). Giltiga värden för SentInAs: Citizen, Company, Organisation (övriga hanteras som Unknown).

### CreateCase – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/CreateCase
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.
- Kräver att aktuella fält i e-tjänsten har konfigurerats med Integrationsargument.

### CreateCase – Verb, headers och parametrar vid anrop

Anrop till CreateCase (POST /api/v2/services/{serviceShortName}/cases/CreateCase).
När man hämtar ett detaljerat ärende måste man skicka med information som JSON. (Så formulerat i originalet, trots att avsnittet gäller CreateCase.)

| | |
|---|---|
| Verb | POST |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "Fields": Lista med Field-objekt (1,
 "Citizen": "Citizenobjekt" (2,
 "OmitSocialSecurityNumberValidation": true/false (3,
 "UpdateExistingCitizen": true/false (4,
 "SentInAs": "Typ av invånare" (5,
 "SignatureData": "Signeringsdata" (6,
 "SignatureIssuer": "Utgivare av signering" (7,
 "Actor": "Anropande systems namn" (8,
 "Comment": "Kommentar" (8,
 "EnablePublishToPlugin": true/false (9
}
```

I originalet är följande fältnamn fetmarkerade: `Fields`, `Citizen`, `SentInAs`, `SignatureData`, `SignatureIssuer`, `Actor`, `Comment`.

Fotnoter till datablocket för CreateCase:

1. Obligatorisk lista enligt:<br>`[{"Answer":"Fältsvar", "Arguments":[{"Name":"Fältets specifika argumentnamn", "Value":" Fältets specifika argumentvärde"}, {…}]}, {…}]`
2. Obligatorisk **om** aktuell e-tjänst kräver inloggning/signering, Citizen:<br>`{"UserIdentity":"Personnummer eller annan unik identifierare", "FirstName":"Förnamn","LastName":"Efternamn", "Email":"E-postadress"}`.
3. Boolean, anger om personnummervalidering skall utföras på UserIdentity för Citizen.
4. Boolean, anger om redan befintlig Citizen’s värden skall uppdateras.
5. Obligatorisk **om** aktuell e-tjänst kräver inloggning/signering, använd någon av följande typer: ”Citizen”, ”Company” eller ”Organisation” (andra värden kommer att hanteras som ”Unknown”).
6. Obligatorisk **om** aktuell e-tjänst kräver signering.
7. Obligatorisk **om** aktuell e-tjänst kräver signering.
8. Obligatorisk (Actor och Comment kommer att skrivas till ärendets historik i Abou).
9. Boolean, anger om publicering till integration-plugins skall ske (fr.o.m. rel. 3.30.1607.1)

### CreateCase – Svar (response)

Svar från CreateCase (POST /api/v2/services/{serviceShortName}/cases/CreateCase): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: String (JSON objekt) med Abous unika ärendenummer för det nya ärendet, t.ex:

```text
”150810-AAA-WM56”
```

## PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage – Skapa direktmeddelande (NewDirectMessage)

NewDirectMessage skapar ett direktmeddelande i ett ärende i Abou, i namn av en administratör (AdministratorIdentity = UserName för en AdminUser i Abou). Metoden dokumenterades i dokumentrevision 2.3.1.A.

### NewDirectMessage – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/NewDirectMessage
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet Statusuppdaterare för aktuell e-tjänst i Abou.

### NewDirectMessage – Verb, headers och parametrar vid anrop

Anrop till NewDirectMessage (PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage).
När man skapar ett direktmeddelande måste man skicka med information som JSON.

| | |
|---|---|
| Verb | PUT |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

Data (pseudo-JSON enligt originalet; markeringen inom parentes, t.ex. `(1`, hänvisar till fotnoterna nedan):

```jsonc
{
 "UniqueId": "Abous unika ärendenummer för aktuellt ärende" (1,
 "DiaryNumber": "Anropande systems unika identifierare" (1,
 "AdministratorIdentity": "Meddelandets administratör" (2,
 "Text": “Själva meddelandet (3”
}
```

I originalet är följande fältnamn fetmarkerade: `UniqueId`, `DiaryNumber`, `AdministratorIdentity`, `Text`.

Fotnoter till datablocket för NewDirectMessage:

1. Obligatorisk UniqueId **eller** DiaryNumber (DiaryNumber förutsatt att ärendet uppdaterats med ett sådant).
2. Obligatorisk (UserName för någon AdminUser i Abou)
3. Obligatorisk

### NewDirectMessage – Svar (response)

Svar från NewDirectMessage (PUT /api/v2/services/{serviceShortName}/cases/NewDirectMessage): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data: String (JSON objekt) som bekräftar skickat meddelande för aktuellt ärende, t.ex:

```text
” 220223-AAA-IH39 - New direct message created”
```

## GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity – Hämta en lista av ärendenummer för ett personnummer (GetCaseListFromUserIdentity)

GetCaseListFromUserIdentity returnerar en lista med de senaste ärendenumren för ett person- eller organisationsnummer (query-parametern userIdentity). Ingen request body.

### GetCaseListFromUserIdentity – Exempel på URL för anrop

```text
https://abou.sokigo.com/api/v2/services/serviceShortName/cases/GetCaseListFromUserIdentity?userIdentity= userIdentity
```

| Del av URL | Beskrivning |
|---|---|
| abou.sokigo.com | Fiktiv URL till Abou |
| serviceShortName | En e-tjänsts kortnamn i Abou |
| userIdentity | Person- eller organisationsnummer (eller annan identifierare) som man vill hämta en lista av de senaste ärendena för |
| (userName | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-användare i Abou) |
| (apiKey | ***Tokenbaserad autentisering rekommenderas.*** Registrerad API-nyckel i Abou) |

- Kräver att API-användaren har lägst behörighet ”Enbart läsbehörighet” för aktuell e-tjänst i Abou.

### GetCaseListFromUserIdentity – Verb, headers och parametrar vid anrop

Anrop till GetCaseListFromUserIdentity (GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity).

| | |
|---|---|
| Verb | GET |
| Header | Authorization: Bearer … |
| | Content-Type: application/json |

### GetCaseListFromUserIdentity – Svar (response)

Svar från GetCaseListFromUserIdentity (GET /api/v2/services/{serviceShortName}/cases/GetCaseListFromUserIdentity): System.Net.Http.HttpResponseMessage

| Statuskod | Betydelse |
|---|---|
| 200 | OK |
| 404 | Not Found (felmeddelande i HttpResponseMessage.Content.Result) |
| 406 | Not Acceptable, (felmeddelande i HttpResponseMessage.Content.Result) |
| 500 | InternalServerError, (felmeddelande i HttpResponseMessage.Content.Result) |

Data:

- Content type: application/json eller xml
- Content: string[]

## Begäran om komplettering

Metoder för att begära komplettering från sökande (invånare) i Abou: RequestSupplementExistingCase, RequestSupplementNewCase, CancelSupplement och CancelAllSupplements. Kan användas tillsammans med RestwrapperPlugin se Att använda RestwrapperPluginet via REST-API nedan.

### POST /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementExistingCase – Begäran om komplettering på ett befintligt ärende i Abou

RequestSupplementExistingCase skapar en kompletteringsbegäran på ett ärende som redan finns i Abou (ärendet anges med UniqueId).

| RequestSupplementExistingCase | | |
|---|---|---|
| Request | RequestSupplementRequest | Se RequestSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [], "Applicant": "" }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2021.2.0.0 | |

Exempel på url för anrop (RequestSupplementExistingCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/RequestSupplementExistingCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (RequestSupplementExistingCase):

```json
{
  "Title": "Komplettera med markkarta",
  "Instructions": "Vänligen ladda upp ny markkarta med korrekt skala 1:400",
  "Arguments": [{
    "Name": "EventID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "InstructionFile": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  },
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "UniqueId": "190401-INTTESTANSOK-QX47",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "FileTypeCategories": 4
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/RequestSupplementNewCase – Begäran om komplettering då ärende saknas i Abou

RequestSupplementNewCase skapar en kompletteringsbegäran när ärendet saknas i Abou; i exemplet refereras ärendet med anropande systems DiaryNumber. Citizen är obligatoriskt när ett nytt ärende ska skapas i Abou.

| RequestSupplementNewCase | | |
|---|---|---|
| Request | RequestSupplementRequest | Se RequestSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [], "Applicant": "" }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2021.2.0.0 | |

Exempel på url för anrop (RequestSupplementNewCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/RequestSupplementNewCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (RequestSupplementNewCase):

```json
{
  "Title": "Komplettera med markkarta",
  "Instructions": "Vänligen ladda upp ny markkarta med korrekt skala 1:400",
  "Arguments": [{
    "Name": "EventID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "InstructionFile": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  },
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "DiaryNumber": "BYGG.2017.32",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "FileTypeCategories": 4
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/CancelSupplement – Ta bort en väntande komplettering

CancelSupplement tar bort (avbryter) en eller flera väntande kompletteringsbegäranden på ett ärende i Abou, angivna med SupplementIds. Ny metod i API 2.4.0.

| CancelSupplement | | |
|---|---|---|
| Request | CancelSupplementRequest | Se CancelSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [] }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2023.2.0.0 | |

Exempel på url för anrop (CancelSupplement):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/CancelSupplement
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (CancelSupplement):

```json
{
"SupplementIds":[4083,4084],
"Comment":"Tid för komplettering har gått ut",
"UniqueId": "190401-INTTESTANSOK-QX47"
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/CancelAllSupplements – Ta bort samtliga väntande kompletteringar

CancelAllSupplements tar bort samtliga väntande kompletteringsbegäranden på ett ärende i Abou. Request-modellen anges som CancelSupplementRequest, men exempel-payloaden innehåller inga SupplementIds. Ny metod i API 2.4.4 (Abou 2025.3 enligt versionshistoriken; metodtabellen anger Abou release 2023.2.0.0).

| CancelAllSupplements | | |
|---|---|---|
| Request | CancelSupplementRequest | Se CancelSupplementRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "SupplementIds": [] }` |
| E-service permission | Statusuppdaterare | |
| Abou release | 2023.2.0.0 | |

I originalet slutar URL-exemplet på `CancelAllSupplement` (utan avslutande s; radbrutet som ”CancelAllSupplemen” + ”t”).

Exempel på url för anrop (CancelAllSupplements):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/CancelAllSupplement
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (CancelAllSupplements):

```json
{
"Comment":"Tid för komplettering har gått ut",
"UniqueId": "190401-INTTESTANSOK-QX47"
}
```

## Delgivning av beslut

Metoder för att delge sökande (invånare) ett beslut via Abou: DecisionOnExistingCase och DecisionToNewCase. Kan användas tillsammans med RestwrapperPlugin se Att använda RestwrapperPluginet via REST-API nedan.

### POST /api/v2/services/{SERVICESHORTNAME}/cases/DecisionOnExistingCase – Delgivning av beslut på ett befintligt ärende i Abou

DecisionOnExistingCase delger ett beslut (beslutsdokument som Base64 i DecisionDocument, DecisionType Approved eller Rejected) på ett ärende som redan finns i Abou (anges med UniqueId).

| DecisionOnExistingCase | | |
|---|---|---|
| Request | CaseDecisionRequest | Se CaseDecisionRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "DecisionId": "", "Applicant": "" }` |
| E-service permission | Beslutsfattare | |
| Abou release | 2019.8.0.0 | |

Exempel på url för anrop (DecisionOnExistingCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/DecisionOnExistingCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (DecisionOnExistingCase):

```json
{
  "DecisionType": "Approved",
  "Description": "Här kommer ett beslut",
  "Arguments": [{
    "Name": "castor_CaseID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "UniqueId": "190515-INTTESTANSOK-DU65",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "DecisionDocument": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  }
}
```

### POST /api/v2/services/{SERVICESHORTNAME}/cases/DecisionToNewCase – Delgivning av beslut då ärende saknas i Abou

DecisionToNewCase delger ett beslut när ärendet saknas i Abou; i exemplet refereras ärendet med anropande systems DiaryNumber. Citizen är obligatoriskt när ett nytt ärende ska skapas i Abou.

| DecisionToNewCase | | |
|---|---|---|
| Request | CaseDecisionRequest | Se CaseDecisionRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result serialiserad modell: `{ "DecisionId": "" }` |
| E-service permission | Beslutsfattare | |
| Abou release | 2019.8.0.0 | |

Exempel på url för anrop (DecisionToNewCase):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/DecisionToNewCase
```

- Verb: POST
- Headers: Authorization: Bearer …

Exempel på Payload (DecisionToNewCase):

```json
{
  "DecisionType": "Approved",
  "Description": "Här kommer ett beslut",
  "Arguments": [{
    "Name": "castor_CaseID",
    "Value": "00000000-0000-0000-0000-000000000000"
  }],
  "Citizen": {
    "UserIdentity": "197110021834",
    "FirstName": "Waldemar",
    "LastName": "Filipsson",
    "Email": "abouinbox@gmail.com",
    "MobilePhone": "08932244"
  },
  "SentInAs": null,
  "SignatureData": null,
  "SignatureIssuer": null,
  "EnablePublishToPlugin": false,
  "UpdateExistingCitizen": false,
  "UpdateExisting": false,
  "DisableSendNotification": false,
  "OmitSocialSecurityNumberValidation": false,
  "DiaryNumber": "BYGG.2017.32",
  "Actor": "REST Client",
  "Comment": "Test från REST-klient",
  "DecisionDocument": {
    "FileName": "Test.pdf",
    "Base64Data": "JVBERi0xLjAKMSAwIG9iajw8L1BhZ2VzIDIgMCBSPj5lbmRvYmogMiAwIG9iajw8L0tpZHNbMyAw\nIFJdL0NvdW50IDE+PmVuZG9iaiAzIDAgb2JqPDwvTWVkaWFCb3hbMCAwIDMgM10+PmVuZG9iagp0\ncmFpbGVyPDwvUm9vdCAxIDAgUj4+Cg=="
  }
}
```

## PUT /api/v2/services/{SERVICESHORTNAME}/cases/UpdateFieldAnswers – Uppdatera fältsvar på ett befintligt ärende (UpdateFieldAnswers)

UpdateFieldAnswers uppdaterar svaret på ett eller flera fält i ett befintligt ärende i Abou. Fältet anges med ett unikt integrationsargument (FieldKeyValue med Name/Value). Med DoPublishPdf kan ärendets PDF genereras på nytt. Ny metod i API 2.2.2.

| UpdateFieldAnswers | | |
|---|---|---|
| Request | CaseUpdateFieldAnswersRequest | Se CaseUpdateFieldAnswersRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse |
| E-service permission | Statusuppdaterare | |
| Abou release | 2020.2.16.0 | |

Exempel på url för anrop (UpdateFieldAnswers):

```text
https://abou.sokigo.com/api/v2/services/SERVICESHORTNAME/cases/UpdateFieldAnswers
```

- Verb: PUT
- Headers: Authorization: Bearer …

Exempel på Payload (UpdateFieldAnswers), återgiven exakt som i originalet. Observera att kommatecken saknas efter `"Comment"` och efter `"Answer"`, så exemplet är inte giltig JSON som det står:

```json
{
   "UniqueId": "200507-MMLA-MS11",
   "DiaryNumber": null,
   "Actor": "System X",
   "Comment": "Uppdatering av fältsvar…"
   "Fields": [
        {
             "Answer": "Nytt svar"
             "FieldKeyValue": {
                  "Name": "abou_an_unique_integrationargument_name",
                  "Value": "some_value"
             }
        }
   ],
   "DoPublishPdf": true
}
```

## GET /api/v2/services/cases/GetVersion – Hämta befintlig version av Abou API (GetVersion)

GetVersion returnerar befintlig version av Abou API. Ingen request-modell och ingen e-tjänstebehörighet anges.

| GetVersion | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationResponse> | Se IntegrationResponse |
| E-service permission | | |
| Abou release | 2019.5.0.0 | |

Exempel på url för anrop (GetVersion):

```text
https://abou.sokigo.com/api/v2/services/cases/GetVersion
```

- Verb: GET

## GET /api/v2/services/{ServiceShortName}/cases/GetCaseStatistics – Hämta ärendestatistik för en specifik e-tjänst (GetCaseStatistics)

GetCaseStatistics returnerar ärendestatistik (påbörjade ärenden, inskickade ärenden, inskickade som ombud) för en e-tjänst. Kräver systembehörigheten ”Hämta ärendestatistik”.

| GetCaseStatistics | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | Hämta ärendestatistik | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för GetCaseStatistics (IntegrationResponse.Result):

```json
{
"ServiceShortName":"",
"StartedCases": 0,
"SubmittedCases": 0,
"SubmittedAsOmbudsman": 0
}
```

Exempel på url för anrop (GetCaseStatistics):

```text
https://abou.sokigo.com/api/v2/services/ServiceShortName/cases/GetCaseStatistics
```

- Verb: GET
- Headers: Authorization: Bearer …

## GET /api/v2/services/SearchServices?Searchstring={query} – Söka bland publicerade e-tjänster (SearchServices)

SearchServices söker bland publicerade e-tjänster med en söksträng (query-parametern Searchstring) och returnerar kortnamn, visningsnamn och URL:er för matchande e-tjänster.

| SearchServices | | |
|---|---|---|
| Request | | |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för SearchServices (IntegrationResponse.Result), återgiven som i originalet (inklusive avslutande kommatecken efter objektet):

```jsonc
[
{
"ServiceShortName":"",
"DisplayName": "",
"ServiceUrl": "",
"FormUrl": ""
},
]
```

I URL-exemplet är `query` (söksträngen) fetmarkerad.

Exempel på url för anrop (SearchServices):

```text
https://abou.sokigo.com/api/v2/services/SearchServices?Searchstring=query
```

- Verb: GET

## POST /api/v2/services/GetServices – Hämta information för en specifik e-tjänst (GetServices)

GetServices returnerar information om e-tjänster (aktiv/öppen, öppettider, autentisering/signering, beslut, organisation, ärendestatusar), filtrerat enligt ServiceOrganisationRequest. Kräver systembehörigheten ”Hämta e-tjänster”.

| GetServices | | |
|---|---|---|
| Request | ServiceOrganisationRequest | Se ServiceOrganisationRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Vid IntegrationResponse.Success = true innehåller IntegrationResponse.Result modell (se nedan) |
| E-service permission | | |
| Systembehörighet | Hämta e-tjänster | |
| Abou release | 2021.5.0.0 | |

Resultatmodell för GetServices (IntegrationResponse.Result), återgiven som i originalet (med `=` i stället för `:`):

```text
[{
"ServiceShortName" = "",
"ServiceDisplayName" = "",
"ServiceUrl" = "",
"FormUrl" = "",
"ServiceIsActive" = true/false,
"ServiceIsOpen" = true/false,
"ServiceOpenFrom" = datum/null,
"ServiceOpenTo" = datum/null,
"ServiceWindowFrom" = datum/null,
"ServiceWindowTo" = datum/null,
"ServiceHasAuthentication" = true/false,
"ServiceHasSigning" = true/false,
"ServiceHasMultipleSigning" = true/false,
"ServiceHasAlternativeSigning" = true/false,
"ServiceHasDecision" = true/false,
"ServiceLastUpdated" = datum,
"OrganisationName" = "",
"CaseStatusList" = [""]
}]
```

Exempel på url för anrop (GetServices):

```text
https://abou.sokigo.com/api/v2/services/GetServices
```

- Verb: POST
- Headers: Authorization: Bearer …

## PUT /api/v2/registers/ImportRegister – Import register (ImportRegister)

ImportRegister importerar ett register till Abou (skapar nytt eller skriver över befintligt med samma SystemName) och kan koppla registret till e-tjänster. Kräver systembehörigheten ”Importera register”. Ny metod i API 2.3.2.

| ImportRegister | | |
|---|---|---|
| Request | ImportRegisterRequest | Se ImportRegisterRequest |
| Response | HttpResponseMessage<HttpStatusCode, IntegrationObjectResponse> | Se IntegrationResponse. Inkluderar Success och Message |
| E-service permission | | |
| Systembehörighet | Importera register | |
| Abou release | 2022.8.0.0 | |

Exempel på url för anrop (ImportRegister):

```text
https://abou.sokigo.com/api/v2/registers/ImportRegister
```

- Verb: PUT
- Headers: Authorization: Bearer …

## Entiteter (request- och response-modeller)

*Kolumnen Obl (obligatorisk) nedan anges som * och – där * innebär att argumentet är strikt obligatoriskt medan – innebär att argumentet är obligatoriskt beroende på vilket ska framgå i beskrivning.*

I tabellerna nedan återges * som `*` och – som `-`; tom cell betyder att inget anges i originalet. Namn och typer är i originalet satta i teckensnitt med fast bredd, och modellnamn i typkolumnen (t.ex. FileData, CitizenRequest, FieldArgument) är länkar till respektive entitet.

### Entitet RequestSupplementRequest

Request-modell för Begäran om komplettering (RequestSupplementExistingCase och RequestSupplementNewCase).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Title` | String | `*` | Rubrik för kompletteringsbegäran. |
| `Instructions` | String | `-` | För sökande vägledande information för att kunna utföra komplettering.<br>Obligatorisk om det saknas ”InstructionFIle” |
| `InstructionFile` | FileData | `-` | För sökande vägledande information för att kunna utföra komplettering.<br>Obligatorisk om det saknas ”Instructions” |
| `DescriptionToAdministrator` | String |  | Anledning till begäran om komplettering, lagras i ärendet som ärendehistorik i Abou |
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om begäran om komplettering ska ske i ett redan <u>existerande</u> ärende i Abou |
| `DiaryNumber` | String |  | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou |
| `Actor` | String |  | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String |  | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `Arguments` | List<FieldArgument> | `-` | Lista med Namn/Värde-par som rör kompletteringen. Dessa behövs vid eventuell återkopplande integration till anropande system.<br>Se FieldArgument. |
| `Citizen` | CitizenRequest | `-` | Obligatoriskt när ett nytt ärende ska skapas i Abou.<br>Se CitizenRequest |
| `OmitSocialSecurityNumberValidation` | Bool |  | True innebär att personnummervalidering på Citizen.UserIdentity utelämnas |
| `UpdateExistingCitizen` | Bool |  | True innebär att Citizen-FirstName, LastName, Email och MobilePhone uppdaterar befintlig invånare I Abou |
| `DisableSendNotification` | Bool |  | True innebär att e-tjänstens notifieringar inaktiveras |
| `SentInAs` | String |  | Anger vilken roll sökande får i nytt ärende baserad på specifik e-tjänst för komplettering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureData` | String | `-` | Information som ska signeras.<br>Obligatorisk om specifik e-tjänst för komplettering kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureIssuer` | String | `-` | Utgivare av signeringen.<br>Obligatorisk om specifik e-tjänst för komplettering kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `EnablePublishToPlugin` | Bool |  | True innebär att nytt ärende baserad på specifik e-tjänst för komplettering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt, triggar händelse för integration |
| `AllowMultipleFiles` | Bool |  | True innebär att invånaren kan komplettera med flera filer inom en och samma kompletteringsbegäran |
| `FileTypeCategories` | Int |  | De typer av fil invånaren tillåts komplettera med. Giltiga värden är 1, 2 och 4.<br>1 – Bilder (".jpg", ".jpeg", ".png")<br>2 – Office-dokument (".xls", ".xlsx", ".doc", ".docx")<br>4 – PDF-fil (".pdf")<br>Så kallad bit-skiftning (bitwise) kan användas för att kombinera tillåtna typer av filer, t.ex. innebär värdet 5 att Bilder och PDF-fil tillåts.<br>Default (om FileTypeCategories utelämnas) är att Bilder, Office-dokument och PDF-fil tillåts. |

#### RequestSupplementRequest – värden för FileTypeCategories

Enumvärden (bitflaggor som kan kombineras) för fältet FileTypeCategories i RequestSupplementRequest, enligt tabellen ovan:

| Värde | Tillåtna filtyper |
|---|---|
| 1 | Bilder (".jpg", ".jpeg", ".png") |
| 2 | Office-dokument (".xls", ".xlsx", ".doc", ".docx") |
| 4 | PDF-fil (".pdf") |
| 5 (exempel, 1 + 4) | Bilder och PDF-fil |
| utelämnat (default) | Bilder, Office-dokument och PDF-fil |

### Entitet CancelSupplementRequest

Request-modell för CancelSupplement och CancelAllSupplements (ta bort väntande komplettering).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Comment` | String |  | Det anropande systemets kommentar för anropet, presenteras i ärendehistorik. |
| `UniqueId` | String | `*` | Identifierare för ett ärende i Abou. |
| `DiaryNumber` | String | `-` | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou. |
| `SupplementIds` | List<int> | `*` | Id för de kompletteringsbegäran som skall avbrytas. Värdet kan vara sparat från när kompletteringsbegärand skapades eller hämtas med GetDetailed. |

### Entitet CaseDecisionRequest

Request-modell för Delgivning av beslut (DecisionOnExistingCase och DecisionToNewCase).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Description` | String |  | Kommentar som beskriver beslutet. Ska ses som en kommentar från en handläggare. Visas för sökande i Abou. |
| `DecisionType` | String | `*` | Typ av beslut. Giltiga värden är: Rejected och Approved. |
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om beslut ska tilldelas ett redan <u>existerande</u> ärende i Abou. |
| `DiaryNumber` | String |  | Det anropande systemets ärendenummer, kompletterar ärendeinformationen i Abou |
| `Actor` | String | `*` | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String |  | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `DecisionDocument` | FileData | `*` | Innehåller information om beslutsdokumentet. Se FileData |
| `Citizen` | CitizenRequest | `-` | Obligatoriskt när ett nytt ärende ska skapas i Abou.<br>Se CitizenRequest |
| `OmitSocialSecurityNumberValidation` | Bool |  | True innebär att personnummervalidering på Citizen.UserIdentity utelämnas |
| `UpdateExistingCitizen` | Bool |  | True innebär att Citizen-FirstName, LastName, Email och MobilePhone uppdaterar aktuell invånare (sökande) i Abou |
| `DisableSendNotification` | Bool |  | True innebär att e-tjänstens notifieringar inaktiveras |
| `SentInAs` | String |  | Anger vilken roll sökande får i nytt ärende baserad på specifik e-tjänst för beslut som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt. |
| `SignatureData` | String | `-` | Information som ska signeras.<br>Obligatorisk om specifik e-tjänst för beslut kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `SignatureIssuer` | String | `-` | Utgivare av signeringen.<br>Obligatorisk om specifik e-tjänst för beslut kräver signering som används då ärende saknas, dvs då ansökan i anropande system inkommit manuellt |
| `Arguments` | List<FieldArgument> | `-` | Lista med Namn/Värde-par som rör beslutet. Dessa behövs vid eventuell återkopplande integration till anropande system.<br>Se FieldArgument. |
| `EnablePublishToPlugin` | Bool |  | True invånaren kan välja att komplettera med flera filer i en och samma komplettering |

Anm.: Beskrivningen av `EnablePublishToPlugin` i CaseDecisionRequest är återgiven exakt som i originalet (den liknar beskrivningen av AllowMultipleFiles i RequestSupplementRequest).

Enumvärden för `DecisionType` i CaseDecisionRequest: `Approved`, `Rejected`.

### Entitet CitizenRequest

Modell för invånare/sökande (Citizen) i bl.a. RequestSupplementRequest och CaseDecisionRequest.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `UserIdentity` | String | `*` | Ett giltigt personnummer |
| `FirstName` | String | `*` | Förnamn |
| `LastName` | String | `*` | Efternamn |
| `Email` | String | `*` | En giltig e-post adress |
| `MobilePhone` | String |  | Mobiltelefon |
| `SendNotificationType` | String |  | Giltiga värden är Email (default) eller Sms |

### Entitet ServiceOrganisationRequest

Request-modell (filter) för GetServices (POST /api/v2/services/GetServices). Tabellen saknar kolumnen Obl i originalet.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Open` | Bool? | Enbart e-tjänster som är öppna(true)/stängda/(false). Null innebär ingen filtrering. |
| `Active` | Bool? | Enbart e-tjänster som är aktiva(true)/inaktiva /(false). Null innebär ingen filtrering. |
| `ServiceShortNames` | String[] | Array med kortnamnen på de e-tjänster som skall hämtas. Null innebär ingen filtrering. |
| `Organisations` | String[] | Array med namnen på de organisationer vars e-tjänster skall hämtas. Null innebär ingen filtrering. |

### Entitet ImportRegisterRequest

Request-modell för ImportRegister (PUT /api/v2/registers/ImportRegister). Tabellen saknar kolumnen Obl i originalet.

| Namn | Typ | Beskrivning |
|---|---|---|
| `SystemName` | String | Systemnamn för det importerade registret. Anges ett existerade systemnamn skrivs det befintliga registret över. |
| `DisplayName` | String | Visningsnamn för det importerade registret. |
| `Description` | String | Beskrivning av det importerade registret. |
| `ServiceShortNames` | String[] | Array med kortnamnen på de nya e-tjänster som ska kopplas till registret. Existerande kopplingar påverkas inte. Om tom eller null utförs ingen koppling. Eventuella dubbletter ignoreras. Samtliga e-tjänster behöver finnas i noden. |
| `Data` | String[] | Array med data som skall finnas i registret. Tomma värden tas bort. Dubbletter ignoreras. Tom lista godkänns inte. |

### Entitet FieldArgument

Namn/värde-par (integrationsargument). Används i Arguments-listor (RequestSupplementRequest, CaseDecisionRequest) och i FieldRequest.FieldKeyValue.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Name` | String | `*` |  |
| `Value` | String | `*` |  |

### Entitet FileData

Fil som Base64-data. Används i CaseDecisionRequest.DecisionDocument och RequestSupplementRequest.InstructionFile.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `FileName` | String | `*` | Beslutsdokumentets namn |
| `Base64Data` | String | `*` | Fildata i Base64 |

### Entitet CaseUpdateFieldAnswersRequest

Request-modell för UpdateFieldAnswers (uppdatera fältsvar på ett befintligt ärende).

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `UniqueId` | String | `-` | Identifierare för ett ärende i Abou.<br>Obligatorisk om INTE DiaryNumber används |
| `DiaryNumber` | String | `-` | Att systemets ärendenummer på ett ärende i Abou.<br>Obligatorisk om INTE UniqueId används |
| `Actor` | String | `*` | Det anropande systemets benämning, presenteras bla i ärendehistorik |
| `Comment` | String |  | Det anropande systemets kommentar för anropet, presenteras bla i ärendehistorik |
| `Fields` | List<FieldRequest> | `*` | Lista med nytt fältsvar samt fältreferens.<br>Se FieldRequest. |
| `DoPublishPdf` | Bool |  | True innebär att det aktuella ärendets PDF genereras på nytt för att |

Anm.: Beskrivningen av `DoPublishPdf` slutar abrupt (”…genereras på nytt för att”) i originalet; resten av meningen finns inte i dokumentet.

### Entitet FieldRequest

Modell för ett fältsvar i CaseUpdateFieldAnswersRequest.Fields.

| Namn | Typ | Obl | Beskrivning |
|---|---|---|---|
| `Answer` | String | `*` | Nytt fältsvar |
| `FieldKeyValue` | FieldArgument | `*` | Unik kombination av namn och värde för ett integrationsargument som anger fältet för uppdatering av svar |

### Entitet IntegrationResponse

Response-modell (Result som sträng) för bl.a. Begäran om komplettering, Delgivning av beslut, UpdateFieldAnswers och GetVersion. Tabellen saknar kolumnen Obl.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Success` | Bool | True innebär att anropet utfördes i sin helhet |
| `Message` | String | Felmeddelande vid Success = false |
| `Result` | String | Resultat vid Success = true |
| `Id` | String | Vanligen aktuellt ärendenummer i Abou |

### Entitet IntegrationObjectResponse

Response-modell (Result som objekt) för GetCaseStatistics, SearchServices, GetServices och ImportRegister. Tillagd i API 2.3.1. Tabellen saknar kolumnen Obl.

| Namn | Typ | Beskrivning |
|---|---|---|
| `Success` | Bool | True innebär att anropet utfördes i sin helhet |
| `Message` | String | Felmeddelande vid Success = false |
| `Result` | Object | Resultat vid Success = true |
| `Id` | String | Vanligen aktuellt ärendenummer i Abou |

## Kodexempel för att anropa Abous REST API, .Net C#

C#-exempel (HttpClient, Newtonsoft.Json) från dokumentet för att anropa Abou REST API med Bearer-token. Radbrytningar som i PDF:en uppstått mitt i strängliteraler och kommentarer på grund av sidbredden har slagits ihop; i övrigt återges koden som i dokumentet, inklusive eventuella fel (t.ex. `URI.EscapeDataString(filename)`, dubbla parenteser i `NameValueHeaderValue((`, och `stringContents` i GetByDateAndState).

### Kodexempel C# – using-direktiv och konstanter

Gemensamma using-direktiv och konstanter (ApiUrl, ApiUserName, ApiKey, ServiceShortName, CaseUniqueId, DiaryNumber) som används i kodexemplen nedan.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading;
using Newtonsoft.Json;

private const string ApiUrl = "https://abou.sokigo.com/api";
private const string ApiUserName = "api user name";
private const string ApiKey = "api user key";
private const string ServiceShortName = "aaa";
private const string CaseUniqueId = "150527-AAA-UI91";
private const string DiaryNumber = "";
```

### Kodexempel C# – Hämta Bearer Token (Authenticate)

Hämtar en Bearer-token via GET {ApiUrl}/authenticate/{ServiceShortName} med Basic Authorization (ApiUserName:ApiKey, Base64-kodat).

```csharp
var httpRequestTokenMessage = new HttpRequestMessage(HttpMethod.Get,
   string.Format("{0}/authenticate/{1}", ApiUrl, ServiceShortName));
var basicAuth =  new AuthenticationHeaderValue("Basic", Convert.ToBase64String(new
   UTF8Encoding().GetBytes(ApiUserName + ":" + ApiKey)));
httpRequestTokenMessage.Headers.Authorization = basicAuth;

var client = new HttpClient();
var request = client.SendAsync(httpRequestTokenMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
var httpResponse = request.Result;
if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
   return;
var bearerToken = httpResponse.Content.ReadAsStringAsync().Result;
```

### Kodexempel C# – FileUpload med Bearer Token

Bifogar filer via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/FileUpload som MultipartFormDataContent: en JSON-del med namnet CaseBaseRequest och en del per fil med namnet file. Per fil kan Content-Disposition-parametrarna useReceipt, fileDescription och fileDefinition anges. Kommentaren `//←` avslutar i originalet blocket som bara behövs för dessa parametrar.

```csharp
var content = new MultipartFormDataContent();

const string ServiceShortName = "kortnamn";
const string CaseUniqueId = "ärendenummer";
const string DiaryNumber = "";
const bool DisableSendNotification = false;

var stringContent = new
StringContent($"{{\"UniqueId\":\"{CaseUniqueId}\",\"DiaryNumber\":\"{DiaryNumber}\",\"Comment\":\"Test av V2api\",\"Actor\":\"ConsoleApp\",\"DisableSendNotification\":\"{DisableSendNotification}\"}}");
stringContent.Headers.Add("Content-Disposition", "form-data; name=\"CaseBaseRequest\"");
content.Add(stringContent);

var files = new[] { @"C:\Temp\Test1.pdf", @"C:\Temp\Test2.pdf" };

foreach (var file in files)
{
   var fileStream = new FileStream(file, FileMode.Open);
   var fileName = Path.GetFileName(file);
   var streamContent = new StreamContent(fileStream);

   //Only needed when we want to use useReceipt, fileDescription or fileDefinition
   streamContent.Headers.Add("Content-Type", "application/octet-stream");
   streamContent.Headers.Add("Content-Disposition", "form-data; name=\"file\"; filename=\"" + URI.EscapeDataString(filename) + "\"");
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("useReceipt", "true"));
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("fileDescription", " beskrivning"));
   streamContent.Headers.ContentDisposition.Parameters.Add(new
      NameValueHeaderValue(("fileDefinition", " typ"));
   //←

   content.Add(streamContent, "file", fileName);
}

var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
   string.Format("{0}/v2/services/{1}/cases/FileUpload", ApiUrl, ServiceShortName));
var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
httpRequestMessage.Headers.Authorization = bearerAuth;
httpRequestMessage.Content = content;

var client = new HttpClient();
request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
httpResponse = request.Result;
if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
   return;
var response = httpResponse.Content.ReadAsStringAsync().Result;
```

### Kodexempel C# – UpdateStatus med Bearer Token

Sätter status (i exemplet ”Makulerat”) via PUT {ApiUrl}/v2/services/{ServiceShortName}/cases/UpdateStatus med JSON-body.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"State\":\"{4}\",
      \"DisableSendNotification\":\"{5}\"}}",
   CaseUniqueId, DiaryNumber, "Test av V2api", "ConsoleApp", "Makulerat", false));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Put,
      string.Format("{0}/v2/services/{1}/cases/UpdateStatus", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

### Kodexempel C# – GetByDateAndState

Söker ärendenummer via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/GetByDateAndState (datumintervall, statusar ”inkommet”/”avslutad” och filter på fältsvar) och itererar över resultatet för att hämta varje ärende med GetDetailed.

```csharp
using (var client = new HttpClient())
{
   var str = "{\"FromDate\":\"2012-01-01\", \"ToDate\":\"2015-12-12\",
      \"Comment\":\"Test av V2api\", \"Actor\":\"ConsolApp\", \"States\":[\"inkommet\",
      \"avslutad\"], \"ExcludeCasesWithDiaryNumber\":false, \"Field\":{\"Answer\":
      \"ett fältsvar\", \"Argument\":{\"Name\":\"integrationsargumentets namn\",
      \"Value\":\"integrationsargumentets värde\"}}}";

   var stringContent = new StringContent(str);
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
   string.Format("{0}/v2/services/{1}/cases/GetByDateAndState", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
      HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;

   var ids = JsonConvert.DeserializeObject<IEnumerable<string>>(stringContents);
   var enumerable = ids as string[] ?? ids.ToArray();

   if (ids == null || !enumerable.Any())
      return;

   foreach (var id in enumerable)
   {
      // Get detailed case via GetDetailed
   }
}
```

### Kodexempel C# – GetDetailed med Bearer Token

Hämtar ett detaljerat ärende via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/GetDetailed med XmlGeneratorType DefaultXmlCaseGenerator och sparar svaret som XML-fil under C:\Temp.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"XmlGeneratorType\":\"{4}\",
      \"IncludeAllFields\":\"{5}\",\"IncludeAllAttachements\":\"{6}\",
      \"OmitXmlDeclaration\":\"{7}\"}}", uniqueId ?? CaseUniqueId, "", "Test av V2api",
      "ConsolApp","Abou.Calamare.Framework.Integration.Xml.Default.DefaultXmlCaseGenerator", true, true, true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/GetDetailed", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;

   var response = httpResponse.Content.ReadAsStringAsync().Result;

   File.WriteAllText(string.Format(@"C:\Temp\{0}.xml", uniqueId ?? CaseUniqueId),
      response);
}
```

### Kodexempel C# – AttachmentDownload med Bearer Token

Hämtar en specifik bilaga (SystemFileName ”150907-AAA-UL67_abou_produktblad.pdf”) och sparar den som fil. Observera att exemplet anropar sökvägen `…/cases/CaseAttachmentDownload`, medan metoden i API-beskrivningen heter AttachmentDownload.

```csharp
const string systemFilename = "150907-AAA-UL67_abou_produktblad.pdf";

using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Comment\":\"{2}\",\"Actor\":\"{3}\",\"SystemFileName\":\"{4}\"}}",
      uniqueId ?? CaseUniqueId, "", "Test av V2api", "ConsolApp", systemFilename));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/CaseAttachmentDownload", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var data = httpResponse.Content.ReadAsByteArrayAsync();

   File.WriteAllBytes(string.Format(@"C:\Temp\{0}", systemFilename), data.Result);
}
```

### Kodexempel C# – AddCitizens med Bearer Token

Lägger till två invånare (Kalle Karlsson och Sven Svensson) på ett ärende via PUT {ApiUrl}/v2/services/{ServiceShortName}/cases/AddCitizens.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"UniqueId\":\"{0}\",\"DiaryNumber\":\"{1}\",
      \"Citizens\":" +

      "[{{\"UserIdentity\":\"121212121212\",\"FirstName\":\"Kalle\",\"LastName\":
      \"Karlsson\",\"Email\":\"kalle@karlsson.se\"}}," +

      "{{\"UserIdentity\":\"121312127374\",\"FirstName\":\"Sven\",\"LastName\":
      \"Svensson\",\"Email\":\"sven@svensson.se\"}}]," +

      "\"Comment\":\"{2}\",\"Actor\":\"{3}\",\"UpdateExisting\":false,
      \"OmitSocialSecurityNumberValidation\":false," +

      "\"DisableSendNotification\":\"{4}\"}}", CaseUniqueId, DiaryNumber,
      "Test av V2api", "ConsolApp", true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Put,
      string.Format("{0}/v2/services/{1}/cases/AddCitizens", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

### Kodexempel C# – CreateCase med Bearer Token

Skapar ett nytt ärende via POST {ApiUrl}/v2/services/{ServiceShortName}/cases/CreateCase med två fältsvar (integrationsargument ArgumentName1/ArgumentName2), Citizen, SentInAs ”Citizen” och signeringsdata.

```csharp
using (var client = new HttpClient())
{
   var stringContent = new
      StringContent(string.Format("{{\"Fields\":[{{\"Answer\":
      \"Fältsvar förnamn\",\"Arguments\":[{{\"Name\":\"ArgumentName1\",\"Value\":
      \"ArgumentValue1\"}}]}}," +

      "{{\"Answer\":\"Fältsvar efternamn\",\"Arguments\":[{{\"Name\":\"ArgumentName2\",
      \"Value\":\"ArgumentValue2\"}}]}}]," +

      "\"Citizen\":{{\"UserIdentity\":\"121212121212\",\"FirstName\":\"Kalle\",
      \"LastName\":\"Karlsson\",\"Email\":\"kalle@karlsson.se\"}}," +

      "\"Comment\":\"{2}\",\"Actor\":\"{3}\",\"UpdateExistingCitizen\":false,
      \"OmitSocialSecurityNumberValidation\":false," +

      "\"SentInAs\":\"Citizen\",\"SignatureData\":\"signdata\",\"SignatureIssuer\":
      \"signer\"," +

      "\"DisableSendNotification\":\"{4}\"}}", CaseUniqueId, DiaryNumber,
      "Test av V2api", "ConsolApp", true));
   stringContent.Headers.ContentType = new MediaTypeHeaderValue("application/json");

   var httpRequestMessage = new HttpRequestMessage(HttpMethod.Post,
      string.Format("{0}/v2/services/{1}/cases/CreateCase", ApiUrl,
      ServiceShortName));
   var bearerAuth = new AuthenticationHeaderValue("Bearer", bearerToken); //Se ex "Hämta Bearer Token"
   httpRequestMessage.Headers.Authorization = bearerAuth;
   httpRequestMessage.Content = stringContent;

   request = client.SendAsync(httpRequestMessage,
   HttpCompletionOption.ResponseContentRead, CancellationToken.None);
   httpResponse = request.Result;
   if (httpResponse.StatusCode != HttpStatusCode.OK || httpResponse.Content == null)
      return;
   var response = httpResponse.Content.ReadAsStringAsync().Result;
}
```

## Testa REST API (Postman, YARC)

Kan enkelt göras med verktyget Postman eller t.ex. YARC som är ett tillägg till Google Chrome:

### Bild: Test av Authenticate i YARC (Chrome-tillägg)

Skärmbild från YARC som visar ett lyckat anrop till Authenticate (hämta token). Text i bilden:

- **Request Settings**
  - URL: `https://abou.sokigo.com/api/authenticate/AAA`, metod: **GET**
  - Payload: tomt fält med platshållartexten `application/json`
- **Custom Headers** (hopfälld panel)
- **Authentication**: ”Basic Authentication is supported. Enter a username and password and the Authorization Header will be generated and sent with the request.”
  - Authorization: `Basic YWJvdTyAdA91YAda` (avläst från skärmbilden; kan innehålla avläsningsfel). Knapp: *Add Credentials*
- Knapp: *Send Request*
- **Response**
  - Request URL: `https://abou-a3-dev.abou.se/api/authenticate/ABOU123`
  - Request Method: GET
  - Response Time: 0.29 seconds
  - Response Status: 200 - OK (visas även som en stor grön ruta med ”200”)
  - Flikar: *Response Body* (vald), *Response Body (RAW)*, *Response Headers*, *Request Details*
  - Knappar: *Copy Request*, *Copy Response*

Response Body i skärmbilden (JWT-token; header-delen i fetstil, resten i rött). Avläst från skärmbilden: payload-delen är kontrollerad genom Base64-avkodning, signaturdelen (efter sista punkten) kan innehålla avläsningsfel:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJc3MiOiJhYm91IiwiRXhwIjoiMjAyMS0wOC0yM1QwODoyNjozNC44MTkyMTUxWiIsIlNlcnZpY2VTaG9ydE5hbWUiOiJBQk9VMTIzIiwiU3lzdGVtUGVybWlzc2lvbiI6MjQsIlNlcnZpY2VQZXJtaXNzaW9uIjoyNTQsIkN1c29tZXJJZCI6MTAwMn0.c4NOmKFBEfbFnrEsbOO4bDw_1A-SoVLebt30hlKKLnw
```

## Att använda RestwrapperPluginet via REST-API

Gäller metoderna för Begäran om komplettering (RequestSupplementExistingCase, RequestSupplementNewCase) och Delgivning av beslut (DecisionOnExistingCase, DecisionToNewCase).

Följande metoder har stöd för att ta emot argument som gör att RestwrapperPluginet kan skicka ett anrop för att tillexempel skapa ett läskvitto i ett annat system när invånaren tar del av ett beslutsdokument:

- Begäran om komplettering – anrop körs när invånaren utför kompletteringen
- Delgivning av beslut – anrop körs när beslutsdokumentet laddas ned för första gången

För att detta ska kunna användas krävs att man har tillgång till RestwrapperPluginet samt att lämplig konfiguration för anropet har lags in. Utöver detta ska man skicka med följande värden som Name i Arguments

- ConfigurationDataKey – Nyckeln på den konfiguration som skall användas
- ServicePurpose – Grundmodell för hur Restwrappern ska hantera ärendet, t.ex. CaseAsGenericModel
- IncludeCaseParameters – true/false, valfritt. Bestämmer om parametrar för tokens från ärendet ska inkluderas till anropet

Det finns också stöd för att skicka med ytterligare värden som kommer att hanteras som om de vore integrationsargument ifrån ärendet.
