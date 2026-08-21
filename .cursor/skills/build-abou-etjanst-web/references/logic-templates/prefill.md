# Förifyll värden

Tab: **Logik**. Copy fields, läggtillrad JSON (`Answer1`…), dynamic `SetOptions`, split `"synligt|hemligt"`.

```python
from System import Array
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):

        #Förifyllnad

        #Byta rubrik för fält
        self.SetQuestionText('ANGEFÄLTID', 'ANGE ÖNSKAD RUBRIK')
    
        #Hämta ett fältsvar
        answer = self.GetAnswer("ANGEFÄLTID")

        #Skriv in fältsvaret i ett annat fält om det är tomt
        self.SetAnswerIfEmpty("ANGEFÄLTID", answer)
 
        #Kopiera ett värde från ett fält till ett annat
        self.CopyTo('ANGE_FRÅN_FÄLTID', 'ANGE_TILL_FÄLTID')

    
        #Förifyllnad av Lägg till rad-fält
    
        personuppgifter = '[{"Answer1":"196305011234","Answer2":"Ulla","Answer3":"Andersson","Answer4":"070-1122334","Answer5":"mamma"},{"Answer1":"199010075678","Answer2":"Kalle","Answer3":"Andersson","Answer4":"070-55667788","Answer5":"barn"}]' 
        self.SetAnswer("ANGEFÄLTID",personuppgifter)
    

        #Förifyll dynamiska värden till rullgardinslista-fält
    
        #hämta ett svar med ålder valt
        alder = self.GetAnswer("ANGEFÄLTID")
        #skapa en array-variabel
        kurs= []        
    
        #skriv in värden i arrayen beroende på valet för ålder 
        if alder.Equals("20-25"):
            kurs = ["Balett","Bugg"]
    
        if alder.Equals("26-30"):
            kurs = ["Vals","Hip-hop","Tango"]
    
        if alder.Equals("31-35"):
            kurs=["Salsa","Samba"]
    
        #skriv in valet i ett rullgardinslista-fält
        self.SetOptions("ANGEFÄLTID", Array[str]((kurs)))

        #Hantera hemliga värden i flervalsfält.
        #Använd hemliga värden när det inte är önskvärt att visa det valda värdet för användaren.
        
        #Förifyll ett flervalsfält med "synligt värde|hemligt värde"
        #För användaren visas valen aaa, bbb och cccc.
        self.SetOptions("ANGEFÄLTID",Array[str](["aaa|hemligt1","bbb|hemligt2","cccc|hemligt3"]))

        #Hämta dolt värde från en flervalslista med separerade värden.
        self.GetValueFromQuestionAlternative('ANGEFÄLTID')

        #Hämta synligt värde från en flervalslista med separerade värden.
        self.GetAnswerFromQuestionAlternative('ANGEFÄLTID')


    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
