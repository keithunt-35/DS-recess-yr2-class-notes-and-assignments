import os
import telebot
# Initialize the bot with the API key from environment variables
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(command=['Greet'])
def greet(message):
    bot.reply_to(message, "Hello! How is it going?")

bot.polling()