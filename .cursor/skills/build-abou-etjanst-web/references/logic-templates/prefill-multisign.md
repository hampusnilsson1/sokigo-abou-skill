# Förifyll från Multipelsigneringsfält

Tab: **Logik**. Multi-sign answer is JSON: `SocialSecurityNumber`, `FirstName`, `LastName`, `Email`.

```python
from System.Web.Script.Serialization import JavaScriptSerializer
from Abou.Calamare.Web import PageNode

class InfoPage(PageNode):
    def Initialize(self):
        # Hämtar information från multipelsigneringsfältet
        answer = self.GetAnswer('ANGE FÄLTID')
        # Skapar en Dictionary<string, object> av svaret
        data = JavaScriptSerializer().DeserializeObject(answer)
        # Kopierar personnumret (SocialSecurityNumber) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['SocialSecurityNumber'])
        # Kopierar Förnamnet (FirstName) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['FirstName'])
        # Kopierar Efternamnet (LastName) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['LastName'])
        # Kopierar Epost (Email) till fältet med det ID man väljer
        self.SetAnswer('ANGE FÄLTID', data['Email'])
```
