# PageNode API — Dokumentation för hjälpmetoder

This **is** the supported IronPython library (builder mall **Dokumentation för hjälpmetoder**, UI 2026-08-21). Use it to explain and review Python, not only to copy a new class.

How it fits with client JS and integrations: [libraries.md](libraries.md). Worked examples: [INDEX.md](INDEX.md).

Field id: under Fältdetaljer. In code use `'x.1'` where `x` is the current service short name and `1` is the number. Other services: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)` → `"<shortName>.15"`.

Lifecycle: `Initialize` on page load (prefill, hide). `BeforeGetNextPage` before leave. `GetNextPage` must return a page: `PageNode.GetNextPage(self)`, `self.GetPage('Systemnamn')`, or `self.Page` to stay (validation). Thank-you uses `Published(self)` not GetAnswer.

IronPythonType **class name must match**.

## How to use the methods

- **Answers:** `GetAnswer` is one string. Checkboxes and tables need `GetAnswers`. `SetAnswerIfEmpty` lets the citizen keep a changed value.
- **Visibility:** `SetHidden` / `SetHiddenBlock` run on the **server** when the page loads or on Nästa. Same-page instant hide is [client/api.md](client/api.md). Clearing a hidden required field: [required-when-hidden.md](required-when-hidden.md).
- **Validation:** `SetValidationText` does nothing unless you `return self.Page`.
- **Options:** `SetOptions` with `"Text|Value"` when **Separera text och värde** is on. Read with `GetValueFromQuestionAlternative` vs `GetAnswerFromQuestionAlternative`.
- **Citizen:** `self.Citizen` is GDPR-stripped. Fuller PersonPost: `GetCitizenInfoLookUp` (session) or Navet types in [libraries.md](libraries.md).
- **Other cases:** `GetAnswerFromCase` requires the logged-in user to be tied to that case. After submit use `*PublishedCase*`.
- **JSON:** mall comments mention `DeserializeObject`; the hjälpmetoder **code** calls `Deserialize`. Läggtillrad uses `AnswersModel` in [calculations.md](calculations.md), not these helpers.

## Methods (from the mall)

Field id: under Fältdetaljer. In code use `'x.1'` where `x` is the current service short name and `1` is the number. Other services: `'KORTNAMN.15'`. Helper: `GetFriendlyFieldIdFromFieldNumber(15)` → `"<shortName>.15"`.

Lifecycle: `Initialize` on page load (prefill, hide). `BeforeGetNextPage` before leave. `GetNextPage` must return a page: `PageNode.GetNextPage(self)`, `self.GetPage('Systemnamn')`, or `self.Page` to stay (validation). Thank-you uses `Published(self)` not GetAnswer.

IronPythonType **class name must match**.

## Methods (from the mall)

| Method | Use |
| --- | --- |
| `GetAnswer('x.1')` | Single answer |
| `GetAnswers('x.1')` | Checkboxes, table — list |
| `GetValueFromQuestionAlternative('x.1')` | Separated **value** (radio/checkbox) |
| `GetAnswerFromQuestionAlternative('x.1')` | Separated **display text** |
| `SetAnswer('x.1', value)` | Set answer |
| `SetAnswerIfEmpty('x.1', value)` | Set only if empty; citizen change wins |
| `SetQuestionText('x.1', 'Rubrik')` | Field label |
| `GetOptions("x.1")` | Current alternatives |
| `SetOptions("x.1", Array[String]([…]))` | Alternatives; with split: `"Text\|Value"` |
| `SetOptionHelpTexts("x.1", Array[str]([…]))` | Per-alternative help |
| `SetDisabled('x.1', True/False)` | Read-only |
| `SetRequired("x.1", True/False)` | Required |
| `SetHidden("x.1", True/False)` | Hide field |
| `SetHiddenBlock("BLOCK1", True/False)` | Hide block |
| `SetHiddenAndClearBlock("BLOCK1", True/False)` | Clear + hide / show |
| `CopyTo(fromId, toId)` | Copy answer (same field kinds) |
| `LogDebug` / `LogInfo` / `LogError` | String → preview **Visa skriptlogg** |
| `LogDebugObject` / `LogInfoObject` / `LogErrorObject` | Object |
| `GetAgeOnDate(pnr, "2026-03-03")` | Age from personnummer + date strings |
| `SetValidationText("x.1", "…")` | Then **`return self.Page`** or the user is not stopped |
| `Serialize(obj)` | Object → JSON string (store as answer) |
| `Deserialize(json)` | JSON → dict/list (mall comment says DeserializeObject; **code uses Deserialize**) |
| `GetJsonDeserializedObjectSibling(obj, "key")` | First nested value for key |
| `GetCasesByServiceAndQuestionAnswer(shortName, Dictionary, whiteList, blackList)` | Case numbers matching field answers/status |
| `GetDetailed(caseId)` | Full case (dates, answers, parties, queue, …) |
| `GetAnswerFromCase(caseId, friendlyId)` | Other case; **logged-in user must be tied to that case** |
| `GetAnswerFromPublishedCase(caseId, friendlyId)` | Submitted case; on thank-you: `self.Service.UniqueCaseId` |
| `GetPublishedCasePdf(customerId, uniqueId, writeToDisk)` | Thank-you: PDF `Name` + `Data` bytes |
| `GetCitizenInfoLookUp(pnr)` | Session Navet lookup; bypasses GDPR-stripped `self.Citizen` fields (not saved to DB) |
| `self.Session['key']` | HttpSession; any serializable value |
| `self.Citizen` | Logged-in person. GDPR: MaritalStatusCode, BirthPlace.*, CitizenData **not** populated unless LookUp |
| `self.Service` | Id, DisplayName, ShortName, Nr, ServiceVersion, UniqueCaseId, RequiresAuthentication/Signature, IsAnonymous, HasAlternativeSigning, IsQueueService, RequiresPayment, CustomerId, Properties, ServiceParameters. URL mall also: **SessionParameters** dict |
| `self.Page` | PageId, DisplayName, PageName, PageIndex, HTML, ClientLogic, HiddenBlocks, ShowInSummary, Layout, ActivationRule, GetBlocksInPage() |
| `self.Service.GetField(id)` | Field object (TypeOfField, Arguments, …) |

Citizen LookUp keys in the mall: ProtectedIdentity, ProtectedIdentityCivilRegister, FirstName, LastName, Adress, Postcode, City, Email, phones, alt address, WantEmailContact, MunicipalityKey, CitizenCaseRelations, …

## Full mall

```python
from Abou.Calamare.Web import PageNode
from System import *
from System.Collections.Generic import *

class InfoPage(PageNode):

	# I den här mallen hittar du korta beskrivningar av våra Pagenode-metoder, tillsammans med exempel.
	
	## FältId ##
	# Varje fält i en e-tjänst har ett unikt id som syns under Fältdetaljer på varje fält.
	# För att nå ett fält från kod, skriv 'x.id', där id är siffran i fält-id:t
	# Exempelvis 'x.1'
	
	## Initialize
	# Initialize körs när sidan laddas och kan användas för att förifylla fält och styra vilka block och fält som ska visas.
	def Initialize(self):
		## GetAnswer ##
		# Hämta svaret från ett fält.
		svar = self.GetAnswer('x.1')
		
		## GetAnswers ##
		# Används för ex. kryssrutor och tabellfält
		# Hämta svar som en lista
		svar = self.GetAnswers('x.1')
		
		## GetValueFromQuestionAlternative ##
		# Används för ex. radioknappar och kryssrutor
		# Få värdet i ett svarsalternativ, där "Separera text och värde" är ikryssat
		svarsvarde = self.GetValueFromQuestionAlternative('x.1')
		
		## GetAnswerFromQuestionAlternative ##
		# Används för ex. radioknappar och kryssrutor
		# Få texten i ett svarsalternativ, där "Separera text och värde" är ikryssat
		svarstext = self.GetAnswerFromQuestionAlternative('x.1')
		
		## SetAnswer ##
		# Sätter svaret i ett fält. Ange först fältet, och sedan det svar du vill sätta.
		self.SetAnswer('x.1', 'Svar')
		
		## SetAnswerIfEmpty ##
		# Sätter svaret i ett fält om det är tomt. Om det redan fanns ett svar, eller om invånaren byter svar, kommer inte den här metoden ändra svaret.
		self.SetAnswerIfEmpty('x.1', 'Svar om tomt')
		
		## SetQuestionText ##
		# Sätter rubriken på ett fält
		self.SetQuestionText('x.1','Fältrubrik')
		
		## GetOptions ##
		# Hämtar tillåtna svarsalternativ för till exempel kryssrute- och radioknappsfält
		svarsalternativ = self.GetOptions("x.1")
		
		## SetOptions ##
		# Används för ex. radioknappar och kryssrutor
		# För ett fält UTAN separerade värden:
		self.SetOptions("x.1", Array[String](["Alternativ A", "Alternativ B", "Alternativ C"]))
		# För ett fält MED separerade värden:
		self.SetOptions("x.2", Array[String]((["Alternativ A|A", "Alternativ B|B", "Alternativ C|C"])))
		# Text och värde separeras med | 
		# Första svarsalternativet har då texten "Alternativ A" och värdet "A"
		
		## SetOptionHelpTexts ##
		# Används för ex. radioknappar och kryssrutor
		# Sätter hjälptext för vardera svarsalternativ
		self.SetOptionHelpTexts("x.1", Array[str](["Hjälptext till Alternativ A", "Hjälptext till Alternativ B", "Hjälptext till Alternativ C"]))

		## SetDisabled ##
		# Sätter att ett fält ska vara inaktiverat eller inte, dvs om fältet ska gå att fylla i eller ej. Default är aktiverat
		# Sätter fältet till inaktiverat
		self.SetDisabled('x.1', True)
		# Sätter fältet till aktiverat
		self.SetDisabled('x.1', False)
		
		## SetRequired ##
		# Sätter att ett fält ska vara obligatoriskt eller inte
		# Sätter fältet till icke-obligatoriskt
		self.SetRequired("x.1", False)
		# Sätter fältet till obligatoriskt
		self.SetRequired("x.1", True)
		
		## SetHidden ##
		# Sätter att ett fält ska vara dolt eller inte.
		# Sätter fältet till dolt
		self.SetHidden("x.1", True)
		# Sätter fältet till icke dolt
		self.SetHidden("x.1", False)
		
		## SetHiddenBlock ##
		# Sätter att ett block ska vara dolt eller inte.
		# Sätter blocket till dolt
		self.SetHiddenBlock("BLOCK1", True)
		# Sätter blocket till icke dolt
		self.SetHiddenBlock("BLOCK1", False)
		
		## SetHiddenAndClearBlock ##
		# Tömmer alla fält i ett block och gömmer dem
		self.SetHiddenAndClearBlock("BLOCK1", True)
		# Visar ett block
		self.SetHiddenAndClearBlock("BLOCK1", False)
		
		## CopyTo ##
		# Kopierar svar mellan två fält. Bör vara samma sorts fält.
		kopieraTillFält = "x.1"
		kopieraFrånFält = "x.2"
		self.CopyTo(kopieraFrånFält, kopieraTillFält)
		
		## Loggmetoder ##
		## Dessa Loggar presenteras i "Visa skriptlogg" under "Förhandsvisa e-tjänst"
		self.LogDebug("Sträng")
		värde = self.GetAnswer('x.1')
		self.LogDebugObject({"Nyckel":värde})
		self.LogInfo("Sträng")
		värde = "Hej"
		self.LogInfoObject({"Nyckel":värde})
		self.LogError("Sträng")
		värde = "Hej"
		self.LogErrorObject({"Nyckel":värde})
		
		## GetAgeOnDate ##
		personnummer = self.Citizen.UserIdentity
		datum = "2026-03-03"
		self.GetAgeOnDate(personnummer, datum)
		
		## GetFriendlyFieldIdFromFieldNumber ##
		friendlyFieldId = self.GetFriendlyFieldIdFromFieldNumber(15)
		
		## SetValidationText ##
		# OBS: sätt alltid return self.Page efter valideringen, annars stoppas inte invånaren från att gå vidare
		self.SetValidationText("x.1", "Fel svar; Vänligen försök igen.")
		
		## Serialize / Deserialize / GetJsonDeserializedObjectSibling ##
		data = {
			"geometry": {
				"type": "Point",
				"coordinates": [18.0649, 59.3326]
			}
		}
		json_string = self.Serialize(data)
		deserialized = self.Deserialize(json_string)
		coordinates = deserialized["geometry"]["coordinates"]
		json_deserialized = self.Deserialize(json_string)
		coordinates = self.GetJsonDeserializedObjectSibling(json_deserialized, "coordinates")
		
		## GetCasesByServiceAndQuestionAnswer
		serviceShortName = "EX_TJANST"
		fieldsAndValues = {"EX_TJANST.3": "Ja"}
		statusWhiteList = []
		statusBlackList = ["Avslutat"]
		results = self.GetCasesByServiceAndQuestionAnswer(serviceShortName, Dictionary[str,str](fieldsAndValues), List[str](statusWhiteList), List[str](statusBlackList))
		
		## GetDetailed
		caseId = "250204-EX_TJANST-KW03"
		case = self.GetDetailed(caseId)
		
		## GetAnswerFromCase / GetAnswerFromPublishedCase / SetAnswerToPublishedCase
		otherCaseAnswer = self.GetAnswerFromCase(caseId, "x.1")
		otherCaseAnswer = self.GetAnswerFromPublishedCase(caseId, "x.1")
		otherCaseAnswer = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId, 'x.1')
		self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', "Ja")
		self.SetAnswerToPublishedCase("201021-ABC-AB12", 'x.1', "Nej")
		
		## GetCitizenInfoLookUp — kringgår GDPR-strip på self.Citizen (session only)
		citizen = self.GetCitizenInfoLookUp(self.Citizen.UserIdentity)
		
		## Service / Page / BLOCK / Field / Session — see mall comments in builder
		self.Session['MyKey'] = "Mitt värde"
		MyValue = self.Session['MyKey']
 
	def BeforeGetNextPage(self):
		pass
		
	def GetNextPage(self):
		return PageNode.GetNextPage(self)
		# return self.GetPage('Sida2')
		# return self.Page
```

Citizen LookUp, Service, Page, Block, and Field property dumps are in the builder mall verbatim; copy from the UI if you need a property not listed above. Do not log real personnummer in production.
