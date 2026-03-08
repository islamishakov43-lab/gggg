import logging
import random
import time
import sys

# Фикс для Python 3.13
if sys.version_info >= (3, 13):
    import types
    imghdr = types.ModuleType('imghdr')
    def what(*args, **kwargs):
        return None
    imghdr.what = what
    sys.modules['imghdr'] = imghdr

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = '8591103954:AAHT_7rhAtmOISrFuwtWYCDaWhnp8Vt18Mk'

PHRASES = [
    "Каждое утро я просыпаюсь и понимаю, что самый счастливый человек на Земле — это я, потому что ты есть у меня. 💗",
    "В этом огромном мире моя душа всегда находит покой только рядом с тобой. 💗",
    "ты мой сладкий медвежонок 💗",
    "мой любимый медвежонок это ты 💗",
]

def start(update, context):
    name = update.effective_user.first_name
    update.message.reply_text(f'Привет, {name}! Я бот от Савелия, напиши мне 💗')

def love(update, context):
    update.message.reply_text(random.choice(PHRASES))

def echo(update, context):
    update.message.reply_text(random.choice(PHRASES))

def main():
    try:
        print("🚀 Запуск бота...")
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("love", love))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        updater.start_polling()
        print("✅ Бот успешно запущен!")
        updater.idle()
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        time.sleep(5)
        main()

if __name__ == '__main__':
    main()
    
