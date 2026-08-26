# Ärendehantering

Menu **Ärenden**. Rights: [permissions.md](permissions.md).

## Ärendelistan

Filters: statuses (all on by default), **Dina ärenden**, **Dölja avslutade**. Search: submit date, ärendetyp (only services you may see), status, diarienummer, ärendenummer, handläggare username or full name. Optional extra columns = chosen fältsvar. Click headers to sort.

## Detalj — actions

Default statuses (change under service **Inställningar**): Inkommet, Registrerat, Under handläggning, Avslutad.

| Action | Notes |
| --- | --- |
| Uppdatera status | Status list from the service |
| Ange diarienummer | Free text (letters/digits/symbols). Shown on Min sida and tacksida **instead of** ärendenummer unless hidden in service settings. List sort is **string** order (`1,10,11,2…`) |
| Begära komplettering | **From 2021.2: files only** (which files, explanation, optional instruction file, types, multiple). Notify with standard message when status **Väntar på komplettering**. Older: pick fields **Komplettera fält** then begär. **Ångra komplettering** exists. After supplement, multi-sign cases return to **Väntar på medsökandes signatur** |
| Tilldela handläggare | Selectable users = **Statusuppdaterare**. Optional personal text + attachments if tilldelning-mail is coupled |
| Ladda upp bilaga | Citizen sees on Min sida if linked. Optional **läskvitto**. Same allowed types/signature check as filuppladdning. Cannot delete ärende-PDF or beslut; other files are permanent delete |
| Godkänn / Avslå | Service setting **Beslut** + **Beslutsfattare** + person link. Comment and/or file; system builds beslut-PDF; download = läskvitto. Statusnotifiering Godkänd/Avslagen |
| Forcera / ombud sign | [admin.md](admin.md) |
| Skicka meddelande | Needs login, integrated personnummer, or configured email field — builder `messages.md` |
| Ta bort | Soft delete |
| Loggbok | Headings defined **on the e-tjänst**. Same headings for all cases of that service. Cannot delete a heading that has entries; can close a heading for new entries. Deleted entries are struck through (who/when) and omitted from Excel. Read: Läs+; write: Statusuppdaterare+ |

**Läsbehörighet:** view + open attachments only.

## Diarienummer vs REST

UI or API `UpdateDiaryNumber`. Message when **När diarienummer sätts**.
