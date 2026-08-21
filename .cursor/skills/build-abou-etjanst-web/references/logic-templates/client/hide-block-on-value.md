# Göm block när fält får ett visst värde

Tab: **Klientlogik**. `field.When` equals / notequals / contains / notcontains, plus custom compare.

```javascript
PageLogic = function() {
    var self = this;

    //Fältids och blockids
    var ffidYesno = "x.3";
    var bidMoreInfo = "BLOCK1";

    //Hämta ett fält med radioknappar med svarsalternativ Ja och Nej
    var field = self.GetField(ffidYesno);

    //Ange initialt värde
    field.SetAnswer("Ja");

    //När fältsvaret blir Ja, visa blocket
    field.When("equals", "Ja", function() {
        //visa ett block som är dolt via klient-logik
        self.SetHiddenBlock(bidMoreInfo, false);
    });

    //När fältsvaret blir Nej, göm blocket
    field.When("equals", "Nej", function() {
        //dölj blocket
        self.SetHiddenBlock(bidMoreInfo, true);
    });

    //För kryssrutor anges flera svar samtidigt så här (i samma ordning som svarsalternativen):
    //field.When("equals", "Ja;Nej", function(){
    //	self.SetHiddenBlock(bidMoreInfo, false);		
    //});

    //Det går även att göra detta inverterat dvs när svaret skiljer sig från det man jämför med
    //field.When("notequals", "Nej", function() {
        //visa om svaret inte är "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Det går även att kolla om fältets svar innehåller en sträng man jämför med (Obs case sensetive)
    //field.When("contains", "Nej", function() {
        //visa om svaret innehåller "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Det går även att kolla om fältets svar inte innehåller en sträng man jämför med (OBS case sensetive)
    //field.When("notcontains", "Nej", function() {
        //visa om svaret inte innehåller "Nej"
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
    
    //Skulle inte ovanstånde jämförelser räcka till kan man skriva en egendefinerad function som tar emot ett svar och ett värde och jämför på ett eget sätt.
    //Definera egen jämförelsefunktion
    //var ownFunc = function (answer, compareTo){
        //här skriver man egen logik, i det här exemplet så blir resultatet samma som att använda 'equals' men man kan alltså skriva vad man vill här och skicka med det till self.When
    //    return answer === compareTo;
    //};
    
    //Skicka med funktionen till self.When
    //self.When(ownFunc, value, function (){
        //self.SetHiddenBlock(bidMoreInfo, true);
    //});
};
```
