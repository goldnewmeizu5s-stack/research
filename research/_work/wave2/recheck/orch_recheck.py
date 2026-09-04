"""Orchestrator independent re-check of A1/A2 rankings from freshly re-downloaded raw files.
Fresh files were downloaded 2026-09-04 via curl from raw.githubusercontent.com (see sha256 in the report)."""
import pandas as pd, hashlib, re, fitz, os, json
R='wave2/recheck/'; out=[]
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
out.append('# ORCH_data_recheck - независимая перепроверка расчётов A1/A2 оркестратором\n')
out.append('Дата: 2026-09-04. Метод: повторная загрузка исходных файлов curl с raw.githubusercontent.com (ветка master для WHO CSV и NCD-RisC CSV; закреплённый коммит 075cd0da5b7268daa466c84b3b2ff109bf3aea7e для population.csv), сравнение SHA-256 с зеркалами в mirrors/, независимый пересчёт рейтингов кодом (этот скрипт), сравнение с таблицами аналитиков.\n')
out.append('## 1. Целостность файлов (SHA-256)\n\n| файл | свежая загрузка | зеркало в mirrors/ | совпадает |\n|---|---|---|---|')
pairs=[('who_obesity_fresh.csv','mirrors/obesity/share-of-adults-defined-as-obese.csv'),('ncdrisc_dm_fresh.csv','mirrors/ncdrisc_tableau/NCD_RisC_Lancet_2016_DM_age_standardised_countries.csv'),('population_fresh_pinned.csv','mirrors/population/data/population.csv')]
for f,m in pairs:
    a,b=sha(R+f),sha(m); out.append(f'| {f} vs {m} | {a[:16]}... | {b[:16]}... | {"ДА" if a==b else "НЕТ"} |')
# --- Obesity
w=pd.read_csv(R+'who_obesity_fresh.csv'); w.columns=['Entity','Code','Year','val']
pv=w.pivot_table(index=['Entity','Code'],columns='Year',values='val').reset_index()
pv['abs']=(pv[2016]-pv[2006]).round(1); pv['rel']=((pv[2016]/pv[2006]-1)*100).round(1)
un=set(pd.read_csv('data/un_member_states.csv')['member_state'])
pop=pd.read_csv(R+'population_fresh_pinned.csv'); pop23=pop[pop.Year==2023].set_index('Country Code')['Value']
a1=pd.read_csv('data/a1_ranking_filtered.csv')
iso_ok=set(a1[a1.un_member==True]['Code'])
pv['un']=pv['Code'].isin(iso_ok); pv['pop23']=pv['Code'].map(pop23)
main=pv[pv.un & (pv.pop23>=5e6)].sort_values(['abs','rel'],ascending=False)
out.append('\n## 2. Ожирение: пересчёт Топ-12 по абсолютному изменению 2006->2016 (свежий файл; фильтр: член ООН по списку A1 + население 2023 >= 5 млн из закреплённого population.csv)\n')
out.append('| Страна | ISO | 2006 | 2016 | п.п. | % | население 2023 | совпадает с a1_top8_abs.csv |\n|---|---|---|---|---|---|---|---|')
a1top=pd.read_csv('data/a1_top8_abs.csv').set_index('Code')
for _,r in main.head(12).iterrows():
    ok='-'
    if r.Code in a1top.index:
        t=a1top.loc[r.Code]; ok='ДА' if (abs(t.y2006-r[2006])<1e-9 and abs(t.y2016-r[2016])<1e-9 and abs(t.abs_change_pp-r['abs'])<1e-9) else f'НЕТ ({t.y2006},{t.y2016},{t.abs_change_pp})'
    out.append(f'| {r.Entity} | {r.Code} | {r[2006]} | {r[2016]} | {r["abs"]:+.1f} | {r.rel:+.1f} | {int(r.pop23):,} | {ok} |')
out.append(f'\nЧисло стран в основном рейтинге (пересчёт): {len(main)} (A1: 122).')
# entities with abs >= 6.4 excluded and why
big=pv[pv['abs']>=6.4].sort_values('abs',ascending=False)
out.append('\nВсе сущности файла с изменением >= 6.4 п.п. и причина исключения из основного рейтинга:\n\n| Сущность | ISO | п.п. | член ООН (по A1) | население 2023 | статус в рейтинге |\n|---|---|---|---|---|---|')
for _,r in big.iterrows():
    st='в рейтинге' if (r.un and r.pop23>=5e6) else ('не член ООН / территория' if not r.un else f'< 5 млн')
    out.append(f'| {r.Entity} | {r.Code} | {r["abs"]:+.1f} | {r.un} | {"" if pd.isna(r.pop23) else int(r.pop23)} | {st} |')
# relative top
relm=main.sort_values('rel',ascending=False).head(8)
out.append('\nТоп-8 по относительному росту (пересчёт): '+'; '.join(f'{r.Entity} {r[2006]}->{r[2016]} ({r.rel:+.1f}%)' for _,r in relm.iterrows()))
# --- Diabetes
d=pd.read_csv(R+'ncdrisc_dm_fresh.csv'); d.columns=['Country','ISO','Sex','Year','prev','lo','hi']
d=d[d.Year.isin([2004,2014])]
p=d.pivot_table(index=['Country','ISO'],columns=['Sex','Year'],values='prev').reset_index()
p.columns=['Country','ISO']+[f'{s}_{y}' for s,y in p.columns[2:]]
p['both_2004']=(p.Men_2004+p.Women_2004)/2*100; p['both_2014']=(p.Men_2014+p.Women_2014)/2*100
p['abs']=p.both_2014-p.both_2004; p['rel']=(p.both_2014/p.both_2004-1)*100
a2=pd.read_csv('data/a2_top12_abs.csv'); a2f=pd.read_csv('data/a2_full_table.csv')
iso_un2=set(a2f[a2f.is_un_member==True]['iso'])
p['un']=p.ISO.isin(iso_un2); p['pop23']=p.ISO.map(pop23)
mainD=p[p.un & (p.pop23>=5e6)].sort_values('abs',ascending=False)
out.append('\n## 3. Диабет: пересчёт Топ-12 по абсолютному изменению 2004->2014 (свежий файл NCD-RisC 2016; оба пола = среднее Men/Women; фильтр: член ООН по списку A2 + население 2023 >= 5 млн)\n')
out.append('| Страна | ISO | 2004 оба | 2014 оба | п.п. | % | Men 2004->2014 | Women 2004->2014 | население 2023 | совпадает с a2_top12_abs.csv |\n|---|---|---|---|---|---|---|---|---|---|')
a2i=a2.set_index('iso')
for _,r in mainD.head(12).iterrows():
    ok='-'
    if r.ISO in a2i.index:
        t=a2i.loc[r.ISO]; ok='ДА' if (abs(t.prev_both_2004-r.both_2004)<0.01 and abs(t.prev_both_2014-r.both_2014)<0.01 and abs(t.abs_change_pp_both-r['abs'])<0.01) else f'НЕТ ({t.prev_both_2004},{t.prev_both_2014},{t.abs_change_pp_both})'
    out.append(f'| {r.Country} | {r.ISO} | {r.both_2004:.2f} | {r.both_2014:.2f} | {r["abs"]:+.2f} | {r.rel:+.1f} | {r.Men_2004*100:.2f}->{r.Men_2014*100:.2f} | {r.Women_2004*100:.2f}->{r.Women_2014*100:.2f} | {int(r.pop23):,} | {ok} |')
out.append(f'\nЧисло стран в основном рейтинге (пересчёт): {len(mainD)} (A2: 123).')
bigD=p[p['abs']>=3.3].sort_values('abs',ascending=False)
out.append('\nВсе сущности с изменением >= 3.3 п.п. и статус:\n\n| Сущность | ISO | п.п. | член ООН (по A2) | население 2023 | статус |\n|---|---|---|---|---|---|')
for _,r in bigD.iterrows():
    st='в рейтинге' if (r.un and r.pop23>=5e6) else ('не член ООН / территория' if not r.un else '< 5 млн')
    out.append(f'| {r.Country} | {r.ISO} | {r["abs"]:+.2f} | {r.un} | {"" if pd.isna(r.pop23) else int(r.pop23)} | {st} |')
relD=mainD.sort_values('rel',ascending=False).head(8)
out.append('\nТоп-8 по относительному росту (пересчёт): '+'; '.join(f'{r.Country} {r.both_2004:.2f}->{r.both_2014:.2f} ({r.rel:+.1f}%)' for _,r in relD.iterrows()))
# --- Atlas PDF check for selected countries
out.append('\n## 4. World Obesity Atlas: проверка прогнозных значений по локально скачанным PDF (S3 бакет WOF; SHA-256 указан)\n')
pdfs={'2025':'data/World_Obesity_Atlas_2025_rev1.pdf','2023':'data/World_Obesity_Atlas_2023_Report.pdf','2022':'data/World_Obesity_Atlas_2022.pdf'}
for k,pth in pdfs.items(): out.append(f'- Atlas {k}: {pth}, sha256 {sha(pth)}')
sel=pd.read_csv('data/a1_projections_selected.csv')
out.append('\n| Страна | Atlas 2025 стр. | найдено на странице (фрагменты) | Atlas 2023 стр. | фрагменты | Atlas 2022 стр. | фрагменты |\n|---|---|---|---|---|---|---|')
docs={k:fitz.open(v) for k,v in pdfs.items()}
def frag(doc,page,pats):
    if page is None or pd.isna(page): return 'стр. не указана'
    t=doc[int(page)-1].get_text().replace('\n',' | ')
    res=[]
    for pat in pats:
        m=re.search(pat,t)
        res.append(m.group(0)[:90] if m else f'НЕ НАЙДЕНО: {pat[:30]}')
    return '; '.join(res)
for _,r in sel.iterrows():
    name=r.Entity
    f25=frag(docs['2025'],r.get('atlas2025_page'),[re.escape(name), r'Adults living with obesity in 2025[ |]*\d+%?', r'\d+%[ |]*Adults living with obesity in 2025'])
    f23=frag(docs['2023'],r.get('atlas2023_page'),[re.escape(name), r'ADULTS WITH OBESITY[ |]*2035[ |]*\d+%?', r'\d+%[ |]*ADULTS WITH OBESITY']) if 'atlas2023_page' in sel.columns else '-'
    f22=frag(docs['2022'],r.get('atlas2022_page'),[re.escape(name), r'ADULTS WITH OBESITY BY 2030[ |]*[\d.]+%?', r'[\d.]+%[ |]*ADULTS WITH OBESITY BY 2030']) if 'atlas2022_page' in sel.columns else '-'
    out.append(f'| {name} | {r.get("atlas2025_page")} | {f25} | {r.get("atlas2023_page")} | {f23} | {r.get("atlas2022_page")} | {f22} |')
open('wave2/ORCH_data_recheck.md','w').write('\n'.join(out)+'\n')
print('\n'.join(out)[:6000])
