# Hantera obligatoriska fält som döljs i klient-logik

Tab: **Logik**. If JS hides a required field, clear required in `BeforeGetNextPage` or validation blocks navigation with no visible error.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        #Ett obligatoriskt fält där logik påverkar om det är obligatoriskt eller inte bör alltid initialt sättas som obligatoriskt:
        self.SetRequired("ANGEFÄLTID", True)

    def BeforeGetNextPage(self):
        #Om ett obligatoriskt fält döljs i klient-logik måste man ange att fältet ej ska vara obligatoriskt
        #för att undvika stoppande och osynlig validering i samband med att sidhopp sker:
        self.SetRequired("ANGEFÄLTID", False)

    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
