# Проверка уникальности мер U18, U23, U24, U25 (доступ к лекарствам)

Дата доступа ко всем источникам: **2026-09-04**.
Канал открытия страниц: `mcp__Firecrawl__firecrawl_search` (поле `description` = извлечённый текст страницы), `mcp__Firecrawl__firecrawl_research_search_papers`.
WebSearch недоступен. Домены вне github/gitlab/pypi для WebFetch заблокированы прокси — WebFetch не использовался.

Определения, применяемые ниже:
- **Точный аналог** — та же обязывающая конструкция и тот же адресат обязанности (напр. «закон устанавливает потолок в деньгах на платёж пациента именно за инсулин», а не «государство оплачивает лекарство целиком»).
- **Похожая мера** — та же тема/цель, другая правовая конструкция (освобождение от платежа, потолок цены производителя, решение агентства HTA вместо нормы закона и т. п.).

---

# U18. США — потолок платежа пациента за инсулин 35 USD/мес в Medicare + законы штатов

## Подтверждение самой меры (базис)

| Что | Год/дата | Источник | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|
| Part D: копей не более 35 USD за месячный запас каждого покрытого инсулина, дедуктибл не применяется | с 01.01.2023 | ASPE/HHS (репринт в NCBI Bookshelf) | https://www.ncbi.nlm.nih.gov/books/NBK616488/ | "have no deductible for covered insulin products and have a copayment cap of $35 per month supply of each covered insulin product" | T1 |
| Part B (инсулин через помпу как DME): тот же потолок | с 01.07.2023 | ASPE/HHS | https://www.ncbi.nlm.nih.gov/books/NBK616488/ | "Effective July 1, 2023, Medicare Part B beneficiaries ... will have a copayment cap of $35 per month supply" | T1 |
| Правовая база — Inflation Reduction Act 2022, обязателен для ВСЕХ планов Part D | 2022/2023 | KFF | https://www.kff.org/medicare/the-facts-about-the-35-insulin-copay-cap-in-medicare/ | "requires all Part D plans to charge no more than $35 per month for all covered insulin products" | T2 (со ссылкой на T1 congress.gov) |
| Предшественник — добровольная модель Part D Senior Savings (2021–2023), участвовало менее половины планов | 2020–2023 | KFF; CMS | https://www.cms.gov/priorities/innovation/innovation-models/part-d-savings-model | "The Inflation Reduction Act caps cost-sharing for each insulin product covered under a Medicare prescription drug plan at $35 for a month's supply, beginning January 1, 2023." | T1 |

Статус на дату доступа: **действует**.

## Сколько штатов США имеют закон о потолке копеймента за инсулин (расхождение источников не скрываем)

| Оценка | Год | Источник | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|
| 29 штатов + округ Колумбия | текущая страница ADA (год публикации на странице не извлечён) | American Diabetes Association | https://diabetes.org/tools-resources/affordable-insulin/state-insulin-copay-caps | "more than half of the states (29 states plus the District of Columbia) have capped insulin copayments in state-regulated commercial health insurance plans" | T2 |
| 29 штатов + Вашингтон, округ Колумбия, к 2026 г.; ~1,04 млн человек | 2026 (охват 2019–2026) | Diabetes Journals (figshare, приложение к статье) | https://diabetesjournals.figshare.com/articles/figure/_b_State_Insulin_Out-of-Pocket_Cap_Policies_and_Estimated_Eligible_Populations_in_the_United_States_2019_2026_b_/32630322 | "By 2026, 29 states and Washington DC had enacted OOP caps on insulin, covering an estimated 1.04 million individuals with diabetes" | T1 (рецензируемый журнал) |
| «29 штатов + D.C.» — со ссылкой на ADA | не указан на извлечённом фрагменте | ASPE/HHS | https://aspe.hhs.gov/reports/insulin-affordability-landscape | "The American Diabetes Association lists 29 states plus D.C. as having insulin cost-sharing caps for state-regulated commercial health insurance plans" | T1 |
| «не менее 26 штатов + D.C.» (более консервативная оценка) | страница NCSL содержит билли 2025 г. (CA SB 40, NV AB 555) | NCSL | https://www.ncsl.org/health/accessing-diabetes-care-and-management | "Policymakers in at least 26 states and the District of Columbia have passed legislation to cap the monthly copayment for insulin." | T1 |
| «25 штатов + D.C. + Medicare Part D» | обращение к 119-му Конгрессу (2025) | ADA | https://diabetes.org/newsroom/press-releases/american-diabetes-association-shares-legislative-priorities-119th-congress | "To date, 25 states, the District of Columbia and Medicare Part D have insulin copay caps in place." | T2 |

**Расхождение:** 25 / 26 / 29 штатов. Причина расхождения — разные даты среза и разные критерии («не менее», принятые vs. вступившие в силу). Наиболее свежая согласованная оценка: **29 штатов + округ Колумбия по состоянию на 2026 г.** (ADA + Diabetes Journals + ASPE согласуются) — уверенность HIGH. NCSL (26+D.C.) формулирует как «не менее», что не противоречит.
Примеры конкретных потолков (ADA, дословно): Connecticut — "$25 cap for 30-day supply of insulin"; District of Columbia — "$30 cap for a 30-day supply of insulin"; Kentucky — "$30 cap for 30-day supply"; Maine, Nebraska, Washington — "$35 cap for 30-day supply"; Vermont — "$100 collective cap for 30-day supply". Разброс потолков 25–100 USD подтверждён также в Health Affairs: "more than twenty states have implemented monthly caps on insulin out-of-pocket spending, ranging from $25 to $100" (https://pmc.ncbi.nlm.nih.gov/articles/PMC11372709/, T1).

## Аналоги в других СТРАНАХ

| Страна | Вердикт | Что именно | Год/статус | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|---|
| Канада | **Похожая мера** | Pharmacare Act (первая фаза национальной фармакопрограммы) — универсальный доступ к лекарствам от диабета; двусторонние соглашения с провинциями дают «first-dollar»-покрытие, т. е. нулевой платёж пациента, а не денежный потолок | закон принят 10.10.2024; соглашения с провинциями 2025 | https://www.canada.ca/en/health-canada/news/2024/10/government-of-canada-passes-legislation-for-a-first-phase-of-national-universal-pharmacare.html ; https://www.canada.ca/en/health-canada/corporate/transparency/health-agreements/national-pharmacare-bilateral-agreements/british-columbia.html | "Pharmacare Act includes universal access to contraception and diabetes medications"; "A regular benefit is eligible for full reimbursement with no out of pocket cost to the patient." | T1 |
| Великобритания (Англия) | **Похожая мера** | Не потолок в деньгах, а полное освобождение от рецептурного сбора: пациент с диабетом на инсулине/лекарствах получает medical exemption certificate и не платит ничего; в Шотландии, Уэльсе, Северной Ирландии рецепты бесплатны всем | режим действует, централизованная проверка введена в сентябре 2014 | https://www.diabetes.org.uk/living-with-diabetes/life-with-diabetes/free-prescriptions ; https://www.nhsbsa.nhs.uk/help-nhs-prescription-costs/medical-exemption-certificates | "If you use insulin or medicine to manage your diabetes, you're entitled to free prescriptions ... you must have a medical exemption certificate"; "Prescriptions are free for everybody in Scotland, Wales and Northern Ireland." | T2 (Diabetes UK) + T1 (NHSBSA) |
| Франция | **Похожая мера** | ALD (affection de longue durée) «диабет» — экзонерация ticket modérateur, покрытие 100 % тарифа Assurance Maladie по связанным с ALD расходам; нет фиксированного потолка именно на инсулин | действует | https://www.ameli.fr/assure/droits-demarches/maladie-accident-hospitalisation/affection-longue-duree-ald/prise-en-charge-ald-exonerante ; https://www.ameli.fr/assure/sante/themes/diabete-adulte/diabete-suivi/surveillance-fondamentaux | "On parle d'exonération du ticket modérateur ou parfois de « prise en charge à 100 % »"; "Les examens et les soins en rapport avec ces maladies sont pris en charge à 100 %" | T1 |
| Бразилия | **Похожая мера** | Программа Farmácia Popular — инсулин человеческий NPH и Regular выдаются бесплатно; с 14.02.2025 бесплатны 100 % позиций перечня | список инсулинов подтверждён 10.07.2024; 100 %-бесплатность с 14.02.2025 | https://www.gov.br/saude/pt-br/composicao/sectics/farmacia-popular ; https://site.cff.org.br/noticia/Noticias-gerais/10/07/2024/novos-medicamentos-passam-a-ser-gratuitos-no-farmacia-popular-a-partir-de-hoje | "Os medicamentos e insumos são fornecidos gratuitamente."; "Insulina Humana NPH 100 UI/ml — suspensão injetável" (в списке бесплатных) | T1 (Минздрав) + T2 (CFF) |
| Индия | **Похожая мера (другая конструкция)** | NPPA/DPCO 2013 устанавливает **потолок розничной цены** (ceiling price) для препаратов из NLEM, включая противодиабетические формуляции. Это потолок цены, а не потолок платежа пациента | ceiling prices зафиксированы для 930 формуляций, в т. ч. 11 противодиабетических (данные PIB) | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2154217 | "NPPA has fixed the ceiling prices for 930 scheduled formulations, including 131 anti-cancer, 11 anti-diabetic and 66 cardiovascular formulations" | T1 |
| Германия, Япония, Мексика, Египет, Иран, Турция | **Не проверено в этой сессии** | В открытых в этой сессии источниках не найдено нормы, устанавливающей денежный потолок платежа пациента именно за инсулин. Общие механизмы (германская Zuzahlung/Belastungsgrenze, японское 30 %-соучастие + высокозатратный потолок) в этой сессии не открывались | — | — | — | UNVERIFIED |

### Итог U18
- **N (точный аналог — страна с законодательно установленным фиксированным денежным потолком платежа пациента именно за инсулин): 0 стран.** Аналог существует только на субнациональном уровне внутри самих США — 29 штатов + округ Колумбия (2026).
- **M (похожая мера): 5 стран** — Канада, Великобритания, Франция, Бразилия, Индия.
- Источник подсчёта: собственный подсчёт по перечисленным выше открытым страницам (ADA, ASPE, NCSL, Diabetes Journals, canada.ca, NHSBSA/Diabetes UK, ameli.fr, gov.br, PIB India).
- Уверенность: **MEDIUM** по отрицательному выводу (проверены 10 кандидатов из задания, 4 не проверены: Германия, Япония, Мексика, Египет, Иран, Турция), **HIGH** по числу штатов США.
- **Вердикт: АНОМАЛИЯ (N = 0 ≤ 5).** Наша оценка: уникальность конструкции обусловлена тем, что в системах с полным госпокрытием потолок платежа пациента не нужен — там платёж просто равен нулю; потолок в деньгах — это ответ на систему соучастия в оплате.

---

# U23. Германия — § 34 Abs. 1 SGB V: законодательное исключение «Lifestyle-Arzneimittel», включая средства для похудения

## Подтверждение самой меры

| Что | Год | Источник | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|
| Норма закона: исключены средства, применяемые преимущественно «zur Abmagerung oder zur Zügelung des Appetits, zur Regulierung des Körpergewichts» | норма введена с 01.01.2004 (по комментарию Haufe) | Gesetze im Internet (официальная правовая база) | https://www.gesetze-im-internet.de/sgb_5/__34.html | "Ausgeschlossen sind insbesondere Arzneimittel, die überwiegend zur Behandlung der erektilen Dysfunktion, ... zur Abmagerung oder zur Zügelung des Appetits, zur Regulierung des Körpergewichts ... dienen." | T1 |
| Это именно **законодательный** запрет назначения (§ 34 Abs. 1 Satz 7 SGB V), исполняемый через Anlage II Arzneimittel-Richtlinie | 2024 | G-BA (пресс-служба) | https://www.g-ba.de/presse/pressemitteilungen-meldungen/1170/ | "Arzneimittel, die zum Abnehmen eingesetzt werden, hat der Gesetzgeber bereits im Jahr 2004 als Leistung der gesetzlichen Krankenversicherung ausgeschlossen." | T1 |
| Wegovy формально внесён в Anlage II (Lifestyle-Arzneimittel); семаглутид по другим показаниям (СД2) под исключение не подпадает | март 2024 | G-BA | https://www.g-ba.de/presse/pressemitteilungen-meldungen/1170/ | "Der G-BA hat den Ausschluss als Kassenleistung heute durch einen Beschluss formal nachvollzogen und Wegovy® ... in der Arzneimittel-Richtlinie (Anlage II – Lifestyle-Arzneimittel) entsprechend gelistet." | T1 |
| Судебное подтверждение действия нормы | решение LSG Niedersachsen-Bremen, L 16 KR 161/26 B ER, публикация 11.05.2026 | Pharmazeutische Zeitung | https://www.pharmazeutische-zeitung.de/gericht-sieht-abnehmspritze-als-lifestyle-medikament-165160/ | "Grundlage ist § 34 Absatz 1 Satz 7 SGB V, der sogenannte Lifestyle-Arzneimittel vom Leistungskatalog der GKV ausschließt." | T2 |

Статус на дату доступа: **действует**.

## Аналоги в других странах

| Страна | Вердикт | Что именно | Год/статус | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|---|
| США | **Точный аналог** | Законодательное (статутное) исключение категории: Social Security Act §1927(d)(2)(A), включённый по ссылке в §1860D-2(e)(2) — Part D не покрывает «agents when used for anorexia, weight loss, or weight gain». Введено Medicare Modernization Act 2003 (P.L. 108-173) | 2003; **статус на 04.09.2026: норма в законе сохраняется, но CMS запустила демонстрацию «Medicare GLP-1 Bridge» с 01.07.2026** | https://www.ssa.gov/OP_Home/ssact/title19/1927.htm ; https://www.congress.gov/crs-product/IF12758 ; https://www.cms.gov/medicare/coverage/prescription-drug-coverage/medicare-glp-1-bridge | "(A) Agents when used for anorexia, weight loss, or weight gain."; "The Medicare Prescription Drug, Improvement, and Modernization Act of 2003 (MMA; P.L. 108-173), which created Part D, excluded drugs used for anorexia, weight loss, or weight gain."; "Starting July 1, 2026, Medicare will begin a short-term demonstration, called the Medicare GLP-1 Bridge" | T1 |
| Республика Корея | **Точный аналог (регуляторный, не парламентский закон)** | Правило Минздрава «국민건강보험 요양급여의 기준에 관한 규칙», [별표 2] «비급여대상», п. 1: услуги, лекарства и расходные материалы, применяемые при перечисленных состояниях, «не мешающих работе или повседневной жизни», не являются страховым благом; в перечне — ожирение (비만, E66) | правило действует; редакция 별표 2 с изменениями 2021 г. | https://www.nhis.or.kr/static/html/wbma/c/wbmac0104.html ; https://law.go.kr/flDownload.do?flSeq=108181433 ; https://m.blog.naver.com/39954/221923978323 | "다음 각목의 질환으로서 업무 또는 일상생활에 지장이 없는 경우에 실시 또는 사용되는 행위·약제 및 치료재료"; в перечне пунктов — "(비만)" | T1 (nhis.or.kr, law.go.kr) + T3 (блог как расшифровка усечённого пункта) |
| Корея — фактическое следствие | подтверждение | Wegovy не покрывается национальным медстрахованием | 2025 | https://www.facebook.com/thekoreatimes/posts/893866276252472/ (Korea Times) | "Wegovy is not covered by Korea's national health insurance, and a month's supply goes for an average of 372,000 won." | T2 |
| Италия | **Похожая мера** | Не законодательное исключение категории, а классификация AIFA: Wegovy, Saxenda и Mounjaro в показании «контроль массы тела» отнесены к классу C — не возмещаются SSN; те же молекулы при СД2 в классе A/PHT возмещаются | публикация AIFA 18.05.2026 | https://www.aifa.gov.it/-/nuovi-farmaci-diabete-obesita-guida-aifa | "farmaci come Wegovy (semaglutide), Saxenda (liraglutide) e Mounjaro ... non sono rimborsati dal SSN e sono classificati in classe C, con costi a carico del cittadino" | T1 |
| Испания | **Похожая мера** | Отказ в финансировании — решение межминистерской комиссии по ценам (CIPM), а не категорическое исключение законом; финансирование семаглутида ограничено монотерапией при СД2 | декабрь 2025 | https://www.publico.es/sociedad/sanidad-rechaza-financiar-adelgazante-mounjaro-ampliar-uso-ozempic.html ; https://www.larazon.es/salud/ministerio-sanidad-niega-financiar-farmacos-adelgazantes-que-oms-declara-esenciales_20251202692f1afb9261f37ec7399335.html | "La Comisión Interministerial de Precios de los Medicamentos (CIPM) ha rechazado financiar el fármaco Mounjaro"; "su financiación está limitada exclusivamente a su uso como monoterapia" | T2 |
| Дания | **Похожая мера** | Отказ агентства в общем (клаузулированном) возмещении: Wegovy не получил generelt klausuleret tilskud; пациент оплачивает полностью | решение Lægemiddelstyrelsen; повторная заявка Novo Nordisk в июле 2025 | https://laegemiddelstyrelsen.dk/da/tilskud/generelle-tilskud/afgoerelser/~/media/BFB0410830804A5DBF87B8EFADCCDE8B.ashx ; https://www.dagenspharma.dk/nyheder/medicin-nyheder/regionerne-har-vetoret-over-for-novos-onske-om-tilskud-til-wegovy/ | Заголовок решения: "Wegovy får ikke generelt klausuleret tilskud"; "I juli 2025, hvor Novo Nordisk igen havde ansøgt om generelt klausuleret tilskud for Wegovy" | T1 + T2 |
| Франция | **Нет (обратный случай)** | С 15.06.2026 Wegovy и Mounjaro возмещаются Assurance Maladie на 65 % при ИМТ ≥ 35 с коморбидностью или ≥ 40; Франция названа первой страной ЕС с постоянным возмещением | арреты от 23.05.2026 и 10.06.2026 (JORF) | https://www.service-public.gouv.fr/particuliers/actualites/A18932 ; https://www.euractiv.com/news/france-becomes-first-eu-country-to-reimburse-wegovy-and-mounjaro/ | "Les 2 traitements médicamenteux de l'obésité (TMO) Wegovy et Mounjaro sont pris en charge par l'Assurance maladie depuis le 15 juin 2026"; "We are the first country in the European Union to provide reimbursement for patients who need it, under general law, on a permanent basis" | T1 + T2 |
| Швейцария | **Нет** | Wegovy включён в Spezialitätenliste с лимитацией (возмещается при выполнении условий) — см. U24 | 01.03.2024, изменение лимитации 01.05.2025 | https://www.bag.admin.ch/dam/de/sd-web/4UEBFvIzBFFM/wegovy-neuaufnahme-01-03-2024.pdf | "Die maximale Therapiedauer einer Monotherapie mit WEGOVY oder einer sequentiellen Therapie mit WEGOVY nach Saxenda beträgt 3 Jahre." | T1 |
| Нидерланды | **Нет** | Liraglutid (Saxenda) возмещается из базового пакета с 01.04.2022 при условиях приложения 2 GVS | 2022, условия расширены 2022 | https://www.zorginstituutnederland.nl/documenten/2022/02/24/gvs-advies-liraglutide-saxenda | "liraglutide (Saxenda®) vanaf 1 april 2022 wordt vergoed uit het basispakket van de zorgverzekering" | T1 |
| Япония | **Нет** | Wegovy внесён в перечень цен NHI (22 ноября), возмещается при выполнении Optimal Use Promotion Guidelines — см. U24 | 2023 | https://pj.jiho.jp/article/249936 | "Novo Nordisk's GLP-1 receptor agonist Wegovy (semaglutide) is finally joining the NHI price list on November 22" | T2 |
| Австрия | **Не подтверждено** | Найдена только вторичная юридическая заметка о том, что Erstattungskodex «никоим образом не исключает» возмещения; законодательного категорического исключения не найдено | — | https://gesundheitsrecht.blog/abnehmspritzen-oesterreich/ | "Erstattungskodex keineswegs ausschließt, dass die Arzneispezialität erstattet werden kann" (фрагмент извлечён усечённым) | LOW / UNVERIFIED |

### Итог U23
- **N (точный аналог — категорическое исключение препаратов для снижения веса из общественного возмещения нормой права, а не решением HTA-агентства по конкретному препарату): 2 страны — США и Республика Корея.** У США — норма федерального статута (SSA §1927(d)(2)(A)); у Кореи — норма министерского правила ([별표 2] к Правилу о стандартах медстраховых благ). Германия — третья страна с такой конструкцией.
- **M (похожая мера — фактическое невозмещение, но решением агентства/классификацией): 3 страны — Италия, Испания, Дания.**
- Не аналоги (возмещают при условиях): Франция (с 15.06.2026), Швейцария, Нидерланды, Япония. Австрия — UNVERIFIED.
- Источник подсчёта: собственный подсчёт по открытым страницам ssa.gov, congress.gov, cms.gov, nhis.or.kr/law.go.kr, gesetze-im-internet.de, g-ba.de, aifa.gov.it, laegemiddelstyrelsen.dk, service-public.gouv.fr, bag.admin.ch, zorginstituutnederland.nl.
- Уверенность: **MEDIUM–HIGH** (США — HIGH: два T1; Корея — MEDIUM: T1-первоисточник открыт, но нужный пункт перечня извлечён усечённым и достроен по T3; Италия/Дания — HIGH; Испания — MEDIUM; Австрия — UNVERIFIED).
- **Вердикт: АНОМАЛИЯ (N = 2 ≤ 5).** Важная оговорка (наша оценка): «невозмещение препаратов для снижения веса» само по себе — распространённая практика (по Euractiv/Reuters Франция стала первой страной ЕС с постоянным возмещением только в июне 2026 г.), но именно **законодательная категорическая конструкция** редка.

---

# U24. Великобритания — NICE TA875 / TA1026: только в специализированной службе управления весом и не дольше 2 лет

## Подтверждение самой меры — с существенной поправкой к формулировке

| Что | Год | Источник | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|
| TA875 (семаглутид, Wegovy): максимум 2 года и только в специализированной службе управления весом | опубликовано 2023 | NICE | https://www.nice.org.uk/guidance/ta875/chapter/1-Recommendations | "it is used for a maximum of 2 years, and within a specialist weight management service providing multidisciplinary management of overweight or obesity (including but not limited to tiers 3 and 4)" | T1 |
| **ПОПРАВКА:** TA1026 (тирзепатид, Mounjaro) — **НЕ** содержит 2-летнего предела и **разрешает** назначение в первичном звене | TA1026 опубликовано 23.12.2024, обновлено позднее | NHS England (interim commissioning guidance) + NICE | https://www.england.nhs.uk/long-read/interim-commissioning-guidance-nice-ta1026-tirzepatide/ ; https://www.nice.org.uk/guidance/ta1026/chapter/1-Recommendations | "Unlike other NICE-recommended weight management medicines, which currently have a maximum prescription duration of 2 years, tirzepatide (Mounjaro®) for the management of obesity, does not have a set 'stopping rule' or maximum treatment period, allowing for indefinite prescribing."; "Tirzepatide can be used in primary care or specialist weight management services." | T1 |

**Вывод по формулировке меры:** утверждение «TA875 / TA1026 — только в специализированной службе и не дольше 2 лет» верно **только для TA875** (и, по NHS England, для прочих рекомендованных NICE средств управления весом согласно NG246). Для TA1026 обе части неверны. Уверенность поправки: **HIGH** (два T1 согласуются).

## Аналоги в других странах (предел ПРОДОЛЖИТЕЛЬНОСТИ терапии GLP-1 в государственной системе)

| Страна | Вердикт | Что именно | Год/статус | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|---|
| Швейцария | **Точный аналог** | Лимитация в Spezialitätenliste (обязательное базовое страхование OKP): максимальная длительность терапии WEGOVY в монотерапии или последовательно после Saxenda — 3 года; требуется согласование | включение 01.03.2024; изменение лимитации 01.05.2025 (срочная/befristet); правила пересмотрены с 01.12.2025 | https://www.bag.admin.ch/dam/de/sd-web/4UEBFvIzBFFM/wegovy-neuaufnahme-01-03-2024.pdf ; https://www.bag.admin.ch/dam/fr/sd-web/zo5pElZKCzLb/WEGOVY%20Limitations%C3%A4nderung%2001.05.2025%20befristet.pdf | "Die maximale Therapiedauer einer Monotherapie mit WEGOVY oder einer sequentiellen Therapie mit WEGOVY nach Saxenda beträgt 3 Jahre. Die Zustimmung des ..." | T1 |
| Япония | **Точный аналог** | Optimal Use Promotion Guidelines (最適使用推進ガイドライン, MHLW): страховое покрытие GLP-1 RA при ожирении требует обязательной 6-месячной коррекции образа жизни, ограничивает терапию 68 неделями (семаглутид 2,4 мг) и 72 неделями (тирзепатид) и предписывает последующий «отмывочный» период; действуют требования к учреждению | OUG ноябрь 2023; листинг NHI 22.11.2023 | https://pubmed.ncbi.nlm.nih.gov/42552238/ ; https://dom-pubs.onlinelibrary.wiley.com/doi/10.1111/dom.15638 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC13327695/ | "Japan's optimal use guideline restricts insurance-reimbursed GLP-1 receptor agonist (GLP-1 RA) therapy for obesity to patients completing a mandatory 6-month lifestyle intervention, caps treatment at 68 weeks (semaglutide 2.4 mg) or 72 weeks (tirzepatide), and mandates subsequent washout."; "Japan imposes a maximum administration duration limit of 68 weeks for the drug" | T1 (рецензируемые статьи; первичный документ MHLW в этой сессии не открыт) |
| Япония — требования к учреждению | подтверждение | Клиники, не соответствующие требованиям OUG (MHLW, ноябрь 2023), отпускают препарат только за собственный счёт пациента | 2023 | https://ikegawa-clinic.com/en/wegovy/ | "Our clinic does not meet the facility requirements of the Guidelines for Optimal Use (MHLW, November 2023), and provides this medication only as self-pay" | T3 (зацепка, подтверждает T1) |
| Нидерланды | **Похожая мера** | Не жёсткий предел, а условие продолжения: после 2 лет хронического применения возмещение сохраняется только если в эти 2 года выполнялись условия Zvw/приложения 2 GVS | версия документа ZN — август 2025 | https://www.zn.nl/znform/vragen-en-antwoorden-vergoeding-farmacotherapie-in-de-behandeling-van-overgewicht-en-obesitas/ ; https://www.knmp.nl/bedrijfsvoering/contractering-en-vergoeding/bijlage-2-voorwaarden | "een verzekerde komt alleen in aanmerking voor vergoeding (ook na 2 jaar chronisch gebruik) als in die 2 jaar aan de Zvw voorwaarden is voldaan"; "Liraglutide (Saxenda) blijft ook na 2 jaar chronisch gebruik vergoed als is gebleken dat ..." | T2 (ZN, KNMP — профильные отраслевые организации) |
| Канада | **Похожая мера** | Рекомендация по возмещению (CDA/CADTH): продолжение возмещения после первого года требует документированного снижения ИМТ или массы тела ≥5 %; это критерий эффективности, а не предельный срок | — | https://www.ncbi.nlm.nih.gov/books/NBK617241/ | "For continuation of reimbursement after the first year of treatment, at least a 5% reduction in BMI or total body weight must be documented." | T1 |
| Франция | **Похожая мера** | Ограничение не по сроку, а по адресату первого назначения: первичное назначение Wegovy/Mounjaro в показании контроля массы тела зарезервировано за специалистами и структурами 2–3 уровня помощи при ожирении (CSO, CHU, SSR-профили) | арреты от 23.05.2026 и 10.06.2026 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054238200 | "la prescription initiale du médicament soit réservée aux professionnels et structures impliqués dans la prise en charge de l'obésité des niveaux de recours 2 et 3" | T1 |
| Дания | **Нет** | Общего возмещения нет вовсе — ограничивать срок нечего (см. U23) | — | https://laegemiddelstyrelsen.dk/da/tilskud/generelle-tilskud/afgoerelser/~/media/BFB0410830804A5DBF87B8EFADCCDE8B.ashx | "Wegovy får ikke generelt klausuleret tilskud" | T1 |
| Норвегия, Швеция, Ирландия, Израиль | **Не проверено** | В открытых в этой сессии источниках не найдено национальной нормы, ограничивающей срок терапии GLP-1 | — | — | — | UNVERIFIED |
| Бахрейн | **Зацепка, не подтверждена** | Сообщение о запуске препарата с формулировкой «на срок максимум два года»; первоисточник не открыт, возможен пересказ британского правила | — | https://www.facebook.com/GDNOnline/posts/1321945506645489/ | "People will only be given semaglutide on prescription … for a maximum of two years" | T3 / UNVERIFIED |
| США (коммерческие планы) | **Похожая мера, но не государственная** | Обзор Tufts CEVR: восемь планов указали срок одобрения от 12 недель до 2 лет — это частная утилизационная политика, не норма госсистемы | — | https://cevr.tuftsmedicalcenter.org/news/how-us-commercial-health-plans-are-covering-semaglutide-wegovy-for-obesity-management-2 | "Eight health plans reported an approval duration for semaglutide. While approval duration was generally short, it varied substantially among plans (12 weeks to 2 years)." | T2 |

### Итог U24
- **N (точный аналог — государственная система, устанавливающая предельную продолжительность терапии GLP-1 при ожирении): 2 страны — Швейцария (3 года) и Япония (68/72 недели).**
- **M (похожая мера — условие продолжения по эффективности или ограничение по типу назначающего, без предельного срока): 4 страны — Нидерланды, Канада, Франция и США (частные планы, вне госсистемы; при строгом счёте только по госсистемам M = 3).**
- Источник подсчёта: собственный подсчёт по bag.admin.ch, PubMed/PMC (Japan OUG), zn.nl/knmp.nl, NCBI Bookshelf (CDA/CADTH), legifrance.gouv.fr, nice.org.uk, england.nhs.uk.
- Уверенность: **MEDIUM** (Швейцария — HIGH, два документа BAG; Япония — MEDIUM: три согласующихся рецензируемых источника, но первичный документ MHLW не открыт; Норвегия/Швеция/Ирландия/Израиль не проверены).
- **Вердикт: АНОМАЛИЯ (N = 2 ≤ 5).** Дополнительно: британская конструкция даже среди аналогов остаётся самой жёсткой по адресату (обязательная специализированная мультидисциплинарная служба), но применительно к тирзепатиду она в Англии уже снята.

---

# U25. Австралия — PBS субсидирует GLP-1 только при СД2 + TGA с 01.10.2024 исключила GLP-1 RA из аптечного компаундирования

## Подтверждение самой меры

| Что | Год/дата | Источник | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|
| Компаундирование: поправки в Therapeutic Goods Regulations 1990 (Schedule 5, item 6) убрали GLP-1 RA из исключения для экстемпорального аптечного изготовления | применяется ко всему изготовленному **с 01.10.2024** | TGA | https://www.tga.gov.au/news/media-releases/update-glucagon-peptide-1-receptor-agonists-glp-1-ras-pharmacy-compounding-changes | "Amendments to the Therapeutic Goods Regulations 1990 (Schedule 5, item 6) have been made resulting in compounded GLP-1 RA products no longer being able to be compounded by pharmacists and supplied to patients."; "These amendments will apply to all medicines containing GLP-1 RA analogues, regardless of dosage form, compounded on or after 1 October 2024." | T1 |
| Мотив и прецедент конструкции (в 2021 г. так же вывели медицинский каннабис) | 2024 | TGA | https://www.tga.gov.au/news/media-releases/consultation-remove-glucagon-peptide-1-glp-1-receptor-agonist-analogues-pharmacist-extemporaneous-compounding-exemption | "In 2021, the extemporaneous compounding exemption was amended to carve out medicinal cannabis products ... Similarly, the TGA is proposing immediate changes to the Regulations to remove all medicines containing GLP-1 RAs from the compounding exemption" | T1 |
| PBS: GLP-1 не субсидируются для похудения | документ PBS (обзор equitable access) | PBS | https://www.pbs.gov.au/reviews/obesity-treatments-files/OBESITY-Consumer-input-summary.PDF | "Currently, GLP-1s are not subsidised through the PBS for the purpose of losing weight. People who want to use GLP-1s to lose weight must pay for the medicines." | T1 |
| В PBS для СД2 включены семаглутид (Ozempic) и дулаглутид (Trulicity); по состоянию на февраль 2026 | 2026 | PBS | https://www.pbs.gov.au/info/reviews/PBAC-advice-equitable-access-to-GLP-1-obesity-treatments | "Two GLP-1s are listed on the PBS for the treatment of type 2 diabetes, semaglutide (Ozempic®) and dulaglutide (Trulicity®). As of February 2026, ..." | T1 |
| Активное правоприменение по назначению вне ограничений PBS | март 2025 | PBS (PSD ноябрь 2025) | https://www.pbs.gov.au/reviews/obesity-treatments-files/Obesity-Treatments-PSD-Nov-2025.PDF | "In March 2025, the Department dispatched over 1,000 letters to medical practitioners who have prescribed semaglutide (Ozempic®) through the PBS to patients with no history of T2DM" | T1 |

Статус на дату доступа: **действует**.

## Аналоги в других странах (запрет/ограничение аптечного компаундирования GLP-1)

| Страна | Вердикт | Что именно | Год/статус | URL | Дословный фрагмент | Уровень |
|---|---|---|---|---|---|---|
| США | **Точный аналог по эффекту, иная конструкция** | (а) После признания дефицита исчерпанным аптеки 503A и производственные объекты 503B утратили право изготавливать «essentially a copy» — с крайними сроками 18.02/19.03.2025 (тирзепатид) и 22.04/22.05.2025 (семаглутид); (б) FDA предложило исключить семаглутид, тирзепатид и лираглутид из перечня 503B bulks list | декабрьские приказы FDA 2024, сроки — 2025; предложение по bulks list — статус «предложение» | https://www.fda.gov/drugs/drug-alerts-and-statements/fda-clarifies-policies-compounders-national-glp-1-supply-begins-stabilize ; https://www.fda.gov/news-events/press-announcements/fda-proposes-exclude-semaglutide-tirzepatide-and-liraglutide-503b-bulks-list ; https://www.fda.gov/media/185526/download | "compounding, distributing or dispensing semaglutide injection products that are essentially a copy of an FDA-approved product within 60 calendar days from today's announcement, until April 22, 2025"; "FDA is proposing to exclude semaglutide, tirzepatide, and liraglutide from the 503B bulks list, finding no clinical need for outsourcing ..."; "FDA has determined that the semaglutide injection product shortage is resolved." | T1 |
| США — дальнейшее ужесточение | подтверждение | FDA объявило о намерении ограничить оборот АФС GLP-1 | статус: объявление о намерении | https://www.fda.gov/news-events/press-announcements/fda-intends-take-action-against-non-fda-approved-glp-1-drugs | "the U.S. Food and Drug Administration is announcing its intent to take decisive steps to restrict GLP-1 active pharmaceutical ingredients ..." | T1 |
| Канада | **Похожая мера** | Позиция Health Canada: несанкционированное изготовление продуктов, продаваемых как компаундированные GLP-1 RA (в первую очередь семаглутид), не допускается; доводится до аптек провинциальными колледжами | позиция Health Canada, распространена провинциальными регуляторами | https://abpharmacy.ca/news/unauthorized-compounding-of-semaglutide-containing-products-is-not-permitted/ ; https://www.bcpharmacists.org/news/health-canada%E2%80%99s-position-unauthorized-manufacturing-products-sold-compounded-glucagon-peptide-1 | Заголовок: "Unauthorized compounding of semaglutide-containing products is not permitted"; "Health Canada has expressed ongoing concerns about compounding of GLP-1 agonists, particularly, but not limited to, semaglutide." | T2 (провинциальные регуляторы, передающие позицию T1) |
| Великобритания | **Нет специальной меры** | Специального изъятия GLP-1 из режима аптечного изготовления не найдено; действует общий запрет незарегистрированного производства + правоприменение MHRA (изъятия, закрытие подпольных производств) | 2025–2026 | https://www.gov.uk/government/news/mhra-urges-public-to-avoid-illegal-online-weight-loss-medicines-this-new-year | "the Medicines and Healthcare products Regulatory Agency (MHRA) is urging ..." (материал о нелегальных онлайн-препаратах для похудения) | T1 (но по существу — правоприменение, не отдельная норма) |
| ЕС (наднационально) | **Не проверено** | В этой сессии не найдено документа ЕМА/ЕС, вводящего специальное ограничение магистрального изготовления GLP-1; регулирование magistral/officinal formulae — национальное | — | — | — | UNVERIFIED |

## Аналоги по второй части меры — субсидирование GLP-1 только при СД2

Эта часть — **распространённая практика**, а не аномалия. Подтверждено в этой сессии для: Италии (класс C для показания «контроль массы тела», класс A/PHT для СД2 — https://www.aifa.gov.it/-/nuovi-farmaci-diabete-obesita-guida-aifa), Испании (финансирование семаглутида ограничено монотерапией при СД2 — https://www.larazon.es/salud/ministerio-sanidad-niega-financiar-farmacos-adelgazantes-que-oms-declara-esenciales_20251202692f1afb9261f37ec7399335.html), Дании (нет общего возмещения Wegovy — https://laegemiddelstyrelsen.dk/da/tilskud/generelle-tilskud/afgoerelser/~/media/BFB0410830804A5DBF87B8EFADCCDE8B.ashx), Германии (§ 34 Abs. 1 SGB V — https://www.g-ba.de/presse/pressemitteilungen-meldungen/1170/), Кореи (https://www.facebook.com/thekoreatimes/posts/893866276252472/), США до 01.07.2026 (https://www.congress.gov/crs-product/IF12758). Косвенное подтверждение общей картины: Франция стала первой страной ЕС с постоянным возмещением только 15.06.2026 (https://www.euractiv.com/news/france-becomes-first-eu-country-to-reimburse-wegovy-and-mounjaro/, T2; https://www.reuters.com/legal/litigation/france-reimburse-weight-loss-drugs-mid-june-health-minister-says-2026-05-28/, T2).

### Итог U25
- Часть «TGA — исключение GLP-1 RA из аптечного компаундирования»: **N (точный аналог) = 1 страна (США)**; **M (похожая мера) = 2 страны (Канада; Великобритания — только через общий режим и правоприменение).** ЕС — UNVERIFIED.
  Существенное различие конструкций (наша оценка): Австралия внесла прямую поправку в подзаконный акт (Therapeutic Goods Regulations 1990, Sch. 5, item 6) с постоянным изъятием класса препаратов; США пришли к тому же эффекту через истечение статуса дефицита и предложение по 503B bulks list, т. е. более обратимым путём.
- Часть «PBS субсидирует GLP-1 только при СД2»: **распространённая практика** — подтверждено минимум для 6 юрисдикций (Италия, Испания, Дания, Германия, Корея, США до 01.07.2026).
- Источник подсчёта: собственный подсчёт по tga.gov.au, pbs.gov.au, fda.gov, abpharmacy.ca/bcpharmacists.org, gov.uk.
- Уверенность: **MEDIUM** (Австралия и США — HIGH, два и более T1; Канада — MEDIUM, T2 со ссылкой на позицию Health Canada; ЕС не проверен).
- **Вердикт по компаундированию: АНОМАЛИЯ (N = 1 ≤ 5). Вердикт по PBS-ограничению «только СД2»: РАСПРОСТРАНЁННАЯ ПРАКТИКА (> 5 юрисдикций).**

---

# Сводная таблица

| Мера | N точных аналогов (страны) | M похожих мер (страны) | Вердикт |
|---|---|---|---|
| U18 (потолок 35 USD на платёж пациента за инсулин) | 0 (только 29 штатов США + D.C. субнационально) | 5 (Канада, Великобритания, Франция, Бразилия, Индия) | Аномалия |
| U23 (законодательное исключение средств для похудения из возмещения) | 2 (США, Республика Корея) | 3 (Италия, Испания, Дания) | Аномалия |
| U24 (предел продолжительности терапии GLP-1 в госсистеме) | 2 (Швейцария 3 года, Япония 68/72 недели) | 3–4 (Нидерланды, Канада, Франция; + США как частная практика) | Аномалия |
| U25 (изъятие GLP-1 из аптечного компаундирования) | 1 (США) | 2 (Канада, Великобритания) | Аномалия |
| U25 (субсидирование GLP-1 только при СД2) | ≥ 6 | — | Распространённая практика |

---

# Фактические поправки к формулировкам мер

1. **U24, TA1026.** Утверждение «TA1026: только в специализированной службе управления весом и не дольше 2 лет» **неверно**. NHS England: "Unlike other NICE-recommended weight management medicines, which currently have a maximum prescription duration of 2 years, tirzepatide (Mounjaro®) ... does not have a set 'stopping rule' or maximum treatment period, allowing for indefinite prescribing" (https://www.england.nhs.uk/long-read/interim-commissioning-guidance-nice-ta1026-tirzepatide/, T1). NICE: "Tirzepatide can be used in primary care or specialist weight management services" (https://www.nice.org.uk/guidance/ta1026/chapter/1-Recommendations, T1). Двухлетний предел и требование специализированной службы верны для **TA875 (семаглутид)**. Уверенность поправки: HIGH.
2. **U23, статус США.** Статутное исключение сохраняется, но с **01.07.2026** действует демонстрация CMS «Medicare GLP-1 Bridge»: "Starting July 1, 2026, Medicare will begin a short-term demonstration, called the Medicare GLP-1 Bridge" (https://www.cms.gov/medicare/coverage/prescription-drug-coverage/medicare-glp-1-bridge, T1); "Beginning July 1, Medicare beneficiaries with Part D coverage may be eligible to access certain GLP-1 medications at $50 for a monthly supply" (https://www.cms.gov/newsroom/press-releases/coming-soon-cms-provide-50-monthly-access-glp-1-medications-medicare-beneficiaries, T1). То есть американский аналог U23 на дату доступа частично нейтрализован демонстрационной программой.
3. **U23, статус Франции.** Франция, фигурировавшая как кандидат в «исключающие», с 15.06.2026 **возмещает** Wegovy и Mounjaro (65 %) — аналогом U23 не является.

---

# Непроверенное (UNVERIFIED) и зафиксированные ограничения

| Пункт | Почему не подтверждено |
|---|---|
| U18: наличие/отсутствие потолка платежа пациента именно за инсулин в Германии, Японии, Мексике, Египте, Иране, Турции | Целевые страницы в этой сессии не открывались; общие потолки соучастия (герм. Belastungsgrenze, яп. высокозатратный потолок) не проверялись. Отрицательный вывод по этим 6 странам — не установлен |
| U23: Австрия | Найден только вторичный юридический блог с усечённым фрагментом; норма Erstattungskodex/ASVG не открыта |
| U23: Испания — наличие категорического исключения ожирения в RD 1663/1998 / RD 1348/2003 | Тексты BOE в этой сессии открывались только заголовками; дословный фрагмент со словом «obesidad» не получен |
| U24: Норвегия, Швеция, Ирландия, Израиль | Национальных норм о пределе срока терапии GLP-1 в открытых источниках не найдено; отсутствие не доказано |
| U24: Бахрейн | Единственная зацепка — пост в соцсети (T3), первоисточник не открыт |
| U25: ЕС/EMA | Наднационального ограничения магистрального изготовления GLP-1 не найдено; не доказано отсутствие |
| Данные по объёму поиска / CPC / difficulty | Не измерено — проверить в специализированном инструменте |

Все выводы о «распространённости»/«аномалии» — наша оценка на основе перечисленных выше открытых источников, а не результат исчерпывающего обследования всех стран мира.
