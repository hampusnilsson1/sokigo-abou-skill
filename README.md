# sokigo-abou-skill

Cursor skills for Sokigo [Abou](https://sokigo.com/produkter/abou/) e-tjänster (**Abou / Calamare**, not Open ePlatform).

Build in the **e-tjänstebyggaren** (browser). Skill: `.cursor/skills/build-abou-etjanst-web/`. Notes come from Sokigo docs [Att bygga e-tjänster](https://dok.sokigo.com/pages/viewpage.action?pageId=56918159) (login required). Browser work is limited by `.cursor/skills/abou-web-guard/`.

## Use in Cursor

Ask the agent to help **build an e-tjänst in the web builder**. It should use Swedish builder names (Layoutsida, Fältregler, Multipelsignering, …).

## Builder docs

`.cursor/skills/build-abou-etjanst-web/references/` — builder behaviour, **library docs** (`logic-templates/libraries.md` for PageNode/PageLogic), **integration how-to** (`integrations/`), and mallar as examples.

## Public sources

- [Sokigo Abou product](https://sokigo.com/produkter/abou/) — builder, registers, booking, payment, e-ID
- [Abou e-tjänstebyggande courses](https://sokigo.com/kurser/abou-e-tjanstebyggande-steg-1/) — pages, fields, validation, emails, publish
- [Provrummet](https://abou-provrummet.sokigohosting.com/DELAETJANST) — shared catalog; no legacy fältsidor
