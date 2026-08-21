# Förifyll värde med Ärendeväljarfältet

Tab: **Logik** on a page **after** the ärendeväljare. `GetAnswerFromCase` needs login and the user tied to that case.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        
        #hämta ärendenumret från Ärendeväljarfältet
        caseId = self.GetAnswer("ANGEFÄLTID")
        
        #hämta det gamla fältsvaret från ärendet
        answer = self.GetAnswerFromCase(caseId,"FältID för det fält du vill att svaret ska hämtas från")
        
        # skriv in det gamla fältsvaret i ett fält
        self.SetAnswer("ANGEFÄLTID",answer)

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
