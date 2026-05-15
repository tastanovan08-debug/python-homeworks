import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = ""
GROQ_API_KEY = ""

logging.basicConfig(level=logging.INFO)


def получить_мотивацию(настроение, цель, ситуация):
    prompt = f"""
Ты мотивационный AI помощник.

Пользователь:
Настроение: {настроение}
Цель: {цель}
Ситуация: {ситуация}

Сгенерируй ответ на русском языке в формате:
1. Короткая мотивация
2. Совет
3. Одно простое действие
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]


async def старт(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Отправь данные в формате:\nнастроение, цель, ситуация\n\nПример:\nустал, учёба, экзамены"
    )


async def обработка(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        настроение, цель, ситуация = [x.strip() for x in update.message.text.split(",")]
        результат = получить_мотивацию(настроение, цель, ситуация)
    except:
        результат = "Ошибка формата. Используй: настроение, цель, ситуация"

    await update.message.reply_text(результат)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", старт))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, обработка))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()