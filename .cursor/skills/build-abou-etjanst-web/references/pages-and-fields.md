# Pages and fields in the builder

Source: Sokigo Abou docs (read 2026-08-21).

## Add a page

1. **Ny sida** — settings open automatically
2. Fill **Egenskaper**
3. Drag the page to the right place

### Page properties

**Systemnamn** — for the system and for Python. Same character rules as service systemnamn. Tip: `HarSkriverJagEttSidnamn`. Citizens do not see it.

**Sidnamn** — heading in the service, admin, and PDF.

**Sidtyp** — default **Layoutsida**. See below.

**Visa på sammanfattningssidan** — uncheck so the page is omitted from summary (typical for info-only pages). User then cannot go back and change that page from summary.

**Förhandsgranska ärendesammanfattning** — on the summary page: draft PDF marked “Utkast”.

**Dölj navigeringsknappar** — hides next/back, step counter, save, cancel.

**Dölj inte tillbaka-knappen** — hide other nav but keep back.

**Sidbryt** — blankettgenerator / PDF page break after last field.

Delete page: red cross.

## Sidtyper

New pages default to **Layoutsida**. Change under the page’s **Inställningar**.

| Sidtyp | Use |
| --- | --- |
| Layoutsida | Normal pages: blocks and fields. Not summary, sign, thank-you. |
| Sammanfattningssida | Created automatically. No extra fields. Every new page is shown here unless you uncheck **Visa på sammanfattningssidan**. |
| Signeringssida | Created if the service requires e-legitimation. Add manually if that was not ticked at create. No extra fields. |
| Betalningssida | Payment; needs no fields. |
| Tacksida: ThankYou | Default thank-you. Hardcoded case number. **Huvudinnehåll** after the case number; may replace the municipality “signatur”. No extra fields. |
| Tacksida: ThankYouSimple | Empty; no hardcoded text (e.g. hide case number). |
| Tacksida: PdfLinkThankYou | Link to case summary (from 2023.11 HTML summary + PDF link). **Huvudinnehåll** at top, replaces part of “Tack för din ansökan/anmälan”. |
| Tacksida: PaymentThankYou | Payment info (from 3.48). |
| Tacksida: ThankYouAdvanced | Razor in **Huvudinnehåll** for dynamic text (case number etc.). Test thoroughly. |
| NoNavigationFieldPage.aspx | Removed in 2020.5 |
| Fältsida | Removed in 2020.5. Convert via Inställningar → Sidtyper. **Re-set validators** after convert. |

## Add a field (classic field tab)

1. Select the page
2. Tab **Fält**
3. **Nytt fält**
4. Fill properties, **Spara**

Prefer layout builder blocks when working on a Layoutsida (see builder-ui.md).

### Field properties

- **Rubrik** — citizen label. Bold via `<br/><strong>Övrigt</strong>`
- **Fälttyp** — dropdown of types (see field-types.md)
- **Svarsalternativ** — where the type needs them
- **Obligatoriskt**
- **Anpassade valideringstexter** — only when format is wrong, not when empty (system texts then). Not for köfält.
- Show answer in admin case list (per version; only new cases). **Redigera** reorders those columns.
- **Viktigt** — highlight for caseworkers
- **Antal rader** — textarea height; for radio/checkbox = number of **columns**
- **Validering** + **Validatorargument**
- **Minsta längd** / **Maxlängd**

### Field texts tab

- **Hjälptext** — i-icon
- **Text ovanför fält** — not for spacing; use **LabelField**
- **Text under fält**
- **Svarsalternativ hjälptexter** — after a choice is selected
- **Muspekartext** — keep short
