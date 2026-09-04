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
| **Австралия** | точный аналог | Austroads "Assessing Fitness to Drive" (AP-G56) - национальные медицинские стандарты для частных и коммерческих водителей; условная лицензия (conditional licence) при инсулине с периодическим пересмотром специалистом | действует (изд. 2022 г. по данным вторичного источника) | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/diabetes-mellitus/medical-standards-for-licensing-2 | "For commercial drivers receiving insulin treatment, at least three months of blood glucose monitoring records should be reviewed in assessing fitness to drive." | T1 |
| **Австралия (механизм условной лицензии)** | - | Austroads, гл. по условным лицензиям | действует | https://austroads.gov.au/publications/assessing-fitness-to-drive/ap-g56/cardiovascular-conditions/medical-standards-for-licensing-1 | "For a conditional licence to be issued, the health professional must provide to the driver licensing authority details of the medical criteria not met" | T1 |
| **Новая Зеландия** | точный аналог (нижняя уверенность) | NZTA: ежегодная медицинская оценка для классов 2-5 и эндорсментов P,V,I,O при диабете на инсулине | действует | https://t2dm.nzssd.org.nz/Section-100-Diabetes-and-driving | "annual assessment is required for class 2,3,4 and 5 licence applications or P,V,I or O endorsements for all people with type 2 diabetes on insulin" | T2 |
| **Япония** | похожая мера (не подтверждено детально) | Дорожный закон Японии был ужесточён для диабетиков; конструкция формы не установлена | не установлен | https://pmc.ncbi.nlm.nih.gov/articles/PMC5089940/ | "The regulations of driver's license for diabetic patients have been tightened in Japan and EU countries recently for public safety." | T2 |
| **Южная Корея** | не установлено | - | - | - | страница с национальной нормой не открыта в этой сессии | - |

### Ключ к подсчёту: ЕС как блок

Annex III п. 10.3 - это **минимальный обязательный стандарт**, который все государства-члены ЕС обязаны
транспонировать. То есть конструкция "инсулинозависимый водитель группы 2 допускается при заключении
компетентного медоргана + регулярный пересмотр с ограниченным сроком (<=3 года)" существует
не менее чем в 27 странах ЕС плюс Великобритания (сохранила норму), Ирландия (входит в 27),
Норвегия/Исландия/Лихтенштейн (EEA - **не проверено в этой сессии**), Гибралтар
(транспонировано отдельным актом: https://www.gibraltarlaws.gov.gi/legislations/traffic-third-driving-licence-directive-regulations-2012-3064/download,
фрагмент: "interval should not exceed five years. 10.2. Driving licences shall not be issued to, nor renewed for, applicants or drivers who have ...", T1).

### Итог по мере 1

- **Точных аналогов N = не менее 31**: 27 государств-членов ЕС (через обязательную Директиву 2006/126/EC
  Annex III п. 10.3), плюс Великобритания, Канада, Австралия, Новая Зеландия.
  Если считать по формальному критерию "явно открытая в этой сессии национальная страница":
  подтверждено дословно 5 юрисдикций (Великобритания, Ирландия, Канада, Австралия, Новая Зеландия)
  + текст обязывающей Директивы для остальных 26 стран ЕС.
- **Похожих мер M = 1** (Япония - тема та же, конструкция не установлена).
- **Источник подсчёта**: (1) текст Annex III Директивы 2006/126/EC (даёт перечень адресатов - все
  государства-члены ЕС); (2) национальные страницы GOV.UK, gov.bc.ca/CCMTA, Austroads, NDLS/diabetes.ie,
  NZSSD. Обзор Beshyah et al., Br J Diabetes 2017;17:3-10 ("Information on licensing was obtained from
  85 countries. No restrictions on drivers with insulin-treated diabetes existed in 59 countries (69.4%)",
  https://www.bjd-abcd.com/index.php/bjd/article/view/228, T2) подтверждает, что тема регулируется
  во множестве стран, но его разбивка по коммерческому транспорту в открытом фрагменте обрывается.
- **Уверенность: MEDIUM-HIGH.** HIGH для факта, что конструкция распространена (открыт обязывающий
  текст Директивы + 5 национальных источников, из них 4 - T1). MEDIUM для точного числа: перечень
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
