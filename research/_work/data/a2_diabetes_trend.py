#!/usr/bin/env python3
"""A2 diabetes-trend: ranking of countries by growth of age-standardised diabetes prevalence
(NCD-RisC Lancet 2016 file, window 2004 -> 2014), per research/_work/00_definitions.md section 2.2.
Outputs CSVs research/_work/data/a2_*.csv. Run: python3 a2_diabetes_trend.py
"""
import re, sys
import pandas as pd
import numpy as np

W = '/home/user/research/research/_work'
DM_FILE = f'{W}/mirrors/ncdrisc_tableau/NCD_RisC_Lancet_2016_DM_age_standardised_countries.csv'
POP_FILE = f'{W}/mirrors/population/data/population.csv'
CL_FILE = f'{W}/mirrors/ncdrisc/data-raw/country-list-2025.csv'
UN_FILE = f'{W}/data/un_member_states_a2.csv'
IDF11_TXT = f'{W}/data/IDF_Diabetes_Atlas_11th_Edition_2025_WEB.txt'
OUT = f'{W}/data'
Y0, Y1 = 2004, 2014
POP_MIN = 5_000_000

# ---------- 1. NCD-RisC 2016 file: 2004 and 2014 values, changes ----------
dm = pd.read_csv(DM_FILE)
dm.columns = ['country', 'iso', 'sex', 'year', 'prev', 'lo', 'hi']
assert dm['iso'].nunique() == 200 and set(dm['sex']) == {'Men', 'Women'}
sub = dm[dm['year'].isin([Y0, Y1])].copy()
for c in ['prev', 'lo', 'hi']:
    sub[c] = sub[c] * 100.0  # share -> percent
wide = sub.pivot_table(index=['country', 'iso'], columns=['sex', 'year'], values=['prev', 'lo', 'hi'])
wide.columns = [f'{v}_{s.lower()}_{y}' for v, s, y in wide.columns]
wide = wide.reset_index()
for y in (Y0, Y1):
    # ASSUMPTION (00_definitions 2.2): both sexes = simple mean of Men and Women
    wide[f'prev_both_{y}'] = (wide[f'prev_men_{y}'] + wide[f'prev_women_{y}']) / 2.0
for s in ('both', 'men', 'women'):
    wide[f'abs_change_pp_{s}'] = wide[f'prev_{s}_{Y1}'] - wide[f'prev_{s}_{Y0}']
    wide[f'rel_change_pct_{s}'] = wide[f'abs_change_pp_{s}'] / wide[f'prev_{s}_{Y0}'] * 100.0
    wide[f'pp_per_year_{s}'] = wide[f'abs_change_pp_{s}'] / (Y1 - Y0)

# ---------- 2. population (World Bank 2023), UN membership, NCD-RisC region ----------
pop = pd.read_csv(POP_FILE)
pop23 = pop[pop['Year'] == 2023][['Country Code', 'Value']].rename(columns={'Country Code': 'iso', 'Value': 'pop_2023'})
wide = wide.merge(pop23, on='iso', how='left')
cl = pd.read_csv(CL_FILE, encoding='latin-1')[['iso', 'Region', 'Superregion']]
wide = wide.merge(cl, on='iso', how='left')

un = pd.read_csv(UN_FILE)
un_names = set(un['member_state'])
# explicit mapping NCD-RisC country name -> name in UN member list (Wikipedia, accessed 2026-09-04)
NAME_MAP = {
    'Bahamas': 'Bahamas, The', 'Brunei Darussalam': 'Brunei', "Cote d'Ivoire": "Côte d'Ivoire",
    'Czech Republic': 'Czechia', 'DR Congo': 'Democratic Republic of the Congo',
    'Gambia': 'Gambia (Republic of The)', 'Guinea Bissau': 'Guinea-Bissau',
    'Iran': 'Iran (Islamic Republic of)', 'Lao PDR': "Lao People's Democratic Republic",
    'Macedonia (TFYR)': 'North Macedonia', 'Moldova': 'Republic of Moldova', 'Nauru': 'Naoero',
    'North Korea': "Democratic People's Republic of Korea", 'South Korea': 'Republic of Korea',
    'Swaziland': 'Eswatini', 'Tanzania': 'United Republic of Tanzania', 'Turkey': 'Türkiye',
    'United Kingdom': 'United Kingdom of Great Britain and Northern Ireland',
    'Venezuela': 'Venezuela (Bolivarian Republic of)', 'Viet Nam': 'Vietnam',
}
NON_UN_NOTE = {  # NCD-RisC entities that are not UN member states
    'American Samoa': 'territory (USA)', 'Bermuda': 'territory (UK)', 'China (Hong Kong SAR)': 'SAR of China',
    'Cook Islands': 'associated state (NZ), not UN member', 'French Polynesia': 'territory (France)',
    'Greenland': 'territory (Denmark)', 'Niue': 'associated state (NZ), not UN member',
    'Occupied Palestinian Territory': 'UN observer state, not member', 'Puerto Rico': 'territory (USA)',
    'Taiwan': 'not UN member', 'Tokelau': 'territory (NZ)',
}
wide['un_name'] = wide['country'].map(lambda c: NAME_MAP.get(c, c))
wide['is_un_member'] = wide['un_name'].isin(un_names)
wide['exclusion_note'] = wide['country'].map(NON_UN_NOTE)
unmatched = wide[~wide['is_un_member'] & wide['exclusion_note'].isna()]
assert unmatched.empty, unmatched[['country']]
missing_un = sorted(un_names - set(wide['un_name']))
print('UN members absent from NCD-RisC file:', missing_un)

wide['pop_ge_5m'] = wide['pop_2023'] >= POP_MIN
wide['in_main_ranking'] = wide['is_un_member'] & wide['pop_ge_5m']
# ranks
wide['rank_abs_all200'] = wide['abs_change_pp_both'].rank(ascending=False, method='min').astype(int)
wide['rank_abs_un_all'] = wide.loc[wide['is_un_member'], 'abs_change_pp_both'].rank(ascending=False, method='min')
wide['rank_abs_main'] = wide.loc[wide['in_main_ranking'], 'abs_change_pp_both'].rank(ascending=False, method='min')
wide['rank_rel_main'] = wide.loc[wide['in_main_ranking'], 'rel_change_pct_both'].rank(ascending=False, method='min')

cols_order = ['country', 'iso', 'Region', 'Superregion', 'un_name', 'is_un_member', 'exclusion_note', 'pop_2023', 'pop_ge_5m', 'in_main_ranking',
              f'prev_men_{Y0}', f'lo_men_{Y0}', f'hi_men_{Y0}', f'prev_women_{Y0}', f'lo_women_{Y0}', f'hi_women_{Y0}', f'prev_both_{Y0}',
              f'prev_men_{Y1}', f'lo_men_{Y1}', f'hi_men_{Y1}', f'prev_women_{Y1}', f'lo_women_{Y1}', f'hi_women_{Y1}', f'prev_both_{Y1}',
              'abs_change_pp_both', 'rel_change_pct_both', 'pp_per_year_both',
              'abs_change_pp_men', 'rel_change_pct_men', 'pp_per_year_men',
              'abs_change_pp_women', 'rel_change_pct_women', 'pp_per_year_women',
              'rank_abs_all200', 'rank_abs_un_all', 'rank_abs_main', 'rank_rel_main']
full = wide[cols_order].sort_values('abs_change_pp_both', ascending=False)
full.to_csv(f'{OUT}/a2_full_table.csv', index=False, float_format='%.6f')
print('a2_full_table.csv rows:', len(full), '| main ranking rows:', int(full['in_main_ranking'].sum()))

main = full[full['in_main_ranking']].copy()
top_abs = main.sort_values('abs_change_pp_both', ascending=False).head(12)
top_abs.to_csv(f'{OUT}/a2_top12_abs.csv', index=False, float_format='%.4f')
top_rel = main.sort_values('rel_change_pct_both', ascending=False).head(12)
top_rel.to_csv(f'{OUT}/a2_top12_rel.csv', index=False, float_format='%.4f')

# small UN member states (<5M) that would enter Top-5 of the UN-member ranking without population filter
small = full[full['is_un_member'] & ~full['pop_ge_5m'] & (full['rank_abs_un_all'] <= 5)]
small.to_csv(f'{OUT}/a2_small_states.csv', index=False, float_format='%.4f')
# excluded non-UN entities with what their rank would have been among all 200
excl = full[~full['is_un_member']].sort_values('abs_change_pp_both', ascending=False)
excl.to_csv(f'{OUT}/a2_excluded_non_un.csv', index=False, float_format='%.4f')
# UN members with missing population
print('UN members without WB 2023 population:', full[full['is_un_member'] & full['pop_2023'].isna()]['country'].tolist())

def fmt(df, n=None):
    d = df if n is None else df.head(n)
    out = d[['country', 'pop_2023', f'prev_both_{Y0}', f'prev_both_{Y1}', 'abs_change_pp_both', 'rel_change_pct_both', 'pp_per_year_both',
             f'prev_men_{Y0}', f'prev_men_{Y1}', f'prev_women_{Y0}', f'prev_women_{Y1}', 'rank_abs_main', 'rank_rel_main', 'rank_abs_all200']].copy()
    return out.to_string(index=False, float_format=lambda x: f'{x:.2f}')

print('\n=== TOP-12 by absolute change (pp), UN members, pop>=5M ===')
print(fmt(top_abs))
print('\n=== TOP-12 by relative change (%), UN members, pop>=5M ===')
print(fmt(top_rel))
print('\n=== Small states (<5M) that would be in Top-5 of UN-member ranking ===')
print(fmt(small))
print('\n=== Excluded non-UN entities ===')
print(fmt(excl))
# sanity: both-sexes mean vs sexes
print('\nWorld-level check (simple mean of 200 countries, unweighted):', full[f'prev_both_{Y0}'].mean().round(2), full[f'prev_both_{Y1}'].mean().round(2))

# ---------- 3. IDF Diabetes Atlas 11th edition (2025): country summary tables, 2024 ----------
txt = open(IDF11_TXT, encoding='utf-8').read()
pages = re.split(r'=== PAGE (\d+) ===', txt)
page = {int(pages[i]): pages[i + 1] for i in range(1, len(pages), 2)}
NUM = re.compile(r'^-?[\d,]+(\.\d+)?$')
REGION_CODES = {'AFR', 'EUR', 'MENA', 'NAC', 'SACA', 'SEA', 'WP'}
rows = []
for p in [107, 109, 111, 113, 115, 117, 119, 121]:
    t = page[p]
    k = t.find('(20–79 years), %')
    assert k > 0, p
    body = t[k + len('(20–79 years), %'):]
    lines = [l.strip() for l in body.split('\n') if l.strip()]
    region = None; i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('Country summary in') or l.startswith('IDF Diabetes Atlas') or re.match(r'^\d+\s+\|', l) or l == '2024':
            i += 1; continue
        if NUM.match(l):
            print('WARN stray number', p, l); i += 1; continue
        name = l
        vals = lines[i + 1:i + 5]
        if len(vals) == 4 and all(NUM.match(v) for v in vals):
            if name in REGION_CODES:
                region = name
            foot = ''
            m = re.match(r'^(.*?[a-z\)])(i{1,3})$', name)
            # footnote marker 'i' glued to the name (e.g. 'Qatari'): only strip if the stripped name is not itself a known word ending
            if m and name not in ('Mali', 'Burundi', 'Malawi', 'Fiji', 'Haiti', 'Djibouti', 'Brunei Darussalam', 'Kiribati', 'Saudi', 'Eswatini'):
                name, foot = m.group(1), m.group(2)
            f = lambda v: float(v.replace(',', ''))
            rows.append({'idf_region': region, 'country_idf': name, 'footnote': foot, 'n_adults_1000s_2024': f(vals[0]),
                         'prev_2024_pct': f(vals[1]), 'age_adj_prev_2024_pct': f(vals[2]), 'undiagnosed_2024_pct': f(vals[3]), 'page': p})
            i += 5
        else:
            # multi-line name: join with next line
            if i + 1 < len(lines) and not NUM.match(lines[i + 1]):
                lines[i + 1] = name + ' ' + lines[i + 1]; i += 1; continue
            print('WARN unparsed', p, name, vals); i += 1
idf11 = pd.DataFrame(rows)
idf11.to_csv(f'{OUT}/a2_idf11_country_2024.csv', index=False)
print('\nIDF 11th parsed rows:', len(idf11), '| regions:', idf11[idf11['country_idf'].isin(REGION_CODES)]['country_idf'].tolist())
print('IDF 11th region totals sum (1000s):', idf11[idf11['country_idf'].isin(REGION_CODES)]['n_adults_1000s_2024'].sum())
print(idf11[idf11['footnote'] != ''][['country_idf', 'footnote']].head(20).to_string(index=False))

# ---------- 4. Integrity check of the GitHub mirror vs. published NCD-RisC 2016 global figures ----------
# Published (PMC5081106 abstract, opened 2026-09-04 via firecrawl_research_search_papers): global age-standardised
# diabetes prevalence men 4.3% (1980) -> 9.0% (2014); women 5.0% (1980) -> 7.9% (2014).
# The mirror file has no World row, so we approximate the global value as the World Bank total-population-weighted
# mean of the 200 country values (weights = total population of the same year; adult population not available).
chk = []
for y in (1980, 2014):
    py = pop[pop['Year'] == y][['Country Code', 'Value']].rename(columns={'Country Code': 'iso', 'Value': 'w'})
    for s in ('Men', 'Women'):
        d = dm[(dm['year'] == y) & (dm['sex'] == s)].merge(py, on='iso', how='inner')
        chk.append({'year': y, 'sex': s, 'n_countries_with_pop': len(d), 'pop_weighted_mean_pct': round(float(np.average(d['prev'], weights=d['w']) * 100), 2),
                    'unweighted_mean_pct': round(float(d['prev'].mean() * 100), 2), 'min_pct': round(float(d['prev'].min() * 100), 2), 'max_pct': round(float(d['prev'].max() * 100), 2),
                    'published_ncdrisc_2016_pct': {(1980, 'Men'): 4.3, (1980, 'Women'): 5.0, (2014, 'Men'): 9.0, (2014, 'Women'): 7.9}[(y, s)]})
chk = pd.DataFrame(chk)
chk.to_csv(f'{OUT}/a2_integrity_check.csv', index=False)
print('\n=== Integrity check (mirror vs published global) ===')
print(chk.to_string(index=False))
top14 = dm[dm['year'] == 2014].sort_values('prev', ascending=False).head(6)[['country', 'sex', 'prev']]
top14['prev'] = (top14['prev'] * 100).round(1)
print('Highest 2014 values in file:\n', top14.to_string(index=False))
