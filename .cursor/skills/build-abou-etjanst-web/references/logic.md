# Python and client logic

Where to type code in the builder, and how it relates to the **libraries**.

**How the APIs work** (read this when explaining or reviewing, not only when pasting a new file): [logic-templates/libraries.md](logic-templates/libraries.md).

Sokigo supports the **mallar in the builder** plus the listed PageNode / PageLogic methods. Other Python/JS is the municipality’s own risk. Do not invent methods.

Prefer **fältregler / visningsvillkor** ([rules-validators.md](rules-validators.md)) before code.

## Where to write it

- **Logik** tab: IronPython `PageNode`. `Initialize` on enter, `BeforeGetNextPage` before leave, `GetNextPage` must return a page. Class name = IronPythonType = page systemnamn.
- **Klientlogik** tab: JavaScript `PageLogic` on **Layoutsida** only. Runs when answers on **this page** change.
- Thank-you: `Published(self)` → `PublishedResult`. Mall: [logic-templates/thankyou.md](logic-templates/thankyou.md).

Field ids: `'x.1'` = current short name + number.

Method lists: [pagenode-api.md](logic-templates/pagenode-api.md), [client/api.md](logic-templates/client/api.md). Worked examples: [INDEX.md](logic-templates/INDEX.md).

## Thank-you plugin (sysadmin)

Confluence: *Kod på tacksidor - PythonCaseService och PythonPlugin*. Needs app-pool recycle (`Python plugin loaded`).

`IPythonCaseService`: `AddRelationToCase`, `UpdateStateForCase`, `AssignAdministratorToCase`, `RegisterCase`. Normal `GetAnswer` does not work; use published-case helpers in the thank-you mall. See [libraries.md](logic-templates/libraries.md).

## Preview

**Förhandsvisa** reloads **this page only**. No logikhopp, no previous-page `GetNextPage` prefills, no tabellfält. **Visa skriptlogg** shows `Log*`.
