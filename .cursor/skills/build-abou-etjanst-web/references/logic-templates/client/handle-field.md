# Hantera fält

Tab: **Klientlogik**. Get/set/hide/empty one field, with or without a field instance. Split text/value on change.

```javascript
PageLogic = function() {
    var self = this;

    //Fältid
    var friendlyfieldid = "x.1";

    //Exempel på fält-logik med fält-instans
    //--------------------------------------

    //Hämta ett fält
    var field = self.GetField(friendlyfieldid);
    //Sätt svar
    //field.SetAnswer("test");

    //Sätt svar om fältet är tomt
    //field.SetAnswerIfEmpty("test");

    //Göm ett fält
    //field.SetHidden(true);

    //Visa ett fält som är dolt via klient-logik
    // field.SetHidden(false);

    //Töm ett fält
    //field.EmptyField();

    //Hämta fältsvar
    //var myanswer = field.GetAnswer();
    //alert(myanswer);

    // Hämta olika typer av fältsvar för kryssrutor och radioknappar med inställningen "Separera text och värde" när fältsvar ändras    
    // field.WhenEvent(function () {
    //     var myanswerFull = field.GetAnswer();
    //     var myanswerValue = field.GetValueFromQuestionAlternative();
    //     var myanswerDisplay = field.GetAnswerFromQuestionAlternative();
    //     self.SetAnswer("test.6", myanswerDisplay)
    // }, "change");

    //Exempel på fält-logik utan fält-instans
    //--------------------------------------
    //Sätt svar
    //self.SetAnswer(friendlyfieldid, "test");

    //Sätt svar om fältet är tomt
    //self.SetAnswerIfEmpty(friendlyfieldid, "test");

    //Göm ett fält
    //self.SetHidden(friendlyfieldid, true);

    //Visa ett fält som är dolt via klient-logik
    //self.SetHidden(friendlyfieldid, false);

    //Töm ett fält
    //self.EmptyField(friendlyfieldid);

    //Hämta fältsvar
    //var myanswer = self.GetAnswer(friendlyfieldid);
    //alert(myanswer);    
};
```
