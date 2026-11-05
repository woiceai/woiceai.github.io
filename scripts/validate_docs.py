#!/usr/bin/env python3
"""Validate portable documentation links, JSON examples and obvious secret patterns."""
from pathlib import Path
import re, json, sys
root = Path(__file__).resolve().parents[1]
errors = []
links = 0
for p in root.rglob('*.md'):
    text = p.read_text()
    if sum(1 for line in text.splitlines() if line.startswith('```')) % 2:
        errors.append(f'{p.relative_to(root)}: unclosed code fence')
    for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)', text):
        if target.startswith(('https://', 'http://', '#', 'mailto:')): continue
        target = target.split('#')[0]
        if not target: continue
        links += 1
        if not (p.parent / target).exists():
            errors.append(f'{p.relative_to(root)}: missing {target}')
for p in (root / 'examples').glob('*.json'):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f'{p.name}: {e}')
for p in root.rglob('*'):
    if not p.is_file() or p == Path(__file__).resolve(): continue
    text = p.read_text(errors='replace')
    for pattern in (r'AKIA[A-Z0-9]{16}', r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----', r'hf_[A-Za-z0-9]{25,}', r'ghp_[A-Za-z0-9]{30,}'):
        if re.search(pattern, text): errors.append(f'{p.relative_to(root)}: possible secret')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {links} local links, JSON payloads, balanced fences, basic secret-pattern scan')
