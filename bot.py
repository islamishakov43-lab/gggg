import logging
import random
import time
import sys

# Костыль для Python 3.13
if sys.version_info >= (3, 13):
    import types
    # Создаем заглушку для imghdr
    imghdr = types.ModuleType('imghdr')
    def what(*args, **kwargs):
        return None
    imghdr.what = what
    sys.modules['imghdr'] = imghdr
    
    # Заглушка для шести
    import types
    six = types.ModuleType('six')
    six.moves = types.ModuleType('six.moves')
    sys.modules['six'] = six
    sys.modules['six.moves'] = six.moves

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен бота
TOKEN = '8591103954:AAHT_7rhAtmOISrFuwtWYCDaWhnp8Vt18Mk'

# Все фразы
PHRASES = [
    "Каждое утро я просыпаюсь и понимаю, что самый счастливый человек на Земле — это я, потому что ты есть у меня. 💗",
    "В этом огромном мире моя душа всегда находит покой только рядом с тобой. 💗",
    "Твоя улыбка для меня дороже всех сокровищ мира — она освещает мою жизнь. 💗",
    "Я люблю тебя не за что-то, а просто потому, что ты — это ты. 💗",
    "ты мой сладкий медвежонок 💗",
    "мой любимый медвежонок это ты 💗",
    "ты мой золотой медвежонок 💗",
    "ты моя любимая девочка 💗",
    "ты моя любимая умничка 💗",
    "ты мой самый самый лучший любимый единственный и важный для меня человек 💗"
]

def start(update, context):
    name = update.effective_user.first_name
    update.message.reply_text(f'Привет, {name}! Я бот от Савелия, напиши мне 💗')

def love(update, context):
    update.message.reply_text(random.choice(PHRASES))

def handle_message(update, context):
    update.message.reply_text(random.choice(PHRASES))

def main():
    try:
        print("🚀 Запуск бота BeerAlina...")
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("love", love))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        updater.start_polling()
        print("✅ Бот запущен!")
        updater.idle()
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        time.sleep(5)
        main()

if __name__ == '__main__':
    main()
