import pandas as pd, re, pymupdf, hashlib
pdfs={'2025':'data/World_Obesity_Atlas_2025_rev1.pdf','2023':'data/World_Obesity_Atlas_2023_Report.pdf','2022':'data/World_Obesity_Atlas_2022.pdf'}
docs={k:pymupdf.open(v) for k,v in pdfs.items()}
sel=pd.read_csv('data/a1_projections_selected.csv')
out=['\n## 4. World Obesity Atlas: прямая проверка прогнозных значений по локально скачанным PDF (бакет s3-eu-west-1.amazonaws.com/wof-files/)\n',
'Канал: файлы скачаны curl в этой сессии, текст извлечён pymupdf. Это единственный канал, где страновые страницы Атласов читаются (Firecrawl их не индексирует, поэтому верификаторы wave2 помечали эти утверждения NOT FOUND).\n']
for k,v in pdfs.items(): out.append(f'- Atlas {k}: `{v}`, sha256 `{hashlib.sha256(open(v,"rb").read()).hexdigest()}`, страниц {len(docs[k])}')
out.append('\n| Страна | заявлено A1 | Atlas 2025 стр. | найдено в PDF | Atlas 2023 стр. | найдено в PDF | Atlas 2022 стр. | найдено в PDF | вердикт |\n|---|---|---|---|---|---|---|---|---|')
def page_text(doc,p):
    try: return doc[int(p)-1].get_text().replace('\n',' | ')
    except Exception: return ''
ok=0; bad=0
for _,r in sel.iterrows():
    name=str(r.country_atlas) if pd.notna(r.country_atlas) else r.Entity
    res={}; verd=[]
    for ed,pcol,valcol,label in (('2025','page_atlas2025','atlas2025_adult_obesity_2025_pct','Adults living with obesity in 2025'),
                                 ('2023','page_atlas2023','atlas2023_adult_obesity_2035_pct','ADULTS WITH OBESITY 2035'),
                                 ('2022','page_atlas2022','atlas2022_adult_obesity_2030_pct','ADULTS WITH OBESITY BY 2030')):
        p=r.get(pcol); val=r.get(valcol)
        if pd.isna(p) or pd.isna(val): res[ed]='нет данных'; continue
        t=page_text(docs[ed],p)
        namefound=name.split('(')[0].strip() in t
        vs=f'{val:g}'
        # look for the value near the label
        pat=re.compile(re.escape(vs)+r'\s*%?')
        near=False
        idxs=[m.start() for m in pat.finditer(t)]
        li=t.find(label[:18])
        for i in idxs:
            if li>=0 and abs(i-li)<400: near=True
        res[ed]=f'стр.{int(p)}: страна {"есть" if namefound else "НЕТ"}; значение {vs}% {"найдено рядом с меткой" if near else ("найдено на странице" if idxs else "НЕ найдено")}'
        verd.append(namefound and bool(idxs))
    v='ПОДТВЕРЖДЕНО' if verd and all(verd) else ('ЧАСТИЧНО' if any(verd) else 'НЕ ПОДТВЕРЖДЕНО')
    if v=='ПОДТВЕРЖДЕНО': ok+=1
    else: bad+=1
    claim=f"2025: {r.get('atlas2025_adult_obesity_2025_pct')}%; 2035: {r.get('atlas2023_adult_obesity_2035_pct')}%; 2030: {r.get('atlas2022_adult_obesity_2030_pct')}%"
    out.append(f"| {r.Entity} | {claim} | {r.get('page_atlas2025')} | {res.get('2025','-')} | {r.get('page_atlas2023')} | {res.get('2023','-')} | {r.get('page_atlas2022')} | {res.get('2022','-')} | {v} |")
out.append(f'\nИтог прямой проверки Атласов: ПОДТВЕРЖДЕНО {ok}, не полностью {bad}.')
# also print an example raw page for transparency
ex=sel.iloc[0]
out.append('\nПример сырого текста страницы (Atlas 2025, страна '+str(ex.Entity)+f', стр. {int(ex.page_atlas2025)}), первые 700 символов:\n\n```\n'+page_text(docs["2025"],ex.page_atlas2025)[:700]+'\n```')
txt='\n'.join(out)
open('wave2/ORCH_data_recheck.md','a').write(txt+'\n')
print(txt[:4500])
