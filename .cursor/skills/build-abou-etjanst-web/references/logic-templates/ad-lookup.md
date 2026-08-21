# Hämta uppgifter om inloggad från AD

Tab: **Logik**. Internal node. Needs sysadmin `RestWrapperConfiguration` key **InternalWebSearch**. Class in mall is `page` — rename to the page system name.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Framework.Integration import IntegrationHttpRequest
from Abou.Calamare.Framework.Integration.RestWrapper import IRestWrapperServiceFactory
from System.Collections.Generic import Dictionary, List
from System.Web.Script.Serialization import JavaScriptSerializer

class page(PageNode):
    debugFieldId = 'x.8'
    def Initialize(self):
        #Följande konfiguration behöver finnas i Abou.Calamare.Framework.Integration.RestWrapper.RestWrapperConfiguration i sysadmin
        # "InternalWebSearch": {
        #     "IsEnabled": true,
        #     "IsCaseEventsEnabled": false,
        #     "ServiceType": "Abou.Calamare.Framework.Integration.RestWrapper.V2.RestWrapperServiceV2",
        #     "Url": "{addresstillinternalweb}/api/v1/activedirectoryuser/Search?apiapplication={apiapplication}&apikey={apikey}",
        #     "Password": lösenord,
        #     "UserName": användarnamn,
        #     "ExtendedConfigurationData": {
        #         "integrationHttpRequest.Data": "{'searchString':'{searchString}','searchProperty':'{searchProperty}','resultProperties':{resultProperties}}",
        #     }
        # }
        internalWebSearch = self.Resolve[IRestWrapperServiceFactory]().Create(self.IntegrationContext, "InternalWebSearch")

        request = IntegrationHttpRequest()
        request.Parameters = Dictionary[str,str](
            {
                "integrationHttpRequest.data.searchString":self.Citizen.UserIdentity, #värdet som ska sökas på, här satt till inloggad användares användarnamn. Obligatoriskt
                "integrationHttpRequest.data.searchProperty":"sAMAccountName", #egenskapen i AD:t som skall matcha värdet, här satt till kontonamn ett annat intressant värde kan vara distinguishedname. Obligatoriskt
                "integrationHttpRequest.data.resultProperties":"['sAMAccountName','manager','givenName','sn','mail','telephoneNumber','homePhone','mobile']", #exempel på egenskaper som skall hämtas alla värden som finns på avändaren kan hämtas, förnamn, efternamn, kontonamn och epost är default om ett tomt värde anges
            })

        #Hämta inloggad användare i AD
        try:
            result = internalWebSearch.Post(request)
            
            if (not result is None and not result.Result is None):
                properties = JavaScriptSerializer().Deserialize[Dictionary[str,List[str]]](result.Result)
                self.SetAnswer('x.1', properties['givenName'][0]) #Förnamn
                self.SetAnswer('x.2', properties['sn'][0]) #Efternamn
                self.SetAnswer('x.3', properties['sAMAccountName'][0]) #Användarnamn
                self.SetAnswer('x.4', properties['mail'][0]) #Epost
                self.SetAnswer('x.5', properties['telephoneNumber'][0]) #Telefon
                self.SetAnswer('x.6', properties['mobile'][0]) #Mobil
                self.SetAnswer('x.7', properties['manager'][0]) #Chef
        except:
            self.SetAnswer(self.debugFieldId, 'FEL vid hämtning av inloggad användare i AD')
            return
```
