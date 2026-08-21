# Inloggning (loggning)

Tab: **Logik**. Builder mall name **Inloggning**; the code is **system log** examples. Preview: **Visa skriptlogg**.

```python
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):

    def Initialize(self):

        #Exempel på loggning till Systemloggen i Abou
        #Du kan logga valfri text, fältsvar, svar från integrationer med mer
        
        #Debug-loggning
        self.LogDebug('DEBUGTEXT');

        #DebugObject-loggning
        self.LogDebugObject(self);

        #Info-loggning
        self.LogInfo('INFOTEXT');

        #InfoObject-loggning
        self.LogInfoObject(self);

        #Fel-loggning
        self.LogError('FELTEXT');

        #FelObject-loggning
        self.LogErrorObject(self);
```
