# Emails, booking, queue, FAQ

Clone these from a real export when the user needs them. The JSON packager emits empty `<ServiceEmails />` / `<EmailMessages />` unless you extend the definition. After import, many teams configure mail in the Abou UI instead.

## ServiceEmail

Lives under `Service/ServiceEmails` and is mirrored in `Content/ServiceEmails` (Content also inlines `ServiceEmailMessage`).

| Element | Example | Role |
| --- | --- | --- |
| `EmailFromAdress` | `noreply@kommun.se` | From address (site mailbox, not a secret) |
| `EmailFromName` | organisation display name | From display name |
| `EmailToCitizenEmail` | true | Send to the signed-in citizen |
| `EmailToAdmin` | false | Notify handläggare |
| `EmailToAdress` | optional fixed to-address | |
| `EmailToAdressFromField` | optional friendly field id | |
| `WhenToSendEmail` | `Standard` or `StateUpdated` | Trigger |
| `MessageCategory` | `Standard` or `Reservation` | |
| `IncludeAttachments` | true/false | |
| `EmailMessageID` | id of `EmailMessage` | |
| `MessageEvent` | JSON | Filters when it fires |

`StateUpdated`: notify on case statuses including `Inkommet`, `Registrerat`, `Under handläggning`, `Avslutat`, plus extra statuses the site uses.

Reservation: `MessageCategory` = `Reservation`, `ReservationEvent` in `MessageEvent` JSON, optional `ServiceNotification` with `NotificationType` = `Sms`.

## EmailMessage

Templates under `Service/EmailMessages`:

- `Name`, `MessageSubject`, `MessageBody` (HTML)
- `ShortMessage` (plain/SMS-sized)
- Placeholders seen in booking mail: `$ReservationDate$`, `@this.Model.Administrator.DisplayName`
- `AttachPDF` / `AttachXML` / Mina meddelanden variants
- `IsForServiceUsage` / `IsForManualUsage`

Do not invent Abou placeholder syntax. Copy from an export that already works in the same site.

## Booking and queue

Service-level `SlotSettings` JSON:

```json
{
  "Filter": null,
  "ShowAdminUser": true,
  "DefaultSpanMinutes": 33,
  "ReservationTimeoutMinutes": 20,
  "NotifyAdministratorEmailMessageId": 0,
  "IncludeICalendar": true,
  "CancelHourLimit": 0
}
```

Field `ReservationField2` arguments:

| Name | Example |
| --- | --- |
| `ShowEndTime` | `True` |
| `MultipleSelect` | `True` |
| `ShowAdminUser` | `True` |
| `MaxNumberOfReservations` | `2` |
| `MultipleReservations` | `True` |

`QueueField` has no extra arguments in exports seen so far. Runtime queues/slots are configured in Abou, not as secrets in the zip.

JSON authoring (packager already accepts `type` + `arguments`):

```json
{
  "id": 1,
  "type": "ReservationField2",
  "question": "Boka tid",
  "arguments": [
    { "name": "ShowEndTime", "value": "True" },
    { "name": "MultipleSelect", "value": "True" },
    { "name": "ShowAdminUser", "value": "True" },
    { "name": "MaxNumberOfReservations", "value": "2" },
    { "name": "MultipleReservations", "value": "True" }
  ]
}
```

## FAQ

`Content` may contain `FaqEntries`, `FaqEntryToServices`, `FaqEntryToPages`. Safe to omit for new services. Do not copy placeholder FAQ text.
