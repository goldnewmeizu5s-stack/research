#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A1 obesity-trend: рейтинг стран по росту распространённости ожирения (определение 2.1 из 00_definitions.md).

Входные файлы (все локальные, скачаны ранее):
  mirrors/obesity/share-of-adults-defined-as-obese.csv          - WHO GHO via OWID, age-std, 18+, both sexes, 1975-2016 (ОСНОВНОЙ)
  mirrors/ncdrisc_tableau/NCD_RisC_Lancet_2017_BMI_age_standardised_country.csv - NCD-RisC 2017, Men/Women (только проверка)
  mirrors/population/data/population.csv                        - World Bank population
  mirrors/ncdrisc/data-raw/country-list-2025.csv                - регионы NCD-RisC
  data/un_member_states.csv                                      - 193 члена ООН (Wikipedia via Firecrawl, 2026-09-04)
  data/World_Obesity_Atlas_2022.txt, World_Obesity_Atlas_2023_Report.txt, World_Obesity_Atlas_2025_rev1.txt - текст PDF WOF

Выходные файлы: data/a1_*.csv
"""
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path('/home/user/research/research/_work')
DATA = ROOT / 'data'
MIR = ROOT / 'mirrors'

Y0, Y1 = 2006, 2016          # окно "последние 10 лет данных источника"
POP_YEAR = 2023
POP_MIN = 5_000_000
INTEGRITY_TOL = 1.5          # п.п.

# ----------------------------------------------------------------------------
# 0. Загрузка
# ----------------------------------------------------------------------------
ob = pd.read_csv(MIR / 'obesity' / 'share-of-adults-defined-as-obese.csv')
ob.columns = ['Entity', 'Code', 'Year', 'obesity_pct']
ob['obesity_pct'] = ob['obesity_pct'].astype(float)

nr = pd.read_csv(MIR / 'ncdrisc_tableau' / 'NCD_RisC_Lancet_2017_BMI_age_standardised_country.csv',
                 encoding='latin-1')
# нормализация битого символа ² в заголовках
nr.columns = [c.replace('\xb2', '2').replace('Â²', '2') for c in nr.columns]
OBCOL = 'Prevalence of BMI>=30 kg/m2 (obesity)'
assert OBCOL in nr.columns, nr.columns.tolist()
nr = nr[['Country/Region/World', 'ISO', 'Sex', 'Year', OBCOL]].rename(
    columns={'Country/Region/World': 'ncd_country', OBCOL: 'prev'})
nr['prev_pct'] = nr['prev'] * 100.0

pop = pd.read_csv(MIR / 'population' / 'data' / 'population.csv')
pop.columns = ['pop_name', 'Code', 'Year', 'pop']

reg = pd.read_csv(MIR / 'ncdrisc' / 'data-raw' / 'country-list-2025.csv', encoding='latin-1')
reg = reg.rename(columns={'iso': 'Code', 'Country': 'ncd_country_2025'})[['Code', 'ncd_country_2025', 'Region', 'Superregion']]

un = pd.read_csv(DATA / 'un_member_states.csv')
assert len(un) == 193, len(un)

# ----------------------------------------------------------------------------
# 0b. Сопоставление названий ООН -> ISO3 (только нормализация названий, не данные)
# ----------------------------------------------------------------------------
def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).encode('ascii', 'ignore').decode()
    s = s.lower().replace('&', 'and')
    s = re.sub(r"[^a-z0-9 ]", ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

name_to_iso = {}
for df, ncol, ccol in [(pop[pop.Year == POP_YEAR], 'pop_name', 'Code'),
                       (reg, 'ncd_country_2025', 'Code'),
                       (ob.drop_duplicates('Entity'), 'Entity', 'Code')]:
    for n, c in zip(df[ncol], df[ccol]):
        if isinstance(c, str) and len(c) == 3:
            name_to_iso.setdefault(norm(n), c)

UN_OVERRIDES = {  # официальные названия ООН (Wikipedia) -> ISO3
    'Bahamas, The': 'BHS', 'Gambia (Republic of The)': 'GMB', 'Naoero': 'NRU', 'Türkiye': 'TUR',
    "Democratic People's Republic of Korea": 'PRK', 'Republic of Korea': 'KOR',
    'Iran (Islamic Republic of)': 'IRN', "Lao People's Democratic Republic": 'LAO',
    'Micronesia (Federated States of)': 'FSM', 'Republic of Moldova': 'MDA', 'Russian Federation': 'RUS',
    'Syrian Arab Republic': 'SYR', 'United Kingdom of Great Britain and Northern Ireland': 'GBR',
    'United Republic of Tanzania': 'TZA', 'United States of America': 'USA',
    'Venezuela (Bolivarian Republic of)': 'VEN', "Côte d'Ivoire": 'CIV', 'Cabo Verde': 'CPV',
    'Czechia': 'CZE', 'Eswatini': 'SWZ', 'North Macedonia': 'MKD', 'Timor-Leste': 'TLS', 'Brunei': 'BRN',
    'Vietnam': 'VNM', 'Congo': 'COG', 'Democratic Republic of the Congo': 'COD', 'Bolivia': 'BOL',
    'Sudan': 'SDN', 'South Sudan': 'SSD', 'Saint Kitts and Nevis': 'KNA', 'Saint Lucia': 'LCA',
    'Saint Vincent and the Grenadines': 'VCT', 'Sao Tome and Principe': 'STP', 'Slovakia': 'SVK',
    'Kyrgyzstan': 'KGZ', 'Egypt': 'EGY', 'Yemen': 'YEM',
}
un['Code'] = [UN_OVERRIDES.get(n) or name_to_iso.get(norm(n)) for n in un['member_state']]
missing = un[un.Code.isna()]
assert missing.empty, f'Не сопоставлены члены ООН: {missing.member_state.tolist()}'
assert un.Code.is_unique
UN_CODES = set(un.Code)
un_name = dict(zip(un.Code, un.member_state))

# ----------------------------------------------------------------------------
# 1. Проверка целостности: OWID both sexes vs среднее Men/Women NCD-RisC 2017
# ----------------------------------------------------------------------------
nr_mw = nr.pivot_table(index=['ISO', 'ncd_country', 'Year'], columns='Sex', values='prev_pct').reset_index()
nr_mw['ncd_mean_MW_pct'] = (nr_mw['Men'] + nr_mw['Women']) / 2.0
nr_mw = nr_mw.rename(columns={'ISO': 'Code', 'Men': 'ncd_men_pct', 'Women': 'ncd_women_pct'})

chk = ob.merge(nr_mw, on=['Code', 'Year'], how='inner')
chk['abs_diff_pp'] = (chk['obesity_pct'] - chk['ncd_mean_MW_pct']).abs()
chk_win = chk[chk.Year.isin([Y0, Y1])].copy()
integ = {
    'n_pairs_2006_2016': int(len(chk_win)),
    'n_countries_matched': int(chk_win.Code.nunique()),
    'max_abs_diff_pp_2006_2016': float(chk_win.abs_diff_pp.max()),
    'median_abs_diff_pp_2006_2016': float(chk_win.abs_diff_pp.median()),
    'mean_abs_diff_pp_2006_2016': float(chk_win.abs_diff_pp.mean()),
    'n_over_tol_2006_2016': int((chk_win.abs_diff_pp > INTEGRITY_TOL).sum()),
    'max_abs_diff_pp_all_years': float(chk.abs_diff_pp.max()),
    'median_abs_diff_pp_all_years': float(chk.abs_diff_pp.median()),
    'n_pairs_all_years': int(len(chk)),
}
over = chk_win[chk_win.abs_diff_pp > INTEGRITY_TOL][['Entity', 'Code', 'Year', 'obesity_pct', 'ncd_mean_MW_pct', 'abs_diff_pp']]
chk_win.sort_values('abs_diff_pp', ascending=False).to_csv(DATA / 'a1_integrity_check.csv', index=False)
pd.Series(integ).to_csv(DATA / 'a1_integrity_summary.csv', header=['value'])

# сущности OWID без пары в NCD-RisC и наоборот
owid_codes = set(ob.Code.dropna())
ncd_codes = set(nr.ISO.dropna())
only_owid = sorted(owid_codes - ncd_codes)
only_ncd = sorted(ncd_codes - owid_codes)

# ----------------------------------------------------------------------------
# 2. Полная таблица: 2006, 2016, изменения
# ----------------------------------------------------------------------------
ob_w = ob[ob.Year.isin([Y0, Y1])].copy()
ob_w['Code'] = ob_w['Code'].fillna('NOCODE:' + ob_w['Entity'])   # 'Sudan (former)' без кода
w = ob_w.pivot_table(index=['Entity', 'Code'], columns='Year', values='obesity_pct').reset_index()
w.columns = ['Entity', 'Code', f'y{Y0}', f'y{Y1}']
w.loc[w.Code.str.startswith('NOCODE:'), 'Code'] = np.nan
w['abs_change_pp'] = w[f'y{Y1}'] - w[f'y{Y0}']
w['rel_change_pct'] = (w[f'y{Y1}'] / w[f'y{Y0}'] - 1.0) * 100.0
w['annual_pp_per_year'] = w['abs_change_pp'] / (Y1 - Y0)

pop23 = pop[pop.Year == POP_YEAR][['Code', 'pop']].rename(columns={'pop': f'pop_{POP_YEAR}'})
pop_last = pop.sort_values('Year').groupby('Code').tail(1)[['Code', 'Year', 'pop']].rename(
    columns={'Year': 'pop_last_year', 'pop': 'pop_last'})
w = w.merge(pop23, on='Code', how='left').merge(pop_last, on='Code', how='left').merge(reg, on='Code', how='left')
w['un_member'] = w.Code.isin(UN_CODES)
w['un_name'] = w.Code.map(un_name)
w['pop_for_filter'] = w[f'pop_{POP_YEAR}'].fillna(w['pop_last'])
w['pop_ge_5m'] = w['pop_for_filter'] >= POP_MIN
# NCD-RisC 2017 по полам для справки
for y in (Y0, Y1):
    s = nr_mw[nr_mw.Year == y][['Code', 'ncd_men_pct', 'ncd_women_pct', 'ncd_mean_MW_pct']].rename(
        columns={'ncd_men_pct': f'ncd_men_{y}', 'ncd_women_pct': f'ncd_women_{y}', 'ncd_mean_MW_pct': f'ncd_meanMW_{y}'})
    w = w.merge(s, on='Code', how='left')
w['rank_abs_all'] = w['abs_change_pp'].rank(ascending=False, method='min')
w['rank_rel_all'] = w['rel_change_pct'].rank(ascending=False, method='min')
w = w.sort_values('abs_change_pp', ascending=False).reset_index(drop=True)
w.to_csv(DATA / 'a1_full_table.csv', index=False)

# ----------------------------------------------------------------------------
# 3. Фильтры и рейтинги
# ----------------------------------------------------------------------------
f = w[w.un_member & w.pop_ge_5m].copy()
f['rank_abs'] = f['abs_change_pp'].rank(ascending=False, method='min').astype(int)
f['rank_rel'] = f['rel_change_pct'].rank(ascending=False, method='min').astype(int)
f = f.sort_values('rank_abs').reset_index(drop=True)
f.to_csv(DATA / 'a1_ranking_filtered.csv', index=False)
top8_abs = f.head(8)
top8_rel = f.sort_values('rank_rel').head(8)
near = f[(f.rank_abs >= 6) & (f.rank_abs <= 10)]

# ----------------------------------------------------------------------------
# 4. Малые государства (< 5 млн, члены ООН), попавшие бы в Топ-5 без фильтра по населению
# ----------------------------------------------------------------------------
un_all = w[w.un_member].copy()
un_all['rank_abs_unfiltered'] = un_all['abs_change_pp'].rank(ascending=False, method='min').astype(int)
small = un_all[(un_all.rank_abs_unfiltered <= 5) & (~un_all.pop_ge_5m)].sort_values('rank_abs_unfiltered')
small.to_csv(DATA / 'a1_small_states.csv', index=False)

# Исключённые: не члены ООН / без кода
excl = w[~w.un_member].copy()
excl['reason'] = np.where(excl.Code.isna(), 'нет ISO-кода в файле (историческая сущность)', 'не член ООН (территория / непризнанное)')
excl.to_csv(DATA / 'a1_excluded.csv', index=False)

# ----------------------------------------------------------------------------
# 5. World Obesity Atlas: парсинг текстов PDF (ПРОГНОЗЫ, crude prevalence)
# ----------------------------------------------------------------------------
def pages(path):
    """Возвращает список (page_no, [lines])."""
    txt = Path(path).read_text(encoding='utf-8', errors='replace')
    out, cur, num = [], [], None
    for line in txt.split('\n'):
        m = re.match(r'^=== PAGE (\d+) ===', line)
        if m:
            if num is not None:
                out.append((num, cur))
            num, cur = int(m.group(1)), []
        else:
            cur.append(line.rstrip())
    if num is not None:
        out.append((num, cur))
    return out

def to_num(s):
    s = s.strip().replace(',', '').replace('%', '')
    try:
        return float(s)
    except ValueError:
        return np.nan

atlas_rows = []

# --- Atlas 2025: страницы стран "World Obesity Atlas 2025" / <Country> / "Overweight and obesity prevalence over time"
for pno, L in pages(DATA / 'World_Obesity_Atlas_2025_rev1.txt'):
    if len(L) < 5:
        continue
    country = None
    for i in range(min(6, len(L) - 2)):
        if L[i].strip() == 'World Obesity Atlas 2025' and L[i + 2].strip().startswith('Overweight and obesity prevalence over time'):
            country = L[i + 1].strip()
            break
    if not country:
        continue
    row = {'edition': 'World Obesity Atlas 2025', 'page': pno, 'country_atlas': country}
    for j, line in enumerate(L):
        s = line.strip()
        if s == 'Adults living with obesity in 2025' and j + 1 < len(L):
            row['atlas2025_adult_obesity_2025_pct'] = to_num(L[j + 1])
        if s == 'Adults with high BMI in 2025' and j + 1 < len(L):
            row['atlas2025_adult_highBMI_2025_pct'] = to_num(L[j + 1])
    # таблица численности (тыс.): строки "30-<35" и "35+" -> Men 2010,2015,2030, Women 2010,2015,2030
    try:
        i30 = next(k for k, x in enumerate(L) if x.strip() == '30-<35')
        i35 = next(k for k, x in enumerate(L) if x.strip() == '35+' and k > i30)
        v30 = [to_num(x) for x in L[i30 + 1:i30 + 7]]
        v35 = [to_num(x) for x in L[i35 + 1:i35 + 7]]
        if all(np.isfinite(v30)) and all(np.isfinite(v35)) and L[i30 + 7].strip() == '35+':
            ob2015 = v30[1] + v30[4] + v35[1] + v35[4]
            ob2030 = v30[2] + v30[5] + v35[2] + v35[5]
            row['atlas2025_obese_adults_2015_thousands'] = ob2015
            row['atlas2025_obese_adults_2030_thousands'] = ob2030
    except StopIteration:
        pass
    atlas_rows.append(row)

# --- Atlas 2023: <Country> перед "PROJECTED ECONOMIC IMPACT OF OVERWEIGHT"; "ADULTS WITH / OBESITY 2035 / X%"
for pno, L in pages(DATA / 'World_Obesity_Atlas_2023_Report.txt'):
    idx = [k for k, x in enumerate(L) if x.strip().startswith('PROJECTED ECONOMIC IMPACT OF OVERWEIGHT')]
    if not idx:
        continue
    k = idx[0]
    country = L[k - 1].strip()
    if k >= 2 and (country.lower().startswith('of ') or L[k - 2].strip().endswith(('of', 'Republic', 'and'))):
        country = (L[k - 2].strip() + ' ' + country).strip()
    row = {'edition': 'World Obesity Atlas 2023', 'page': pno, 'country_atlas': re.sub(r'\s+', ' ', country)}
    for j in range(len(L) - 2):
        if L[j].strip() == 'ADULTS WITH' and L[j + 1].strip() == 'OBESITY 2035':
            row['atlas2023_adult_obesity_2035_pct'] = to_num(L[j + 2])
        if L[j].strip() == 'ANNUAL INCREASE' and L[j + 1].strip() == 'IN ADULT OBESITY' and j + 3 < len(L):
            row['atlas2023_annual_increase_adult_obesity_2020_2035_pct'] = to_num(L[j + 3])
    atlas_rows.append(row)

# --- Atlas 2022: <Country> перед "GLOBAL / PREPAREDNESS / RANKING"; "ADULTS WITH / OBESITY BY 2030 / X%"; MEN/WOMEN 2030
for pno, L in pages(DATA / 'World_Obesity_Atlas_2022.txt'):
    idx = [k for k, x in enumerate(L) if x.strip() == 'GLOBAL' and k + 2 < len(L)
           and L[k + 1].strip() == 'PREPAREDNESS' and L[k + 2].strip() == 'RANKING']
    if not idx or not any(x.strip() == 'ADULT OBESITY IN 2030' for x in L):
        continue
    k = idx[0]
    country = L[k - 1].strip()
    if k >= 2 and (country.lower().startswith('of ') or L[k - 2].strip().endswith(('of', 'Republic', 'and'))):
        country = (L[k - 2].strip() + ' ' + country).strip()
    row = {'edition': 'World Obesity Atlas 2022', 'page': pno, 'country_atlas': re.sub(r'\s+', ' ', country)}
    for j in range(len(L) - 2):
        if L[j].strip() == 'ADULTS WITH' and L[j + 1].strip() == 'OBESITY BY 2030':
            row['atlas2022_adult_obesity_2030_pct'] = to_num(L[j + 2])
        if L[j].strip() == 'ANNUAL INCREASE' and L[j + 1].strip() == 'IN ADULT OBESITY' and j + 3 < len(L):
            row['atlas2022_annual_increase_adult_obesity_2010_2030_pct'] = to_num(L[j + 3])
        if L[j].strip() == 'MEN' and L[j + 1].strip().startswith('Prevalence'):
            row['atlas2022_men_obesity_2030_pct'] = to_num(L[j + 2])
        if L[j].strip() == 'WOMEN' and L[j + 1].strip().startswith('Prevalence'):
            row['atlas2022_women_obesity_2030_pct'] = to_num(L[j + 2])
    atlas_rows.append(row)

atlas = pd.DataFrame(atlas_rows)

# сопоставление названий Атласа с ISO
ATLAS_OVERRIDES = {
    'china (hong kong sar)': 'HKG', 'hong kong': 'HKG', 'cote divoire': 'CIV', 'cote d ivoire': 'CIV',
    'guinea bissau': 'GNB', 'brunei darussalam': 'BRN', 'lao pdr': 'LAO', 'laos': 'LAO',
    'republic of korea': 'KOR', 'korea republic of': 'KOR', 'south korea': 'KOR',
    'democratic people s republic of korea': 'PRK', 'dpr korea': 'PRK', 'north korea': 'PRK',
    'iran islamic republic of': 'IRN', 'iran': 'IRN', 'russian federation': 'RUS', 'russia': 'RUS',
    'syrian arab republic': 'SYR', 'syria': 'SYR', 'united republic of tanzania': 'TZA', 'tanzania': 'TZA',
    'united states of america': 'USA', 'united states': 'USA', 'usa': 'USA', 'venezuela bolivarian republic of': 'VEN',
    'venezuela': 'VEN', 'viet nam': 'VNM', 'vietnam': 'VNM', 'republic of moldova': 'MDA', 'moldova': 'MDA',
    'bolivia plurinational state of': 'BOL', 'bolivia': 'BOL', 'micronesia federated states of': 'FSM',
    'micronesia': 'FSM', 'turkiye': 'TUR', 'turkey': 'TUR', 'united kingdom': 'GBR', 'czechia': 'CZE',
    'czech republic': 'CZE', 'eswatini': 'SWZ', 'swaziland': 'SWZ', 'north macedonia': 'MKD', 'macedonia': 'MKD',
    'timor leste': 'TLS', 'cabo verde': 'CPV', 'cape verde': 'CPV', 'congo': 'COG', 'republic of congo': 'COG',
    'democratic republic of the congo': 'COD', 'democratic republic of congo': 'COD', 'dr congo': 'COD',
    'taiwan': 'TWN', 'occupied palestinian territory': 'PSE', 'palestine': 'PSE', 'state of palestine': 'PSE',
    'kosovo': 'XKX', 'sudan': 'SDN', 'south sudan': 'SSD', 'gambia': 'GMB', 'bahamas': 'BHS', 'the bahamas': 'BHS',
    'saint kitts and nevis': 'KNA', 'st kitts and nevis': 'KNA', 'saint lucia': 'LCA', 'st lucia': 'LCA',
    'saint vincent and the grenadines': 'VCT', 'st vincent and the grenadines': 'VCT', 'sao tome and principe': 'STP',
    'united arab emirates': 'ARE', 'puerto rico': 'PRI', 'greenland': 'GRL', 'french polynesia': 'PYF',
    'american samoa': 'ASM', 'tokelau': 'TKL', 'cook islands': 'COK', 'niue': 'NIU', 'bermuda': 'BMU',
    'antigua and barbuda': 'ATG', 'trinidad and tobago': 'TTO', 'papua new guinea': 'PNG', 'solomon islands': 'SLB',
    'marshall islands': 'MHL', 'central african republic': 'CAF', 'dominican republic': 'DOM', 'el salvador': 'SLV',
    'equatorial guinea': 'GNQ', 'sierra leone': 'SLE', 'south africa': 'ZAF', 'sri lanka': 'LKA', 'burkina faso': 'BFA',
    'costa rica': 'CRI', 'new zealand': 'NZL', 'saudi arabia': 'SAU', 'bosnia and herzegovina': 'BIH',
}
name_to_iso_all = dict(name_to_iso)
for n, c in zip(un.member_state, un.Code):
    name_to_iso_all.setdefault(norm(n), c)
atlas['Code'] = [ATLAS_OVERRIDES.get(norm(n)) or name_to_iso_all.get(norm(n)) for n in atlas.country_atlas]
atlas = atlas.sort_values(['edition', 'page']).reset_index(drop=True)
atlas.to_csv(DATA / 'a1_atlas_projections_long.csv', index=False)
atlas_unmatched = atlas[atlas.Code.isna()].country_atlas.unique().tolist()

# широкая таблица по ISO (одна строка на страну)
vals = [c for c in atlas.columns if c.startswith('atlas')]
atlas_wide = atlas.dropna(subset=['Code']).groupby('Code').agg({**{c: 'first' for c in vals},
                                                                 'country_atlas': 'first'})
pg = atlas.dropna(subset=['Code']).pivot_table(index='Code', columns='edition', values='page', aggfunc='first')
pg.columns = ['page_' + c.replace('World Obesity Atlas ', 'atlas') for c in pg.columns]
atlas_wide = atlas_wide.join(pg).reset_index()
atlas_wide.to_csv(DATA / 'a1_atlas_projections_wide.csv', index=False)

# соединяем прогнозы с Топ-8 и малыми государствами (отдельная таблица, помечена как ПРОГНОЗ)
sel_codes = list(top8_abs.Code) + [c for c in small.Code if c not in set(top8_abs.Code)]
proj = w[w.Code.isin(sel_codes)][['Entity', 'Code', f'y{Y1}']].merge(atlas_wide, on='Code', how='left')
proj['is_top8'] = proj.Code.isin(set(top8_abs.Code))
proj.to_csv(DATA / 'a1_projections_selected.csv', index=False)

# ----------------------------------------------------------------------------
# Вывод
# ----------------------------------------------------------------------------
pd.set_option('display.width', 250, 'display.max_columns', 40, 'display.max_rows', 300)
print('=== 1. ЦЕЛОСТНОСТЬ (OWID both sexes vs mean(Men,Women) NCD-RisC 2017), в п.п. ===')
for k, v in integ.items():
    print(f'  {k}: {v:.4f}' if isinstance(v, float) else f'  {k}: {v}')
print('  страны с |diff| > 1.5 п.п. (2006/2016):')
print(over.to_string(index=False) if len(over) else '  (нет)')
print('  топ-10 по |diff| 2006/2016:')
print(chk_win.sort_values('abs_diff_pp', ascending=False).head(10)[['Entity', 'Code', 'Year', 'obesity_pct', 'ncd_mean_MW_pct', 'abs_diff_pp']].to_string(index=False))
print(f'  только в OWID (нет в NCD-RisC): {only_owid}')
print(f'  только в NCD-RisC (нет в OWID): {only_ncd}')
print(f'  сущности OWID: {ob.Entity.nunique()}, с кодом: {len(owid_codes)}; NCD-RisC: {len(ncd_codes)}')

print('\n=== 2. Полная таблица: N =', len(w), '; членов ООН в файле:', int(w.un_member.sum()),
      '; членов ООН без данных в файле:', sorted(UN_CODES - set(w.Code.dropna())))
print('   членов ООН (в файле) без населения 2023:', w[w.un_member & w[f'pop_{POP_YEAR}'].isna()][['Entity', 'Code', 'pop_last_year', 'pop_last']].to_string(index=False))

cols = ['rank_abs', 'Entity', 'Code', f'y{Y0}', f'y{Y1}', 'abs_change_pp', 'rel_change_pct', 'annual_pp_per_year', f'pop_{POP_YEAR}', 'rank_rel', 'Region']
print(f'\n=== 3a. ТОП-8 по абсолютному изменению (члены ООН, население >= 5 млн; N={len(f)}) ===')
print(top8_abs[cols].to_string(index=False))
print('\n=== 3b. ТОП-8 по относительному изменению ===')
print(top8_rel[['rank_rel', 'Entity', 'Code', f'y{Y0}', f'y{Y1}', 'abs_change_pp', 'rel_change_pct', 'rank_abs', f'pop_{POP_YEAR}']].to_string(index=False))
print('\n=== 3c. Кто близко: места 6-10 (абсолютное) ===')
print(near[cols].to_string(index=False))
print('\n=== 3d. места 9-15 для контекста ===')
print(f[(f.rank_abs >= 9) & (f.rank_abs <= 15)][cols].to_string(index=False))

print('\n=== 4. Малые государства (< 5 млн, члены ООН), в Топ-5 без фильтра ===')
print(small[['rank_abs_unfiltered', 'Entity', 'Code', f'y{Y0}', f'y{Y1}', 'abs_change_pp', 'rel_change_pct', 'annual_pp_per_year', f'pop_{POP_YEAR}']].to_string(index=False))
print('\n   Топ-10 без фильтра (только члены ООН):')
print(un_all.sort_values('rank_abs_unfiltered').head(10)[['rank_abs_unfiltered', 'Entity', 'Code', f'y{Y0}', f'y{Y1}', 'abs_change_pp', f'pop_{POP_YEAR}', 'pop_ge_5m']].to_string(index=False))

print('\n=== Исключённые (не члены ООН / без кода) ===')
print(excl[['Entity', 'Code', f'y{Y0}', f'y{Y1}', 'abs_change_pp', 'rank_abs_all', f'pop_{POP_YEAR}', 'reason']].to_string(index=False))

print('\n=== 5. Атлас: распарсено строк по редакциям ===')
print(atlas.groupby('edition').agg(n=('country_atlas', 'size'), n_iso=('Code', 'count')))
print('   не сопоставлены с ISO:', atlas_unmatched)
print('   дубликаты Code внутри редакции:', atlas.dropna(subset=['Code']).groupby(['edition', 'Code']).size().loc[lambda s: s > 1].reset_index().to_dict('records'))
print(proj.to_string(index=False))
print('\nNCD-RisC 2017 по полам для Топ-8:')
print(top8_abs[['Entity', f'ncd_men_{Y0}', f'ncd_women_{Y0}', f'ncd_men_{Y1}', f'ncd_women_{Y1}', f'ncd_meanMW_{Y0}', f'ncd_meanMW_{Y1}']].round(2).to_string(index=False))
