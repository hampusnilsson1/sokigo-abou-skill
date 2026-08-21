# Betalning (för PaymentPage.aspx)

Tab: **Logik** on the **Betalningssida**. Amount and order text. Read answers via `GetAnswerFromFieldId(fields, fieldId)`, not `GetAnswer`.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        answer = self.GetAnswer('')

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)

    #För att logiken för betalningen ska fungera som önskat ska fältsvar hämtas via den här metoden istället för den vanliga GetAnswer
    def GetAnswerFromFieldId(self,fields,fieldId):
        return filter(lambda f: f.FieldId == fieldId, fields)[0].Answer

    def HasPaymentInfo(self):
        return True
    
    #Ange ordertext här
    def GetPaymentOrderText(self):
        return 'MIN ORDERTEXT'

    #Ange ev. felsida här
    #def GetPaymentErrorPage(self):
        #return 'felsidan'

    #här beräknas summan
    def CalculatePaymentAmount(self, fields):
        #Definiera konstanter
        baseAmount = 100
        numItemsFieldId='ANGEFÄLTID'
        nameFieldId='ANGEFÄLTID'
        
        #Hämta och parsa fältsvar från fields parametern istället för vanliga GetAnswer
        numItems = int(self.GetAnswerFromFieldId(fields, numItemsFieldId))
        strName = self.GetAnswerFromFieldId(fields, nameFieldId)

        #Beräkna summan
        amount = numItems * baseAmount
        
        if(strName=='emelie'):
            amount = amount * 0.75 # 25% rabatt !!

        return amount
```
