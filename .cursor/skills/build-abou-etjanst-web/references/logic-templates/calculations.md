# Summeringar och beräkningar

Tab: **Logik**. `int.TryParse` via `GetAnswerAsInt`. Läggtillrad: `AnswersModel.Deserialize`, cells `Answer1`, `Answer2`.

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Web.UI.EGovLib.Fields.Models import AnswersModel

class InfoPage(PageNode):

    #hämtar ett fältsvar och returnerar det konverterat till siffra, 0 returneras om det ej går att konvertera till siffra.
    def GetAnswerAsInt(self, friendlyFieldId):
        answer = self.GetAnswer(friendlyFieldId)
        result = int.TryParse(answer)
        if result[0]:
            return result[1]        
        return 0;

    def Initialize(self):

        #addera flera fältsvar som heltal och skriv in dem i fält 

        #hämta värden som heltal
        arvoden = self.GetAnswerAsInt('ANGEFÄLTID')
        socialaavgifter = self.GetAnswerAsInt('ANGEFÄLTID')
        lokalhyra = self.GetAnswerAsInt('ANGEFÄLTID')

        #summera
        summa = arvoden + socialaavgifter + lokalhyra

        #skriv in summan i ett fält
        self.SetAnswer('ANGEFÄLTID', str(summa))

        #Beräkna med läggtill radfält
        #Läggtillradfälts bryter ur celler som answer1 och answer2 = kolumn 1,2 
        
        #Hämta fältsvar från läggtill-radfält
        pubTot = self.GetAnswer("ANGEFÄLTID")
        
        #deserialisera svaret
        pubTotModels = AnswersModel.Deserialize(pubTot)
        #om det gick att deserialisera, loopa igenom raderna och multiplicera cellerna Answer1 & Answer2
        if pubTotModels is not None:
            sum = 0
            for pubTotModel in pubTotModels:
                Answer1 = int.Parse(pubTotModel.Answer1)
                Answer2 = int.Parse(pubTotModel.Answer2)         
                sum += Answer1 * Answer2                                  
            self.SetAnswer("ANGEFÄLTID",str(sum))
```
