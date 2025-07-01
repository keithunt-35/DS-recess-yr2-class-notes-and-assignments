import os
import telebot
from dotenv import load_dotenv
# Initialize the bot with the API key from environment variables
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hello! How is it going?")

bot.polling()