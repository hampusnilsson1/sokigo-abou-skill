# Payment

Read 2026-08-21. Builder: `../create-and-settings.md` (Betalningssida). How the **library** on Payment.aspx is used (`HasPaymentInfo`, `GetPaymentOrderText`, `CalculatePaymentAmount`, `GetAnswerFromFieldId`): [payment mall](../logic-templates/payment.md), [libraries.md](../logic-templates/libraries.md).

| Provider | Status in docs |
| --- | --- |
| **Swedbank Pay** | Current. V1 (Swish/card) until 2023.11; **V3.1 from Abou 2024.1** (invoice, Apple/Google Pay, wallets). V1 being shut down. Extra Swedbank Pay avtal for new methods. Sokigo config change (no extra Abou license). |
| **Paynova P3** | Being phased out; no new customers |
| **Dibs** | Being phased out; no new customers (in Abou from 3.48) |

All need provider avtal + Sokigo config. Do not add a payment page unless that stack is live.
