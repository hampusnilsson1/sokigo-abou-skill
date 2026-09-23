# Edlevo / Procapita (school system)

Edlevo **is** Procapita. Same product, new name when the vendor shipped a new UI. Working Abou services still resolve the named RestWrapper **`procapita1_1`**. Treat `Edlevo`, `Procapita` and `procapita1_1` as one integration.

There is **no** Sokigo Confluence method list for this API. The contract below is from production Skolstart (barnsida + tacksida). Adapter REST mentions Ängelholm → Procapita Education via Mule — same idea, URL lives in sysadmin.

Koddocs (copy-paste PageNode, Skolstart field map): `/integrationer/edlevo`.

## When to use it

| Need | Source |
| --- | --- |
| Legal guardian (`VF`), protected identity, tilltalsnamn, child list | [navet.md](navet.md) — **not** Edlevo |
| School-registered contacts, email/phone already in the school system | GET `contacts` |
| Write updated email/phone back after submit | POST one person at a time |
| Confirm the child exists as a pupil | GET; empty/error = not in Edlevo |

Do **not** overwrite Navet field `x.20` (other legal guardian JSON) with Edlevo contacts. Extra school contacts go in their own field.

## How it is called

Named RestWrapper, **Get/Post on the service** (not factory + `Send`):

```python
from Abou.Calamare.Framework.Integration.RestWrapper import *

wrapper = self.Resolve[IRestWrapperService]("procapita1_1")
url = wrapper.Configuration.Url          # template with {0}=elev-pnr, {1}=skoltyp
request = RestWrapperService.HttpRequest()
request.Uri = url.format(elevPnr.replace("-", ""), skoltyp)  # e.g. GY
response = wrapper.Get(request)          # read
# request.Data = JavaScriptSerializer().Serialize(payload)
# response = wrapper.Post(request)       # write
```

- Wrapper name can differ per kund; clone a working service on the site.
- `skoltyp` is a field in Skolstart (`x.262`), not hardcoded `"GY"`.
- 12-digit personnummer, no hyphen, in both the URL and `personalIdentityNumber`.
- Some sites instead keep a JSON config `EDLEVO` and build the URI themselves. Prefer the named wrapper if `procapita1_1` is already on the site.

Factory + `RestRequest` + `Send` is the **other** RestWrapper style ([adapter-rest.md](adapter-rest.md)). Do not mix request types.

## GET — contacts for a pupil

`GET` against the formatted URL. Body is JSON with `contacts[]`.

| Field | Meaning |
| --- | --- |
| `relation` | `"Guardian"` = vårdnadshavare in the school system. Other values = extra contacts |
| `personalIdentityNumber` | 12 digits |
| `emailHome` | Home email |
| `telVoice` | Landline |
| `telMobile` | Mobile |

Empty contacts or deserialize failure: pupil missing in Edlevo. Log without full personnummer. Do not stop the e-tjänst if Navet VF is enough.

Filter `relation == "Guardian"` when you only want school-registered guardians. Skolstart still had a commented `hamtaGurdianfronEdlevo` (typo in the name) on the child page — implement it as this GET, after Navet.

## POST — update one person

One POST per person (elev, VH1, VH2). URL is always the **pupil** + `skoltyp`. The body says *which* person to update:

```python
{
  "personalIdentityNumber": "12digits",
  "emailHome":       { "value": "...", "update": "Y" },
  "emailWorkSchool": { "value": "",    "update": "N" },
  "telVoice":        { "value": "...", "update": "Y" },
  "telMobile":       { "value": "...", "update": "Y" }
}
```

`update` is `"Y"` or `"N"`. `"N"` leaves that slot untouched. Skolstart sends the pupil first, then VH1, then VH2, usually from **ThankYou.Initialize** after submit.

### Skolstart field map (change ids per service)

Role field `x.166` contains `Myndig elev` or `Vårdnadshavare`. Pupil in the URL: `x.157` (adult) or `x.13` (child).

| Person | Adult-pupil fields | Guardian-flow fields |
| --- | --- | --- |
| Elev pnr | `x.157` | `x.13` |
| Elev email / tel / mobile | `x.194` / `x.195` / `x.196` | mobile only `x.222` (email+voice often empty/`N`) |
| VH1 pnr / email / tel / mobile | `x.243` / `x.200` / `x.201` / `x.202` | `x.3` / `x.56` / `x.58` / `x.59` |
| VH2 pnr / email / tel / mobile | `x.244` / `x.207` / `x.208` / `x.209` | `x.245` / `x.67` / `x.68` / `x.69` |

Skip a guardian POST when that personnummer is missing.

## Combine with Navet

1. Child list, VF, skyddad identitet, tilltalsnamn → Navet ([navet-dropdown.md](../logic-templates/navet-dropdown.md)).
2. Optional GET Edlevo for school contacts / “is this child a pupil?”.
3. After submit, POST contact updates from ThankYou.

Worked helpers: [edlevo-contacts.md](../logic-templates/edlevo-contacts.md).

## Pitfalls

- Named wrapper uses `RestWrapperService.HttpRequest` + `Get`/`Post`, not `RestRequest` + `Send`.
- URL is a **format string**. Wrong `skoltyp` → 404 even if the pnr is correct.
- POST with empty `personalIdentityNumber` still hits the API — guard before send.
- Test vs prod URL is in the wrapper config. Do not also branch on `HostName.Contains("test")`.
- Do not log full personnummer. Mask or omit.
- Names in Edlevo and Navet do not always match. Show Navet names on the blankett.
