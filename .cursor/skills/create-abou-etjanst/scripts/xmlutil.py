"""Minimal XML writer that matches Abou DataContractSerializer exports."""

from __future__ import annotations

from html import escape
from typing import Iterable


XSI = "http://www.w3.org/2001/XMLSchema-instance"


def cdata(value: str | None) -> str:
    text = "" if value is None else str(value)
    # Split nested "]]>" so the CDATA remains well-formed.
    return "<![CDATA[" + text.replace("]]>", "]]]]><![CDATA[>") + "]]>"


class XmlWriter:
    def __init__(self) -> None:
        self._parts: list[str] = ['<?xml version="1.0" encoding="utf-8"?>']
        self._indent = 0

    def dump(self) -> str:
        return "\n".join(self._parts) + "\n"

    def _pad(self) -> str:
        return "  " * self._indent

    def open(self, tag: str, attrs: str = "") -> None:
        self._parts.append(f"{self._pad()}<{tag}{attrs}>")
        self._indent += 1

    def close(self, tag: str) -> None:
        self._indent -= 1
        self._parts.append(f"{self._pad()}</{tag}>")

    def empty(self, tag: str, attrs: str = "") -> None:
        self._parts.append(f"{self._pad()}<{tag}{attrs} />")

    def raw(self, tag: str, inner: str) -> None:
        self._parts.append(f"{self._pad()}<{tag}>{inner}</{tag}>")

    def text(self, tag: str, value: str | None, *, use_cdata: bool = True) -> None:
        if value is None:
            self.empty(tag)
            return
        inner = cdata(value) if use_cdata else escape(str(value), quote=False)
        self.raw(tag, inner)

    def bool(self, tag: str, value: bool) -> None:
        self.raw(tag, "true" if value else "false")

    def int(self, tag: str, value: int) -> None:
        self.raw(tag, str(int(value)))

    def nil(self, tag: str, prefix: str) -> None:
        self.empty(
            tag,
            f' {prefix}:nil="true" xmlns:{prefix}="{XSI}"',
        )

    def maybe_text(
        self,
        tag: str,
        value: str | None,
        *,
        prefix: str,
        use_cdata: bool = True,
        empty_as_cdata: bool = False,
    ) -> None:
        if value is None:
            self.nil(tag, prefix)
        elif value == "" and not empty_as_cdata:
            self.nil(tag, prefix)
        else:
            self.text(tag, value, use_cdata=use_cdata)

    def comment(self, text: str) -> None:
        self._parts.append(f"{self._pad()}<!-- {text} -->")


def join_alternatives(items: Iterable[str] | None) -> str:
    if not items:
        return ""
    return ";".join(items)
