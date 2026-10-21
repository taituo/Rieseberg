#!/usr/bin/env python3
"""Check the repo's skill conventions. Exits non-zero on any problem.

Run from anywhere: python3 scripts/validate.py
The rules checked here are the ones written in AGENTS.md.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DOC_SECTIONS = ["## What it does", "## When to reach for it", "## Common questions", "## It's working if"]
EM_DASH = "—"

problems = []


def fail(path, msg):
    problems.append(f"{path.relative_to(ROOT) if isinstance(path, Path) else path}: {msg}")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(path, "missing frontmatter")
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        fail(path, "unterminated frontmatter")
        return {}, text
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, text[end + 5 :]


def simple_yaml(path):
    """Read the two-level openai.yaml files without a YAML dependency."""
    data, section = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        if not line.startswith(" "):
            section = line.rstrip(":").strip()
            data[section] = {}
        elif section:
            key, value = line.strip().split(":", 1)
            data[section][key.strip()] = value.strip().strip('"')
    return data


skill_dirs = sorted(p.parent for p in (ROOT / "skills").rglob("SKILL.md"))
plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
listed = {str((ROOT / s).resolve()) for s in plugin.get("skills", [])}
readme = (ROOT / "README.md").read_text(encoding="utf-8")

if not skill_dirs:
    fail("skills/", "no skills found")

for d in skill_dirs:
    skill_md = d / "SKILL.md"
    rel = d.relative_to(ROOT).as_posix()
    fields, body = frontmatter(skill_md)
    name = fields.get("name", "")
    desc = fields.get("description", "")

    if name != d.name:
        fail(skill_md, f"name '{name}' does not match folder '{d.name}'")
    if not NAME_RE.match(name) or len(name) > 64:
        fail(skill_md, "name must be kebab-case, at most 64 characters")
    if not desc:
        fail(skill_md, "missing description")
    if len(desc) > 1024:
        fail(skill_md, f"description is {len(desc)} characters, limit is 1024")
    if not body.strip():
        fail(skill_md, "empty body")

    user_invoked = fields.get("disable-model-invocation", "").lower() == "true"
    if not user_invoked and "Use when" not in desc:
        fail(skill_md, "model-invoked description needs trigger branches ('Use when ...')")

    yaml_path = d / "agents/openai.yaml"
    if not yaml_path.exists():
        fail(d, "missing agents/openai.yaml")
    else:
        y = simple_yaml(yaml_path)
        iface = y.get("interface", {})
        if not iface.get("display_name") or not iface.get("short_description"):
            fail(yaml_path, "needs interface.display_name and interface.short_description")
        implicit_off = y.get("policy", {}).get("allow_implicit_invocation", "").lower() == "false"
        if implicit_off != user_invoked:
            fail(yaml_path, "invocation out of sync with SKILL.md disable-model-invocation")

    if str(d.resolve()) not in listed:
        fail(".claude-plugin/plugin.json", f"skills array is missing ./{rel}")
    if f"./{rel}/SKILL.md" not in readme:
        fail("README.md", f"no link to ./{rel}/SKILL.md")
    bucket_readme = d.parent / "README.md"
    if not bucket_readme.exists():
        fail(d.parent, "bucket has no README.md")
    elif f"./{d.name}/SKILL.md" not in bucket_readme.read_text(encoding="utf-8"):
        fail(bucket_readme, f"no link to ./{d.name}/SKILL.md")

    doc = ROOT / "docs" / f"{d.name}.md"
    if not doc.exists():
        fail(doc, "missing docs page")
    else:
        doc_text = doc.read_text(encoding="utf-8")
        for section in DOC_SECTIONS:
            if section not in doc_text:
                fail(doc, f"missing section '{section}'")

for s in plugin.get("skills", []):
    if not (ROOT / s / "SKILL.md").exists():
        fail(".claude-plugin/plugin.json", f"lists {s}, which has no SKILL.md")

for md in ROOT.rglob("*.md"):
    if ".git" in md.parts:
        continue
    for n, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
        if EM_DASH in line:
            fail(md, f"line {n}: em-dash; rewrite the sentence")

if problems:
    print(f"{len(problems)} problem(s):")
    for p in problems:
        print(f"  - {p}")
    sys.exit(1)
print(f"OK: {len(skill_dirs)} skills checked")
