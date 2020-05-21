from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

token_file = open("token.txt","r")
token_telegram = token_file.read()

updater = Updater(token=token_telegram, use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def caps(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="CAPS")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Message Received")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

if __name__ == '__main__':
    # updater.start_polling()
    username = '12179705535'
    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            print(playlist['name'])
    else:
        print("Can't get token for", username)


