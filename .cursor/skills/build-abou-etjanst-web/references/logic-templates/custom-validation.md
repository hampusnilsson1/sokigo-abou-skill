# Egen valideringstext

Tab: **Logik**. Custom check + `SetValidationText` + `return self.Page` so the citizen cannot continue.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def GetNextPage(self):
        #Vid en del användningsfall där validatorer inte täcker upp helt kan man skapa en egen validator med hjälp av Python.
        #Men för att informera användaren om vad som gör att den kommer tillbaka till samma sida kan det vara bra att
        #visa ett valideringsmeddelande på samma sätt som en validator gör. 
        #Detta går att åstakomma med hjälp av: self.SetValidationText

        #Hämta svar från det fält man vill basera valideringen på.
        #I detta exempel antar vi ett radioknappsfält med svarsalternativ "Ja" och "Nej"
        
        fieldId = 'ANGE FÄLTID'

        answer = self.GetAnswer(fieldId)

        #Om man svarar nej i fältet får man inte gå vidare
        if(answer.Contains('Nej')):
            self.SetValidationText(fieldId, 'ANGE FELMEDDELANDE HÄR')
            return self.Page
        
        #Annars går vi vidare till nästa sida
        return PageNode.GetNextPage(self)
```
