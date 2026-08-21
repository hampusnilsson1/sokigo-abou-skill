# Tacksida

Tab: **Logik** on thank-you. Hook is `Published(self)`, not `GetAnswer`. Return `PublishedResult` (`Success`, `Message`). `Success = False` mails via `CalamareErrorNotificationServiceConfiguration` and sets `Cases.FailedIntegration`.

Also: [pagenode-api.md](pagenode-api.md) thank-you methods, Confluence `IPythonCaseService` in `../logic.md`.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Contracts import PublishedResult

class InfoPage(PageNode):
    # Tacksidans python-skript anropas efter att ett ärende har skickats in
    def Published(self):
        ###
        ## PageNode innehåller en referens till ärendets ID (self.Service.UniqueCaseId)
        ## som kan användas till att slå upp eller uppdatera ärendets fältsvar
        ## Men det är möjligt att ange vilket UniqueCaseId som helst
        ## om det hör till ett inlämnat ärende.
        # self.SetAnswerToPublishedCase('101010-kortnamnet-XX00', 'x.1', 'Updated in another case')
        
        ###
        ## Hämta ett fältsvar från det publicerade ärendet.
        answer1 = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1')
        self.LogDebug("self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1') => " + answer1)
        
        ###
        ## Sätta fältsvar på ett publicerat ärende
        self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', 'Nytt värde angivet')
        self.LogDebug("self.SetAnswerToPublishedCase(self.Service.UniqueCaseId, 'x.1', 'Nytt värde angivet')")
        
        answer1 = self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1')
        self.LogDebug("self.GetAnswerFromPublishedCase(self.Service.UniqueCaseId,'x.1') => " + answer1)
        
        ###
        ## Hämta ärende-PDF för ett publicerat ärende (från FileStorageArea om den redan existerar annars som en ny renderad case-PDF) för att skicka ärende-PDF vidare till ett annat system
        ## Metoden GetPublishedCasePdf har parametrar CustomerId (Integer), CaseUniqueId (String) och WriteToFileStorageArea (Bool) returnerar ett objekt som består av egenskaperna Name och Data
        ## Name - String (filnamn för ärende-PDF i Abou)
        ## Data - Byte[] (ärende-PDF innehåll)
        ## Vill man även spara ärende-PDF till FileStorageArea i filsystemet (den kommer inte att ersättas om den redan existerar) anger man True som sista parameter (WriteToFileStorageArea) i anropet
        casePdf = self.GetPublishedCasePdf(self.Service.CustomerId, self.Service.UniqueCaseId, False)
        self.LogDebug(casePdf.Name)
        
        ###
        ## Returtypen är PublishedResult med medlemmarna Success och Message
        result = PublishedResult()
        
        # När Success = False skickas ett felmeddelande till epost enligt inställningar i
        # Abou.Calamare.Framework.Configurations.CalamareErrorNotificationServiceConfiguration
        # (Det samma gäller när skriptkörningen får exekveringsfel)
        # Ange True för att indikera att allt gått bra.
        # Sparas i databasen på kolumn Cases.FailedIntegration
        result.Success = True
        
        # Message kan innehålla info om hur skriptkörningen gått eller annan information
        # Sparas i databasen på kolumn Cases.PluginData
        result.Message = "Tacksidans skript körde utan fel."
        
        return result
```
