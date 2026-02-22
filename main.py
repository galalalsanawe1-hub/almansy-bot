import telebot
from telebot import types

API_TOKEN = '8458264998:AAGpd2KPzzsBvOxtIpjUErgC4EYshgC09XQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="⚡ مصنع المنسي نشط الآن", callback_data="none")
    markup.add(btn)
    
    welcome_text = (
        f"⚡ **أهلاً بك في بوت المنسي لصناعة البوتات** ⚡\n\n"
        f"أرسل توكن بوتك الجديد لتفعيله فورًا."
    )
    bot.reply_to(message, welcome_text, reply_markup=markup, parse_mode="Markdown")

bot.infinity_polling()
