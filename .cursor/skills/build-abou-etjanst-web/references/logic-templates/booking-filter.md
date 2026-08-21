# Filtrera bokningsbara tillfällen

Tab: **Logik**. `SlotFilter` on a booking field. Filters stack (AND).

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Contracts.Reservation import SlotFilter

class InfoPage(PageNode):
    def Initialize(self):
        reservationField = self.Service.GetField('Ange Fält-id för bokningsfältet')
        slotFilter = SlotFilter() # Skapa SlotFilter-objekt för alla inställningar som önskas.
        reservationField.SetSlotFilter(slotFilter) # ställ in fältet att använda inställningsobjektet
        
        # Alla inställningar läggs ihop för att utöka filtreringen. Tillfällen som inte matchar angivna filter förkastas.
        # Om inget anges sker ingen filtrering på den inställningen.
        
        # Visa bokningstillfällen som ägs av handläggare med angivna inloggningsnamn.
        slotFilter.Admins = ['adminuser1', 'adminuser2']
        
        # Filtrera på Fritext. Tar bara med tillfällen som innehåller angiven sträng.
        # Följande inställning skulle exempelvis matcha 'Loppis i parken' och 'Loppis på torget'
        slotFilter.ContainsText = 'loppis'
        
        # Följande inställningar bestämmer vilka kalenderdagar från dagens datum som skall visas
        # Med följande inställning kan man aldrig boka ett tillfälle på samma dag, nästföljande dag, eller tillfällen längre fram än fem dagar
        slotFilter.DaysUntilFirst = 2 # visar inte dagens eller nästföljande dags tillfällen
        slotFilter.DaysUntilLast = 5  # visar bara tillfällen fem dagar framåt
        
        # ExcludeWeekend = True gör att lördagar och söndagar inte räknas med vid beräkning av DaysUntilFirst och DaysUntilLast.
        # Varje vardag kommer då att räknas som en sammanhängande serie.
        # Om vi bara har bokningstillfällen på vardagar och har DaysUntilFirst = 2
        # vore det exempelvis inte möjligt att boka ett måndagstillfälle på föregående fredag
        slotFilter.ExcludeWeekend = True # Grundinställning är False
        
        # ExcludeDays kan ses som en utökning av ExcludeWeekend.
        # Här kan man skriva in en lista med datum som ska fungera som helger. Anges i formatet yyyy-MM-dd
        slotFilter.ExcludeDays = ['2020-12-23', '2020-12-24', '2020-12-25', '2020-12-26', '2020-12-31', '2021-01-01']
        
        # En enklare inställning som säkerställer att bokning inte kan göras senare än x antal timmar innan tillfället
        slotFilter.MinimumHoursBeforeTime = 2
        

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
