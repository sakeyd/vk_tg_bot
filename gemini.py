import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY не найден в .env")

client = genai.Client(api_key=api_key)


def parse_message(text: str) -> dict:
    prompt = f"""
Ты система распознавания команд университетского Telegram-бота.

Определи намерение пользователя.

Возможные действия:

- get_homework — узнать домашнее задание
- add_homework — добавить домашнее задание
- get_schedule — узнать расписание
- unknown — ничего из перечисленного

Верни ТОЛЬКО JSON.

Формат:
{{
    "action": "get_homework",
    "subject": "математика",
    "date": null
}}

Если предмет или дата не указаны, используй null.

Сообщение пользователя:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config={
            "temperature": 0,
            "response_mime_type": "application/json",
        },
    )

    return json.loads(response.text)