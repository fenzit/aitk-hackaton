# CityMind AI — Стыковка команды

## Запуск бэка
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

---

## Для ФРОНТЕНДА

### WebSocket (основной поток данных)
```js
const ws = new WebSocket("ws://localhost:8000/ws/city");

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  // data.metrics        — текущие показатели
  // data.insights       — AI анализ (уровень, проблемы, действия)
  // data.llm_recommendation — текст от LLM
  // data.history        — массив последних 20 точек для графиков
};
```

### Структура data.metrics
```json
{
  "traffic_index": 74.3,       // 0–100
  "air_quality_index": 132.1,  // AQI (0–300)
  "noise_level": 61.4,         // 0–100 дБ
  "pedestrian_flow": 540,      // чел/час
  "active_incidents": 1
}
```

### Структура data.insights
```json
{
  "level": "HIGH",                        // HIGH / MEDIUM / LOW
  "level_ru": "Критический",
  "city_health_score": 42,               // 0–100 (общий балл города)
  "composite_score": 128.4,
  "problems": ["Критические пробки..."],
  "actions": ["Увеличить частоту автобусов..."],
  "causal_link": "Пробки напрямую усиливают загрязнение...", // или null
  "is_simulation": false
}
```

### Симуляция сценариев
```js
// 1. Получить список сценариев
const res = await fetch("http://localhost:8000/api/scenarios");
const scenarios = await res.json();
// { close_road: { label, prediction }, increase_buses: {...}, ... }

// 2. Запустить сценарий
await fetch("http://localhost:8000/api/simulate", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ scenario: "close_road" })
});
// Данные в WebSocket автоматически изменятся на 30 секунд
// data.insights.is_simulation будет true — покажи индикатор "симуляция активна"
```

---

## Для МЛ-РАЗРАБОТЧИКА

### Схема работы
```
[Твой скрипт] --GET--> /internal/current-metrics  (получаешь метрики + готовый prompt)
                                |
                          Вызываешь LLM
                                |
[Твой скрипт] --POST-> /internal/llm-insight       (шлёшь текст обратно)
```

### Пример интеграции
```python
import httpx
import time

BACKEND = "http://localhost:8000"

while True:
    # 1. Получаем метрики и готовый prompt
    r = httpx.get(f"{BACKEND}/internal/current-metrics")
    data = r.json()
    prompt = data["prompt_hint"]
    
    # 2. Вызываешь свою LLM (OpenAI / Anthropic / любую)
    text = your_llm_call(prompt)
    
    # 3. Отправляешь текст обратно — он попадёт в следующий broadcast
    httpx.post(f"{BACKEND}/internal/llm-insight", json={"text": text})
    
    time.sleep(15)  # обновлять каждые 15 сек достаточно
```

---

## Все endpoints
| Method | Path | Кто использует |
|--------|------|----------------|
| GET | /health | проверка |
| WS | /ws/city | Фронт (основной) |
| GET | /api/city-state | Фронт (первая загрузка) |
| GET | /api/scenarios | Фронт (список кнопок симуляции) |
| POST | /api/simulate | Фронт (запуск симуляции) |
| GET | /internal/current-metrics | МЛ |
| POST | /internal/llm-insight | МЛ |
