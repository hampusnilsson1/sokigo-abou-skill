# E-legitimation (authentication and signing)

Docs: [E-legitimation, flera leverantörer](https://dok.sokigo.com/pages/viewpage.action?pageId=58524202). Read 2026-08-21.

Abou supports login and signing via (docs list): CGI (Logica), Visma Sirius, Svensk e-identitet (Medborgarkonto and E-leg), Mobilt BankID.

Mobile BankID signing (as of that page): Visma Sirius, CGI, Svensk e-identitet.

Sammanställning also names federation/IdP options: CGI, Sirius, Portwise, McAfee, Svensk E-identitet, Microsoft AD, KnowIT (Cybercom/SignPort), SwedenConnect.

**Builder:** tick **Kräva inloggning** / **signering** on the service. Sokigo wires the IdP. You do not pick CGI vs Sirius in the layout builder.

See `../create-and-settings.md` for service checkboxes.
