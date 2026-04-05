"""
CityMind AI — ML Service (Rule-based + Scoring Engine)
Хакатон-версия: полностью автономная, без внешних зависимостей.
Запуск: python ml_service.py
"""

import json
import time
import random
import os
import httpx
from datetime import datetime


# ─────────────────────────────────────────────
# КОНСТАНТЫ ПОРОГОВЫХ ЗНАЧЕНИЙ
# ─────────────────────────────────────────────
THRESHOLDS = {
    "traffic": {
        "high": 80,
        "medium": 60,
        "low": 40,
    },
    "aqi": {
        "hazardous": 200,
        "unhealthy": 150,
        "moderate": 100,
    },
    "noise": {
        "critical": 80,
        "high": 70,
        "medium": 60,
    },
    "pedestrian": {
        "high": 1000,
        "medium": 600,
    },
    "incidents": {
        "critical": 3,
        "high": 1,
    },
}

# Веса для composite_score (сумма = 500 при максимуме)
WEIGHTS = {
    "traffic": 0.8,
    "aqi": 0.3,
    "noise": 0.5,
    "pedestrian": 0.02,
    "incidents": 15.0,
}

SIMULATION_EFFECTS = {
    "close_road": {
        "traffic_index": +15,
        "noise_level": +5,
        "pedestrian_flow": +200,
    },
    "increase_buses": {
        "traffic_index": -12,
        "air_quality_index": -10,
        "pedestrian_flow": +150,
    },
    "restrict_cars": {
        "traffic_index": -20,
        "air_quality_index": -25,
        "noise_level": -8,
    },
    "emergency_response": {
        "active_incidents": -1,
        "traffic_index": +5,
    },
}


# ─────────────────────────────────────────────
# ДВИЖОК АНАЛИЗА
# ─────────────────────────────────────────────
def detect_problems(m: dict) -> list[str]:
    """Определяет список проблем по метрикам."""
    problems = []

    if m["traffic_index"] >= THRESHOLDS["traffic"]["high"]:
        problems.append(f"Критические пробки: индекс {m['traffic_index']:.1f}/100")
    elif m["traffic_index"] >= THRESHOLDS["traffic"]["medium"]:
        problems.append(f"Повышенная загруженность дорог: {m['traffic_index']:.1f}/100")

    if m["air_quality_index"] >= THRESHOLDS["aqi"]["hazardous"]:
        problems.append(f"Опасный уровень загрязнения воздуха: AQI {m['air_quality_index']:.1f}")
    elif m["air_quality_index"] >= THRESHOLDS["aqi"]["unhealthy"]:
        problems.append(f"Нездоровое качество воздуха: AQI {m['air_quality_index']:.1f}")
    elif m["air_quality_index"] >= THRESHOLDS["aqi"]["moderate"]:
        problems.append(f"Умеренное загрязнение воздуха: AQI {m['air_quality_index']:.1f}")

    if m["noise_level"] >= THRESHOLDS["noise"]["critical"]:
        problems.append(f"Критический уровень шума: {m['noise_level']:.1f} дБ")
    elif m["noise_level"] >= THRESHOLDS["noise"]["high"]:
        problems.append(f"Высокий уровень шума: {m['noise_level']:.1f} дБ")

    if m["pedestrian_flow"] >= THRESHOLDS["pedestrian"]["high"]:
        problems.append(f"Перегруженность пешеходных зон: {m['pedestrian_flow']} чел/час")
    elif m["pedestrian_flow"] >= THRESHOLDS["pedestrian"]["medium"]:
        problems.append(f"Повышенный пешеходный поток: {m['pedestrian_flow']} чел/час")

    if m["active_incidents"] >= THRESHOLDS["incidents"]["critical"]:
        problems.append(f"Множественные инциденты: {m['active_incidents']} активных")
    elif m["active_incidents"] >= THRESHOLDS["incidents"]["high"]:
        problems.append(f"Активный инцидент на дороге ({m['active_incidents']} шт.)")

    return problems if problems else ["Все показатели в пределах нормы"]


def generate_actions(m: dict, problems: list[str]) -> list[str]:
    """Генерирует конкретные рекомендации на основе проблем."""
    actions = []

    if m["traffic_index"] >= THRESHOLDS["traffic"]["high"]:
        actions.append("🚦 Активировать адаптивное управление светофорами на центральных перекрёстках")
        actions.append("🚌 Увеличить частоту автобусных маршрутов №№ 5, 12, 34 на 30%")
        actions.append("📢 Оповестить водителей об альтернативных маршрутах через табло и приложение")
    elif m["traffic_index"] >= THRESHOLDS["traffic"]["medium"]:
        actions.append("🚦 Скорректировать циклы светофоров на загруженных направлениях")
        actions.append("📱 Направить push-уведомление о пробках пользователям городского приложения")

    if m["air_quality_index"] >= THRESHOLDS["aqi"]["hazardous"]:
        actions.append("⚠️ Объявить экологическое предупреждение — ограничить въезд грузового транспорта")
        actions.append("🏭 Проверить промышленные объекты на соответствие нормам выбросов")
        actions.append("🏥 Уведомить медицинские учреждения о возможном росте обращений")
    elif m["air_quality_index"] >= THRESHOLDS["aqi"]["unhealthy"]:
        actions.append("🚗 Ввести временные ограничения на въезд автомобилей Евро-3 и ниже")
        actions.append("🌿 Усилить увлажнение воздуха в парковых зонах")

    if m["noise_level"] >= THRESHOLDS["noise"]["critical"]:
        actions.append("🔇 Направить патрули для выявления источников сверхнормативного шума")
        actions.append("📋 Инициировать проверку строительных объектов в зоне превышения")
    elif m["noise_level"] >= THRESHOLDS["noise"]["high"]:
        actions.append("🔇 Усилить мониторинг шумовых источников в проблемных районах")

    if m["pedestrian_flow"] >= THRESHOLDS["pedestrian"]["high"]:
        actions.append("👮 Выставить регулировщиков на перегруженных пешеходных переходах")
        actions.append("🚧 Организовать временное расширение пешеходных зон")

    if m["active_incidents"] >= THRESHOLDS["incidents"]["high"]:
        actions.append("🚨 Направить экстренные службы на место инцидента")
        actions.append("📡 Активировать протокол управления трафиком вокруг зоны ЧП")

    if not actions:
        actions.append("✅ Текущая ситуация стабильна — плановый мониторинг")

    return actions


def compute_composite_score(m: dict) -> float:
    """Агрегированный score риска: 0–500."""
    score = (
        m["traffic_index"] * WEIGHTS["traffic"]
        + m["air_quality_index"] * WEIGHTS["aqi"]
        + m["noise_level"] * WEIGHTS["noise"]
        + m["pedestrian_flow"] * WEIGHTS["pedestrian"]
        + m["active_incidents"] * WEIGHTS["incidents"]
    )
    return round(min(score, 500), 1)


def compute_health_score(composite: float) -> int:
    """City Health Score: 100 = идеально, 0 = катастрофа."""
    health = 100 - (composite / 500) * 100
    return max(0, min(100, round(health)))


def determine_level(composite: float, incidents: int) -> tuple[str, str]:
    """Определяет уровень тревоги по composite_score и инцидентам."""
    if composite >= 300 or incidents >= 3:
        return "CRITICAL", "Критический"
    elif composite >= 180 or incidents >= 1:
        return "HIGH", "Высокий"
    elif composite >= 120:
        return "MEDIUM", "Средний"
    else:
        return "LOW", "Низкий"


def build_causal_link(m: dict, problems: list) -> str:
    """Описывает взаимосвязь проблем, если их несколько."""
    active_issues = [p for p in problems if "норме" not in p]
    if len(active_issues) < 2:
        return None

    if m["traffic_index"] >= 70 and m["air_quality_index"] >= 120:
        return (
            "Высокий трафик напрямую ухудшает качество воздуха: "
            "каждые 10 единиц traffic_index добавляют ~8–12 единиц AQI. "
            "Снижение автомобильного потока даст двойной эффект."
        )
    if m["noise_level"] >= 70 and m["pedestrian_flow"] >= 600:
        return (
            "Высокий пешеходный поток коррелирует с ростом шума: "
            "скопление людей и транспорта создаёт самоусиливающийся шумовой фон."
        )
    if m["active_incidents"] >= 1 and m["traffic_index"] >= 70:
        return (
            "Активный инцидент блокирует полосы движения, "
            "что мультиплицирует затор — устранение ЧП снизит traffic_index на ~15–25 единиц."
        )

    return f"Обнаружено {len(active_issues)} взаимосвязанных проблемы — комплексное воздействие усиливает риски."


def apply_simulation(metrics: dict, simulation: str) -> dict:
    """Применяет эффект симуляции к метрикам."""
    m = metrics.copy()
    effects = SIMULATION_EFFECTS.get(simulation, {})
    field_map = {
        "traffic_index": "traffic_index",
        "air_quality_index": "air_quality_index",
        "noise_level": "noise_level",
        "pedestrian_flow": "pedestrian_flow",
        "active_incidents": "active_incidents",
    }
    for key, delta in effects.items():
        if key in field_map:
            m[key] = max(0, m.get(key, 0) + delta)
    return m


# ─────────────────────────────────────────────
# ГЛАВНАЯ ФУНКЦИЯ АНАЛИЗА
# ─────────────────────────────────────────────
def analyze(raw_metrics: dict) -> dict:
    """Принимает сырые метрики, возвращает JSON-инсайт."""
    simulation = raw_metrics.pop("simulation", None)
    is_simulation = simulation is not None

    metrics = apply_simulation(raw_metrics, simulation) if is_simulation else raw_metrics.copy()

    composite = compute_composite_score(metrics)
    health = compute_health_score(composite)
    level, level_ru = determine_level(composite, metrics["active_incidents"])
    problems = detect_problems(metrics)
    actions = generate_actions(metrics, problems)
    causal = build_causal_link(metrics, problems)

    return {
        "level": level,
        "level_ru": level_ru,
        "city_health_score": health,
        "composite_score": composite,
        "problems": problems,
        "actions": actions,
        "causal_link": causal,
        "is_simulation": is_simulation,
        "simulation_type": simulation,
        "timestamp": datetime.now().isoformat(),
        "metrics_snapshot": metrics,
    }


# ─────────────────────────────────────────────
# ГЕНЕРАЦИЯ MOCK-ДАННЫХ (для demo-режима)
# ─────────────────────────────────────────────
def generate_mock_metrics() -> dict:
    """Генерирует случайные реалистичные метрики."""
    hour = datetime.now().hour
    # Ночью меньше трафика и пешеходов
    traffic_base = 20 if 0 <= hour < 6 else (80 if 7 <= hour <= 9 or 17 <= hour <= 19 else 50)
    pedestrian_base = 50 if 0 <= hour < 6 else (700 if 8 <= hour <= 20 else 150)

    return {
        "traffic_index": round(random.gauss(traffic_base, 12), 1),
        "air_quality_index": round(random.gauss(100, 35), 1),
        "noise_level": round(random.gauss(58, 10), 1),
        "pedestrian_flow": max(0, int(random.gauss(pedestrian_base, 150))),
        "active_incidents": random.choices([0, 1, 2, 3], weights=[70, 20, 7, 3])[0],
    }


# ─────────────────────────────────────────────
# ЗАГРУЗКА mock_metrics.json
# ─────────────────────────────────────────────
def load_mock_file(path: str = "mock_metrics.json") -> list[dict]:
    if not os.path.exists(path):
        print(f"[WARN] {path} не найден, используем авто-генерацию метрик")
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ─────────────────────────────────────────────
# ОСНОВНОЙ ЦИКЛ
# ─────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  CityMind AI — ML Service  |  ЗАПУЩЕН")
    print("=" * 60)

    mock_scenarios = load_mock_file()
    use_file = len(mock_scenarios) > 0
    scenario_idx = 0

    while True:
        print(f"\n{'─'*60}")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Цикл анализа")

        if use_file and scenario_idx < len(mock_scenarios):
            raw = mock_scenarios[scenario_idx].copy()
            scenario_name = raw.pop("scenario", "unknown")
            scenario_desc = raw.pop("description", "")
            print(f"📋 Сценарий: {scenario_name} — {scenario_desc}")
            scenario_idx += 1
            if scenario_idx >= len(mock_scenarios):
                print("\n[INFO] Все сценарии из файла пройдены — переходим на авто-генерацию")
                use_file = False
        else:
            raw = generate_mock_metrics()
            print("🔄 Авто-генерация метрик")

        print("\n📊 ВХОДНЫЕ МЕТРИКИ:")
        display = {k: v for k, v in raw.items() if k not in ("simulation",)}
        for k, v in display.items():
            print(f"   {k:25s} = {v}")

        insight = analyze(raw.copy())
        BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

        # В конце цикла, после вычисления insight:
        try:
            httpx.post(
                f"{BACKEND_URL}/internal/ml-insight",
                json={
                    "city": "Алматы",
                    "level": insight["level"],
                    "level_ru": insight["level_ru"],
                    "city_health_score": insight["city_health_score"],
                    "composite_score": insight["composite_score"],
                    "problems": insight["problems"],
                    "actions": insight["actions"],
                    "causal_link": insight["causal_link"],
                    "is_simulation": insight["is_simulation"],
                    "llm_text": f"{insight['level_ru']} уровень. {insight['problems'][0]}. Рекомендация: {insight['actions'][0]}",
                },
                timeout=5,
            )
            print(f"✅ Отправлено на бэк")
        except Exception as e:
            print(f"⚠ Бэк недоступен: {e}")

        print(f"\n🧠 ИНСАЙТ:")
        print(f"   Уровень:           {insight['level']} ({insight['level_ru']})")
        print(f"   Здоровье города:   {insight['city_health_score']}/100")
        print(f"   Composite score:   {insight['composite_score']}/500")
        print(f"   Симуляция:         {insight['is_simulation']}")
        if insight.get("simulation_type"):
            print(f"   Тип симуляции:     {insight['simulation_type']}")

        print(f"\n⚠️  ПРОБЛЕМЫ:")
        for p in insight["problems"]:
            print(f"   • {p}")

        print(f"\n✅ РЕКОМЕНДАЦИИ:")
        for a in insight["actions"]:
            print(f"   {a}")

        if insight["causal_link"]:
            print(f"\n🔗 ВЗАИМОСВЯЗЬ:\n   {insight['causal_link']}")

        print(f"\n📤 JSON для фронтенда:")
        # Убираем metrics_snapshot из вывода для чистоты (оставляем в реальном API)
        frontend_json = {k: v for k, v in insight.items() if k not in ("metrics_snapshot", "simulation_type", "timestamp")}
        print(json.dumps(frontend_json, ensure_ascii=False, indent=2))

        print(f"\n⏱  Следующий цикл через 3 секунды...")
        time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[СТОП] CityMind AI остановлен.")
