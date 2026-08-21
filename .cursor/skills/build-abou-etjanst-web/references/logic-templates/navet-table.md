# Fördjupad Navet-slagning med tabellfältet

Tab: **Logik**. Same Navet flow using `TableFieldModel` + `SetAnswerIfEmpty`. Selected child identity = `tableAnswerModel.Answers[0]`. Does **not** filter protected identity like the dropdown mall — add that if needed.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.Integration import CitizenServiceProxy, ProxyRequest
from System.Web.Script.Serialization import JavaScriptSerializer
from Abou.Calamare.Web.UI.EGovLib.Fields import TableFieldModel
from System.Collections.Generic import List

class InfoPage(PageNode):
	
	def GetTableFieldModel(self,headers,propertyNames,propertyList,widths):
		# help method to support a dictionary with property names and values
		model = TableFieldModel()
		model.Widths = List[int](widths)
		model.Headers = List[str](headers)
		model.Rows = List[List[str]]()
		for i, val in enumerate(propertyList):
			vals = List[str]()
			for i2, valname in enumerate(propertyNames):
				if(valname in val):
					vals.Add(val[valname])
				else:
					vals.Add('')
			model.Rows.Add(vals)
		return model

	def Initialize(self):		
		if(self.Citizen is not None):
			citizen = self.Citizen
			ssp = CitizenServiceProxy()
			serializer = JavaScriptSerializer()
			
			# define the id for you table field
			tableFieldId = 'ANGEFÄLTID'
			
			# declare request to only get children logged in user is legal guardian for
			request = ProxyRequest()
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True
			children = ssp.FetchMyChildren(citizen.UserIdentity, request)
			
			# define the table here, with column widths and column headers
			model = self.GetTableFieldModel(['Förnamn','Efternamn','Personnummer','Födelseort'],['FirstName','LastName','SocialSecurityNumber','Community','SocialSecurityNumber'],children,[3,3,3,3])
			
			# serialize table
			answer = serializer.Serialize(model)
			
			# write serialized table to table field
			self.SetAnswerIfEmpty(tableFieldId,answer)
			
			# check if logged in user is legal guardian for any child, if not set validation text
			if(ssp.HasChildren(citizen.UserIdentity, request) == False):
				self.SetValidationText(tableFieldId,'Du är inte vårdnadshavare för något barn.')

	def GetNextPage(self):	
		if(self.Citizen is not None):
			citizen = self.Citizen
			serializer = JavaScriptSerializer()
			ssp = CitizenServiceProxy()
			
			# get answer, social security number for choosen child in this case, from table field
			tableFieldId = 'ANGEFÄLTID'
			tableAnswer = self.GetAnswer(tableFieldId)
			tableAnswerModel = serializer.Deserialize[TableFieldModel](tableAnswer)
			currentChildIdentity = tableAnswerModel.Answers[0]
			
			# declare request to only get other legal guardians for choosen child
			request = ProxyRequest()
			request.IdentityToRemoveInRelations = citizen.UserIdentity
			request.ParentsTypeOfRelationToChild = 'VF'
			request.RemoveDeregistratedRelation = True
			
			radiobuttonFieldId = 'ANGEFÄLTID'
			multipleSignatureFieldId = 'ANGEFÄLTID'

			if(ssp.HasParent(currentChildIdentity, request)):
				# if we have an other legal guardian show page with MultipelSigneringsFältet and set field answers
				otherLegalGuardian = ssp.FetchMyParents(currentChildIdentity, request)[0]
				otherLegalGuardianDict = dict(SocialSecurityNumber=otherLegalGuardian['SocialSecurityNumber'], FirstName=otherLegalGuardian['FirstName'], LastName=otherLegalGuardian['LastName'], Email='')
				otherLegalGuardianjson = serializer.Serialize(otherLegalGuardianDict)
				self.SetAnswer(radiobuttonFieldId, 'Ja')
				self.SetAnswer(multipleSignatureFieldId, otherLegalGuardianjson)
				return self.GetPage('Multipelsignatur')
			else:
				# no other legal guardian, reset field answers in MultipelSigneringsFältet and show summary page
				otherLegalGuardianDict = dict(SocialSecurityNumber='', FirstName='', LastName='', Email='')
				otherLegalGuardianjson = serializer.Serialize(otherLegalGuardianDict)
				self.SetAnswer(radiobuttonFieldId, 'Nej')
				self.SetAnswer(multipleSignatureFieldId, otherLegalGuardianjson)
				return self.GetPage('SummaryPage')
		
		return PageNode.GetNextPage(self)
```
