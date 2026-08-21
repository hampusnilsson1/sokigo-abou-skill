# Hantera visning av fält och block

Tab: **Logik**. Server-side hide/disable (also after Nästa). For same-page instant hide, use klientlogik.

```python
from Abou.Calamare.Web import PageNode
# Hantera visning av fält och block
class InfoPage(PageNode):
    def Initialize(self):
        friendlyFieldId = 'x.1'
        shouldHide = True
        shouldDisable = True
        # Döljer eller visar ett fält med matchande id
        self.SetHidden(friendlyFieldId, shouldHide)

        # Sätter ett fält inaktivt så att det inte kan redigeras.
        self.SetDisabled(friendlyFieldId, shouldDisable)
        
        blockId = 'BLOCK1'
        # Döljer eller visar ett helt block med matchande ID och gör
        # SetHidden på alla fält som ingår i blocket
        self.SetHiddenBlock(blockId, shouldHide)


    def GetNextPage(self):        
        return PageNode.GetNextPage(self)
```
