#!/usr/bin/env python3
"""Generate markdown tables for A2 report from a2_*.csv (run after a2_diabetes_trend.py)."""
import pandas as pd, re
D = '/home/user/research/research/_work/data'
full = pd.read_csv(f'{D}/a2_full_table.csv')
idf = pd.read_csv(f'{D}/a2_idf11_country_2024.csv')
main = full[full['in_main_ranking']].sort_values('abs_change_pp_both', ascending=False).reset_index(drop=True)
main['rank'] = main.index + 1
def r(x, n=2): return f'{x:.{n}f}'
def pop_m(x): return f'{x/1e6:.1f}'
print('## Top-12 abs\n')
print('| # | Страна | 2004 оба пола, % | 2014 оба пола, % | 2004 men / women, % | 2014 men / women, % | Δ п.п. | Δ отн., % | п.п./год | Население 2023, млн | Ранг по отн. |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for _, x in main.head(12).iterrows():
    print(f"| {x['rank']} | {x['country']} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {r(x['prev_men_2004'])} / {r(x['prev_women_2004'])} | {r(x['prev_men_2014'])} / {r(x['prev_women_2014'])} | {r(x['abs_change_pp_both'])} | {r(x['rel_change_pct_both'],1)} | {r(x['pp_per_year_both'])} | {pop_m(x['pop_2023'])} | {int(x['rank_rel_main'])} |")
print('\n## Top-8 abs with 95% UI (2014)\n')
print('| # | Страна | Men 2004 (95% UI) | Men 2014 (95% UI) | Women 2004 (95% UI) | Women 2014 (95% UI) |')
print('|---|---|---|---|---|---|')
for _, x in main.head(8).iterrows():
    print(f"| {x['rank']} | {x['country']} | {r(x['prev_men_2004'],1)} ({r(x['lo_men_2004'],1)}-{r(x['hi_men_2004'],1)}) | {r(x['prev_men_2014'],1)} ({r(x['lo_men_2014'],1)}-{r(x['hi_men_2014'],1)}) | {r(x['prev_women_2004'],1)} ({r(x['lo_women_2004'],1)}-{r(x['hi_women_2004'],1)}) | {r(x['prev_women_2014'],1)} ({r(x['lo_women_2014'],1)}-{r(x['hi_women_2014'],1)}) |")
rel = full[full['in_main_ranking']].sort_values('rel_change_pct_both', ascending=False).reset_index(drop=True)
print('\n## Top-8 rel\n')
print('| # | Страна | 2004 оба пола, % | 2014 оба пола, % | Δ п.п. | Δ отн., % | п.п./год | Население 2023, млн | Ранг по абс. |')
print('|---|---|---|---|---|---|---|---|---|')
for i, x in rel.head(8).iterrows():
    print(f"| {i+1} | {x['country']} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {r(x['abs_change_pp_both'])} | {r(x['rel_change_pct_both'],1)} | {r(x['pp_per_year_both'])} | {pop_m(x['pop_2023'])} | {int(x['rank_abs_main'])} |")
print('\n## Small states\n')
sm = pd.read_csv(f'{D}/a2_small_states.csv')
print('| Страна | Население 2023 | 2004, % | 2014, % | Δ п.п. | Δ отн., % | Ранг среди всех членов ООН без фильтра | Ранг среди всех 200 |')
print('|---|---|---|---|---|---|---|---|')
for _, x in sm.iterrows():
    print(f"| {x['country']} | {int(x['pop_2023']):,} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {r(x['abs_change_pp_both'])} | {r(x['rel_change_pct_both'],1)} | {int(x['rank_abs_un_all'])} | {int(x['rank_abs_all200'])} |")
print('\n## Excluded\n')
ex = pd.read_csv(f'{D}/a2_excluded_non_un.csv')
print('| Страна/территория | Статус | Население 2023 | 2004, % | 2014, % | Δ п.п. | Ранг среди всех 200 |')
print('|---|---|---|---|---|---|---|')
for _, x in ex.iterrows():
    p = 'нет в World Bank' if pd.isna(x['pop_2023']) else f"{int(x['pop_2023']):,}"
    print(f"| {x['country']} | {x['exclusion_note']} | {p} | {r(x['prev_both_2004'])} | {r(x['prev_both_2014'])} | {r(x['abs_change_pp_both'])} | {int(x['rank_abs_all200'])} |")
# UN members with pop>=5M ranked 1..8 after excluding — also who would be in top-8 among all UN members
print('\n## UN members (any pop) top-12 by abs\n')
unall = full[full['is_un_member']].sort_values('abs_change_pp_both', ascending=False).head(12)
for i, x in unall.iterrows(): print(x['country'], r(x['abs_change_pp_both']), int(x['pop_2023']))
# IDF 11th for top-8 + top 12
print('\n## IDF 11th 2024 for Top-12 (+ near)\n')
mp = {'Iran': 'Iran (Islamic Republic of)', 'Turkey': 'Türkiye'}
print('| Страна | Число взрослых 20-79 с диабетом 2024, тыс. | Prevalence 20-79 2024, % | Age-adjusted comparative prevalence 2024, % | Недиагностировано, % | стр. PDF |')
print('|---|---|---|---|---|---|')
for _, x in main.head(12).iterrows():
    n = mp.get(x['country'], x['country'])
    y = idf[idf['country_idf'] == n]
    assert len(y) == 1, n
    y = y.iloc[0]
    print(f"| {x['country']} | {y['n_adults_1000s_2024']:,.1f} | {y['prev_2024_pct']} | {y['age_adj_prev_2024_pct']} | {y['undiagnosed_2024_pct']} | {y['page']} |")
# IDF top 15 countries by number 2024
c = idf[~idf['country_idf'].isin(['AFR','EUR','MENA','NAC','SACA','SEA','WP'])]
print('\nIDF countries parsed:', len(c), ' sum n (1000s):', c['n_adults_1000s_2024'].sum())
print(c.sort_values('n_adults_1000s_2024', ascending=False).head(12)[['country_idf','n_adults_1000s_2024','prev_2024_pct','age_adj_prev_2024_pct']].to_string(index=False))
print(c.sort_values('age_adj_prev_2024_pct', ascending=False).head(10)[['country_idf','n_adults_1000s_2024','prev_2024_pct','age_adj_prev_2024_pct']].to_string(index=False))
