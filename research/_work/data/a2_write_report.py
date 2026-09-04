#!/usr/bin/env python3
"""Assemble research/_work/wave1/A2_diabetes_trend.md from a2_*.csv outputs (all numbers come from the CSVs)."""
import pandas as pd, json, os
D = '/home/user/research/research/_work/data'
OUTMD = '/home/user/research/research/_work/wave1/A2_diabetes_trend.md'
full = pd.read_csv(f'{D}/a2_full_table.csv')
idf = pd.read_csv(f'{D}/a2_idf11_country_2024.csv')
chk = pd.read_csv(f'{D}/a2_integrity_check.csv')
main = full[full['in_main_ranking']].sort_values('abs_change_pp_both', ascending=False).reset_index(drop=True)
main['rank'] = main.index + 1
rel = full[full['in_main_ranking']].sort_values('rel_change_pct_both', ascending=False).reset_index(drop=True)
sm = pd.read_csv(f'{D}/a2_small_states.csv'); ex = pd.read_csv(f'{D}/a2_excluded_non_un.csv')
def r(x, n=2): return f'{x:.{n}f}'
def pm(x): return f'{x/1e6:.1f}'
T = []  # markdown chunks
A = T.append
n_main = int(full['in_main_ranking'].sum()); n_un = int(full['is_un_member'].sum())
top8 = main.head(8)
A(f"""# A2 — Диабет: рейтинг стран по росту распространённости (NCD-RisC 2016, окно 2004 → 2014)

Сборщик: data-analyst (A2). Дата доступа ко всем источникам: 2026-09-04. Определения: `research/_work/00_definitions.md`, раздел 2.2. Скрипты: `research/_work/data/a2_diabetes_trend.py` (расчёт), `a2_make_tables.py`, `a2_write_report.py` (сборка этого файла). Промежуточные CSV: `research/_work/data/a2_*.csv`. Все числа ниже — из вывода скриптов.

## 0. Резюме

- Метрика: распространённость диабета среди взрослых (18+), age-standardised, оба пола (= простое среднее Men/Women), %. Источник: NCD-RisC, "Worldwide trends in diabetes since 1980" (Lancet 2016), файл `mirrors/ncdrisc_tableau/NCD_RisC_Lancet_2016_DM_age_standardised_countries.csv` (200 стран, 1980-2014). Окно: 2004 → 2014.
- Фильтр основного рейтинга: члены ООН (193, список открыт через Firecrawl со страницы Wikipedia "Member states of the United Nations") с населением >= 5 000 000 (World Bank 2023). В основной рейтинг вошло {n_main} стран (из {n_un} членов ООН, присутствующих в файле NCD-RisC).
- **Топ-5 по абсолютному приросту (п.п., 2004→2014):** {', '.join(f"{x['country']} (+{r(x['abs_change_pp_both'])})" for _, x in main.head(5).iterrows())}. Места 6-8: {', '.join(f"{x['country']} (+{r(x['abs_change_pp_both'])})" for _, x in main.iloc[5:8].iterrows())}.
- Топ-5 по относительному росту (%): {', '.join(f"{x['country']} (+{r(x['rel_change_pct_both'],1)}%)" for _, x in rel.head(5).iterrows())}.
- Разрывы между соседями в Топ-8 малы (0.01-0.5 п.п.), а 95% интервалы неопределённости NCD-RisC для этих стран широкие (см. таблицу 2.1) — порядок мест внутри Топ-8 статистически не различим; это наша оценка, а не утверждение источника.
- Вторичная колонка IDF (взрослые 20-79, число людей с диабетом, редакции 2021 → 2024; НЕ тренд — методология менялась): Egypt +2,283.8 тыс. (+20.9%), Iraq +658.0 (+32.7%), Morocco +553.3 (+23.8%), Azerbaijan +318.2 (+80.1%), Papua New Guinea +114.0 (+15.7%), Yemen +106.9 (+17.4%), Lebanon +43.6 (+11.0%), Turkmenistan +40.4 (+18.1%). Из Топ-8 только Egypt входит в IDF Топ-10 по числу людей (10.9 млн в 2021, 13.2 млн в 2024).
- Перепроверка уровня 2014 независимыми открытыми источниками (IDF 11th/10th, абстракты PMC): подтверждён для Egypt, Morocco (HIGH), Iraq, Lebanon, Papua New Guinea (MEDIUM); для Turkmenistan, Yemen, Azerbaijan IDF даёт существенно более низкие значения, национальные STEPS-опросы не открылись — LOW. Страновые значения «версии 2022» (NCD-RisC 2024) для Топ-8 не найдены — UNVERIFIED.
- Целостность зеркала (GitHub) проверена: популяционно-взвешенное среднее по 200 странам файла за 2014 = {chk[(chk.year==2014)&(chk.sex=='Men')]['pop_weighted_mean_pct'].iloc[0]}% (men) / {chk[(chk.year==2014)&(chk.sex=='Women')]['pop_weighted_mean_pct'].iloc[0]}% (women) против опубликованных 9.0% / 7.9% (абстракт PMC5081106); максимум 2014 в файле — American Samoa ({r(full[full.country=='American Samoa']['prev_women_2014'].iloc[0],1)}% women), что совпадает с абстрактом ("American Samoa had the highest national prevalence of diabetes (>30%").

## 1. Источники и допущения

| # | Источник | Что взято | Уровень | Как открыт | Примечание |
|---|---|---|---|---|---|
| S1 | NCD-RisC, "Worldwide trends in diabetes since 1980: a pooled analysis of 751 population-based studies with 4.4 million participants", Lancet 2016; doi:10.1016/S0140-6736(16)00618-8; PMC5081106 | Страновой файл age-standardised diabetes prevalence, Men/Women, 1980-2014, 200 стран (+95% UI) | T1 (зеркало на GitHub: github.com/banerjeemdx/Data-Visualisation-with-Tableau---NCD_RisC-dataset-on-BMI-Body-Mass-index-Diabetes-and-Blood-Pre, commit b76316c; см. `mirrors/PROVENANCE.md`) | файл в сессии; абстракт статьи — firecrawl_research_search_papers / inspect_paper | Проверка целостности зеркала — раздел 1.1 |
| S2 | World Bank population (datahub mirror github.com/datasets/population, commit 075cd0d) | Население 2023 по ISO3 | T1 (зеркало) | файл `mirrors/population/data/population.csv` | Нет значений для COK, NIU, TKL, TWN (не члены ООН — на рейтинг не влияет) |
| S3 | Wikipedia, "Member states of the United Nations", https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations | Список 193 членов ООН (таблица "Current members") | T3 (список сверен с файлом параллельного агента A1 `data/un_member_states.csv`: 193 = 193, расхождений нет) | mcp__Firecrawl__firecrawl_search, 2026-09-04; сохранено в `data/un_member_states_a2.csv` | Используется только как фильтр членства |
| S4 | NCD-RisC country list (github.com/NCD-RisC/ncdrisc, data-raw/country-list-2025.csv) | Регион/суперрегион NCD-RisC | T1 (зеркало) | файл в сессии | Только для справочных колонок |
| S5 | IDF Diabetes Atlas, 11th edition (2025), PDF с official IDF S3 bucket (international-diabetes-federation.s3.eu-west-1.amazonaws.com/media/uploads/sites/3/2025/10/IDF_Diabetes_Atlas_11th_Edition_2025_WEB.pdf) | Страновые таблицы (стр. 107-121 PDF): число взрослых 20-79 с диабетом 2024 (тыс.), prevalence, age-adjusted comparative prevalence, доля недиагностированных; Table 3.4/3.5 (стр. 52-53) | T1 | curl S3 (скачан ранее), текст `data/IDF_Diabetes_Atlas_11th_Edition_2025_WEB.txt`; парсер в `a2_diabetes_trend.py` (разобрано 215 стран/территорий + 7 регионов; сумма по странам 588.7 млн = мировое значение Атласа 588.7 млн; Топ-10 по числу и по age-adj prevalence совпали с Table 3.4/3.5) | Возраст 20-79, методология IDF (не сопоставимо с NCD-RisC 18+) |
| S6 | IDF Diabetes Atlas, 10th edition (2021), NCBI Bookshelf, "Country summary tables" https://www.ncbi.nlm.nih.gov/books/n/idfatlas10e/appendices.s1/ (таблицы: https://www.ncbi.nlm.nih.gov/books/NBK582202/table/appendices.tu3/ и др.) | Число взрослых 20-79 с диабетом 2021 и prevalence по странам (фрагменты) | T1 | mcp__Firecrawl__firecrawl_search (site:-запросы; индекс отдаёт только ~200-символьные фрагменты таблицы) | Число людей 2021 извлечено для всех 8 стран Топ-8 (+7 других), prevalence 2021 — для 4 из 8; полная таблица 215 стран не извлечена (раздел 7.2, U4-U5) |
| S7 | Sun H. et al., "IDF Diabetes Atlas: Global, regional and country-level diabetes prevalence estimates for 2021 and projections for 2045", Diabetes Res Clin Pract 2022, PMC11057359 | Глобальные числа 2021 (10th ed.) | T1 (абстракт) | firecrawl_research_search_papers | Полный текст в индексе отсутствует |
| S8 | NCD-RisC, "Worldwide trends in diabetes prevalence and treatment from 1990 to 2022", Lancet 2024, doi:10.1016/S0140-6736(24)02317-1, PMC7616842 | Глобальные значения 2022 (справка "версия 2022") | T1 (абстракт) | firecrawl_research_inspect_paper / search_papers | Полный текст в индексе отсутствует; страновых значений 2022 в абстракте нет |
| S9 | WHO news release 13.11.2024 "Urgent action needed as global diabetes cases increase four-fold over past decades", https://www.who.int/news/item/13-11-2024-urgent-action-needed-as-global-diabetes-cases-increase-four-fold-over-past-decades | Глобальные/региональные значения 2022 (справка) | T1 | mcp__Firecrawl__firecrawl_search (полный текст страницы получен) | Страновых значений нет |
| S10 | Статьи PubMed/PMC по отдельным странам (см. раздел 8) | Независимые оценки распространённости для перепроверки Топ-8 | T1 (абстракты) | firecrawl_research_search_papers | Полные тексты в индексе отсутствуют — цитируются только абстракты |

Допущения и ограничения (фиксируются в Методологии):

1. **Оба пола = простое среднее Men и Women.** Файл NCD-RisC 2016 не содержит both-sexes. Отклонение от популяционно-взвешенного значения мало при соотношении полов ~1:1; для стран с сильно смещённой половой структурой (Qatar, UAE, Kuwait и др.) простое среднее может отличаться от «истинного» both-sexes — в Топ-8 таких стран нет.
2. Age-standardised (к стандартной популяции WHO, как в NCD-RisC), взрослые 18+. Значения в файле — доли (0-1), переведены в проценты.
3. Окно 2004→2014 — последние 10 лет данных источника. Абсолютное изменение = п.п.; относительное = (2014-2004)/2004*100; среднегодовой прирост = п.п./10.
4. Фильтр членства ООН — по названию с явной таблицей соответствий (NAME_MAP в скрипте). В файле NCD-RisC отсутствуют 4 члена ООН: Liechtenstein, Monaco, San Marino, South Sudan (все < 5 млн, кроме South Sudan — но South Sudan данных нет; отмечено как пробел). Kosovo в файле отсутствует.
5. Население World Bank 2023 (последний год файла) — как в 2.1; фильтр >= 5 000 000.
6. Файл NCD-RisC 2024 (1990-2022) и WHO GHO в сессии недоступны (ncdrisc.org, who.int/data заблокированы) — основной рейтинг построен на версии 2016 (данные до 2014). Это главное ограничение блока.
7. Мировой ряд в файле отсутствует; проверка целостности зеркала — через популяционно-взвешенное среднее (веса — общее население World Bank того же года, а не взрослое), см. 1.1.

### 1.1 Проверка целостности зеркала NCD-RisC (файл `a2_integrity_check.csv`)

| Год | Пол | Стран с населением WB | Взвешенное среднее по файлу, % | Невзвешенное среднее, % | Опубликовано NCD-RisC 2016 (абстракт PMC5081106), % |
|---|---|---|---|---|---|
""")
for _, x in chk.iterrows():
    A(f"| {x['year']} | {x['sex']} | {x['n_countries_with_pop']} | {x['pop_weighted_mean_pct']} | {x['unweighted_mean_pct']} | {x['published_ncdrisc_2016_pct']} |\n")
A(f"""
Дословно из абстракта (PMC5081106, открыт через firecrawl_research_search_papers): "Global age-standardised diabetes prevalence increased from 4.3% (95% credible interval 2.4-7.0) in 1980 to 9.0% (7.2-11.1) in 2014 in men, and from 5.0% (2.9-7.9) to 7.9% (6.4-9.7) in women" и "In 2014, American Samoa had the highest national prevalence of diabetes (>30%". Расхождение взвешенного среднего с опубликованным — не более 0.35 п.п. (веса — общее, а не взрослое население); максимум файла за 2014 — American Samoa ({r(full[full.country=='American Samoa']['prev_men_2014'].iloc[0],1)}% men, {r(full[full.country=='American Samoa']['prev_women_2014'].iloc[0],1)}% women) — согласуется. Вывод: зеркало соответствует опубликованным значениям; уровень источника сохраняется T1 (наша оценка: проверка косвенная, на уровне глобальных агрегатов и максимума).

## 2. Основной рейтинг: Топ-8 по абсолютному изменению (п.п.), члены ООН, население >= 5 млн

Метрика: age-standardised diabetes prevalence, взрослые 18+, оба пола (среднее Men/Women), %. Источник строки данных — S1, строки `Country`, `Sex`, `Year`=2004/2014. Источник населения — S2 (2023). Файл: `a2_top12_abs.csv`.

| Место | Страна | 2004, оба пола, % | 2014, оба пола, % | 2004 men / women, % | 2014 men / women, % | Изменение, п.п. | Относительное, % | п.п./год | Население 2023, млн | Ранг по отн. росту | Регион NCD-RisC |
|---|---|---|---|---|---|---|---|---|---|---|---|
""")
for _, x in top8.iterrows():
    A(f"| {x['rank']} | {x['country']} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {r(x['prev_men_2004'])} / {r(x['prev_women_2004'])} | {r(x['prev_men_2014'])} / {r(x['prev_women_2014'])} | +{r(x['abs_change_pp_both'])} | +{r(x['rel_change_pct_both'],1)} | {r(x['pp_per_year_both'])} | {pm(x['pop_2023'])} | {int(x['rank_rel_main'])} | {x['Region']} |\n")
A("""
### 2.1 Строки данных источника (S1) для Топ-8 — значения по полам с 95% интервалами неопределённости

| Место | Страна | ISO | Men 2004 (95% UI) | Men 2014 (95% UI) | Women 2004 (95% UI) | Women 2014 (95% UI) | Δ men, п.п. | Δ women, п.п. |
|---|---|---|---|---|---|---|---|---|
""")
for _, x in top8.iterrows():
    A(f"| {x['rank']} | {x['country']} | {x['iso']} | {r(x['prev_men_2004'],1)} ({r(x['lo_men_2004'],1)}-{r(x['hi_men_2004'],1)}) | {r(x['prev_men_2014'],1)} ({r(x['lo_men_2014'],1)}-{r(x['hi_men_2014'],1)}) | {r(x['prev_women_2004'],1)} ({r(x['lo_women_2004'],1)}-{r(x['hi_women_2004'],1)}) | {r(x['prev_women_2014'],1)} ({r(x['lo_women_2014'],1)}-{r(x['hi_women_2014'],1)}) | +{r(x['abs_change_pp_men'])} | +{r(x['abs_change_pp_women'])} |\n")
A(f"""
Примечание (наша оценка): 95% интервалы 2014 года шире изменения 2004→2014 у всех восьми стран; NCD-RisC в абстракте статьи 2016 сообщает только глобальные/региональные тренды, поэтому попарные различия внутри Топ-8 не следует интерпретировать как установленный факт.

## 3. Альтернативный рейтинг: Топ-8 по относительному росту (%), те же фильтры

Файл: `a2_top12_rel.csv`.

| Место | Страна | 2004, % | 2014, % | Изменение, п.п. | Относительное, % | п.п./год | Население 2023, млн | Ранг по абс. изменению |
|---|---|---|---|---|---|---|---|---|
""")
for i, x in rel.head(8).iterrows():
    A(f"| {i+1} | {x['country']} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | +{r(x['abs_change_pp_both'])} | +{r(x['rel_change_pct_both'],1)} | {r(x['pp_per_year_both'])} | {pm(x['pop_2023'])} | {int(x['rank_abs_main'])} |\n")
A(f"""
Пересечение двух Топ-8: {', '.join(sorted(set(top8['country']) & set(rel.head(8)['country'])))}. Страны с низкой базой (Uganda, Burundi, Central African Republic) попадают в относительный рейтинг при приросте 1-2 п.п.

## 4. Кто близко: места 6-12 основного рейтинга

| Место | Страна | 2004, % | 2014, % | Изменение, п.п. | Отставание от 5-го места, п.п. | Население 2023, млн |
|---|---|---|---|---|---|---|
""")
fifth = main.loc[4, 'abs_change_pp_both']
for _, x in main.iloc[5:12].iterrows():
    A(f"| {x['rank']} | {x['country']} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | +{r(x['abs_change_pp_both'])} | {r(fifth - x['abs_change_pp_both'])} | {pm(x['pop_2023'])} |\n")
A(f"""
Места 6-8 (Morocco, Yemen, Azerbaijan) отстают от 5-го места (Papua New Guinea, +{r(fifth)}) на {r(fifth-main.loc[5,'abs_change_pp_both'])}-{r(fifth-main.loc[7,'abs_change_pp_both'])} п.п.; места 9-12 (Libya, Saudi Arabia, Syrian Arab Republic, Iran) — на {r(fifth-main.loc[8,'abs_change_pp_both'])}-{r(fifth-main.loc[11,'abs_change_pp_both'])} п.п.

## 5. Малые государства (< 5 млн), которые вошли бы в Топ-5 без фильтра по населению

Ранг считался среди всех {n_un} членов ООН, присутствующих в файле, без фильтра по населению. Файл: `a2_small_states.csv`.

| Страна | Население 2023 | 2004, % | 2014, % | Изменение, п.п. | Относительное, % | Ранг среди членов ООН без фильтра | Ранг среди всех 200 |
|---|---|---|---|---|---|---|---|
""")
for _, x in sm.iterrows():
    A(f"| {x['country']} | {int(x['pop_2023']):,} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | +{r(x['abs_change_pp_both'])} | +{r(x['rel_change_pct_both'],1)} | {int(x['rank_abs_un_all'])} | {int(x['rank_abs_all200'])} |\n")
unall = full[full['is_un_member']].sort_values('abs_change_pp_both', ascending=False).head(12)
A(f"""
Без фильтра по населению Топ-5 членов ООН выглядел бы так: {', '.join(f"{x['country']} (+{r(x['abs_change_pp_both'])})" for _, x in unall.head(5).iterrows())}; Egypt — 5-е место, Iraq — 6-е. Georgia (+{r(full[full.country=='Georgia']['abs_change_pp_both'].iloc[0])}, {int(full[full.country=='Georgia']['pop_2023'].iloc[0]):,} чел.), Qatar (+{r(full[full.country=='Qatar']['abs_change_pp_both'].iloc[0])}), Fiji (+{r(full[full.country=='Fiji']['abs_change_pp_both'].iloc[0])}), Vanuatu (+{r(full[full.country=='Vanuatu']['abs_change_pp_both'].iloc[0])}) — также < 5 млн, но в Топ-5 не попадают.

## 6. Исключённые из рейтинга: территории и не члены ООН (файл `a2_excluded_non_un.csv`)

| Страна/территория (как в файле NCD-RisC) | Причина исключения | Население 2023 (WB) | 2004, % | 2014, % | Изменение, п.п. | Ранг среди всех 200 |
|---|---|---|---|---|---|---|
""")
for _, x in ex.iterrows():
    p = 'нет в файле WB' if pd.isna(x['pop_2023']) else f"{int(x['pop_2023']):,}"
    A(f"| {x['country']} | {x['exclusion_note']} | {p} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {'+' if x['abs_change_pp_both']>=0 else ''}{r(x['abs_change_pp_both'])} | {int(x['rank_abs_all200'])} |\n")
A("""
Tokelau (+5.85 п.п.) — максимальный прирост среди всех 200 записей файла, Occupied Palestinian Territory (+4.28) стояла бы на 2-м месте основного рейтинга по приросту при населении 5.17 млн — исключены по правилу 2.1 (территории / не члены ООН), с пометкой.
""")
open(f'{D}/a2_report_part1.md', 'w', encoding='utf-8').write(''.join(T))
print('part1 written', len(''.join(T)))
