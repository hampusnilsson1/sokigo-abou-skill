# Kunskapsbaser (en fil per skill)

Tre markdownfiler med **all kunskap** från respektive Cursor-skill. Ladda in dem i en AI som kunskapsbas (Custom GPT, projektfil, RAG). Wiki på dok.sokigo.com krävs inte.

| Fil | Innehåll |
| --- | --- |
| [abou-web-guard.md](abou-web-guard.md) | Allowlist för webbläsare mot Abou-dokumentation/byggare |
| [build-abou-etjanst-web.md](build-abou-etjanst-web.md) | E-tjänstebyggaren: sidor, fält, logikmallar, Integrationer |
| [abou-platform.md](abou-platform.md) | Admin, behörigheter, Min sida, köer, FAQ, REST, m.m. |

Cursor-agenter ska fortfarande använda `.cursor/skills/` (en referensfil i taget). De här filerna är samma innehåll, samlat.

Efter ändringar i skillarna: `python3 kunskap/rebuild.py`
