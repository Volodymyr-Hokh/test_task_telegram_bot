import asyncio
import json

from openai import AsyncOpenAI

import config

client = AsyncOpenAI(api_key=config.OPENAI_API_KEY)

content = (
    "Тобі потрібно сформувати звіт про рівень задоволення клієнта рестораном. "
    "Звіт повинен бути написаний у форматі JSON, де ключ це назва категорії а значення - орієнтовна оцінка від 1 до 10."
    "Перелік категорій: food_quality_rate, service_rate, ambiance_rate, menu_rate, cleanliness_rate."
    "Окремим ключем необхідно вказати 'report', де значенням буде текстовий звіт українською мовою."
    "У текстовому звіті обов'язково потрібно вказати назву закладу. Обсяг звіту повинен бути у межах 3-5 речень."
    "Якщо значення певного критерію None, то клієнт в цілому задоволений та вирішив не залишати коментарі"
)


async def get_report(data: dict):
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": content},
            {"role": "user", "content": str(data)},
        ],
    )
    report = response.choices[0].message.content
    report = json.loads(report)
    return report
