# Ärendehantering

Confluence children (open those pages for screenshots): Ärendelistan och ärendedetaljvy; Ärendets diarienummer; Handlägga ärenden; Loggboken.

Known from permissions + scheduling (do not invent extra UI):

- Case list + detail + case PDF: needs an e-tjänst right that can **see cases**.
- **Diarienummer** can be set in UI or REST `UpdateDiaryNumber`. Message when **När diarienummer sätts** exists in the builder skill.
- **Tilldela handläggare**: only users with **Statusuppdaterare** on that service are selectable.
- **Beslut** (Godkänn/Avslå + beslutsdokument): **Beslutsfattare** and service setting Beslut.
- **Loggboken**: read vs write/headings depend on role ([permissions.md](permissions.md)).
- **Skicka meddelande**: from 2023.2 email or SMS; mallar marked manuellt — see builder `messages.md`.
- Köärenden also appear here; deleting a köplats does not replace updating case status.

REST counterparts: [technical/rest-api.md](technical/rest-api.md).
