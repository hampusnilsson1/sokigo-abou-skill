# CitizenInfo and Citizen

Source: *CitizenInfo*. Read 2026-08-25.

Person data always comes from an **external plugin** (Navet, KIR, PulsenId, TEIS, …). Builder Python: also [navet.md](../../../build-abou-etjanst-web/references/integrations/navet.md) and mallar.

## CitizenInfo (stored)

On login, Abou looks up the configured service:

1. If a person is found, these are stored: FirstName, LastName, Email, CompanyPhone, HomePhone, MobilePhone, CompanyName, City, AllAddress, MunicipalityKey, ProtectedIdentity.
2. Else only values from the **login** IdP are mapped (name, email, phones, company).
3. A row is inserted/updated in table **CitizenInfo**.

That row is what ties the user to e-tjänster and UI preferences. In page logic it is **`self.Citizen`** (GDPR-stripped — civilstånd, födelse, raw CitizenData often empty). Keep the class small; some fields are no longer maintained unless a setting is on.

Direct lookup **without** saving and **without** GDPR stripping:

```
self.GetCitizenInfoLookup(socialSecurityNumber)
```

(Docs also spell `GetCitizenInfoLookUp`.) Session only.

## Citizen (not stored)

`DefaultCitizenService.GetCitizen(personnummer)` hits the configured person service and maps to **Citizen**. Not written to DB. Unified interface so plugins can change without rewriting mallar. Relatives and civilstånd are examples — **not every plugin has every field**.

`GetCitizenAsJson(personnummer)` returns the source JSON string. **Sekretess / skyddad identitet sits above the PersonPost** and is **not** visible via this method. Same payload may appear as `CitizenData` for Navet and TEIS.

## Field mapping (Kir / Navet / PulsenId / Teis)

| Field | Kir | Navet | PulsenId | Teis |
| --- | --- | --- | --- | --- |
| CitizenData | no | yes | no | yes |
| SocialSecurityNumber, FirstName, LastName | yes | yes | yes | yes |
| MunicipalityKey | yes | yes | yes | no |
| MaritalStatusCode | no | yes | no | yes |
| ProtectedIdentity | yes | yes | no | no |
| ProtectedIdentityCivilRegister | no | yes | no | no |
| Address.PostalAddress / PostalCode | yes | yes | yes | yes |
| Address.CareOf | yes | yes | yes | no |
| BirthPlace (+ CountyCode, Community, OverSea*) | no | yes | no | Teis: BirthPlace yes, subfields empty |
| Relatives | no | yes | yes | yes |
| Relative SSN, TypeOfRelation | no | yes | yes | yes |
| Relative Deregistrated | no | yes | no | no |
| Relative FirstName, LastName | no | no | yes | yes |

Do not log real personnummer.
