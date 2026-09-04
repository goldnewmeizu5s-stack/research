import re, glob, json, collections, os
FILES=sorted(glob.glob('wave1/*.md'))
claims=[]
for path in FILES:
    pre=os.path.basename(path).split('_')[0]
    for l in open(path).read().split('\n'):
        m=re.match(r'^\|\s*('+pre+r'-\d+)\s*\|', l)
        if not m: continue
        c=[x.strip() for x in l.strip('|').split('|')]
        if len(c)<9: continue
        c=(c+['']*14)[:14]
        claims.append(dict(file=os.path.basename(path), id=c[0], claim=c[1], value=c[2], unit=c[3], year=c[4], metric=c[5], country=c[6], source=c[7], url=c[8], tier=c[9], date=c[10], frag=c[11], conf=c[12], notes=c[13]))
print('claims total:', len(claims))
# normalize urls -> registry
def norm(u):
    u=u.strip()
    u=re.sub(r'^\[|\]$','',u)
    m=re.search(r'(https?://[^\s\)\|,;]+)', u)
    if m: return m.group(1).rstrip('.,;')
    m=re.search(r'(pmcid:PMC\d+|pmid:\d+)', u)
    if m: return m.group(1)
    return u
reg=collections.OrderedDict()
for c in claims:
    u=norm(c['url'])
    if not u or u in ('-','—',''): u='(без URL)'
    reg.setdefault(u, dict(ids=[], names=set(), tiers=set()))
    reg[u]['ids'].append(c['id']); reg[u]['names'].add(c['source'][:90]); reg[u]['tiers'].add(c['tier'])
print('unique urls:', len(reg))
os.makedirs('wave4', exist_ok=True)
with open('wave4/claims_all.tsv','w') as f:
    f.write('\t'.join(['file','id','claim','value','unit','year','metric','country','source','url','tier','date','frag','conf','notes'])+'\n')
    for c in claims:
        f.write('\t'.join(str(c[k]).replace('\t',' ') for k in ['file','id','claim','value','unit','year','metric','country','source','url','tier','date','frag','conf','notes'])+'\n')
with open('wave4/sources_registry.tsv','w') as f:
    f.write('S#\turl\tsource_names\ttiers\tn_claims\tclaim_ids\n')
    for i,(u,d) in enumerate(reg.items(), 1):
        f.write(f"S{i}\t{u}\t{' ; '.join(sorted(d['names'])[:3])}\t{','.join(sorted(t for t in d['tiers'] if t))}\t{len(d['ids'])}\t{','.join(d['ids'][:25])}\n")
# stats
byfile=collections.Counter(c['file'] for c in claims)
byconf=collections.Counter(c['conf'].split()[0].upper() if c['conf'] else 'NA' for c in claims)
bytier=collections.Counter(c['tier'] for c in claims)
print('by file:', dict(byfile))
print('by confidence:', dict(byconf))
print('by tier:', dict(sorted(bytier.items(), key=lambda x:-x[1])[:8]))
