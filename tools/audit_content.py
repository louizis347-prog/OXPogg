#!/usr/bin/env python3
"""Audita o catálogo Pogglot sem alterar os arquivos de conteúdo.

Uso:
  python3 tools/audit_content.py                 # resumo de todos os cursos
  python3 tools/audit_content.py --course nbde-b1
  python3 tools/audit_content.py --json > audit.json
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def episodes(course: str, files: list[str]):
    for name in files:
        path = DATA / name
        if not path.exists():
            yield {"_file": name, "_missing_file": True}
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # pragma: no cover
            yield {"_file": name, "_parse_error": str(exc)}
            continue
        for episode in payload if isinstance(payload, list) else payload.get("episodes", []):
            episode["_file"] = name
            yield episode


def audit(course: str, files: list[str]) -> dict:
    eps = list(episodes(course, files))
    titles = collections.defaultdict(list)
    ids = collections.defaultdict(list)
    missing_frames, placeholders, bad_translations, malformed = [], [], [], []
    for i, ep in enumerate(eps):
        title = str(ep.get("t", "")).strip()
        if title:
            titles[title].append(ep.get("en", i + 1))
        if ep.get("n") is not None:
            ids[str(ep["n"])].append(ep.get("en", i + 1))
        if ep.get("_missing_file") or ep.get("_parse_error"):
            malformed.append(ep.get("_file", f"index:{i}"))
        if not isinstance(ep.get("fr"), list) or not ep.get("fr"):
            missing_frames.append(ep.get("en", i + 1))
        if ep.get("pl") or "em produção" in title.lower() or "coming soon" in title.lower():
            placeholders.append(ep.get("en", i + 1))
        for frame in ep.get("fr") or []:
            if not isinstance(frame, dict):
                continue
            for key in ("lines", "items", "S", "E"):
                value = frame.get(key)
                if isinstance(value, list):
                    for row in value:
                        if isinstance(row, (list, tuple)) and len(row) >= 2 and any(str(x).strip() == "" for x in row[:2]):
                            bad_translations.append(ep.get("en", i + 1))
                            break
    duplicate_titles = {k: v for k, v in titles.items() if len(v) > 1}
    duplicate_ids = {k: v for k, v in ids.items() if len(v) > 1}
    return {
        "course": course,
        "episodes": len(eps),
        "duplicate_titles": {k: v for k, v in list(duplicate_titles.items())[:100]},
        "duplicate_title_count": len(duplicate_titles),
        "duplicate_ids_within_course": duplicate_ids,
        "missing_frames": missing_frames[:100],
        "missing_frames_count": len(missing_frames),
        "placeholders": placeholders[:100],
        "placeholders_count": len(placeholders),
        "bad_translations": sorted(set(bad_translations))[:100],
        "bad_translations_count": len(set(bad_translations)),
        "malformed_files": sorted(set(malformed)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", help="audita somente um curso")
    parser.add_argument("--json", action="store_true", help="imprime JSON completo")
    args = parser.parse_args()
    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    courses = [args.course] if args.course else list(manifest)
    report = {cid: audit(cid, manifest.get(cid, [])) for cid in courses if cid in manifest}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    print("curso       eps  títulos repetidos  quadros ausentes  placeholders  traduções suspeitas")
    for cid, item in report.items():
        print(f"{cid:10} {item['episodes']:5} {item['duplicate_title_count']:17} {item['missing_frames_count']:17} {item['placeholders_count']:13} {item['bad_translations_count']:21}")


if __name__ == "__main__":
    main()
