# Utökad invånarinformation

Tab: **Logik**. Full PersonPost JSON via `ICitizenServicePluginFactory` + `GetCitizenAsJson`. Store in `self.Session['personPost']` and reuse on later pages (do not call Navet again). JSON shape differs for Navet vs Abou TEST vs TEIS.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Framework.Configurations import IConfigurationReader
from Abou.Calamare.Framework.CitizenService import ICitizenServicePluginFactory, CitizenServiceConfiguration
from System.Web.Script.Serialization import JavaScriptSerializer

class InfoPage(PageNode):
    def GetNextPage(self):
        # Exempel på hur man kan hämta en fullständig personpost för en invånare

        citizenServicePluginFactory = self.Resolve[ICitizenServicePluginFactory]()
        configReader = self.Resolve[IConfigurationReader]()
        citizenServiceConfiguration = configReader.GetConfiguration[CitizenServiceConfiguration](self.Service.CustomerId)
        citizenService = citizenServicePluginFactory.CreateCitizenServicePlugin(citizenServiceConfiguration.CitizenServicePluginType, self.Service.CustomerId)

        socialSecurityNumber = self.Citizen.UserIdentity.replace('-', '')
        citizenDataJson = citizenService.GetCitizenAsJson(socialSecurityNumber)

        # Deserialisera personposten och lagra som sessionsvariabel
        citizenData = JavaScriptSerializer().DeserializeObject(citizenDataJson)
        self.Session['personPost'] = citizenData
        # OBS: Sessionsvariabeln ska sedan användas i efterkommande sidor istället för att hämta på nytt!

        return PageNode.GetNextPage(self)

        # ------- En efterkommande sida -------

        citizenData = self.Session['personPost']
        if (not citizenData is None):
            self.LogDebug(JavaScriptSerializer().Serialize(citizenData))

            ## Invånarinformation från Navet, ex:
            #if(not citizenData['Namn'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Namn']['Fornamn']))
            #    self.SetAnswer('Field.Id', unicode(citizenData['Namn']['Efternamn']))
            #if(not citizenData['Folkbokforing'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Folkbokforing']['Fastighetsbeteckning']))
            #if (not citizenData['Adresser'] is None and not citizenData['Adresser']['Folkbokforingsadress'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Adresser']['Folkbokforingsadress']['CareOf']))
            #if (not citizenData['Civilstand'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Civilstand']['CivilstandKod']))
            #if (not citizenData['Relationer'] is None and citizenData['Relationer'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relationer'][0]['Relationstyp']))
            #if (not citizenData['Fodelse'] is None and not citizenData['Fodelse']['HemortSverige'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Fodelse']['HemortSverige']['Fodelseforsamling']))

            ## Invånarinformation från Abou TEST, ex:
            #self.SetAnswer('Field.Id', unicode(citizenData['FirstName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['LastName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['MaritalStatusCode']))
            #if (not citizenData['Address'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Address']['CareOf']))
            #if (not citizenData['Relatives'] is None and citizenData['Relatives'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relatives'][0]['TypeOfRelation']))                       
            #if (not citizenData['BirthPlace'] is None):
            #    self.SetAnswer('Field.Id', unicode(citizenData['BirthPlace']['Community']))

            ## Invånarinformation från TEIS, ex:
            #self.SetAnswer('Field.Id', unicode(citizenData['GivenName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['LastName']))
            #self.SetAnswer('Field.Id', unicode(citizenData['CivilStatus']))
            #if (not citizenData['Relations'] is None and citizenData['Relations'].Count > 0):
            #    self.SetAnswer('Field.Id', unicode(citizenData['Relations'][0]['Relationship']))
```
