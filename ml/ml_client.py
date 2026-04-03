import httpx
import time
import json
import ollama

BACKEND = "http://localhost:8000"

def ask_llm(metrics: dict) -> str:
    prompt = f"""Ты — аналитик умного города. Отвечай ТОЛЬКО на русском, максимум 2-3 предложения.

Текущие метрики города:
- Трафик: {metrics['traffic_index']}/100 {'⚠️ высокий' if metrics['traffic_index'] > 75 else '✅ норма'}
- AQI воздух: {metrics['air_quality_index']}/300 {'⚠️ плохой' if metrics['air_quality_index'] > 100 else '✅ норма'}
- Шум: {metrics['noise_level']} дБ {'⚠️ громко' if metrics['noise_level'] > 65 else '✅ норма'}
- Пешеходы: {metrics['pedestrian_flow']} чел/час
- Инциденты: {metrics['active_incidents']} {'⚠️ есть!' if metrics['active_incidents'] > 0 else '✅ нет'}

Опиши ТОЛЬКО реальные проблемы из метрик выше и дай конкретные действия для управленцев."""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

while True:
    try:
        # 1. Получаем метрики с бэкенда
        r = httpx.get(f"{BACKEND}/internal/current-metrics")
        data = r.json()
        metrics = data["metrics"]

        print(f"📊 Метрики получены: {metrics}")

        # 2. Отправляем в настоящий LLM
        print("🤖 Думает Llama3...")
        text = ask_llm(metrics)
        print(f"💬 Ответ AI: {text}")

        # 3. Отправляем обратно на бэкенд
        httpx.post(
            f"{BACKEND}/internal/llm-insight",
            json={"text": text}
        )
        print("✅ Отправлено на бэкенд!")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

    time.sleep(5)