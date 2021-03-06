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
 
    #formal version 
    updater = Updater(token=(os.environ['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    
    global redis1
    redis1 = redis.Redis(host=(os.environ['HOST']), password=(os.environ['PASSWORD']), port=(os.environ['REDISPORT']))
    
    global rapid_headers
    rapid_headers = {
            'x-rapidapi-key': (os.environ['APIKEY']),
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
            }
    #/formal version 
    
    #local debug
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    # dispatcher = updater.dispatcher

    # global redis1
    # redis1 = redis.Redis(host=(config['REDIS']['HOST']), password=(config['REDIS']['PASSWORD']), port=(config['REDIS']['REDISPORT']))

    # global rapid_headers
    # rapid_headers = {
            # 'x-rapidapi-key': (config['RAPIDAPI']['APIKEY']),
            # 'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
            # }
    #/local debug
    
    # You can set this logging module, so you will know when and why things do not work as expected
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    # register a dispatcher to handle message: here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_handler))

    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler("search", searchfood))


    # To start the bot:
    updater.start_polling()
    updater.idle()

# weight recording
def echo(update, context):
    global redis1
    if update.message.text.isdigit():    
        user_id = update.message.from_user.id
        weight_pre = int(redis1.get(user_id).decode("UTF-8"))
        weight = int(update.message.text)
        
        def compare(weight_pre, weight):
            compare_num = 0
            compare_str = ""
            if weight_pre == 0:                     #weight_pre==0?
                return compare_str                  #exit the function if weight_pre==0, which makes compare_str == ""
            if weight_pre > weight:                 #do something if weight_pre!=0, comfirm the content of compare_str
                compare_num = weight_pre - weight
                compare_str = "You have lost "+ str(compare_num) +" kilos in weight!"
            elif weight_pre < weight:
                compare_num = weight - weight_pre
                compare_str = "You have gained "+ str(compare_num) +" kilos in weight!"
            else:
                compare_str = "Your weight hasn't changed!"
            return compare_str

        compare_weight = ""
        compare_weight = compare(weight_pre, weight)
    
        if compare_weight == "":                                                                                #compare_str == "" --> weight_pre==0
            reply_message = "OK! Your weight is " + str(weight) + " kilos. It has been recorded."
        else:                                                                                                   #works if weight_pre==0
            reply_message = "Your previous weight is " + str(weight_pre) + " kilos. Now your weight is " + str(weight)+" kilos. " + compare_weight
        redis1.set(user_id, weight)
    else:
        reply_message = "Please input digit without any letters/spaces/symbols."    
    logging.info("Update: " + str(update))
    logging.info("context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text= reply_message)

# /start and the beginning of the bot 
def start_handler(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    global redis1
    user_id = update.message.from_user.id
    redis1.set(user_id, 0)

    welcome_message = "Hi, my dear master!\n" \
                    "I can record your weight for you!\n" \
                    "Just send me your weight(in kilos) here!\n" \
                    "Also want to search food info? /search is for you!"
    reply_keyboard_markup = ReplyKeyboardMarkup([['/search egg'],['/search tomato']])
    update.message.reply_text(welcome_message, reply_markup=reply_keyboard_markup)


# help command
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    help_message = "I can handle these commands\n" \
                    "number\n" \
                    "/search\n" \
                    "/help\n" \
                    "/start(once you use this function, Your data will be initialized, use it carefully!!!)"
    update.message.reply_text(help_message)


url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"

# search food
def searchfood(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /search is issued."""
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