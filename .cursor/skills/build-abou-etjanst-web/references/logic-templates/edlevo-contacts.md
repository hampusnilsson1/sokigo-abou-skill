# Edlevo / Procapita contacts

Tab: **Logik**. Child page uses GET after Navet. Thank-you uses POST after submit. Needs sysadmin RestWrapper key **`procapita1_1`** (same product as Edlevo). Rename the class to the page system name.

Full field map and pitfalls: [edlevo.md](../integrations/edlevo.md).

```python
from Abou.Calamare.Web import PageNode
from Abou.Calamare.Framework.Integration.RestWrapper import *
from System.Web.Script.Serialization import JavaScriptSerializer

class ThankYou(PageNode):
    wrapperName = "procapita1_1"
    skoltypFieldId = "x.262"
    rollFieldId = "x.166"

    def Initialize(self):
        self.SendUpdatedContactsToProcapita()

    def GetProcapitaWrapper(self):
        return self.Resolve[IRestWrapperService](self.wrapperName)

    def GetProcapitaUri(self, elevPnr, skoltyp):
        url = self.GetProcapitaWrapper().Configuration.Url
        return url.format((elevPnr or "").replace("-", ""), skoltyp)

    def HamtaKontakterFranEdlevo(self, elevPnr, skoltyp):
        request = RestWrapperService.HttpRequest()
        request.Uri = self.GetProcapitaUri(elevPnr, skoltyp)
        response = self.GetProcapitaWrapper().Get(request)
        if not response:
            return None
        try:
            return JavaScriptSerializer().DeserializeObject(response)["contacts"]
        except Exception as e:
            self.LogInfo("Eleven finns inte i Edlevo/Procapita: " + str(e))
            return None

    def BuildContactUpdate(self, pnr, emailHome, telVoice, telMobile, updateVoice="Y"):
        return dict(
            personalIdentityNumber=(pnr or "").replace("-", ""),
            emailHome=dict(value=emailHome or "", update="Y"),
            emailWorkSchool=dict(value="", update="N"),
            telVoice=dict(value=telVoice or "", update=updateVoice),
            telMobile=dict(value=telMobile or "", update="Y"),
        )

    def SkickaKontaktTillEdlevo(self, elevPnr, skoltyp, contactDict):
        if not contactDict.get("personalIdentityNumber"):
            return None
        request = RestWrapperService.HttpRequest()
        request.Data = JavaScriptSerializer().Serialize(contactDict)
        request.Uri = self.GetProcapitaUri(elevPnr, skoltyp)
        return self.GetProcapitaWrapper().Post(request)

    def SendUpdatedContactsToProcapita(self):
        roll = self.GetAnswer(self.rollFieldId) or ""
        skoltyp = self.GetAnswer(self.skoltypFieldId)
        if roll.Contains("Myndig elev"):
            elevPnr = self.GetAnswer("x.157")
            self.SkickaKontaktTillEdlevo(
                elevPnr,
                skoltyp,
                self.BuildContactUpdate(elevPnr, self.GetAnswer("x.194"), "", self.GetAnswer("x.196")),
            )
            self.SkickaKontaktTillEdlevo(
                elevPnr,
                skoltyp,
                self.BuildContactUpdate(self.GetAnswer("x.243"), self.GetAnswer("x.200"), self.GetAnswer("x.201"), self.GetAnswer("x.202")),
            )
            self.SkickaKontaktTillEdlevo(
                elevPnr,
                skoltyp,
                self.BuildContactUpdate(self.GetAnswer("x.244"), self.GetAnswer("x.207"), self.GetAnswer("x.208"), self.GetAnswer("x.209")),
            )
        if roll.Contains("Vårdnadshavare"):
            elevPnr = self.GetAnswer("x.13")
            student = self.BuildContactUpdate(elevPnr, "", "", self.GetAnswer("x.222"), updateVoice="N")
            student["emailHome"] = dict(value="", update="Y")
            self.SkickaKontaktTillEdlevo(elevPnr, skoltyp, student)
            self.SkickaKontaktTillEdlevo(
                elevPnr,
                skoltyp,
                self.BuildContactUpdate(self.GetAnswer("x.3"), self.GetAnswer("x.56"), self.GetAnswer("x.58"), self.GetAnswer("x.59")),
            )
            self.SkickaKontaktTillEdlevo(
                elevPnr,
                skoltyp,
                self.BuildContactUpdate(self.GetAnswer("x.245"), self.GetAnswer("x.67"), self.GetAnswer("x.68"), self.GetAnswer("x.69")),
            )
```
