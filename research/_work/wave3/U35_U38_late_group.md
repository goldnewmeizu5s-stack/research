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
| **Канада** | точный аналог | CCMTA National Safety Code Standard 6 - Determining Driver Fitness; национальный стандарт медфитнеса для частных и коммерческих водителей; отдельный раздел "7 - Diabetes and hypoglycemia" с критериями допуска коммерческого водителя | действует; страница обновлена 05.12.2024 | https://www2.gov.bc.ca/gov/content/transportation/driving-and-cycling/roadsafetybc/medical-fitness/medical-prof/med-standards/7-diabetes | "Commercial driver eligible for a licence if: Has demonstrated good knowledge of the condition and its management and monitoring and assessment" | T1 |
| **Канада (национальный характер стандарта)** | - | CCMTA | действует | https://www.ccmta.ca/en/national-safety-code | "CCMTA has developed a standard entitled National Safety Code (NSC) Standard 6 - Determining Driver Fitness. It addresses both private and commercial drivers." | T1 |
| **Австралия** | точный аналог | Austroads "Assessing Fitness to Drive" (AP-G56) - национальные медицинские стандарты для частных и коммерческих водителей; условная лицензия (conditional licence) при инсулине с периодическим пересмотром специалистом | действует | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/diabetes-mellitus/medical-standards-for-licensing-2 | "For commercial drivers receiving insulin treatment, at least three months of blood glucose monitoring records should be reviewed in assessing fitness to drive." | T1 |
| **Австралия (механизм условной лицензии)** | - | Austroads, гл. по условным лицензиям | действует | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/cardiovascular-conditions/medical-standards-for-licensing-1 | "For a conditional licence to be issued, the health professional must provide to the driver licensing authority details of the medical criteria not met" | T1 |
| **Новая Зеландия** | точный аналог (нижняя уверенность) | NZTA: ежегодная медицинская оценка для классов 2-5 и эндорсментов P,V,I,O при диабете на инсулине | действует | https://t2dm.nzssd.org.nz/Section-100-Diabetes-and-driving | "annual assessment is required for class 2,3,4 and 5 licence applications or P,V,I or O endorsements for all people with type 2 diabetes on insulin" | T2 |
| **Гибралтар** | точный аналог (транспонирование ЕС) | Traffic (Third Driving Licence Directive) Regulations 2012 | действует | https://www.gibraltarlaws.gov.gi/legislations/traffic-third-driving-licence-directive-regulations-2012-3064/download | "interval should not exceed five years. 10.2. Driving licences shall not be issued to, nor renewed for, applicants or drivers who have ..." | T1 |
| **Япония** | похожая мера (не подтверждено детально) | Дорожный закон Японии был ужесточён для диабетиков; конструкция формы не установлена | не установлен | https://pmc.ncbi.nlm.nih.gov/articles/PMC5089940/ | "The regulations of driver's license for diabetic patients have been tightened in Japan and EU countries recently for public safety." | T2 |
| **Южная Корея** | не установлено | - | - | - | страница с национальной нормой не открыта в этой сессии | - |

### Ключ к подсчёту: ЕС как блок

Annex III п. 10.3 - это **минимальный обязательный стандарт**, который все государства-члены ЕС обязаны
транспонировать. То есть конструкция "инсулинозависимый водитель группы 2 допускается при заключении
компетентного медоргана + регулярный пересмотр с ограниченным сроком (<=3 года)" существует
не менее чем в 27 странах ЕС плюс Великобритания (сохранила норму), Гибралтар.
Норвегия/Исландия/Лихтенштейн (EEA) - **не проверено в этой сессии**.

### Итог по мере 1

- **Точных аналогов N = не менее 31**: 27 государств-членов ЕС (через обязательную Директиву 2006/126/EC
  Annex III п. 10.3), плюс Великобритания, Канада, Австралия, Новая Зеландия.
  Если считать только по формальному критерию "явно открытая в этой сессии национальная страница":
  подтверждено дословно 6 юрисдикций (Великобритания, Ирландия, Канада, Австралия, Новая Зеландия,
  Гибралтар) + текст обязывающей Директивы для остальных стран ЕС.
- **Похожих мер M = 1** (Япония - тема та же, конструкция не установлена).
- **Источник подсчёта**: (1) текст Annex III Директивы 2006/126/EC (даёт перечень адресатов - все
  государства-члены ЕС); (2) национальные страницы GOV.UK, gov.bc.ca/CCMTA, Austroads, NDLS/diabetes.ie,
  NZSSD, Gibraltar Laws. Обзор Beshyah et al., Br J Diabetes 2017;17:3-10 ("Information on licensing was
  obtained from 85 countries. No restrictions on drivers with insulin-treated diabetes existed in 59
  countries (69.4%)", https://www.bjd-abcd.com/index.php/bjd/article/view/228, T2) подтверждает, что
  тема регулируется во множестве стран, но его разбивка по коммерческому транспорту в открытом
  фрагменте обрывается.
- **Уверенность: MEDIUM-HIGH.** HIGH для факта, что конструкция распространена (открыт обязывающий
  текст Директивы + 6 национальных источников, из них 5 - T1). MEDIUM для точного числа: перечень
  27 стран ЕС выведен из юридической силы Директивы, а не из 27 открытых национальных документов.
- **ВЕРДИКТ: РАСПРОСТРАНЁННАЯ ПРАКТИКА (N > 5).**

### Что уникально именно в мере США (наша оценка, гипотеза)
Уникален не сам допуск, а **отказ от индивидуальных exemption в пользу единой федеральной формы**:
FMCSA (T1) фиксирует смену режима - "This rule revises the FMCSRs to permit individuals with a stable
insulin regimen and properly controlled ITDM to be qualified to operate CMVs in interstate ..."
(https://www.regulations.gov/document/FMCSA-2005-23151-1487). Ни в одном из открытых источников по
другим странам не найдено именно **45-дневного срока годности формы**. Это - наша оценка, а не факт из
источника; страны с числовым сроком годности формы, кроме Ирландии ("в течение предыдущего месяца"),
в этой сессии не найдены.

### Непроверенное (мера 1)
- Южная Корея: национальная норма не открыта. UNVERIFIED.
- Япония: конкретная норма (статья закона, форма, срок) не открыта. UNVERIFIED.
- Полный текст Beshyah et al. по коммерческому транспорту (число стран без ограничений для LGV/PCV) -
  фрагмент обрывается на "in ...". UNVERIFIED.
- Страны EEA (Норвегия, Исландия, Лихтенштейн) - транспонирование Annex III не проверено. UNVERIFIED.

---

## Мера 2. A-IT-1. Италия, Legge 149/2025: признание ожирения хроническим заболеванием ЗАКОНОМ

### Что именно проверяем (конструкция-эталон)
Ожирение признано хроническим заболеванием **актом парламента (законом)**, а не приказом министерства,
решением медицинской ассоциации или страховщика.

### Базовая мера (Италия) - подтверждено
| Пункт | Данные |
|---|---|
| Акт | Legge 3 ottobre 2025, n. 149 "Disposizioni per la prevenzione e la cura dell'obesita" |
| Публикация | Gazzetta Ufficiale, 09.10.2025, id 25G00158 (https://www.gazzettaufficiale.it/eli/id/2025/10/09/25G00158/sg - страница открыта, но текст в выдаче Firecrawl пустой) |
| Вступление в силу | 24.10.2025 (T2/T3, ildiritto.it): "Obesita: in vigore dal 24 ottobre 2025 la legge per la cura e la prevenzione riconoscendola come malattia cronica." URL: https://ildiritto.it/amministrativo/obesita-cosa-prevede-la-proposta-di-legge/ |
| Содержание (T2, Bollettino ADAPT) | "La presente legge riconosce formalmente l'obesita come malattia cronica, progressiva e recidivante, conferendo dignita a questa condizione e ..." URL: https://www.bollettinoadapt.it/la-legge-3-ottobre-2025-n-149-il-riconoscimento-dellobesita-come-malattia-cronica/ |
| Наблюдательный орган | Osservatorio per lo Studio dell'Obesita (OSO), ст. 4; программа + осс. орган: "La legge 149 del 2025 riconosce l'obesita come malattia cronica, istituisce un programma nazionale di prevenzione e un osservatorio." URL: https://farmaciavirtuale.it/legge-sullobesita-fondi-e-strategie-nellatto-in-gu/ (T3) |

### Таблица стран-кандидатов

| Страна | Вердикт | Что за норма | Год/статус | URL | Дословный фрагмент (<=25 слов) | T |
|---|---|---|---|---|---|---|
| **Колумбия** | **ТОЧНЫЙ АНАЛОГ** | Ley 1355 de 2009 (Congreso de Colombia), ст. 1: объявляет ожирение хроническим заболеванием общественного здоровья; создаёт межсекторную комиссию CISAN (ст. 15-17) | принят 14.10.2009, опубликован Diario Oficial 47502; действует (изменён Ley 2294 de 2023 в части состава CISAN) | https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=37604 | "Articulo 1°. Declarase. La obesidad como una enfermedad cronica de Salud Publica, la cual es causa directa de enfermedades cardiacas, circulatorias" | T1 |
| **Колумбия (подтверждение 2, госбаза)** | - | Gestor Normativo, Funcion Publica | действует | https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=37604 | "Define la obesidad y las enfermedades cronicas no transmisibles asociadas a esta como una prioridad de salud publica y adopta medidas para su control" | T1 |
| **Португалия** | похожая мера (НЕ закон) | Despacho n.º 4571/2005 (2.ª serie) - распоряжение министерства (не акт парламента); признаёт ожирение хроническим заболеванием | 02.03.2005, Diario da Republica | https://diariodarepublica.pt/dr/detalhe/despacho/4571-2005-2044965 | "A obesidade e uma doenca cronica, com genese multifactorial, que requer esforcos continuados para ser controlada" | T1 |
| **Португалия (продолжение линии)** | похожая мера | Despacho n.º 12634/2023 - интегрированная модель профилактики и лечения ожирения в SNS | 2023 | https://www.sns.gov.pt/noticias/2023/12/11/novo-modelo-para-prevencao-e-tratamento-da-obesidade-no-sns/ | "O Ministerio da Saude decidiu reforcar a resposta a obesidade, criando pela primeira vez um programa de resposta integrada a esta doenca cronica" | T1 |
| **Германия** | похожая мера (резолюция парламента, НЕ закон) | Бундестаг 02.07.2020 принял Antrag CDU/CSU и SPD (Drs. 19/20619) "Start einer Nationalen Diabetes-Strategie"; признание ожирения самостоятельным заболеванием произошло в рамках этого решения | принято 07.2020; это Antrag (постановление), а не Gesetz | https://www.bundestag.de/webarchiv/textarchiv/2020/kw27-de-diabetes-strategie-701742 | "Juli 2020, den Start einer nationalen Diabetes-Strategie begrusst, als er bei Enthaltung der Oppositionsfraktionen einen Antrag von CDU/CSU und SPD ... annahm." | T1 |
| **Германия (подтверждение характера решения)** | - | DDG | 07.2020 | https://www.ddg.info/diabetes-zeitung/ddg-06/2022/adipositas-eine-krankheit-mit-folgen | "Die Entscheidung im Juli 2020 gilt als Meilenstein: Die Anerkennung der Adipositas als eigenstandige Krankheit durch den Bundestag." | T2 |
| **Канада** | похожая мера (медассоциация + провинция, НЕ федеральный закон) | Canadian Medical Association признала ожирение хроническим заболеванием; Альберта признала в 2025 г. на уровне провинции | CMA - без даты на открытой странице; Альберта - 2025 | https://obesitycanada.ca/understanding-obesity/obesity-recognized-chronic-disease/ ; https://www.facebook.com/ObesityCanada/posts/... | "Canadian Medical Association (CMA). 'The Canadian Medical Association recognizes obesity as a chronic disease.'" / "Alberta's recognition of obesity as a chronic disease in 2025 was an important st..." | T2 / T3 |
| **США** | похожая мера (решение медассоциации, НЕ закон) | American Medical Association, 2013 | 2013 | https://www.medscape.com/viewarticle/880560 | "Obesity is currently recognized as a disease in the United States (by the American Medical Association in 2013), Canada (by the Canadian Medical ...)" | T2 |
| **Швеция** | похожая мера (министерство, НЕ закон) | Sweden, Ministry of Health - в перечне Obesity Canada | не установлен | https://obesitycanada.ca/understanding-obesity/obesity-recognized-chronic-disease/ | "Portugal, Ministry of Health. Portugal blazed a trail when it recognized ..." + "Sweden, Ministry of Health." | T2 |
| **Чили** | похожая мера (только законопроект/резолюция палаты) | Проект закона (Boletin 14725-11) объявить ожирение болезнью; Camara de Diputados приняла proyecto de resolucion | законопроект от 01.12.2021; закон НЕ принят по открытым источникам | https://www.bcn.cl/obtienearchivo?id=recursoslegales/10221.3/65175/4/14725-11_20211201.pdf ; https://www.minsal.cl/impulsan-proyecto-de-ley-que-busca-establecer-la-obesidad-como-una-enfermedad-cronica/ | "Proyecto de ley que declara de interes nacional la prevencion y control de los trastornos alimentarios, y establece la obesidad como enfermedad." | T1 |
| **Эквадор** | похожая мера (законопроект в процессе) | Проект закона о профилактике и комплексном лечении ожирения; Комиссия по здравоохранению одобрила доклад к первому чтению | на дату доступа - первое чтение, закон НЕ принят | https://www.asambleanacional.gob.ec/es/noticia/116937-comision-de-salud-aprueba-informe-para-primer-debate | "La propuesta reconoce a la obesidad como una enfermedad cronica no transmisible, sistemica, multifactorial, recurrente y progresiva, y establece ..." | T1 |
| **Румыния** | похожая мера (позиция министерства, не закон) | Ministerul Sanatatii: ожирение - хроническое заболевание | не установлена дата акта | https://www.politicidesanatate.ro/ministerul-sanatatii-obezitatea-o-boala-cronica-ce-necesita-interventii-sustinute-pe-termen-lung/ | "Obezitatea nu este doar un stil de viata sau o problema estetica, ci o boala cronica recunoscuta la nivel international" | T2 |
| **Мексика** | нет (закона о признании ожирения болезнью не найдено) | Ley General de Salud реформирована декретами по теме "sobrepeso, obesidad y trastornos de la conducta alimentaria" (DOF 22-12-2020 и др.), но объявления ожирения хроническим заболеванием в открытых фрагментах нет | реформы 2020, 2022 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LGS.pdf | "DECRETO por el que se reforman y adicionan diversas disposiciones de la Ley General de Salud, para prevenir el sobrepeso, la obesidad y los trastornos de la conducta ..." | T1 |
| **Испания** | нет | В открытых источниках - только предложения "Alianza por la Obesidad" в Конгрессе депутатов и требование национальной стратегии; закона нет | 2025 | https://diariofarma.com/2025/02/18/la-alianza-por-la-obesidad-demanda-mejorar-la-financiacion-y-acceso-a-tratamientos-innovadores | "Pacientes y expertos reclaman a la Comision de Sanidad del Congreso una Estrategia Nacional de Atencion Integral a la Obesidad." | T2 |
| **Польша** | нет | Нет закона; есть пилотная программа KOS-BAR по распоряжению министра здравоохранения | с 2021, пилот завершается 06.2026 | https://www.gov.pl/web/zdrowie/program-kompleksowej-opieki-medycznej-dla-chorych-na-otylosc-olbrzymia-leczona-chirurgicznie | "Powstaly zalozenia KOS-BAR, czyli programu kompleksowej opieki medycznej nad pacjentami chorymi na otylosc olbrzymia leczona chirurgicznie." | T1 |

### Итог по мере 2

- **Точных аналогов N = 1** (Колумбия, Ley 1355 de 2009, ст. 1 - акт Конгресса, прямо объявляющий
  ожирение хроническим заболеванием, + межсекторный орган CISAN).
  Важное расхождение источников, которое НЕ скрываем: EASO (T2) и The Conversation (T2) называют
  итальянский закон **первым в мире / первым в Европе**, но колумбийская Ley 1355/2009 (T1) содержит
  прямую формулу "Declarase. La obesidad como una enfermedad cronica de Salud Publica" за 16 лет до
  этого. Наша оценка: корректная формулировка - Италия первая **в Европе** и первая с таким объёмом
  гарантий (включение в LEA), но не первая в мире по факту законодательного признания.
- **Похожих мер M = 9**: Португалия (министерское распоряжение 2005), Германия (постановление
  Бундестага 2020), Канада (CMA + Альберта 2025), США (AMA 2013), Швеция (министерство), Чили
  (законопроект + резолюция палаты), Эквадор (законопроект в первом чтении), Румыния (позиция
  министерства), Австрия (ВОЗ-Европа фиксирует построение национальной системы лечения:
  https://www.who.int/europe/de/news/item/08-09-2022-time-to-accept-that-obesity-is-a-disease---austria-is-building-a-national-system-to-treat-it, T1).
- **Мексика, Испания, Польша - "нет"** по открытым источникам.
- **Источник подсчёта**: перечень стран-кандидатов задан заданием; проверка - по национальным
  правовым базам (alcaldiabogota.gov.co / funcionpublica.gov.co, diariodarepublica.pt, bundestag.de,
  diputados.gob.mx, bcn.cl, asambleanacional.gob.ec, gov.pl) плюс перечень организаций Obesity Canada
  и обзорные материалы EASO / The Conversation.
- **Уверенность: MEDIUM-HIGH.** HIGH по Колумбии и Португалии (открыты первичные правовые тексты),
  HIGH по Германии (открыт сайт Бундестага с номером Drs. 19/20619). MEDIUM по общей полноте:
  систематическая база "страны, где ожирение признано законом" не найдена; проверены только
  10 стран из задания + Эквадор, Швеция, Австрия, Румыния, Чили.
- **ВЕРДИКТ: АНОМАЛИЯ (N = 1 <= 5).**

### Дословный фрагмент, ограничивающий распространённость (T2)
The Conversation (https://theconversation.com/obesity-is-now-legally-recognised-as-a-chronic-disease-in-italy-a-historic-advance-for-public-health-in-europe-269305):
"To date, no other European country has enacted a national law that recognises obesity with such breadth"
и там же: "Germany's Bundestag recognised obesity as a medical and social disease in 2020, as part of its
National Diabetes Strategy."

### Непроверенное (мера 2)
- Полный текст Legge 149/2025 в Gazzetta Ufficiale - страница вернула пустой контент через Firecrawl;
  формулировка ст. 1 взята из вторичных источников (ADAPT, OMCeO Venezia). Статус: MEDIUM.
- Мексика: не исключено, что признание есть в NOM или в реформе LGS, которую фрагмент не показал.
  UNVERIFIED.
- Румыния: Legea 163/23.10.2025 (https://legislatie.just.ro/Public/DetaliiDocumentAfis/303706) - предмет
  закона в открытом фрагменте не виден, связь с ожирением НЕ подтверждена. UNVERIFIED.
- Швеция: конкретный акт министерства не открыт. UNVERIFIED.

---
