import os
import telebot

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

users = [
    {"id": 7502713731, "name": "Baluka Aibyek"},
    {"id": 135182170, "name": "Dana"},
    {"id": 988494617, "name": "alz_sana"},
    {"id": 836832942, "name": "araysn16"},
    {"id": 997621105, "name": "dayanatalgat"},
    {"id": 319296930, "name": "Aia"},
    {"id": 500280475, "name": "Dana2"},
    {"id": 614649210, "name": "eclatant_aa"},
    {"id": 491966138, "name": "nailyamussayeva"},
    {"id": 947989741, "name": "alisher"},
    {"id": 422359565, "name": "Aizhan025"},
    {"id": 328952267, "name": "tomikandre"},
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Ваш ID: {message.from_user.id}")

@bot.message_handler(commands=['tagall'])
def tag_all(message):
    print("Команда /tagall получена")
    mentions = []
    for user in users:
        mention = f"[{user['name']}](tg://user?id={user['id']})"
        mentions.append(mention)
    text = " ".join(mentions)
    bot.reply_to(message, "Привет всем!\n" + text)

while True:
    try:
        bot.polling()
    except Exception as e:
        print(f"Ошибка: {e}")
