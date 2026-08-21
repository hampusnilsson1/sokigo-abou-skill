# Fördjupad Navet-slagning med enkel lista

Tab: **Logik**. Children in a dropdown (`FetchMyChildren` / `FetchMyChildrenFlatList`), other guardian into multipelsigneringsfält. Relation `VF`. Children/guardians with protected identity are dropped or blocked. JSON for multi-sign: `SocialSecurityNumber`, `FirstName`, `LastName`, `Email`.

Also see [integrations/navet.md](../integrations/navet.md).

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.Integration import CitizenServiceProxy, ProxyRequest
from System.Web.Script.Serialization import JavaScriptSerializer
from System import Array, String

class InfoPage(PageNode):

	# Rullgardingslista
	dropDownFieldId = 'ANGEFÄLTID'
	# Multipelsigneringsfält
	multipleSignatureFieldId = 'ANGEFÄLTID'
	# Radioknapp - krävs flera signaturer?
	radiobuttonFieldId = 'ANGEFÄLTID'

	def Initialize(self):
		# barn innehåller mer information om varje barn, medan barnFlatList innehåller namn och personnummer
		# Barn med skyddad identitet följer inte med
		barn, barnFlatList = self.HamtaBarnFranNavet()

		if barnFlatList:
			self.SetOptions(self.dropDownFieldId, barnFlatList)
		else:
			self.SetOptions(self.dropDownFieldId, Array[String](""))
			self.SetValidationText(self.dropDownFieldId, 'Du är inte vårdnadshavare för något barn.')

	def GetNextPage(self):	
		ssp = CitizenServiceProxy()
		# Hämta ut valt barn ur rullgardingslistan
		valtBarn = ssp.GetIdentityFromFlatListAnswer(self.GetAnswer(self.dropDownFieldId))


		andraVardnadshavare = self.HamtaAndraVardnadshavareFranNavet(valtBarn)
		if andraVardnadshavare:
			if andraVardnadshavare == "Skyddad":
				# Om den andra vårdnadshavaren har skyddad identitet bör dennes uppgifter 
				# inte förifyllas i e-tjänsten. Det kan hanteras t.ex. genom att vårdnadshavaren 
				# utan skyddad identitet inte kan skicka in ärendet och får en instruktion för
				# annan hantering av ärendet.
				self.SetValidationText(self.dropDownFieldId, 'Du kan inte skicka in ett ärende i denna e-tjänst. Hör av dig till kontaktcenter för vidare hjälp med ditt ärende.')
				return self.Page
			else:
				self.SetAnswer(self.multipleSignatureFieldId, andraVardnadshavare)
				self.SetAnswer(self.radiobuttonFieldId, 'Ja')
				return self.GetPage('Multipelsignatur')
			
		# Om det inte finns en andra vårdnadshavare, gå vidare. Skriv in nedan vilken sida, annars går den direkt till nästa
		return PageNode.GetNextPage(self)

	def HamtaBarnFranNavet(self):
		# Barn med skyddad identitet följer inte med
		if(self.Citizen is not None):
			citizen = self.Citizen
			ssp = CitizenServiceProxy()
			
			# Skapa request för att hämta de barn den inloggade användaren är vårdnadshavare för
			request = ProxyRequest()
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True

			# Kontrollera om den inloggade användaren har barn
			if ssp.HasChildren(citizen.UserIdentity, request) == False:
				return None, None

			# Hämta barn från Navet
			children = ssp.FetchMyChildren(citizen.UserIdentity, request)
			children = self.TaBortBarnSkyddadIdentitet(children)
			
			# Hämta barn i kortare format från Navet
			childrenFlatList = ssp.FetchMyChildrenFlatList(citizen.UserIdentity, request)
			childrenFlatList = self.TaBortBarnSkyddadIdentitetFlatList(children, childrenFlatList)

			return children, childrenFlatList
		return None, None

	def HamtaAndraVardnadshavareFranNavet(self, valtBarn):
		ssp = CitizenServiceProxy()
		citizen = self.Citizen
		serializer = JavaScriptSerializer()
		
		# Skapa upp request för att hämta andra vårdnadshavare
		request = ProxyRequest()
		request.IdentityToRemoveInRelations = citizen.UserIdentity
		request.ParentsTypeOfRelationToChild = 'VF'
		request.RemoveDeregistratedRelation = True

		andraVardnadshavare = ssp.FetchMyParents(valtBarn, request)[0]
		if andraVardnadshavare:
			# Kontrollera ifall vårdnadshavare har skyddad identitet
			if andraVardnadshavare["ProtectedIdentity"] == "False" and andraVardnadshavare["ProtectedIdentityCivilRegister"] == "False":
				# Formattera andra vårdnadshavaren till json som kan användas till multipelsigneringsfältet
				andraVardnadshavareDict = dict(SocialSecurityNumber=andraVardnadshavare['SocialSecurityNumber'], FirstName=andraVardnadshavare['FirstName'], LastName=andraVardnadshavare['LastName'], Email='')
				andraVardnadshavarejson = serializer.Serialize(andraVardnadshavareDict)
				return andraVardnadshavarejson
			else:
				return "Skyddad"
		else:
			return None

	def TaBortBarnSkyddadIdentitet(self, children):
		# Kontrollera varje barn för att inte ta med de med skyddad identitet
		kontrolleradLista = []
		if children:
			for child in children:
				if child['ProtectedIdentityCivilRegister'] == "False" and child['ProtectedIdentity'] == "False":
					kontrolleradLista.append(child)
		return kontrolleradLista

	def TaBortBarnSkyddadIdentitetFlatList(self, children, childrenFlatList):
		# Kontrollera varje barn för att inte ta med de med skyddad identitet
		# Returnerar barnen i FlatList-format, dvs ["Förnamn efternamn, personnummer"]
		kontrolleradLista = []
		if children:
			for child in children:			
				if child['ProtectedIdentityCivilRegister'] == "False" and child['ProtectedIdentity'] == "False":
					childWithNoProtectedIdentity = [x for x in childrenFlatList if child['SocialSecurityNumber'] in x]
					childWithNoProtectedIdentity = str.format('{0} {1}, {2}', child['FirstName'], child['LastName'], child['SocialSecurityNumber'])
					kontrolleradLista.append(childWithNoProtectedIdentity)
		return Array[String](kontrolleradLista)
```
