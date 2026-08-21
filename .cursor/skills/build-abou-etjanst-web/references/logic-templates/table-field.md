# Tabellfältet

Tab: **Logik**. Serialize a dict with Widths (sum ≤ 12), Headers, Rows. Extra columns without headers stay hidden; `AnswerIndex` reads them. `SummaryType`: `SelectedRows`, `Table`, or empty = selected answers only. Preview does **not** support this field.

```python
from Abou.Calamare.Web import PageNode
from System.Web.Script.Serialization import JavaScriptSerializer

class InfoPage(PageNode):

    def Initialize(self):        
        #ange fältid för din tabell
        tableFieldId = 'ANGEFÄLTID'
        
        #definera raderna i tabellen
        rowList =   [
                        ['ABC123','Nybyggnad','2015-01-01','0'],
                        ['ABC234','Rivning','2012-05-20','1'],
                        ['ABD567','Utbyggnad','2013-03-10','2'],
                    ]
        
        #observera att kolumner som inte har motsvarande rubriker, kommer bli gömda i tabellen, men kan
        #användas för att få ut värden genom att sätta fältargumentet AnswerIndex till kolumnen.

        #definera tabellen här, med kolumnbredder och kolumnrubriker och rader.
        #summan av bredderna bör inte överskrida 12.
        table = dict(Widths=[4,5,3],Headers=['Diarienummer','Ärendemening','Inkommet'],Rows=rowList)
        
        #här är ett exempel på en tabell med styling
        #table = dict(Widths=[4,5,2,1],Headers=['Diarienummer','Ärendemening','Inkommet','id'],Rows=rowList,
        #HeaderStyle="background-color:#ffffff !important;border:1px solid #000000;color:#000000 !important",
        #RowStyle="background-color:#bbbbbb;border:1px solid #000000;",
        #TableStyle="font-family: 'Times New Roman', Georgia, Serif;font-size:18px;",
        #SummaryType="SelectedRows"
        #)
        #SummaryType styr hur tabellfältet presenteras i ärendepdf, sammanfattningssida och ärendeyv för handläggare
        #SummaryType = "SelectedRows" används för att visa valda rader
        #SummaryType = "Table" används för att visa hela tabellen
        #Lämna SummaryType tom för att endast visa valda svar

        #serialisera tabellen
        serializedTable = JavaScriptSerializer().Serialize(table)
        
        #skriv in den serialiserade tabellen till fältet
        self.SetAnswerIfEmpty(tableFieldId,serializedTable)

    def GetNextPage(self):
        #tableFieldId 'x.1'
        self.LogDebugObject(self.GetAnswers('x.1'))
        
        return PageNode.GetNextPage(self)
```
