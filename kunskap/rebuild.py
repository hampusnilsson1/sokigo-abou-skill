#!/usr/bin/env python3
"""Concatenate each Cursor skill into one markdown knowledge-base file."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".cursor/skills"
OUT = Path(__file__).resolve().parent

SKIP_NAMES = {"README.md"}


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    return text[end + 5 :].lstrip("\n")


def collect_md(skill_dir: Path, ordered: list[str] | None = None) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    def add(rel: str) -> None:
        p = skill_dir / rel
        if p.is_file() and p not in seen:
            files.append(p)
            seen.add(p)

    add("SKILL.md")
    for rel in ordered or []:
        add(rel)

    remaining = sorted(
        p
        for p in skill_dir.rglob("*.md")
        if p not in seen and p.name not in SKIP_NAMES
    )
    files.extend(remaining)
    return files


def render(skill_id: str, title: str, blurb: str, files: list[Path], skill_dir: Path) -> str:
    parts: list[str] = [
        f"# {title}",
        "",
        blurb,
        "",
        "Detta är en **sammanslagen kunskapsfil** för en AI. All kunskap från skillen "
        f"`{skill_id}` ligger här. Svara från den här filen. Hitta inte på API:er, "
        "behörigheter eller fält som inte står här. Svenska UI-namn från Abou gäller.",
        "",
        "Källfiler (samma innehåll som under `.cursor/skills/`):",
        "",
    ]
    for p in files:
        rel = p.relative_to(skill_dir).as_posix()
        parts.append(f"- `{rel}`")
    parts += ["", "---", ""]

    for p in files:
        rel = p.relative_to(skill_dir).as_posix()
        body = strip_frontmatter(p.read_text(encoding="utf-8")).rstrip() + "\n"
        parts.append(f"## Källa: `{rel}`")
        parts.append("")
        parts.append(body)
        parts.append("")
        parts.append("---")
        parts.append("")

    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    guard_dir = SKILLS / "abou-web-guard"
    (OUT / "abou-web-guard.md").write_text(
        render(
            "abou-web-guard",
            "Abou web guard — kunskapsbas",
            "Begränsar webbläsararbete till allowlistad dokumentation eller byggare. "
            "Läs före varje webbläsaranrop mot Sokigo/Abou.",
            collect_md(guard_dir),
            guard_dir,
        ),
        encoding="utf-8",
    )

    builder_dir = SKILLS / "build-abou-etjanst-web"
    builder_order = [
        "references/catalog.md",
        "references/builder-ui.md",
        "references/create-and-settings.md",
        "references/pages-and-fields.md",
        "references/field-types.md",
        "references/rules-validators.md",
        "references/logic.md",
        "references/messages.md",
        "references/logic-templates/INDEX.md",
        "references/logic-templates/libraries.md",
        "references/logic-templates/pagenode-api.md",
        "references/logic-templates/standard.md",
        "references/logic-templates/url-parameters.md",
        "references/logic-templates/payment.md",
        "references/logic-templates/custom-validation.md",
        "references/logic-templates/booking-filter.md",
        "references/logic-templates/file-upload.md",
        "references/logic-templates/navet-dropdown.md",
        "references/logic-templates/navet-table.md",
        "references/logic-templates/prefill-multisign.md",
        "references/logic-templates/prefill-case-selector.md",
        "references/logic-templates/prefill.md",
        "references/logic-templates/required-when-hidden.md",
        "references/logic-templates/hide-fields-blocks.md",
        "references/logic-templates/ad-lookup.md",
        "references/logic-templates/logging.md",
        "references/logic-templates/page-skip.md",
        "references/logic-templates/calculations.md",
        "references/logic-templates/table-field.md",
        "references/logic-templates/thankyou.md",
        "references/logic-templates/extended-citizen.md",
        "references/logic-templates/client/api.md",
        "references/logic-templates/client/empty.md",
        "references/logic-templates/client/handle-field.md",
        "references/logic-templates/client/handle-many.md",
        "references/logic-templates/client/hide-block-on-value.md",
        "references/integrations/INDEX.md",
        "references/integrations/catalog.md",
        "references/integrations/navet.md",
        "references/integrations/bolagsverket.md",
        "references/integrations/adapter-rest.md",
        "references/integrations/e-legitimation.md",
        "references/integrations/sokigo-fb.md",
        "references/integrations/geo.md",
        "references/integrations/payment.md",
        "references/integrations/sms.md",
        "references/integrations/mina-meddelanden.md",
        "references/integrations/active-directory.md",
        "references/integrations/edp-future.md",
        "references/integrations/verksamhetssystem.md",
        "references/integrations/plattformar.md",
        "references/integrations/arkiv.md",
        "references/integrations/ovrigt.md",
    ]
    (OUT / "build-abou-etjanst-web.md").write_text(
        render(
            "build-abou-etjanst-web",
            "Bygg Abou e-tjänst — kunskapsbas",
            "All kunskap för **e-tjänstebyggaren**: sidor, fält, fältregler, validatorer, "
            "Python/JS-bibliotek, logikmallar och Integrationer (Navet, REST, betalning, AD, EDP, …).",
            collect_md(builder_dir, builder_order),
            builder_dir,
        ),
        encoding="utf-8",
    )

    platform_dir = SKILLS / "abou-platform"
    platform_order = [
        "references/INDEX.md",
        "references/catalog.md",
        "references/permissions.md",
        "references/scheduling.md",
        "references/min-sida.md",
        "references/queues.md",
        "references/modules.md",
        "references/document-templates.md",
        "references/admin.md",
        "references/cases.md",
        "references/booking.md",
        "references/registers.md",
        "references/e-forslag.md",
        "references/functionality.md",
        "references/faq.md",
        "references/sharing.md",
        "references/operations.md",
        "references/message-tokens.md",
        "references/technical/INDEX.md",
        "references/technical/rest-api.md",
        "references/technical/citizeninfo.md",
        "references/technical/htmlcasemodel.md",
        "references/technical/compliance.md",
    ]
    (OUT / "abou-platform.md").write_text(
        render(
            "abou-platform",
            "Abou-plattform — kunskapsbas",
            "All kunskap utanför byggaren: behörigheter, admin, ärenden, Min sida, köer, "
            "bokning, register, e-förslag, schemaläggning, dokumentmallar, FAQ, Funktionalitet, "
            "REST-metodnamn, CitizenInfo, HtmlCaseModel, GDPR/TLS.",
            collect_md(platform_dir, platform_order),
            platform_dir,
        ),
        encoding="utf-8",
    )

    for name in ("abou-web-guard.md", "build-abou-etjanst-web.md", "abou-platform.md"):
        p = OUT / name
        print(f"{name}: {p.stat().st_size} bytes, {p.read_text().count(chr(10))} lines")


if __name__ == "__main__":
    main()
