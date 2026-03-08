import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(level=logging.INFO)

TOKEN = '8591103954:AAHT_7rhAtmOISrFuwtYCDaWhnp8Vt18Mk'

PHRASES = [
    "Каждое утро я просыпаюсь и понимаю, что самый счастливый человек на Земле — это я, потому что ты есть у меня. 💗",
    "В этом огромном мире моя душа всегда находит покой только рядом с тобой. 💗",
    "ты мой сладкий медвежонок 💗",
    "мой любимый медвежонок это ты 💗",
]

def start(update: Update, context: CallbackContext):
    name = update.effective_user.first_name
    update.message.reply_text(f'Привет, {name}! Я бот от Савелия, напиши мне 💗')

def love(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(PHRASES))

def handle_message(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(PHRASES))

def main():
    print("🚀 Запуск бота...")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("love", love))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    print("✅ Бот успешно запущен!")
    updater.idle()

if __name__ == '__main__':
    main()
