# Checklista och deploy

Confluence: *Projektdokument, Checklistor Och Processer* — **Checklista: Driftsättning av e-tjänst** and **Deployprocess**.

Until those pages are copied into this file, use what is already known elsewhere in the skill:

- Builder work in **test**; import to prod grants **Redaktör** only ([admin.md](admin.md), [faq.md](faq.md)).
- Publishing a service ≠ activating it. Menygrupper can stay hidden if empty. Blankett link is a separate publish tick ([admin.md](admin.md), [document-templates.md](document-templates.md)).
- Python needs system right **Redigera och exekvera Python-kod**; ThankYou Python plugin may need app-pool recycle (builder `logic.md`).
- Rights: importer cannot see cases until someone grants Läs/Status/Verksamhetsadmin ([permissions.md](permissions.md)).
- Integrations (Navet, payment, e-leg, AD, REST) are Sokigo/sysadmin — not finished by a field tick alone.
- Test mail often hits a generic mailbox, not the real address ([faq.md](faq.md)).
- Do not delete a production e-tjänst until cases/köer/bokningar are removed ([admin.md](admin.md)).

Do not invent a Sokigo deploy pipeline (IIS, slots, who clicks deploy). Kundservice/Support process is not in this skill.
