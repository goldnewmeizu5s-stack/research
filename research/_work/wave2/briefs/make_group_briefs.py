import re, sys, json, collections
FILES=[('wave1/B3_anomalies_europe.md','B3'),('wave1/B5_anomalies_south_asia_africa.md','B5'),('wave1/B6_anomalies_by_category.md','B6'),('wave1/B7_hypotheses.md','B7')]
for extra in sys.argv[1:]:
    p,pre=extra.split(':'); FILES.append((p,pre))
GROUPS=collections.OrderedDict([
 ('Denmark_Nordics',['Дания','Финляндия','Норвегия']),
 ('Hungary_Poland_Baltics',['Венгрия','Польша','Латвия','Литва']),
 ('UK_Ireland_Austria',['UK','Великобритания','Ирландия','Австрия']),
 ('Germany_EU_Italy',['Германия','ЕС','Европа','Италия']),
 ('France_Iberia_Swiss_NL',['Франция','Испания','Португалия','Швейцария','Нидерланды']),
 ('Russia_CIS_Mongolia',['Россия','Беларусь','Украина','Казахстан','Узбекистан','Киргизия','Монголия','КНДР']),
 ('India',['Индия']),
 ('SriLanka_Maldives_Pakistan_Korea',['Шри-Ланка','Мальдивы','Пакистан','Корея']),
 ('Africa',['ЮАР','Нигерия','Маврикий','Сейшелы','Ботсвана','Зимбабве','Гана','Эфиопия','Кения','Руанда','Уганда']),
 ('Japan_China',['Япония','Китай']),
 ('Singapore_Australia_NZ',['Сингапур','Австралия','Новая Зеландия']),
 ('Pacific_SEAsia',['Самоа','Тонга','Фиджи','Науру','Вануату','Острова Кука','Токелау','Тихий океан','Филиппины','Малайзия','Таиланд','Индонезия','Вьетнам']),
 ('USA',['США']),
 ('Canada_LatAm_Caribbean',['Канада','Мексика','Чили','Аргентина','Бразилия','Колумбия','Эквадор','Перу','Куба','Барбадос','Бермуды','Америк','Уругвай']),
 ('MENA',['ОАЭ','Саудовская','Катар','Кувейт','Египет','Израиль','Иран','Турция','GCC','EMR','Оман','Бахрейн','Марокко','Ливан','Иордания','Ирак','Тунис','Алжир']),
 ('Global_bases',['мир','Мир','WHO','ВОЗ']),
])
B7MAP={'H1':'Japan_China','H2':'Singapore_Australia_NZ','H3':'Pacific_SEAsia','H4':'MENA','H5':'Japan_China','H6':'Singapore_Australia_NZ','H7':'Canada_LatAm_Caribbean','H8':'Canada_LatAm_Caribbean','H9':'USA','H10':'Canada_LatAm_Caribbean','H11':'Denmark_Nordics','H12':'Hungary_Poland_Baltics','H13':'UK_Ireland_Austria','H14':'Germany_EU_Italy','H15':'Germany_EU_Italy','H16':'MENA','H17':'MENA'}
def grp(country):
    for g,keys in GROUPS.items():
        for k in keys:
            if k in country: return g
    return None
cands=collections.defaultdict(list); claims=collections.defaultdict(list); hdrs={}
for path,pre in FILES:
    lines=open(path).read().split('\n')
    hdr=None
    for l in lines:
        if not l.startswith('|'): continue
        c=[x.strip() for x in l.strip('|').split('|')]
        if re.match(r'^'+pre+r'-\d+$', c[0]):
            if len(c)<9: continue
            g=grp(c[6]) or 'Global_bases'
            claims[g].append((pre,c))
            continue
        if set(l.replace('|','').strip())<=set('-: '): continue
        low=l.lower()
        if ('страна' in low or 'гипотеза' in low) and ('мера' in low or 'вердикт' in low or 'гипотеза' in low) and (c[0] in ('#','№','id','№ / id') or 'гипотез' in c[1].lower()):
            hdr=c; hdrs[(pre,tuple(c))]=True; continue
        if hdr and c[0] not in ('id','#','№') and not c[0].startswith(pre+'-'):
            if pre=='B7':
                m=re.match(r'^(H\d+)',c[0]); g=B7MAP.get(m.group(1)) if m else None
            else:
                g=grp(c[1]) if len(c)>1 else None
            if g: cands[g].append((pre,hdr,c))
import os
os.makedirs('wave2/briefs/groups',exist_ok=True)
summary=[]
for g in GROUPS:
    if not claims[g] and not cands[g]: continue
    out=[f"# Бриф верификатора аномалий: {g}","","Ниже - ТОЛЬКО описания кандидатов-мер и утверждения сборщиков с URL, без их оценок и аргументов. Дата доступа сборщиков: 2026-09-04.","","## Кандидаты (как сформулировали сборщики; каждое поле подлежит проверке)",""]
    for pre,hdr,c in cands[g]:
        keep=[i for i,h in enumerate(hdr) if not re.search('оценк|уверен|аномальн|вердикт|claims',h.lower())]
        out.append(f"- [{pre}] "+"; ".join(f"{hdr[i]}: {c[i]}" for i in keep if i<len(c) and c[i]))
    out+=["","## Утверждения (claims)","","| id | утверждение | значение | единица | год/период | определение метрики | страна | название источника | URL |","|---|---|---|---|---|---|---|---|---|"]
    for pre,c in claims[g]:
        c=(c+['']*14)[:14]
        out.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]} | {c[6]} | {c[7]} | {c[8]} |")
    fn=f"wave2/briefs/groups/{g}.md"; open(fn,'w').write('\n'.join(out)+'\n')
    summary.append((g,len(cands[g]),len(claims[g]),os.path.getsize(fn)))
for s in summary: print(s)
