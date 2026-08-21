# Hantera flera fält och block samtidigt

Tab: **Klientlogik**. Batch empty/hide/show fields and blocks.

The mall as shipped uses `ffidMoreInfo` without declaring it. Declare that id (or reuse `ffidYesno`) before calling `EmptyFields` / `SetHiddenFields`.

```javascript
PageLogic = function() {
    var self = this;

    //Fältids och blockids
    var ffidYesno = "x.3";
    var ffidDropdown = "x.4";
    var block1 = "BLOCK1";
    var block2 = "BLOCK2";
    var block3 = "BLOCK3";

    //Töm flera fält samtidigt
    self.EmptyFields([ffidMoreInfo, ffidDropdown]);

    //Göm flera fält samtidigt
    self.SetHiddenFields([ffidMoreInfo, ffidDropdown], true);
    
    //Visa flera fält  som är dolda via klient-logik samtidigt
    self.SetHiddenFields([ffidMoreInfo, ffidDropdown], false);
    
    //Göm flera block samtidigt
    self.SetHiddenBlocks([block1, block2, block3], true);

    //Visa flera block som är dolda via klient-logik samtidigt
    self.SetHiddenBlocks([block1, block2, block3], false);
};
```
