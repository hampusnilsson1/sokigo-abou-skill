# Tokens in meddelandemallar

Source: *Värden i meddelandemallar* (pageId `60096729`) plus builder messages notes. Read 2026-08-25.

Always `$name$` (case-sensitive). Field answers: Razor `@this.Model["AVB.2"]` (FriendlyFieldId). Razor **does not** work in **scheduled reminder** mallar or in SMS.

If you write a field id with a raw `@` in the answer and skip `@Model[]`, PDF generation can fail.

Builder coupling (when/to/attachments): `build-abou-etjanst-web/references/messages.md`. Object model: [technical/htmlcasemodel.md](technical/htmlcasemodel.md).

## General

| Token | Meaning |
| --- | --- |
| `$uniqueID$` | Ärendenummer |
| `$registrationNumber$` | Diarienummer |
| `$serviceName$` | E-tjänstens namn |
| `$administrator$` | Assigned caseworker username |
| `$administratorName$` | Assigned caseworker full name |
| `$caseID$` | Internal case id |
| `$customerName$` | Municipality / node name |
| `$customerUrl$` | Abou base URL |
| `$dateSubmitted$` | Submit date |
| `$dateSubmitted6$` | Submit timestamp |

Min sida case URL pattern (builder docs): `…/Citizen/MyPage2#/cases/$uniqueID$`.

## Citizen (needs login or integrated personnummer)

`$citizenName$`, `$citizenFirstName$`, `$citizenLastName$`, `$citizenMobileNumber$`, `$citizenHomePhoneNumber$`.

## Kö status notices

`$Comment$` (manual status comment), `$QueuePosition$`, `$QueueName$`.

## Bookings

`$ReservationDate$` (single booking only), `$ReservationSpots$`, `$ReservationUTCStart$`, `$ReservationUTCEnd$` (e.g. `2022-12-14T09:00:00`). All occasions: `@this.Model["fältId"]`.

## Payments (Razor)

`@Model.ApplicantPayment.Amount`, `.TransactionId`, `.PayedBy`.
