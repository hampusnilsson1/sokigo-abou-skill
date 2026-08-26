# Använda url-parametrar

Tab: **Logik**. From **2019.2**. Prefill from query string, stored in `self.Service.SessionParameters` (string dict). Product page: [functionality.md](../../../abou-platform/references/functionality.md) *Värden som parametrar*.

Example URL: `Siteurl/Etjänstenamn?Smak=sur&Frukt=citron` or `…/GRUSK?skola=Lyckoskolan&årskurs=3`. Missing keys throw — check `in` first. Dict keys are **case sensitive** (`Frukt` vs `frukt`).

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        #I det här exemplet antas det att e-tjänsten har startats med parametrar
        #Det betyder att man i anropet till e-tjänsten anget parametrar i urlen
        #I det här exemplet anropas abou med parametrarna 'Smak' och 'Frukt'
        #Urlen ser då ut såhär 'Siteurl/Etjänstenamn?Smak=sur&Frukt=citron'
        #Dessa parametrar lagras i propertyn self.Service.SessionParameters
        #self.Service.SessionParameters är en dictionary med strängar. 
        
        #Exempel på att hämta ut en parameter och förifylla ett fält
        #notera att om Smak inte skulle finnas i dictionaryn kommer detta smälla. 
        #Var noga med att kolla om nycklar finns vid implementation där parameterlistan är okänd innan man försöker hämta ut dom.
        smak = self.Service.SessionParameters['Smak']
        friendlyFieldId = 'x.1'
        self.SetAnswer(friendlyFieldId, smak)
        
        #Ett säkrare sätt att kolla om värdet finns i dictionaryn.
        #Exempel på användning
        
        #Försök hämta värdet för parametern 'Frukt'
        friendlyFieldId2 = 'x.2'
        
        if 'frukt' in self.Service.SessionParameters:
            self.SetAnswer(friendlyFieldId2, self.Service.SessionParameters['frukt'])
        else:
            self.SetAnswer(friendlyFieldId2, 'Värdet finns inte')

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
