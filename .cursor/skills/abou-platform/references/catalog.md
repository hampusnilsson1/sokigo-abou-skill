# Abou space catalog (outside builder + integrations)

Space: [Abou](https://dok.sokigo.com/display/ABOU). Read 2026-08-25.

**Already in `build-abou-etjanst-web`:** *Att bygga e-tjänster* (pageId 56918159) and *Integrationer*. Do not duplicate those here.

**Not ingested as notes (titles only):** Release notes bodies, Community presentations, Webinar videos, Minut Bygg, Minut Miljö (other products), remaining FAQ article bodies, a few Funktionalitet pages still thin (see [functionality.md](functionality.md)).

## Abou (main hub)

### Administrationsidorna
Administrera Organisationer; Administrera Text Och Bild I Abou; Aktivera/Inaktivera E-Tjänst; Ange Öppettider För En E-Tjänst; Forcera Ärenden (Signera Som Ombud); Frågor Och Svar; Hantera Behörigheter; Hantera Dokument; Importera Och Exportera E-Tjänster; Integrationslogg; Menygrupper; Permanent Borttagning Av Ärenden; Publicera E-Tjänst Och/Eller Blankett; Skicka In Ärende Som Ombud; Statistik Och Rapporter; Systemhändelser; Sök Och Ta Bort Invånare (Personpost); Ta Bort E-Tjänst I Admin; Ändra Organisation För En E-Tjänst; Ändra Texter I E-Tjänster.

Notes: [admin.md](admin.md). PDF/dokumentmallar: [document-templates.md](document-templates.md).

### Ärendehantering
Ärendelistan Och Ärendedetaljvy; Ärendets Diarienummer; Handlägga Ärenden; Loggboken.

Notes: [cases.md](cases.md).

### Behörighetsnivåer
Introduktion Behörigheter; Systembehörigheter; Systemadministrator; E-Tjänstebehörighet: Verksamhetsadministrator; Beslutsfattare; Statusuppdaterare; Läsbehörighet; Skicka In Ärende; Redaktör; Behörighet På Individ-Eller Gruppnivå.

Notes: [permissions.md](permissions.md).

### Bokningsmodulen
Beskrivning; Handläggning Av Bokningar; Skapa Nytt Bokningstillfälle; Återkommande Bokningstillfällen; Boka Om Och Avboka; Konfigurera Bokningar; Bokningsmeddelanden.

Notes: [booking.md](booking.md).

### Dela e-tjänster med andra
Share catalog / other municipalities. Titles only here.

### E-Förslag
Beskrivning; Skapa E-Tjänst För Att Lämna Förslag; Inställningar; Handlägga Förslag; Handlägga Kommentarer; Rösta Som Ombud; Läsa, Rösta, Dela Och Kommentera; Texter I Invånarvy; E-Förslagsmeddelanden.

Notes: [e-forslag.md](e-forslag.md).

### FAQ
~30 Q&A pages (AD, fält visa/dölja, hjälptexter, blankettgenerator, roller, en/två vårdnadshavare, ärende-PDF i mail, handläggarnotifiering, ärendenummerformat, dela e-tjänster, taggar, Oracle vs SQL, förhindra inklistring e-post, funktionsbrevlåda per val, följa process, SMS, utskrift, editera sidor, när AD-uppslag, personuppgifter sparas, grafisk anpassning, ärendelista filter, Navet-kostnad, redaktör vid import, inga mail i test, Navet-data, e-leg leverantörer, SQL-databaser, första-inloggning lösenord).

Use the matching topic file; do not invent answers.

### Funktionalitet
~40 feature pages. Index: [functionality.md](functionality.md).

### Kömodulen
Beskrivning; Komma Igång; Skapa Ny Kö; Konfigurera En Kö; Handlägga Köer (+ byt köplats, digital betalning, lägg till manuellt, ta bort, uppdatera kontakt, uppdatera registreringsdatum, uppdatera status); Köbetalning; Köer: Hur Gör Invånaren; Köfilter; Kömeddelanden.

Notes: [queues.md](queues.md).

### Meddelandemallar
Exempel; Exempel (multipelsignering); Koppla Meddelandemall Till E-Tjänst; Skapa/Redigera/Ta Bort; Statusnotifieringar; Värden I Meddelandemallar.

Builder-adjacent: `build-abou-etjanst-web/references/messages.md`. Tokens: [message-tokens.md](message-tokens.md). Razor model: [technical/htmlcasemodel.md](technical/htmlcasemodel.md).

### Min sida
Att Göra; Beskrivning (2020.11 och tidigare); Direktmeddelanden; Händelser; Köplatser Och Bokningar; Publicering Och Villkorsstyrning; Tjänster.

### Min sida 2021.2 och 2024.2
Funktioner Som Stöds; Övergripande Beskrivning Min Sida Och Min Sida Plus; Video; Min sida efter 2024.2, med sidor som översta nivå.

Notes: [min-sida.md](min-sida.md).

### Moduler
Schemaläggningsmodul; E-Förslagsmodulen; Betalningsfunktion; Min Sida; Användningsmodulen; Kömodulen; Bokningsmodulen; Register.

Notes: [modules.md](modules.md).

### Projektdokument, Checklistor Och Processer
Kundservice/Support; Deployprocess; Checklista: Driftsättning Av E-Tjänst. Titles only.

### Registermodulen
Fokuswebinar; Beskrivning; Import Och Export; Redigera Register; Koppla Register Och E-Tjänst; Behörigheter För Register; Text/Värdeseparering.

Notes: [registers.md](registers.md).

### Release notes
V26; 2025.11 … back through 2021 and earlier. **Catalog only** — read Confluence for a specific version, do not dump changelogs into the skill.

### Schemaläggning
Beskrivning; Ärendepåminnelser; Bokningspåminnelser; Köplatspåminnelser; Notifiering Vid Röstningsperiodens Slut; Signeringspåminnelse; Skapa Fil; Synkronisera Personuppgifter; Ta Bort Ärenden Mjukt; Ta Bort Ärenden Permanent; Uppdatera Status På Ärende.

Notes: [scheduling.md](scheduling.md). From version **2018.2**.

### Teknisk Information & Dokumentation
Abou REST API; Ansvarsfördelning vid drift On Prem; CitizenInfo; HtmlCaseModel; Information Om GDPR; Penetrationstester Av Abou; Teknisk Kravspecifikation - Abou Intern Hosting; Testpersoner I Abou; Tillgänglighetsredogörelse; Vad Är EIDAS; Vilka Protokoll Stödjer Abou; Vilka Webbläsare Stödjer Abou.

Notes: [technical/INDEX.md](technical/INDEX.md).

## Other top-level in the space

- **Community** — användarträffar, webinars (titles only).
- **Minut Bygg / Minut Miljö** — other Sokigo products; do not open.
