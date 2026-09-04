# Проверка уникальности мер U05 / U11 / U16 (маркировка и реклама)

Дата доступа ко всем источникам: **2026-09-04**.
Канал открытия страниц: `mcp__Firecrawl__firecrawl_search` (поле `description` = текст страницы) и `firecrawl_research_*`.
WebSearch недоступен. WebFetch к не-github доменам заблокирован прокси — не использовался.

Уровни источников: T1 — WHO/PAHO, министерства, официальные вестники, правовые базы (FAOLEX, UNEP-LEAP, InfoLEG, IMPO, DOF), рецензируемые статьи; T2 — GFRP/UNC, WCRF, USDA GAIN, отраслевые/НКО-сводки; T3 — соцсети, блоги (только как зацепка).

---

## Базовый счётный каркас (общий для трёх мер)

Основной счётный источник по обязательной FOP-маркировке — рецензируемый обзор:
**Global overview of government-endorsed nutrition labeling policies of packaged foods: a document review** (Front Public Health, 2024), PMC11581873.
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ — T1.

Фрагмент (Results 3.3): «we found that 44 countries have a government-endorsed policy for front-of-pack labeling (FOPL) schemes. Of them, 16 countries have adopted FOPL as mandatory».

**16 стран с ОБЯЗАТЕЛЬНОЙ FOP-маркировкой (Table 5):** Аргентина, Боливия, Бразилия, Канада, Чили, Колумбия, Эквадор, Мексика, Перу, Уругвай, Венесуэла (Америка, n=11); Израиль (Европа); Иран (Вост. Средиземноморье); Шри-Ланка, Таиланд* (Юго-Вост. Азия); Сингапур* (Зап. Тихоокеанский). (* — страна имеет и обязательную, и добровольную схему.)

Фрагмент (Results 3.4): «Of the interpretive approaches, ... the Warning Label in 10 countries, the Nutri-score/Nutri-grade scheme in nine countries, and Traffic Light Labeling (TLL) in two countries» и «The warning label was the most common type of mandatory interpretive system ... Only Israel has the red warning label, and the rest of the country has black, although the shape of the warning label varies from country to country».

Второй счётный источник — **PAHO (2026)**, техническая записка «Best practices for front-of-package food labeling in the Region of the Americas», PAHO/NMH/RF/26-0001, данные на 30 июня 2024.
URL: https://iris.paho.org/bitstreams/4ed78405-64da-4a7e-8b9b-6fa61a530fe1/download — T1.
Фрагменты: «8 countries with front-of-package labeling policies in place»; «Argentina, Chile, Colombia, Mexico, Peru, and Uruguay have adopted the octagonal warning»; «The traffic light system adopted in Ecuador has...»; «...include bans on advertising or sales in schools, such as those implemented in Argentina, Chile, Mexico, and Uruguay».

Пресс-релиз PAHO 10.03.2026: https://www.paho.org/en/news/10-3-2026-new-paho-report-highlights-progress-front-package-food-labeling-americas — T1.
Фрагмент: «In recent years, Argentina, Chile, Colombia, Mexico, Peru, Uruguay, Brazil, and Ecuador have adopted front-of-package labeling systems» и «Currently, more than 30 countries are evaluating or discussing new regulations to introduce this type of warning on food packages».

---

# U05. Сингапур — Nutri-Grade: запрет рекламы по КЛАССУ обязательной маркировки

## Что именно является уникальным элементом
Обязанность привязана не к порогу состава напрямую и не к аудитории, а к **присвоенному классу обязательной маркировки (D)**; запрет рекламы — **тотальный, для всех аудиторий, на всех медиаплатформах**.

## Подтверждение самой меры (Сингапур)

| Элемент | Источник | Фрагмент | Уровень |
|---|---|---|---|
| Обязательная маркировка A–D, маркировка обязательна для C и D | HPB, https://www.hpb.gov.sg/healthy-living/food-and-beverage/nutri-grade/ | «The mandatory nutrition label, called “Nutri-Grade”, has four colour-coded grades. Grade A ... is in green. Grade D ... is in red.» | T1 |
| Тотальный запрет рекламы класса D | HPB, там же | «Advertisements of Nutri-Grade beverages graded "D", are prohibited across all media platforms (e.g. broadcast, print, out-of-home, on-ground, online) except ... point-of-sale (POS) platforms within variety shops» | T1 |
| Разрешена реклама A/B/C и бренд-реклама | HPB, там же | «Brand advertisements that do not feature any particular product, and advertisements that promote the sale of Nutri-Grade beverages graded "A", "B" or "C" are allowed.» | T1 |
| Дата вступления в силу 30.12.2022, норма 184F(2) | MOH, https://www.moh.gov.sg/newsroom/mandatory-nutrition-labelling-and-advertising-prohibitions-for-nutri-grade-beverages-from-30-december-2022/ | «Advertisements related to Nutri-Grade beverages graded “D” are prohibited, except in certain circumstances detailed in regulation 184F(2) as introduced by the Amendment Regulations.» | T1 |
| Расширение на свежеприготовленные напитки с 30.12.2023 | HPB, там же | «**[new from 30 December 2023]** labelled next to freshly prepared beverages listed for sale, such as on physical or online menus at their point of purchase» | T1 |
| Расширение на натрий/насыщенные жиры (SSSIO) с середины 2027 | MOH, https://www.moh.gov.sg/newsroom/nutri-grade-requirements-sodium-and-saturated-fat/ | «The Nutri-Grade labelling requirements and advertising prohibitions will apply to all 23 sub-categories of prepacked salt, sauces, seasonings, instant noodles, and cooking oil (SSSIO) sold in retail settings» | T1 |
| Статус SSSIO-мер | HPB, там же | «the specifications are subjected to World Trade Organisation (WTO) consultations and pending gazettal» — **объявлено, не в силе** | T1 |

## Таблица стран-аналогов U05

| Страна | Вердикт | Что именно обязательно | Год | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Чили | **Похожая мера** (ближайший аналог) | Реклама «altos en» (продуктов с обязательным предупреждением) запрещена на ТВ и в кино кроме 22:00–06:00 и всегда при обращении к детям <14 | 2015 (Ley 20.869), в силе с 2016/2018 | https://faolex.fao.org/docs/pdf/chi150722.pdf | «entre las 22:00 y las 6:00 horas, siempre que no estén dirigidas a menores de catorce años» | T1 |
| Чили (подтверждение уникальности конструкции) | — | Единственная страна, сочетающая контент+аудиторию+время с широким запретом 06:00–22:00 | 2019 (обзор) | https://pmc.ncbi.nlm.nih.gov/articles/PMC7528677/ | «Chile is the only country to combine advertising restrictions on the basis of content ..., audience composition ..., and time, with broad scheduling restrictions extending from 6:00 am to 10:00 pm» | T1 |
| Аргентина | **Похожая мера** | Запрет рекламы/промо/спонсорства продуктов, имеющих ≥1 обязательный «sello de advertencia», **но только направленной на детей и подростков** | 2021 (Ley 27.642) | https://www.argentina.gob.ar/justicia/derechofacil/leysimple/salud/ley-de-etiquetado-frontal | «Está prohibida la publicidad, promoción y patrocinio de los alimentos y bebidas sin alcohol que contengan al menos 1 sello de advertencia dirigida a niños, niñas y adolescentes» | T1 |
| Мексика | **Похожая мера** | Детский маркетинг запрещён для продуктов с обязательными «sellos» (на упаковке); запрет персонажей/мультгероев | 2020 (NOM-051) | https://www.gob.mx/promosalud/acciones-y-programas/etiquetado-de-alimentos | «la NOM 051 prohíbe que los envases contengan personajes infantiles, dibujos animados, celebridades, etc. o elementos interactivos que estén dirigidos a niños y niñas» | T1 |
| Мексика (подтверждение) | — | Привязка к наличию маркировки | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Child-directed marketing is prohibited for products with warning labels» | T1 |
| Перу | **Похожая мера** | Ограничения рекламы для детей <16 лет по тем же порогам, что и октагоны | 2013/2018 | https://faolex.fao.org/docs/pdf/per171696.pdf | «niñas y adolescentes menores de 16 años se encuentran establecidas en los artículos 8, 9 y 10 de la Ley 30021» | T1 |
| Уругвай | **Похожая мера** | Продукты с октагоном нельзя рекламировать и выставлять в учебных заведениях (ограничение по месту, не по медиа) | 2018 (Decreto 272/018) | https://www.gub.uy/ministerio-salud-publica/comunicacion/noticias/fiscalizacion-del-rotulado-frontal | «Decreto del Poder Ejecutivo N° 272/018 que establece que “los alimentos envasados … realizar publicidad ni exhibirse en los centros educativos”» | T1 |
| Эквадор | **Похожая мера** | Реклама продуктов, превышающих пороги (semáforo), запрещена в учебных заведениях | 2014 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7528677/ | «Ecuador (2014) ... Setting: advertising in educational establishments» | T1 |
| Турция | **Похожая мера, другая конструкция** | Продукты «красной»/«оранжевой» категорий Минздрава ограничены в рекламе у детских программ; красная категория — по категориям продуктов, а не по обязательной маркировке на упаковке | 2011/2018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7528677/ | «Ministry of Health places foods into red, orange, and green categories; red categories ... subject to restrictions» | T1 |
| Израиль | **Нет** (маркировка есть, рекламной привязки не найдено) | Обязательная красная предупреждающая маркировка; в открытых источниках привязки запрета рекламы к метке не обнаружено | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Red Warning Logo | Israel (2020) • Ministry of Health • Applicable to all industrially processed packaged solid and liquid foods» | T1 |
| Бразилия, Канада, Венесуэла, Боливия, Иран, Шри-Ланка, Колумбия | **Нет** | Обязательная FOP-маркировка без привязанного к ней запрета рекламы вне школ | 2019–2026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ ; https://iris.paho.org/bitstreams/4ed78405-64da-4a7e-8b9b-6fa61a530fe1/download | PAHO: «bans on advertising or sales in schools, such as those implemented in Argentina, Chile, Mexico, and Uruguay» (Бразилия, Колумбия, Венесуэла не названы) | T1 |

## Итог U05

- **Точных аналогов: 0 стран.** Ни одна другая страна из открытых в этой сессии источников не имеет: (а) обязательной ГРАДУИРОВАННОЙ маркировки (A–D) как классификатора и (б) тотального запрета рекламы для одного класса на всех медиаплатформах для всех аудиторий. Все прочие обязательные градуированные схемы (Nutri-Score) — добровольные (PMC11581873, Table 6: Nutri-Score — France, Belgium, Spain, Austria, Germany, Luxembourg, Portugal, Switzerland, все в разделе «Interpretative voluntary FOPLs»).
- **Похожих мер: 7 стран** — Чили, Аргентина, Мексика, Перу, Уругвай, Эквадор, Турция. Конструкция иная: ограничение по аудитории (дети), по времени суток, по месту (школы) или по медиаканалу, а не тотальный запрет по классу маркировки.
- **Источник подсчёта:** PMC11581873 (обязательные FOPL и их типы), PMC7528677 (сравнение статутных ограничений рекламы), PAHO 2026 (Америка), первичные тексты Сингапура (HPB/MOH), Чили (FAOLEX Ley 20.869), Аргентины (argentina.gob.ar), Мексики (gob.mx), Перу (FAOLEX), Уругвая (gub.uy).
- **Уверенность: HIGH** для факта самой меры Сингапура (два независимых T1: HPB и MOH, открыты дословно). **MEDIUM** для утверждения «0 точных аналогов»: это отрицательный вывод из двух системных обзоров (PMC11581873, PMC7528677) и региональной сводки PAHO 2026; исчерпывающего глобального реестра «реклама по классу маркировки» в открытых источниках нет.
- **Вердикт: АНОМАЛИЯ** (0 точных аналогов ≤ 5).

Отдельно (не проверено до T1): формулировка «Singapore is the first in the world» встречается только в T3-источниках (посты в соцсетях, YouTube-заголовок Channel NewsAsia «in a world first»). В раздел «Непроверенное».

---

# U11. Шри-Ланка — обязательная цветовая маркировка ТОЛЬКО по сахару и ТОЛЬКО для напитков

## Подтверждение самой меры

| Элемент | Источник | Фрагмент | Уровень |
|---|---|---|---|
| Действующая редакция 2022 г., название | eohfs.health.gov.lk (Минздрав Шри-Ланки), Gazette No. 2416/52, https://eohfs.health.gov.lk/food/images/2319-42_E.pdf | «Food (Colour Coding for sugar levels - liquid) Regulations 2022 “amber” means R255, G195 and B9 in Red, Green, Blue colour system (RGB) “red” ...» | T1 |
| Перечень действующих регламентов | https://eohfs.health.gov.lk/food/index.php?option=com_content&view=article&id=18&Itemid=159&lang=en | «Food (Colour coding for sugar levels - liquid) Regulations 2022 No.2416/52, Sinhala · English» | T1 |
| Предмет регулирования — только жидкая готовая к употреблению пища с сахаром | UNEP-LEAP, https://leap.unep.org/en/countries/lk/national-legislation/food-colour-coding-sugar-levels-liquid-regulations-2022 | «They provide for labelling standards for liquid food which is in a ready to drink form and which contain sugar.» | T1 |
| Пороги 2022 г. | USDA GAIN CE2023-0014, https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Sri%20Lanka%20Enacts%20New%20Legislation%20to%20Color%20Code%20Sugar%20Levels%20for%20Liquid%20Food_Colombo_Sri%20Lanka_CE2023-0014.pdf | «More than 8.0g/100 ml. Red. 2.5g to 8.0g/100 ml. Amber. Less than 2.5g/100 ml» | T2 |
| Статус: отсрочка, регламент 2016 г. действовал до 01.07.2025 | USDA GAIN, https://www.fas.usda.gov/data/gain/2025/02/sri-lanka-sri-lanka-extends-implementation-color-coding-sugar-levels-liquid-foods-regulation | «The current Food (Color Coding for Sugar Levels) Regulations (2016) are in place until July 01, 2025, allowing additional time for industry to ...» | T2 |

**Важное уточнение (снижает «чистоту» уникального элемента):** у Шри-Ланки есть ОТДЕЛЬНЫЙ регламент цветового кодирования для твёрдой/полутвёрдой пищи по сахару, соли и жиру.
Источник: USDA GAIN «Food Color Coding for Sugar-Salt-Fat Regulations 2019», https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Food%20Color%20Coding%20for%20Sugar-Salt-Fat%20Regulations%202019_Colombo_Sri%20Lanka_02-05-2020 — фрагмент: «Both locally manufactured and imported foods must be labeled in the manner specified in the regulation for sugar, salt (sodium) and fat» (T2).
Наша оценка: уникальный элемент корректно формулировать как «отдельный обязательный регламент цветового кодирования **сахара** для **жидкой готовой к употреблению** пищи», а не как «в стране цветом маркируется только сахар».

## Таблица стран-аналогов U11 (обязательные цветовые / «светофорные» системы)

| Страна | Вердикт | Что именно обязательно | Год | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| Эквадор | **Похожая мера** (не точный аналог: 3 нутриента, все переработанные продукты, не только напитки) | Обязательный «semáforo»: красный/жёлтый/зелёный по жиру, сахару и соли; отдельные пороги для напитков | 2014 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Nutritional Traffic Light Label | Ecuador (2014) ... classified into red (high), yellow (medium), or green (low) based on levels of salt, sugar, and fat» | T1 |
| Иран | **Похожая мера** (гибридный multiple traffic light, все продукты, соль/сахар/трансжиры) | Обязательная multiple traffic light маркировка Iranian FDA | 2015 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Multiple Traffic Light Labeling | Iran (2015) • Iranian Food and Drug Administration under Food and Beverage Labeling Regulation» | T1 |
| Боливия | **Похожая мера, НЕ внедрена** | Закон о продвижении здорового питания предусматривает цветовое кодирование; на дату обзора не имплементирован | 2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Traffic Light Label | Bolivia (2016) (Not implemented yet) • Healthy Food Promotion Law» | T1 |
| Израиль | **Нет** (не «светофор») | Обязательная КРАСНАЯ предупреждающая метка (бинарная), не трёхцветная шкала | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Only Israel has the red warning label, and the rest of the country has black» | T1 |
| Сингапур | **Похожая мера** (ближайшая по «только напитки»: но 4 класса, сахар + насыщенные жиры) | Обязательная цветовая градуировка A–D только для напитков | 2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Beverage will be graded using a single set of thresholds for sugar and saturated fat content with four color-coded grades (A, B, C, D)» | T1 |
| Великобритания, Ирландия | **Нет** (добровольные) | Multiple traffic light — добровольный | 2013 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «**Hybrid voluntary FOPLs** ... Multiple Traffic Light Label | United Kingdom (2013), Ireland (2013)» | T1 |
| Саудовская Аравия, ОАЭ, Россия, Южная Корея | **Нет** (добровольные) | Multiple traffic light — добровольные схемы | 2011–2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | Все перечислены в разделе «Hybrid voluntary FOPLs» | T1 |

## Итог U11

- **Точных аналогов: 0 стран.** Ни одна другая страна не имеет обязательного цветового кодирования, ограниченного одновременно (а) единственным нутриентом — сахаром и (б) единственной категорией — готовыми к употреблению жидкими продуктами.
- **Похожих мер: 4 страны** — Эквадор (обязательный трёхцветный семафор, 3 нутриента, все переработанные продукты), Иран (обязательный MTL), Сингапур (обязательная цветовая градуировка только напитков, но 2 нутриента и 4 класса), Боливия (принято, не внедрено).
- Обязательные «светофорные»/цветовые системы всего: **2 страны** по классификации PMC11581873 в категории «Traffic Light Labeling» + гибридные обязательные Иран и Шри-Ланка. Фрагмент: «Traffic Light Labeling (TLL) in two countries».
- **Источник подсчёта:** PMC11581873 (Tables 5–6), газет Минздрава Шри-Ланки № 2416/52, UNEP-LEAP, USDA GAIN.
- **Уверенность: MEDIUM.** Причины понижения: (1) расхождение источников (см. ниже); (2) статус вступления в силу редакции 2022 г. после 01.07.2025 в открытых источниках на дату доступа не подтверждён.
- **Вердикт: АНОМАЛИЯ** (0 точных аналогов ≤ 5).

### Зафиксированные расхождения по U11
1. **PMC11581873 vs газета Шри-Ланки.** Обзор в Table 6 описывает Шри-Ланку как «Traffic Light Coding System | Sri Lanka (2019) ... (Only to beverage) ... It is color-coded for sugar, salt, and fat ... Over 22.5 g of sugar, 17.5 g of fat ... per 100 g is colored red». Официальный ггазет 2022 г. называется «Colour Coding for sugar levels - **liquid**» и оперирует порогами **на 100 мл только по сахару** (USDA GAIN: «More than 8.0g/100 ml. Red»). Наша оценка: обзор смешал регламент по твёрдой пище (сахар-соль-жир, 2019) и по жидкой (сахар).
2. **Пороги 2016 vs 2022.** PMC10795608 (https://pmc.ncbi.nlm.nih.gov/articles/PMC10795608/) фиксирует прежние пороги: «red label for drinks that contain more than 11 grams (g) of sugar per 100 millilitres (ml)». Редакция 2022 г. ужесточает: красный >8,0 г/100 мл, янтарный 2,5–8,0, зелёный <2,5. Оба значения корректны для своих периодов.

---

# U16. Чили — Ley 20.606: чёрные восьмиугольники «ALTO EN» + запрет рекламы детям <14 + запрет продаж в школах

## Подтверждение самой меры

| Элемент | Источник | Фрагмент | Уровень |
|---|---|---|---|
| Первенство и тройная конструкция | https://pmc.ncbi.nlm.nih.gov/articles/PMC7012389/ | «Chile's Law of Food Labeling and Advertising, implemented in 2016, was the first national regulation to jointly mandate front-of-package warning labels, restrict child-directed marketing, and ban sales in schools of all foods and beverages containing added sugars» | T1 |
| Восьмиугольник «HIGH IN», пороги, запрет для детей <14 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Chile was the first country to implement the FOP warning label ... This law also prohibits promotions and sales of products carrying warning labels to children under 14» | T1 |
| Правовая база (PAHO, Table 1) | https://iris.paho.org/bitstreams/4ed78405-64da-4a7e-8b9b-6fa61a530fe1/download | «Chile | Law No.20606 on Food Labeling and Advertising, dated 6 June 2012. Decree 13. Amends Supreme Decree No.977 of 1996 ... of 16 April 2015.» | T1 |
| Школы + маркетинг (сводка GFRP) | https://www.globalfoodresearchprogram.org/policy-research/labeling-regulations/ | «“High in” products cannot be marketed, sold, or offered for free at kiosks, cafeterias, and feeding programs at schools and nurseries.» | T2 |

## Таблица стран-аналогов U16

Критерий «точный аналог» = обязательная предупреждающая FOP-маркировка **плюс** ограничение маркетинга, привязанное к этой маркировке, **плюс** запрет продажи/предложения таких продуктов в школах.

| Страна | Вердикт | Что именно | Год | URL | Фрагмент (≤25 слов) | Уровень |
|---|---|---|---|---|---|---|
| **Аргентина** | **ТОЧНЫЙ АНАЛОГ** | Октагоны «EXCESO EN»; запрет рекламы/промо/спонсорства продуктов с ≥1 sello для детей и подростков; запрет продажи и промо в школах | 2021 (Ley 27.642), Decreto 151/2022 | https://www.argentina.gob.ar/justicia/derechofacil/leysimple/salud/ley-de-etiquetado-frontal | «Los alimentos y bebidas analcohólicas que contengan al menos 1 sello de advertencia ... no pueden ser vendidos ni promocionados en los establecimientos educativos» | T1 |
| **Мексика** | **ТОЧНЫЙ АНАЛОГ** | Октагоны «EXCESO EN» (NOM-051, 2020); запрет детского маркетинга у продуктов с sellos; с 29.03.2025 обязательный запрет продажи в школах | 2020 + 2025 | https://www.gob.mx/promosalud/acciones-y-programas/etiquetado-de-alimentos ; https://vidasaludable.gob.mx/storage/recursos/materiales/Manual-cooperativas.pdf | «Dichos Lineamientos entraron en vigor con carácter obligatorio a partir del 29 de marzo de 2025 en todas las escuelas de todos los niveles educativos» | T1 |
| **Уругвай** | **ТОЧНЫЙ АНАЛОГ (частично)** | Октагоны «EXCESO» (Decreto 272/018, в силе с 01.03.2021); продукты с октагоном нельзя рекламировать и выставлять в учебных заведениях. Общенационального запрета детской рекламы вне школ не подтверждено | 2018/2021 | https://www.gub.uy/ministerio-salud-publica/comunicacion/noticias/fiscalizacion-del-rotulado-frontal | «los alimentos envasados … realizar publicidad ni exhibirse en los centros educativos» | T1 |
| **Перу** | **ТОЧНЫЙ АНАЛОГ (частично)** | Октагоны «ALTO EN» (DS 012-2018-SA); ограничения рекламы для детей <16; регулирование школьных киосков в Ley 30021. PAHO 2026 не относит Перу к странам с запретами рекламы/продаж в школах | 2013/2019 | https://faolex.fao.org/docs/pdf/per171696.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «all food and beverages must contain a mandatory white or black warning label» / «menores de 16 años se encuentran establecidas en los artículos 8, 9 y 10 de la Ley 30021» | T1 |
| **Колумбия** | **Похожая мера** | Обязательные предупреждающие sellos (Ley 2120/2021, Res. 2492/2022); ограничения рекламы для детей сформулированы мягче (обязательная информационная «franja», не запрет) | 2021/2022 | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=168029 | «En todo espacio publicitario ... deberán incluir una franja visible o audible que dé cuenta de la información veraz e imparcial que este dirigida a niños, niñas y adolescentes» | T1 |
| **Бразилия** | **Похожая мера** | Предупреждение «ALTO EM» в прямоугольнике с лупой (RDC 429/2020, IN 75/2020); нет привязанных к метке запретов рекламы и продаж в школах | 2020/2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Brazil (2020) ... A rectangle with a black and white magnifying glass and “high in” for added sugar, saturated fat, and sodium» | T1 |
| **Венесуэла** | **Похожая мера** | Октагоны «ALTO EN» по резолюции Минздрава дек. 2021; срок внедрения — до 07.12.2024; сопутствующих рекламных/школьных запретов не подтверждено | 2021/2024 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «The warning label must be octagonal in shape, and the text inside must say “HIGH IN” followed by “SUGAR,” “SATURATED FATS,” “TRANS FATS,” or “SALT”» | T1 |
| **Израиль** | **Похожая мера** | Обязательная КРАСНАЯ (не чёрная восьмиугольная) метка; рекламных/школьных запретов, привязанных к метке, не найдено | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Red Warning Logo | Israel (2020) • Ministry of Health • Applicable to all industrially processed packaged solid and liquid foods» | T1 |
| **Канада** | **Похожая мера** | Чёрно-белая «лупа» «high in», не восьмиугольник; срок соответствия 01.01.2026; рекламных/школьных запретов, привязанных к метке, не найдено | 2022/2026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Health Canada introduced the nutrition labeling regulation on July 2022 • Industry has until January 1, 2026 to comply» | T1 |
| **Эквадор** | **Похожая мера** | Обязательный трёхцветный semáforo (не восьмиугольник); реклама превышающих пороги продуктов запрещена в учебных заведениях | 2014 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7528677/ | «The traffic light system adopted in Ecuador» (PAHO) / «Ecuador (2014) ... Setting: advertising in educational establishments» | T1 |
| **Боливия** | **Похожая мера, не внедрена** | Закон 2016 г., цветовое кодирование; на дату обзора не имплементирован | 2016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11581873/ | «Traffic Light Label | Bolivia (2016) (Not implemented yet)» | T1 |
| Доминиканская Республика | **Проект (не в силе)** | Предложен регламент FOP с чёрным восьмиугольником | 2024 (проект) | https://apps.fas.usda.gov/newgainapi/api/Report/DownloadReportByFileName?fileName=Dominican%20Republic%20Proposes%20Regulation%20for%20Front%20of%20Pack%20Nutritional%20Warning%20Labeling%20for%20Prepackaged%20Foods%20_Santo%20Domingo_Dominican%20Republic_DR2024-0021.pdf | «Warning Label Design: The EFAN will be presented as a black octagon with border, containing white capital letters.» | T2 |

## Итог U16

Три уровня подсчёта (все — по открытым в этой сессии источникам):

1. **Обязательная предупреждающая FOP-маркировка (любой формы) — 10 стран** помимо/включая Чили.
   Источник: PMC11581873, фрагмент: «the Warning Label in 10 countries». Перечень из Table 6: Чили, Уругвай, Перу, Мексика, Израиль, Бразилия, Колумбия, Аргентина, Венесуэла, Канада. → **9 стран кроме Чили**. Это **распространённая практика**.
2. **Именно чёрный ВОСЬМИУГОЛЬНИК «ALTO/EXCESO EN» — 6 стран** (Америка, на 30.06.2024).
   Источник: PAHO 2026, фрагмент: «Argentina, Chile, Colombia, Mexico, Peru, and Uruguay have adopted the octagonal warning». → **5 стран кроме Чили**.
3. **Полная чилийская тройная конструкция (метка + ограничение маркетинга, привязанное к метке + запрет продаж/рекламы в школах) — 4 страны**, из них 3 кроме Чили.
   Источник: PAHO 2026, фрагмент: «...include bans on advertising or sales in schools, such as those implemented in Argentina, Chile, Mexico, and Uruguay». Плюс Перу как частичный аналог (метка + рекламные ограничения для <16, школьное регулирование по Ley 30021 — PAHO в этот перечень Перу не включает).

- **N (точных аналогов): 3–4 страны** — Аргентина, Мексика, Уругвай (по PAHO), с добавлением Перу как спорного четвёртого.
- **M (похожих мер): 8 стран** — Колумбия, Бразилия, Венесуэла, Израиль, Канада, Эквадор, Боливия, Доминиканская Республика (проект).
- **Источник подсчёта:** PAHO 2026 (iris.paho.org, PAHO/NMH/RF/26-0001), PMC11581873, PMC7012389, национальные тексты (argentina.gob.ar, gob.mx/vidasaludable.gob.mx, gub.uy, FAOLEX Peru).
- **Уверенность: HIGH** для счёта «6 стран с восьмиугольником» и «10 стран с предупреждающей меткой» (два независимых T1 согласуются). **MEDIUM** для счёта тройной конструкции (единственный явный перечень — PAHO 2026; Перу и Колумбия классифицируются по-разному в разных источниках).
- **Вердикт (двойной):**
  - По **точной тройной конструкции: АНОМАЛИЯ** — 3–4 точных аналога (≤ 5). Уникальность конструкции в целом сохраняется.
  - По **самой предупреждающей FOP-маркировке: РАСПРОСТРАНЁННАЯ ПРАКТИКА** — 9 стран кроме Чили (> 5). Уникальность отдельного элемента «чёрная предупреждающая метка» утрачена.
  - По **восьмиугольнику**: 5 стран кроме Чили — на границе (≤ 5), формально **АНОМАЛИЯ**, но с явным трендом к распространению (PAHO: «more than 30 countries are evaluating or discussing new regulations»).

### Статус на дату доступа (обязательное различение)
- Чили, Ley 20.606: **в силе** (PAHO 2026 включает Чили в таблицу действующих регламентов; PAHO/NMH/RF/26-0001, Table 1).
- Аргентина, Ley 27.642: **в силе, но под угрозой отмены.** Исполнительная власть внесла в Конгресс законопроект о полной отмене (Expediente 186/26). Источник T2: FIC Argentina, https://www.ficargentina.org/mas-de-300-organizaciones-rechazan-la-derogacion-de-la-ley-de-etiquetado-frontal/ — фрагмент: «A través del proyecto del Poder Ejecutivo N° Expediente 186/26 de ley que propone eliminar la Ley N° 27.642». Есть также документ Палаты депутатов: https://rest.hcdn.gob.ar/web/proyectos/291968/adjuntos/105773 — фрагмент: «La Ley 27.642 de Etiquetado Frontal fue sancionada con el objetivo central de entregar información clara y comprensible al consumidor sobre el contenido». Отмена на дату доступа **не принята**. Уверенность MEDIUM.
- Венесуэла: срок внедрения истёк 07.12.2024; фактическое исполнение по открытым источникам не подтверждено — LOW.
- Канада: срок соответствия 01.01.2026 — по PMC11581873 (данные 2024) значилось «Not implemented yet»; подтверждения фактического исполнения на 2026 г. в этой сессии не получено — LOW.

### Зафиксированные расхождения по U16
1. **Форма метки Колумбии.** PMC11581873 (Table 6): «Colombian Warning Label ... Circular FOPL warning labels are required». PAHO 2026: «Argentina, Chile, Colombia, Mexico, Peru, and Uruguay have adopted the **octagonal** warning». Расхождение не разрешено; приоритет отдан PAHO 2026 как более позднему T1-источнику по региону.
2. **Число стран с обязательной FOPL.** PMC11581873 (данные на авг. 2024): 16 стран мира. PAHO 2026 (на 30.06.2024, только Америка): «8 countries with front-of-package labeling policies in place», при том что Table 5 PMC для Америки даёт 11 (включая Боливию, Канаду, Венесуэлу, которые на тот момент были «не внедрены»). Расхождение объясняется критерием «implemented» vs «adopted».
3. **Аргентинские пороги.** PMC11581873: «No thresholds for critical nutrients were found» для Аргентины, хотя Decreto 151/2022 их содержит: https://www.argentina.gob.ar/normativa/nacional/decreto-151-2022-362577/texto — «Todos aquellos productos que aporten una cantidad igual o mayor a SEISCIENTOS MILIGRAMOS (600 mg) de sodio cada CIEN GRAMOS (100 g) deberán llevar el sello de 'EXCESO EN SODIO'» (T1). Пробел обзора, не расхождение по существу.

---

# Сводная таблица

| Мера | Точных аналогов (N) | Похожих мер (M) | Основной источник подсчёта | Уверенность | Вердикт |
|---|---|---|---|---|---|
| U05 Сингапур Nutri-Grade, запрет рекламы по классу D | **0** | **7** (Чили, Аргентина, Мексика, Перу, Уругвай, Эквадор, Турция) | PMC11581873 + PMC7528677 + PAHO 2026 + HPB/MOH | MEDIUM (отрицательный вывод), HIGH по самой мере | **АНОМАЛИЯ** |
| U11 Шри-Ланка, цвет по сахару только для напитков | **0** | **4** (Эквадор, Иран, Сингапур, Боливия — не внедрена) | PMC11581873 Tables 5–6 + газет № 2416/52 + UNEP-LEAP + USDA GAIN | MEDIUM | **АНОМАЛИЯ** |
| U16 Чили Ley 20.606 — тройная конструкция | **3–4** (Аргентина, Мексика, Уругвай; Перу спорно) | **8** (Колумбия, Бразилия, Венесуэла, Израиль, Канада, Эквадор, Боливия, Дом. Республика) | PAHO 2026 PAHO/NMH/RF/26-0001 + PMC11581873 + PMC7012389 | HIGH по счёту меток, MEDIUM по тройной конструкции | **АНОМАЛИЯ по конструкции в целом; РАСПРОСТРАНЁННАЯ ПРАКТИКА по элементу «предупреждающая FOP-метка» (9 стран кроме Чили)** |

---

# Непроверенное (UNVERIFIED) и ограничения

1. «Сингапур — первая в мире страна, полностью запретившая рекламу напитков с высоким содержанием сахара». Найдено только в T3: посты Facebook (Sugar Kickers, MOH-комментарии), YouTube-заголовок. До T1/T2 не прослежено. Официальные страницы HPB и MOH такой формулировки не содержат.
2. Фактический статус Шри-Ланки после 01.07.2025 (вступила ли в силу редакция 2022 г. или была ещё одна отсрочка) — не подтверждён ни одним открытым в этой сессии источником.
3. Наличие/отсутствие национального запрета маркетинга нездоровых продуктов, привязанного к красной метке, в **Израиле** — прямого подтверждения ни «за», ни «против» не получено; вывод «нет привязки» сделан по умолчанию из PMC11581873 и PAHO (Израиль не упоминается среди стран с такими запретами). Уверенность LOW.
4. Статус школьных ограничений в **Колумбии** по Ley 2120 (есть ли прямой запрет продажи продуктов с sellos в школах) — не открыт дословно. Уверенность LOW.
5. Фактическое исполнение регламентов в **Венесуэле** и **Канаде** на 2026 г. — не подтверждено.
6. Никаких оценок объёма поиска, CPC, difficulty не производилось — **не измерено, проверить в соответствующем инструменте**.
7. Домены `policydatabase.wcrf.org` и `globalfoodresearchprogram.org` открывались через Firecrawl, но выдавали сильно усечённые фрагменты; полные страновые перечни WCRF NOURISHING в этой сессии получить не удалось — зафиксировано как ограничение. Основной вес подсчёта перенесён на PAHO 2026 и PMC11581873.
