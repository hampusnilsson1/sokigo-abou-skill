# E-förslag

Module. Sokigo flags the submit e-tjänst in sysadmin so submit **creates a proposal linked to the case**. Right **Handlägga förslag**. Citizen list: `/Citizen/Proposal`. Filter via `?status=Godkänt&status=Avslaget` (space as `%20`).

## Map fields (integrationsargument `proposal`)

| Argument value | Meaning | Required |
| --- | --- | --- |
| Title | Rubrik | yes |
| Text | Brödtext | yes |
| File | Filuppladdning | no |
| SentBy | Inskickad av | no |
| Email | E-post | no |

Builder: field → **Integration → Nytt integrationsargument** → `proposal` / value. Extra fields stay on the **case** only. Prefer image-only uploads (files are public). Optional login + **kommunintillhörighet** (Navet) so only residents submit.

## Inställningar (Admin → E-förslag → Inställningar)

1. Cookie-only voting (IP stored; same browser cannot vote twice) **or** require personuppgifter (still cookies)
2. **Kräv inloggning för röstning** + **Kräv kommunintillhörighet** (needs Navet)
3. ReCaptcha keys (Sokigo per site) — graphic captcha is **not** recommended for a11y
4. **Tillåt kommentarer** / **Publicera kommentarer automatiskt**
5. Facebook share + delningsbeskrivning
6. **Livslängd (dagar)** — first vote day = publish day; last = publish + N − 1. Existing proposals unchanged if you edit the default
7. **Minst antal röster för beslut** → status **Inväntar ställningstagande** else **Avslutad**. Per-proposal override possible

## Handläggning statuses

**Inväntar publicering** (hidden) → edit title/text (logged in case history), optional public comment, tick **Publicerad** (shows period), or delete from e-förslag view (case remains). Link to case. Override vote threshold.

**Röstning pågår** — optional message **När antal röster uppnåtts**.

**Inväntar ställningstagande** — **Skapa beslutsunderlag** regenerates case PDF (tokens for vote count). Then Godkänt / Avslaget / Besvarat + motivering + optional file (replaceable later).

Comments: blue bubble = new; publish / publicera ej; can reverse.

**Rösta som ombud:** on the proposal; if login-voting, personnummer + name + legitimering; no duplicate SSN; kommun check if configured.

## Messages (e-tjänst → E-förslagsmeddelanden)

When: **Vid publicering**; **Vid förberedande för ställningstagande** (beslutsunderlag — typical funktionsbrevlåda + PDF); **Vid ställningstagande**; **Vid röstningsperiodens slut** (must combine with scheduled job **Skicka notifiering vid röstningsperiodens slut**); **När minst antal röster har uppnåtts**.

Citizen texts: resource strings on list + proposal page (button, empty list, vote/comment help).
