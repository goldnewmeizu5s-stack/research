#!/usr/bin/env python3
"""Reproducible count of independent-verification verdicts.

Scans every markdown file under _work/wave2/ and counts table CELLS whose value
is exactly a verdict token (optionally followed by a qualifier). Prose mentions
of the words are therefore not counted. Run:  python3 count_verdicts.py
"""
import glob, re, collections, os

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'wave2')
V = ('CONFIRMED', 'PARTIALLY', 'NOT FOUND', 'CONTRADICTED')

total = collections.Counter()
rows = []
for p in sorted(glob.glob(os.path.join(BASE, '**', '*.md'), recursive=True)):
    n = collections.Counter()
    for line in open(p, encoding='utf-8', errors='ignore'):
        s = line.strip()
        if not s.startswith('|'):
            continue
        for cell in (x.strip().strip('*').strip() for x in s.strip('|').split('|')):
            cu = cell.upper()
            for v in V:
                if re.match(re.escape(v) + r'\b', cu):
                    n[v] += 1
                    break
            else:
                continue
            break
    if sum(n.values()):
        rows.append((os.path.basename(p), n))
        total += n

for name, n in rows:
    print(f'{name:45s} {sum(n.values()):4d}  ' +
          '  '.join(f'{v}={n[v]}' for v in V))
print('-' * 90)
print(f'files with verdicts: {len(rows)}')
for v in V:
    print(f'{v:14s} {total[v]}')
print(f'{"TOTAL":14s} {sum(total.values())}')
