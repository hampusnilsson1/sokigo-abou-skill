# Adapter REST

Docs: [Adapter Rest](https://dok.sokigo.com/display/ABOU/Adapter+Rest). Read 2026-08-21.

Generic adapter toward **one or more REST APIs**.

- **Python in the e-tjänst** names the methods and the request/response JSON.
- The adapter handles **security** and **which endpoints** to call (sysadmin).
- You must know the target API. Examples in docs: Ängelholm → Procapita Education via Mule; Täby → BookIT.

There is **no method list** on this Confluence page. The library in Python is `IRestWrapperServiceFactory` + a **named** sysadmin config (URL, auth, `ExtendedConfigurationData`). Example of how to call it: [ad-lookup.md](../logic-templates/ad-lookup.md) (`InternalWebSearch`). How it fits: [libraries.md](../logic-templates/libraries.md).

Clone a working service on the same site, or get the API contract from the municipality. Do not put API keys in field help text or git.
