# DIGG Mina meddelanden

Encrypted digital mailbox (Kivra, Min myndighetspost, Bring Digimail) via FAR + sealing. Sokigo installs the plugin. Do not store cert passwords in the skill or git.

## Prerequisites

- Abou **3.21+**
- **Separate** Steria server cert (not the Navet cert)
- DIGG anslutningsavtal; org.nr, support text/email/URL/phone/logo to Sokigo
- Configured in **produktion**
- Citizen has joined Mina meddelanden **and** chosen this kommun
- Message malls coupled to the e-tjänst
- Service has **inloggning or integrerat personnummerfält** (the integration looks up personnummer)
- Works for privatpersoner and företag

## What it does

If the citizen opted in, **all** Abou message sends to them go to their chosen secure mailbox operator.

- Different body for e-post vs Mina meddelanden: unique MM text if present, else the e-post body. Same fallback for företag → invånare body.
- The only attachment you can treat differently vs ordinary e-post is the **ärende-PDF**.
- Other case-file attachments follow the notifiering tick and then go to **both** e-post and MM.
- On **beslut**, case files **including the decision file** always go with the MM send.
- Does **not** replace SMS (own kortmeddelande mall).

Builder: mall editor has a Mina meddelanden body (or falls back). Coupling: `../messages.md`.
