"""
CityMind AI — Backend (FastAPI + WebSocket)
==========================================
Запуск: uvicorn main:app --reload --port 8000

Структура:
  GET  /health              — проверка
  GET  /api/city-state      — текущий снимок метрик (для первой загрузки)
  POST /api/simulate        — симуляция решения
  WS   /ws/city             — реалтайм поток данных каждые 3 сек
  
  (внутренний) POST /internal/llm-insight — сюда МЛ-разработчик пушит текст
"""

import asyncio
import random
import time
from collections import deque
from typing import Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI(title="CityMind AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # на хакатоне не парься с безопасностью
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────
# СОСТОЯНИЕ В ПАМЯТИ
# ─────────────────────────────────────────

# История метрик за последние 60 точек (~3 мин при интервале 3 сек)
history: deque = deque(maxlen=60)

# Последний текст от МЛ (LLM рекомендация)
llm_insight_cache: dict = {
    "text": "Система анализирует данные...",
    "updated_at": 0,
}

# Активные WebSocket клиенты
connected_clients: list[WebSocket] = []

# Текущий "режим" симуляции (None = обычный режим)
simulation_mode: Optional[dict] = None
simulation_until: float = 0  # timestamp когда симуляция заканчивается


# ─────────────────────────────────────────
# ГЕНЕРАЦИЯ MOCK ДАННЫХ
# ─────────────────────────────────────────

def generate_metrics() -> dict:
    """
    Генерирует реалистичные метрики.
    Если активна симуляция — применяет модификаторы.
    """
    global simulation_mode, simulation_until

    base_traffic = 65
    base_air = 110
    base_noise = 55

    # Суточный паттерн: утром и вечером пробки выше
    hour = time.localtime().tm_hour
    if 7 <= hour <= 9 or 17 <= hour <= 19:
        base_traffic += 20
        base_air += 30

    traffic = min(100, max(0, base_traffic + random.gauss(0, 8)))
    air_quality = min(300, max(0, base_air + random.gauss(0, 15)))
    noise_level = min(100, max(0, base_noise + random.gauss(0, 5)))
    pedestrian_flow = random.randint(200, 800)
    incidents = random.choices([0, 1, 2], weights=[70, 25, 5])[0]

    # Применяем симуляцию если активна
    if simulation_mode and time.time() < simulation_until:
        mod = simulation_mode.get("modifiers", {})
        traffic = min(100, max(0, traffic + mod.get("traffic", 0)))
        air_quality = min(300, max(0, air_quality + mod.get("air_quality", 0)))
        noise_level = min(100, max(0, noise_level + mod.get("noise", 0)))
    elif simulation_mode and time.time() >= simulation_until:
        simulation_mode = None  # симуляция закончилась

    return {
        "traffic_index": round(traffic, 1),
        "air_quality_index": round(air_quality, 1),
        "noise_level": round(noise_level, 1),
        "pedestrian_flow": pedestrian_flow,
        "active_incidents": incidents,
    }


# ─────────────────────────────────────────
# RULE-BASED AI ДВИЖОК
# ─────────────────────────────────────────

def analyze(metrics: dict) -> dict:
    """
    Три слоя: детекция → критичность → рекомендации.
    Это и есть "AI" который отличает нас от простого дашборда.
    """
    traffic = metrics["traffic_index"]
    air = metrics["air_quality_index"]
    noise = metrics["noise_level"]
    incidents = metrics["active_incidents"]

    problems = []
    actions = []

    # — Детекция проблем —
    if traffic > 80:
        problems.append("Критические пробки в центральном районе")
        actions.append("Увеличить частоту автобусов на 40%")
        actions.append("Активировать динамическое управление светофорами")
    elif traffic > 60:
        problems.append("Повышенная нагрузка на дорожную сеть")
        actions.append("Рекомендовать объездные маршруты через приложение")

    if air > 150:
        problems.append("Опасный уровень загрязнения воздуха")
        actions.append("Ограничить въезд дизельного транспорта в центр")
        actions.append("Отправить оповещение жителям")
    elif air > 100:
        problems.append("Повышенное загрязнение воздуха")
        actions.append("Усилить мониторинг воздуха в жилых кварталах")

    if noise > 70:
        problems.append("Превышение нормы шума")
        actions.append("Проверить строительные работы в зоне")

    if incidents > 0:
        problems.append(f"Зафиксировано инцидентов: {incidents}")
        actions.append("Направить патрульные бригады")

    # — Причинно-следственная связь (это жюри запомнит) —
    causal_link = None
    if traffic > 70 and air > 120:
        causal_link = "Пробки напрямую усиливают загрязнение воздуха: снижение трафика на 20% даст улучшение AQI ~15 единиц"

    # — Оценка критичности —
    score = traffic * 0.5 + air * 0.35 + noise * 0.1 + incidents * 10
    if score > 130:
        level = "HIGH"
        level_ru = "Критический"
    elif score > 85:
        level = "MEDIUM"
        level_ru = "Средний"
    else:
        level = "LOW"
        level_ru = "Нормальный"

    # — City Health Score (0–100, инвертированный) —
    health_score = max(0, round(100 - (score / 2.2)))

    return {
        "level": level,
        "level_ru": level_ru,
        "city_health_score": health_score,
        "composite_score": round(score, 1),
        "problems": problems if problems else ["Все показатели в норме"],
        "actions": actions if actions else ["Штатный режим мониторинга"],
        "causal_link": causal_link,
        "is_simulation": simulation_mode is not None and time.time() < simulation_until,
    }


# ─────────────────────────────────────────
# ФОНОВАЯ ЗАДАЧА: генерация и рассылка
# ─────────────────────────────────────────

async def city_data_loop():
    """Каждые 3 секунды генерирует новые данные и рассылает всем клиентам."""
    while True:
        await asyncio.sleep(20)

        metrics = generate_metrics()
        insights = analyze(metrics)

        snapshot = {
            "timestamp": time.time(),
            "metrics": metrics,
            "insights": insights,
            "llm_recommendation": llm_insight_cache["text"],
            # Последние 20 точек истории для графиков
            "history": list(history)[-20:],
        }

        history.append({
            "timestamp": snapshot["timestamp"],
            "traffic_index": metrics["traffic_index"],
            "air_quality_index": metrics["air_quality_index"],
            "noise_level": metrics["noise_level"],
        })

        # Рассылаем всем подключённым клиентам
        dead = []
        for ws in connected_clients:
            try:
                await ws.send_text(json.dumps(snapshot, ensure_ascii=False))
            except Exception:
                dead.append(ws)

        for ws in dead:
            connected_clients.remove(ws)


@app.on_event("startup")
async def startup():
    asyncio.create_task(city_data_loop())


# ─────────────────────────────────────────
# WEBSOCKET ENDPOINT
# ─────────────────────────────────────────

@app.websocket("/ws/city")
async def websocket_city(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    # Сразу отправляем первый снимок не ждя 3 сек
    metrics = generate_metrics()
    insights = analyze(metrics)
    await websocket.send_text(json.dumps({
        "timestamp": time.time(),
        "metrics": metrics,
        "insights": insights,
        "llm_recommendation": llm_insight_cache["text"],
        "history": [],
    }, ensure_ascii=False))

    try:
        while True:
            # Просто держим соединение живым, данные шлём из loop
            await websocket.receive_text()
    except WebSocketDisconnect:
        connected_clients.remove(websocket)


# ─────────────────────────────────────────
# REST ENDPOINTS
# ─────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok", "clients_connected": len(connected_clients)}


@app.get("/api/city-state")
def city_state():
    """Разовый снимок — для первой загрузки страницы."""
    metrics = generate_metrics()
    insights = analyze(metrics)
    return {
        "timestamp": time.time(),
        "metrics": metrics,
        "insights": insights,
        "llm_recommendation": llm_insight_cache["text"],
        "history": list(history)[-20:],
    }


# ─────────────────────────────────────────
# СИМУЛЯЦИЯ
# ─────────────────────────────────────────

SIMULATION_SCENARIOS = {
    "close_road": {
        "label": "Закрыть центральную дорогу",
        "duration_sec": 30,
        "modifiers": {"traffic": +15, "air_quality": -5, "noise": -3},
        "side_effects": [
            "Трафик смещается на Кольцевую +15%",
            "Центральный район разгружается",
            "Возможные задержки для экстренных служб",
        ],
        "prediction": "Кратковременное увеличение пробок на периферии, долгосрочное улучшение воздуха в центре",
    },
    "increase_buses": {
        "label": "Увеличить частоту автобусов",
        "duration_sec": 30,
        "modifiers": {"traffic": -18, "air_quality": -12, "noise": -2},
        "side_effects": [
            "Снижение числа личных автомобилей на ~12%",
            "Требуется дополнительный бюджет: ~2.4M тг/день",
        ],
        "prediction": "Устойчивое улучшение трафика через 25-40 минут после запуска",
    },
    "restrict_diesel": {
        "label": "Ограничить дизельный транспорт",
        "duration_sec": 30,
        "modifiers": {"traffic": -5, "air_quality": -35, "noise": -8},
        "side_effects": [
            "Часть грузовиков переходит на объездные маршруты",
            "Возможное недовольство перевозчиков",
        ],
        "prediction": "Значительное улучшение AQI в течение 15-20 минут",
    },
    "green_wave": {
        "label": "Включить зелёную волну",
        "duration_sec": 30,
        "modifiers": {"traffic": -22, "air_quality": -8, "noise": -5},
        "side_effects": [
            "Снижение времени в пути на 18%",
            "Снижение выбросов CO2 за счёт плавного движения",
        ],
        "prediction": "Быстрый эффект — улучшение через 5-10 минут",
    },
}


class SimulateRequest(BaseModel):
    scenario: str  # ключ из SIMULATION_SCENARIOS


@app.post("/api/simulate")
def simulate(req: SimulateRequest):
    global simulation_mode, simulation_until

    scenario = SIMULATION_SCENARIOS.get(req.scenario)
    if not scenario:
        return {"error": f"Unknown scenario. Available: {list(SIMULATION_SCENARIOS.keys())}"}

    simulation_mode = scenario
    simulation_until = time.time() + scenario["duration_sec"]

    return {
        "status": "simulation_started",
        "scenario": req.scenario,
        "label": scenario["label"],
        "duration_sec": scenario["duration_sec"],
        "modifiers": scenario["modifiers"],
        "side_effects": scenario["side_effects"],
        "prediction": scenario["prediction"],
    }


@app.get("/api/scenarios")
def get_scenarios():
    """Список доступных сценариев — фронт строит кнопки из этого."""
    return {
        key: {"label": val["label"], "prediction": val["prediction"]}
        for key, val in SIMULATION_SCENARIOS.items()
    }


# ─────────────────────────────────────────
# ИНТЕГРАЦИЯ С МЛ-РАЗРАБОТЧИКОМ
# ─────────────────────────────────────────

class LLMInsightRequest(BaseModel):
    text: str
    context_snapshot: Optional[dict] = None  # МЛ может прислать контекст обратно


@app.post("/internal/llm-insight")
def receive_llm_insight(req: LLMInsightRequest):
    """
    МЛ-разработчик вызывает этот endpoint когда LLM сгенерировала текст.
    Текст попадёт в следующий WebSocket broadcast автоматически.
    """
    llm_insight_cache["text"] = req.text
    llm_insight_cache["updated_at"] = time.time()
    return {"status": "ok", "updated_at": llm_insight_cache["updated_at"]}


@app.get("/internal/current-metrics")
def current_metrics_for_ml():
    """
    МЛ-разработчик периодически дёргает этот endpoint
    чтобы получить свежие метрики и сгенерировать новый текст.
    """
    metrics = generate_metrics()
    insights = analyze(metrics)
    return {
        "metrics": metrics,
        "insights": insights,
        "prompt_hint": (
            f"Traffic index: {metrics['traffic_index']}/100, "
            f"Air quality: {metrics['air_quality_index']} AQI, "
            f"City health: {insights['city_health_score']}/100, "
            f"Alert level: {insights['level_ru']}. "
            f"Problems: {', '.join(insights['problems'])}. "
            f"Write a concise 2-sentence city management recommendation in Russian."
        )
    }
