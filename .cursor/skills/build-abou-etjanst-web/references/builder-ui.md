# Layout builder UI

Source: Sokigo Abou docs, *Layoutbyggaren* (from Abou 2018.11). Read 2026-08-21.

## Blocks and fields on a layout page

The video/guide covers: create layout page; add/configure blocks; rows and columns; add/configure fields; duplicate/move fields and blocks; delete; block colour.

Default: field **rubrik above** the input. Block setting **Fältrubriker bredvid fält** puts labels beside inputs.

That setting does **not** apply (need full width) for:

- Bokningsfält
- Etikettfält
- Filuppladdningsfält
- Kartfält, generellt
- Kryssrutor with 3+ columns
- Läggtillradfält with 2+ columns
- Radioknappar with 3+ columns
- Tabellfält
- Ärendeinformationsfält
- Ärendeväljarfält

Block setting **Dölj i ärende-PDF** hides the whole block from the case PDF (default: blocks with answers are shown).

Search/navigate-to-field is a separate short guide (video).

## Preview

**Förhandsvisa e-tjänsten** in the builder opens the flow in a new tab (like **Testa e-tjänsten**). Stay on the working page, edit in the builder, **Spara**, then refresh the preview tab. Log prints on the page.

Does not re-run the whole flow: no logikhopp, no previous-page `GetNextPage` prefills, no tabellfält. Moving pages breaks the preview.

Do **not** publish from preview. Do not open Mina ärenden or other citizens’ cases.

## Shortcuts (layout pages)

| Keys | Action |
| --- | --- |
| Ctrl+C | Copy field |
| Ctrl+X | Cut field |
| Ctrl+V | Paste into a placeholder |
| Del | Delete field |
| Ctrl+S | Save (whole builder) |
| Escape | Undo last shortcut |
