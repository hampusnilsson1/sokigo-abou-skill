# Filuppladdningsfältet

Tab: **Logik**. Needs file field with **AllowMultiple** and **Kräver filtyp**, **Separera text och värde**, empty svarsalternativ (types set in Python). `HasUploadedTypes` checks the **value** after `|`.

```python
### Denna mall fungerar med följande.
# 1. Ett filuppladdningsfält
# 2. AllowMultiple och RequireFileType satt till true
# 3. Inga alternativ under Svarsalternativ, samt true under Separera text och värde
from System import Array
from Abou.Calamare.Web import PageNode

fileUploadFieldId = "x.2"

# Filtyper använder sig av samma gränssnitt som kryssrutefältet
# I det här exemplet kör vi med Separera text och värde, detta görs med tecknet '|'
requiredTypes = ["Nåt vi vet att vi behöver|vi-behover", "Nåt mer vi redan känner till|nat-mer"]

# Obligatoriska filtyper kollas med värdedelen av alternativen, dvs det efter '|'-tecknet
requiredTypeValues =    ["vi-behover"               , "nat-mer"]
requiredTypeDisplayed = ["Nåt vi vet att vi behöver", "Nåt mer vi redan känner till"]
# Om vi inte har separerade värden räcker det att bara jobba med visningsvärdena.

class InfoPage(PageNode):
    # När vi anländer till sidan kan vi dynamiskt ange filtyper för filuppladdningsfältet
    def Initialize(self):
        # Sätt fältrubrik, för att indikera obligatoriska element
        self.SetQuestionText(fileUploadFieldId, "Ladda up bilagor, (obligatoriska typer: " + ", ".join(requiredTypeDisplayed) + ")")
        
        # Vi hämtar alternativ som kan bero på andra system eller logik under e-tjänstekörningen
        integrationTypes = self.GetIntegrationTypes()
        
        ## Vi lägger ihop listorna och sorterar för användarvänligheten
        allTypes = sorted(integrationTypes + requiredTypes)
    
        # Och nu blir alternativen tillgängliga för fältet.
        self.SetOptions(fileUploadFieldId, Array[str](allTypes))

    # Vid navigering till nästa sida kan vi lägga till validering som 
    # verifierar att alla obligatoriska filtyper har blivit uppladdade
    def GetNextPage(self):
        fileUploadField = self.Service.GetField(fileUploadFieldId)
        if (not fileUploadField.HasUploadedTypes(Array[str](requiredTypeValues))):
            self.SetValidationText(fileUploadFieldId, "Det saknas filtyper. Du måste skicka med " + (", ".join(requiredTypeDisplayed)))
            return self.Page
        
        return PageNode.GetNextPage(self)
    
    def GetIntegrationTypes(self):
        integrationTypeSessionKey = "typesFromMyIntegration-" + self.Service.UniqueCaseId
        if (self.Session[integrationTypeSessionKey] == None):
            # Om alternativen ex. behöver hämtas från ett externt api kan det
            # vara bra att spara listan i sessionen istället för skicka nya anrop när vi besöker sidan på nytt.
            self.Session[integrationTypeSessionKey] = ["Bild på registreringsplåt|bild-registreringsplåt", "Bild på stötfångare|bild-stötfångare"]
        return self.Session[integrationTypeSessionKey]
```
