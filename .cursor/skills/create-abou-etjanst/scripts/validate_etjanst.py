#!/usr/bin/env python3
"""Validate an Abou e-tjänst zip or a Service/Content pair.

Usage:
  python validate_etjanst.py MyService.zip
  python validate_etjanst.py --service Service --content Content
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


ZIP_NAME_RE = re.compile(
    r"^(?P<short>.+)-(?P<nr>\d+)-(?P<date>\d{4}-\d{2}-\d{2})-export(?:\.zip)?$",
    re.IGNORECASE,
)

KNOWN_PAGE_URLS = {
    "BlockPage.aspx",
    "FieldPage.aspx",
    "Summary.aspx",
    "SignEID.aspx",
    "ThankYou.aspx",
    "PaymentPage.aspx",
    "PaymentThankYou.aspx",
}

VERIFIED_FIELD_TYPES = {
    "EGovTextField",
    "EGovRadioButtonField",
    "EGovCheckBoxField",
    "EGovDropDownField",
    "EGovDateChooserField",
    "EGovEmailField",
    "EGovLabelField",
    "FirstNameField",
    "LastNameField",
    "IntegratedEmailField",
    "PostcodeField",
    "PhoneNumberField",
    "IntegratedSocialSecurityNumberField",
    "AddressField",
    "IntegratedPostcodeField",
    "CityField",
    "HomePhoneField",
    "TableField",
    "SocialSecurityNumberField",
    "FileUploadField2",
    "MobilePhoneField",
    "ReservationField2",
    "QueueField",
    "OrganisationNumberField",
    "EGovAddRows2ColumnsListField",
    "EGovAddRows3ColumnsListField",
    "EGovAddRows4ColumnsListField",
    "EGovAddRows5ColumnsListField",
}

DOCUMENTED_FIELD_TYPES = VERIFIED_FIELD_TYPES | {
    "EGovNavigationButtonField",
    "ServiceBlockAccessField",
    "EGovPastCasesDisplayField",
}


def read_zip(path: Path) -> tuple[str, str]:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        service_name = next(
            (n for n in names if n.replace("\\", "/").rstrip("/").endswith("Service") and not n.endswith("/")),
            None,
        )
        content_name = next(
            (n for n in names if n.replace("\\", "/").rstrip("/").endswith("Content") and not n.endswith("/")),
            None,
        )
        if not service_name or not content_name:
            raise SystemExit(
                "zip must contain Service/Service and Service/Content "
                f"(found: {names})"
            )
        service = zf.read(service_name).decode("utf-8")
        content = zf.read(content_name).decode("utf-8")
        return service, content


def parse_xml(text: str, label: str) -> ET.Element:
    try:
        return ET.fromstring(text)
    except ET.ParseError as exc:
        raise SystemExit(f"{label} is not well-formed XML: {exc}") from exc


def local(tag: str) -> str:
    return tag.split("}", 1)[-1]


def children(el: ET.Element) -> list[ET.Element]:
    return list(el)


def text_of(el: ET.Element | None) -> str:
    if el is None or el.text is None:
        return ""
    return el.text.strip()


def find_direct(el: ET.Element, name: str) -> list[ET.Element]:
    return [c for c in el if local(c.tag) == name]


def first(el: ET.Element, name: str) -> ET.Element | None:
    found = find_direct(el, name)
    return found[0] if found else None


def validate(
    service_xml: str, content_xml: str, *, zip_path: Path | None = None
) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    service = parse_xml(service_xml, "Service")
    content = parse_xml(content_xml, "Content")
    if local(service.tag) != "Service":
        errors.append(f"Service root is <{local(service.tag)}>, expected <Service>")
    if local(content.tag) != "Content":
        errors.append(f"Content root is <{local(content.tag)}>, expected <Content>")

    short_nodes = find_direct(service, "ServiceShortName")
    short = text_of(short_nodes[0]) if short_nodes else ""
    if not short:
        errors.append("ServiceShortName is missing")
    elif not re.match(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,39}$", short):
        errors.append(f"ServiceShortName {short!r} looks invalid")

    ids = find_direct(service, "Id")
    if len(ids) < 2:
        errors.append("Service should have two <Id> elements (entity + content)")

    pages_parent = first(service, "Pages")
    if pages_parent is None:
        errors.append("Service has no <Pages>")
        return errors + [f"warning: {w}" for w in warnings]

    pages = find_direct(pages_parent, "Page")
    if not pages:
        errors.append("Service has no pages")

    page_names = []
    page_entity_ids = {}
    page_content_ids = {}
    field_ids = []
    field_content_ids = []
    urls = []
    for page in pages:
        name = text_of(first(page, "PageName"))
        page_names.append(name)
        url = text_of(first(page, "PageURL"))
        urls.append(url)
        if url and url not in KNOWN_PAGE_URLS:
            warnings.append(f"page {name}: uncommon PageURL {url}")
        if url == "FieldPage.aspx":
            warnings.append(
                f"page {name}: FieldPage.aspx is a legacy fältsida; "
                "new packages should use BlockPage.aspx"
            )
        page_ids = find_direct(page, "Id")
        if len(page_ids) < 2:
            errors.append(f"page {name}: expected two <Id> elements")
        else:
            page_entity_ids[name] = text_of(page_ids[0])
            page_content_ids[name] = text_of(page_ids[1])
        fields_parent = first(page, "Fields")
        if fields_parent is None:
            continue
        for field in find_direct(fields_parent, "Field"):
            fid = text_of(first(field, "FriendlyFieldID"))
            field_ids.append(fid)
            if short and fid and not fid.startswith(f"{short}."):
                errors.append(f"field {fid} does not start with {short}.")
            ftype = text_of(first(field, "TypeOfField"))
            if ftype and ftype not in DOCUMENTED_FIELD_TYPES:
                warnings.append(f"field {fid}: unknown TypeOfField {ftype}")
            if ftype in {
                "EGovRadioButtonField",
                "EGovCheckBoxField",
                "EGovDropDownField",
            } and not text_of(first(field, "QuestionAlternatives")):
                errors.append(f"field {fid}: {ftype} has no alternatives")
            fids = find_direct(field, "Id")
            if len(fids) < 2:
                errors.append(f"field {fid}: expected two <Id> elements")
            else:
                field_content_ids.append(text_of(fids[1]))
            page_id = text_of(first(field, "PageID"))
            if name in page_entity_ids and page_id != page_entity_ids[name]:
                errors.append(
                    f"field {fid}: PageID {page_id} != page entity id {page_entity_ids[name]}"
                )

    if len(page_names) != len(set(page_names)):
        errors.append("duplicate page names")
    if len(field_ids) != len(set(field_ids)):
        errors.append("duplicate FriendlyFieldID values")

    required_system = {"SummaryPage", "ThankYou"}
    missing_sys = required_system - set(page_names)
    if missing_sys:
        warnings.append(f"missing typical system pages: {sorted(missing_sys)}")
    if "SignEID.aspx" not in urls and text_of(first(service, "RequiresSignature")) == "true":
        warnings.append("RequiresSignature is true but no SignEID.aspx page was found")
    if "PaymentPage.aspx" in urls or "PaymentThankYou.aspx" in urls:
        warnings.append(
            "payment pages are present; clone PageNodes from a current export "
            "(RequiresPayment may still be false)"
        )

    contents_pages = first(content, "PageContents")
    content_page_ids = []
    content_page_names = []
    if contents_pages is not None:
        for pc in find_direct(contents_pages, "PageContent"):
            content_page_names.append(text_of(first(pc, "PageName")))
            content_page_ids.append(text_of(first(pc, "Id")))
    for name, cid in page_content_ids.items():
        if name not in content_page_names:
            errors.append(f"page {name} is missing from Content/PageContents")
        elif cid not in content_page_ids:
            errors.append(f"page {name} content Id {cid} not found in Content")

    extra_content_pages = set(content_page_names) - set(page_names)
    if extra_content_pages:
        warnings.append(
            f"Content has pages not present in Service: {sorted(extra_content_pages)}"
        )

    field_contents = first(content, "FieldContents")
    content_field_ids = []
    if field_contents is not None:
        for fc in find_direct(field_contents, "FieldContent"):
            content_field_ids.append(text_of(first(fc, "Id")))
            ffid = text_of(first(fc, "FriendlyFieldId"))
            if ffid and ffid not in field_ids:
                warnings.append(f"Content FieldContent {ffid} has no Service field")
    for cid in field_content_ids:
        if cid not in content_field_ids:
            errors.append(f"field content Id {cid} missing from Content/FieldContents")

    svc_contents = first(content, "ServiceContents")
    if svc_contents is None or not find_direct(svc_contents, "ServiceContent"):
        errors.append("Content is missing ServiceContents/ServiceContent")
    else:
        sc = find_direct(svc_contents, "ServiceContent")[0]
        sc_id = text_of(first(sc, "Id"))
        if len(ids) >= 2 and sc_id != text_of(ids[1]):
            errors.append("Service content Id does not match Content ServiceContent Id")

    try:
        json.loads(text_of(first(service, "Properties")) or "[]")
    except json.JSONDecodeError:
        errors.append("Service Properties is not valid JSON")

    if zip_path is not None:
        name = zip_path.name
        match = ZIP_NAME_RE.match(name)
        service_nr = text_of(first(service, "ServiceNr"))
        last_updated = text_of(first(service, "LastUpdated"))
        expected = f"{short}-{service_nr}-YYYY-MM-DD-export.zip"
        if not match:
            warnings.append(
                f"zip name {name!r} does not match Abou export pattern "
                f"{{kortnamn}}-{{ServiceNr}}-{{YYYY-MM-DD}}-export.zip "
                f"(example: KOMPOST-150-2026-08-20-export.zip; expected from XML: {expected})"
            )
        else:
            if short and match.group("short") != short:
                errors.append(
                    f"zip kortnamn {match.group('short')!r} != ServiceShortName {short!r}"
                )
            if service_nr and match.group("nr") != service_nr:
                errors.append(
                    f"zip ServiceNr {match.group('nr')!r} != ServiceNr {service_nr!r}"
                )
            updated_day = last_updated[:10] if last_updated else ""
            if updated_day and match.group("date") != updated_day:
                warnings.append(
                    f"zip date {match.group('date')} differs from LastUpdated {updated_day}"
                )

    return errors + [f"warning: {w}" for w in warnings]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an Abou e-tjänst package")
    parser.add_argument("zip", nargs="?", type=Path)
    parser.add_argument("--service", type=Path)
    parser.add_argument("--content", type=Path)
    args = parser.parse_args(argv)

    if args.zip:
        service_xml, content_xml = read_zip(args.zip)
        messages = validate(service_xml, content_xml, zip_path=args.zip)
    elif args.service and args.content:
        service_xml = args.service.read_text(encoding="utf-8")
        content_xml = args.content.read_text(encoding="utf-8")
        messages = validate(service_xml, content_xml)
    else:
        parser.error("provide a zip or --service and --content")
    errors = [m for m in messages if not m.startswith("warning:")]
    warnings = [m for m in messages if m.startswith("warning:")]
    for msg in messages:
        print(msg, file=sys.stderr if not msg.startswith("warning:") else sys.stdout)
    if errors:
        print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
