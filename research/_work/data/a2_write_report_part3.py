#!/usr/bin/env python3
"""Part 3: verification of Top-8, '2022 version' reference, CLAIMS table, UNVERIFIED list; then assemble final md."""
import pandas as pd, csv
D = '/home/user/research/research/_work/data'
OUTMD = '/home/user/research/research/_work/wave1/A2_diabetes_trend.md'
full = pd.read_csv(f'{D}/a2_full_table.csv')
idf = pd.read_csv(f'{D}/a2_idf11_country_2024.csv')
fr = pd.read_csv(f'{D}/a2_idf10_fragments.csv')
sf = pd.read_csv(f'{D}/a2_source_fragments.csv').set_index('key')
dm = pd.read_csv('/home/user/research/research/_work/mirrors/ncdrisc_tableau/NCD_RisC_Lancet_2016_DM_age_standardised_countries.csv')
dm.columns = ['country', 'iso', 'sex', 'year', 'prev', 'lo', 'hi']
main = full[full['in_main_ranking']].sort_values('abs_change_pp_both', ascending=False).reset_index(drop=True)
main['rank'] = main.index + 1
rel = full[full['in_main_ranking']].sort_values('rel_change_pct_both', ascending=False).reset_index(drop=True)
top8 = main.head(8)
def r(x, n=2): return f'{x:.{n}f}'
def row(c, s, y):
    x = dm[(dm.country == c) & (dm.sex == s) & (dm.year == y)].iloc[0]
    return f'"{c}","{x.iso}","{s}",{y},{x.prev:.6f},{x.lo:.6f},{x.hi:.6f}'
T = []; A = T.append
A("""
## 8. Перепроверка Топ-8 независимыми открытыми источниками

Для каждой страны: значение основного источника (NCD-RisC 2016, 2014, 18+, age-standardised, оба пола = среднее M/W) против (а) IDF Diabetes Atlas 11th ed. 2024 (20-79, crude и age-adjusted comparative), (б) IDF 10th ed. 2021, (в) рецензируемых статей (абстракты PubMed/PMC, открыты через firecrawl_research_search_papers; полные тексты в индексе отсутствуют). Расхождения не скрываются; объяснения — «наша оценка/гипотеза», если не подтверждены источником.

| Место | Страна | NCD-RisC 2014, % (M / W) | IDF 11th, 2024: crude / age-adj, % (20-79) | IDF 10th, 2021: тыс. чел.; prevalence % | Независимые оценки (абстракты) | Сравнение и объяснение расхождений | Уверенность (уровень / тренд) |
|---|---|---|---|---|---|---|---|
""")
mp = {'Iran': 'Iran (Islamic Republic of)', 'Turkey': 'Türkiye'}
V = {
 'Egypt': ("Alexandria (pmid:30056190, 18-90 лет): \"age-adjusted prevalence of diabetes of 16.8% (men, 12.7%; women 19.1%)\"; Sohag 2019, 50+ (PMC8212402): \"The prevalence of DM was 20.9%\"; обзор (pmid:27108148): \"around 15.6% of all adults aged 20 to 79\"",
           "Уровень согласуется: NCD-RisC 2014 17.9% лежит между IDF 2024 crude 19.8% / age-adj 22.4% и региональными опросами 16.8-20.9%; IDF 10th comparative prevalence 2021 — 20.9% (Table 4 PMC11057359). Разница IDF vs NCD-RisC: возраст 20-79 vs 18+, год (2024 vs 2014), стандарт населения (IDF world vs WHO), определение (NCD-RisC включает HbA1c/лечение).", "HIGH / MEDIUM"),
 'Iraq': ("STEPS 2015, 18+ (PMC9684960): \"The prevalence of UT2D was 8.1% and the prevalence of diagnosed T2D (DT2D) was 8.9%\" → суммарно 17.0% (crude, наш расчёт); Basrah 19+ (PMC4014373): 8.7% ранее диагностированных",
          "NCD-RisC 2014 17.4% ≈ STEPS 2015 crude 17.0%. IDF (2021: 9.4%; 2024: 11.0% / 13.4%) существенно ниже — гипотеза: IDF исключил STEPS-опрос как ненадёжный (Атлас 11th, стр. 15: \"The exclusion of specific WHO STEPS surveys ... concerns about their validity\") и опирается на другие источники.", "MEDIUM / MEDIUM"),
 'Turkmenistan': ("Национальных оценок в PubMed/PMC не найдено (pmid:23867899: \"Data on the prevalence of gestational diabetes (GDM) is not available for Turkmenistan or any other central Asian country\"). WHO STEPS 2018 существует (каталог extranet.who.int/ncdsmicrodata TKM_2018_STEPS_v01 найден), результаты не открылись → UNVERIFIED",
                  "Противоречие: NCD-RisC 2014 12.2% vs IDF 2021 6.0% / 2024 6.6% (age-adj 7.1%). Гипотеза: оценка NCD-RisC 2016 для Turkmenistan модельная (без национальных измерений до STEPS 2018), IDF использует STEPS 2018. Подтвердить нельзя — STEPS не открыт.", "LOW / LOW"),
 'Lebanon': ("Национальный опрос, ≥25 лет, WHO STEPwise, n=2195 (pmid:25005850): \"The prevalence of type 2 diabetes was 8.5% (95%CI=7.3-9.7)\" (год опроса в абстракте не указан; публикация 2014); PMC6233908: \"As of 2017, the prevalence of diabetes in Lebanon is estimated to be 14.6%\"",
             "Разброс 8.5-8.9% (опрос ≥25 и IDF 2021 crude) vs 13.4-14.6% (NCD-RisC 2014, IDF 2024, оценка 2017). IDF 10th сам даёт CI до 17.6%. Гипотеза: опросные значения — диагностированный/самоотчёт, модельные включают недиагностированных.", "MEDIUM / MEDIUM"),
 'Papua New Guinea': ("Только локальные/старые исследования: Wanigela (pmid:8208193): \"Age-standardised prevalence of NIDDM in Koki Wanigelas was 27.5% in men and 33.0% in women\"; Port Moresby (pmid:7000592): \"15.8% of urban residents had diabetes mellitus\"; систематический обзор PMC7682215 — чисел в абстракте нет",
                      "NCD-RisC 2014 14.8% ≈ IDF 2024 14.2% / 14.1%. Национальных измерений нет (IDF 11th: 73.2% недиагностированных — оценка). Уровень согласуется между двумя модельными источниками, но оба опираются на скудные данные (наша оценка).", "MEDIUM / LOW"),
 'Morocco': ("STEPS 2017, ≥18 (PMC9515107): \"the prevalence of undiagnosed T2D was 5.9% (44.7% of total T2D), diagnosed T2D 7.3% and total T2D 13.2%\"; национальный опрос 2000 (pmid:12714863): \"The prevalence of diabetes was 6.6%\"",
             "NCD-RisC 2014 13.7% ≈ STEPS 2017 crude 13.2%; IDF 2024 11.6% / 11.9% чуть ниже (20-79, методология). Рост с 6.6% (2000) до 13.2% (2017) по национальным опросам согласуется с направлением тренда NCD-RisC.", "HIGH / MEDIUM"),
 'Yemen': ("Sana'a, 20-85 лет, только известный диабет (pmid:15339127): \"The crude prevalence of known diabetes was 6.57% ... age-standardized prevalence for the age range 30-64 years was 9.75%\"; полусельский район, ≥35 (pmid:18557451): \"overall crude prevalence of diabetes was 10.4%\"",
           "Противоречие: NCD-RisC 2014 11.4% vs IDF 2024 4.1% / 5.5%. Опросы (только известный диабет, городские/старшие выборки) дают 6.6-10.4%. Гипотеза: IDF экстраполирует из-за отсутствия свежих национальных данных; NCD-RisC включает недиагностированных. Не разрешимо в сессии.", "LOW / LOW"),
 'Azerbaijan': ("Национальных оценок в PubMed/PMC не найдено; WHO STEPS 2017 существует (who.int/europe/publications/i/item/WHO-EURO-2021-4673-44436-62812; каталог AZE_2017_STEPS_v01), результаты не открылись → UNVERIFIED",
                "Противоречие: NCD-RisC 2014 12.3% vs IDF 2021 5.6% vs IDF 2024 9.9% / 10.2%. Сам IDF между редакциями поднял число людей с 397.1 до 715.3 тыс. (+80%) — признак смены источника данных (гипотеза: включение STEPS 2017). С учётом IDF 2024 уровень ближе к NCD-RisC.", "LOW / LOW"),
}
for _, x in top8.iterrows():
    c = x['country']; n = mp.get(c, c); y = idf[idf.country_idf == n].iloc[0]; f = fr[fr.country == c].iloc[0]
    p21 = f"{f['n_adults_1000s_2021']:,.1f}; " + (f"{f['prev_2021_pct']}%" if pd.notna(f['prev_2021_pct']) else "prevalence не извлечена")
    if c == 'Egypt': p21 += " (comparative prevalence 20.9%, Table 4 PMC11057359)"
    v = V[c]
    A(f"| {x['rank']} | {c} | {r(x['prev_both_2014'],1)} ({r(x['prev_men_2014'],1)} / {r(x['prev_women_2014'],1)}) | {y['prev_2024_pct']} / {y['age_adj_prev_2024_pct']} | {p21} | {v[0]} | {v[1]} | {v[2]} |\n")
A("""
Итог перепроверки (наша оценка): уровень 2014 года подтверждается независимыми источниками для Egypt, Morocco (HIGH), Iraq, Lebanon, Papua New Guinea (MEDIUM); для Turkmenistan, Yemen, Azerbaijan независимые источники (IDF) дают существенно более низкие значения, а национальные STEPS-опросы не открылись — LOW. Сам 10-летний тренд 2004→2014 ни один открытый источник для отдельных стран не подтверждает (все статьи — одномоментные опросы; полный текст NCD-RisC недоступен) — тренд по каждой стране остаётся MEDIUM при подтверждённом уровне и LOW при неподтверждённом.

## 9. Справочная колонка «версия 2022» (NCD-RisC 2024, Lancet, 1990-2022) — отдельно, не смешивая с рейтингом

Страновые значения 2022 для Топ-8 в открытых в сессии источниках НЕ найдены: абстракт PMC7616842 содержит только глобальные цифры; пресс-релиз WHO (13.11.2024) — глобальные и региональные; новость Imperial College (imperial.ac.uk/news/258217) отдаётся индексом фрагментами, содержащими только значение для USA; страница WHO GHO не открылась. Ниже — то, что открыто дословно.

| Утверждение | Значение | Источник | URL | Дословный фрагмент |
|---|---|---|---|---|
| Число взрослых 18+ с диабетом в мире, 2022 | 828 млн (95% CrI 757-908) | NCD-RisC 2024, абстракт (T1) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7616842/ | "In 2022, an estimated 828 million (95% credible interval [CrI] 757-908) adults (those aged 18 years and older) had diabetes, an increase of 630 million (554-713) from 1990" |
| Глобальная распространённость среди взрослых, 1990 → 2022 | 7% → 14% | WHO news release 13.11.2024 (T1) | https://www.who.int/news/item/13-11-2024-urgent-action-needed-as-global-diabetes-cases-increase-four-fold-over-past-decades | "global diabetes prevalence in adults rose from 7% to 14% between 1990 and 2022. LMICs experienced the largest increases" |
| Распространённость 18+ в регионах WHO SEAR и EMR, 2022 | около 20% | WHO news release 13.11.2024 (T1) | там же | "the prevalence of diabetes among adults aged 18 and older around 20% in the WHO South-East Asia and the Eastern Mediterranean Regions" |
| Нелеченые взрослые 30+, 2022 | ~450 млн (59%) | WHO news release 13.11.2024 (T1) | там же | "in 2022, almost 450 million adults aged 30 and older – about 59% of all adults with diabetes – remained untreated" |
| Число людей с диабетом, 1990 → 2022 | 200 млн → 830 млн | WHO fact sheet Diabetes (T1) | https://www.who.int/news-room/fact-sheets/detail/diabetes | "The number of people living with diabetes rose from 200 million in 1990 to 830 million in 2022" |
| USA 2022 (среди высокодоходных стран — максимум) | 11.4% women, 13.6% men | Imperial College London news (T2, ссылается на NCD-RisC) | https://www.imperial.ac.uk/news/258217/diabetes-rate-doubles-800-million-adults/ | "Among high-income industrialised nations, diabetes rates in 2022 were highest in the USA (11.4% amongst in women and 13.6% in men)" |
| Где были наибольшие приросты 1990-2022 | ЛМИК Юго-Восточной Азии и др. | NCD-RisC 2024, абстракт (T1) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7616842/ | "The largest increases were in low-income and middle-income countries in southeast Asia (eg," (фрагмент обрезан индексом) |
| Расхождение IDF vs NCD-RisC 2022 | 589 млн (IDF 2024, 20-79) vs 828 млн (NCD-RisC 2022, 18+) | IDF Atlas 11th, стр. 8 PDF (T1) | S5 | "the recent WHO/NCD-RisC publication estimated that 828 million people aged 18 years or older had diabetes in 2022, considerably more than estimates provided in this IDF Diabetes Atlas (589 million) for 2024" |

Для Топ-8: колонка «версия 2022» = «не найдено в открытых источниках сессии» (см. раздел 11).

## 10. Таблица CLAIMS (схема раздела 4 из 00_definitions.md)

Канал в примечаниях. Для значений из файла NCD-RisC «дословный фрагмент» = строка CSV (доля 0-1, переведена в %). Для расчётных величин — формула и строки-источники. Уверенность: значения из файла — MEDIUM (один открытый T1, целостность зеркала подтверждена косвенно); уровни, подтверждённые независимым T1 в разделе 8, — HIGH; остальное — как указано.

| id | утверждение (одно предложение) | значение | единица | год / период | определение метрики | страна | название источника | URL | уровень источника | дата доступа | дословный фрагмент (до 25 слов) | уверенность сборщика | примечания |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
""")
SRC = 'NCD-RisC, Worldwide trends in diabetes since 1980 (Lancet 2016), country file'
URL1 = 'https://github.com/banerjeemdx/Data-Visualisation-with-Tableau---NCD_RisC-dataset-on-BMI-Body-Mass-index-Diabetes-and-Blood-Pre (зеркало; оригинал ncdrisc.org, заблокирован)'
MET = 'age-standardised diabetes prevalence, adults 18+'
conf_level = {'Egypt': 'HIGH', 'Morocco': 'HIGH', 'Iraq': 'MEDIUM', 'Lebanon': 'MEDIUM', 'Papua New Guinea': 'MEDIUM', 'Turkmenistan': 'LOW', 'Yemen': 'LOW', 'Azerbaijan': 'LOW'}
cid = [0]
def C(stmt, val, unit, yr, met, country, src, url, lvl, frag, conf, note):
    cid[0] += 1
    frag = str(frag).replace('|', '/')
    A(f"| A2-{cid[0]:03d} | {stmt} | {val} | {unit} | {yr} | {met} | {country} | {src} | {url} | {lvl} | 2026-09-04 | {frag} | {conf} | {note} |\n")
# --- Top-8 abs: per-country claims
for _, x in top8.iterrows():
    c = x['country']; cl = conf_level[c]
    for s in ('Men', 'Women'):
        for y in (2004, 2014):
            v = x[f"prev_{s.lower()}_{y}"]; lo = x[f"lo_{s.lower()}_{y}"]; hi = x[f"hi_{s.lower()}_{y}"]
            C(f"Распространённость диабета ({s.lower()}) в {c} в {y} г. составляла {r(v,1)}% (95% UI {r(lo,1)}-{r(hi,1)}).", r(v,2), '%', y, f'{MET}, {s}', c, SRC, URL1, 'T1 (зеркало GitHub, целостность проверена)', row(c, s, y), 'MEDIUM' if y == 2004 else cl, 'файл в сессии (git mirror); ' + ('уровень 2014 сверен в разд. 8' if y == 2014 else ''))
    for y in (2004, 2014):
        C(f"Распространённость диабета (оба пола) в {c} в {y} г. = {r(x[f'prev_both_{y}'])}% (среднее Men/Women).", r(x[f'prev_both_{y}']), '%', y, f'{MET}, both sexes = mean(Men, Women)', c, SRC, URL1, 'T1 (расчёт)', f"расчёт: ({r(x[f'prev_men_{y}'],3)} + {r(x[f'prev_women_{y}'],3)})/2", 'MEDIUM' if y == 2004 else cl, 'a2_diabetes_trend.py; допущение простого среднего')
    C(f"{c}: место {x['rank']} основного рейтинга — прирост распространённости диабета 2004→2014 составил +{r(x['abs_change_pp_both'])} п.п.", r(x['abs_change_pp_both']), 'п.п.', '2004-2014', f'{MET}, both sexes; абсолютное изменение', c, SRC, URL1, 'T1 (расчёт)', f"расчёт: {r(x['prev_both_2014'],3)} − {r(x['prev_both_2004'],3)}", 'MEDIUM', 'тренд независимо не подтверждён (разд. 8); ранг среди 123 стран фильтра')
    C(f"{c}: относительный рост распространённости диабета 2004→2014 = +{r(x['rel_change_pct_both'],1)}%.", r(x['rel_change_pct_both'],1), '%', '2004-2014', f'{MET}, both sexes; относительное изменение', c, SRC, URL1, 'T1 (расчёт)', f"расчёт: {r(x['abs_change_pp_both'],3)} / {r(x['prev_both_2004'],3)} × 100", 'MEDIUM', f"ранг по отн. росту {int(x['rank_rel_main'])}")
    C(f"{c}: среднегодовой прирост 2004→2014 = {r(x['pp_per_year_both'])} п.п./год.", r(x['pp_per_year_both']), 'п.п./год', '2004-2014', f'{MET}, both sexes', c, SRC, URL1, 'T1 (расчёт)', f"расчёт: {r(x['abs_change_pp_both'],3)} / 10", 'MEDIUM', '')
    C(f"Население {c} в 2023 г. = {int(x['pop_2023']):,} чел.", int(x['pop_2023']), 'чел.', 2023, 'World Bank total population', c, 'World Bank population (datahub mirror github.com/datasets/population)', 'https://github.com/datasets/population', 'T1 (зеркало)', f"{c},{x['iso']},2023,{int(x['pop_2023'])}", 'MEDIUM', 'файл в сессии (git mirror)')
# --- relative top-8 extras and close (9-12)
for _, x in rel.head(8).iterrows():
    if x['country'] in set(top8['country']): continue
    C(f"{x['country']}: относительный рост 2004→2014 = +{r(x['rel_change_pct_both'],1)}% (с {r(x['prev_both_2004'])}% до {r(x['prev_both_2014'])}%; +{r(x['abs_change_pp_both'])} п.п.).", r(x['rel_change_pct_both'],1), '%', '2004-2014', f'{MET}, both sexes', x['country'], SRC, URL1, 'T1 (расчёт)', row(x['country'], 'Men', 2014) + ' ; ' + row(x['country'], 'Women', 2014), 'MEDIUM', 'альтернативный рейтинг (разд. 3)')
for _, x in main.iloc[8:12].iterrows():
    C(f"{x['country']}: место {x['rank']} основного рейтинга, прирост 2004→2014 = +{r(x['abs_change_pp_both'])} п.п. ({r(x['prev_both_2004'])}% → {r(x['prev_both_2014'])}%).", r(x['abs_change_pp_both']), 'п.п.', '2004-2014', f'{MET}, both sexes', x['country'], SRC, URL1, 'T1 (расчёт)', row(x['country'], 'Men', 2014) + ' ; ' + row(x['country'], 'Women', 2014), 'MEDIUM', 'кто близко (разд. 4)')
# --- small states and excluded
sm = pd.read_csv(f'{D}/a2_small_states.csv'); ex = pd.read_csv(f'{D}/a2_excluded_non_un.csv')
for _, x in sm.iterrows():
    C(f"{x['country']} (население {int(x['pop_2023']):,}) без фильтра заняла бы место {int(x['rank_abs_un_all'])} среди членов ООН: +{r(x['abs_change_pp_both'])} п.п. ({r(x['prev_both_2004'])}% → {r(x['prev_both_2014'])}%).", r(x['abs_change_pp_both']), 'п.п.', '2004-2014', f'{MET}, both sexes', x['country'], SRC, URL1, 'T1 (расчёт)', row(x['country'], 'Men', 2014) + ' ; ' + row(x['country'], 'Women', 2014), 'MEDIUM', 'малые государства (разд. 5); население — World Bank 2023')
for _, x in ex.head(3).iterrows():
    C(f"{x['country']} исключена из рейтинга ({x['exclusion_note']}); прирост 2004→2014 = +{r(x['abs_change_pp_both'])} п.п., ранг {int(x['rank_abs_all200'])} среди всех 200 записей.", r(x['abs_change_pp_both']), 'п.п.', '2004-2014', f'{MET}, both sexes', x['country'], SRC, URL1, 'T1 (расчёт)', row(x['country'], 'Men', 2014) + ' ; ' + row(x['country'], 'Women', 2014), 'MEDIUM', 'исключённые (разд. 6)')
# --- integrity / global NCD-RisC 2016
C("Глобальная age-standardised распространённость диабета (men) выросла с 4.3% (1980) до 9.0% (2014).", '4.3 → 9.0', '%', '1980-2014', 'age-standardised diabetes prevalence, men 18+', 'World', 'NCD-RisC Lancet 2016 (PMC5081106), абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5081106/', 'T1', sf.loc['NCDRISC2016_global','fragment'], 'HIGH', 'firecrawl_research_search_papers; сверка с файлом: взвешенное 4.16 → 8.99')
C("Глобальная age-standardised распространённость диабета (women) выросла с 5.0% (1980) до 7.9% (2014).", '5.0 → 7.9', '%', '1980-2014', 'age-standardised diabetes prevalence, women 18+', 'World', 'NCD-RisC Lancet 2016 (PMC5081106), абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5081106/', 'T1', sf.loc['NCDRISC2016_global','fragment'], 'HIGH', 'firecrawl_research_search_papers; сверка с файлом: взвешенное 4.93 → 8.22')
C("Число взрослых с диабетом в мире выросло со 108 млн (1980) до 422 млн (2014).", '108 → 422', 'млн чел.', '1980-2014', 'adults 18+ with diabetes', 'World', 'NCD-RisC Lancet 2016 (PMC5081106), абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5081106/', 'T1', sf.loc['NCDRISC2016_number','fragment'], 'HIGH', 'firecrawl_research_search_papers; также IDF 11th стр. 8: "the WHO/NCD-RisC estimate of 422 million"')
C("В 2014 г. наивысшая национальная распространённость диабета была в American Samoa (>30%).", '>30', '%', 2014, 'age-standardised diabetes prevalence 18+', 'American Samoa', 'NCD-RisC Lancet 2016 (PMC5081106), абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5081106/', 'T1', sf.loc['NCDRISC2016_regions','fragment'], 'HIGH', f"файл: American Samoa 2014 men {r(full[full.country=='American Samoa']['prev_men_2014'].iloc[0],1)}%, women {r(full[full.country=='American Samoa']['prev_women_2014'].iloc[0],1)}%")
# --- IDF 11th for top-8
for _, x in top8.iterrows():
    c = x['country']; n = mp.get(c, c); y = idf[idf.country_idf == n].iloc[0]
    C(f"IDF 11th: в {c} в 2024 г. {y['n_adults_1000s_2024']:,.1f} тыс. взрослых 20-79 лет с диабетом.", f"{y['n_adults_1000s_2024']:,.1f}", 'тыс. чел.', 2024, 'number of adults 20-79 with diabetes (IDF estimate)', c, 'IDF Diabetes Atlas 11th edition (2025), country summary tables', 'https://international-diabetes-federation.s3.eu-west-1.amazonaws.com/media/uploads/sites/3/2025/10/IDF_Diabetes_Atlas_11th_Edition_2025_WEB.pdf', 'T1', f"стр. {y['page']} PDF: {n} / {y['n_adults_1000s_2024']:,.1f} / {y['prev_2024_pct']} / {y['age_adj_prev_2024_pct']} / {y['undiagnosed_2024_pct']}", 'HIGH', 'curl S3 + текст PDF; парсер сверен с Table 3.4/3.5')
    C(f"IDF 11th: распространённость диабета 20-79 лет в {c} в 2024 г. = {y['prev_2024_pct']}% (crude), age-adjusted comparative {y['age_adj_prev_2024_pct']}%.", f"{y['prev_2024_pct']} / {y['age_adj_prev_2024_pct']}", '%', 2024, 'diabetes prevalence 20-79, crude / age-adjusted comparative (IDF)', c, 'IDF Diabetes Atlas 11th edition (2025), country summary tables', 's3 bucket IDF (см. S5)', 'T1', f"стр. {y['page']} PDF: {n} / {y['n_adults_1000s_2024']:,.1f} / {y['prev_2024_pct']} / {y['age_adj_prev_2024_pct']}", 'HIGH', 'НЕ сопоставимо с NCD-RisC (18+, WHO-стандарт)')
    f = fr[fr.country == c].iloc[0]
    C(f"IDF 10th: в {c} в 2021 г. {f['n_adults_1000s_2021']:,.1f} тыс. взрослых 20-79 лет с диабетом" + (f", prevalence {f['prev_2021_pct']}%." if pd.notna(f['prev_2021_pct']) else "."), f"{f['n_adults_1000s_2021']:,.1f}" + (f" / {f['prev_2021_pct']}" if pd.notna(f['prev_2021_pct']) else ''), 'тыс. чел. / %', 2021, 'number of adults 20-79 with diabetes; prevalence (IDF 10th ed.)', c, 'IDF Diabetes Atlas 10th edition (2021), Country summary tables, NCBI Bookshelf', f['source_url'], 'T1', f['verbatim_fragment'], 'MEDIUM', 'firecrawl_search: ~200-символьный фрагмент таблицы; порядок колонок: число (95% CI), prevalence (95% CI), age-adj (95% CI), недиагностированные')
    d = y['n_adults_1000s_2024'] - f['n_adults_1000s_2021']
    C(f"Разница оценок IDF 11th (2024) − 10th (2021) для {c}: {d:+,.1f} тыс. ({d/f['n_adults_1000s_2021']*100:+.1f}%) — НЕ тренд, методология менялась.", f"{d:+,.1f}", 'тыс. чел.', '2021→2024', 'difference of two IDF editions, adults 20-79', c, 'IDF 10th (NCBI) и 11th (PDF)', 'см. выше', 'T1 (расчёт)', f"{f['n_adults_1000s_2021']:,.1f} → {y['n_adults_1000s_2024']:,.1f}", 'LOW', 'вторичная колонка с оговоркой (разд. 7)')
# --- IDF global / tables
C("IDF 10th: в 2021 г. в мире 536.6 млн взрослых 20-79 лет с диабетом (10.5%); прогноз 2045 — 783.2 млн (12.2%).", '536.6 (10.5%)', 'млн чел.', 2021, 'adults 20-79 with diabetes (IDF)', 'World', 'Sun et al. 2022, PMC11057359, абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11057359/', 'T1', sf.loc['IDF10_global','fragment'], 'HIGH', 'firecrawl_research_search_papers; 2045 — прогноз')
C("IDF 11th: в 2024 г. в мире 588.7 млн взрослых 20-79 лет с диабетом (11.1%); прогноз 2050 — 852.5 млн (13.0%).", '588.7 (11.1%)', 'млн чел.', 2024, 'adults 20-79 with diabetes (IDF)', 'World', 'IDF Diabetes Atlas 11th edition (2025), Table 3.4', 's3 bucket IDF (см. S5)', 'T1', 'Table 3.4 ... World 11.1 11.1 588.7 13.0 13.0 852.5 (стр. 52 PDF)', 'HIGH', 'текст PDF; 2050 — прогноз')
C("IDF 10th, Table 5: Топ-10 по числу взрослых 20-79 с диабетом в 2021 г.: China 140.9, India 74.2, Pakistan 33.0, USA 32.2, Indonesia 19.5, Brazil 15.7, Mexico 14.1, Bangladesh 13.1, Japan 11.0, Egypt 10.9 млн.", 'см. утверждение', 'млн чел.', 2021, 'adults 20-79 with diabetes (IDF)', 'Top-10', 'Sun et al. 2022, PMC11057359, Table 5', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11057359/', 'T1', sf.loc['IDF10_table5','fragment'][:200], 'HIGH', 'firecrawl_search: таблица на странице PMC')
C("IDF 11th, Table 3.4: Топ-10 по числу взрослых 20-79 с диабетом в 2024 г.: China 148.0, India 89.8, USA 38.5, Pakistan 34.5, Indonesia 20.4, Brazil 16.6, Bangladesh 13.9, Mexico 13.6, Egypt 13.2, Japan 10.8 млн.", 'см. утверждение', 'млн чел.', 2024, 'adults 20-79 with diabetes (IDF)', 'Top-10', 'IDF Diabetes Atlas 11th edition (2025), Table 3.4', 's3 bucket IDF (см. S5)', 'T1', '1 China 148.0 ... 2 India 89.8 ... 3 United States of America 38.5 ... 4 Pakistan 34.5 (стр. 52 PDF)', 'HIGH', 'текст PDF')
C("IDF 10th: наивысшая comparative prevalence 2021 — Pakistan 30.8%, French Polynesia 25.2%, Kuwait 24.9%; Egypt — 10-е место, 20.9%.", '30.8 / 25.2 / 24.9 / 20.9', '%', 2021, 'age-adjusted comparative diabetes prevalence 20-79 (IDF)', 'Pakistan; French Polynesia; Kuwait; Egypt', 'IDF 10th, Chapter 3 (NBK581940) и Table 4 PMC11057359', 'https://www.ncbi.nlm.nih.gov/books/NBK581940/', 'T1', sf.loc['IDF10_top_prev','fragment'], 'HIGH', 'firecrawl_search')
C("IDF 11th: наивысшая age-standardised prevalence 2024 — Pakistan 31.4%, Marshall Islands 25.7%, Kuwait 25.6%.", '31.4 / 25.7 / 25.6', '%', 2024, 'age-standardised diabetes prevalence 20-79 (IDF)', 'Pakistan; Marshall Islands; Kuwait', 'IDF Diabetes Atlas 11th edition (2025), стр. 46', 's3 bucket IDF (см. S5)', 'T1', sf.loc['IDF11_top_prev','fragment'], 'HIGH', 'текст PDF')
C("IDF 11th: 62 из 215 стран/территорий (29%) не имеют собственных данных; использовано 246 источников из 153 стран.", '62/215; 246/153', 'стран', 2024, 'coverage of in-country data sources', 'World', 'IDF Diabetes Atlas 11th edition (2025), стр. 7, 28', 's3 bucket IDF (см. S5)', 'T1', sf.loc['IDF11_lack','fragment'], 'HIGH', 'текст PDF')
C("IDF 10th: использовано 219 источников данных из 144 стран.", '219/144', 'источников/стран', 2021, 'data sources', 'World', 'IDF 10th, Chapter 3 (NBK581940)', 'https://www.ncbi.nlm.nih.gov/books/NBK581940/', 'T1', sf.loc['IDF10_sources','fragment'], 'HIGH', 'firecrawl_search')
C("IDF 11th перечисляет причины расхождений между 10-й и 11-й редакциями (новые исследования, регистры, исключение STEPS-опросов).", '—', '—', '2021→2024', 'методологическая оговорка', 'World', 'IDF Diabetes Atlas 11th edition (2025), стр. 15', 's3 bucket IDF (см. S5)', 'T1', 'Possible reasons to account for significant differences between the 10th edition (2021) and 11th edition (2024) figures are: The inclusion of new studies', 'HIGH', 'текст PDF')
C("IDF 11th сопоставляет свою оценку (589 млн, 2024, 20-79) с NCD-RisC (828 млн, 2022, 18+).", '589 vs 828', 'млн чел.', '2022/2024', 'adults with diabetes', 'World', 'IDF Diabetes Atlas 11th edition (2025), стр. 8', 's3 bucket IDF (см. S5)', 'T1', sf.loc['IDF11_vs_ncdrisc','fragment'], 'HIGH', 'текст PDF')
# --- 2022 reference
C("NCD-RisC 2024: в 2022 г. 828 млн (95% CrI 757-908) взрослых 18+ имели диабет, +630 млн к 1990 г.", '828', 'млн чел.', 2022, 'adults 18+ with diabetes (NCD-RisC 2024 definition)', 'World', 'NCD-RisC Lancet 2024 (PMC7616842), абстракт', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7616842/', 'T1', sf.loc['NCDRISC2024_global','fragment'], 'HIGH', 'firecrawl_research_search_papers; согласуется с WHO fact sheet (830 млн)')
C("WHO: глобальная распространённость диабета среди взрослых выросла с 7% до 14% между 1990 и 2022 гг.", '7 → 14', '%', '1990-2022', 'diabetes prevalence adults 18+ (NCD-RisC 2024)', 'World', 'WHO news release 13.11.2024', 'https://www.who.int/news/item/13-11-2024-urgent-action-needed-as-global-diabetes-cases-increase-four-fold-over-past-decades', 'T1', sf.loc['WHO2024_prev','fragment'], 'HIGH', 'firecrawl_search (полный текст)')
C("WHO: распространённость диабета 18+ около 20% в регионах Юго-Восточной Азии и Восточного Средиземноморья (2022).", '~20', '%', 2022, 'diabetes prevalence adults 18+', 'WHO SEAR; WHO EMR', 'WHO news release 13.11.2024', 'см. выше', 'T1', sf.loc['WHO2024_regions','fragment'], 'MEDIUM', 'firecrawl_search; один источник')
C("WHO: в 2022 г. почти 450 млн взрослых 30+ с диабетом (59%) не получали лечения.", '450 (59%)', 'млн чел.', 2022, 'untreated adults 30+ with diabetes', 'World', 'WHO news release 13.11.2024', 'см. выше', 'T1', sf.loc['WHO2024_untreated','fragment'], 'MEDIUM', 'firecrawl_search; Imperial: "445 million adults aged 30 years and older with diabetes (59%) did not receive treatment in 2022"')
C("Imperial/NCD-RisC: среди высокодоходных стран в 2022 г. наивысшая распространённость — USA (11.4% women, 13.6% men).", '11.4 / 13.6', '%', 2022, 'diabetes prevalence adults 18+ (NCD-RisC 2024)', 'United States of America', 'Imperial College London news 258217', 'https://www.imperial.ac.uk/news/258217/diabetes-rate-doubles-800-million-adults/', 'T2 (ссылается на T1)', sf.loc['IMPERIAL_USA','fragment'], 'MEDIUM', 'firecrawl_search: только сниппет страницы')
# --- verification claims
C("Iraq STEPS 2015 (18+): недиагностированный T2D 8.1%, диагностированный 8.9%.", '8.1 + 8.9', '%', 2015, 'crude prevalence T2D, adults 18+, STEPS', 'Iraq', 'Pengpid & Peltzer 2022, BMJ Open, PMC9684960 (абстракт)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9684960/', 'T1', sf.loc['V_IRQ_steps','fragment'], 'MEDIUM', 'firecrawl_research_search_papers; сумма 17.0% — наш расчёт')
C("Morocco STEPS 2017 (≥18): total T2D 13.2% (недиагностированный 5.9%, диагностированный 7.3%).", '13.2', '%', 2017, 'crude prevalence T2D, adults 18+, STEPS', 'Morocco', 'Pengpid & Peltzer 2022, Sci Rep, PMC9515107 (абстракт)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9515107/', 'T1', sf.loc['V_MAR_steps','fragment'], 'MEDIUM', 'firecrawl_research_search_papers')
C("Morocco, национальный опрос 2000: распространённость диабета 6.6%.", '6.6', '%', 2000, 'crude diabetes prevalence, national survey', 'Morocco', 'pmid:12714863 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/12714863/', 'T1', sf.loc['V_MAR_2000','fragment'], 'MEDIUM', 'firecrawl_research_search_papers')
C("Lebanon, национальный опрос ≥25 лет (n=2195, WHO STEPwise): T2D 8.5% (95% CI 7.3-9.7).", '8.5', '%', 'публикация 2014 (год опроса не в абстракте)', 'prevalence T2D adults ≥25', 'Lebanon', 'Costanian et al. 2014, Diabetes Res Clin Pract, pmid:25005850 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/25005850/', 'T1', sf.loc['V_LBN_national','fragment'], 'MEDIUM', 'firecrawl_research_search_papers')
C("Lebanon: «на 2017 г. распространённость диабета оценивается в 14.6%» (по цитирующей статье).", '14.6', '%', 2017, 'diabetes prevalence (источник оценки в абстракте не назван)', 'Lebanon', 'PMC6233908 (абстракт)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6233908/', 'T1 (вторичная цитата)', sf.loc['V_LBN_2017','fragment'], 'LOW', 'firecrawl_research_search_papers; первоисточник оценки не открыт')
C("Egypt, Alexandria (18-90 лет): age-adjusted prevalence диабета 16.8% (men 12.7%, women 19.1%).", '16.8', '%', 'публикация 2018', 'age-adjusted diabetes prevalence, adults 18-90, Alexandria', 'Egypt', 'pmid:30056190 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/30056190/', 'T1', sf.loc['V_EGY_alex','fragment'], 'MEDIUM', 'firecrawl_research_search_papers; региональная выборка')
C("Egypt, Sohag 2019 (50+): распространённость диабета 20.9% (95% CI 19.3-22.5).", '20.9', '%', 2019, 'diabetes prevalence, adults 50+, Sohag', 'Egypt', 'AlSawahli et al. 2021, BMJ Open, PMC8212402 (абстракт)', 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8212402/', 'T1', sf.loc['V_EGY_sohag','fragment'], 'MEDIUM', 'firecrawl_research_search_papers; выборка 50+')
C("Обзор 2016: распространённость T2D в Egypt около 15.6% взрослых 20-79 лет.", '15.6', '%', 'публикация 2016', 'T2D prevalence adults 20-79 (обзор)', 'Egypt', 'Hegazi et al. 2015, Ann Glob Health, pmid:27108148 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/27108148/', 'T1 (обзор)', sf.loc['V_EGY_review','fragment'], 'MEDIUM', 'firecrawl_research_search_papers')
C("Yemen, Sana'a (20-85 лет): известный диабет 6.57% (crude); age-standardized 30-64 лет — 9.75%.", '6.57 / 9.75', '%', 'публикация 2002', 'known (diagnosed) diabetes, adults 20-85, Sana\'a', 'Yemen', 'Gunaid 2002, pmid:15339127 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/15339127/', 'T1', sf.loc['V_YEM_sanaa','fragment'], 'MEDIUM', 'firecrawl_research_search_papers; только диагностированные')
C("Yemen, полусельский район у Sana'a (≥35 лет, n=250): crude prevalence диабета 10.4%.", '10.4', '%', 'публикация 2008', 'crude diabetes prevalence, adults ≥35', 'Yemen', 'pmid:18557451 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/18557451/', 'T1', sf.loc['V_YEM_semirural','fragment'], 'LOW', 'firecrawl_research_search_papers; малая выборка')
C("Papua New Guinea, Koki Wanigela: age-standardised NIDDM 27.5% (men), 33.0% (women).", '27.5 / 33.0', '%', 'публикация 1994', 'age-standardised NIDDM prevalence, one community', 'Papua New Guinea', 'pmid:8208193 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/8208193/', 'T1', sf.loc['V_PNG_wanigela','fragment'], 'LOW', 'firecrawl_research_search_papers; локальная община, не национальное значение')
C("Papua New Guinea, Port Moresby: 15.8% городских жителей имели диабет (OGTT).", '15.8', '%', 'публикация 1980', 'diabetes prevalence, urban sample, OGTT', 'Papua New Guinea', 'pmid:7000592 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/7000592/', 'T1', sf.loc['V_PNG_urban','fragment'], 'LOW', 'firecrawl_research_search_papers; малая выборка 1970-х')
C("Turkmenistan: данных по распространённости гестационного диабета для страны и Центральной Азии не было (2013).", '—', '—', 2013, 'data availability', 'Turkmenistan', 'pmid:23867899 (абстракт)', 'https://pubmed.ncbi.nlm.nih.gov/23867899/', 'T1', sf.loc['V_TKM_gdm','fragment'], 'MEDIUM', 'firecrawl_research_search_papers; косвенно о дефиците данных')
C("Список членов ООН: 193 государства (таблица Current members).", 193, 'государств', '2026-09-04', 'UN membership', '—', 'Wikipedia, Member states of the United Nations', 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations', 'T3 (сверено с A1: 193=193)', 'Current members | Member state | Date of admission | ... Afghanistan | 19 November 1946 ... Zimbabwe | 25 August 1980', 'MEDIUM', 'firecrawl_search; файл data/un_member_states_a2.csv')
A(f"""
Всего утверждений: {cid[0]}.

## 11. UNVERIFIED — непроверенное (в отчёт не выносить как факт)

| # | Утверждение / пробел | Что искали | Что получено | Статус |
|---|---|---|---|---|
| U1 | Значения NCD-RisC 2024 (данные 2022) для Топ-8 (Egypt, Iraq, Turkmenistan, Lebanon, Papua New Guinea, Morocco, Yemen, Azerbaijan) | PMC7616842 (inspect/read_paper — полного текста нет), WHO news 13.11.2024 (только глобально/регионально), Imperial news 258217 (индекс отдаёт только сниппеты про USA и нелеченых), WHO GHO (who.int/data — не открылся), ncdrisc.org — заблокирован | Ни одного странового значения 2022 | UNVERIFIED — колонка «версия 2022» для Топ-8 пуста |
| U2 | WHO STEPS Turkmenistan 2018: доля с повышенной глюкозой/диабетом | site:who.int, iris.who.int (PDF-обзор STEPS Европейского региона найден, но индекс отдаёт только общую фразу "All the countries surveyed had a prevalence of raised blood glucose or being currently on medication for diabetes of over 4%"), каталог extranet.who.int TKM_2018_STEPS_v01 (без результатов) | Документ найден, цифра не получена | UNVERIFIED (LOW) — независимая проверка Turkmenistan опирается только на IDF |
| U3 | WHO STEPS Azerbaijan 2017: доля с повышенной глюкозой/диабетом | who.int/europe/publications/i/item/WHO-EURO-2021-4673-44436-62812 (страница найдена, текст не отдан), iris.who.int PDF-обзор (см. U2), каталог AZE_2017_STEPS_v01 | Документ найден, цифра не получена | UNVERIFIED (LOW) |
| U4 | Prevalence 2021 (IDF 10th) для Egypt, Morocco, Papua New Guinea, Yemen, Pakistan | Сниппеты NCBI Bookshelf appendices.s1 (запросы по строкам таблицы) | Число людей извлечено, столбец prevalence в сниппет не попал (для Egypt есть comparative prevalence 20.9% из Table 4 PMC11057359) | Частично; ячейки оставлены пустыми |
| U5 | Полная страновая таблица IDF 10th (все 215 стран) для рейтинга «Топ по приросту числа людей 2021→2024» | NCBI Bookshelf (только фрагменты), Supplementary Table 1 PMC11057359 (файл не открыт), S3-бакет IDF (кандидатные URL 10-й редакции — 403), GitHub-зеркал не найдено (firecrawl categories github — пусто; WebSearch — бюджет сессии исчерпан) | Таблица не построена; извлечены 15 строк | Не выполнено — см. 7.2 |
| U6 | Гипотезы об источниках расхождений NCD-RisC vs IDF для Iraq, Turkmenistan, Yemen, Azerbaijan (исключение/включение STEPS) | Текст IDF 11th (общая оговорка об исключении STEPS есть; поимённого списка нет) | Общая формулировка есть, страновой привязки нет | Гипотеза (наша оценка), не факт |
| U7 | Год проведения национального опроса Lebanon (pmid:25005850) | Абстракт (firecrawl_research); полный текст недоступен | Год не указан в абстракте | Уточнить в полном тексте |
| U8 | South Sudan (член ООН, население > 5 млн) отсутствует в файле NCD-RisC 2016 | Файл NCD-RisC (200 стран) | Нет строки | Пробел покрытия; в рейтинге не участвует |
| U9 | Значение «оба пола» NCD-RisC (популяционно-взвешенное) для Топ-8 | Файл содержит только Men/Women | Использовано простое среднее (допущение) | Допущение зафиксировано в разд. 1 |

## 12. Файлы

- Скрипты: `research/_work/data/a2_diabetes_trend.py` (расчёт, парсер IDF 11th, проверка целостности), `a2_make_tables.py`, `a2_write_report.py`, `a2_write_report_part2.py`, `a2_write_report_part3.py` (сборка).
- CSV: `a2_full_table.csv` (200 стран, все колонки), `a2_top12_abs.csv`, `a2_top12_rel.csv`, `a2_small_states.csv`, `a2_excluded_non_un.csv`, `a2_integrity_check.csv`, `a2_idf11_country_2024.csv` (222 строки: 215 стран/территорий + 7 регионов), `a2_idf10_fragments.csv` (фрагменты 10-й редакции с дословными строками и URL), `a2_source_fragments.csv` (дословные фрагменты всех открытых источников), `un_member_states_a2.csv` (193 члена ООН, URL, дата), `a2_run_log.txt`.
""")
p1 = open(f'{D}/a2_report_part1.md', encoding='utf-8').read()
p2 = open(f'{D}/a2_report_part2.md', encoding='utf-8').read()
open(OUTMD, 'w', encoding='utf-8').write(p1 + p2 + ''.join(T))
print('written', OUTMD, 'claims:', cid[0])
