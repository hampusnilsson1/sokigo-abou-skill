#!/usr/bin/env python3
"""Build an Abou/Sokigo e-tjänst import zip from a JSON definition.

Abou export zip names follow:

  {kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export.zip

Example: KOMPOST-150-2026-08-20-export.zip

Inside the zip the payload is always Service/Service + Service/Content.

Usage:
  python package_etjanst.py definition.json
  python package_etjanst.py definition.json -o KOMPOST-150-2026-08-20-export.zip
  python package_etjanst.py definition.json --stdout-dir /tmp/out
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from xmlutil import XmlWriter, join_alternatives


CHOICE_FIELD_TYPES = {
    "EGovRadioButtonField",
    "EGovCheckBoxField",
    "EGovDropDownField",
}

ADD_ROWS_COLUMN_COUNTS = {
    "EGovAddRows2ColumnsListField": 2,
    "EGovAddRows3ColumnsListField": 3,
    "EGovAddRows4ColumnsListField": 4,
    "EGovAddRows5ColumnsListField": 5,
}

SYSTEM_PAGE_URLS = {
    "SummaryPage": "Summary.aspx",
    "SignPage": "SignEID.aspx",
    "Sign": "SignEID.aspx",
    "ThankYou": "ThankYou.aspx",
    "payment": "PaymentPage.aspx",
}

SHORT_NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,39}$")

DEFAULT_UPDATED_BY = "hani001"
DEFAULT_UPDATED_BY_NAME = "Hampus Nilsson"

DEFAULT_SLOT_SETTINGS = {
    "Filter": None,
    "ShowAdminUser": False,
    "DefaultSpanMinutes": 30,
    "ReservationTimeoutMinutes": 20,
    "NotifyAdministratorEmailMessageId": 0,
    "IncludeICalendar": False,
    "CancelHourLimit": 0,
}

DEFAULT_ACTIVATION = {
    "enabled": False,
    "field": None,
    "answer": "",
    "condition": "Equals",
    "setsVisibility": False,
    "setsMandatory": False,
}

DEPENDENCY_VALIDATOR = {
    "Name": "FieldAnswerDependencyValidator",
    "Description": "Beroende",
    "HelpText": (
        "Validatorn används för att göra aktuellt fält obligatoriskt beroende "
        "på svaret i ett annat fält."
    ),
    "WhiteList": [],
    "BlackList": [
        "EGovLabelField",
        "ServiceBlockAccessField",
        "EGovNavigationButtonField",
        "EGovPastCasesDisplayField",
    ],
}


def arg_names(args: list[dict[str, Any]]) -> set[str]:
    return {str(a.get("name")) for a in args}


def normalize_column(col: Any) -> dict[str, Any]:
    if isinstance(col, str):
        return {"question": col}
    if isinstance(col, dict):
        return col
    raise SystemExit(f"add-rows column must be a string or object, got {type(col)}")


def expand_columns(field: dict[str, Any]) -> list[dict[str, Any]]:
    columns = field.get("columns")
    if not columns:
        return []
    args: list[dict[str, Any]] = []
    for i, raw in enumerate(columns, start=1):
        col = normalize_column(raw)
        title = col.get("question") or col.get("label") or ""
        args.append({"name": f"Question{i}", "value": title})
        if col.get("validator"):
            args.append({"name": f"Answer{i}Validator", "value": col["validator"]})
        summarized = col.get("summarizedNumbers")
        if summarized and summarized is not True:
            args.append({"name": f"Answer{i}SummarizedNumbers", "value": str(summarized)})
    return args


def build_field_arguments(field: dict[str, Any]) -> list[dict[str, Any]]:
    args = [dict(a) for a in (field.get("arguments") or [])]
    names = arg_names(args)
    ftype = str(field.get("type") or "")

    for col_arg in expand_columns(field):
        if col_arg["name"] not in names:
            args.append(col_arg)
            names.add(col_arg["name"])

    if ftype == "FileUploadField2":
        if "RequireFileDescription" not in names:
            args.append(
                {
                    "name": "RequireFileDescription",
                    "value": "True" if field.get("requireFileDescription") else "False",
                }
            )
            names.add("RequireFileDescription")
        if "AllowMultiple" not in names:
            args.append(
                {
                    "name": "AllowMultiple",
                    "value": "True" if field.get("allowMultiple") else "False",
                }
            )
            names.add("AllowMultiple")
        if field.get("maxFileSize") is not None and "MaxFileSize" not in names:
            args.append({"name": "MaxFileSize", "value": str(field["maxFileSize"])})
            names.add("MaxFileSize")

    if field.get("enabled") is False and "Enabled" not in names:
        args = [{"name": "Enabled", "value": "false"}, *args]
        names.add("Enabled")
    if field.get("hide") and "Hide" not in names:
        args = [{"name": "Hide", "value": "True"}, *args]
    return args


def dependency_validator(short: str, field: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    return {
        **DEPENDENCY_VALIDATOR,
        "Arguments": [
            {
                "Name": "FieldOnPage",
                "Description": "Välj fält",
                "Value": friendly_id(short, spec["field"]),
                "Type": "FieldSingleSelect",
                "Data": None,
                "Placeholder": "Välj fält",
                "IsRequired": True,
            },
            {
                "Name": "FieldAnswer",
                "Description": "Fältsvar",
                "Value": spec["answer"],
                "Type": "Text",
                "Data": None,
                "Placeholder": None,
                "IsRequired": True,
            },
            {
                "Name": "ErrorText",
                "Description": "Felmeddelande",
                "Value": spec.get("errorText")
                or field.get("question")
                or "Obligatoriskt fält",
                "Type": "Text",
                "Data": None,
                "Placeholder": None,
                "IsRequired": True,
            },
        ],
    }


class IdPool:
    def __init__(self, start: int = 1000) -> None:
        self._n = start

    def next(self) -> int:
        self._n += 1
        return self._n


def load_definition(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("Definition must be a JSON object")
    return data


def validate_definition(defn: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    short = str(defn.get("shortName") or "").strip()
    if not short:
        errors.append("shortName is required")
    elif not SHORT_NAME_RE.match(short):
        errors.append(
            "shortName must be 1-40 chars of letters, digits, underscore or hyphen"
        )
    if not str(defn.get("displayName") or defn.get("menuDisplayName") or "").strip():
        errors.append("displayName or menuDisplayName is required")

    pages = defn.get("pages") or []
    if not isinstance(pages, list) or not pages:
        errors.append("pages must be a non-empty list")
        return errors

    names = []
    field_ids = []
    for i, page in enumerate(pages):
        name = str(page.get("name") or "").strip()
        if not name:
            errors.append(f"pages[{i}].name is required")
        elif name in names:
            errors.append(f"duplicate page name {name!r}")
        names.append(name)
        for j, field in enumerate(page.get("fields") or []):
            fid = field.get("id")
            if fid is None:
                errors.append(f"pages[{i}].fields[{j}].id is required")
            else:
                field_ids.append(str(fid))
            if not field.get("type"):
                errors.append(f"pages[{i}].fields[{j}].type is required")
            ftype = str(field.get("type") or "")
            if not field.get("question"):
                if ftype != "EGovLabelField":
                    errors.append(f"pages[{i}].fields[{j}].question is required")
                elif not field.get("preFieldHtml"):
                    errors.append(
                        f"pages[{i}].fields[{j}] (EGovLabelField) needs preFieldHtml"
                    )
            alts = field.get("alternatives") or []
            if ftype in CHOICE_FIELD_TYPES and not alts:
                errors.append(
                    f"pages[{i}].fields[{j}] ({ftype}) needs alternatives"
                )
            columns = field.get("columns")
            expected_cols = ADD_ROWS_COLUMN_COUNTS.get(ftype)
            if columns is not None:
                if expected_cols is None:
                    errors.append(
                        f"pages[{i}].fields[{j}] ({ftype}) does not take columns"
                    )
                elif len(columns) != expected_cols:
                    errors.append(
                        f"pages[{i}].fields[{j}]: {ftype} needs {expected_cols} columns, "
                        f"got {len(columns)}"
                    )
    if len(field_ids) != len(set(field_ids)):
        errors.append("field ids must be unique within the service")
    return errors


def friendly_id(short_name: str, field_id: Any) -> str:
    raw = str(field_id)
    if raw.startswith(f"{short_name}."):
        return raw
    return f"{short_name}.{raw}"


def parse_export_date(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    raw = value.strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            dt = datetime.strptime(raw, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    raise SystemExit(f"invalid export date {value!r}, expected YYYY-MM-DD")


def export_zip_stem(short_name: str, service_nr: int, export_day: date) -> str:
    """Abou download name: KOMPOST-150-2026-08-20-export"""
    return f"{short_name}-{int(service_nr)}-{export_day.isoformat()}-export"


def export_zip_filename(short_name: str, service_nr: int, export_day: date) -> str:
    return export_zip_stem(short_name, service_nr, export_day) + ".zip"


def now_iso(when: datetime | None = None) -> str:
    dt = when or datetime.now(timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def bool_opt(value: Any, default: bool) -> bool:
    if value is None:
        return default
    return bool(value)


def ensure_system_pages(defn: dict[str, Any]) -> list[dict[str, Any]]:
    pages = [dict(p) for p in defn.get("pages") or []]
    names = {p.get("name") for p in pages}

    if defn.get("infoHtml") and "InfoPage" not in names:
        pages.insert(
            0,
            {
                "name": "InfoPage",
                "displayName": "Information",
                "headerHtml": defn.get("infoHtml"),
                "showInSummary": False,
                "fields": [],
                "kind": "info",
            },
        )
        names.add("InfoPage")

    if "SummaryPage" not in names:
        pages.append(
            {
                "name": "SummaryPage",
                "displayName": "Sammanfattningssida",
                "showInSummary": False,
                "fields": [],
                "kind": "summary",
            }
        )
    if bool_opt(defn.get("requiresSignature"), True) and "SignPage" not in names:
        pages.append(
            {
                "name": "SignPage",
                "displayName": "Signeringssida",
                "showInSummary": False,
                "fields": [],
                "kind": "sign",
            }
        )
    if "ThankYou" not in names:
        pages.append(
            {
                "name": "ThankYou",
                "displayName": "Tacksida",
                "headerHtml": defn.get("thankYouHtml") or "<p>Tack för din ansökan.</p>",
                "showInSummary": False,
                "fields": [],
                "kind": "thankyou",
            }
        )
    return pages


def page_url(page: dict[str, Any]) -> str:
    if page.get("url"):
        return str(page["url"])
    name = page.get("name")
    if name in SYSTEM_PAGE_URLS:
        return SYSTEM_PAGE_URLS[name]
    kind = page.get("kind")
    if kind == "summary":
        return "Summary.aspx"
    if kind == "sign":
        return "SignEID.aspx"
    if kind == "thankyou":
        return "ThankYou.aspx"
    if kind == "payment":
        return "PaymentPage.aspx"
    if kind == "paymentthankyou":
        return "PaymentThankYou.aspx"
    return "BlockPage.aspx"


def is_block_page(page: dict[str, Any]) -> bool:
    return page_url(page) == "BlockPage.aspx"


def default_layout(fields: list[dict[str, Any]], short_name: str, block_id: str) -> str:
    layout = []
    widths = []
    for i, field in enumerate(fields):
        layout.append(
            {
                "Id": friendly_id(short_name, field["id"]),
                "Row": i,
                "Col": 0,
            }
        )
        widths.append([{"Xs": 12, "S": 12, "M": 12, "L": 12}])
    if not layout:
        return ""
    area = {
        "BlockId": block_id,
        "Header": None,
        "Color": "#F5F5F5",
        "HideInPdf": False,
        "HorizontalFieldQuestion": False,
        "UsingCustomColor": False,
        "ColumnWidths": widths,
        "FieldLayout": layout,
        "Description": None,
        "ActivationRule": DEFAULT_ACTIVATION,
    }
    return json.dumps([area], ensure_ascii=False, separators=(",", ":"))


def field_has_alternatives(field: dict[str, Any]) -> bool:
    return bool(field.get("alternatives"))


def write_service(
    defn: dict[str, Any], ids: dict[str, Any], *, export_dt: datetime
) -> str:
    w = XmlWriter()
    short = defn["shortName"]
    display = defn.get("displayName") or defn.get("menuDisplayName")
    menu = defn.get("menuDisplayName") or display
    pages = ids["pages"]
    w.open("Service")
    w.int("Version", int(defn.get("version", 1)))
    w.bool("IsAdvancedService", bool_opt(defn.get("isAdvancedService"), False))
    w.bool("AutoDiaryNumbering", bool_opt(defn.get("autoDiaryNumbering"), False))
    w.text("ServiceName", short)
    w.text("ServiceShortName", short)
    w.text("MenuDisplayName", menu)
    w.int("ServiceNr", int(defn.get("serviceNr", ids["serviceNr"])))
    w.bool("AvailableCitizen", bool_opt(defn.get("availableCitizen"), True))
    w.bool("AvailableCompany", bool_opt(defn.get("availableCompany"), False))
    w.bool("AvailableClub", bool_opt(defn.get("availableClub"), False))
    w.bool("IsEnabled", bool_opt(defn.get("isEnabled"), False))
    w.bool("RequiresAuthentication", bool_opt(defn.get("requiresAuthentication"), True))
    w.bool("RequiresSignature", bool_opt(defn.get("requiresSignature"), True))
    w.bool("RequiresPayment", bool_opt(defn.get("requiresPayment"), False))
    w.bool("RequiresDigitalServing", bool_opt(defn.get("requiresDigitalServing"), False))
    w.bool("IsAnonymous", bool_opt(defn.get("isAnonymous"), False))
    w.nil("AvailableYears", "p2")
    w.bool(
        "RequiresMultipleSignatures",
        bool_opt(defn.get("requiresMultipleSignatures"), False),
    )
    w.text(
        "CaseStatusList",
        defn.get("caseStatusList")
        or "Inkommet;Registrerat;Under handläggning;Avslutat",
    )
    w.nil("ExternalURL", "p2")
    w.nil("MenuGroupID", "p2")
    w.bool("AddCaseAttachment", bool_opt(defn.get("addCaseAttachment"), False))
    w.bool("HasAlternativeSigning", bool_opt(defn.get("hasAlternativeSigning"), False))
    w.nil("FieldsToShowInAdmin", "p2")
    w.maybe_text("Note", defn.get("note"), prefix="p2")
    w.nil("QueueFilter", "p2")
    w.raw("LastUpdated", now_iso(export_dt))
    w.text("UpdatedBy", defn.get("updatedBy") or DEFAULT_UPDATED_BY)
    w.text("UpdatedByName", defn.get("updatedByName") or DEFAULT_UPDATED_BY_NAME)
    w.raw("Type", defn.get("type") or "Internal")
    w.bool("IsAvailableMobile", bool_opt(defn.get("isAvailableMobile"), False))
    w.bool("IsCaseStatusNotificationEnabled", False)
    w.bool("IsHelpTextInGeneratedServicePdfEnabled", False)
    w.bool("EditorCanUpdateQuestionAlternatives", True)
    w.nil("PermissionByQuestionAlternative", "p2")
    w.bool("UseDefaultContent", False)
    w.bool("InvisibleToUser", bool_opt(defn.get("invisibleToUser"), False))
    w.bool("IsUsedByMultipleCustomers", False)
    w.bool("IsHelixService", False)
    w.int("Id", ids["serviceEntityId"])
    w.bool("IsDeleted", False)
    w.open("ServiceTags")
    w.nil("Package", "p3")
    w.nil("PackageClass", "p3")
    w.nil("ClassVersion", "p3")
    w.close("ServiceTags")
    w.raw(
        "Properties",
        json.dumps(defn.get("properties") if defn.get("properties") is not None else [], ensure_ascii=False),
    )
    w.raw(
        "SlotSettings",
        json.dumps(defn.get("slotSettings") or DEFAULT_SLOT_SETTINGS, ensure_ascii=False),
    )
    w.bool("RequireEID", bool_opt(defn.get("requireEID"), True))
    w.open("Organisation")
    w.text(
        "OrganisationName",
        defn.get("organisationName") or "Organisation",
    )
    w.int("Id", int(defn.get("organisationId") or ids["organisationId"]))
    w.bool("IsDeleted", False)
    w.close("Organisation")

    w.open("Pages")
    for page in pages:
        write_page(w, defn, page, short)
    w.close("Pages")

    w.empty("PdfTemplate")
    w.empty("Diary")
    w.empty("ServiceEmails")
    w.empty("EmailMessages")
    w.empty("ServiceRequestEmails")
    w.empty("LinkedRegisters")
    w.empty("Chapters")
    w.text("ServiceDisplayName", display)
    w.maybe_text("Description", defn.get("description"), prefix="p2")
    w.maybe_text("HowItWorksInformation", defn.get("howItWorksInformation"), prefix="p2")
    w.maybe_text("MyCasesInformation", defn.get("myCasesInformation"), prefix="p2")
    w.maybe_text("ProcessingTime", defn.get("processingTime"), prefix="p2")
    w.bool("IsDefault", False)
    w.int("Id", ids["serviceContentId"])
    w.bool("IsDeleted", False)
    w.open("DirektFeedbackSettings")
    w.nil("CasePublishedSurveyName", "p3")
    w.nil("CaseCancelledSurveyName", "p3")
    w.close("DirektFeedbackSettings")
    w.nil("ProecessingTime", "p2")  # exported spelling
    w.raw(
        "ExtendedData",
        json.dumps(
            {
                "AttachmentSettings": json.dumps(
                    {"MaxTotalSize": 0, "MaxTotalSizeErrorMessage": None},
                    separators=(",", ":"),
                )
            },
            ensure_ascii=False,
        ),
    )
    w.close("Service")
    return w.dump()


def write_page(w: XmlWriter, defn: dict[str, Any], page: dict[str, Any], short: str) -> None:
    url = page["_url"]
    block = is_block_page(page)
    w.open("Page")
    w.int("PageOrder", page["_order"])
    w.text("PageName", page["name"])
    w.text("PageType", page.get("pageType") or "Common")
    w.text("PageURL", url)
    w.nil("ClientLogic", "p4")
    w.bool("ShowInSummary", bool_opt(page.get("showInSummary"), block and bool(page.get("fields"))))
    w.bool("GeneratedServicePdfPageBreak", False)
    w.bool("IsEnabled", bool_opt(page.get("isEnabled"), True))
    w.text("ServiceShortName", short)
    w.bool("IsBlockPage", block)
    w.bool("UseDefaultContent", False)
    w.bool("IsServicePage", True)
    w.int("Id", page["_entityId"])
    w.bool("IsDeleted", False)
    w.text("DisplayName", page.get("displayName") or page["name"])
    header = page.get("headerHtml")
    if header:
        w.text("PageHeaderHTML", header)
    else:
        w.nil("PageHeaderHTML", "p4")
    w.maybe_text("PageInfoBoxTitle", page.get("infoBoxTitle"), prefix="p4")
    w.maybe_text("PageInfoBoxHTML", page.get("infoBoxHtml"), prefix="p4")
    w.bool("IsDefault", True)
    w.bool("ShowInMenu", bool_opt(page.get("showInMenu"), False))
    w.int("MenuOrder", int(page.get("menuOrder") or 0))
    w.bool("UseExternalLink", False)
    w.nil("ExternalLink", "p4")
    w.int("Id", page["_contentId"])
    w.bool("IsDeleted", False)

    if page.get("pageNodeXml"):
        w.open("PageNode")
        w.text("Xml", page["pageNodeXml"])
        w.int("Id", page["_pageNodeId"])
        w.bool("IsDeleted", False)
        w.close("PageNode")

    fields = page.get("fields") or []
    if fields:
        layout = page.get("layoutAreas") or default_layout(
            fields, short, page["_blockId"]
        )
        w.raw("LayoutAreas", layout)
        w.open("Fields")
        for field in fields:
            write_field(w, short, page, field)
        w.close("Fields")
    else:
        w.empty("Fields")
    w.raw("Properties", "[]")
    w.raw("ActivationRule", json.dumps(page.get("activationRule") or DEFAULT_ACTIVATION, ensure_ascii=False))
    w.close("Page")


def write_field(w: XmlWriter, short: str, page: dict[str, Any], field: dict[str, Any]) -> None:
    ftype = str(field["type"])
    fid = friendly_id(short, field["id"])
    alts = [str(a) for a in (field.get("alternatives") or [])]
    has_alts = bool(alts)
    alt_mode = (
        field.get("typeOfFieldAlternative")
        or (
            "AlternativesWithValues"
            if has_alts or ftype in CHOICE_FIELD_TYPES or ftype == "FileUploadField2"
            else "None"
        )
    )

    w.open("Field")
    w.int("PageID", page["_entityId"])
    w.text("FriendlyFieldID", fid)
    w.int("FieldOrder", field["_order"])
    w.nil("InheritsGF", "p6")
    w.text("TypeOfField", ftype)
    w.maybe_text("Question", field.get("question"), prefix="p6")
    w.maybe_text("MouseOverText", field.get("mouseOverText") or field.get("question"), prefix="p6")
    rows = field.get("textFieldNrOfRows")
    if rows is None:
        w.nil("TextFieldNrOfRows", "p6")
    else:
        w.int("TextFieldNrOfRows", int(rows))
    w.nil("ValidatorName", "p6")
    w.nil("ValidatorArgument", "p6")
    w.bool("IsRequired", bool_opt(field.get("required"), False))
    w.maybe_text("RequiredValidationText", field.get("requiredValidationText"), prefix="p6")
    w.bool("IsImportant", bool_opt(field.get("important"), False))
    w.bool("IncludeEmptyAnswer", False)
    w.nil("MinLength", "p6")
    w.nil("MaxLength", "p6")
    w.maybe_text("SummaryQuestion", field.get("summaryQuestion") or field.get("question"), prefix="p6")
    w.raw("ServiceCategory", field.get("serviceCategory") or "Unknown")
    w.text("ServiceShortName", short)
    w.text("PageName", page["name"])
    w.bool("GeneratedServicePdfPageBreak", False)
    w.bool("UseDefaultContent", False)
    w.bool("IsGFField", False)
    w.raw("TypeOfFieldAlternative", alt_mode)
    w.raw("DisplayType", field.get("displayType") or "None")
    w.nil("FieldScript", "p6")
    w.int("Id", field["_entityId"])
    w.bool("IsDeleted", False)

    args = list(field.get("arguments") or [])
    if args:
        w.open("Arguments")
        for arg in args:
            w.open("FieldCreateArgument")
            w.text("Name", arg["name"])
            w.text("Value", str(arg.get("value", "")))
            w.raw("Type", arg.get("type") or "Standard")
            w.int("Id", arg["_id"])
            w.bool("IsDeleted", False)
            w.close("FieldCreateArgument")
        w.close("Arguments")

    w.maybe_text("PreFieldHtml", field.get("preFieldHtml"), prefix="p6")
    w.maybe_text("PostFieldHtml", field.get("postFieldHtml"), prefix="p6")
    w.maybe_text("InfoButtonText", field.get("infoButtonText"), prefix="p6")
    w.bool("IsDefault", True)
    w.nil("AutoCompleteProviderName", "p6")
    w.maybe_text("UsedRegisterSystemName", field.get("usedRegisterSystemName"), prefix="p6")
    if has_alts:
        compat = json.dumps(
            [{"Name": a, "HelpText": None, "Order": 0} for a in alts],
            ensure_ascii=False,
            separators=(",", ":"),
        )
        w.text("QuestionAlternativesCompability", compat)
    else:
        w.nil("QuestionAlternativesCompability", "p6")
    w.int("Id", field["_contentId"])
    w.bool("IsDeleted", False)
    w.text("QuestionAlternatives", join_alternatives(alts), use_cdata=True)
    if has_alts:
        w.open("QuestionAlternativeModels")
        for i, alt in enumerate(alts):
            w.open("QuestionAlternativeModel")
            w.text("Name", alt)
            w.nil("HelpText", "p8")
            w.int("Order", i)
            w.close("QuestionAlternativeModel")
        w.close("QuestionAlternativeModels")
    else:
        w.empty("QuestionAlternativeModels")

    validators = field.get("validators")
    required_when = field.get("requiredWhen")
    if required_when and not validators:
        specs = required_when if isinstance(required_when, list) else [required_when]
        validators = [dependency_validator(short, field, spec) for spec in specs]
    if validators:
        w.raw("Validators", json.dumps(validators, ensure_ascii=False))

    w.raw(
        "ActivationRule",
        json.dumps(field.get("activationRule") or DEFAULT_ACTIVATION, ensure_ascii=False),
    )
    w.raw("Properties", "[]")
    w.close("Field")


def write_content(defn: dict[str, Any], ids: dict[str, Any]) -> str:
    w = XmlWriter()
    short = defn["shortName"]
    display = defn.get("displayName") or defn.get("menuDisplayName")
    w.open("Content")
    w.open("ServiceContents")
    w.open('ServiceContent CustomerName=""')
    w.nil("Service", "p4")
    w.text("ServiceShortName", short)
    w.text("ServiceDisplayName", display)
    w.maybe_text("Description", defn.get("description"), prefix="p4")
    w.maybe_text("HowItWorksInformation", defn.get("howItWorksInformation"), prefix="p4")
    w.maybe_text("MyCasesInformation", defn.get("myCasesInformation"), prefix="p4")
    w.maybe_text("ProcessingTime", defn.get("processingTime"), prefix="p4")
    w.bool("IsDefault", True)
    w.int("Id", ids["serviceContentId"])
    w.bool("IsDeleted", False)
    w.open("DirektFeedbackSettings")
    w.nil("CasePublishedSurveyName", "p5")
    w.nil("CaseCancelledSurveyName", "p5")
    w.close("DirektFeedbackSettings")
    w.close("ServiceContent")
    w.close("ServiceContents")

    w.open("PageContents")
    for page in ids["pages"]:
        w.open('PageContent CustomerName=""')
        w.text("ServiceShortName", short)
        w.text("PageName", page["name"])
        w.text("DisplayName", page.get("displayName") or page["name"])
        header = page.get("headerHtml")
        if header:
            w.text("PageHeaderHTML", header)
        else:
            w.nil("PageHeaderHTML", "p4")
        w.maybe_text("PageInfoBoxTitle", page.get("infoBoxTitle"), prefix="p4")
        w.maybe_text("PageInfoBoxHTML", page.get("infoBoxHtml"), prefix="p4")
        w.bool("IsDefault", True)
        w.bool("ShowInMenu", bool_opt(page.get("showInMenu"), False))
        w.int("MenuOrder", int(page.get("menuOrder") or 0))
        w.bool("UseExternalLink", False)
        w.nil("ExternalLink", "p4")
        w.int("Id", page["_contentId"])
        w.bool("IsDeleted", False)
        w.close("PageContent")
    w.close("PageContents")

    w.open("FieldContents")
    for page in ids["pages"]:
        for field in page.get("fields") or []:
            alts = [str(a) for a in (field.get("alternatives") or [])]
            w.open('FieldContent CustomerName=""')
            w.maybe_text("PreFieldHtml", field.get("preFieldHtml"), prefix="p4")
            w.maybe_text("PostFieldHtml", field.get("postFieldHtml"), prefix="p4")
            w.maybe_text("InfoButtonText", field.get("infoButtonText"), prefix="p4")
            w.bool("IsDefault", True)
            w.nil("AutoCompleteProviderName", "p4")
            w.text("ServiceShortName", short)
            w.text("PageName", page["name"])
            w.text("FriendlyFieldId", friendly_id(short, field["id"]))
            w.maybe_text("UsedRegisterSystemName", field.get("usedRegisterSystemName"), prefix="p4")
            if alts:
                compat = json.dumps(
                    [{"Name": a, "HelpText": None, "Order": 0} for a in alts],
                    ensure_ascii=False,
                    separators=(",", ":"),
                )
                w.text("QuestionAlternativesCompability", compat)
            else:
                w.text("QuestionAlternativesCompability", "[]")
            w.int("Id", field["_contentId"])
            w.bool("IsDeleted", False)
            w.text("QuestionAlternatives", join_alternatives(alts))
            if alts:
                w.open("QuestionAlternativeModels")
                for i, alt in enumerate(alts):
                    w.open("QuestionAlternativeModel")
                    w.text("Name", alt)
                    w.nil("HelpText", "p6")
                    w.int("Order", i)
                    w.close("QuestionAlternativeModel")
                w.close("QuestionAlternativeModels")
            else:
                w.empty("QuestionAlternativeModels")
            w.close("FieldContent")
    w.close("FieldContents")

    w.empty("PDFTemplates")
    w.empty("ServiceEmails")
    w.empty("ServiceRequestEmails")
    w.empty("FaqEntries")
    w.empty("FaqEntryToServices")
    w.empty("FaqEntryToPages")
    w.close("Content")
    return w.dump()


def assign_ids(defn: dict[str, Any]) -> dict[str, Any]:
    pool = IdPool(int(defn.get("idStart") or 1000))
    pages = ensure_system_pages(defn)
    out_pages = []
    for order, page in enumerate(pages):
        p = dict(page)
        p["_order"] = order
        p["_url"] = page_url(p)
        p["_entityId"] = pool.next()
        p["_contentId"] = pool.next()
        p["_pageNodeId"] = pool.next() if p.get("pageNodeXml") else None
        p["_blockId"] = f"BLOCK{order + 1}"
        fields_out = []
        for fo, field in enumerate(p.get("fields") or []):
            f = dict(field)
            f["_order"] = fo
            f["_entityId"] = pool.next()
            f["_contentId"] = pool.next()
            args = build_field_arguments(f)
            for arg in args:
                arg["_id"] = pool.next()
            f["arguments"] = args
            fields_out.append(f)
        p["fields"] = fields_out
        out_pages.append(p)
    return {
        "serviceEntityId": pool.next(),
        "serviceContentId": pool.next(),
        "serviceNr": int(defn.get("serviceNr") or pool.next()),
        "organisationId": int(defn.get("organisationId") or pool.next()),
        "pages": out_pages,
    }


def write_zip(service_xml: str, content_xml: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # Abou imports a folder named Service with extensionless XML files.
        zf.writestr("Service/Service", service_xml.encode("utf-8"))
        zf.writestr("Service/Content", content_xml.encode("utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Package an Abou e-tjänst zip")
    parser.add_argument("definition", type=Path, help="JSON service definition")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output zip path (default: {kortnamn}-{ServiceNr}-{YYYY-MM-DD}-export.zip)",
    )
    parser.add_argument(
        "--date",
        help="Export date YYYY-MM-DD used in the zip name and LastUpdated (default: today UTC)",
    )
    parser.add_argument(
        "--stdout-dir",
        type=Path,
        help="Also write Service/ and Content files to this directory",
    )
    args = parser.parse_args(argv)

    defn = load_definition(args.definition)
    errors = validate_definition(defn)
    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 1

    export_dt = parse_export_date(args.date or defn.get("exportDate"))
    ids = assign_ids(defn)
    service_xml = write_service(defn, ids, export_dt=export_dt)
    content_xml = write_content(defn, ids)

    short = defn["shortName"]
    default_name = export_zip_filename(short, ids["serviceNr"], export_dt.date())
    output = args.output or Path(default_name)
    write_zip(service_xml, content_xml, output)
    print(f"Wrote {output}")

    if args.stdout_dir:
        root = args.stdout_dir / "Service"
        root.mkdir(parents=True, exist_ok=True)
        (root / "Service").write_text(service_xml, encoding="utf-8")
        (root / "Content").write_text(content_xml, encoding="utf-8")
        print(f"Wrote {root / 'Service'} and {root / 'Content'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
