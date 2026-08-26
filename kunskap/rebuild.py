#!/usr/bin/env python3
"""Concatenate each Cursor skill into one markdown knowledge-base file for RAG."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".cursor/skills"
OUT = Path(__file__).resolve().parent

SKIP_NAMES = {"README.md"}
SKIP_RELATIVE = {"references/INDEX.md"}

MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BACKTICK_PATH = re.compile(
    r"`(?:[^`]*\.md[^`]*|\.\.?/[^`]+|(?:build-abou-etjanst-web|abou-platform|abou-web-guard)[^`]*)`"
)
SKILL_PATH = re.compile(r"\.cursor/skills/\S+")


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    return text[end + 5 :].lstrip("\n")


def _replace_md_link(match: re.Match[str]) -> str:
    label, url = match.group(1), match.group(2)
    url_l = url.lower()
    is_file = (
        url_l.endswith(".md")
        or ".md#" in url_l
        or url_l.startswith("references/")
        or "../" in url
        or ".cursor" in url_l
        or url_l.startswith("build-abou")
        or url_l.startswith("abou-")
    )
    if not is_file:
        return match.group(0)
    if label.endswith(".md") or "/" in label or label.startswith("references"):
        return ""
    return label


def strip_skill_refs(text: str) -> str:
    """Remove pointers to skill files so RAG does not cite them."""
    text = MD_LINK.sub(_replace_md_link, text)
    text = BACKTICK_PATH.sub("", text)
    text = SKILL_PATH.sub("", text)
    text = re.sub(r"\b[\w./-]+\.md\b", "", text)
    text = re.sub(r"`references/`", "", text)
    text = re.sub(r"this folder \(\s*\)", "this documentation", text)
    text = re.sub(r":\s*\.(?=\s|$)", ".", text)
    text = re.sub(r"(?i)^notes:\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\(\s*\)", "", text)
    text = re.sub(r"\s+—\s*\.", ".", text)
    text = re.sub(r"\b[Ss]ee\s*\.", "", text)
    text = re.sub(r":\s*,(?:\s*,)*\s*\.?", ".", text)
    text = re.sub(r",\s*\.", ".", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" +", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def collect_md(skill_dir: Path, ordered: list[str] | None = None) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()

    def add(rel: str) -> None:
        p = skill_dir / rel
        if p.is_file() and p not in seen and p.name not in SKIP_NAMES:
            rel = p.relative_to(skill_dir).as_posix()
            if rel in SKIP_RELATIVE:
                return
            files.append(p)
            seen.add(p)

    if skill_dir.name == "abou-web-guard":
        add("SKILL.md")
    for rel in ordered or []:
        add(rel)

    remaining = sorted(
        p
        for p in skill_dir.rglob("*.md")
        if p not in seen
        and p.name not in SKIP_NAMES
        and p.relative_to(skill_dir).as_posix() not in SKIP_RELATIVE
        and not (p.name == "SKILL.md" and skill_dir.name != "abou-web-guard")
    )
    files.extend(remaining)
    return files


def render(title: str, blurb: str, files: list[Path]) -> str:
    parts: list[str] = [
        f"# {title}",
        "",
        blurb,
        "",
        "Detta är en **självständig kunskapsfil för RAG**. Svara från den här texten. "
        "Hitta inte på API:er, behörigheter eller fält som inte står här. "
        "Svenska UI-namn från Abou gäller. Referera inte till interna dokumentationsfiler.",
        "",
        "---",
        "",
    ]
    for p in files:
        body = strip_skill_refs(strip_frontmatter(p.read_text(encoding="utf-8")))
        if not body.strip():
            continue
        parts.append(body.rstrip())
        parts.append("")
        parts.append("---")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    guard_dir = SKILLS / "abou-web-guard"
    (OUT / "abou-web-guard.md").write_text(
        render(
            "Abou web guard — kunskapsbas",
            "Begränsar webbläsararbete till allowlistad dokumentation eller byggare. "
            "Läs före varje webbläsaranrop mot Sokigo/Abou.",
            collect_md(guard_dir),
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
            "Bygg Abou e-tjänst — kunskapsbas",
            "All kunskap för **e-tjänstebyggaren**: sidor, fält, fältregler, validatorer, "
            "Python/JS-bibliotek, logikmallar och Integrationer (Navet, REST, betalning, AD, EDP, …).",
            collect_md(builder_dir, builder_order),
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
            "Abou-plattform — kunskapsbas",
            "All kunskap utanför byggaren: behörigheter, admin, ärenden, Min sida, köer, "
            "bokning, register, e-förslag, schemaläggning, dokumentmallar, FAQ, Funktionalitet, "
            "REST-metodnamn, CitizenInfo, HtmlCaseModel, GDPR/TLS.",
            collect_md(platform_dir, platform_order),
        ),
        encoding="utf-8",
    )

    for name in ("abou-web-guard.md", "build-abou-etjanst-web.md", "abou-platform.md"):
        p = OUT / name
        print(f"{name}: {p.stat().st_size} bytes, {p.read_text().count(chr(10))} lines")


if __name__ == "__main__":
    main()
