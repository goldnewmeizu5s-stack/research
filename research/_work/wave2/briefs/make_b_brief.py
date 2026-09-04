import sys, re, json
# usage: make_b_brief.py <wave1 file> <prefix e.g. B5> <group_name> <candidate ids comma> <claim ids comma (ranges ok: 1-10,76)>
path, prefix, group, cands, claims = sys.argv[1:6]
t=open(path).read().split('\n')
cand_ids=[c.strip() for c in cands.split(',') if c.strip()]
def expand(s):
    out=[]
    for p in s.split(','):
        p=p.strip()
        if not p: continue
        if '-' in p:
            a,b=p.split('-'); out+=list(range(int(a),int(b)+1))
        else: out.append(int(p))
    return out
claim_nums=set(expand(claims))
# summary table rows: lines starting with "| C" or "| #"? find rows whose first cell is in cand_ids
cand_rows=[]; header=None
for l in t:
    if l.startswith('|'):
        c=[x.strip() for x in l.strip('|').split('|')]
        if c and c[0] in ('#','№','id') and header is None and 'Страна' in l: header=c
        if c and c[0] in cand_ids: cand_rows.append(c)
claim_rows=[]
for l in t:
    m=re.match(r'\| '+prefix+r'-(\d+) ', l)
    if m and int(m.group(1)) in claim_nums:
        c=[x.strip() for x in l.strip('|').split('|')]
        claim_rows.append(c)
out=[f"# Бриф верификатора: {prefix} - {group}", "", "Ниже - ТОЛЬКО утверждения сборщика и URL, без его аргументов и оценок. Дата доступа сборщика: 2026-09-04.", "", "## Кандидаты (описание меры, как её сформулировал сборщик - каждое поле подлежит проверке)", ""]
if header:
    # drop assessment/confidence-like columns
    keep=[i for i,h in enumerate(header) if not re.search('Оценк|Уверен|аномальн', h)]
    out.append('| '+' | '.join(header[i] for i in keep)+' |'); out.append('|'+'---|'*len(keep))
    for c in cand_rows:
        out.append('| '+' | '.join(c[i] if i<len(c) else '' for i in keep)+' |')
else:
    for c in cand_rows: out.append('| '+' | '.join(c[:9])+' |')
out+=["", "## Утверждения (claims)", "", "| id | утверждение | значение | единица | год/период | определение метрики | страна | название источника | URL |", "|---|---|---|---|---|---|---|---|---|"]
for c in claim_rows:
    c=(c+['']*14)[:14]
    out.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]} | {c[6]} | {c[7]} | {c[8]} |")
fn=f"wave2/briefs/{prefix}_{group}.md"
open(fn,'w').write('\n'.join(out)+'\n')
print(fn, 'candidates', len(cand_rows), 'claims', len(claim_rows))
