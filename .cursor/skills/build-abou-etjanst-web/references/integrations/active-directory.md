# Microsoft AD (internal login)

Docs: [AD för inloggning](https://dok.sokigo.com/pages/viewpage.action?pageId=58524264). Read 2026-08-21.

LDAP or IdP. Can cover external admin, internal admin, and **internal citizen node** (internal e-tjänster + Min sida).

- **Abou LDAP:** users sign with AD; signing in the internal citizen view is possible. Rights in Abou users **or** AD groups synced into Abou groups (same names). Highest of user+group wins. **Behörigheter → Grupper → Synkronisera användare** copies name/email into Abou for those group members (creates missing users; does **not** delete leavers). Synced users cannot be edited or given individual rights in Abou.
- **IdP:** IdP owns login (can combine SMS 2FA). **No signing** in the citizen view. Cannot drive Abou rights from AD groups.

Builder mall: [ad-lookup.md](../logic-templates/ad-lookup.md) — `IRestWrapperServiceFactory` + sysadmin key **InternalWebSearch**. How RestWrapper is used: [adapter-rest.md](adapter-rest.md), [libraries.md](../logic-templates/libraries.md). Attestlista med sök is the internal multi-approve field (`../field-types.md`).
