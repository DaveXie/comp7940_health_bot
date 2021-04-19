from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import configparser
import logging
import redis
import os
import requests

global redis1
global rapid_headers

def main():
    # Load your token and create an Updater for your Bot
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    
    global redis1
    redis1 = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']), port=(config['REDIS']['REDISPORT']))
    
    global rapid_headers
    rapid_headers = {
            'x-rapidapi-key': (config['RAPIDAPI']['APIKEY']),
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
            }
    # You can set this logging module, so you will know when and why things do not work as expected
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("hello", hello))
    dispatcher.add_handler(CommandHandler("search", searchfood))


    # To start the bot:
    updater.start_polling()
    updater.idle()


def echo(update, context):
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)

def start_handler(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = "Hi, my dear master!\n" \
                    "Send me your weight! Let me record for you!\n" \
                    "Want to search food info? /search is for you!"
    reply_keyboard_markup = ReplyKeyboardMarkup([['/search egg'],['/search tomato']])
    update.message.reply_text(welcome_message, reply_markup=reply_keyboard_markup)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Helping you helping you.')

def add(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /add is issued."""
    try: 
        global redis1
        logging.info(context.args[0])
        msg = context.args[0]   # /add keyword <-- this should store the keyword
        redis1.incr(msg)
        update.message.reply_text('You have said ' + msg +  ' for ' + redis1.get(msg).decode('UTF-8') + ' times.')
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /add <keyword>')

def hello(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /hello is issued."""
    update.message.reply_text('Good day,' + context.args[0] + '!')



url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

def searchfood(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /hello is issued."""
    global rapid_headers
    try:
        outputstr = ""
        inputstring  = context.args[0]
        querystring = {"query":inputstring}
        response = requests.request("GET", url, headers=rapid_headers, params=querystring)
        response = response.json()['items']
        if (response == []): outputstr = "Sorry, I am not sure whether "+ inputstring + " is a kind of food or not."
        else: 
            res_data = response[0]
            outputstr = inputstring + " contains " + str(res_data['sugar_g']) + "g sugar" + " and " + str(res_data['fiber_g']) + "g fiber" " as well as " + str(res_data['calories']) + " calories."

        update.message.reply_text(outputstr)
    except (IndexError, ValueError):
        update.message.reply_text("Please type something followed by search command!")


if __name__ == '__main__':
    main()