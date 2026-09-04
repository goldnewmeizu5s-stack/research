#!/usr/bin/env python3
"""Part 2 of the A2 report: IDF section (11th ed. parsed tables + 10th ed. fragments)."""
import pandas as pd
D = '/home/user/research/research/_work/data'
full = pd.read_csv(f'{D}/a2_full_table.csv')
idf = pd.read_csv(f'{D}/a2_idf11_country_2024.csv')
fr = pd.read_csv(f'{D}/a2_idf10_fragments.csv')
main = full[full['in_main_ranking']].sort_values('abs_change_pp_both', ascending=False).reset_index(drop=True)
main['rank'] = main.index + 1
mp = {'Iran': 'Iran (Islamic Republic of)', 'Turkey': 'Türkiye'}
REG = ['AFR','EUR','MENA','NAC','SACA','SEA','WP']
c = idf[~idf['country_idf'].isin(REG)]
T = []; A = T.append
A("""
## 7. Вторичная колонка: прирост абсолютного числа людей с диабетом (IDF Diabetes Atlas, взрослые 20-79 лет)

**Оговорки (обязательные):** (а) IDF считает взрослых 20-79 лет и использует собственную методологию отбора источников и экстраполяции; NCD-RisC — 18+ и age-standardised по своей модели; значения не сопоставимы между собой. (б) Между 10-й (2021) и 11-й (2024) редакциями IDF методология менялась — сам Атлас перечисляет причины расхождений (стр. 15 PDF, дословно): "Possible reasons to account for significant differences between the 10th edition (2021) and 11th edition (2024) figures are: The inclusion of new studies for some countries. The inclusion of national diabetes registry data with modification ... The exclusion of specific WHO STEPS surveys included in the previous edition, as a result of concerns about their validity". Поэтому «прирост 2021→2024» — не измеренный тренд, а разница двух оценок; используется только как вторичная проверка. (в) Age-adjusted comparative prevalence IDF — стандартизация к мировой популяции IDF (не WHO-стандарт NCD-RisC). (г) Атлас сам отмечает расхождение с NCD-RisC (стр. 8 PDF): "the recent WHO/NCD-RisC publication estimated that 828 million people aged 18 years or older had diabetes in 2022, considerably more than estimates provided in this IDF Diabetes Atlas (589 million) for 2024".

### 7.1 IDF 11th edition (2025), данные 2024 — Топ-12 основного рейтинга (страновые таблицы, стр. 107-121 PDF; файл `a2_idf11_country_2024.csv`)

| Место (A2) | Страна (название IDF) | Число взрослых 20-79 с диабетом 2024, тыс. | Diabetes prevalence 20-79, 2024, % | Age-adjusted comparative prevalence 20-79, 2024, % | Недиагностировано, % | Стр. PDF | NCD-RisC 2014 (18+, age-std, оба пола), % — для сравнения, НЕ сопоставимо |
|---|---|---|---|---|---|---|---|
""")
for _, x in main.head(12).iterrows():
    n = mp.get(x['country'], x['country']); y = idf[idf['country_idf'] == n].iloc[0]
    A(f"| {x['rank']} | {n} | {y['n_adults_1000s_2024']:,.1f} | {y['prev_2024_pct']} | {y['age_adj_prev_2024_pct']} | {y['undiagnosed_2024_pct']} | {y['page']} | {x['prev_both_2014']:.1f} |\n")
A(f"""
Контроль парсера: разобрано {len(c)} стран/территорий (Атлас: "this edition presents data for 215 countries and territories", стр. 28 PDF); сумма по странам {c['n_adults_1000s_2024'].sum()/1000:.1f} млн против мирового значения Table 3.4 — 588.7 млн; Топ-10 по числу и по age-adjusted prevalence из разобранной таблицы совпадают с Table 3.4 и Table 3.5 Атласа (стр. 52-53 PDF).

### 7.2 IDF 10th edition (2021) — фрагменты страновых таблиц NCBI Bookshelf (файл `a2_idf10_fragments.csv`)

Индекс Firecrawl отдаёт страницы таблиц NCBI только фрагментами по ~200 символов; извлечены только строки, попавшие во фрагменты. Колонки таблицы 10-й редакции: "Number of adults 20–79 years with diabetes (1,000s) (95% CI)", "Diabetes prevalence (%) in adults 20–79 years (95% CI)". Пустая ячейка = число не попало во фрагмент (НЕ извлечено).

| Страна | Число взрослых 20-79 с диабетом 2021, тыс. (95% CI) | Prevalence 2021, % (95% CI) | Число 2024 (11th), тыс. | Разница 2024−2021, тыс. | Разница, % | Дословный фрагмент | URL |
|---|---|---|---|---|---|---|---|
""")
for _, f in fr.iterrows():
    nm = f['country'].replace(' (region)', '')
    y = idf[idf['country_idf'] == nm]
    if nm == 'MENA': y = idf[idf['country_idf'] == 'MENA']
    n24 = f"{y.iloc[0]['n_adults_1000s_2024']:,.1f}" if len(y) else '—'
    d = (y.iloc[0]['n_adults_1000s_2024'] - f['n_adults_1000s_2021']) if len(y) else None
    dd = f"{d:+,.1f}" if d is not None else '—'; dp = f"{d/f['n_adults_1000s_2021']*100:+.1f}" if d is not None else '—'
    prev = f"{f['prev_2021_pct']} ({f['prev_ci_2021']})" if pd.notna(f['prev_2021_pct']) and pd.notna(f['prev_ci_2021']) else (f"{f['prev_2021_pct']}" if pd.notna(f['prev_2021_pct']) else '')
    A(f"| {f['country']} | {f['n_adults_1000s_2021']:,.1f} ({f['n_ci_2021']}) | {prev} | {n24} | {dd} | {dp} | \"{f['verbatim_fragment']}\" | {f['source_url']} |\n")
A("""
Глобально (10th ed., абстракт PMC11057359, дословно): "The global diabetes prevalence in 20-79 year olds in 2021 was estimated to be 10.5% (536.6 million people), rising to 12.2% (783.2 million) in 2045". 11th ed. (Table 3.4, стр. 52 PDF): World 2024 — 588.7 млн, prevalence 11.1%; 2050 — 852.5 млн (прогноз). Разница оценок 2021→2024: +52.1 млн (+9.7%) — с оговоркой (б).

### 7.3 Топ-10 стран по числу взрослых 20-79 с диабетом — IDF 11th edition, Table 3.4 (стр. 52 PDF; 2050 — прогноз IDF)

| Место 2024 | Страна | Число 2024, млн | Место 2050 (прогноз) | Страна | Число 2050, млн (прогноз) |
|---|---|---|---|---|---|
| 1 | China | 148.0 | 1 | China | 168.3 |
| 2 | India | 89.8 | 2 | India | 156.7 |
| 3 | United States of America | 38.5 | 3 | Pakistan | 70.2 |
| 4 | Pakistan | 34.5 | 4 | United States of America | 43.0 |
| 5 | Indonesia | 20.4 | 5 | Indonesia | 28.6 |
| 6 | Brazil | 16.6 | 6 | Egypt | 24.7 |
| 7 | Bangladesh | 13.9 | 7 | Brazil | 24.0 |
| 8 | Mexico | 13.6 | 8 | Bangladesh | 23.1 |
| 9 | Egypt | 13.2 | 9 | Mexico | 19.9 |
| 10 | Japan | 10.8 | 10 | Turkey | 14.1 |

Из Топ-8 основного рейтинга A2 в этот список входит только Egypt (9-е место 2024 → 6-е место 2050 по прогнозу IDF). Table 3.5 (стр. 53): Топ-3 по age-standardised prevalence 2024 — Pakistan 31.4%, Marshall Islands 25.7%, Kuwait 25.6%; Egypt — 9-е (22.4%), Saudi Arabia — 7-е (23.1%). Таблица "Топ по приросту числа людей" по всем странам между редакциями НЕ построена: страновые таблицы 10-й редакции извлечены лишь фрагментарно (см. 7.2 и раздел 10).
""")
open(f'{D}/a2_report_part2.md', 'w', encoding='utf-8').write(''.join(T))
print('part2 written', len(''.join(T)))
