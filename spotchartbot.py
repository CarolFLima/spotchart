from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

token_file = open("token.txt","r")
token = token_file.read()

updater = Updater(token=token, use_context=True)

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

    client_credentials_manager = SpotifyClientCredentials(client_id='ac', client_secret='secret')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    scope = 'user-library-read'
    token = util.prompt_for_user_token('carolinelima0', scope)

    results = sp.current_user_top_tracks(time_range='short_term', limit=10)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])

    # playlists = sp.user_playlists('manutunan')
    # while playlists:
    #     for i, playlist in enumerate(playlists['items']):
    #         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
    #     if playlists['next']:
    #         playlists = sp.next(playlists)
    #     else:
    #         playlists = None


