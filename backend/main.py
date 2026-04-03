"""
CityMind AI — Backend (FastAPI + WebSocket)
==========================================
Запуск: uvicorn main:app --reload --port 8000
"""

import asyncio
import random
import time
from collections import deque
from typing import Optional, Dict
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI(title="CityMind AI Multi-City")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────
# СОСТОЯНИЕ В ПАМЯТИ ПО ГОРОДАМ
# ─────────────────────────────────────────

CITIES = ["Алматы", "Астана", "Шымкент"]

class CityState:
    def __init__(self, name: str):
        self.name = name
        self.history = deque(maxlen=60)
        self.simulation_mode: Optional[dict] = None
        self.simulation_until: float = 0
        self.llm_insight = "Система анализирует данные..."
        
        # Разные базовые показатели для реализма
        if name == "Алматы":
            self.base_traffic = 65
            self.base_air = 110
        elif name == "Астана":
            self.base_traffic = 45
            self.base_air = 80
        else: # Шымкент
            self.base_traffic = 55
            self.base_air = 100

# Инициализируем состояния для всех городов
city_states: Dict[str, CityState] = {name: CityState(name) for name in CITIES}

# Активные WebSocket клиенты с привязкой к городу
# { websocket: city_name }
connected_clients: Dict[WebSocket, str] = {}

# ─────────────────────────────────────────
# ГЕНЕРАЦИЯ MOCK ДАННЫХ
# ─────────────────────────────────────────

def generate_metrics(city: CityState) -> dict:
    hour = time.localtime().tm_hour
    traffic_spike = 20 if (7 <= hour <= 9 or 17 <= hour <= 19) else 0
    air_spike = 30 if (7 <= hour <= 9 or 17 <= hour <= 19) else 0

    traffic = min(100, max(0, city.base_traffic + traffic_spike + random.gauss(0, 8)))
    air_quality = min(300, max(0, city.base_air + air_spike + random.gauss(0, 15)))
    noise_level = min(100, max(0, 55 + random.gauss(0, 5)))
    pedestrian_flow = random.randint(200, 800)
    incidents = random.choices([0, 1, 2], weights=[75, 20, 5])[0]

    # Применяем симуляцию
    if city.simulation_mode and time.time() < city.simulation_until:
        mod = city.simulation_mode.get("modifiers", {})
        traffic = min(100, max(0, traffic + mod.get("traffic", 0)))
        air_quality = min(300, max(0, air_quality + mod.get("air_quality", 0)))
        noise_level = min(100, max(0, noise_level + mod.get("noise", 0)))
    elif city.simulation_mode and time.time() >= city.simulation_until:
        city.simulation_mode = None

    return {
        "traffic_index": round(traffic, 1),
        "air_quality_index": round(air_quality, 1),
        "noise_level": round(noise_level, 1),
        "pedestrian_flow": pedestrian_flow,
        "active_incidents": incidents,
    }

def analyze(metrics: dict, city: CityState) -> dict:
    traffic = metrics["traffic_index"]
    air = metrics["air_quality_index"]
    noise = metrics["noise_level"]
    incidents = metrics["active_incidents"]

    problems = []
    actions = []

    if traffic > 80:
        problems.append(f"Критические пробки: {city.name}")
        actions.append("Увеличить частоту автобусов")
    elif traffic > 60:
        problems.append("Повышенная нагрузка на дороги")
        actions.append("Рекомендовать объездные пути")

    if air > 140:
        problems.append("Неудовлетворительное качество воздуха")
        actions.append("Ограничить въезд грузового транспорта")
    
    if incidents > 0:
        problems.append(f"Активных инцидентов: {incidents}")

    score = traffic * 0.5 + air * 0.35 + noise * 0.1 + incidents * 10
    
    level = "HIGH" if score > 120 else ("MEDIUM" if score > 80 else "LOW")
    level_ru = "Критический" if level == "HIGH" else ("Средний" if level == "MEDIUM" else "Нормальный")
    health_score = max(0, round(100 - (score / 2.2)))

    return {
        "level": level,
        "level_ru": level_ru,
        "city_health_score": health_score,
        "composite_score": round(score, 1),
        "problems": problems if problems else ["Все показатели в норме"],
        "actions": actions if actions else ["Штатный режим мониторинга"],
        "is_simulation": city.simulation_mode is not None,
    }

# ─────────────────────────────────────────
# ФОНОВАЯ ЗАДАЧА
# ─────────────────────────────────────────

async def city_data_loop():
    while True:
        await asyncio.sleep(3)
        
        for name, city in city_states.items():
            metrics = generate_metrics(city)
            insights = analyze(metrics, city)
            
            snapshot = {
                "city": name,
                "timestamp": time.time(),
                "metrics": metrics,
                "insights": insights,
                "llm_recommendation": city.llm_insight,
                "history": list(city.history)[-20:],
            }

            city.history.append({
                "timestamp": snapshot["timestamp"],
                "traffic_index": metrics["traffic_index"],
                "air_quality_index": metrics["air_quality_index"],
                "noise_level": metrics["noise_level"],
            })

            # Рассылаем клиентам этого города
            dead = []
            for ws, client_city in connected_clients.items():
                if client_city == name:
                    try:
                        await ws.send_text(json.dumps(snapshot, ensure_ascii=False))
                    except:
                        dead.append(ws)
            
            for ws in dead:
                if ws in connected_clients:
                    del connected_clients[ws]

@app.on_event("startup")
async def startup():
    asyncio.create_task(city_data_loop())

# ─────────────────────────────────────────
# ENDPOINTS
# ─────────────────────────────────────────

@app.websocket("/ws/city")
async def websocket_city(websocket: WebSocket, city: str = "Алматы"):
    await websocket.accept()
    if city not in city_states:
        city = "Алматы"
    connected_clients[websocket] = city

    # Initial snapshot
    cs = city_states[city]
    metrics = generate_metrics(cs)
    insights = analyze(metrics, cs)
    await websocket.send_text(json.dumps({
        "city": city,
        "timestamp": time.time(),
        "metrics": metrics,
        "insights": insights,
        "llm_recommendation": cs.llm_insight,
        "history": list(cs.history)[-20:],
    }, ensure_ascii=False))

    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        if websocket in connected_clients:
            del connected_clients[websocket]

@app.get("/api/city-state")
def city_state(city: str = "Алматы"):
    if city not in city_states:
        city = "Алматы"
    cs = city_states[city]
    metrics = generate_metrics(cs)
    insights = analyze(metrics, cs)
    return {
        "city": city,
        "timestamp": time.time(),
        "metrics": metrics,
        "insights": insights,
        "llm_recommendation": cs.llm_insight,
        "history": list(cs.history)[-20:],
    }

SIMULATION_SCENARIOS = {
    "close_road": {"label": "Закрыть центральную дорогу", "duration_sec": 30, "modifiers": {"traffic": +15, "air_quality": -5}, "prediction": "Перегрузка периферии"},
    "increase_buses": {"label": "Увеличить частоту автобусов", "duration_sec": 30, "modifiers": {"traffic": -18, "air_quality": -12}, "prediction": "Улучшение через 30 мин"},
    "restrict_diesel": {"label": "Ограничить дизельный транспорт", "duration_sec": 30, "modifiers": {"traffic": -5, "air_quality": -35}, "prediction": "Резкое улучшение AQI"},
    "green_wave": {"label": "Включить зелёную волну", "duration_sec": 30, "modifiers": {"traffic": -22, "air_quality": -8}, "prediction": "Быстрый эффект оптимизации"},
}

class SimulateRequest(BaseModel):
    scenario: str
    city: str = "Алматы"

@app.post("/api/simulate")
def simulate(req: SimulateRequest):
    cs = city_states.get(req.city, city_states["Алматы"])
    scenario = SIMULATION_SCENARIOS.get(req.scenario)
    if not scenario: return {"error": "Unknown scenario"}
    
    cs.simulation_mode = scenario
    cs.simulation_until = time.time() + scenario["duration_sec"]
    return {"status": "started", "city": cs.name, "scenario": req.scenario}

@app.get("/api/scenarios")
def get_scenarios():
    return {k: {"label": v["label"], "prediction": v["prediction"]} for k,v in SIMULATION_SCENARIOS.items()}

@app.get("/health")
def health():
    return {"status": "ok", "total_clients": len(connected_clients)}
