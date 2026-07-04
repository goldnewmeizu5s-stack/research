# Скрытые гемы: нестандартные travel-платформы для хардкорных путешественников

**Дата ресёрча:** 2026-07-04
**Метод:** 199 автономных research-агентов — 24 «искателя» по разным углам тревел-хаков + 5 «охотников за пробелами» + 170 адверсариальных верификаторов (по одному на платформу).
**Воронка:** найдено 187 уникальных платформ → проверено 170 → **167 подтверждены как живые и нишевые** (2 мертвы, 1 отклонена как мейнстрим, 17 не влезли в кап верификации).

Каждый верификатор независимо проверял: жив ли сайт в середине 2026, делает ли он заявленное, и не является ли он мейнстримом. Каждой платформе выставлены два скора:

- **U (необычность, 0–100)** — насколько нестандартна сама механика, «выпадает ли из логики»;
- **E (эффективность, 0–100)** — сколько реальных денег/ценности выжимает из неё частый путешественник.

Референс запроса: [besttimetobookhotels.com](https://www.besttimetobookhotels.com) — data-driven тайминг бронирования отелей. Ниже — 20 главных «читов» с такой же энергией, но с разными механиками, плюс бонусный пул и полная таблица всех 167 подтверждённых платформ.

---

## ТОП-20 «читов»

| # | Платформа | Механика одной строкой | U | E |
|---|-----------|------------------------|---|---|
| 1 | [Routing Ruler](https://www.routingruler.com) | Парсит сырые тарифные правила из GDS и находит самый длинный легальный маршрут на дешёвом тарифе | 88 | 55 |
| 2 | [Pasporta Servo](https://www.pasportaservo.org) | Выучи эсперанто — получи сеть бесплатных ночёвок в 121 стране (с 1974 года) | 85 | 38 |
| 3 | [Bahn-Vorhersage](https://bahnvorhersage.de/) | ML на 700 ГБ истории опозданий Deutsche Bahn: предсказывает, какая пересадка сорвётся | 78 | 52 |
| 4 | [RailForLess](https://railforless.us/) | Open-source сканер тарифных «вёдер» Amtrak — календарь низких цен, которого нет у самого Amtrak | 78 | 68 |
| 5 | [StatusMatcher](https://statusmatcher.com) | Краудсорсинговая база: кто кому реально сматчил элитный статус — разведка по непубличным политикам лояльности | 78 | 65 |
| 6 | [Sanctifly](https://www.sanctifly.club/) | Спортзалы/бассейны/души аэропортовых отелей без номера за ~$12/мес; задержка рейса 2ч+ автоматически начисляет бесплатный визит | 78 | 55 |
| 7 | [Fly for Points](https://search.flyforpoints.com) | Поиск авиабилетов наоборот: сортирует не по цене, а по статусным баллам на доллар | 78 | 58 |
| 8 | [The Caretaker Gazette](https://caretaker.org/) | Бумажная газета объявлений (с 1983): смотрители частных островов, ранчо и маяков — жильё бесплатно, иногда с зарплатой | 75 | 60 |
| 9 | [Grabr](https://grabr.io) | Твой пустой чемодан = доход: везёшь заказы попутно и отбиваешь ~$300 с перелёта | 75 | 55 |
| 10 | [TUG Last-Minute Rentals](https://tugbbs.com/forums/forums/last-minute-discounted-timeshare-rentals-offered.45/) | Форум, где владельцы таймшеров обязаны сливать «сгорающие» недели с потолком цены $800/неделя | 74 | 62 |
| 11 | [Imoova](https://www.imoova.com/) | Кемперы за $1/день: ты сам — логистика перегона флота, топливо часто компенсируют | 72 | 70 |
| 12 | [Welcome To My Garden](https://welcometomygarden.org) | ~8 700 частных садов Европы для бесплатной палатки — но только если ты пришёл пешком или на велосипеде | 72 | 60 |
| 13 | [Seatfrog](https://seatfrog.com/) | Живые аукционы на непроданные места 1-го класса в поездах UK — апгрейд от £5 | 70 | 72 |
| 14 | [Eurowings Blind Booking](https://www.eurowings.com/en/discover/offers/blind-booking.html) | Авиалотерея с читом: за €5 вычёркиваешь нежеланные города и «управляешь» случайностью | 70 | 58 |
| 15 | [AZair](https://www.azair.eu/) | Брутфорс-комбинатор билетов лоукостеров: маршруты, которые не продаст ни одна система | 68 | 74 |
| 16 | [AutoSlash](https://www.autoslash.com/) | Следит за ценой ТВОЕЙ брони авто и перебронирует дешевле — бронь превращается в потолок цены | 68 | 80 |
| 17 | [Pruvo](https://www.pruvo.net/) | Работает только ПОСЛЕ оплаты отеля: ловит падение цены на тот же номер и даёт перебронировать | 68 | 70 |
| 18 | [Where to Credit](https://wheretocredit.com/en) | Арбитраж начисления миль: один билет = 25% миль в одной программе или 150% в партнёрской | 68 | 70 |
| 19 | [Caravanistan Border Crossings](https://caravanistan.com/border-crossings/) | Викибаза свежих отчётов о наземных границах Шёлкового пути — данные, которых нет ни у одного государства | 68 | 70 |
| 20 | [Seats.aero](https://seats.aero) | Кэшированная база премиальных award-мест 20+ программ + календарь моментов «вброса» мест авиакомпаниями | 65 | 84 |

---

## Карточки топ-20

### 1. Routing Ruler — компилятор тарифных правил
**U 88 / E 55** · https://www.routingruler.com
Берёт на вход сырой текст routing rules из ExpertFlyer/KVS/Amadeus и генерирует все валидные маршруты тарифа с учётом стоповеров, зон IATA и Maximum Permitted Mileage, сортируя по дальности. Механизирует «тёмное искусство» FlyerTalk: на дешёвый билет ~£708 можно легально навесить ~14 400 квалификационных миль и лишние города-стоповеры вместо нонстопа в 3 500 миль.
**Подвох:** нужен доступ к ExpertFlyer/GDS для входных данных; окупается только там, где мили начисляют за дистанцию. Бесплатно до 100 маршрутов, дальше $4.99/мес.

### 2. Pasporta Servo — язык как ключ от бесплатных ночёвок
**U 85 / E 38** · https://www.pasportaservo.org
Сеть гостеприимства Всемирной эсперанто-молодёжной организации с 1974 года: ~2 400 хостов в 121 стране принимают бесплатно любого, кто говорит на эсперанто. Ворота входа — не деньги, а несколько месяцев Duolingo.
**Подвох:** пул хостов маленький и стареющий, отвечают не все. Но как механика — чистый анти-мейнстрим.

### 3. Bahn-Vorhersage — квант-аналитика для дешёвых ж/д тарифов
**U 78 / E 52** · https://bahnvorhersage.de/
Два студента обучили модель на ~700 ГБ истории задержек DB (презентовали на хакерском конгрессе 38C3). Скорит вероятность успеха каждой пересадки. Чит: дешёвые Sparpreis-билеты привязаны к конкретному поезду — выбирая статистически надёжные стыковки, безопасно берёшь самый дешёвый негибкий тариф.
**Подвох:** только Германия, интерфейс немецкий.

### 4. RailForLess — сканер тарифных вёдер Amtrak
**U 78 / E 68** · https://railforless.us/
Amtrak использует авиационные fare buckets, но показывает цену только на один день. Этот open-source инструмент (наследник культового AmSnag) рисует календарь низких цен на недели вперёд + алерты. Сдвинул выезд на два дня — заплатил вдвое меньше за спальный roomette.
**Подвох:** только США; зависит от капризов API Amtrak.

### 5. StatusMatcher — разведбаза статус-матчей
**U 78 / E 65** · https://statusmatcher.com
С 2007 года собирает полевые отчёты: какая авиакомпания/отель/прокат сматчила чей статус, на каком уровне и когда. Статус-матчи нигде не документированы — это единственный структурированный датасет «кто говорит да». Позволяет «лесенкой» превратить один дешёвый статус (например, National Emerald с кредитки) в лаунжи, апгрейды и бесплатные ночи по всей индустрии, не налетав ни мили.
**Подвох:** только разведданные, матч не гарантирован; не путать с платным брокером statusmatch.com.

### 6. Sanctifly — лаунж-хак через отельные спортзалы
**U 78 / E 55** · https://www.sanctifly.club/
За ~$11.95/мес пускает в спортзалы, бассейны и души аэропортовых отелей БЕЗ бронирования номера (160+ аэропортов). Вишенка: зарегистрируй рейс — при задержке 2ч+ автоматически падает 100 баллов (= бесплатный визит). Задержка буквально платит тебе.
**Подвох:** визиты жгут баллы сверх подписки, часть «аэропортовых» залов на самом деле в стороне.

### 7. Fly for Points — поисковик статус-ранов
**U 78 / E 58** · https://search.flyforpoints.com
Инверсия любого поиска билетов: ранжирует маршруты по элитным баллам на потраченный доллар. Автоматизирует табличную математику mileage-раннеров: находишь билет за ~$1 300, который закрывает Oneworld Emerald на год.
**Подвох:** оценки приблизительные; бесполезен для чисто revenue-based программ (США/BA).

### 8. The Caretaker Gazette — газета смотрителей с 1983 года
**U 75 / E 60** · https://caretaker.org/
Ретро-механика в чистом виде: подписная газета ($39.95/год) с объявлениями о рент-фри смотрительстве — поместья, охотничьи домики, частные острова, зимовки на рыболовных базах, часто с зарплатой сверху. Де-факто монополист жанра; такие объявления никогда не попадают на TrustedHousesitters.
**Подвох:** это работа на месяцы, а не отпуск; часть объявлений устаревшая.

### 9. Grabr — чемодан как источник дохода
**U 75 / E 55** · https://grabr.io
P2P-маркетплейс: принимаешь заказы на покупки по своему маршруту, привозишь, получаешь 15–20% награды из эскроу (~$200–300 за рейс NYC→Буэнос-Айрес на электронике). Пустое место в багаже субсидирует авиабилет.
**Подвох:** покупку авансируешь сам, выплаты могут задерживаться, таможенные риски на тебе; спрос скошен на маршруты США→Латам.

### 10. TUG Last-Minute Rentals — дистресс-рынок таймшеров
**U 74 / E 62** · https://tugbbs.com/forums/forums/last-minute-discounted-timeshare-rentals-offered.45/
Форум 1993 года, внутри которого прячется рынок «сгорающего» инвентаря: недели, начинающиеся в ближайшие 45 дней, по правилам форума нельзя выставлять дороже $800/неделя (~$115/ночь). Полноценные resort-кондо 2BR в Орландо за $114/ночь против $250+ ритейла. Торговаться не нужно — потолок вшит в правила.
**Подвох:** инвентарь тонкий («бери что есть»), оплата напрямую незнакомцу без защиты.

### 11. Imoova — кемпер за $1 в день
**U 72 / E 70** · https://www.imoova.com/
Крупнейший маркетплейс перегонов: прокатным компаниям нужно вернуть кемперы/авто между депо (AU/NZ/US/CA/EU/JP), и они отдают их за $1/день, часто с компенсацией топлива и паромов до $500. Мотохоум за $200–300/день превращается в почти бесплатный роудтрип — экономия $1 000–2 000 за поездку.
**Подвох:** жёсткие маршруты и сроки, невозвратные сборы, депозиты; разбирают в первые минуты.

### 12. Welcome To My Garden — сад вместо кемпинга
**U 72 / E 60** · https://welcometomygarden.org
~8 700 частных садов по Европе, где хозяева бесплатно разрешают поставить палатку. Фильтр входа — способ передвижения: только пешком или на велосипеде. Двухнедельный велотур по Бельгии-Франции = €250–400 экономии на кемпингах.
**Подвох:** членство €36/год обязательно для связи с хостами; покрытие скошено в Бенилюкс/Францию.

### 13. Seatfrog — eBay для пустых мест первого класса
**U 70 / E 72** · https://seatfrog.com/
Живые аукционы на непроданные места 1-го класса поездов UK в последние часы перед отправлением: ставки от ~£5. Комбо-чит: дешёвый advance-билет London–Edinburgh за £40 + снайп апгрейда за £15–25 = первый класс с едой дешевле обычного гибкого стандарта (walk-up first — £135+).
**Подвох:** только UK, +£3 комиссия, на загруженных маршрутах ставки разгоняют.

### 14. Eurowings Blind Booking — управляемая лотерея
**U 70 / E 58** · https://www.eurowings.com/en/discover/offers/blind-booking.html
Авиакомпания продаёт distressed-инвентарь как лотерею направлений: платишь ~€89 за возвратный билет «куда-то» по теме (пляж/город/пати). Чит внутри чита: за €5 вычёркиваешь каждое нежеланное направление и фактически рулишь «случайным» розыгрышем в сторону Мальорки.
**Подвох:** невозвратно, вылеты в основном из DACH-хабов.

### 15. AZair — брутфорс лоукостеров
**U 68 / E 74** · https://www.azair.eu/
Чешский движок комбинирует раздельные билеты Ryanair+Wizz+Pegasus в self-transfer маршруты, которые не продаёт ни один GDS, и понимает запросы типа «из Праги/Вены куда угодно на Средиземноморье, 7–10 дней, когда-нибудь в июле» → €40–80 за всё. Интерфейс из 1998-го отпугивает туристов — и это фича.
**Подвох:** риск стыковок целиком на тебе; Европа/Средиземноморье.

### 16. AutoSlash — бронь авто как потолок цены
**U 68 / E 80** · https://www.autoslash.com/
В США прокат авто по умолчанию с бесплатной отменой — значит, бронь это просто максимум, который ты заплатишь. AutoSlash бесплатно перепроверяет твою бронь до самого пикапа, стакает купоны (Costco/AAA) и шлёт алерт, когда можно перебронировать то же авто дешевле. Типично −20–30% ($120–200 с недельной аренды) без единого действия.
**Подвох:** фокус США/Канада, котировки по email, роутинг через Priceline.

### 17. Pruvo — воронка наоборот
**U 68 / E 70** · https://www.pruvo.net/
Начинает работать после того, как ты заплатил: форвардишь подтверждение отеля на save@pruvo.net, он 24/7 следит за тем же номером и алертит при падении цены — перебронируешь и отменяешь старую. ~40% возвратных броней дешевеют до заезда, в среднем −17%. Ближайший родственник besttimetobookhotels по духу.
**Подвох:** только free-cancellation брони; предложения перебронирования часто через партнёрские тарифы Pruvo с другими условиями отмены.

### 18. Where to Credit — арбитраж начисления миль
**U 68 / E 70** · https://wheretocredit.com/en
Забытая половина majles-хакинга: один и тот же платный билет может дать 25% миль в «родной» программе и 100–150% + статусные мили в партнёрской. Вводишь перевозчика и букинг-класс — получаешь, куда кредитовать. Дешёвая экономика Lufthansa класса K → Aegean вместо Miles & More = Star Alliance Gold на годы быстрее бесплатно. Инструмент умер, был спасён Travel-Dealz в конце 2025 — почти никто не знает, что он снова жив.
**Подвох:** не считает revenue-based начисления.

### 19. Caravanistan Border Crossings — база знаний о границах
**U 68 / E 70** · https://caravanistan.com/border-crossings/
Краудсорсинговая вики+форум свежих отчётов о каждом наземном переходе Центральной Азии, Кавказа, Ирана, Китая, Монголии. Ни одно государство не скажет, пускает ли перевал Кульма туристов в этом месяце — здесь это узнают раньше путеводителей. Экономит сотни долларов на несорвавшихся объездах и пропусках.
**Подвох:** только регион Шёлкового пути.

### 20. Seats.aero — база award-инвентаря всего мира
**U 65 / E 84** · https://seats.aero
Инвертирует поиск наградных мест: вместо живых запросов к сайтам авиакомпаний держит постоянно обновляемую базу award-инвентаря 20+ программ — скан года по всем программам за секунды + календарь Award Release Dates (точный момент, когда авиакомпания вбрасывает места). Бизнес США→Токио за ~75k баллов вместо $5–6k кэшем.
**Подвох:** полный горизонт 360 дней — в Pro ($99.99/год); кэш бывает фантомным; идёт суд с Air Canada за скрейпинг.

---

## Бонусный пул: ещё 30 подтверждённых читов

**Ты — логистическое решение**
- [Movacar](https://www.movacar.com/) (U65/E62) — европейские перегоны авто/кемперов за €1 с топливом; про-ход: алерт на свой маршрут.
- [Transfercar](https://www.transfercar.co.nz/) (U68/E70) — то же для NZ/AU, пионер жанра.
- [Vogavecmoi](https://www.vogavecmoi.com/en/) (U64/E68) — французский клуб «bateau-stop»: через Атлантику как экипаж за долю в еде; англофоны о нём не знают — конкуренция за койки ниже.
- [Latitude 38 Crew List](https://www.latitude38.com/crew-list-home/) (U72/E62) — бумажный журнал яхтсменов SF: подписался в лист, пришёл на вечеринку за $10 — уплыл в Мексику бесплатно.
- [Crewbay](https://www.crewbay.com/) (U70/E55), [OceanCrewLink](https://oceancrewlink.com/) (U68/E55), [HandGegenKoje](https://www.handgegenkoje.de) (U68/E60) — биржи яхтенных экипажей.

**Перебронирование и refare после покупки**
- [HotelSlash](https://www.hotelslash.com/) (U65/E68) — как Pruvo, от создателей AutoSlash.
- [Autopilot](https://www.withautopilot.com/) (U65/E62), [JetBack](https://getjetback.com/) (U58/E65) — автоматический refare авиабилетов после падения цены.

**Данные как чит (дух besttimetobookhotels)**
- [Thrill Data](https://www.thrill-data.com/) (U55/E62) — квант-терминал тем-парков: предиктивные crowd-календари + история цен Lightning Lane.
- [Avoid Crowds](https://avoid-crowds.com/) (U68/E42) — календари толп по городам Европы с учётом школьных каникул и круизных заходов.
- [BestTime.app](https://besttime.app/) (U65/E32) — прогноз пешего трафика любого заведения мира.
- [AirHint](https://www.airhint.com/) (U62/E50) — предсказатель «брать сейчас или ждать» по конкретному рейсу.
- [KnowDelay](https://knowdelay.com/) (U62/E42) — прогноз задержек рейсов по погоде на 3 дня вперёд.

**Статусные игры и мили**
- [StatusMatch.com](https://statusmatch.com) (U68/E65) — официальный брокер статус-матчей: $199 → SkyTeam Elite Plus на год.
- [SkyStatus](https://skystatus.pro) (U70/E55) — симулятор XP-ранов Flying Blue.
- [Roame](https://roame.travel) (U62/E75) — «Skiplagged для баллов» + трекер трансфер-бонусов.
- [rooms.aero](https://rooms.aero) (U58/E74) — сканер отельных award-ночей: находит даты, где Hyatt-баллы дают 3–5¢ ценности.
- [Cashback Monitor](https://www.cashbackmonitor.com) (U65/E68) — арбитраж шопинг-порталов в реальном времени.

**Нестандартное жильё**
- [Ospitalità Religiosa](https://ospitalitareligiosa.it/en/) (U62/E75) — 1 600+ монастырей и конвентов Италии от €25.
- [Mennonite Your Way](https://mennoniteyourway.com) (U75/E55) — каталог меннонитского гостеприимства, живёт с 1976.
- [Educators Travel](https://educatorstravel.com) (U70/E55) — сеть ночёвок «учитель у учителя» за ~$50.
- [Evergreen Club](https://www.evergreenclub.com) (U62/E58) — B&B в домах людей 50+ за символическую благодарность ~$30.
- [UniversityRooms](https://www.universityrooms.com/) (U60/E65) — студенческие общаги (включая колледжи Оксфорда/Кембриджа) как отели на каникулах.
- [Warmshowers](https://www.warmshowers.org) (U65/E78) — 185 000 хостов для велотуристов: 3-месячный тур = $2 000–4 000 экономии.
- [Kindred](https://livekindred.com) (U55/E72) — home-swap за кредиты: уехал из своей квартиры — заработал ночи в чужих.

**Тарифные эксплойты**
- [TrainSplit](https://trainsplit.com/) (U60/E75) — автоматический split-ticketing UK: те же места, −20–40%, легально по Condition 19.
- [BRFares](https://www.brfares.com/) (U70/E72) — сырая тарифная база UK rail для ручного поиска аномалий.
- [ExpertFlyer](https://www.expertflyer.com/) (U68/E72) — доступ к «пилотским» данным: fare buckets, наличие мест, алерты.
- [ITA Matrix](https://matrix.itasoftware.com/) (U62/E68) + [BookWithMatrix](https://bookwithmatrix.com/) (U68/E55) — конструктор тарифов с языком routing codes.
- [EUflight](https://euflight.de/) (U62/E60) — не взыскивает компенсацию EU261, а ПОКУПАЕТ твоё требование: €400 на счету через 24–72 часа после задержки.

**Связь и деньги в дороге**
- [Firsty](https://www.firsty.app) (U72/E58) — бесплатный роуминг за просмотр рекламы: реклама = 30–60 мин интернета, навсегда.
- [RatePunk](https://www.ratepunk.com) (U65/E55) — расширение, которое называет страну, из-под VPN которой этот отель дешевле всего.
- [ATM Fee Saver](https://atmfeesaver.com) (U65/E58) — краудсорсинговая база комиссий и лимитов банкоматов по странам.

---

## Отсеяно верификаторами

- **Мертво/зомби:** ShipHitching (Facebook-группа мертва), CabinCrew.Cruises (домен брошен).
- **Мейнстрим:** WiFi Map (170M юзеров — уже не «гем»).
- Также в полном списке ниже есть платформы с U<50 — живые и полезные, но по механике ближе к обычным сравнивалкам; они не проходят порог «необычности» этого ресёрча.

---

## Приложение: все 167 подтверждённых платформ

Отсортировано по совокупному скору (0.6×U + 0.4×E). Полные данные верификации — в `data/verified-platforms.json`.

| Платформа | Категория | U | E | Что делает |
|---|---|---|---|---|
| [Routing Ruler](https://www.routingruler.com) | routing-rules | 88 | 55 | A routing-rules calculator and mileage-run planner: it parses raw fare routing rules (from ExpertFlyer, KVS Tool, or Amadeus GDS output) … |
| [RailForLess](https://railforless.us/) | fare-calendar | 78 | 68 | An open-source Amtrak fare-bucket scanner: scrapes Amtrak's booking system and renders a Google-Flights-style low-fare calendar across we… |
| [AutoSlash](https://www.autoslash.com/) | car-rental-rebooking | 68 | 80 | Free service that tracks the price of a rental car reservation you already hold (from any company) and emails you when the rate drops so … |
| [StatusMatcher](https://statusmatcher.com) | status-match | 78 | 65 | A crowdsourced database (running since 2007) of real status-match and status-challenge outcomes across airlines, hotels, and car rental p… |
| [Seats.aero](https://seats.aero) | award-scanner | 65 | 84 | A cached award-availability scanner that continuously crawls award seat inventory from ~20 airline loyalty programs and lets you scan up … |
| [Imoova](https://www.imoova.com/) | campervan-relocation | 72 | 70 | The largest marketplace for $1/day vehicle relocations: rental companies post cars, campervans, RVs and motorhomes that need to be driven… |
| [BRFares](https://www.brfares.com/) | fare-database | 70 | 72 | A raw, enthusiast-built front-end to the entire British rail fares database: type any two stations and see every fare that exists — inclu… |
| [Seatfrog](https://seatfrog.com/) | upgrade-auction | 70 | 72 | An app that runs eBay-style live auctions for unsold first-class seats on UK trains: bid from about 5 pounds in the final hours before de… |
| [AZair](https://www.azair.eu/) | virtual-interlining | 68 | 74 | A Czech-built search engine that brute-force combines separate low-cost-carrier tickets (Ryanair + Wizz + Pegasus, etc.) into self-transf… |
| [Warmshowers](https://www.warmshowers.org) | cyclist-hospitality | 65 | 78 | A nonprofit reciprocal-hospitality community of 185,000+ touring cyclists and hosts worldwide: free beds, showers, and often dinner and b… |
| [Fly for Points](https://search.flyforpoints.com) | status-run | 78 | 58 | A flight search engine that ranks itineraries not by price but by elite-qualifying earnings: it computes tier points / status credits / q… |
| [ExpertFlyer](https://www.expertflyer.com/) | fare-intelligence | 68 | 72 | A subscription tool exposing raw airline inventory: per-flight fare-bucket availability (e.g. '7J'), full fare rules, upgrade and award s… |
| [TUG Last-Minute Rentals (Timeshare Users Group)](https://tugbbs.com/forums/forums/last-minute-discounted-timeshare-rentals-offered.45/) | forum-distressed-inventory | 74 | 62 | A forum-based marketplace where timeshare owners must offload weeks starting within 45 days, with a hard price cap enforced by forum rule… |
| [The Caretaker Gazette](https://caretaker.org/) | caretaking-classifieds | 75 | 60 | A subscription classifieds publication (bimonthly issues plus several-times-weekly email blasts, $39.95/yr) running since 1983 that lists… |
| [Pruvo](https://www.pruvo.net/) | hotel-rebooking | 68 | 70 | Free hotel post-booking monitor: forward your confirmation email and Pruvo watches the exact same room 24/7, alerting you when the price … |
| [Transfercar](https://www.transfercar.co.nz/) | car-relocation | 68 | 70 | The original free relocation-car platform (Auckland, since 2008): rental companies in NZ and Australia list cars and campers that must mo… |
| [Sanctifly](https://www.sanctifly.club/) | airport-wellness-access | 78 | 55 | A ~$11.95/month travel-wellness membership that gets you into airport hotel gyms, pools, spas, and showers WITHOUT booking a room, plus 1… |
| [Caravanistan Border Crossings](https://caravanistan.com/border-crossings/) | border-crossing-intel | 68 | 70 | A crowdsourced database and forum of first-hand land-border crossing reports across the Silk Road region (Central Asia, Caucasus, China, … |
| [Where to Credit](https://wheretocredit.com/en) | miles-crediting | 68 | 70 | Enter your marketing/operating carrier and booking class, and it tells you which of 50+ frequent flyer programs would earn you the most r… |
| [Latitude 38 Crew List](https://www.latitude38.com/crew-list-home/) | crew-list | 72 | 62 | A free online crew list run by San Francisco's Latitude 38 sailing magazine, pairing skippers and would-be crew for Bay daysails, coastal… |
| [Pueblo Inglés (by Diverbo)](https://www.volunteerspuebloingles.com) | language-barter | 72 | 62 | Volunteer as a native/fluent English speaker at 6–8 day immersion retreats in Spain and Germany: you get a free all-inclusive resort stay… |
| [Bahn-Vorhersage](https://bahnvorhersage.de/) | delay-prediction | 78 | 52 | A machine-learning train-delay and connection-reliability predictor for Germany, trained on ~700 GB of historical Deutsche Bahn delay dat… |
| [foodsharing.de (Fairteiler map)](https://foodsharing.de) | food-sharing | 80 | 48 | Germany/Austria/Switzerland grassroots network (200,000+ users, 4,500+ partner businesses) whose public map shows 'Fairteiler' — shelves … |
| [Roame](https://roame.travel) | transfer-bonus-tracker | 62 | 75 | Free award flight search engine ('Google Flights for points') covering availability on nearly 200 airlines with alerts, plus a maintained… |
| [Welcome To My Garden](https://welcometomygarden.org) | garden-camping | 72 | 60 | A citizen-run network of ~8,500 private gardens across Europe where hosts let slow travelers pitch a tent for free. Strictly limited to n… |
| [Ospitalità Religiosa Italiana](https://ospitalitareligiosa.it/en/) | religious-hospitality-directory | 62 | 75 | Non-profit portal run by the Italian Religious Hospitality Association listing thousands of convents, monasteries, hermitages, sanctuarie… |
| [Points Path](https://pointspath.com) | points-cash-arbitrage | 65 | 70 | A browser extension that injects live award-points prices from airline programs (United, AA, Delta, JetBlue, Flying Blue, Aeroplan, Alask… |
| [Mennonite Your Way](https://mennoniteyourway.com) | faith-based-hospitality | 75 | 55 | A faith-based hospitality directory running since 1976: ~900 host households (Mennonite, Brethren, and 'like-spirited' Christians) worldw… |
| [Grabr](https://grabr.io) | crowdshipping | 75 | 55 | A peer-to-peer marketplace connecting travelers with shoppers abroad: travelers accept shopping orders along their route, buy the item, h… |
| [StatusMatch.com](https://statusmatch.com) | status-match | 68 | 65 | The official broker that many airlines now outsource elite status matching to. You upload proof of your existing elite status with a comp… |
| [Firsty](https://www.firsty.app) | free-roaming-data | 72 | 58 | A global eSIM app (160 countries) whose 'Firsty Free' tier gives genuinely free mobile data abroad: watch a short ad to unlock 30–60 minu… |
| [HotelSlash](https://www.hotelslash.com/) | hotel-rebooking | 65 | 68 | From the AutoSlash team: a membership site ($49.95/yr, free trial) that books hotels at negotiated member rates and then keeps monitoring… |
| [Pasporta Servo](https://www.pasportaservo.org) | language-based-hospitality | 85 | 38 | A hospitality directory run by the World Esperanto Youth Organization (TEJO) since 1974: ~2,400 hosts in 121 countries offer completely f… |
| [Cashback Monitor](https://www.cashbackmonitor.com) | portal-arbitrage | 65 | 68 | A meta-comparison engine that tracks, in near real time, the payout rates of dozens of cashback and airline/hotel-mile shopping portals (… |
| [TrainSplit](https://trainsplit.com/) | split-ticketing | 60 | 75 | A UK rail booking engine that automatically splits one journey into multiple tickets at intermediate stations on the same train (e.g. Lon… |
| [Landvergnügen](https://landvergnuegen.com) | farm-stay-network | 62 | 72 | Germany's 'other pitch guide': 2,100+ rural hosts — breweries, apiaries, cheese dairies, wineries — across Germany and Austria let member… |
| [Vogavecmoi](https://www.vogavecmoi.com/en/) | boat-hitchhiking | 64 | 68 | French 'bourse aux équipiers' (crew exchange) and co-navigation club running since 2010, with 109,000+ members matching boat owners with … |
| [Stille Finden](https://stillefinden.org/) | monastery-retreats-germany | 70 | 58 | German directory-with-configurator covering ~250 monasteries in Germany and Austria that take individual overnight guests — filterable by… |
| [Eurowings Blind Booking](https://www.eurowings.com/en/discover/offers/blind-booking.html) | airline-blind-fare | 70 | 58 | The original airline blind fare: pick your departure airport, dates, and a theme box (Sun & Beach, City Trip, Party...), pay a flat disco… |
| [ITA Matrix PowerTools](https://chromewebstore.google.com/detail/ita-matrix-powertools/menecfddnlmanmpadcalononkolnplpp) | pos-booking-companion | 72 | 55 | FlyerTalk-community-built browser extension that injects extra tooling directly into ITA Matrix results: one-click booking links to dozen… |
| [France Passion](https://www.france-passion.com/en/) | farm-stay-network | 62 | 70 | The original 'invitation' scheme: ~2,000 French winegrowers, farmers, beekeepers and brewers let self-contained motorhomes/vans park over… |
| [Hitchmap](https://hitchmap.com) | hitchhiking-map | 72 | 55 | A crowdsourced world map of hitchhiking spots where every pin carries real ride data: measured wait times, spot ratings, and written revi… |
| [HandGegenKoje.de](https://www.handgegenkoje.de) | boat-hitching | 68 | 60 | A German classifieds board for 'hand gegen Koje' (work in exchange for a bunk) sailing: skippers post berths on yachts — including transa… |
| [ITA Matrix (by Google)](https://matrix.itasoftware.com/) | fare-construction | 62 | 68 | The raw airfare-construction engine that powers Google Flights, exposed with power-user controls: routing codes to force connections thro… |
| [rooms.aero](https://rooms.aero) | hotel-award-scanner | 58 | 74 | Free hotel-award scanner from the seats.aero team: instant award-night searches across Marriott, Hyatt, Hilton, IHG and Choice for entire… |
| [KOALA](https://www.go-koala.com) | timeshare-rental-marketplace | 62 | 68 | A verified marketplace for renting other people's unused timeshare weeks at Wyndham, Hilton, Marriott, Westin and similar resorts, up to … |
| [LeBonTrain](https://www.lebontrain.co) | resale-meta-search | 70 | 55 | A meta-search engine that aggregates 2,000+ secondhand train tickets listed by individuals across the whole French resale ecosystem — Tro… |
| [Crewbay](https://www.crewbay.com/) | yacht-delivery-crew | 70 | 55 | A free crew-matching network (since 2004) where yacht owners and delivery skippers post ocean passages that need extra hands — travelers … |
| [Educators Travel Network](https://educatorstravel.com) | niche-community-educators | 70 | 55 | A decades-old hospitality network for anyone working in (or retired from) education: members host fellow educators in a spare room at a f… |
| [SkyStatus](https://skystatus.pro) | status-run | 70 | 55 | A free Flying Blue (Air France/KLM) analytics platform with an XP calculator, XP-run simulator and run optimizer: enter routes and cabins… |
| [Autopilot](https://www.withautopilot.com/) | flight-refare | 65 | 62 | Links to your inbox, imports flights you've already ticketed on Alaska/American/Delta/JetBlue/United, and when the same itinerary and far… |
| [Movacar](https://www.movacar.com/) | car-relocation | 65 | 62 | European one-way rental relocations for €1: book a transfer drive (car or campervan) between rental stations across Germany and Europe — … |
| [Frachtschiffreisen Pfeiffer](https://frachtschiffreisen-pfeiffer.de/en/) | freighter-travel | 85 | 32 | Family-run German agency selling passenger berths on ocean container ships and — unusually — on working river cargo barges ('inland voyag… |
| [DayBreakHotels](https://www.daybreakhotels.com/US/en-US) | day-use-hotels | 65 | 62 | European-born day-use platform (3,500+ hotels, 15 countries incl. US) selling daytime hotel rooms in 3-8 hour slots at up to 75% off, and… |
| [David's Vacation Club Rentals](https://dvcrequest.com) | points-rental-brokerage | 58 | 72 | A brokerage that matches you with Disney Vacation Club owners to rent their points, letting you book Disney's Deluxe resorts (Grand Flori… |
| [Brit Stops](https://www.britstops.com) | pub-stopover-network | 60 | 68 | The UK/Ireland version of the scheme: 1,200+ hosts — pubs, farm shops, breweries, vineyards — offer motorhomers a free overnight stop, wi… |
| [BookWithMatrix](https://bookwithmatrix.com/) | fare-construction | 68 | 55 | A companion tool (built by the Wanderlog team) where you paste the final itinerary page from ITA Matrix and it reconstructs that exact en… |
| [OceanCrewLink](https://oceancrewlink.com/) | sail-crewing | 68 | 55 | The World Cruising Club's crew-matching database dedicated purely to ocean crossings: roughly 150 new opportunities a month for amateur c… |
| [Servas International](https://servas.org) | vetted-peace-network | 68 | 55 | The original peace-movement hospitality network, founded 1949: vetted members stay free with hosts in 100+ countries for two-night visits… |
| [SkyAuction](https://www.skyauction.com) | resort-week-auction | 68 | 55 | An auction site (running since 1999) where surplus resort and timeshare weeks — much of it unclaimed RCI exchange inventory — are auction… |
| [ATM Fee Saver](https://atmfeesaver.com) | fx-cash | 65 | 58 | A crowdsourced database and app of foreign-card ATM fees and per-withdrawal limits for individual banks and machines in 160+ countries, w… |
| [UniversityRooms](https://www.universityrooms.com/en-GB/) | university-dorms | 60 | 65 | Booking engine for empty student dorms and college guest rooms at 400+ universities in 100+ cities worldwide (Oxford and Cambridge colleg… |
| [PointsYeah](https://www.pointsyeah.com) | award-scanner | 55 | 72 | Free award flight and hotel search engine covering 20+ airline programs and major bank/hotel currencies, with unlimited live searches and… |
| [Kindred](https://livekindred.com) | credit-based-home-swap | 55 | 72 | Members-only home-swapping network built on a strict credit economy: hosting your home for one night earns 1 credit, staying anywhere cos… |
| [Trading Places International — Hot Deals Weekly Rentals](https://www.tradingplaces.com/rentals/) | exchange-overflow-rentals | 68 | 52 | The rentals arm of the #3 independent timeshare exchange company: full 7-night resort condo stays at 75+ resorts (US, Hawaii, Mexico, Dom… |
| [Movacamper](https://www.movacamper.com/) | relocation-metasearch | 70 | 48 | A meta-search engine solely for campervan relocation deals in Europe: it queries Imoova, Roadsurfer, Indie Campers, Bunk Campers and Mova… |
| [Bonvoyou](https://bonvoyou.de) | package-holiday-resale | 72 | 45 | German-language (DACH) marketplace for selling booked trips instead of cancelling: flights, hotels and especially package holidays are tr… |
| [EUflight](https://euflight.de/) | claim-factoring | 62 | 60 | German lawyer-run 'Sofortentschädigung' (instant compensation) service: it buys your EU261 delay/cancellation claim outright and wires th… |
| [Nomador](https://www.nomador.com/) | house-sitting | 55 | 70 | A France-born house/pet-sitting community strongest in Europe (sit an apartment in Paris or a farmhouse in Provence), with sitter-side su… |
| [House Sitters America (and its country-network siblings)](https://www.housesittersamerica.com/) | regional-house-sitting | 55 | 70 | A US-only house/pet-sitting network ($49/yr for sitters, free for homeowners, free to browse all ads without registering) that is part of… |
| [People Like Us](https://peoplelikeus.world) | points-based-home-exchange | 55 | 70 | Community-run home exchange network (~120 countries) whose 'Globes' token system enables non-simultaneous, chain-based swaps: one Globe =… |
| [Back-on-Track Night Train Map & Database](https://back-on-track.eu/night-train-map/) | night-train-map | 65 | 55 | Interactive map and open database of all ~205 regular sleeper-train lines running in Europe in 2026, maintained annually by the Back-on-T… |
| [The Guide to Sleeping in Airports](https://www.sleepinginairports.net/) | airport-sleeping-guide | 65 | 55 | Crowdsourced database of 1200+ airports with traveler-written reviews and 800+ guides on sleeping in terminals overnight: which airports … |
| [Wingly](https://www.wingly.io/en) | flight-sharing | 75 | 40 | Europe's flight-sharing marketplace: private pilots list seats on their small-plane trips and passengers pay only a legal cost-share (fue… |
| [RatePunk (Location Change Suggestion)](https://www.ratepunk.com) | vpn-hotel-geo-pricing | 65 | 55 | Free browser extension/app from a Lithuanian team that overlays hotel booking sites and compares the same room across OTAs. Its 'location… |
| [Falling Fruit](https://fallingfruit.org) | free-food-foraging | 85 | 25 | Open-source collaborative world map of 1.5M+ urban foraging spots — fruit trees, edible plants, herbs, even free-food dumpsters — across … |
| [JetBack](https://getjetback.com/) | flight-refare | 58 | 65 | Forward your flight confirmation once; JetBack monitors the fare and automatically files credit/refund claims with the airline every time… |
| [Volunteer.gov (federal caretaker/host/lighthouse-keeper portal)](https://www.volunteer.gov/s/) | public-lands-caretaking | 62 | 58 | The US government's interagency volunteer portal (NPS, USFS, BLM, FWS) with searchable live-in gigs: campground host, remote campground c… |
| [Behomm](https://www.behomm.com) | niche-community-designers | 62 | 58 | Invitation-only home exchange community exclusively for designers, architects, photographers, art directors and other visual creatives — … |
| [Evergreen Club](https://www.evergreenclub.com) | seniors-gratuity-homestay | 62 | 58 | A North American B&B-style homestay club for travelers over 50, running since 1982: ~thousands of member homes where a night including br… |
| [Sailsquare](https://www.sailsquare.com/) | cabin-charter | 62 | 58 | Europe's largest 'social sailing' marketplace: vetted skippers and boat owners list their holiday itineraries and travelers book one spot… |
| [WirkaufendeinenFlug.de](https://www.wirkaufendeinenflug.de/de/) | claim-factoring | 62 | 58 | Literally 'We buy your flight': a German factoring service that checks your disrupted-flight claim online in ~2 minutes, purchases it, an… |
| [Junova](https://www.junova.ai/) | flight-refare | 58 | 62 | Email-forwarding flight monitor for American, Alaska, Delta, United and Southwest cash tickets: if your exact flight's fare drops, Junova… |
| [Plot](https://www.plot.travel/) | multi-vertical-rebooking | 62 | 55 | Forward any flight or hotel confirmation to plans@plot.travel; it builds your itinerary and watches the price until departure/check-in. O… |
| [Trustroots](https://www.trustroots.org) | hitchhiker-hospitality | 62 | 55 | A volunteer-run, nonprofit hospitality network born from the hitchhiking community (founded 2014 by Hitchwiki people), where hosts and gu… |
| [SkyAccess](https://skyaccess.com/) | empty-leg-jets | 62 | 55 | A metasearch/booking engine purely for private-jet empty legs: searchable live inventory of 150,000+ repositioning flights from ~1,500 ce… |
| [Sailwiz](https://www.sailwiz.com/en) | shared-sailing | 62 | 55 | A Spanish shared-sailing marketplace where you book a single spot on a skippered yacht and split costs with strangers — including a dedic… |
| [HotelsByDay](https://www.hotelsbyday.com/en) | day-use-hotels | 55 | 65 | US-centric day-use hotel marketplace selling rooms in fixed daytime 'time bands' of 3-11 hours (e.g. 10am-6pm) at 50-75% below the overni… |
| [Armed Forces Vacation Club (R&R Weeks)](https://www.afvclub.com) | military-space-a-weeks | 55 | 65 | A free club for active-duty, retired and veteran US military that sells 7-night stays in RCI's excess timeshare inventory ('R&R' / former… |
| [AwardFares](https://awardfares.com) | award-alerts | 48 | 74 | Real-time award seat search and 24/7 monitoring across 19+ loyalty programs and 150+ airlines, with a Timeline View for scanning many dat… |
| [Plans Change](https://www.planschange.com) | hotel-resale | 72 | 38 | UK-based marketplace dedicated to reselling non-refundable hotel rooms: sellers upload proof of booking and must price at least 25% below… |
| [AirWander](https://airwander.com/) | self-transfer | 70 | 40 | A flight search that deliberately splits your A-to-B trip into separate tickets with a multi-day stopover city inserted in the middle, sh… |
| [Roomer](https://www.roomertravel.com) | hotel-resale | 70 | 40 | The original distressed hotel-room marketplace (since 2011): people stuck with non-refundable hotel reservations list them at a discount,… |
| [SabbaticalHomes](https://www.sabbaticalhomes.com) | niche-community-academics | 60 | 55 | Since 2000, the housing marketplace of academia: professors and researchers on sabbatical list their homes for exchange, house-sitting, s… |
| [Home Exchange 50plus](https://homeexchange50plus.com) | niche-community-seniors | 60 | 55 | A small (~1,000-member) home-swap network exclusively for travellers over 50 (plus Rotarians), run by a retired couple since 2009. Suppor… |
| [RepositioningCruise.com](https://www.repositioningcruise.com/) | repositioning-cruises | 55 | 62 | A single-purpose cruise agency that sells nothing but repositioning sailings — one-way relocations like Alaska-to-Hawaii and Mediterranea… |
| [Workamper News](https://workamper.com/) | work-camping | 55 | 62 | The original RV work-camping job service, publishing since 1987. Members get the weekday-updated 'Hotline' of live-in jobs across the US … |
| [Swaphouse](https://swaphouse.io) | niche-community-remote-workers | 55 | 62 | Completely free home-swapping platform built for remote workers: ~3,600 homes in 93 countries, every listing must show a dedicated worksp… |
| [FlightConnections](https://www.flightconnections.com) | route-network | 55 | 62 | An interactive map of every scheduled direct flight worldwide (900+ airlines): click any airport and see its entire nonstop network, filt… |
| [Thrill Data](https://www.thrill-data.com/) | theme-park-crowd-prediction | 55 | 62 | Statistical crowd calendars and wait-time analytics for theme parks worldwide (Disney, Universal, Six Flags, Cedar Fair and more), with b… |
| [Avoid Crowds](https://avoid-crowds.com/) | destination-crowd-calendar | 68 | 42 | Daily crowd forecasts for Europe's busiest tourist cities (Venice, Amsterdam, Barcelona, Rome and ~30+ more), condensed into a 1-100 crow… |
| [AirHint](https://www.airhint.com/) | flight-price-prediction | 62 | 50 | A buy-now-or-wait flight price predictor built specifically around individual airlines' pricing algorithms (Ryanair, Vueling, jetBlue and… |
| [CoolWorks — Jobs with Housing](https://www.coolworks.com/jobs-with-housing) | seasonal-work-housing | 55 | 60 | Seasonal job board (since 1995) with a dedicated filter for jobs that include employee housing: ski resorts, national-park lodges, dude r… |
| [LugLess](https://www.lugless.com) | luggage-shipping | 55 | 60 | A luggage-shipping engine that rate-shops FedEx and UPS excess ground capacity to move suitcases, skis, and golf bags door-to-door from ~… |
| [Nappr](https://www.nappr.io/) | hourly-hotel-naps | 58 | 55 | Marketplace for booking hotel rooms by the hour (2-12 hour daytime blocks) at 5,300+ properties in ~500 cities and 60 major airports, at … |
| [Yindii](https://www.yindii.co) | surplus-food | 55 | 58 | Southeast Asia's largest surplus-food marketplace: end-of-day 'surprise boxes' from hotels, bakeries and restaurants in Bangkok, Hong Kon… |
| [SpareHolidays](https://spareholidays.com) | flight-and-holiday-resale | 68 | 38 | Newer travel-resale marketplace covering flights, hotels, trains, buses, car rentals, cruises and full holiday packages. You forward your… |
| [Cargo Ship Voyages](https://www.cargoshipvoyages.com/) | freighter-travel | 80 | 20 | A 30+ year-old UK broker that books passengers into spare cabins on working cargo and coastal freight ships. You live aboard a working ve… |
| [Langsamreisen (Slow Travel) freighter desk](https://www.langsamreisen.de/en/freightertravel) | freighter-travel | 72 | 32 | German 'slow travel' agency that books passenger cabins on container ships and mail/supply ships — e.g. Belgium to Finland, Netherlands t… |
| [REMPART](https://www.rempart.com/en/) | heritage-restoration | 60 | 50 | Union of 180+ French heritage associations running volunteer restoration workcamps: you help rebuild castles, ramparts, chapels and medie… |
| [Kibbutz Volunteers Program Center (KPC)](https://kibbutzvolunteers.org.il) | farm-communal-work | 55 | 55 | The official Israeli placement office (operating since 1967, 400,000+ alumni) for volunteering on a kibbutz: 10 weeks to 12 months of com… |
| [Pintrip](https://pintrip.eu/en/) | farm-stay-network | 55 | 55 | Denmark's farm-stopover membership: ~300 hosts and 700+ overnight spots at farms, distilleries, dairies and country estates where members… |
| [Olio](https://olioapp.com/en/) | surplus-food | 68 | 35 | Hyper-local sharing app where neighbors and 'Food Waste Hero' volunteers give away surplus food (and household items) completely free; op… |
| [New Dungeness Light Station Keeper Program](https://newdungenesslighthouse.com/keeper-program/) | lighthouse-caretaking | 72 | 28 | A volunteer program where members ($35 individual / $50 family annual membership) reserve a full week living in the restored 1857 keeper'… |
| [Gronze](https://www.gronze.com/) | pilgrim-hostels | 45 | 68 | The definitive Spanish-language database of pilgrim albergues on every Camino de Santiago route: stage-by-stage listings with bed counts,… |
| [TransferTravel](https://www.transfertravel.com) | travel-resale-general | 70 | 30 | The broadest-inventory 'unwanted travel' marketplace: discounted non-refundable flights, rail and coach tickets, festival tickets and pac… |
| [KnowDelay](https://knowdelay.com/) | delay-prediction | 62 | 42 | Built by pilots and meteorologists, it predicts weather-driven airport delays up to 3 days in advance for the 35 most delay-prone US airp… |
| [iOverlander](https://ioverlander.com) | free-campsite-database | 40 | 75 | A traveler-built global database of free and informal sleeping spots (wild camps, safe street parking, water and dump points), with 1M+ c… |
| [ByHours](https://www.byhours.com/en) | microstay-hotels | 55 | 52 | Books hotel rooms as 'microstays' in packs of 3, 6, or 12 hours at 4,000+ hotels across ~24 countries (Europe, LatAm, Middle East hubs), … |
| [Freedge](https://freedge.org) | community-fridges | 75 | 22 | Global map and database of independent community fridges ('freedges') — public refrigerators stocked with free food, open to anyone, anon… |
| [SeatSpy](https://www.seatspy.com) | award-calendar | 48 | 62 | Shows a full year of reward-seat availability for a route in one calendar view for British Airways, Virgin Atlantic, American, Cathay, Ai… |
| [Travel-Dealz Error Fares](https://travel-dealz.com/tag/error-fares/) | error-fare-alerts-europe | 45 | 65 | The English edition of the hardcore German deal-hunting site Travel-Dealz, with a dedicated running feed of error fares (economy and prem… |
| [EUclaim Flight Checker](https://www.euclaim.com/) | compensation-eligibility-data | 45 | 65 | A claim firm whose real asset is a forensic flight database ingesting ~13 million flight, weather, and news reports per day going back ye… |
| [Koyasan Shukubo Association](https://eng-shukubo.net/) | temple-lodging-koyasan | 55 | 48 | Official association portal for the 51 temple lodgings on Mt. Koya (Koyasan), Japan's sacred mountain monastery town — browse each shukub… |
| [Templestay (Jogye Order of Korean Buddhism)](https://eng.templestay.com/) | temple-stay-korea | 48 | 58 | Official English booking portal of Korea's Jogye Order for overnight temple stays at Buddhist temples nationwide — searchable by temple, … |
| [Guess Where Trips](https://guesswheretrips.com/en-us) | surprise-roadtrip | 68 | 28 | Pre-planned surprise one-day road trips sold as five sealed envelopes ($65 physical / $39 digital): a 'Before You Go' envelope plus four … |
| [BestTime.app](https://besttime.app/) | venue-foot-traffic-forecast | 65 | 32 | Foot-traffic forecasting for millions of public venues (attractions, museums, restaurants, bars, gyms) in 150+ countries, derived from an… |
| [Troc des Trains](https://www.trocdestrains.com) | train-ticket-resale | 55 | 45 | Free French peer-to-peer exchange entirely dedicated to reselling non-exchangeable, non-refundable train tickets (SNCF, Ouigo, Eurostar, … |
| [FerryGoGo](https://ferrygogo.co.uk/) | overnight-ferry-tool | 55 | 45 | Independent ferry comparison and guide site for European routes: compares operators, crossing times, cabin types and live fares, with fir… |
| [Monastery Stays](https://www.monasterystays.com/) | monastery-booking | 55 | 45 | English-language booking service (est. 2006) for 500+ convent and monastery guest houses across Italy and Austria, with real-time availab… |
| [refundrebel](https://www.refundrebel.com/) | refund-automation | 55 | 45 | German legal-tech service that automates EU rail passenger-rights claims: upload or forward your Deutsche Bahn ticket after a 60+ minute … |
| [Rialto Vacations](https://rialtovacations.com) | timeshare-rental-marketplace | 55 | 45 | A newer (2025-2026) timeshare rental platform where owners list unused weeks free of commission and guests pay a flat 10% service fee — u… |
| [Nachtzug.net](https://nachtzug.net/en/) | night-train-aggregator | 48 | 55 | Independent platform that consolidates every European night-train connection in one place: route pages with timetables, seat/couchette/sl… |
| [FlightList](https://www.flightlist.io/) | cheapest-anywhere-engine | 48 | 55 | A free, ad-free one-way/round-trip search engine built for people with no fixed dates and no fixed destination: search across 30/60/90/18… |
| [FareDetective](https://www.faredetective.com/farehistory/) | airfare-history | 60 | 35 | One of the only consumer-accessible archives of historical airfare: interactive fare-history charts for roughly 1 million route combinati… |
| [eSIMDB](https://esimdb.com) | esim-arbitrage | 40 | 65 | A cross-provider database of 400,000+ prepaid travel eSIM plans from 170+ providers, filterable per country by cheapest price, best price… |
| [FlyHouse ASAP (formerly JetASAP)](https://jetasap.com/) | charter-direct-bidding | 55 | 42 | An app that broadcasts your trip request directly to 700+ FAA charter operators who bid back live bookable quotes — no broker, no commiss… |
| [Hotel Hops](https://www.hotelhops.com/) | hotel-rebooking | 52 | 45 | Tiny free service: upload or forward your hotel confirmation from anywhere (Booking, Expedia, direct) and it monitors the whole web for a… |
| [Waynabox](https://waynabox.com/en) | mystery-package | 55 | 40 | Barcelona-based surprise-trip engine: choose departure airport, dates, and traveler count, veto a few cities, pay from €150 per person fo… |
| [srprs.me](https://srprs.me/) | mystery-package | 65 | 25 | Dutch pioneer of surprise city breaks: book a trip to 'destination unknown', get told only the weather forecast beforehand, and reveal wh… |
| [MyResortNetwork](https://www.myresortnetwork.com) | owner-direct-classifieds | 45 | 55 | An old-school flat-fee classifieds site where timeshare owners advertise weeks for rent directly: owners pay ~$19.95 to list and keep 100… |
| [LoungePair](https://www.loungepair.com) | lounge-access | 45 | 55 | A marketplace for airport lounge access without any premium credit card or membership: buy single-entry passes to 1,400+ lounges a la car… |
| [TABETE](https://tabete.me) | surplus-food | 48 | 50 | Japan's food-rescue app: 1.2M+ users buy end-of-day surplus from 3,000+ bakeries, delis and restaurants across Tokyo, Osaka, Sapporo, Nag… |
| [Minute Suites](https://minutesuites.com/) | airport-nap-suites | 42 | 58 | Private lockable mini-suites inside airport security at US hubs (ATL, DFW, PHL, CLT, JFK, SLC), rented by the hour with a daybed, workspa… |
| [mymizu](https://www.mymizu.co) | free-water-map | 55 | 38 | Free water-refill map born in Japan: 200,000+ mapped spots in ~50 countries (13,000+ in Japan) — public fountains plus cafés/shops/hotels… |
| [Viatrec](https://viatrec.com/) | rv-relocation | 50 | 45 | US-focused $1/day RV and campervan relocation platform: partners with American RV rental companies to fill their fleet-repositioning driv… |
| [CruiseMapper Repositioning Finder](https://www.cruisemapper.com/repositioning) | repositioning-cruises | 40 | 58 | A free database and filter tool for ship-relocation voyages: currently 1,376 repositioning itineraries for 2026-2029, searchable by year,… |
| [Pack Up + Go](https://www.packupgo.com/) | mystery-agency | 62 | 25 | US surprise-travel agency: you fill out a pre-trip survey (interests, travel history, budget), they book a 3-day US getaway — plane, road… |
| [ErrorFareAlerts](https://errorfarealerts.com) | automated-error-fare-scanner | 45 | 50 | German-built automated error-fare detector: its algorithm continuously scans the web for airline pricing mistakes and extreme anomalies i… |
| [Terahaku](https://terahaku.jp/) | temple-stay-japan | 55 | 35 | Japan's dedicated search-and-reservation platform for shukubo (temple lodging), listing Buddhist temples across the country — from tradit… |
| [AirAdvisor Live Disruption Tracker](https://airadvisor.com/en-us/flights) | compensation-eligibility-data | 45 | 50 | A constantly updated public list of flights delayed or canceled today (US and worldwide), each annotated with the estimated compensation … |
| [Hookhub](https://www.hookhub.co) | boondocking-marketplace | 55 | 35 | A US marketplace where ranchers, farmers and rural landowners rent out raw private land for RV parking, boondocking and long-term stays w… |
| [Fahrgemeinschaft.de](https://www.fahrgemeinschaft.de) | rideshare-board | 45 | 50 | Germany's commission-free rideshare board with roughly 1.5 million users and about 3 million listings a year: drivers and riders contact … |
| [Vandrouki](https://vandrouki.ru) | regional-community-cis | 40 | 55 | Legendary Russian-language budget-travel community ('ways to travel almost for free') that posts error fares, glitch promos and absurdly … |
| [Promociones Aéreas](https://promociones-aereas.com.ar) | regional-community-latam | 38 | 58 | Argentine flight-deal watchdog that reviews about 1,300 air routes daily across metasearch engines and OTAs, publishing 'tarifa error' (m… |
| [MindMyHouse](https://www.mindmyhouse.com/) | house-sitting | 40 | 55 | A deliberately small, ad-free 'mom and pop' house-sitting matchmaker running since 2005. Sitters pay US$29/year — the lowest fee of any s… |
| [WILLER Travel / Japan Bus Pass](https://willer-travel.com/en/) | sleeper-bus-pass | 55 | 30 | English-language booking platform for Japan's highway and overnight night buses, including the foreigner-only Japan Bus Pass: 3 days of u… |
| [Napcabs](https://www.napcabs.com/) | airport-sleep-pods | 45 | 45 | Single-occupancy sleeping cabins installed in German airports (Munich, Berlin BER, Stuttgart, Frankfurt) with online booking at booking.n… |
| [Flyagain.la](https://flyagain.la) | regional-community-asia | 30 | 62 | Hong Kong Cantonese-language fare-alert site posting cheap-fare anomalies, flash sales and package glitches for HKG departures within hou… |
| [Skycop Care](https://www.skycop.com/skycop-care/) | auto-claim-subscription | 40 | 45 | A flat subscription (~€31.99/year) from Lithuanian claim firm Skycop that drops their success fee to 0% on unlimited claims: register you… |
| [Terego](https://www.terego.ca/en) | farm-stay-network | 32 | 55 | Canada's farm/brewery/winery overnight network: 1,700+ free RV parking spots offered by local producers, bookable up to 30 days ahead. On… |
| [Sleepover (sleep 'n fly)](https://sleep-n-fly.com/en) | airport-sleep-pods | 30 | 55 | Direct-booking platform for hourly sleep pods, capsules and cabins located airside in the transit zones of Dubai DXB, Doha DOH and Lima a… |
| [HotelPriceTracker](https://hotelpricetracker.io/en) | hotel-price-history | 40 | 35 | A completely free hotel rate monitor: paste any hotel URL with your dates and it watches the price 24/7, charts full day-by-day price his… |
| [TicketSpy](https://ticketspy.nl) | regional-community-benelux | 25 | 55 | Dutch deal-hunting crew posting 6-10 flight/travel deals per day for Benelux departures, with loudly flagged 'ERROR FARE!!!' posts (KLM/D… |
| [LuggageHero](https://luggagehero.com/) | luggage-storage-network | 30 | 45 | A luggage-storage network that stashes your bags inside vetted everyday businesses — cafes, souvenir shops, bike shops, hotels — across U… |
| [Camli Hidden City](https://camli.com/hidden-city) | hidden-city | 42 | 18 | A small flight platform with a dedicated hidden-city engine: you enter your real origin and destination and it generates candidate routin… |
| [Luxury House Sitting](https://www.luxuryhousesitting.com/) | estate-sitting | 45 | 13 | A niche board ($45/yr for sitters) focused on high-end homes and estates — Beverly Hills, San Diego, Colorado mountain homes — posting ro… |
