# Abou web guard — kunskapsbas

Begränsar webbläsararbete till allowlistad dokumentation eller byggare. Läs före varje webbläsaranrop mot Sokigo/Abou.

Detta är en **sammanslagen kunskapsfil** för en AI. All kunskap från skillen `abou-web-guard` ligger här. Svara från den här filen. Hitta inte på API:er, behörigheter eller fält som inte står här. Svenska UI-namn från Abou gäller.

Källfiler (samma innehåll som under `.cursor/skills/`):

- `SKILL.md`

---

## Källa: `SKILL.md`

# Abou web access guard

The user builds Sokigo **Abou** e-tjänster in the browser. Do **not** roam Abou admin, citizen cases, or other hosts. Read this skill before any browser tool call against Sokigo/Abou.

## Before browsing

1. The user must give a **base URL** (documentation or builder). Until they do, do not navigate.
2. Confirm they are already logged in if the page requires auth. Do not type passwords. If a login form appears, **stop and ask** them to log in.
3. One session = one tab. Lock the tab, work, unlock when done.

## Allowlist

Allowed only if the URL is on the **same host** and under the **same path prefix** as the base URL they gave.

Current known docs base (when the user pointed here):

- Host: `dok.sokigo.com`
- Prefix: `/pages/` and `/display/ABOU/` (Confluence in the **Abou** space only).
- In-scope documentation: the whole Abou tree — *Att bygga e-tjänster*, *Integrationer*, *Abou* (behörighet, schemaläggning, Min sida, köer, moduler, admin, teknisk information, …).
- Out of scope even on this host: other Sokigo products (**Minut Bygg**, **Minut Miljö**), user profiles (`/display/~`), logout, Community file dumps unless the user asked to update those notes.
- **Skill files are the knowledge base.** Answer from `build-abou-etjanst-web` and `abou-platform`. The wiki is behind login; agents usually cannot open it. Browse Confluence only to **fill or correct** those files while the user is already logged in — never as the way to answer a question.

When they later give a builder base (e.g. a municipal Abou host or Provrummet), replace the allowlist for that session. Do not keep using the docs host to open the builder, or the builder host to open unrelated admin.

## Forbidden (stop and ask)

- Any other host (Google, Sokigo marketing, GitHub, mail, IdP except the login page they must complete themselves)
- Live Abou **Admin**, Mina ärenden, handläggarvyer, ärendelistor, medborgardata (docs about those screens are OK; opening real cases is not)
- Användaradmin on a **customer site**, impersonation, other customers’ tjänster
- Logout, “impersonate”, switching user
- Creating, publishing, or deleting a live e-tjänst unless the user explicitly asked in **this** message
- Following a link off the allowlist “to see how something works”

If a link is off-allowlist: do not click. Tell the user the URL and wait.

## Screenshots

Do not capture pages that show personnummer, names of citizens, or case contents. Skip those pages.

## After reading

Write notes into `build-abou-etjanst-web` (builder) or `abou-platform` (admin/modules/technical). Do not paste secrets, API keys, personnummer, or customer case dumps into git.


---
