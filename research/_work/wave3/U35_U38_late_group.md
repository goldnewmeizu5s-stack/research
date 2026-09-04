# U35-U38 (late group). Проверка уникальности четырёх мер

Дата работы: 2026-09-04. Все источники открыты в этой сессии через `mcp__Firecrawl__firecrawl_search`
(текст страницы приходит в поле `description`/`highlights`). WebSearch/WebFetch в контейнере недоступны
(egress-политика), поэтому все дословные фрагменты - из поля `description` результатов Firecrawl.

Ограничение метода, зафиксировано честно: Firecrawl возвращает фрагмент страницы, а не полный текст.
Там, где фрагмент обрывался и число/перечень не удалось получить дословно, утверждение помечено
UNVERIFIED и вынесено в раздел "Непроверенное" внутри меры.

---

## Мера 1. A-US-4. США, FMCSA: допуск водителей коммерческого транспорта на инсулине (49 CFR 391.46, форма MCSA-5870, срок 45 дней)

### Что именно проверяем (конструкция-эталон)
Национальная норма, которая: (а) разрешает водителям коммерческого транспорта на инсулине работать;
(б) делает это на основании **стандартизованной формы/заключения врача**; (в) с **ограниченным сроком
действия** этого документа; (г) **вместо индивидуальных разрешений (exemption)**.

### Базовая мера (США) - подтверждено
| Пункт | Данные |
|---|---|
| Норма | 49 CFR § 391.46 |
| Фрагмент (T1, Cornell LII) | "(1) The medical examiner must receive a completed Insulin-Treated Diabetes Mellitus Assessment Form, MCSA-5870, signed and dated by the individual's treating ..." |
| URL | https://www.law.cornell.edu/cfr/text/49/391.46 |
| Срок 45 дней (T1, GovInfo CFR-2018) | "At least annually, but no later than 45 days after the treating clinician signs and dates the Insulin-Treated Diabetes Mellitus Assessment Form, MCSA-5870, an ..." |
| URL | https://www.govinfo.gov/content/pkg/CFR-2018-title49-vol5/pdf/CFR-2018-title49-vol5-sec391-46.pdf |
| Статус | Действует; FMCSA (T1): "diabetes mellitus are no longer absolutely prohibited from driving commercial motor vehicles in interstate commerce." URL: https://www.fmcsa.dot.gov/medical/driver-medical-requirements/qualifications-drivers-diabetes-standard-83-fr-47486-sept-19 |
| Форма 45 дней (T1, FMCSA) | "ITDM individuals are required to provide the ITDM Assessment Form, MCSA-5870, to the Certified Medical Examiner within 45 days of completion by ..." URL: https://www.fmcsa.dot.gov/regulations/medical/insulin-treated-diabetes-mellitus-assessment-form-mcsa-5870 |

### Таблица стран-кандидатов

| Страна | Вердикт | Что за норма | Год/статус | URL | Дословный фрагмент (<=25 слов) | T |
|---|---|---|---|---|---|---|
| **ЕС (27 гос-в) как блок** | точный аналог по конструкции (не по форме) | Директива 2006/126/EC, Annex III, п. 10.3 (в ред. Commission Directive 2009/113/EC, 2016/1106): группа 2 на инсулине допускается при заключении компетентного медоргана и регулярном медпересмотре не реже 1 раза в 3 года | действует (текст открыт в редакции, размещённой на legislation.gov.uk как retained EU law) | https://www.legislation.gov.uk/eudr/2006/126/annexes/data.xht?view=snippet&wrap=true | "Consideration may be given to the issuing/renewal of group 2 licences to drivers with diabetes mellitus." + "such licences should be issued subject to the opinion of a competent medical authority and to regular medical review, undertaken at intervals of not more than three years." | T1 |
| **Великобритания** | точный аналог | DVLA: группа 2 (bus/lorry) на инсулине лицензируется на 1 год, обязательна форма VDIAB1I и осмотр каждые 12 мес независимым консультантом-диабетологом | действует; страница обновлена 26.09.2025 | https://www.gov.uk/guidance/diabetes-mellitus-assessing-fitness-to-drive | "attend an examination every 12 months by an independent consultant specialist in diabetes" | T1 |
| **Великобритания (форма)** | - | форма VDIAB1I | действует | https://diabetesonthenet.com/diabetes-primary-care/how-to-assess-fitness-to-drive-apr-2026/ | "Must stop driving and notify the DVLA when insulin treatment is started. Complete form VDIAB1I." | T2 |
| **Ирландия** | точный аналог (по конструкции ближе всех к США: форма с коротким сроком годности) | Медицинская форма для NDLS, заполненная в течение предыдущего месяца, для водителей на инсулине | действует | https://www.diabetes.ie/living-with-diabetes/living-type-1/driving-type-1-diabetes/ | "you must present a completed medical form (completed within the previous month)" | T2 |
| **Ирландия (правила ЕС в нацприменении)** | - | воспроизведение Annex III | действует | https://www.diabetes.ie/living-with-diabetes/living-type-1/driving-type-1-diabetes/ | "Driving licences shall not be issued to, or renewed, for applicants or drivers who have recurrent severe hypoglycaemia, 1-3-year licence" | T2 |
| **Ирландия (гос. подтверждение формы)** | - | NDLS: медицинский отчёт при отдельных состояниях | действует | https://www.ndls.ie/medical-fitness/do-i-need-to-submit-a-medical-report.html | "Some medical conditions require a report from your doctor, read our guidelines to see if you need one before applying for your licence" | T1 |
| **Канада** | точный аналог | CCMTA National Safety Code Standard 6 - Determining Driver Fitness; национальный стандарт медфитнеса для частных и коммерческих водителей; раздел "7 - Diabetes and hypoglycemia" с критериями допуска коммерческого водителя | действует; страница обновлена 05.12.2024 | https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/roadsafetybc/medical-fitness/medical-prof/med-standards/7-diabetes | "Commercial driver eligible for a licence if: Has demonstrated good knowledge of the condition and its management and monitoring and assessment" | T1 |
| **Канада (национальный характер стандарта)** | - | CCMTA | действует | https://www.ccmta.ca/en/national-safety-code | "CCMTA has developed a standard entitled National Safety Code (NSC) Standard 6 - Determining Driver Fitness. It addresses both private and commercial drivers." | T1 |
| **Австралия** | точный аналог | Austroads "Assessing Fitness to Drive" (AP-G56) - национальные медстандарты для частных и коммерческих водителей; условная лицензия при инсулине с периодическим пересмотром специалистом | действует | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/diabetes-mellitus/medical-standards-for-licensing-2 | "For commercial drivers receiving insulin treatment, at least three months of blood glucose monitoring records should be reviewed in assessing fitness to drive." | T1 |
| **Австралия (механизм условной лицензии)** | - | Austroads | действует | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/cardiovascular-conditions/medical-standards-for-licensing-1 | "For a conditional licence to be issued, the health professional must provide to the driver licensing authority details of the medical criteria not met" | T1 |
| **Новая Зеландия** | точный аналог (нижняя уверенность) | NZTA: ежегодная медоценка для классов 2-5 и эндорсментов P,V,I,O при диабете на инсулине | действует | https://t2dm.nzssd.org.nz/Section-100-Diabetes-and-driving | "annual assessment is required for class 2,3,4 and 5 licence applications or P,V,I or O endorsements for all people with type 2 diabetes on insulin" | T2 |
| **Гибралтар** | точный аналог (транспонирование ЕС) | Traffic (Third Driving Licence Directive) Regulations 2012 | действует | https://www.gibraltarlaws.gov.gi/legislations/traffic-third-driving-licence-directive-regulations-2012-3064/download | "interval should not exceed five years. 10.2. Driving licences shall not be issued to, nor renewed for, applicants or drivers who have ..." | T1 |
| **Япония** | похожая мера (не подтверждено детально) | Дорожный закон Японии ужесточён для диабетиков; конструкция формы не установлена | не установлен | https://pmc.ncbi.nlm.nih.gov/articles/PMC5089940/ | "The regulations of driver's license for diabetic patients have been tightened in Japan and EU countries recently for public safety." | T2 |
| **Южная Корея** | не установлено | - | - | - | страница с национальной нормой не открыта в этой сессии | - |

### Ключ к подсчёту: ЕС как блок
Annex III п. 10.3 - **минимальный обязательный стандарт**, который все государства-члены ЕС обязаны
транспонировать. Конструкция "инсулинозависимый водитель группы 2 допускается при заключении
компетентного медоргана + регулярный пересмотр с ограниченным сроком (<=3 года)" существует
не менее чем в 27 странах ЕС плюс Великобритания и Гибралтар.
Норвегия/Исландия/Лихтенштейн (EEA) - **не проверено в этой сессии**.

### Итог по мере 1
- **Точных аналогов N = не менее 31**: 27 государств-членов ЕС (через обязательную Директиву 2006/126/EC
  Annex III п. 10.3), плюс Великобритания, Канада, Австралия, Новая Зеландия.
  По формальному критерию "открытая в этой сессии национальная страница": дословно подтверждено
  6 юрисдикций (Великобритания, Ирландия, Канада, Австралия, Новая Зеландия, Гибралтар)
  + текст обязывающей Директивы для остальных стран ЕС.
- **Похожих мер M = 1** (Япония).
- **Источник подсчёта**: текст Annex III Директивы 2006/126/EC (перечень адресатов = все государства-члены
  ЕС) + национальные страницы GOV.UK, gov.bc.ca/CCMTA, Austroads, NDLS/diabetes.ie, NZSSD, Gibraltar Laws.
  Обзор Beshyah et al., Br J Diabetes 2017;17:3-10 ("Information on licensing was obtained from 85
  countries. No restrictions on drivers with insulin-treated diabetes existed in 59 countries (69.4%)",
  https://www.bjd-abcd.com/index.php/bjd/article/view/228, T2) - подтверждает массовость регулирования,
  но разбивка по коммерческому транспорту в открытом фрагменте обрывается.
- **Уверенность: MEDIUM-HIGH.** HIGH для вывода "конструкция распространена"; MEDIUM для точного числа.
- **ВЕРДИКТ: РАСПРОСТРАНЁННАЯ ПРАКТИКА (N > 5).**

### Что уникально именно в мере США (наша оценка, гипотеза)
Уникален не допуск, а **отказ от индивидуальных exemption в пользу единой федеральной формы**.
FMCSA (T1): "This rule revises the FMCSRs to permit individuals with a stable insulin regimen and properly
controlled ITDM to be qualified to operate CMVs in interstate ..."
(https://www.regulations.gov/document/FMCSA-2005-23151-1487). **45-дневного** срока годности формы
в других странах в этой сессии не найдено; ближайшее - Ирландия ("в течение предыдущего месяца").

### Непроверенное (мера 1)
- Южная Корея, Япония: национальные нормы не открыты. UNVERIFIED.
- Разбивка Beshyah et al. по LGV/PCV. UNVERIFIED.
- Транспонирование Annex III в странах EEA. UNVERIFIED.

---

## Мера 2. A-IT-1. Италия, Legge 149/2025: признание ожирения хроническим заболеванием ЗАКОНОМ

### Что именно проверяем (конструкция-эталон)
Ожирение признано хроническим заболеванием **актом парламента (законом)**, а не приказом министерства,
решением медассоциации или страховщика.

### Базовая мера (Италия) - подтверждено
| Пункт | Данные |
|---|---|
| Акт | Legge 3 ottobre 2025, n. 149 "Disposizioni per la prevenzione e la cura dell'obesita" |
| Публикация | Gazzetta Ufficiale, 09.10.2025, id 25G00158 (https://www.gazzettaufficiale.it/eli/id/2025/10/09/25G00158/sg - страница открыта, но текст в выдаче Firecrawl пустой) |
| Вступление в силу | 24.10.2025 (T3, ildiritto.it): "Obesita: in vigore dal 24 ottobre 2025 la legge per la cura e la prevenzione riconoscendola come malattia cronica." https://ildiritto.it/amministrativo/obesita-cosa-prevede-la-proposta-di-legge/ |
| Содержание (T2, Bollettino ADAPT) | "La presente legge riconosce formalmente l'obesita come malattia cronica, progressiva e recidivante, conferendo dignita a questa condizione e ..." https://www.bollettinoadapt.it/la-legge-3-ottobre-2025-n-149-il-riconoscimento-dellobesita-come-malattia-cronica/ |
| Наблюдательный орган | Osservatorio per lo Studio dell'Obesita (OSO), ст. 4. T3: "La legge 149 del 2025 riconosce l'obesita come malattia cronica, istituisce un programma nazionale di prevenzione e un osservatorio." https://farmaciavirtuale.it/legge-sullobesita-fondi-e-strategie-nellatto-in-gu/ |

### Таблица стран-кандидатов

| Страна | Вердикт | Что за норма | Год/статус | URL | Дословный фрагмент (<=25 слов) | T |
|---|---|---|---|---|---|---|
| **Колумбия** | **ТОЧНЫЙ АНАЛОГ** | Ley 1355 de 2009 (Congreso de Colombia), ст. 1: объявляет ожирение хроническим заболеванием общественного здоровья; создаёт межсекторную комиссию CISAN (ст. 15-17) | принят 14.10.2009, Diario Oficial 47502; действует (изменён Ley 2294 de 2023 в части состава CISAN) | https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=37604 | "Articulo 1°. Declarase. La obesidad como una enfermedad cronica de Salud Publica, la cual es causa directa de enfermedades cardiacas, circulatorias" | T1 |
| **Колумбия (подтверждение 2)** | - | Gestor Normativo, Funcion Publica | действует | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=37604 | "Define la obesidad y las enfermedades cronicas no transmisibles asociadas a esta como una prioridad de salud publica y adopta medidas para su control" | T1 |
| **Португалия** | похожая мера (НЕ закон) | Despacho n.º 4571/2005 (2.ª serie) - распоряжение министерства | 02.03.2005, Diario da Republica | https://diariodarepublica.pt/dr/detalhe/despacho/4571-2005-2044965 | "A obesidade e uma doenca cronica, com genese multifactorial, que requer esforcos continuados para ser controlada" | T1 |
| **Португалия (продолжение линии)** | похожая мера | Despacho n.º 12634/2023 - интегрированная модель в SNS | 2023 | https://www.sns.gov.pt/noticias/2023/12/11/novo-modelo-para-prevencao-e-tratamento-da-obesidade-no-sns/ | "O Ministerio da Saude decidiu reforcar a resposta a obesidade, criando pela primeira vez um programa de resposta integrada a esta doenca cronica" | T1 |
| **Германия** | похожая мера (постановление парламента, НЕ закон) | Бундестаг 07.2020 принял Antrag CDU/CSU и SPD (Drs. 19/20619) о нацстратегии по диабету | принято 07.2020 | https://www.bundestag.de/webarchiv/textarchiv/2020/kw27-de-diabetes-strategie-701742 | "Juli 2020, den Start einer nationalen Diabetes-Strategie begrusst, als er bei Enthaltung der Oppositionsfraktionen einen Antrag von CDU/CSU und SPD ... annahm." | T1 |
| **Германия (характер решения)** | - | DDG | 07.2020 | https://www.ddg.info/diabetes-zeitung/ddg-06/2022/adipositas-eine-krankheit-mit-folgen | "Die Entscheidung im Juli 2020 gilt als Meilenstein: Die Anerkennung der Adipositas als eigenstandige Krankheit durch den Bundestag." | T2 |
| **Канада** | похожая мера (медассоциация + провинция, НЕ федеральный закон) | CMA признала ожирение хроническим заболеванием; Альберта - 2025 (уровень провинции) | CMA - дата на открытой странице отсутствует; Альберта - 2025 | https://obesitycanada.ca/understanding-obesity/obesity-recognized-chronic-disease/ | "Canadian Medical Association (CMA). 'The Canadian Medical Association recognizes obesity as a chronic disease.'" | T2 |
| **США** | похожая мера (решение медассоциации, НЕ закон) | American Medical Association, 2013 | 2013 | https://www.medscape.com/viewarticle/880560 | "Obesity is currently recognized as a disease in the United States (by the American Medical Association in 2013), Canada (by the Canadian Medical ...)" | T2 |
| **Швеция** | похожая мера (министерство, НЕ закон) | Sweden, Ministry of Health - в перечне Obesity Canada | не установлен | https://obesitycanada.ca/understanding-obesity/obesity-recognized-chronic-disease/ | "Portugal, Ministry of Health. Portugal blazed a trail when it recognized ..." (Sweden в том же перечне) | T2 |
| **Австрия** | похожая мера (нацсистема лечения, не признание законом) | ВОЗ-Европа о строительстве национальной системы лечения ожирения | 08.09.2022 | https://www.who.int/europe/de/news/item/08-09-2022-time-to-accept-that-obesity-is-a-disease---austria-is-building-a-national-system-to-treat-it | заголовок: "Es ist Zeit zu erkennen, dass Adipositas eine Krankheit ist" | T1 |
| **Чили** | похожая мера (законопроект + резолюция палаты) | Boletin 14725-11: проект закона, объявляющий ожирение болезнью | законопроект 01.12.2021; закон НЕ принят по открытым источникам | https://www.bcn.cl/obtienearchivo?id=recursoslegales/10221.3/65175/4/14725-11_20211201.pdf | "Proyecto de ley que declara de interes nacional la prevencion y control de los trastornos alimentarios, y establece la obesidad como enfermedad." | T1 |
| **Эквадор** | похожая мера (законопроект в процессе) | Проект закона о профилактике и комплексном лечении ожирения; комиссия одобрила доклад к первому чтению | первое чтение; закон НЕ принят | https://www.asambleanacional.gob.ec/es/noticia/116937-comision-de-salud-aprueba-informe-para-primer-debate | "La propuesta reconoce a la obesidad como una enfermedad cronica no transmisible, sistemica, multifactorial, recurrente y progresiva, y establece ..." | T1 |
| **Румыния** | похожая мера (позиция министерства) | Ministerul Sanatatii | дата акта не установлена | https://www.politicidesanatate.ro/ministerul-sanatatii-obezitatea-o-boala-cronica-ce-necesita-interventii-sustinute-pe-termen-lung/ | "Obezitatea nu este doar un stil de viata sau o problema estetica, ci o boala cronica recunoscuta la nivel international" | T2 |
| **Мексика** | нет | Ley General de Salud реформирована декретами по теме "sobrepeso, obesidad y trastornos de la conducta alimentaria", но объявления ожирения болезнью в открытых фрагментах нет | реформы 2020, 2022 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LGS.pdf | "DECRETO por el que se reforman y adicionan diversas disposiciones de la Ley General de Salud, para prevenir el sobrepeso, la obesidad y los trastornos de la conducta ..." | T1 |
| **Испания** | нет | Только предложения "Alianza por la Obesidad" в Конгрессе и требование нацстратегии | 2025 | https://diariofarma.com/2025/02/18/la-alianza-por-la-obesidad-demanda-mejorar-la-financiacion-y-acceso-a-tratamientos-innovadores | "Pacientes y expertos reclaman a la Comision de Sanidad del Congreso una Estrategia Nacional de Atencion Integral a la Obesidad." | T2 |
| **Польша** | нет | Закона нет; есть пилотная программа KOS-BAR по распоряжению министра здравоохранения | с 2021, пилот до 06.2026 | https://www.gov.pl/web/zdrowie/program-kompleksowej-opieki-medycznej-dla-chorych-na-otylosc-olbrzymia-leczona-chirurgicznie | "Powstaly zalozenia KOS-BAR, czyli programu kompleksowej opieki medycznej nad pacjentami chorymi na otylosc olbrzymia leczona chirurgicznie." | T1 |

### Итог по мере 2
- **Точных аналогов N = 1** (Колумбия, Ley 1355 de 2009 ст. 1 - акт Конгресса + межсекторный орган CISAN).
  Расхождение источников, которое НЕ скрываем: EASO (T2) и The Conversation (T2) называют итальянский
  закон первым в мире / первым в Европе, но колумбийская Ley 1355/2009 (T1) содержит формулу
  "Declarase. La obesidad como una enfermedad cronica de Salud Publica" за 16 лет до этого.
  Наша оценка: корректно - Италия первая **в Европе** и первая с таким объёмом гарантий (включение в LEA),
  но не первая в мире по факту законодательного признания.
- **Похожих мер M = 9**: Португалия, Германия, Канада, США, Швеция, Австрия, Чили, Эквадор, Румыния.
- **Мексика, Испания, Польша - "нет"** по открытым источникам.
- **Источник подсчёта**: перечень стран задан заданием; проверка по национальным правовым базам
  (alcaldiabogota.gov.co, funcionpublica.gov.co, diariodarepublica.pt, bundestag.de, diputados.gob.mx,
  bcn.cl, asambleanacional.gob.ec, gov.pl) + перечень организаций Obesity Canada + EASO / The Conversation.
- **Уверенность: MEDIUM-HIGH.** HIGH по Колумбии, Португалии, Германии (открыты первичные документы).
  MEDIUM по полноте: систематической базы "страны, где ожирение признано законом" не существует
  в открытом виде; проверено 10 стран из задания + Эквадор, Швеция, Австрия, Румыния, Чили.
- **ВЕРДИКТ: АНОМАЛИЯ (N = 1 <= 5).**

### Фрагмент, ограничивающий распространённость (T2)
The Conversation (https://theconversation.com/obesity-is-now-legally-recognised-as-a-chronic-disease-in-italy-a-historic-advance-for-public-health-in-europe-269305):
"To date, no other European country has enacted a national law that recognises obesity with such breadth";
там же: "Germany's Bundestag recognised obesity as a medical and social disease in 2020, as part of its
National Diabetes Strategy."

### Непроверенное (мера 2)
- Полный текст Legge 149/2025 в Gazzetta Ufficiale - страница вернула пустой контент; формулировка ст. 1
  взята из вторичных источников. MEDIUM.
- Мексика: возможное признание в NOM или в непоказанном фрагменте LGS. UNVERIFIED.
- Румыния: Legea 163/23.10.2025 (https://legislatie.just.ro/Public/DetaliiDocumentAfis/303706) - предмет
  закона во фрагменте не виден, связь с ожирением НЕ подтверждена. UNVERIFIED.
- Швеция: конкретный акт министерства не открыт. UNVERIFIED.

---

## Мера 3. A-IT-2. Италия, imposta sul consumo delle bevande edulcorate (L. 160/2019, commi 661-676): принята в 2019, восемь переносов, не вступила в силу

### Базовая мера (Италия) - подтверждено
| Пункт | Данные | Источник |
|---|---|---|
| Норма | Legge 27 dicembre 2019, n. 160, art. 1, commi 661-676 | Il Sole 24 Ore (T2): "The 2020 Relaunch Decree had first postponed the entry into force of the sugar tax to 1 January 2021. ... 1, paragraphs 661-676, Law No." https://en.ilsole24ore.com/art/first-round-the-economy-decree-and-seventh-postponement-the-sugar-tax-AHQqPMzB |
| Число переносов | 8 переносов за 5 лет | Osservatorio CPI (T2, Univ. Cattolica): заголовок "Plastic Tax e Sugar Tax: otto rinvii in cinque anni"; текст: "Dal 2020 viene rinviata l'introduzione di due imposte, la Plastic Tax e la Sugar Tax, nate per ridurre il consumo di ..." https://osservatoriocpi.unicatt.it/ocpi-pubblicazioni-plastic-tax-e-sugar-tax-otto-rinvii-in-cinque-anni |
| Один из переносов (парламентский документ) | с 01.07.2025 на 01.01.2026 | Senato della Repubblica, Dossier n. 259, XIX лег. (T1): "L'articolo dispone la proroga dal 1° luglio 2025 al 1° gennaio 2026 della data di entrata in vigore dell'imposta sul consumo delle bevande edulcorate (c.d. ..." https://www.senato.it/show-doc?id=1463045&leg=19&tipodoc=DOSSIER&part=dossier_dossier1-sezione_sezione8-h4_h49 |
| Текущая дата вступления | 01.01.2027 | FISCOeTASSE (T3): "La Legge di Bilancio 2026 in vigore dal 1° gennaio ha differito l'entrata in vigore della plastic tax e della sugar tax al 1° gennaio 2027." https://www.fiscoetasse.com/new-rassegna-stampa/2409-sugar-e-plastic-tax-differimento-al-1-gennaio-2027.html ; IPSOA (T2): "Il Ddl di Bilancio 2026 (A.S. 1689) rinvia al 1° gennaio 2027 l'entrata in vigore di plastic e sugar tax." https://www.ipsoa.it/documents/quotidiano/2025/11/10/sugar-plastic-tax-2027-rinvio-preludio-abrogazione |
| Статус | принята 2019, НЕ вступила в силу на дату доступа | см. выше |

### Таблица стран-кандидатов

| Страна | Вердикт | Что за норма | Год/статус | URL | Дословный фрагмент (<=25 слов) | T |
|---|---|---|---|---|---|---|
| **Индонезия** | **ТОЧНЫЙ АНАЛОГ** | Акциз на упакованные подслащённые напитки (cukai MBDK): включён в закон о госбюджете (APBN), но многократно перенесён (2023 -> 2024 -> 2025) и не введён | не введён на дату публикаций | https://pmc.ncbi.nlm.nih.gov/articles/PMC12039701/ | "However, the implementation of this policy has repeatedly been delayed, with the latest postponement to 2024." | T1 (рецензируемая статья) |
| **Индонезия (подтверждение: зафиксировано в бюджете, не применено)** | - | APBN | 2022 | https://www.globalcompliancenews.com/2022/07/14/indonesia-indonesian-government-is-proposing-to-impose-excise-on-sugar-sweetened-beverages-29062022/ | "Although it has been stipulated in the APBN, excise on MBDK has not yet been implemented." | T2 |
| **Индонезия (перенос за 2025)** | - | Минфин | 2025 | https://www.amcham.or.id/news/detail/amcham-update-vol-6-64 | "Indonesia's Ministry of Finance has confirmed that the excise tax on sweetened packaged beverages will not be implemented in 2025." | T2 |
| **Эстония** | похожая мера (принят парламентом, НЕ вступил в силу, но не из-за переносов, а из-за отказа президента промульгировать) | Закон о налоге на подслащённые напитки, принят Riigikogu в 2017 | не вступил в силу; новый законопроект - вступление ожидается 2026 | https://www.chinimandi.com/estonia-to-introduce-sugar-tax/ | "However, this legislation never came into force as former President Kersti Kaljulaid declined to promulgate the law, citing constitutional ..." | T3 |
| **Эстония (подтверждение отказа)** | - | - | 2017 | https://bnn-news.com/estonian-president-refuses-to-proclaim-sugar-tax-law-as-granting-unjustified-advantage-167971 | "The President of Estonia, Kersti Kaljulaid, has this week returned to the Riigikogu a law that would have set in place a tax on sweetened drinks" | T2 |
| **Эстония (правительственное одобрение)** | - | Обсерватория ВОЗ/Европа | 29.05.2017 | https://eurohealthobservatory.who.int/monitors/health-systems-monitor/updates/hspm/estonia-2018/government-approves-the-tax-on-soft-drinks-in-estonia-to-combat-obesity-and-raise-funds | "Government approves the tax on soft drinks in Estonia to combat obesity and raise funds. 29 May 2017" | T1 |
| **Израиль** | похожая мера (введён, затем ОТМЕНЁН - другая конструкция) | Налог на подслащённые напитки принят парламентом 11.2021, введён 01.2022, отменён 01.2023 | отменён | https://healthpolicy-watch.news/israels-decision-to-revoke-sugar-tax-is-grievous-blow-to-public-health/ | "Israeli government decision to cancel the country's sweetened beverage tax, which was only passed in November 2021. The SSB tax was removed in ..." | T2 |
| **Израиль (подтверждение 2)** | - | ВОЗ-обсерватория | 2023 | https://eurohealthobservatory.who.int/monitors/health-systems-monitor/updates/hspm/israel-2015/sugar-beverage-tax-cancelled-after-one-year-of-implementation | заголовок раздела: "Sugar beverage tax cancelled after one year of implementation" | T1 |
| **ЮАР** | похожая мера (налог ДЕЙСТВУЕТ; переносились повышение и расширение) | Health Promotion Levy действует с 2018; повышение на 4,5% отложено на год; распространение на соки анонсировано | действует | https://news.bloombergtax.com/daily-tax-report-international/south-africa-postpones-increase-in-sugar-tax-presented-in-budget | "South African Treasury proposes that implementation of a 4.5% increase in the levy on sugar-sweetened drinks be postponed by a year to April ..." | T2 |
| **ЮАР (подтверждение переноса 2022)** | - | SAMJ/SciELO | 04.2022 | https://scielo.org.za/scielo.php?script=sci_arttext&pid=S0256-95742022000900005 | "In a surprising move in April 2022, the government postponed the implementation of this increase to allow for broader consultation." | T2 |
| **Бразилия** | похожая мера (принят 2025, вступление 2027 - плановая отсрочка, не серия переносов) | Imposto Seletivo на подслащённые напитки, Lei Complementar n. 214 de 16.01.2025 (ст. 409, Anexo XVII), созданный EC 132/2023 | принят 16.01.2025; вступление с 01.01.2027 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm | "LEI COMPLEMENTAR Nº 214, DE 16 DE JANEIRO DE 2025" | T1 |
| **Бразилия (дата вступления)** | - | юр. обзор | 2027 | https://www.barbieriadvogados.com/imposto-seletivo/ | "A cobranca do imposto seletivo comeca em 1º de janeiro de 2027" | T2 |
| **Вьетнам** | похожая мера (принят 2025, вступление 2027 - плановая отсрочка) | Law on Special Consumption Tax No. 66/2025/QH15, принят Нацсобранием 14.06.2025 | 8% с 01.01.2027, 10% с 01.01.2028 | https://www.vietnam-briefing.com/news/vietnam-updates-special-consumption-tax-system-new-compliance-starts-in-2026.html/ | "Sugar-sweetened beverages of over 5g sugar/100ml, as per TCVN | - From January 1, 2027: 8%; and - From January 1, 2028: 10%." | T2 |
| **Вьетнам (акт)** | - | LuatVietnam | 14.06.2025 | https://english.luatvietnam.vn/legal-updates/law-on-special-consumption-tax-2025-no-66-2025-qh15-enacted-892-103032-article.html | "66/2025/QH15 on Special Consumption Tax is passed by the National Assembly on June 14, 2025, and will take effect from January 1, 2026." | T2 |
| **Филиппины** | нет (налог введён и действует) | Sweetened Beverage Tax, TRAIN Law, с 2018 | действует | https://pmc.ncbi.nlm.nih.gov/articles/PMC6357562/ | "The tax rate was set to 6.00 Philippine pesos (0.111 United States dollars) per litre of sweetened beverages." | T1 |
| **Нигерия** | нет (налог введён и действует) | Finance Act 2021, акциз N10/литр, подписан 31.12.2021, применяется с 2022 | действует | https://www.populationmedicine.eu/Taxation-on-beverages-in-Nigeria-Impact-and-burden-of-the-new-policy,146129,0,2.html | "The Nigerian Government recently signed into a law a policy on 31 December 2021 that mandates the payment of an excise duty of 10 NGN ... per liter" | T2 |
| **Индия** | нет (действует через GST + cess с 01.07.2017) | 28% GST + 12% cess на газированные напитки с сахаром | действует | https://thedocs.worldbank.org/en/doc/d9612c480991c5408edca33d54e2028a-0390062021/original/World-Bank-2020-SSB-Taxes-Evidence-and-Experiences.pdf | "India | July 1, 2017 | GST | 40%(28% GST+12% cess-tax upon a tax) | Includes aerated waters and drinks containing added sugar" | T1 |
| **Шри-Ланка** | нет (акциз введён 11.2017, снижен 12.2018) | Специфический акциз на сахар | действует, ставка снижена | https://thedocs.worldbank.org/en/doc/d9612c480991c5408edca33d54e2028a-0390062021/original/World-Bank-2020-SSB-Taxes-Evidence-and-Experiences.pdf | "Sri Lanka | US$50 per gram sugar excise tax in effect since November 2017 lowered to US$30 per gram (40%) in December 2018 | Industry lobbying, domestic politics" | T1 |

### Итог по мере 3
- **Точных аналогов N = 1** (Индонезия: налог закреплён в законе о госбюджете, многократно перенесён,
  спустя годы не введён). С оговоркой: в Индонезии инструментом является закон о бюджете + необходимость
  подзаконного акта, а не отдельный налоговый закон, как в Италии. Наша оценка: конструкция
  "принято - многократно перенесено - не действует" совпадает.
- **Похожих мер M = 6**: Эстония (принят парламентом, не промульгирован, не вступил в силу),
  Израиль (введён и отменён через год), ЮАР (налог действует, но повышение/расширение переносились),
  Бразилия (принят 2025, вступление 2027), Вьетнам (принят 2025, вступление 2027),
  Финляндия (по FTM - налог на сладости отменён после жалоб в Еврокомиссию; фрагмент:
  "In Finland, a tax on sweets and ice cream was eventually scrapped following complaints to the European
  Commission, while in Estonia a similar levy collapsed after the industry threatened to take the matter
  to Brussels", https://www.ftm.eu/articles/industry-lobby-sugar-taxes-postponed-cancelled, T2).
- **Индия, Филиппины, Нигерия, Шри-Ланка - "нет"** (налоги введены и действуют).
- **Источник подсчёта**: World Bank "Taxes on Sugar-Sweetened Beverages: Summary of International
  Evidence and Experiences" (сводная таблица по странам, T1); Osservatorio CPI и Senato (Италия, T1/T2);
  рецензируемая статья по Индонезии (T1); FTM-расследование по Европе (T2).
  Систематической базы "принятые, но не вступившие в силу налоги на сладкие напитки" не существует -
  подсчёт собран вручную по страновым источникам. Это ограничение.
- **Уверенность: MEDIUM.** Первичные тексты открыты для Бразилии (Planalto) и Италии (Senato-дossier);
  по Индонезии - рецензируемая статья + два вторичных подтверждения. Полнота перечня не гарантирована:
  проверены 8 стран из задания + Эстония, Бразилия, Вьетнам, Финляндия.
- **ВЕРДИКТ: АНОМАЛИЯ (N = 1 <= 5).**
  Отдельно отметим: даже среди аналогов Италия выделяется числом переносов - **восемь за пять лет**
  (Osservatorio CPI), при том что закон принят 27.12.2019.

### Непроверенное (мера 3)
- Текст L. 160/2019, commi 661-676 в Gazzetta Ufficiale не открыт; ссылка на статью взята из Il Sole 24 Ore
  и дossier Сената. MEDIUM.
- Полный список стран из "Global report on the use of sugar-sweetened beverage taxes, 2025" (WHO,
  https://www.who.int/publications/i/item/9789240118942) - страница открыта, но перечень стран
  с отменёнными/невведёнными налогами во фрагменте отсутствует. UNVERIFIED.
- FTM-статья закрыта пейволлом после первого абзаца; страны Portugal, Denmark, Norway упомянуты
  в аннотации, но конструкция их мер не проверена. UNVERIFIED.

---
