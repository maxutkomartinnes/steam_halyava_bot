from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# Вставь токен от BotFather
TOKEN = "7777623230:AAH1BqO4q6fPfPzPSd9-RcZOu1oUVsrVvbg"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Напиши /free — покажу текущие раздачи игр.")

def get_free_games():
    url = "https://www.freegamer.xyz/api/"
    response = requests.get(url)
    data = response.json()
    result = []

    for item in data:
        title = item['title']
        link = item['link']
        store = item['platform']
        result.append(f"{title} ({store})\n{link}")

    return "\n\n".join(result[:5])  # показываем 5 раздач

def free(update: Update, context: CallbackContext):
    update.message.reply_text("Ищу халяву...")
    try:
        games = get_free_games()
        update.message.reply_text(games)
    except Exception as e:
        update.message.reply_text(f"Ошибка: {e}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("free", free))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
