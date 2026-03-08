import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = '8591103954:AAECK7gVJBxVumhkiRJCNjGg38cFj-SYXyI'

LOVE_PHRASES = [
    "Каждое утро я просыпаюсь и понимаю, что самый счастливый человек на Земле — это я, потому что ты есть у меня. 💗",
    "В этом огромном мире моя душа всегда находит покой только рядом с тобой. 💗",
    "Твоя улыбка для меня дороже всех сокровищ мира — она освещает мою жизнь. 💗",
    "Я люблю тебя не за что-то, а просто потому, что ты — это ты. 💗",
    "ты мой сладкий медвежонок 💗",
    "мой любимый медвежонок это ты 💗",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(f'Привет, {name}! Я бот от Савелия, напиши мне 💗')

async def love_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(LOVE_PHRASES))

async def bear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bear = ["ты мой сладкий медвежонок 💗", "мой любимый медвежонок это ты 💗", "ты мой золотой медвежонок 💗"]
    await update.message.reply_text(random.choice(bear))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if 'люблю' in text:
        await update.message.reply_text(random.choice(LOVE_PHRASES))
    elif 'медвежонок' in text:
        bear = ["ты мой сладкий медвежонок 💗", "мой любимый медвежонок это ты 💗"]
        await update.message.reply_text(random.choice(bear))
    else:
        await update.message.reply_text(random.choice(LOVE_PHRASES))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("love", love_command))
    app.add_handler(CommandHandler("bear", bear_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен!")
    app.run_polling()

if __name__ == '__main__':
    main()
  
