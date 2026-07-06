# Статистические аномалии массового пользователя и consumer-приложений, 2024–2026 (волна 2)

*Линза: статистические выбросы, разрывы «говорят vs делают», страны-аномалии, парадоксы платёжеспособности, расхождения оценок рынков. Метод: 14 новых поисковых запросов (WebSearch); WebFetch заблокирован egress-политикой, цифры извлечены из поисковых выдержек. Анти-дублирование с волной 1 (mass-anomalies.md, mass-user-portrait.md) проверено: AI-компаньоны/churn, винил, dumbphones, подписочная усталость, RevenueCat-бенчмарки, концентрация 94,5% выручки в топ-10% приложений — НЕ повторяются; здесь только новые сюжеты.*

## Сводка

Волна 2 показывает, что «средних цифр» о массовом пользователе фактически не существует — рынок состоит из экстремальных выбросов по трём осям. **Ось географии:** Япония с 2,2% мировой игровой аудитории даёт ~9–14% мировых трат, Индия — обратный полюс: 25,5 млрд загрузок (×2 к США) при $0,03 выручки на загрузку (~×150 меньше США). **Ось людей:** 1% игроков платит ~29% выручки мобильных игр, беднейшие домохозяйства тратят на ставки и fast-fashion большую долю дохода, чем богатые, а подростки из бедных семей сидят в экранах почти вдвое дольше богатых — цифровой разрыв перевернулся: теперь привилегия — не доступ к экрану, а свобода от него. **Ось данных:** самоотчёты систематически врут (недооценка скринтайма до 71 мин/день; 52% Gen Z «бросали соцсети» при неснижающихся 8–9 часах), а оценки одних и тех же рынков у research-фирм расходятся в 10–100 и более раз (AI-компаньоны: от $221 млн фактических трат до $36,8 млрд «рынка»). Отдельные структурные сломы: бесплатный YouTube стал ТВ-дистрибьютором №1 в США (больше Disney и Netflix), а «мёртвая» модель pay-per-episode воскресла в short drama (ReelShort: ×33 выручки за 2 года).

---

## Новые аномалии

### 1. Япония: 2,2% мировой игровой аудитории — ~9–14% мировых денег
- **Цифры:** Япония генерирует ~9,1% мировой выручки игр при ~2,2% мировой игровой аудитории; в марте 2025 при глобальных тратах App Store + Google Play $6,79 млрд Япония дала ~14,3%. ARPU в мобильных играх — до ×4 к среднемировому; Япония обходила США по выручке Google Play; ~$16 млрд IAP — №3 в мире при населении в 2,7 раза меньше США. При этом в 2025 — снижение на 7% (иена, экономика), но страна остаётся выбросом.
- **Источники:** AppSamurai, JetSynthesys, OneSky/Sensor Tower.
- **Почему не вписывается:** ни одна модель «ARPU ~ ВВП на душу» не объясняет ×4: Корея и США богаче на пользователя платят меньше. Работают культурные механики (гача, коллекционирование, IP-привязанность, iOS-доля), а не платёжеспособность.
- **Продуктовый вывод:** локализация монетизации важнее локализации языка: одна и та же механика (гача/коллекция) меняет ARPU в разы; японский плейбук (live-ops + IP + коллекционность) — самый недоиспользованный рычаг на западных рынках.

### 2. Индия: ×2 загрузок США — и $0,03 с загрузки (разрыв ×150)
- **Цифры:** Индия-2025: 25,5 млрд загрузок (США — 12,6 млрд), 1,2 трлн часов в приложениях (+9% YoY), при этом страны нет даже в топ-20 по потребительским тратам. Выручка на загрузку: ~$0,03 против $0,20+ в Юго-Восточной Азии/ЛатАм и ~$4,7 в США ($60 млрд IAP / 12,6 млрд загрузок) — разрыв на два порядка. Весь IAP Индии за 2025 — чуть более $1 млрд (прогноз $1,25 млрд на 2026).
- **Источники:** Sensor Tower via TechCrunch (21.01.2026), Business Standard, Mobile Marketing Reads.
- **Почему не вписывается:** даже с поправкой на доход разрыв аномален: ЮВА и ЛатАм с сопоставимым ВВП на душу монетизируются в 6–7 раз лучше. Время внимания — мировое, деньги — нулевые; «следующий миллиард пользователей» так и не стал следующим миллиардом долларов.
- **Продуктовый вывод:** для Индии подписка — тупик; работают реклама, микротранзакции <$1, UPI-платежи и экспорт внимания (реклама глобальных брендов на индийскую аудиторию). Глобальным платформам Индия ценна как «фабрика часов», а не чека — и это уже закладывают в юнит-экономику.

### 3. Short drama: воскрешение «мёртвой» модели pay-per-episode — ReelShort ×33 за два года
- **Цифры:** ReelShort: ~$36 млн (2023) → ~$1,2 млрд валовых потребительских трат (2025, +119% YoY); Q1 2025 — $130 млн IAP. DramaBox: $8 млн (2023) → $323 млн (2024) → сотни млн в 2025 ($120 млн только за Q1). Категория: ~$700 млн глобального IAP за Q1 2025 (≈×4 к Q1 2024); рынок 2025 вне Китая ~$3 млрд, США — ~$1,3 млрд.
- **Источники:** Sensor Tower (State of Short Drama Apps 2025), TechBuzz, Filmustage, Antom.
- **Почему не вписывается:** пользователи платят $10–30 за «сериал» мыльного качества поэпизодно (модель, которую индустрия похоронила ещё в эпоху ринтонов), при живых Netflix за $8–15/мес с голливудской библиотекой. Рост ×33 за 24 месяца — быстрее любой контентной категории в истории мобильного рынка.
- **Продуктовый вывод:** cliffhanger + микроплатёж в момент пикового желания бьёт подписку с отложенной ценностью. Продавать надо не доступ к библиотеке, а разрешение «узнать, что дальше» прямо сейчас; поэпизодная разблокировка применима далеко за пределами видео (курсы, аудио, фичи).

### 4. Киты: 1% игроков = ~29% выручки, «средний пользователь» статистически не существует
- **Цифры:** топ-1% плательщиков даёт ~29% выручки мобильных игр (в отдельных играх до 30%+), топ-5% — 50%+, топ-10% — ~48%; 60–70% игроков не платят никогда. Кит в среднем тратит ~$25/мес, в гаче — $1000+/год. (Дополняет, но не дублирует волну 1, где была концентрация по приложениям — 94,5% выручки у топ-10% приложений; здесь — концентрация по людям внутри приложения.)
- **Источники:** Game Developer (отчёты о whales), Plarium, SQ Magazine.
- **Почему не вписывается:** распределение трат — не нормальное, а степенное: медианный плательщик и средний ARPU описывают несуществующего пользователя; «средний ARPU $2» — это ноль у 95% и $200 у 1%.
- **Продуктовый вывод:** проектировать надо два продукта в одном: бесплатный социальный «стадион» для 95% (они — контент и статус для китов) и VIP-трек для 1–5%; метрики среднего (ARPU, средняя сессия) заменять перцентильными (P95/P99 spend).

### 5. Парадокс платёжеспособности №1: ставки на спорт «доят» именно бедных
- **Цифры:** NBER (w33108): средние траты ставящего домохозяйства — ~$1100/год; домохозяйства с низкими сбережениями тратят на ставки долю дохода на 32% выше, чем обеспеченные; легализация онлайн-ставок не замещает другие развлечения, а вытесняет сбережения (взносы в инвестсчета падают, кредитная задолженность и овердрафты растут — эффект сконцентрирован у финансово уязвимых). 1 из 7 ставящих влезал в долги ради ставок; 1 из 4 пропускал оплату счетов (US News 2025); 27% ставят $500+/мес.
- **Источники:** NBER Working Paper 33108, Kellogg Insight, US News 2025 Sports Betting Survey, NerdWallet 2025.
- **Почему не вписывается:** классическая модель дискреционных трат предсказывает обратное — люксовые/развлекательные расходы должны расти с доходом. Здесь доля дохода падает с ростом достатка: продукт продаёт не развлечение, а надежду на выход из бедности.
- **Продуктовый вывод:** «дофаминовые» вертикали с переменным вознаграждением имеют отрицательную эластичность по доходу — их TAM среди бедных недооценён рынком, но это же делает их первым кандидатом на регуляторный удар (лимиты, affordability checks). Строить продукт на этом паттерне = строить на регуляторном риске.

### 6. Парадокс платёжеспособности №2: Temu/Shein — беднейшие тратят на одежду ×3 долю дохода богатых
- **Цифры:** беднейшие домохозяйства США тратят на одежду более чем втрое большую долю дохода, чем богатейшие (Trade Partnership Worldwide); бедные zip-коды заметно чаще получают de minimis-посылки из Китая (NBER 2024: отмена льготы = потеря $10,9–13 млрд «совокупного благосостояния», непропорционально у бедных и меньшинств); 60% низкодоходных пользователей готовы урезать другие расходы, лишь бы не отказываться от Temu/Shein.
- **Источники:** NBER 2024, RetailWire, UCLA/Yale (февраль 2025), Fashion Dive.
- **Почему не вписывается:** e-commerce-приложение — «дискреционная» категория, но для нижнего дециля оно ведёт себя как инфраструктура (как ЖКХ): от него отказываются в последнюю очередь. Приложение с геймификацией (колёса, таймеры) стало каналом базового потребления.
- **Продуктовый вывод:** для низкодоходной аудитории выигрывает не «дёшево и стыдно», а «дёшево как игра»: геймифицированная экономия удерживает сильнее скидок. И наоборот — тарифные/регуляторные шоки бьют по этим продуктам мгновенно, т.к. вся ценность — в цене.

### 7. Скринтайм-неравенство: у бедных подростков экрана почти вдвое больше — цифровой разрыв перевернулся
- **Цифры:** подростки из семей с доходом <$35k — 9ч19м экранного времени в день, из семей $100k+ — 7ч16м (разрыв ~2 часа); tweens (8–12 лет): 7ч19м против 4ч13м — ×1,74. Каждые +$1000 дохода — минус ~1% к шансам экстремального скринтайма. Родители с доходом <$30k чаще называют контроль телефона топ-приоритетом (22% против 14% у $75k+) — и всё равно проигрывают.
- **Источники:** Common Sense Census via Statista, CDC NCHS Data Brief 513, Pew Research (2024).
- **Почему не вписывается:** 20 лет политика боролась с digital divide как с нехваткой доступа у бедных; данные показывают инверсию — избыток экрана стал маркером бедности, а офлайн-время (секции, няни, поездки) — платной привилегией.
- **Продуктовый вывод:** premium-сегмент будущего — «продукты меньшего экрана» (см. dumbphones в волне 1, но теперь с механизмом: покупатель — обеспеченный родитель). Для массовых продуктов это этический и регуляторный риск: ядро тяжёлых пользователей смещено к уязвимым группам, и телеметрия это покажет регулятору.

### 8. Самоотчёты врут на десятки процентов: до −71 мин/день против телеметрии
- **Цифры:** участники систематически недооценивали свой скринтайм на ~71 мин/день в период высокого использования (lockdown-исследование); «неосознанные» пользователи недооценивают время на ~40%, фактически используя телефон на 15% больше; студенты стабильно занижают длительность и число разблокировок, завышая при этом самооценку контроля. Направление ошибки нестабильно: часть iOS-исследований находит и переоценку — т.е. self-report не просто смещён, а неврестабилен.
- **Источники:** PMC (Discrepancies Before/During Lockdown), ScienceDirect (Smartphone Screen Time: Inaccuracy of self-reports), Frontiers in Computer Science (2026), ABCD Study via PMC.
- **Почему не вписывается:** огромная часть индустриальных «инсайтов» (опросы Deloitte, YouGov, панели «сколько часов вы...») строится на данных с ошибкой 30–70+ минут в день неизвестного знака — это больше, чем большинство измеряемых YoY-эффектов.
- **Продуктовый вывод:** любые продуктовые решения на опросных данных о времени/частоте — шум; доверять только телеметрии. В коммуникации наоборот: пользователь искренне не знает своих 5 часов — показ реальной цифры (как Screen Time) сам по себе behaviour-changing фича и источник «детокс»-спроса.

### 9. «Говорят vs делают» у Gen Z: 52% «бросали соцсети» — скринтайм не упал
- **Цифры:** 52% Gen Z пытались бросить соцсети в 2025; 68% брали «ментальные паузы»; лишь 17% никогда не пробовали себя ограничить; 41% американцев «сокращают скринтайм». Фактические замеры: у подростков в среднем 8ч45м/день, у Gen Z ~9ч/день — без устойчивого снижения; 46% признают «начал решительно — сорвался».
- **Источники:** YourTango/опрос 2025, Demandsage Screen Time Statistics 2026, AWISEE, eMarketer Gen Z Social Media 2025.
- **Почему не вписывается:** по опросам категория должна сжиматься (половина аудитории «уходит»), по телеметрии — плато на историческом максимуме. Раскаяние стало частью цикла потребления, а не его тормозом (ср. privacy paradox: 73% «стали больше беспокоиться о данных», но 56% жмут «согласен» не читая).
- **Продуктовый вывод:** «намерение уйти» — не churn-сигнал, а сегмент для продукта: спрос на ритуалы самоограничения (детокс-режимы, лимиты, grayscale) можно монетизировать внутри той же экосистемы, которая создаёт зависимость. Опросам о «намерении отказаться от X» верить нельзя без телеметрической пары.

### 10. YouTube — телеканал №1 США: бесплатный UGC обошёл Disney и Netflix на большом экране
- **Цифры:** Nielsen Media Distributor Gauge: YouTube — 13,4% всего ТВ-времени США (июль 2025), Disney — 9,4%, Netflix — ~8,3–9,0% (9,0% — рекорд платформы, декабрь 2025); отрыв в 4,0 п.п. — крупнейший с начала измерений (ноябрь 2023); 8+ месяцев подряд №1. При этом Nielsen меряет только ТВ-экран — с мобильными доля YouTube ещё выше.
- **Источники:** Nielsen (июль/декабрь 2025), Variety, Hollywood Reporter, The Desk.
- **Почему не вписывается:** контент за $0 производственных затрат платформы съедает больше времени на телевизоре, чем весь Disney (со спортом и кабелем) и чем Netflix с бюджетом $17 млрд/год на контент. «Профессиональный контент премиум-дистрибуции» перестал быть отдельной лигой — лента алгоритма победила программную сетку и на большом экране.
- **Продуктовый вывод:** экран телевизора — новый рост для «мобильных» форматов (вертикальное видео, стримы, подкасты с картинкой). Для подписочных стримингов главный конкурент — не другой стриминг, а бесплатное; ценность надо формулировать против YouTube, а не против HBO.

### 11. Рынок AI-компаньонов: оценки расходятся на 2–3 порядка ($221 млн факта vs $36,8 млрд «рынка»)
- **Цифры:** фактические измеренные потребительские траты в AI-companion-приложениях — $221 млн за всю историю к июлю 2025 (Appfigures, телеметрия сторов). Оценки research-фирм того же/смежного рынка на 2025: $2,8 млрд (DataIntelo, только AI girlfriend), $3,08 млрд (SNS Insider), $36,79 млрд (Grand View Research, «AI companion market»), у Business Research Insights стартовая точка — $501 млрд к 2026. Разброс — от ×13 до ×2200 к телеметрии.
- **Источники:** Appfigures via TechCrunch, Grand View Research, DataIntelo, Verified Market Research, Business Research Insights, Market Clarity.
- **Почему не вписывается:** это не разница методологий, а разница вселенных: в «рынок» дописывают enterprise-ботов, голосовых ассистентов, NSFW-сегмент и просто TAM-фантазии. Аналогично creator economy: размер «$180–254 млрд» при числе креаторов 50 млн (Goldman) против 120 млн (Citi) — ×2,4 по базовому физическому показателю.
- **Продуктовый вывод:** для новых категорий рыночные отчёты непригодны для решений — сверяться только с телеметрией сторов (Appfigures/Sensor Tower) и выручкой публичных компаний. Правило: если оценки фирм расходятся более чем в 3 раза — категория ещё не существует как рынок, существует как нарратив (что само по себе сигнал для фандрайзинга, но не для юнит-экономики).

### 12. AI-адаптация: 34% американцев «когда-либо пробовали ChatGPT» — при 800–900 млн WAU в мире
- **Цифры:** Pew (июнь 2025): лишь 34% взрослых США когда-либо использовали ChatGPT, 20% вообще о нём не слышали; 10% из 65+ пробовали хоть раз. Одновременно телеметрия: 800 млн weekly active users (начало 2026) → 900+ млн к февралю 2026 (×1,8 к марту 2025); до 30 лет — 76% пользуются AI, 50% — еженедельно.
- **Источники:** Pew Research (25.06.2025; 12.03.2026), Reuters/CNBC via Backlinko, Brookings, Menlo Ventures State of Consumer AI.
- **Почему не вписывается:** самый быстрорастущий продукт в истории по WAU сосуществует с большинством взрослых богатейшей страны, ни разу его не открывшим; возрастной обрыв (76% vs 10%) круче, чем был у смартфонов или соцсетей на той же стадии. Плюс расхождение survey vs telemetry: YouGov даёт 56% «использовали AI», Pew — 34% по ChatGPT: сама формулировка вопроса двигает рынок на десятки процентов.
- **Продуктовый вывод:** AI-рынок — ещё не массовый, а «глубокий»: рост идёт интенсивностью у молодого ядра, а не проникновением. Продукты «AI для тех, кто не пользуется AI» (невидимый AI внутри привычных интерфейсов) — самый большой нетронутый сегмент: 2/3 взрослых США.

---

## Сквозные выводы линзы

1. **Средние значения мертвы:** траты (киты ×100), время (бедные ×2), география (Япония/Индия ×150) распределены степенно — сегментировать по перцентилям, не по средним.
2. **Деньги ходят против дохода:** в «дофаминовых» категориях (ставки, fast-fashion-игра, микротранзакции) доля кошелька растёт по мере бедности — коммерчески мощно, регуляторно токсично.
3. **Опросы систематически недостоверны:** ошибка самоотчёта (±40–70 мин/день, 52% «бросающих» без снижения телеметрии) больше типичных годовых трендов; решения — только на телеметрии.
4. **Оценкам рынков новых категорий верить нельзя:** разброс ×13–×2200 (AI-компаньоны) и ×2,4 по числу креаторов — «рынок» на этой стадии есть нарратив.

## Источники

1. AppSamurai — Why Japan Leads in Mobile Game Monetization (2025): https://appsamurai.com/blog/why-japan-leads-in-mobile-game-monetization/
2. JetSynthesys — Why ARPU in Japan is 4x higher: https://www.jetsynthesysjp.com/post/why-arpu-in-japan-is-4x-higher-than-that-of-global-markets
3. OneSky — Japan overtakes US for Google Play revenue: https://www.onesky.ai/blog/japan-overtook-us-to-become-the-top-country-for-google-play-revenue
4. TechCrunch — India's app downloads rebounded to 25.5B in 2025: https://techcrunch.com/2026/01/21/indias-app-downloads-rebounded-to-25-5-billion-in-2025-fueled-by-ai-assistants-and-microdrama-boom/
5. Business Standard — India leads downloads, spending gap persists (Sensor Tower): https://www.business-standard.com/technology/tech-news/india-app-downloads-revenue-gap-sensor-tower-report-126042400618_1.html
6. Mobile Marketing Reads — India IAP crosses $1B: https://mobilemarketingreads.com/indias-in-app-purchase-revenue-crosses-1b-set-to-reach-1-25b-in-2026/
7. Sensor Tower — State of Short Drama Apps 2025: https://sensortower.com/blog/state-of-short-drama-apps-2025
8. Filmustage — ReelShort vs DramaBox 2026: https://filmustage.com/blog/short-drama-apps-compared-reelshort-vs-dramabox-in-2026/
9. TechBuzz — Microdrama apps hit $1.5B: https://www.techbuzz.ai/articles/microdrama-apps-hit-1-5b-as-tiktok-enters-the-game
10. Game Developer — 29% of mobile game revenue from top 1% of spenders: https://www.gamedeveloper.com/business/report-29-of-mobile-game-revenue-generated-by-top-1-of-spenders
11. SQ Magazine — In-Game Purchases Statistics 2026: https://sqmagazine.co.uk/in-game-purchases-statistics/
12. Plarium — 50 Mobile Game Monetization Statistics: https://plarium.com/en/blog/mobile-game-monetization-statistics/
13. NBER — Sports Betting's Impact on Vulnerable Households (w33108): https://www.nber.org/system/files/working_papers/w33108/w33108.pdf
14. Kellogg Insight — Online Sports Betting Is Draining Household Savings: https://insight.kellogg.northwestern.edu/article/online-sports-betting-is-draining-household-savings
15. US News — 2025 Sports Betting Survey: https://www.usnews.com/banking/articles/2025-sports-betting-and-debt-survey
16. NerdWallet — 2025 Sports Betting and Gambling Survey: https://www.nerdwallet.com/investing/studies/2025-sports-betting-and-gambling-survey
17. RetailWire — The End of De Minimis (Temu/Shein, NBER): https://retailwire.com/discussion/de-minimis-tariff-temu-shein/
18. Fashion Dive — 30% would stop buying from Shein/Temu if prices rise: https://www.fashiondive.com/news/shein-temu-customers-cut-back/745149/
19. CDC NCHS — Daily Screen Time Among Teenagers (Data Brief 513): https://www.cdc.gov/nchs/products/databriefs/db513.htm
20. Statista — Daily screen time of US teens/tweens by income: https://www.statista.com/statistics/1099629/hours-screen-time-teens-income/
21. Pew Research — How Teens and Parents Approach Screen Time: https://www.pewresearch.org/internet/2024/03/11/how-teens-and-parents-approach-screen-time/
22. PMC — Discrepancies Between Self-reported and Measured Screen Time (lockdown): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9872730/
23. ScienceDirect — Smartphone Screen Time: Inaccuracy of self-reports: https://www.sciencedirect.com/science/article/abs/pii/S0747563220303630
24. Frontiers — Beyond screen time: objective vs perceived usage in adolescents (2026): https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1773348/full
25. YourTango — Over Half of Gen Z Tried to Quit Social Media in 2025: https://www.yourtango.com/self/survey-says-over-half-gen-z-tried-quit-social-media-2025
26. Demandsage — Screen Time Statistics 2026: https://www.demandsage.com/screen-time-statistics/
27. Nielsen — YouTube leads Media Distributor Gauge (июль 2025): https://www.nielsen.com/news-center/2025/youtube-netflix-ride-the-wave-of-summer-streaming-highs-in-nielsens-media-distributor-gauge/
28. Variety — YouTube No. 1 most-watched streamer (Nielsen): https://variety.com/2025/tv/news/youtube-top-most-watched-streamer-nielsen-1236498774/
29. Hollywood Reporter — YouTube leads US TV distributors: https://www.hollywoodreporter.com/business/business-news/youtube-leads-us-tv-distributors-6-straight-months-1236353108/
30. Grand View Research — AI Companion Market ($36.79B): https://www.grandviewresearch.com/industry-analysis/ai-companion-market-report
31. DataIntelo — AI Girlfriend App Market ($2.8B): https://dataintelo.com/report/ai-girlfriend-app-market
32. Market Clarity — The AI Companion Market in 2025 (разбор разброса оценок): https://mktclarity.com/blogs/news/ai-companion-market
33. Goldman Sachs — Creator economy could approach half-a-trillion by 2027: https://www.goldmansachs.com/insights/articles/the-creator-economy-could-approach-half-a-trillion-dollars-by-2027
34. Neal Schaffer — Creator Economy Statistics 2026 (разброс $180–254 млрд): https://nealschaffer.com/creator-economy-statistics/
35. Pew Research — 34% of US adults have used ChatGPT: https://www.pewresearch.org/short-reads/2025/06/25/34-of-us-adults-have-used-chatgpt-about-double-the-share-in-2023/
36. Backlinko — ChatGPT Statistics (800–900M WAU): https://backlinko.com/chatgpt-stats
37. Brookings — How are Americans using AI: https://www.brookings.edu/articles/how-are-americans-using-ai-evidence-from-a-nationwide-survey/
38. Usercentrics — Data Privacy Statistics 2025 (privacy paradox): https://usercentrics.com/guides/data-privacy/data-privacy-statistics/
39. Enzuzo — Data Privacy Statistics: https://www.enzuzo.com/blog/data-privacy-statistics
