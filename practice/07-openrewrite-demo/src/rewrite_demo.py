"""Minimal deterministic rewrite demo inspired by OpenRewrite."""

from pathlib import Path
import re


FIELD_PATTERN = re.compile(
    r"(?P<indent>\s*)@Autowired\s*\n"
    r"(?P=indent)private\s+(?P<type>\w+)\s+(?P<name>\w+);\n",
    re.MULTILINE,
)


def rewrite_field_injection_to_constructor(source):
    match = FIELD_PATTERN.search(source)
    if not match:
        return source

    indent = match.group("indent")
    dependency_type = match.group("type")
    dependency_name = match.group("name")

    field_block = (
        f"{indent}private final {dependency_type} {dependency_name};\n\n"
        f"{indent}public LegacyOrderService({dependency_type} {dependency_name}) {{\n"
        f"{indent}    this.{dependency_name} = {dependency_name};\n"
        f"{indent}}}\n"
    )

    rewritten = FIELD_PATTERN.sub(field_block, source, count=1)
    rewritten = rewritten.replace(
        "import org.springframework.beans.factory.annotation.Autowired;\n", ""
    )
    return rewritten


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def rewrite_file(path):
    original = read_text(path)
    return rewrite_field_injection_to_constructor(original)
