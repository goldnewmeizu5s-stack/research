# U07-U10. Проверка уникальности четырёх налоговых конструкций (Дания, Венгрия, Маврикий, Эфиопия)

Дата работы: 2026-09-04. Все источники открыты в этой сессии через mcp__Firecrawl__firecrawl_search / firecrawl_research_*.
WebSearch недоступен. WebFetch к не-github доменам заблокирован прокси — не использовался.
Ограничение сессии: инструмента прямого скрейпинга произвольного URL нет; тексты получены из индексируемых фрагментов (description/highlights) Firecrawl. PDF-карты GFRP (Tax maps foods, March 2026) в индексе присутствуют только как ссылки, содержимое PDF получить не удалось — зафиксировано как ограничение.

---

## РАЗДЕЛ 0. ОБЩАЯ КАРТИНА: сколько стран имеют налоги на сладкие напитки и какой конструкции

### (а) Сколько всего стран/юрисдикций облагают сладкие напитки

| Оценка | Значение | Год данных | Определение метрики | Источник (уровень) | URL | Дословный фрагмент |
|---|---|---|---|---|---|---|
| WHO, пресс-релиз к двум глобальным отчётам | **не менее 116 стран** | данные 2024, публикация 13.01.2026 | страны, облагающие налогом sugary drinks (любой национальный налог) | WHO (T1) | https://www.who.int/news/item/13-01-2026-cheaper-drinks-will-see-a-rise-in-noncommunicable-diseases-and-injuries | "The reports show that at least 116 countries tax sugary drinks, many of which are sodas." |
| WHO Global report on the use of SSB taxes, 2023 | **не менее 108 стран** | на июль 2022 | национальные акцизы хотя бы на один тип SSB | WHO IRIS PDF (T1) | https://iris.who.int/server/api/core/bitstreams/9dc39e4a-e2ba-4ae3-b10e-579101605264/content | "As of July 2022, at least 108 countries worldwide apply national-level excise taxes to at least one type of SSB." |
| WHO Fiscal policies to promote healthy diets (policy brief, 2022) | **85 из 194 государств-членов (44%)** | на май 2022 | национальный налог на SSB; ещё 3 государства — субнациональные | WHO IRIS PDF (T1) | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "As of May 2022, 85 of the 194 Member States (44%) taxed sugar-sweetened beverages at ... national level" |
| JAMA Network Open 2023 (Hattersley & Mandeville) | **103 страны и территории**, 118 налогов (105 национальных + 13 субнациональных), 51% населения мира | данные до 2022 | верифицированные налоги на SSB | рецензируемая статья (T1) | https://pubmed.ncbi.nlm.nih.gov/36988952/ | "National SSB taxes are in effect in 103 countries and territories, covering 51% of the world's population." |
| Lancet Global Health 2026 (Tufts, 183 страны) | **64 страны** ввели SSB-налог "for health purposes" 1990-2024, охват 3,5 млрд чел. | 1990-2024 | только налоги со здравоохранительной мотивацией | PMC (T1) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13386411/ | "From 1990 to 2024, 64 countries implemented sugar-sweetened beverage taxes, accelerating over time and covering 3·5 billion people globally." |
| World Bank Global SSB Tax Database | **более 100 стран и территорий** (национальные налоги) | база, обновление 2023+ | национальные налоги на SSB | World Bank (T1) | https://ssbtax.worldbank.org/ | "SSB taxes are in effect across all World Bank regions, including national level taxes in more than 100 countries and territories." |
| Tax Foundation со ссылкой на World Bank SSB Tax Database (август 2023) | **117 стран** | 2023 | "some form of sugary drink tax" | T2 со ссылкой на T1 | https://taxfoundation.org/research/all/global/sugar-tax-soda-tax-ssb/ | "According to the World Bank, 117 countries have adopted some form of sugary drink tax." |
| Obesity Evidence Hub | **более 130 юрисдикций, почти 120 стран и территорий** | обновляемая база | все юрисдикции (вкл. города) | T2 | https://www.obesityevidencehub.org.au/collections/prevention/countries-that-have-implemented-taxes-on-sugar-sweetened-beverages-ssbs | "Over 130 jurisdictions across nearly 120 countries and territories have implemented taxes on sugar-sweetened beverages (SSBs) to date." |

**Расхождения не скрываем:** разброс 64 / 85 / 103 / 108 / 116 / 117 / ~120 объясняется разными определениями (только "здравоохранительные" налоги vs любые акцизы; страны vs юрисдикции; год среза). Для целей этого отчёта базовая цифра: **116 стран (WHO, данные 2024, публикация 13.01.2026)**.

### (б) Сколько из них построены на СОДЕРЖАНИИ САХАРА, а не адвалорные/объёмные

| Метрика | Значение | Год | Источник (уровень) | URL | Фрагмент |
|---|---|---|---|---|---|
| Доля стран, дифференцирующих ставку акциза по содержанию сахара | **менее 1 из 4** | 2022 | WHO Global report 2023 (T1) | https://iris.who.int/server/api/core/bitstreams/9dc39e4a-e2ba-4ae3-b10e-579101605264/content | "Less than one in four countries differentiate between excise tax rates based on sugar content." |
| Доля акцизов, вообще являющихся акцизами | 104 из 118 (88%) | до 2022 | JAMA 2023 (T1) | https://pubmed.ncbi.nlm.nih.gov/36988952/ | "Most SSB taxes are excise taxes (104 of 118 [88%])." |
| Доля многоступенчатых (tiered) акцизов | 55 из 104 (53%) | до 2022 | JAMA 2023 (T1) | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2802843 | "More than half of excise taxes worldwide (55 of 104 [53%]) apply tiered ..." |
| Из них ступени определены **по содержанию сахара** | **18 из 55 (33%)** — т.е. ~18 налогов в мире | до 2022 | JAMA 2023 (T1) | https://pubmed.ncbi.nlm.nih.gov/36988952/ | "... beverage type (41 of 55 [75 %]) than by sugar content (18 of 55 [33 %])." |
| Где применяются сахарные ступени | 13 из 18 (72%) — страны с высоким доходом | до 2022 | JAMA 2023 (T1) | https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2802843 | "Tiers defined by sugar content are mainly used in high-income countries (13 of 18 [72%])" |
| Структура 64 "здравоохранительных" налогов | 45% адвалорные, 44% объёмные, **только 11% на содержании сахара или смешанные** | 1990-2024 | Lancet Glob Health 2026 (T1) | https://pmc.ncbi.nlm.nih.gov/articles/PMC13386411/ | "45% of countries adopted an ad valorem tax, 44% adopted volume-based specific taxes, and only 11% used a sugar content-focused approach" |
| Налоги на АБСОЛЮТНОЕ содержание сахара (за грамм) | **5 стран** | на янв. 2020 | World Bank 2020 (T1) | https://thedocs.worldbank.org/en/doc/d9612c480991c5408edca33d54e2028a-0390062021/original/World-Bank-2020-SSB-Taxes-Evidence-and-Experiences.pdf | "Five countries have implemented sugar-based taxes to date: the Cook Islands, France, Mauritius, South Africa, and Sri Lanka." |
| Польша (добавилась после 2020) | переменная часть 0,05 PLN за каждый грамм сахара свыше 5 г/100 мл | 2021 | PwC/KPMG (T2), USDA GAIN (T1) | https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Poland%20Taxes%20Soft%20Drinks%20and%20Energy%20Drinks_Warsaw_Poland_03-02-2021 | "A variable tax of PLN 0.05 ($0.01) is applied to each gram of sugar over five grams per 100 ml per liter" |

**Вывод по (б):** налоги, привязанные к содержанию сахара, — меньшинство: ~18 налогов с сахарными ступенями в мире (2022) и лишь **5-6 стран с налогом за грамм сахара** (Кука, Франция — скользящая шкала, Маврикий, ЮАР, Шри-Ланка, + Польша с 2021). Уверенность HIGH.

### (в) Кто облагает ТВЁРДЫЕ продукты по составу/содержанию сахара

| Страна | Конструкция | База | Год / статус | Источник, URL | Фрагмент |
|---|---|---|---|---|---|
| Маврикий | акциз 15 центов за грамм сахара, порог 4 г/100 г или 100 мл, включая "non-staple sugar sweetened food products" | **содержание сахара (за грамм)** | 2016 напитки, твёрдые продукты внесены поправкой 7/2020, ставка 15 центов в бюджете 2026/27; действует | MRA (T1) https://www.mra.mu/customs1/more-topics/excise-tax-on-sugar-content-of-sugar-sweetened-non-alcoholic-beverages | "An excise duty of fifteen cents per gram of sugar is applicable on non-alcoholic beverages containing sugar and non-staple sugar sweetened food products" |
| Венгрия | NETA, специфический акциз (HUF/кг) на предупакованные неосновные продукты по порогам сахара/соли/кофеина | **пороги состава** | 2011, действует | WHO (T1) https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "snacks with more than 1 g salt per 100 g, condiments with more than 5 g salt per 100 g ... pre-packaged sugarsweetened products" |
| Колумбия | налог на ультрапереработанные продукты, пороги: >10% энергии из свободных сахаров, >10% из насыщенных жиров, >300 мг натрия/100 г | **пороги состава, адвалорно 10/15/20%** | Ley 2277 (13.12.2022), с 01.11.2023 | GFRP (T2) https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | ">10% of total energy from free sugars; >10% of total energy form saturated fats. The tax rates will be 10% in 2023, 15% in 2024 and 20% in 2025." |
| Мексика | IEPS, 8% адвалорный акциз на "неосновные" продукты с энергоплотностью >275 ккал/100 г | **калорийность, НЕ сахар** | 2014, действует | WHO (T1) https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Nonessential foods with an energy density of more than 275 kcal per 100 g have been subject to an 8% ad valorem excise tax since 2014." |
| Дания | акциз на шоколад, кондитерские изделия, печенье и торты (специфический, по весу продукта) | **категория, НЕ состав** | действует (отдельно от отменённого fedtafgift) | WHO (T1) https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Denmark still taxes chocolates, confectionaries, biscuits and cakes via specific excise taxes." |
| Норвегия | акциз на шоколад и сахарные изделия 36,92 NOK/кг продукта | **вес продукта, НЕ содержание сахара** | повышен 2018, **отменён с 2021** | Guardian (T2), newsinenglish.no (T2) https://www.theguardian.com/world/2019/nov/23/norwegian-sugar-tax-confectionery-border-sweden | "the levy on chocolate and confectionery was raised by 83% to 36.92 kroner (£3.12) per kilo" |
| Бермуды | импортная пошлина на сахар, конфеты, продукты с какао; 50% (2018) → 75% (2019) | **адвалорно по категориям** | 2018, действует | Правительство Бермуд (T1) https://www.gov.bm/articles/sugar-tax ; PMC (T1) https://pmc.ncbi.nlm.nih.gov/articles/PMC9379233/ | "On 1 April 2019, the level of the tax was increased to 75%, and the tax base was expanded to include food products containing cocoa." |
| Тонга | акциз/импортная пошлина на жирные продукты (турецкие хвосты, бараньи отрубы), продукты с высоким содержанием сахара, лапша б/п | **категории продуктов** | с 2016 | WHO (T1) https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Since 2016, Tonga has imposed an excise tax and/or import duty on high fat foods – including very fatty meat products such as turkey tails and mutton flaps" |
| Норвегия, Венгрия, Индия, Дания, Бермуды, Доминика, Сент-Винсент и Гренадины, Навахо (США) | сводный перечень стран с налогами на нерафинированный сахар / продукты с добавленным сахаром | смешанные конструкции | обзор Cochrane 2020, цитируется в 2025 | PMC (T1) https://pmc.ncbi.nlm.nih.gov/articles/PMC12396183/ | "Other countries, such as Norway, Hungary, India, Denmark, Bermuda, Dominica, St. Vincent and the Grenadines, and the Navajo Nation (USA), have implemented taxes on unprocessed sugar and sugar-added foods" |
| Барбадос | акциз на солёные снеки | категория | принят 10.03.2025 | GFRP (T2) https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | "Excise tax on salty snacks \| Passed March 10, 2025" |

Опорная цифра WHO: **"As of 2022, 29 Member States implemented national level taxes on food products"** (WHO Fiscal policies policy brief, T1, https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download). То есть налоги на *еду* (не напитки) есть у 29 стран из 194, но подавляющее большинство — по категориям товаров, а не по содержанию нутриента.

**Финляндия (налог на сладости/мороженое до 2017) и Керала (fat tax 2016-2017)** — не подтверждены в этой сессии дословными фрагментами первичных источников по конструкции: Керала подтверждена как адвалорный налог на сети быстрого питания ("The Fat Tax was levied only on multinational chains and branded trademark owners", https://effectivecooperation.org/system/files/2021-06/GDI%20Case%20Study%20on%20Fat%20Tax%20in%20Kerala.pdf, T2), Финляндия — см. раздел "Непроверенное".

### (г) Кто облагает продукты по содержанию НАСЫЩЕННЫХ или ТРАНСжиров

| Страна | Конструкция | Статус | Источник | Фрагмент |
|---|---|---|---|---|
| Дания | специфический акциз 16 DKK/кг насыщенного жира, порог 2,3% | окт.2011 - 01.01.2013, **отменён** | Folketinget (T1) https://www.ft.dk/samling/20101/lovforslag/l111/index.htm | "Afgiften er fastsat til 16 kr. pr. kg mættet fedt i fødevaren. Desuden indfører loven en bagatelgrænse, så fødevarer med et indhold af mættet fedt på 2,3 pct." |
| Эфиопия | адвалорный акциз на жиры и масла с высоким содержанием насыщенных/трансжиров | введён февраль 2020 | WHO (T1) https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "In February 2020, Ethiopia introduced an ad valorem excise tax on imported and locally produced foods, including fats and oils with high levels of saturated or trans-fatty acids" |
| Венгрия | с 2022 в нутриент-профильную модель NETA добавлены **насыщенные жирные кислоты для солёных снеков** | действует | WHO Global report on sodium intake reduction (T1) https://iris.who.int/server/api/core/bitstreams/296605a9-820a-41bc-8f28-bf4b1367d530/content | "From 2022 the nutrient profile model was complemented with saturated fatty acids for salty snacks, and fibre content for the newly added food category mueslis and breakfast cereals." |
| Колумбия | порог >10% энергии из насыщенных жиров в налоге на UPF | с 01.11.2023 | GFRP (T2) https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | ">10% of total energy form saturated fats" |
| Тонга | налог на "high fat foods" по категориям (не по содержанию нутриента) | с 2016 | WHO (T1) | см. выше |

Ключевая рамка (T1, рецензируемая): **"Denmark has been the only country in the world to operate a tax on saturated fat content in foods, from 2011 to 2012."** — Proceedings of the Nutrition Society, "State-of-the-art for food taxes to promote public health", https://www.cambridge.org/core/journals/proceedings-of-the-nutrition-society/article/stateoftheart-for-food-taxes-to-promote-public-health/EDA28CE1643DBDED53EA0E31CEDD7592 (T1, 2017; pmid:29166954).

### (д) Есть ли ещё страны с правилом "нет данных на этикетке = максимальная ставка"

| Страна | Правило | Статус | Источник | Фрагмент |
|---|---|---|---|---|
| Эфиопия | если уровень насыщенного жира нельзя определить по этикетке — продукт облагается | 2020 | Только T3-копии текста прокламации (scribd/pdfcoffee/weebly): https://pdfcoffee.com/ethiopian-tax-law-new-text-book-pdf-free.html | "40g or more saturated fat per 100g, or more than 0.5g of trans fat per 100g, or unable to a determinate level of saturated fat from label" |
| ЮАР | если содержание сахара не заявлено/нет валидного тест-отчёта — **презюмируется 20 г/100 мл** (штрафной уровень) | Health Promotion Levy, действует | SARS (T1) https://www.sars.gov.za/customs-and-excise/excise/health-promotion-levy-on-sugary-beverages/ | "In the absence of such a valid test report, a deemed sugar content of 20 grams per 100 ml is assumed." |
| Маврикий | требуется сертификат, удостоверяющий содержание сахара по каждому продукту (административная, не штрафная конструкция) | действует | MRA (T1) https://www.mra.mu/customs1/more-topics/excise-tax-on-sugar-content-of-sugar-sweetened-non-alcoholic-beverages | "...certifying the sugar content for each non-staple sugar sweetened food product." |

**Итог (д):** документально подтверждён **один** аналог правила "нет данных → облагается по максимуму" — ЮАР (для сахара в напитках). Для **насыщенных жиров** аналогов не найдено. Уверенность MEDIUM (доказательство отсутствия ограничено охватом поиска).

---

## U07. ДАНИЯ — налог на насыщенные жиры (fedtafgiftsloven, Lov nr. 247 af 30/03/2011)

### Верификация самой меры
- Ставка и порог: "Afgiften er fastsat til 16 kr. pr. kg mættet fedt i fødevaren. Desuden indfører loven en bagatelgrænse, så fødevarer med et indhold af mættet fedt på 2,3 pct." — Folketinget, L 111 (T1), https://www.ft.dk/samling/20101/lovforslag/l111/index.htm, доступ 2026-09-04.
- Текст закона: "LOV nr 247 af 30/03/2011 ... Afgiftspligtige fødevarer. § 1. Der betales afgift til statskassen af vægten af mættet fedt i følgende fødevarer" — FAOLEX (T1), https://faolex.fao.org/docs/pdf/den102367.pdf.
- Отмена: "Afgiften er ophævet med virkning fra 1. januar 2013 ved lov nr. 1395 af 23. december 2012." — Skattestyrelsen, info.skat.dk (T1), https://info.skat.dk/data.aspx?oid=1948954.
- **Статус на 2026-09-04: отменён с 01.01.2013.**

### Таблица стран-аналогов

| Страна | Точный аналог / похожая / нет | Конструкция | Год / статус | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Дания (сама мера) | — | специфический акциз 16 DKK за кг насыщенного жира, порог 2,3% | 2011-2013, отменён | https://www.ft.dk/samling/20101/lovforslag/l111/index.htm | "Afgiften er fastsat til 16 kr. pr. kg mættet fedt i fødevaren" | T1 |
| **Нет ни одной страны** с акцизом «за килограмм насыщенного жира» | **точных аналогов 0** | — | — | https://www.cambridge.org/core/journals/proceedings-of-the-nutrition-society/article/stateoftheart-for-food-taxes-to-promote-public-health/EDA28CE1643DBDED53EA0E31CEDD7592 | "Denmark has been the only country in the world to operate a tax on saturated fat content in foods, from 2011 to 2012." | T1 |
| Эфиопия | похожая | адвалорный акциз (не за кг жира) на жиры/масла с высоким содержанием насыщенных и трансжиров | 2020, действует (изм. 1287/2023) | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Ethiopia introduced an ad valorem excise tax ... including fats and oils with high levels of saturated or trans-fatty acids" | T1 |
| Венгрия | похожая | насыщенные жирные кислоты как один из критериев нутриент-профиля NETA для солёных снеков | с 2022 | https://iris.who.int/server/api/core/bitstreams/296605a9-820a-41bc-8f28-bf4b1367d530/content | "From 2022 the nutrient profile model was complemented with saturated fatty acids for salty snacks" | T1 |
| Колумбия | похожая | порог >10% энергии из насыщенных жиров в адвалорном налоге на UPF | с 01.11.2023 | https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | ">10% of total energy form saturated fats" | T2 |
| Тонга | похожая | акциз/пошлина на "high fat foods" по категориям продуктов | с 2016 | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Tonga has imposed an excise tax and/or import duty on high fat foods" | T1 |
| Индия (Керала) | похожая, отменена | 14,5% адвалорно на сети быстрого питания, не по составу | 2016-2017 | https://effectivecooperation.org/system/files/2021-06/GDI%20Case%20Study%20on%20Fat%20Tax%20in%20Kerala.pdf | "The Fat Tax was levied only on multinational chains and branded trademark owners" | T2 |

**Итог U07: точных аналогов N = 0. Похожих мер M = 5 (Эфиопия, Венгрия, Колумбия, Тонга, Керала/Индия).**
Источник подсчёта: Proceedings of the Nutrition Society 2017 (прямое утверждение об уникальности) + WHO Fiscal policies policy brief 2022 (Box 6) + WHO Global report on sodium intake reduction (Box 16) + GFRP.
Уверенность: **HIGH** (два независимых T1 согласуются: рецензируемый обзор прямо называет Данию единственной; WHO Box 6 при перечислении налогов на продукты не приводит ни одного второго налога «за вес насыщенного жира»).
**Вердикт: АНОМАЛИЯ (N=0 ≤ 5). Уникальная в мировой практике конструкция; при этом мера отменена с 01.01.2013.**

---

## U08. ВЕНГРИЯ — Népegészségügyi termékadó (NETA), 2011. évi CIII. törvény

### Верификация самой меры
- Конструкция: "Paid on a per unit measure (Kg, Liter). Based on sugar, salt and methylxantine (caffeine) content of products." — Европейская комиссия, презентация "The Hungarian Public Health Product Tax" (T1), https://health.ec.europa.eu/system/files/2019-07/ev_201906201_co012_en_0.pdf.
- Охват категорий: "Sugar sweetened drinks; energy drinks; salty snacks; condiments; sweets (chocolate, ice cream etc.); alcopops, flavoured beer; fruit jams." — там же (T1).
- Расширенный перечень и эволюция: "The tax applies to soft drinks, energy drinks, flavoured beers, alcoholic soda beverages, pre-packaged sweetened products, bakery products, cocoa-containing products, fruit preserves, salty snacks, bouillons, condiments, mueslis and breakfast cereals" — WHO Global report on sodium intake reduction, Box 16 (T1), https://iris.who.int/server/api/core/bitstreams/296605a9-820a-41bc-8f28-bf4b1367d530/content.
- Дата вступления: "the Public Health Product Tax came into effect in September 2011" — там же (T1). **Статус: действует.**

### Таблица стран-аналогов (конструкция: ОДИН налог, охватывающий несколько категорий продуктов И напитков, с порогами по составу/нутриент-профилю)

| Страна | Точный аналог / похожая / нет | Конструкция | Год / статус | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Колумбия | **точный аналог** | единый «здоровый налог» (Ley 2277) на UPF: молочные с сахаром, колбасы, шоколад, снеки, выпечка, хлопья, джемы, соусы, приправы — по порогам натрия/сахаров/насыщенных жиров | принят 13.12.2022, действует с 01.11.2023 | https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | "Ultra-processed food categories subject to taxation will include: milk products added with sugar, sausages and cold cut meats, chocolates and confectionary candies, snacks, bakery products" | T2 |
| Мексика | похожая | ДВА раздельных налога: 1 песо/л на SSB и 8% на «неосновные» продукты по **энергоплотности**, а не по составу нутриентов | 2014, действует | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Nonessential foods with an energy density of more than 275 kcal per 100 g have been subject to an 8% ad valorem excise tax since 2014." | T1 |
| Маврикий | похожая | единый акциз за грамм сахара на напитки И твёрдые продукты, но один нутриент (сахар), не мультинутриентный профиль | 2016/2020, действует | https://www.mra.mu/customs1/more-topics/excise-tax-on-sugar-content-of-sugar-sweetened-non-alcoholic-beverages | "excise duty of fifteen cents per gram of sugar ... non-alcoholic beverages containing sugar and non-staple sugar sweetened food products" | T1 |
| Тонга | похожая | пакет акцизов/пошлин на жирное мясо, продукты с высоким сахаром, лапшу б/п — по категориям | с 2016 | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "excise tax and/or import duty on high fat foods ... as well as foods and beverages high in sugars and instant noodles" | T1 |
| Бермуды | похожая | импортная пошлина 50→75% на сахар, конфеты, какао-продукты и напитки — по категориям, адвалорно | 2018/2019, действует | https://pmc.ncbi.nlm.nih.gov/articles/PMC9379233/ | "the level of the tax was increased to 75%, and the tax base was expanded to include food products containing cocoa" | T1 |
| Дания | похожая | отдельные специфические акцизы на шоколад, кондитерские, печенье, торты (без порогов состава) | действует | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Denmark still taxes chocolates, confectionaries, biscuits and cakes via specific excise taxes." | T1 |
| Норвегия | похожая, отменена | акциз на шоколад и сахарные изделия 36,92 NOK/кг продукта | повышен 2018, отменён 2021 | https://www.theguardian.com/world/2019/nov/23/norwegian-sugar-tax-confectionery-border-sweden | "the levy on chocolate and confectionery was raised by 83% to 36.92 kroner (£3.12) per kilo" | T2 |
| Барбадос | похожая | акциз на солёные снеки | принят 10.03.2025 | https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | "Excise tax on salty snacks \| Passed March 10, 2025" | T2 |
| Доминика, Сент-Винсент и Гренадины, Навахо (США), Индия | похожие (конструкции не верифицированы поштучно) | налоги на нерафинированный сахар / продукты с добавленным сахаром | по обзору Cochrane 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12396183/ | "Norway, Hungary, India, Denmark, Bermuda, Dominica, St. Vincent and the Grenadines, and the Navajo Nation (USA), have implemented taxes on unprocessed sugar and sugar-added foods" | T1 |

Опорное утверждение об уникальности нутриент-профильной части: **"Of the 194 Member States, one Member State (Hungary) has had an excise tax since 2011 targeting foods high in sodium through underlying nutrient profile modelling."** — WHO Global report on sodium intake reduction (T1), https://iris.who.int/server/api/core/bitstreams/296605a9-820a-41bc-8f28-bf4b1367d530/content. Там же: "Several other Member States tax foods that may be typically high in sodium, such as salty snacks or bouillon cubes, but are without a threshold for sodium content in an underlying nutrient profile model".

**Итог U08: точных аналогов N = 1 (Колумбия). Похожих мер M = 8+ (Мексика, Маврикий, Тонга, Бермуды, Дания, Норвегия(отм.), Барбадос, + Доминика/Сент-Винсент/Навахо/Индия по сводке Cochrane).**
Источник подсчёта: WHO Fiscal policies policy brief 2022 (Box 6), WHO Global report on sodium intake reduction (Box 16), GFRP Fiscal policies, EC presentation.
Уверенность: **HIGH** для утверждения «мультикатегорийный налог по нутриент-профилю — редкость» (WHO прямо: единственная страна с порогом натрия в нутриент-профильной модели); **MEDIUM** для точного числа аналогов (Колумбия отнесена к точным аналогам по конструкции «единый налог + пороги состава + много категорий», но она адвалорная, а NETA специфическая — это отличие ставки, не базы).
**Вердикт: АНОМАЛИЯ (N=1 ≤ 5).**

---

## U09. МАВРИКИЙ — акциз по содержанию сахара, включая ТВЁРДЫЕ продукты

### Верификация самой меры
- "An excise duty of fifteen cents per gram of sugar is applicable on non-alcoholic beverages containing sugar and non-staple sugar sweetened food products" — Mauritius Revenue Authority (T1), https://www.mra.mu/customs1/more-topics/excise-tax-on-sugar-content-of-sugar-sweetened-non-alcoholic-beverages, доступ 2026-09-04.
- Порог: "...4 grams per 100 grams or 4 grams per 100 millilitres" — там же (T1).
- Более ранняя ставка 6 центов и тот же порог: "the excise duty of 6 cents per gram of sugar shall not apply to: (i) sugar-sweetened products with total sugar content of up to 4 grams per 100" — MRA Communiqué 08.02.2022 (T1), https://www.mra.mu/download/Communique080222.pdf.
- Правовая база расширения на твёрдые продукты: "(b) non-staple sugar sweetened food products; [Inserted 7/2020 ...]" — Excise Act, Laws of Mauritius (T1), https://lawsofmauritius.govmu.org/portal/viewlegislationdocument/web/?doctitle=RXhjaXNlIEFjdA%3D%3D&docnumber=&doctype=act.
- Расширение на шоколад и мороженое: "Excise Duty on sugar content of 12 cents per gram of sugar shall be extended to locally manufactured and imported ..." — MRA (T2, официальный аккаунт MRA в LinkedIn), https://www.linkedin.com/posts/mauritius-revenue-authority-mra_mra-exciseduty-activity-7366353352474996740-2kAW.
- **Статус: действует; ставка повышена до 15 центов за грамм.**

### Таблица стран-аналогов (конструкция: акциз, начисляемый ПО СОДЕРЖАНИЮ САХАРА, на ТВЁРДЫЕ продукты)

| Страна | Точный аналог / похожая / нет | Конструкция | Год / статус | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Кука, Франция, ЮАР, Шри-Ланка | **нет** (только напитки) | налог за грамм сахара / скользящая шкала — исключительно на напитки | до 2020 | https://thedocs.worldbank.org/en/doc/d9612c480991c5408edca33d54e2028a-0390062021/original/World-Bank-2020-SSB-Taxes-Evidence-and-Experiences.pdf | "Five countries have implemented sugar-based taxes to date: the Cook Islands, France, Mauritius, South Africa, and Sri Lanka." | T1 |
| Польша | нет (только напитки) | 0,05 PLN за каждый грамм сахара свыше 5 г/100 мл — напитки | 2021 | https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Poland%20Taxes%20Soft%20Drinks%20and%20Energy%20Drinks_Warsaw_Poland_03-02-2021 | "A variable tax of PLN 0.05 ($0.01) is applied to each gram of sugar over five grams per 100 ml" | T1 |
| Венгрия | похожая | твёрдые продукты облагаются, но по ставке HUF/кг продукта при превышении порогов состава, а не за грамм сахара | 2011, действует | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "specific excise tax applied to a variety of products including snacks ... and pre-packaged sugarsweetened products" | T1 |
| Колумбия | похожая | твёрдые UPF облагаются адвалорно при >10% энергии из свободных сахаров | 2023, действует | https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | ">10% of total energy from free sugars ... tax rates will be 10% in 2023, 15% in 2024 and 20% in 2025" | T2 |
| Мексика | похожая | твёрдые продукты, но база — калорийность (275 ккал/100 г), не сахар | 2014, действует | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Nonessential foods with an energy density of more than 275 kcal per 100 g ... 8% ad valorem excise tax since 2014" | T1 |
| Бермуды | похожая | твёрдые сахарсодержащие продукты, адвалорная импортная пошлина 75% | 2018/2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9379233/ | "the tax base was expanded to include food products containing cocoa" | T1 |
| Дания | похожая | акциз на шоколад/кондитерку/печенье по весу продукта | действует | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Denmark still taxes chocolates, confectionaries, biscuits and cakes via specific excise taxes." | T1 |
| Норвегия | похожая, отменена | 36,92 NOK/кг продукта на шоколад и сахарные изделия | отменён 2021 | https://www.theguardian.com/world/2019/nov/23/norwegian-sugar-tax-confectionery-border-sweden | "levy on chocolate and confectionery was raised by 83% to 36.92 kroner (£3.12) per kilo" | T2 |
| Индия (Керала) | похожая, отменена | 14,5% на брендовый фастфуд, не по составу | 2016-2017 | https://effectivecooperation.org/system/files/2021-06/GDI%20Case%20Study%20on%20Fat%20Tax%20in%20Kerala.pdf | "The Fat Tax was levied only on multinational chains and branded trademark owners" | T2 |

**Итог U09: точных аналогов N = 0 (ни одной другой страны с акцизом «за грамм сахара», распространённым на твёрдые продукты, в открытых источниках не найдено). Похожих мер M = 8 (Венгрия, Колумбия, Мексика, Бермуды, Дания, Норвегия(отм.), Керала(отм.), Финляндия(отм., см. Непроверенное) + группа Cochrane: Доминика, Сент-Винсент, Навахо).**
Источник подсчёта: World Bank 2020 (закрытый список из 5 «сахарных» налогов — все только на напитки), WHO Fiscal policies policy brief Box 6, GFRP Fiscal policies, MRA.
Уверенность: **MEDIUM** (утверждение об отсутствии аналогов — это доказательство отрицания; World Bank явно перечисляет всего 5 стран с sugar-based налогами и все они беверажные, но список датирован январём 2020; полнотекстовые карты GFRP (март 2026) открыть не удалось).
**Вердикт: АНОМАЛИЯ (N=0 ≤ 5). Наиболее уникальная конструкция из четырёх по базе налога.**

---

## U10. ЭФИОПИЯ — Excise Tax Proclamation No. 1186/2020, акциз на маргарин и гидрогенизированные жиры

### Верификация самой меры
- Факт и рамка (T1): "In February 2020, Ethiopia introduced an ad valorem excise tax on imported and locally produced foods, including fats and oils with high levels of saturated or trans-fatty acids, sugar and sugar confectionery" — WHO, Fiscal policies to promote healthy diets: policy brief, Box 6, https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download. Там же ссылка 70: "Excise Tax Proclamation No 1186/2020, Federal Negarit Gazette, 26th Year, No 25, 17 March 2020. Addis Ababa: Ministry of Finance, Ethiopia; 2020."
- Пороги и ставка 50% — подтверждены только копиями текста на T3-ресурсах: "Edible margarine 40g or more saturated fat per 100g, or more than 0.5g of trans fat per 100g. 50%" (https://ethiogermany.de/excise-tax-ethiopia/, T3).
- Правило «нет данных на этикетке»: "40g or more saturated fat per 100g, or more than 0.5g of trans fat per 100g, or unable to a determinate level of saturated fat from label" (https://pdfcoffee.com/ethiopian-tax-law-new-text-book-pdf-free.html, T3). Первичный текст Negarit Gazette в этой сессии открыть не удалось — **эти два элемента помечены как MEDIUM/LOW**.
- Статус: изменён Excise Tax (Amendment) Proclamation No. 1287/2023, вступил в силу 27.04.2023 — "Ethiopia has amended its Excise Tax Proclamation no. 1186, published in 2020, with a 2023 edition. The changes were effective on 27 April 2023" (EY, T2, https://www.ey.com/en_gl/technical/tax-alerts/ethiopia-issues-excise-tax--amendment--proclamation--2023).
- Расхождение по ставке: "Ethiopia's Parliament has decided to disregard a proposal to lift excise duties on imported saturated fat, reinstating the item's 30 percent ..." (The Reporter Ethiopia, T2, https://www.thereporterethiopia.com/33585/). То есть на дату доступа ставка по насыщенным жирам может составлять 30%, а не 50% — расхождение фиксируем, не скрываем.

### Таблица стран-аналогов

Элемент А — акциз, привязанный к содержанию насыщенных/трансжиров с числовым порогом:

| Страна | Точный аналог / похожая / нет | Конструкция | Год / статус | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Дания | похожая (не точный аналог: специфическая ставка за кг жира, а не адвалорно с порогом) | 16 DKK/кг насыщенного жира, порог 2,3% | 2011-2013, отменён | https://www.ft.dk/samling/20101/lovforslag/l111/index.htm | "Afgiften er fastsat til 16 kr. pr. kg mættet fedt ... bagatelgrænse ... 2,3 pct." | T1 |
| Колумбия | **точный аналог по конструкции** (адвалорный налог с числовым порогом по насыщенным жирам) | >10% энергии из насыщенных жиров → 10/15/20% | с 01.11.2023, действует | https://www.globalfoodresearchprogram.org/policy-research/fiscal-policies/ | ">10% of total energy form saturated fats. The tax rates will be 10% in 2023, 15% in 2024 and 20% in 2025." | T2 |
| Венгрия | похожая | насыщенные жирные кислоты как критерий нутриент-профиля NETA только для солёных снеков, ставка HUF/кг | с 2022, действует | https://iris.who.int/server/api/core/bitstreams/296605a9-820a-41bc-8f28-bf4b1367d530/content | "From 2022 the nutrient profile model was complemented with saturated fatty acids for salty snacks" | T1 |
| Тонга | похожая | «high fat foods» по категориям товаров, без порога содержания жира | с 2016 | https://iris.who.int/bitstreams/0bd486d5-7f6e-4532-a392-b7cf59dfd3be/download | "Tonga has imposed an excise tax and/or import duty on high fat foods" | T1 |
| Любая другая страна с налогом по содержанию **трансжиров** | нет | — | — | — | не найдено ни одного примера; глобальные меры по трансжирам — запреты/лимиты, не налоги (WHO REPLACE) | — |

Элемент Б — правило «нет данных на этикетке = облагается / максимальная ставка»:

| Страна | Точный аналог / похожая / нет | Конструкция | Год / статус | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| ЮАР | похожая (тот же принцип, другой нутриент и другой объект) | при отсутствии валидного тест-отчёта презюмируется 20 г сахара/100 мл | Health Promotion Levy, действует | https://www.sars.gov.za/customs-and-excise/excise/health-promotion-levy-on-sugary-beverages/ | "In the absence of such a valid test report, a deemed sugar content of 20 grams per 100 ml is assumed." | T1 |
| Маврикий | похожая (административная) | обязательный сертификат содержания сахара по каждому продукту | действует | https://www.mra.mu/customs1/more-topics/excise-tax-on-sugar-content-of-sugar-sweetened-non-alcoholic-beverages | "certifying the sugar content for each non-staple sugar sweetened food product" | T1 |

**Итог U10: точных аналогов N = 0** (страны с акцизом одновременно по порогу насыщенных жиров ≥40 г/100 г, порогу трансжиров >0,5 г/100 г и правилом «нет данных на этикетке → облагается» не найдено). **Похожих мер M = 5** (Дания — насыщенные жиры; Колумбия — насыщенные жиры с порогом; Венгрия — насыщенные жиры в нутриент-профиле; Тонга — жирные продукты по категориям; ЮАР — правило «нет данных = презумпция максимума»).
Источник подсчёта: WHO Fiscal policies policy brief 2022 (Box 6), WHO Global report on sodium intake reduction (Box 16), Proceedings of the Nutrition Society 2017, GFRP Fiscal policies, SARS.
Уверенность: **MEDIUM** (сама мера подтверждена T1 на уровне «WHO зафиксировал факт налога на жиры с высоким содержанием насыщенных/трансжиров», но числовые пороги 40 г/100 г и 0,5 г/100 г, ставка 50% и формулировка про этикетку получены только из T3-копий текста прокламации; действующая ставка в 2023-2026 гг. расходится: 50% (текст 1186/2020) vs 30% (The Reporter о решении парламента)).
**Вердикт: АНОМАЛИЯ (N=0 ≤ 5).**

---

## СВОДНАЯ ТАБЛИЦА ПО ЧЕТЫРЁМ МЕРАМ

| Мера | Страна | Точных аналогов N | Похожих M | Уверенность | Вердикт |
|---|---|---|---|---|---|
| U07 налог на насыщенные жиры (16 DKK/кг, порог 2,3%) | Дания | **0** | 5 | HIGH | АНОМАЛИЯ (мера отменена 01.01.2013) |
| U08 NETA — единый налог по нутриент-профилю на много категорий | Венгрия | **1** (Колумбия) | 8+ | HIGH / MEDIUM | АНОМАЛИЯ |
| U09 акциз за грамм сахара, распространённый на твёрдые продукты | Маврикий | **0** | 8 | MEDIUM | АНОМАЛИЯ |
| U10 акциз по порогам насыщенных/трансжиров + правило «нет этикетки → облагается» | Эфиопия | **0** | 5 | MEDIUM | АНОМАЛИЯ |

Общий контекст (для контраста): налоги на сладкие НАПИТКИ — распространённая практика (**не менее 116 стран**, WHO, данные 2024). Налоги на ПРОДУКТЫ (не напитки) — **29 государств-членов WHO** (2022). Налоги, привязанные к содержанию сахара, — **~18 налогов с сахарными ступенями** (2022) и **5-6 стран с расчётом за грамм сахара**. Налоги по содержанию насыщенных/трансжиров — единичные случаи (Дания-отменён, Эфиопия, Венгрия-частично, Колумбия-порог).

---

## РАЗДЕЛ «НЕПРОВЕРЕННОЕ» (UNVERIFIED / не подтверждено дословным фрагментом в этой сессии)

1. **Финляндия — налог на сладости и мороженое, отменён с 2017.** Упоминание встречалось в результатах, но дословный фрагмент из T1/T2 с датой отмены и конструкцией не получен. UNVERIFIED — проверить в базе WCRF NOURISHING / Vero.fi.
2. **Точные ставки и пороги эфиопской прокламации (50%, 40 г/100 г, 0,5 г/100 г, формулировка про этикетку).** Подтверждены только копиями на scribd/pdfcoffee/ethiogermany (T3). LOW. Требуется Federal Negarit Gazette, 26th Year, No 25, 17 March 2020.
3. **Действующая ставка Эфиопии на насыщенные жиры после Proclamation No. 1287/2023 (30% или 50%).** Расхождение между текстом 1186/2020 и сообщением The Reporter Ethiopia. LOW.
4. **Карты GFRP «Food taxes» (март 2026, PDF).** Известны URL (https://www.globalfoodresearchprogram.org/wp-content/uploads/2026/03/GFRP-UNC_Tax_maps_foods_2026-March.pdf) и факт обновления, но содержимое PDF получить не удалось — потенциально самый полный перечень стран с продуктовыми налогами остаётся непроверенным.
5. **База WCRF NOURISHING (policydatabase.wcrf.org).** Открылась только корневая страница без страновых записей — постраничный подсчёт по ней не выполнен.
6. **WHO Global report on the use of SSB taxes, 2025 (полный текст, 37 с.).** Из отчёта получена только headline-цифра через пресс-релиз WHO (116 стран) и аннотацию IRIS; разбивка по типам акцизов из издания 2025 г. не извлечена — цифры по конструкциям взяты из издания 2023 г. и JAMA 2023.
7. **Доминика, Сент-Винсент и Гренадины, Навахо (США), Индия** — упомянуты в сводке Cochrane 2020 как страны с налогами на сахар/продукты с добавленным сахаром, но конструкция каждой из них поштучно не верифицирована. LOW.
8. Объёмы поиска / CPC / difficulty по темам — **не измерено, проверить в отдельном инструменте**.

## ЗАФИКСИРОВАННЫЕ ОГРАНИЧЕНИЯ СЕССИИ
- WebSearch недоступен по условию задачи.
- Прямого скрейпинга произвольного URL нет; всё содержимое получено из индекса Firecrawl (описания/highlights), что ограничивает глубину извлечения из больших PDF.
- Доказательства отсутствия аналогов (N=0) по своей природе ограничены охватом использованных источников: WHO IRIS, World Bank, GFRP, PMC/PubMed, национальные налоговые органы (MRA, SARS, Skattestyrelsen, Folketinget), Европейская комиссия.
