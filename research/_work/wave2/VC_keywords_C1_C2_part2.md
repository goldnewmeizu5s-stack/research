# VC (verification) — C1 + C2, часть 2 (кластеры, не проверявшиеся первым верификатором)

Верификатор: независимый (part 2). Дата доступа: 2026-09-04. Инструмент: `mcp__Firecrawl__firecrawl_search` (`highlights: true`, `limit` как заявлено), один вызов за раз. WebSearch недоступен. Ничего из памяти.

Область проверки: C1 — кластеры 5, 6, 7, 9, 10, 12, 13, 15, 16, 20; C2 — K03, K04, K06, K10, K11, K12, K13, K15, K16, K17, K18, K19, K21, K23, K24, K25, K26, K27, K28, K29, K30, L02. Кластеры C1 1-4, 8, 11, 14, 17-19 и C2 K01, K02, K05, K07-K09, K14, K20, K22, L01 НЕ проверялись (закреплены за другим верификатором).

Критерий по числу результатов: совпадение в пределах ±30% = подтверждено.
Все "числа" в проверяемых кластерах — это число результатов выдачи Firecrawl, а не объём поиска/CPC/difficulty; отдельно проверено отсутствие непроверяемых метрик (колонка «метрики без инструмента»).

## Таблица проверки

| Файл | Кластер | Запрос (дословно) | Заявлено / получено мной | Доказательный URL | Открыт? | Дословный фрагмент | Платформ ≥ 2? | Вердикт | Комментарий |
|---|---|---|---|---|---|---|---|---|---|
| C1 | 5 — диабетические носки vs компрессионные | `site:reddit.com diabetic socks neuropathy feet swelling` (limit 10); `site:diabetesdaily.com diabetic socks shoes recommendations` (limit 10) | 10 / 10; 10 / 10 | reddit.com/r/neuropathy/comments/174ebhe/compression_socks_for_neuropathy/ ; diabetesdaily.com/forum/threads/socks-recommendations.141665/ | да (оба в выдаче с title+description) | "compression socks can be bad for neuropathy as they force" ; "100% cotton-- that's best for absorbing perspiration" | да (reddit.com + diabetesdaily.com) | CONFIRMED | Все 3 заявленных reddit-URL (1vy36mw, 174ebhe, 1k8ncgw) и все 3 diabetesdaily-URL (141665, 148220, 84524) присутствуют в выдаче. Формулировки «тонкие носки вместо толстых» и «semi-stylish» подтверждены дословно. Метрик объёма/CPC/difficulty нет — везде «не измерено». |
| C1 | 6 — десерты без сахара / тяга к сладкому (в т.ч. ГСД) | `site:reddit.com diabetes sugar free dessert recipe craving` (limit 10); `site:quora.com diabetic dessert sugar free recipe` (limit 10) | 10 / 10; 10 / 10 | reddit.com/r/diabetes/comments/1hc1utr/diabetes_friendly_desserts/ ; quora.com/How-do-you-make-a-sugar-free-keto-cheesecake | да (оба в выдаче) | "Whipped Cream is surprisingly low carb and goes great" ; "use Stevia or Erythritol (sugar substitute) instead of sugar" | да (reddit.com + quora.com) | CONFIRMED | Заявленные reddit-URL 1lflknq, k9avm1, 1hc1utr и оба quora-URL присутствуют. Формулировки «взбитые сливки низкоуглеводны», «no-bake батончики из миндальной муки и арахисовой пасты», «эритрит» подтверждены дословно. Метрик без инструмента нет. |
