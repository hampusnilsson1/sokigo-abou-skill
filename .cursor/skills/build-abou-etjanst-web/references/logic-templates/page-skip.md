# Logikhopp

Tab: **Logik**. `GetNextPage` must return a page. `GetPage('Systemnamn')` jumps. Only one return path runs — uncomment/adapt a single pattern.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def GetNextPage(self):
        #exempel: logikhopp beroende på val i tjänsten 
        answer = self.GetAnswer('ANGEFÄLTID')
        if answer.Contains('Bil'):
            return self.GetPage('UppgifterBil')
        if answer.Contains('Båt'):
            return self.GetPage('UppgifterBat')
        return self.GetPage('SummaryPage')


        #exempel: logikhopp beroende på flera val i tjänsten 
        answer1 = self.GetAnswer('ANGEFÄLTID')
        answer2 = self.GetAnswer('ANGEFÄLTID')
        if answer1.Contains('Bil') and answer2.Contains('Flygplan'):
            return self.GetPage('UppgifterBil&Flyg')
        return self.GetPage('SummaryPage')

        
        #exempel: logikhopp beroende på om ett val är ifyllt eller inte
        answer = self.GetAnswer('ANGEFÄLTID')
        if not answer:
            return self.GetPage('Fastighetsbeteckning2')
        return self.GetPage('Karta')

        #exempel: logikhopp obereoende av val i e-tjänsten
        return self.GetPage('Kontaktperson')
```
