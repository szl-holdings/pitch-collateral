#!/usr/bin/env python3
"""Fail-closed integrity and doctrine checks for the investor diligence deck."""

from __future__ import annotations

import hashlib
import hmac
import posixpath
import re
import sys
import urllib.parse
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET


DECK_NAME = "SZL_Investor_Deck_2026-08-30.pptx"
SOURCE_SHA = "20cd4537effa28bacda8ef832e2a720b852c98d7"
SOURCE_PREFIX = (
    "https://github.com/szl-holdings/pitch-collateral/blob/"
    f"{SOURCE_SHA}/"
)
EXPECTED_SLIDES = 11
EXPECTED_SIZE_EMU = ("12192000", "6858000")
MAX_MEMBER_BYTES = 10 * 1024 * 1024
MAX_PACKAGE_BYTES = 50 * 1024 * 1024

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
RID = f"{{{NS['r']}}}id"
A_TEXT = f"{{{NS['a']}}}t"
A_BREAK = f"{{{NS['a']}}}br"

REQUIRED_VISIBLE_FRAGMENTS = (
    "Governed execution",
    "AI actions are difficult to approve without inspectable evidence",
    "SZL wraps the action with four governed-execution primitives",
    "DECLARED design target: an inspectable action chain",
    "Product and proof surfaces have separate authority",
    "Dated evidence snapshot with explicit limits",
    "MODELED first commercial motion: one buyer, one workflow, one bounded pilot",
    "MODELED market size and pricing hypotheses",
    "Diligence is structured, but institutional readiness is not yet complete",
    "ROADMAP for a focused seed extension",
    "Prototype, proof boundary,",
    "a-11-oy.com/verify",
    "a11oy.net/diligence/#investors",
    "a11oy.net/record/",
    "NOT FOR EXTERNAL CIRCULATION",
    "Unconditional Lambda uniqueness remains Conjecture 1",
    "DECLARED",
    "MODELED",
    "SIMULATED",
    "ROADMAP",
    "UNAVAILABLE",
)

ALLOWED_EVIDENCE_STATES = {
    "MEASURED",
    "REPORTED",
    "DECLARED",
    "SIMULATED",
    "SAMPLE",
    "MODELED",
    "ROADMAP",
    "UNKNOWN",
    "UNAVAILABLE",
    "BLOCKED",
}

PROHIBITED_STATUS_PATTERNS = (
    r"\bPARTIAL\b",
    r"\bREV-BOUNDED\b",
    r"\bNONE EVIDENCED\b",
    r"\bNOT YET PREPARED\b",
    r"\bVERIFIED\b",
)

PROHIBITED_VISIBLE_FRAGMENTS = (
    "holdings.a-11-oy.com/docs-site/",
    "counter-UAS route",
    "Series A-ready",
    "production-ready platform",
    "formally verified platform",
    "formally verified AI",
    "certified compliant",
    "DoD-approved",
    "paying customers",
    "customer traction",
)


class DeckCheckError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DeckCheckError(message)


def parse_xml(archive: zipfile.ZipFile, member: str) -> ET.Element:
    try:
        return ET.fromstring(archive.read(member))
    except KeyError as exc:
        raise DeckCheckError(f"missing package member: {member}") from exc
    except ET.ParseError as exc:
        raise DeckCheckError(f"invalid XML in {member}: {exc}") from exc


def relationship_map(archive: zipfile.ZipFile, rels_part: str) -> dict[str, dict[str, str]]:
    root = parse_xml(archive, rels_part)
    result: dict[str, dict[str, str]] = {}
    for rel in root.findall("rel:Relationship", NS):
        rel_id = rel.get("Id")
        require(bool(rel_id), f"relationship without Id in {rels_part}")
        require(rel_id not in result, f"duplicate relationship Id {rel_id} in {rels_part}")
        result[rel_id] = dict(rel.attrib)
    return result


def resolve_target(source_part: str, target: str) -> str:
    require(bool(target), f"empty relationship target from {source_part}")
    require("\\" not in target, f"backslash in relationship target: {target}")
    if target.startswith("/"):
        normalized = posixpath.normpath(target.lstrip("/"))
    else:
        normalized = posixpath.normpath(posixpath.join(posixpath.dirname(source_part), target))
    parts = PurePosixPath(normalized).parts
    require(normalized not in {"", "."}, f"empty normalized target from {source_part}")
    require(not normalized.startswith("../") and ".." not in parts, f"unsafe target: {target}")
    return normalized


def rels_part_for(part: str) -> str:
    return posixpath.join(posixpath.dirname(part), "_rels", f"{posixpath.basename(part)}.rels")


def paragraph_texts(root: ET.Element) -> list[str]:
    paragraphs: list[str] = []
    for paragraph in root.findall(".//a:p", NS):
        pieces: list[str] = []
        for node in paragraph.iter():
            if node.tag == A_TEXT:
                pieces.append(node.text or "")
            elif node.tag == A_BREAK:
                pieces.append("\n")
        text = "".join(pieces)
        paragraphs.extend(text.splitlines() or [text])
    return paragraphs


def element_text(root: ET.Element) -> str:
    return " ".join(" ".join(paragraph_texts(root)).split())


def validate_evidence_state_tables(slide_root: ET.Element, slide_part: str) -> int:
    validated_tables = 0
    for table in slide_root.findall(".//a:tbl", NS):
        rows = table.findall("a:tr", NS)
        if not rows:
            continue
        header_cells = rows[0].findall("a:tc", NS)
        headers = [element_text(cell).casefold() for cell in header_cells]
        state_columns = [
            index
            for index, header in enumerate(headers)
            if header in {"state", "current state"}
        ]
        if not state_columns:
            continue
        validated_tables += 1
        for state_column in state_columns:
            for row_number, row in enumerate(rows[1:], start=2):
                cells = row.findall("a:tc", NS)
                require(
                    state_column < len(cells),
                    f"{slide_part}: row {row_number} is missing an evidence-state cell",
                )
                state = element_text(cells[state_column])
                require(
                    state in ALLOWED_EVIDENCE_STATES,
                    f"{slide_part}: non-doctrinal evidence state: {state!r}",
                )
    return validated_tables


def notes_body_lines(notes_root: ET.Element, notes_part: str) -> list[str]:
    body_shapes: list[ET.Element] = []
    for shape in notes_root.findall(".//p:sp", NS):
        placeholder = shape.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if placeholder is not None and placeholder.get("type") == "body":
            body_shapes.append(shape)
    require(len(body_shapes) == 1, f"{notes_part}: expected one body placeholder")
    return [line.strip() for line in paragraph_texts(body_shapes[0]) if line.strip()]


def validate_source_lines(lines: list[str], notes_part: str, repository_root: Path) -> None:
    require(lines, f"{notes_part}: empty source notes")
    require(lines[0] == "[Sources]", f"{notes_part}: first line must be [Sources]")
    require(lines[-1] == "[/Sources]", f"{notes_part}: last line must be [/Sources]")
    sources = lines[1:-1]
    require(bool(sources), f"{notes_part}: source block is empty")
    for entry in sources:
        require(entry.startswith("- "), f"{notes_part}: malformed source entry: {entry}")
        url = entry[2:].strip()
        require(url.startswith(SOURCE_PREFIX), f"{notes_part}: source is not pinned to {SOURCE_SHA}: {url}")
        parsed = urllib.parse.urlsplit(url)
        require(not parsed.query and not parsed.fragment, f"{notes_part}: source URL must not have query/fragment")
        suffix = urllib.parse.unquote(url[len(SOURCE_PREFIX) :])
        relative = PurePosixPath(suffix)
        require(not relative.is_absolute() and ".." not in relative.parts, f"{notes_part}: unsafe source path")
        source_path = repository_root.joinpath(*relative.parts).resolve()
        try:
            source_path.relative_to(repository_root)
        except ValueError as exc:
            raise DeckCheckError(f"{notes_part}: source escapes repository: {suffix}") from exc
        require(source_path.is_file(), f"{notes_part}: cited source does not exist: {suffix}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest(manifest_path: Path) -> str:
    text = manifest_path.read_text(encoding="utf-8")
    match = re.fullmatch(rf"([0-9a-f]{{64}})  {re.escape(DECK_NAME)}\n?", text)
    require(match is not None, "MANIFEST.sha256 must contain exactly one lowercase sha256sum entry")
    return match.group(1)


def validate_archive(deck_path: Path, repository_root: Path) -> tuple[int, int]:
    with zipfile.ZipFile(deck_path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        require(len(names) == len(set(names)), "PPTX contains duplicate ZIP members")
        total_size = 0
        for info in infos:
            pure = PurePosixPath(info.filename)
            require(not pure.is_absolute() and ".." not in pure.parts, f"unsafe ZIP member: {info.filename}")
            require("\\" not in info.filename, f"backslash in ZIP member: {info.filename}")
            require(not (info.flag_bits & 0x1), f"encrypted ZIP member: {info.filename}")
            require(info.file_size <= MAX_MEMBER_BYTES, f"oversized ZIP member: {info.filename}")
            total_size += info.file_size
        require(total_size <= MAX_PACKAGE_BYTES, "PPTX uncompressed size exceeds safety ceiling")
        corrupt = archive.testzip()
        require(corrupt is None, f"corrupt ZIP member: {corrupt}")

        required = {"[Content_Types].xml", "ppt/presentation.xml", "ppt/_rels/presentation.xml.rels"}
        require(required.issubset(names), f"missing required package members: {sorted(required - set(names))}")
        lowered = [name.lower() for name in names]
        require(not any("vbaproject" in name or "/activex/" in name or "/embeddings/" in name for name in lowered), "active or embedded content is prohibited")

        for rels_name in (name for name in names if name.endswith(".rels")):
            rels_root = parse_xml(archive, rels_name)
            external = [rel for rel in rels_root.findall("rel:Relationship", NS) if rel.get("TargetMode") == "External"]
            require(not external, f"external package relationships are prohibited: {rels_name}")

        presentation_part = "ppt/presentation.xml"
        presentation = parse_xml(archive, presentation_part)
        size = presentation.find("p:sldSz", NS)
        require(size is not None, "presentation is missing p:sldSz")
        require((size.get("cx"), size.get("cy")) == EXPECTED_SIZE_EMU, "unexpected slide dimensions")

        presentation_rels = relationship_map(archive, "ppt/_rels/presentation.xml.rels")
        slide_ids = presentation.findall("p:sldIdLst/p:sldId", NS)
        require(len(slide_ids) == EXPECTED_SLIDES, f"expected {EXPECTED_SLIDES} slides, found {len(slide_ids)}")
        slide_parts: list[str] = []
        for slide_id in slide_ids:
            rel_id = slide_id.get(RID)
            require(bool(rel_id) and rel_id in presentation_rels, "slide has missing relationship")
            rel = presentation_rels[rel_id]
            require(rel.get("TargetMode") != "External", "external slide relationship is prohibited")
            require(rel.get("Type", "").endswith("/slide"), f"unexpected slide relationship type: {rel.get('Type')}")
            slide_part = resolve_target(presentation_part, rel.get("Target", ""))
            require(slide_part in names, f"missing slide part: {slide_part}")
            slide_parts.append(slide_part)
        require(len(slide_parts) == len(set(slide_parts)), "duplicate slide targets in presentation order")

        notes_parts: list[str] = []
        visible_paragraphs: list[str] = []
        evidence_state_tables = 0
        for slide_part in slide_parts:
            slide_root = parse_xml(archive, slide_part)
            visible_paragraphs.extend(paragraph_texts(slide_root))
            evidence_state_tables += validate_evidence_state_tables(slide_root, slide_part)
            slide_rels_part = rels_part_for(slide_part)
            require(slide_rels_part in names, f"missing slide relationships: {slide_rels_part}")
            slide_rels = relationship_map(archive, slide_rels_part)
            notes_rels = [rel for rel in slide_rels.values() if rel.get("Type", "").endswith("/notesSlide")]
            require(len(notes_rels) == 1, f"{slide_part}: expected exactly one notes relationship")
            notes_rel = notes_rels[0]
            require(notes_rel.get("TargetMode") != "External", f"{slide_part}: external notes relationship")
            notes_part = resolve_target(slide_part, notes_rel.get("Target", ""))
            require(notes_part in names, f"missing notes part: {notes_part}")
            notes_parts.append(notes_part)
            notes_root = parse_xml(archive, notes_part)
            validate_source_lines(notes_body_lines(notes_root, notes_part), notes_part, repository_root)

        require(len(notes_parts) == EXPECTED_SLIDES, "unexpected notes count")
        require(len(notes_parts) == len(set(notes_parts)), "duplicate notes targets")
        packaged_notes = {
            name
            for name in names
            if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)
        }
        require(packaged_notes == set(notes_parts), "orphan or unlinked notes parts detected")
        require(evidence_state_tables == 2, "expected two evidence-state tables")

        visible_text = "\n".join(visible_paragraphs)
        for fragment in REQUIRED_VISIBLE_FRAGMENTS:
            require(fragment in visible_text, f"required visible fragment missing: {fragment}")
        for pattern in PROHIBITED_STATUS_PATTERNS:
            require(
                re.search(pattern, visible_text, flags=re.IGNORECASE) is None,
                f"prohibited evidence status present: {pattern}",
            )
        lowered_visible = visible_text.lower()
        for fragment in PROHIBITED_VISIBLE_FRAGMENTS:
            require(fragment.lower() not in lowered_visible, f"prohibited visible fragment present: {fragment}")
        require("Khipu BFT safety is proven".lower() not in lowered_visible, "Khipu Conjecture 2 overclaim present")

        return len(slide_parts), len(notes_parts)


def main() -> int:
    deck_dir = Path(__file__).resolve().parent
    repository_root = deck_dir.parent.resolve()
    deck_path = deck_dir / DECK_NAME
    manifest_path = deck_dir / "MANIFEST.sha256"
    require(deck_path.is_file(), f"missing deck: {deck_path}")
    require(manifest_path.is_file(), f"missing manifest: {manifest_path}")
    expected_hash = read_manifest(manifest_path)
    actual_hash = sha256_file(deck_path)
    require(hmac.compare_digest(expected_hash, actual_hash), "deck SHA-256 does not match MANIFEST.sha256")
    slides, notes = validate_archive(deck_path, repository_root)
    print(
        f"OK deck/{DECK_NAME} sha256={actual_hash} slides={slides} notes={notes} "
        f"source_base={SOURCE_SHA}"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (DeckCheckError, OSError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
