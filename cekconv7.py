from telethon.sync import TelegramClient, events
import asyncio
import winsound  # Untuk memainkan suara alarm di Windows
from telethon.tl.types import PeerChat, PeerChannel, InputPeerChat
import requests
import json
import asyncio
import datetime
import time
import re
from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto
from telethon import TelegramClient, events, sync, tl
import telethon
from telethon.errors import AuthKeyUnregisteredError
from telethon.errors import PersistentTimestampOutdatedError
import os
from telethon.tl.types import InputPeerChannel
import asyncio
import aiohttp
from telethon.tl.types import InputPeerChannel, InputPeerUser
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from datetime import datetime, timedelta, timezone
import traceback
import statistics
from collections import Counter
from collections import Counter, defaultdict


# Ganti dengan informasi Anda sendiri
#api_id = '20623228'
#api_hash = '98017a0e6daf0198a836d5cbcd2d9b96'


fifo_queue = deque()
expired_fifo_queue = deque()

api_id = '14167964'
api_hash = '371a87545c9a82871e7daf51437883f8'
out1 = ""
out2 = ""

# Inisiasi penerima
user_id = 4151033946

userId_McapBot = "@ttfbotbot"
userId_TgBot = "@RickBurpBot"
userId_Prio2 = "@paris_trojanbot"
session_name = 'session_name'
user_tesrick = 2228414903
user_check_x = 2198583984
user_news = 2087255766
user_news_p0 = 4266297407
trend_list = 4239753664
Dj_channel= 2015507752
P00_alert = 4266098748
plonk_bot = 2193363840

# Inisialisasi klien Telegram
client = TelegramClient(session_name, api_id, api_hash)
banned = ["Red Bean", "cats" , "**Simon's Cat" , "BLUE" , "LEAF", "HUNGRY" , "FRIED" , "DAWG", "SWAG", "DARK", "HUNGRY", "SWAG", "DEVIL", "CHlKO", "PANFLlP", "MUSHl", "EVlLDOGE", "SNlFFY", "PlNDA", "ROARKlT", "SNlFFY", "WISH"]
#Tools and Forward messages ================================================================================================================================================
banned_wallet = ["35fzgfD4vS8fWt2yRDrT1aG9Z3otWRE53hyESFFzAijY", "4wd6tHctTEiYuoLLn6mi7T9gXd9RT58w2q5jXZG2FN51", "ewGF1MtkaewDHDQSLnmLyLViJzHisSgTxHv7s1tcvbo" ,"FtLF1iFw6qxnWwBqudV8NdZuURtb79PL8wGZim2CuLzs","GYmzLDuN5MM96tosXhGjcVyX15K78xF19SYnuA3ChYkS", "Fu3cbX91uGFLdm78HZf3SJdkKsPEUwwDmbCCfTEtqote", "4scDibb8LPqDNchtKqoMJRjgZC9x7z7gEiw57KkK81ek" , "ewGF1MtkaewDHDQSLnmLyLViJzHisSgTxHv7s1tcvbo" , "225DbTXRw5JYxyMjNkoddoJpoeQFvdF92fn4Dqas8UNV" , "DeVNNc2cVbx6zx4eqosciA5nuf2wWejtFFrVzWuwNtoU", "GYRMdZrdxgarYpYbA7q5dk24UXGW99Wi8X6NrD3X7Cua", "7ZPFGD1QfghJjCG5AbM9Gkve1HsFdZAqKTCL4ZFV2LMT", "5KHqy5JRp6Bz6SVQJZdxr1yHQDWHsm6Z1xSWs6cJjCcC", "9xq4YuWc21i7pCgPpapfrBp3m1dtSHVgpguctnpus8rd" , "9Gmc5BeP5vsqMeXMWn3VCmxAN8SxNnzEsJaPEuyYNaYW" , "9VpdeDf4krozG4StFX98AezKZqmDEgABiCsjs3JChvVD", "3FnV7DWZCmN9a4caZUyxxkKm5vwRTQgbZEjWa3DLiAqD", "HGUNQ2YC47HDUwv3TQJCNT3sSy5PvAc1HsuvJELueno6", "HGUNQ2YC47HDUwv3TQJCNT3sSy5PvAc1HsuvJELueno6","DVKKYe2dBRUKE2BN3Km8EQVug5mEV3en7LgNxxVqRhv9", "FtLF1iFw6qxnWwBqudV8NdZuURtb79PL8wGZim2CuLzs" ,"7xZYqDB5osFNB1DRgnZtV9ue1bn3AFeDedgWR7hJ7c5u", "87fkEVZXdN1BEhQRwXpdxiBANRJyWR7QX5Q5hprrUeVt"]

async def add_to_queue(queue, code):
    timestamp = datetime.now().isoformat()
    queue.append((code, timestamp))

# Fungsi untuk memainkan suara alarm
def play_alarm():
    frequency = 2500  # Frekuensi suara
    duration = 10000  # Durasi suara dalam milidetik (1 detik)
    winsound.Beep(frequency, duration)

async def play_alarm_async():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, play_alarm)

async def forward_msg(message, file=None):
    receiver = InputPeerChat(user_id)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_alert(message, file=None):
    receiver = InputPeerChat(P00_alert)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_trojan(message, file=None):
    receiver = userId_Prio2
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_mcap_bot(message, file=None):
    receiver = userId_McapBot
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_msg_tw_bot(message, media):
    receiver = userId_TgBot
    if isinstance(media, telethon.tl.types.MessageMediaDocument) or isinstance(media, telethon.tl.types.MessageMediaPhoto):
        file = media.document if isinstance(media, telethon.tl.types.MessageMediaDocument) else media.photo
        await client.send_message(receiver, message, file=file, parse_mode='html')
    else:
        await client.send_message(receiver, message, parse_mode='html')

async def forward_rick_bot(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    entity = await client.get_entity(4232182480)
    
    entity = await client.get_input_entity(user_tesrick)
    
    # Sending the message to the channel or user
    await client.send_message(entity, message, file=file, parse_mode='html')

async def forward_news(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    channel = await client.get_entity(user_news)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)
    
    # Sending the message to the channel
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_check_x(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    channel = await client.get_entity(user_check_x)
    
    # Creating an InputPeerChannel object
    receiver = InputPeerChannel(channel_id=channel.id, access_hash=channel.access_hash)
    
    # Sending the message to the channel
    await client.send_message(receiver, message, file=file, parse_mode='html')


async def forward_news_p0(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    receiver = InputPeerChat(user_news_p0)
    await client.send_message(receiver, message, file=file, parse_mode='html')

async def forward_trend(message, file=None):
    # Replace 'channel_username_or_id' with the actual username or ID of the channel
    receiver = InputPeerChat(trend_list)
    await client.send_message(receiver, message, file=file, parse_mode='html')
#Tools and Forward messages ================================================================================================================================================


# News P0 ===========================================================================================================================
@client.on(events.NewMessage(chats=["@dbnewsdelayed"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorA: {e}")

# News P0
@client.on(events.NewMessage(chats=["@news_crypto"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorGG: {e}")

@client.on(events.NewMessage(chats=["@WatcherGuru"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorB: {e}")

# News P0
@client.on(events.NewMessage(chats=["@walter_bloomberg"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        if "SHARES" in event.message.text:
            await forward_msg(event.message.text+"  #P0")
        #print(event.message.text)
        await forward_news_p0(event.message.text+"  #P0")
    except Exception as e:
        print(f"ErrorC: {e}")

# News P0
@client.on(events.NewMessage(chats=["@BWEnews"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorD: {e}")

# News P0
@client.on(events.NewMessage(chats=["@Tree_Alpha_News"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorE: {e}")

@client.on(events.NewMessage(chats=["@TwttrToTG_TweetBot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text , event.message.media)
    except Exception as e:
        print(f"ErrorF: {e}")

# P0 news ==================================================================================================================================


# cexalert binance bybit ===================================================================================================================
@client.on(events.NewMessage(chats=["@CexAlerts"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print(event.message.text)
        if "Binance" in event.message.text or "ByBit" in event.message.text or "Bybit" in event.message.text:
            print("String mengandung kata 'Binance'")
            await forward_news_p0(event.message.text , event.message.media)
        else:
            print("String tidak mengandung kata 'Binance'")
    except Exception as e:
        print(f"ErrorG: {e}")
# cexalert binance bybit ===================================================================================================================


# sinyal liquidity =========================================================================================================================
@client.on(events.NewMessage(chats=["@ttfbotbot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        # Mencari kecocokan dengan ekspresi reguler
        print("New message received:")
        print(event.message.text)
        match_mcap = re.search(r"Launch MC:\*\* \$([\d\.,M,K]+)", event.message.text)
        if match_mcap and "VERY LOW LIQUIDITY" not in event.message.text and "Freezable" not in event.message.text:
            number_string = match_mcap.group(1)

            # Konversi simbol M ke angka
            number_string = number_string.replace("M", "e6")

            # Konversi simbol K ke angka
            number_string = number_string.replace("K", "e3")

            # Konversi string ke float
            number = float(number_string)
            print(number)
            if number > 200000:
                print(event.message.text)
                await forward_msg(event.message.text)
    except Exception as e:
        print(f"ErrorH: {e}")

# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=["@tbtokenbot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    #print("New message received:")

    ''''pattern_x = r"token/([^?]+)\?"
    match_x = re.search(pattern_x, event.message.text)
    if match_x:
        await add_to_queue(fifo_queue, match_x.group(1))
        print("Kode dan timestamp ditambahkan ke antrian:", fifo_queue)'''

    pattern1 = r"Liquidity:\s+(\d+(,\d{3})*(\.\d+)?)"
    # Mencari kecocokan dengan ekspresi reguler
    match_liquidity = re.search(pattern1, event.message.text)

    # Jika kecocokan ditemukan, ekstrak angkanya
    if match_liquidity:
        liquidity_amount = float(match_liquidity.group(1).replace(",", ""))
        #print("Nilai Liquidity:", liquidity_amount)
    
    pattern2 = r"Volume 24h:\s+(\d+(,\d{3})*(\.\d+)?)"
    # Mencari kecocokan dengan ekspresi reguler
    match_volume = re.search(pattern2, event.message.text)

    # Jika kecocokan ditemukan, ekstrak angkanya
    if match_volume:
        volume_amount = float(match_volume.group(1).replace(",", ""))
        #print("Nilai Volume:", volume_amount)
    
    pattern = r"\+(\d+(\.\d+)?)%"

    # Mencari kecocokan dengan ekspresi reguler
    match_percentage = re.search(pattern, event.message.text)

    # Jika kecocokan ditemukan, ekstrak angkanya
    if match_percentage:
        percentage_change = float(match_percentage.group(1))
        #print("Persentase Perubahan:", percentage_change)

    if match_volume and match_liquidity:
        if liquidity_amount > 100000 and volume_amount > 100000:
            print(event.message.text)
            print("Nilai Volume:", volume_amount)
            print("Nilai Liquidity:", liquidity_amount)
            await forward_msg_mcap_bot(event.message.text+"  #sinyalSOLANA", event.message.media)
    elif match_volume:
        if volume_amount > 500000:
            print(event.message.text)
            print("Volume Perubahan:", volume_amount)
            await forward_msg(event.message.text+"  #sinyalSOLANA", event.message.media)
    elif match_percentage:
        if percentage_change > 200:
            print(event.message.text)
            print("Persentase Perubahan:", percentage_change)
            await forward_msg(event.message.text+"  #sinyalSOLANA", event.message.media)
# sinyal liquidity =========================================================================================================================


# sinyal dj ===================================================================================================================
async def detect_and_join_token_address(text):
    # Mencari token address yang memiliki spasi sebelum "pump" dan mengabaikan kata lain
    pattern = re.compile(r'([a-zA-Z0-9]+)\s+pump')
    matches = pattern.findall(text)
    
    joined_addresses = []
    for match in matches:
        # Menggabungkan token address dengan "pump"
        joined_address = f"{match}pump"
        # Mengecek apakah panjang token address lebih dari 15 karakter
        if len(joined_address) > 15:
            joined_addresses.append(joined_address)
    
    return joined_addresses

temp_dj_call = ""

@client.on(events.NewMessage(chats=["@djenbullz"]))  # DJ bulls
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        await forward_msg_tw_bot(event.message.text+"  #sinyallDJJJJ", event.message.media)
        if "pump" in event.message.text or "0x" in event.message.text or "Bought" in event.message.text or  "aped" in event.message.text or "degen" in event.message.text or "Degen" in event.message.text or "Play" in event.message.text or "play" in event.message.text or "plays" in event.message.text or "Plays" in event.message.text:
            await forward_msg(event.message.text+"  #sinyallDJJJJ", event.message.media)
        result = await detect_and_join_token_address(event.message.text)
        if len(result) > 0:
            await forward_msg_trojan(str(result))
            await forward_msg_tw_bot(event.message.text+"  #sinyallDJJJJ Auto Buy", event.message.media)
            await forward_msg(str(result))

    except Exception as e:
        print(f"ErrorI: {e}")


@client.on(events.NewMessage(chats=["@ray_silver_bot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd:")
        print(temp_dj_call)
        match_ca = re.search(r'`([A-Za-z0-9]+)`\s*$', event.message.text)

        if match_ca:
            dex_url = match_ca.group(1)
            #print("New message werfwereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: "+str(dex_url))
                        
        if "DjDegen" in event.message.text and  ("SELL" in event.message.text or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #DJDegen", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("dj02" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text  or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #dj02", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("DjMain" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text  or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #djMain", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("dj01" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text  or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #dj01", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("djav" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text  or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted01", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("dev01" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text  or "SWAP" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted2", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("luca1" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted2", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("luca2" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted2", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("luca3" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted2", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("luca4" in event.message.text) and ("BUY" in event.message.text or "SELL" in event.message.text) and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #trusted2", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif "BUY" in event.message.text and "DjDegen" in event.message.text and "BUY" in event.message.text and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            patter_cad = r"\(MC: \$(\d+(\.\d+)?[KM]?)\)"
            matches_cad = re.findall(patter_cad, event.message.text)
            if matches_cad:
                last_match = matches_cad[-1][0]
                print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd: "+str(matches_cad))
                print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd: "+str(last_match))
                if last_match[-1].upper() == 'K':
                    mc_buy= float(last_match[:-1]) * 1_000
                elif last_match[-1].upper() == 'M':
                    mc_buy= float(last_match[:-1]) * 1_000_000
                else:
                    mc_buy= float(last_match)
                
                dex_url=""
                if match_ca:
                    dex_url = match_ca.group(1)
                if mc_buy <= 30000:
                    await forward_msg_trojan(dex_url)
                if mc_buy <= 30000:
                    print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd: "+str(mc_buy))
                    await forward_msg(event.message.text+"  #DjDegen Autobuy!!!!!!!!!!!", event.message.media)
                    await forward_msg(dex_url+ " Autobuy!!!!!!!!!!!")
                else:
                    print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd: "+str(mc_buy))
                    await forward_msg(event.message.text+"  #DjDegen NOBUY", event.message.media)
                    await forward_msg(dex_url+" Nobuy")
        if match_ca:
            dex_url = match_ca.group(1)             
            url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/'+dex_url
            headers_dexscreener = {
                'Cookie': '_ga_CFY1SSGE2N=GS1.1.1720353864.2.0.1720353864.0.0.0; _gid=GA1.2.1007166714.1722067188; _ga=GA1.1.1571615799.1702193879; cf_clearance=DAX6hNUR1EXDn1Y4BqSYUSqMtlWAzElF09z8My0I770-1722087608-1.0.1.1-HJnclhkye5z1u0TFwLJOOgPezl7KUDrAzwAMQwdk_FuE2r5Zk3YYlOJr2O491iYghjfQKj3eQxZGqBDgFK.j9g; _ga_532KFVB4WT=GS1.1.1722083517.783.1.1722096796.60.0.0; __cf_bm=IoQrPu9umlNj.l8JPtdrqQjcip9xaJztsaH2KdLYVTk-1722098687-1.0.1.1-q6N_SegQhyqMYGtBuQnUzReU4LQGQyrepoUEOHwREqyAesZeIhF2z_pMSRRXsuwOPcZcxgKOoObif1vVNmrRrEex0dU6uSQ04fT0PQd5ulQ; _ga_RD6VMQDXZ6=GS1.1.1722100207.25.0.1722100207.0.0.0'
                
            }
            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

            if 'error' in dexscreener_data:
                print("ASSSSSOOOOOy")
                print(dexscreener_data['error'])
            pairs = dexscreener_data.get('pairs', None)

            if pairs:
                for pair in dexscreener_data["pairs"]:
                    token_temp = pair.get('baseToken', {}).get('address', None)
                    if pair["dexId"] == "raydium":
                        socials = pair.get('info', {}).get('socials', [])
                        twitter_url = None
                        telegram_url = None
                        for social in socials:
                            if social.get('type') == 'twitter':
                                twitter_url = str(social.get('url'))
                            elif social.get('type') == 'telegram':
                                telegram_url = str(social.get('url'))
                        if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                            if telegram_url:
                                group_link = telegram_url
                            await forward_msg("https://dexscreener.com/solana/"+token_temp+" #DJCTOTOKENNNN"+str(twitter_url)+" "+str(telegram_url)+ "  Members_TG:")
    except Exception as e:
        print(f"ErrorJ: {e}")

# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=["@RickBurpBot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received: wokwokwokwokwokwokwokwokowk")
        if any(keyword in event.message.text for keyword in ["SPEED","AMC","$ROGER","$NAMI","DJCAT", "SELFIE", "TABBY","DUK","DRIFTY","$W","$MINI","$GOMU","$GIKO","PEANIE","$MUZKI","$CGW","$WIWI","$MIJI","$DISKNEE","$SC","$MICHI","$MOG","$GME","$KAMA","$NUT","PIXI","$BUCK","$NUB","$ANAL","$NOK","$𝕏","$CEICAT","$BB*","$VCAT","ROAR"]):
            print("New message received: gygyygygygygygyggygygygygy")
        else:
            #print(event.message.text)   
            # temp_dj_call             
            await forward_msg(event.message.text+"  #sinyallDJJJJ", event.message.media)
            #await forward_msg(temp_dj_call+" #sinyallDJJJJ")
            #await forward_msg_trojan(event.message.text+"  #sinyallDJJJJ", event.message.media)
    except Exception as e:
        print(f"ErrorK: {e}")
# sinyal dj ===================================================================================================================

# sinyal prefer ==============================================================================================================
''''
@client.on(events.NewMessage(chats=["@preferrichroom"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        sender = await event.get_sender()
        sender_id = sender.id
        sender_username = sender.username
        if sender_username == "elroybandicoot" or sender_username == "elroysadrakh" or sender_username == "godstonk" or sender_username == "limehizel" or sender_username == "captainJedi" or sender_username == "vannightmare" or sender_username == "donRichX" or sender_username == "jojobmnn" or sender_username == "chenzeth" :   
            await forward_rick_bot(event.message.text+" sinyalprefer", event.message.media)
            #print(event.message.text)
            if "grup" in event.message.text or "cto" in event.message.text or "aped" in event.message.text or "play" in event.message.text or "$" in event.message.text or "chads" in event.message.text or "one" in event.message.text or "dj" in event.message.text or "Dj" in event.message.text:
                await forward_trend(event.message.text+"  #sinyalPreferGrup" + str(sender_username))
            if "buatin tg" in event.message.text or "setup tg" in event.message.text or "Buatin tg" in event.message.text:
                 await forward_msg(event.message.text+"  #sinyalCTOLuca" + str(sender_username))

    except Exception as e:
        print(f"ErrorL: {e}")
'''


username_adam=""
# Fungsi untuk menangani pesan baru
'''@client.on(events.NewMessage(chats=[PeerChannel(Dj_channel)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received: wokwokwokwokwokwokwokwokowk")
        #print(event.message.text)
        sender = await event.get_sender()
        sender_username = sender.username
        username_adam = sender_username
        if sender_username == "RickBurpBot" and username_adam == "adamdahhaan":
            await forward_msg(event.message.text+"  #sinyaladam", event.message.media)
    except Exception as e:
        print(f"ErrorM: {e}")
'''
# sinyal adam ============================================================================================================== 


# news all ============================================================================================================== 
async def fetch_news(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Request failed with status code {response.status}")
                return []
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")
        
async def send_post_request_pos(session, endpoint, title, suggestions):
    coin=""
    for suggestion in suggestions:
        coin = suggestion.get('coin')
        if coin:
            a=""
        else:
            coin = ""
    payload = {
        "model": "llama3",
        "prompt": f"{title} , do you think the News will have a very huge positive price impact on the its {coin} crypto market? , please answer just with one word either Yes or No !",
        "stream": False
    }
    try:
        async with session.post(endpoint, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                response_text = response_data.get('response', 'No response field found')
                print(f"Response from POST request POS: {response_text}")
                if response_text == "Yes":
                    print(f"Title: {title}")
                    print(f"Coin: {coin}")
                    await forward_news(title+" "+"Coin: "+coin+" POS")
            else:
                print(f"Failed to send POST request for title: {title} with status code {response.status}")
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")

async def send_post_request_neg(session, endpoint, title, suggestions):
    coin=""
    for suggestion in suggestions:
        coin = suggestion.get('coin')
        if coin:
            a=""
        else:
            coin = ""
    payload = {
        "model": "llama3",
        "prompt": f"{title} , do you think the News will have a very huge negative price impact on the its {coin} crypto market? , please answer just with one word either Yes or No !",
        "stream": False
    }
    try:
        async with session.post(endpoint, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                response_text = response_data.get('response', 'No response field found')
                #print(f"Response from POST request NEG: {response_text}")
                if response_text == "Yes":
                    #print(f"Title: {title}")
                    #print(f"Coin: {coin}")
                    await forward_news(title+" "+"Coin: "+coin+" NEG")
            else:
                print(f"Failed to send POST request for title: {title} with status code {response.status}")
    except aiohttp.ClientOSError as e:
        print(f"ClientOSError: {e}")
    except asyncio.TimeoutError:
        print("Request timeout")

async def fetch_and_post_news():
    fetch_url = "https://news.treeofalpha.com/api/news?limit=10"
    post_endpoint = "http://localhost:11434/api/generate"
    previous_ids = set()

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                data = await fetch_news(session, fetch_url)
                if data is not None and len(data) > 0:
                    current_ids = {item['_id'] for item in data}

                    # Find new ids by subtracting previous_ids from current_ids

                    for item in data:
                        if item['_id'] not in previous_ids:
                            await send_post_request_pos(session, post_endpoint, item['title'], item.get('suggestions', []))
                            await send_post_request_neg(session, post_endpoint, item['title'], item.get('suggestions', []))

                    # Update previous_ids
                    previous_ids = current_ids

                    # Sleep for 1 second before the next request
                    await asyncio.sleep(15)
            except Exception as e:
                print(f"ErrorN: {e}")
# news all ============================================================================================================== 


# ricky 5 menit awal ============================================================================================================== 
def datetime_converter(o):
    if isinstance(o, datetime):
        return o.__str__()
    
async def chek_ten_minutes():
    while True:
        await asyncio.sleep(30)
        try:
            params_bulk1 = []
            params_bulktemp= ""
            count = 0
            count_t = 0
            for token in list(high_count_tokens.keys()):
                if (time.time() - high_count_tokens[token]['createdDelta']) <= 1200 and token not in high_count_tokens_correction:
                    count += 1
                    if count <= 7:
                        params_bulktemp += token+","
                        print("sdoiusidusoi")
                        print(len(high_count_tokens))
                        print(count)
                        if count == 7:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=14 :
                        params_bulktemp += token+","
                        if count == 14:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=21 :
                        params_bulktemp += token+","
                        if count == 21:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=28 :
                        params_bulktemp += token+","
                        if count == 28:
                            params_bulk1.append(params_bulktemp)
                            params_bulktemp= ""
                else:
                    count_t += 1

                if count + count_t == len(high_count_tokens.keys()) and count % 7 != 0:
                    params_bulk1.append(params_bulktemp)

            print(params_bulk1)

            for s in params_bulk1:
                if s != "":
                    url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/'+s
                    headers_dexscreener = {
                        'Cookie': '_ga_CFY1SSGE2N=GS1.1.1720353864.2.0.1720353864.0.0.0; _gid=GA1.2.1007166714.1722067188; _ga=GA1.1.1571615799.1702193879; cf_clearance=DAX6hNUR1EXDn1Y4BqSYUSqMtlWAzElF09z8My0I770-1722087608-1.0.1.1-HJnclhkye5z1u0TFwLJOOgPezl7KUDrAzwAMQwdk_FuE2r5Zk3YYlOJr2O491iYghjfQKj3eQxZGqBDgFK.j9g; _ga_532KFVB4WT=GS1.1.1722083517.783.1.1722096796.60.0.0; __cf_bm=IoQrPu9umlNj.l8JPtdrqQjcip9xaJztsaH2KdLYVTk-1722098687-1.0.1.1-q6N_SegQhyqMYGtBuQnUzReU4LQGQyrepoUEOHwREqyAesZeIhF2z_pMSRRXsuwOPcZcxgKOoObif1vVNmrRrEex0dU6uSQ04fT0PQd5ulQ; _ga_RD6VMQDXZ6=GS1.1.1722100207.25.0.1722100207.0.0.0'
                    }
                    dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                    if 'error' in dexscreener_data:
                        print("ASSSSSOOOOOy")
                        print(dexscreener_data['error'])
                    pairs = dexscreener_data.get('pairs', None)

                    if pairs:
                        for pair in dexscreener_data["pairs"]:
                            token_temp = pair.get('baseToken', {}).get('address', None)
                            if token_temp not in high_count_tokens_correction and pair["dexId"] == "raydium":
                                fdv_temp = 0
                                liq_temp = 0
                                if 'fdv' in pair:
                                    fdv_temp = pair["fdv"]
                                if 'liquidity' in pair:
                                    liq_temp = pair["liquidity"]["usd"]
                                websites = pair.get('info', {}).get('websites', [])
                                website_url = websites[0].get('url', None) if websites else None

                                socials = pair.get('info', {}).get('socials', [])
                                twitter_url = None
                                telegram_url = None

                                for social in socials:
                                    if social.get('type') == 'twitter':
                                        twitter_url = str(social.get('url'))
                                    elif social.get('type') == 'telegram':
                                        telegram_url = str(social.get('url'))
                                if fdv_temp > 150000 and liq_temp >= 30000:
                                    high_count_tokens_correction[token_temp] = {'status': "moon", 'website_url': website_url, 'twitter_url': twitter_url , 'telegram_url' : telegram_url ,'createdDelta': high_count_tokens[token_temp]['createdDelta'] }
                                if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                    if token_temp in high_count_tokens_correction:
                                        if high_count_tokens_correction[token_temp]['status'] != "cto" :
                                            await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO "+str(twitter_url)+" "+str(telegram_url))
                                            await forward_msg(str(token_temp)+" member_TG:  #CTO")
                                    elif token_temp not in high_count_tokens_correction:
                                            await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO "+str(twitter_url)+" "+str(telegram_url))
                                            await forward_msg(str(token_temp)+" #CTO")
                                    high_count_tokens_correction[token_temp] = {'status': "cto", 'website_url': website_url, 'twitter_url': twitter_url , 'telegram_url' : telegram_url ,'createdDelta': high_count_tokens[token_temp]['createdDelta'] }


            #tahap 2 cari koreksi
            params_bulk2 = []
            params_bulktemp= ""
            count = 0
            count_t = 0
            for token in list(high_count_tokens_correction.keys()):
                if (time.time() - high_count_tokens_correction[token]['createdDelta']) <= 7200 and (high_count_tokens_correction[token]['status'] == "moon" or high_count_tokens_correction[token]['status'] == "dip") :
                    count += 1
                    if count <= 7:
                        params_bulktemp += token+","
                        if count == 7:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=14 :
                        params_bulktemp += token+","
                        if count == 14:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=21 :
                        params_bulktemp += token+","
                        if count == 21:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                    elif count <=28 :
                        params_bulktemp += token+","
                        if count == 28:
                            params_bulk2.append(params_bulktemp)
                            params_bulktemp= ""
                elif (time.time() - high_count_tokens_correction[token]['createdDelta']) > 9200:
                    del high_count_tokens_correction[token]   
                    count_t += 1
                else:
                    count_t += 1
                if count + count_t == len(high_count_tokens.keys()) and count % 7 != 0:
                    params_bulk1.append(params_bulktemp)

            for s in params_bulk2:         
                if s != "":
                    url_dexscreener2 = f'https://api.dexscreener.com/latest/dex/tokens/'+s
                    headers_dexscreener2 = {
                        'Cookie': '_ga_CFY1SSGE2N=GS1.1.1720353864.2.0.1720353864.0.0.0; _gid=GA1.2.1007166714.1722067188; _ga=GA1.1.1571615799.1702193879; cf_clearance=DAX6hNUR1EXDn1Y4BqSYUSqMtlWAzElF09z8My0I770-1722087608-1.0.1.1-HJnclhkye5z1u0TFwLJOOgPezl7KUDrAzwAMQwdk_FuE2r5Zk3YYlOJr2O491iYghjfQKj3eQxZGqBDgFK.j9g; _ga_532KFVB4WT=GS1.1.1722083517.783.1.1722096796.60.0.0; __cf_bm=IoQrPu9umlNj.l8JPtdrqQjcip9xaJztsaH2KdLYVTk-1722098687-1.0.1.1-q6N_SegQhyqMYGtBuQnUzReU4LQGQyrepoUEOHwREqyAesZeIhF2z_pMSRRXsuwOPcZcxgKOoObif1vVNmrRrEex0dU6uSQ04fT0PQd5ulQ; _ga_RD6VMQDXZ6=GS1.1.1722100207.25.0.1722100207.0.0.0'
                    }
                    dexscreener_data2 = await fetch_data_coin(url_dexscreener2, headers_dexscreener2)
                    
                    if 'error' in dexscreener_data2:
                        print("ASSSSSOOOOOy")
                        print(dexscreener_data2['error'])
                    pairs = dexscreener_data2.get('pairs', None)

                    if pairs:
                        for pair in dexscreener_data2["pairs"]:
                            token_temp = pair.get('baseToken', {}).get('address', None)
                            if token_temp in high_count_tokens_correction and pair["dexId"] == "raydium":
                                fdv_temp = 0
                                liq_temp = 0
                                if 'fdv' in pair:
                                    fdv_temp = pair["fdv"]
                                if 'liquidity' in pair:
                                    liq_temp = pair["liquidity"]["usd"]
                                websites = pair.get('info', {}).get('websites', [])
                                website_url = websites[0].get('url', None) if websites else None
                                socials = pair.get('info', {}).get('socials', [])
                                twitter_url = None
                                telegram_url = None
                                price_change_h24 = pair.get('priceChange', {}).get('h24', None)

                                for social in socials:
                                    if social.get('type') == 'twitter':
                                        twitter_url = str(social.get('url'))
                                    elif social.get('type') == 'telegram':
                                        telegram_url = str(social.get('url'))
                            
                                if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()) and high_count_tokens_correction[token_temp]['status'] != "cto" :
                                    if twitter_url:
                                        found_tokens = [token for token in viral_store if token in twitter_url.lower()]
                                        if found_tokens:
                                            await forward_alert("https://dexscreener.com/solana/"+token_temp+" https://bullx.io/terminal?chainId=1399811149&address="+token_temp+" #ALR CTO")
                                    await forward_msg("https://dexscreener.com/solana/"+token_temp+" #CTO "+str(twitter_url)+" "+str(telegram_url))
                                    await forward_msg(str(token_temp)+" member_TG:  #CTO")
                                    high_count_tokens_correction[token_temp]['status'] = "cto"                         
                                elif float(price_change_h24) < 20 and  high_count_tokens_correction[token_temp]['status'] != "dip" and high_count_tokens_correction[token_temp]['status'] != "cto":
                                    await forward_trend("https://dexscreener.com/solana/"+token_temp+" #dip "+str(twitter_url)+" "+str(telegram_url))
                                    await forward_trend(str(token_temp)+" #dip")
                                    high_count_tokens_correction[token_temp]['status'] = "dip"       
   
        except Exception as e:
            tb = traceback.format_exc()
            print("An error occurred:\n", tb)
            print(f"Error55: {e}")
        


# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=[PeerChannel(user_check_x)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received: asawfd")
        #print(event.message.text)

        if  "/dp" in event.message.text and ": No" not in event.message.text:
            await forward_msg(event.message.text)

    except Exception as e:
        print(f"Error33: {e}")

# ricky 5 menit awal ============================================================================================================== 



# get volume ============================================================================================================== 
url = 'https://api-v2.solscan.io/v2/account/balance_change'
params = {
    'address': 'AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS',
    'page_size': '100',
    'page': '1',
    'flow': 'out'
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
    'cookie': '_ga=GA1.1.1552685285.1703187686; amp_1adb3b=ewmgcpLztfynKaJxQoFPW3...1hpvuj7s3.1hpvuj7s3.c.0.c; cf_clearance=aAUMgOCRrNEZUJO.f2nEepYeW.oVxxtw_6QtDJfKwaA-1722390903-1.0.1.1-ifiR5dSN7josSzEJgxD6eJ1xL3h1OCe2iuUG69dAnye6VuGnoIU8k79RL3fVcO_fyweBFaBco6AnvZbyWJwd0w; _ga_PS3V7B7KV0=GS1.1.1722390892.214.1.1722391066.0.0.0',
    'origin': 'https://solscan.io',
    'priority': 'u=1, i',
    'referer': 'https://solscan.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sol-aut': 'jVoIbjkS=-VTzL=gtq5=m2MVZCB9dls0fKUTXaeI',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}


temp2_data = {}
# Penyimpanan token_address dan waktu terakhir diperbarui
token_store = {}
# Penyimpanan token_address dengan count > 10 dan waktu ditambahkannya
high_count_tokens = {}

high_count_tokens_correction = {}

token_store_pump = {}

high_count_tokens_5m = {} 

high_count_tokens_6m = {}

high_count_tokens_00 = {}

token_temps = {}

viral_token = {}

token_volume = {}

viral_store = {}



async def fetch_data(session):
    #proxy = "http://192.168.100.98:80"
    async with session.get(url, headers=headers, params=params) as response:
        #print("Response content:", response.text)
        try:
            #data = response.json()
            #print(data)
            return await response.json()
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            print("Response content:", response.text)
    
async def fetch_data_dex(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()

async def get_volume():
    #connector = aiohttp.TCPConnector()
    global temp2_data
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await asyncio.sleep(10)
                current_time = datetime.now()    
                # Fetch data from API
                data = await fetch_data(session)
                #print(data)
                if data.get('success') and 'data' in data :
                    transactions = data['data']
                    #transactions = data['data']
                    new_tokens = set()
                    current_date = datetime.now()
                    temp_data = {}
                    for transaction in reversed(transactions):
                        #change = transaction.get('change', {})
                        token_address = transaction.get('token_address')
                        if token_address and token_address != 'So11111111111111111111111111111111111111112': #and str(change_amount).startswith('-'):
                            change_amount = int(transaction.get('amount', 0))
                            decimals = transaction.get('token_decimals', 0)
                            block_time = transaction.get('block_time')
                            if token_address in temp2_data:
                                if block_time> temp2_data[token_address]['block_time']: 
                                    if token_address not in temp_data :
                                        temp_data[token_address] = {'change_amount': [change_amount], 'decimals': [decimals], 'block_time': block_time, 'array_block' : [block_time] }
                                        new_tokens.add(token_address)
                                    elif token_address in temp_data and block_time > temp_data[token_address]['block_time']:
                                        temp_data[token_address]['change_amount'].append(change_amount)
                                        temp_data[token_address]['array_block'].append(block_time)
                                        temp_data[token_address]['decimals'].append(decimals)
                                        temp_data[token_address]['block_time']=block_time
                                        new_tokens.add(token_address)
                            elif token_address not in temp2_data:
                                if token_address not in temp_data:
                                    temp_data[token_address] = {'change_amount': [change_amount], 'decimals': [decimals], 'block_time': block_time, 'array_block' : [block_time] }
                                    new_tokens.add(token_address)
                                elif token_address in temp_data and block_time > temp_data[token_address]['block_time']:
                                    temp_data[token_address]['change_amount'].append(change_amount)
                                    temp_data[token_address]['array_block'].append(block_time)
                                    temp_data[token_address]['decimals'].append(decimals)
                                    temp_data[token_address]['block_time']=block_time
                                    new_tokens.add(token_address)                     
                    
                    temp2_data = temp_data

                    batch_size = []
                    if len(temp_data) <= 7:
                        batch_size.append(len(temp_data))
                    elif len(temp_data) <= 14:
                        batch_size = [7,len(temp_data)-7]
                    elif len(temp_data) <= 21:
                        batch_size = [7,7,len(temp_data)-14]
                    elif len(temp_data) <= 28:
                        batch_size = [7,7,7,len(temp_data)-21]
                    elif len(temp_data) <= 35:
                        batch_size = [7,7,7,7,len(temp_data)-28]
                    elif len(temp_data) <= 42:
                        batch_size = [7,7,7,7,7,len(temp_data)-35]
                    elif len(temp_data) <= 49:
                        batch_size = [7,7,7,7,7,7,len(temp_data)-42]
                    elif len(temp_data) <= 56:
                        batch_size = [7,7,7,7,7,7,7,len(temp_data)-49]

                    start = 0
                    for idx, size in enumerate(batch_size):
                        params_bulk = ""
                        end = start + size
                        data_batch = {k: temp_data[k] for k in list(temp_data)[start:end]}
                        start = end
                        #print(len(temp_data))
                        #print(f"Batch {idx + 1}:")
                        #print(f"len batc {len(data_batch)}:")
                        

                        for token_address in data_batch.keys():
                                params_bulk += token_address + ","

                        #print(params_bulk)
                        if params_bulk != "":
                            url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{params_bulk}'
                            headers_dexscreener = {
                                'Cookie': '_ga_CFY1SSGE2N=GS1.1.1720353864.2.0.1720353864.0.0.0; _gid=GA1.2.1007166714.1722067188; _ga=GA1.1.1571615799.1702193879; cf_clearance=DAX6hNUR1EXDn1Y4BqSYUSqMtlWAzElF09z8My0I770-1722087608-1.0.1.1-HJnclhkye5z1u0TFwLJOOgPezl7KUDrAzwAMQwdk_FuE2r5Zk3YYlOJr2O491iYghjfQKj3eQxZGqBDgFK.j9g; _ga_532KFVB4WT=GS1.1.1722083517.783.1.1722096796.60.0.0; __cf_bm=IoQrPu9umlNj.l8JPtdrqQjcip9xaJztsaH2KdLYVTk-1722098687-1.0.1.1-q6N_SegQhyqMYGtBuQnUzReU4LQGQyrepoUEOHwREqyAesZeIhF2z_pMSRRXsuwOPcZcxgKOoObif1vVNmrRrEex0dU6uSQ04fT0PQd5ulQ; _ga_RD6VMQDXZ6=GS1.1.1722100207.25.0.1722100207.0.0.0'
                            }
                            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                            if 'error' in dexscreener_data:
                                print("ASSSSSOOOOOy")
                                print(dexscreener_data['error'])

                            pairs = dexscreener_data.get('pairs', None)
                            current_time = time.time()
                            #print(f"len pairs {len(pairs)}:")
                            #print(pairs) 
                            if pairs and len(pairs)>0:
                                for pair in dexscreener_data["pairs"]:
                                    token_address = pair.get('baseToken', {}).get('address', None)
                                    if token_address in temp_data and pair["dexId"] == "raydium":
                                        
                                        socials = pair.get('info', {}).get('socials', [])
                                        twitter_url = None
                                        telegram_url = None
                                        for social in socials:
                                            if social.get('type') == 'twitter':
                                                twitter_url = str(social.get('url'))
                                            elif social.get('type') == 'telegram':
                                                telegram_url = str(social.get('url'))

                                        for index, block_time in enumerate(temp_data[token_address]['array_block']):
                                            #print(f"Index: {index}, Time: {block_time}")
                                            change_amount = temp_data[token_address]['change_amount'][index]
                                            decimals = temp_data[token_address]['decimals'][index]
                                            if token_address not in token_store:
                                                #print(pairs)
                                                result = {}
                                                pair_created_at = pair["pairCreatedAt"] / 1000  # convert to seconds
                                                created_at_datetime = datetime.fromtimestamp(pair_created_at, tz=timezone.utc)
                                                fdv_temp = 100000
                                                liq_temp = 160000
                                                if 'fdv' in pair:
                                                    fdv_temp = pair["fdv"]
                                                if 'liquidity' in pair:
                                                    liq_temp = pair["liquidity"]["usd"]
                                                
                                                token_store[token_address] = {'last_seen': current_date, 'count': 1, 'block_time': block_time, 'createdTime': pair_created_at, 'array_time' : [block_time] , 'telegram_url' : telegram_url , 'twitter_url' : twitter_url , 'fdv' : fdv_temp  }
                                                #print(current_time - pair_created_at)
                                                if pair_created_at > 0 :  # 5 minutes in seconds
                                                    result[pair["baseToken"]["symbol"]] = {
                                                    "pairCreatedAt": created_at_datetime.strftime('%Y-%m-%d %H:%M:%S'),
                                                    "priceChange_m5": pair["priceChange"]["m5"],
                                                    "volume_m5": pair["volume"]["m5"],
                                                    "txns_m5": pair["txns"]["m5"],
                                                    "fdv" : fdv_temp,
                                                    "liquidity" :liq_temp,
                                                    "price" : pair["priceUsd"],
                                                    "change_amount" : abs(change_amount),
                                                    "decimals" : decimals
                                                    }
                                                    print("Token Baruuuu:", token_address)
                                                    result_str = json.dumps(result)
                                                    temp_tx_sol = (abs(change_amount)/(10 ** decimals))*float(pair["priceUsd"])
                                                    if (current_time - pair_created_at) <= 1000 and pair["priceChange"]["h1"] > 15 and temp_tx_sol > 1000 and token_address not in  high_count_tokens and liq_temp > 15000 :
                                                        if twitter_url:
                                                            found_tokens = [token for token in viral_store if token in twitter_url.lower()]
                                                            if found_tokens:
                                                                await forward_alert("https://dexscreener.com/solana/"+token_address+" https://bullx.io/terminal?chainId=1399811149&address="+token_address+" #ALR  #DATA="+str(result_str)+" SAATNYA JPPPPP!!!! From Viral WOY")
                                                        elif  token_address in token_volume:
                                                            await forward_alert("https://dexscreener.com/solana/"+token_address+" https://bullx.io/terminal?chainId=1399811149&address="+token_address+" #ALR  #DATA="+str(result_str)+" SAATNYA JPPPPP!!!! From Volume WOY")
                                                        elif temp_tx_sol > 10000:
                                                            await forward_alert("https://dexscreener.com/solana/"+token_address+" https://bullx.io/terminal?chainId=1399811149&address="+token_address+" #ALR  #DATA="+str(result_str)+"  10K JEPEWOY VIRALWOY")
                                                        print(token_address)
                                                        print("1113331111")
                                                        convic = 0
                                                        if token_address in high_count_tokens_6m:
                                                            convic += 1
                                                        if token_address in high_count_tokens_5m:
                                                            convic += 1
                                                        if token_address in high_count_tokens_00:
                                                            convic += 1
                                                        high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1 , 'createdDelta': pair_created_at }
                                                        counts = high_count_tokens[token_address]['count']
                                                        if (current_time - pair_created_at) <= 300:
                                                            await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                            #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                            if (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                                                await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #11CTOOO")
                                                                #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#44CTOOO")
                                                            elif token_address in token_store_pump:
                                                                store_str = json.dumps(token_store_pump[token_address], default=datetime_converter)
                                                                if "cto" in  store_str.lower():
                                                                    await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #11CTOOO")
                                                                    #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#11CTOOO")
                                                    elif token_address in token_store_pump:
                                                        store_str = json.dumps(token_store_pump[token_address], default=datetime_converter)
                                                        if "cto" in  store_str.lower() or (twitter_url and "cto" in twitter_url.lower()) or (telegram_url and "cto" in telegram_url.lower()):
                                                            await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts)+" #55CTOOO")
                                                            if token_address in token_volume :
                                                                await forward_alert("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #ALR #DATA="+str(result_str)+" #PUMPFUN_1000USD #VOLUME #C:"+str(convic)+" Count:"+str(counts)+" #55CTOOO")
                                                            #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana Member_TG:"+str(member_count)+"#55CTOOO")   
                                                    elif (pair["priceChange"]["h24"] > 15  and 'fdv' in pair and liq_temp > 200000 and pair["fdv"] < 11000000) :
                                                        print("owoowc")
                                                        print(token_address)
                                                        print("3333666633333")
                                                        if (current_time - pair_created_at) <= 300:
                                                            await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_200k")
                                                            #await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                            await forward_check_x(token_address)
                                                    elif pair["priceChange"]["h24"] > 15 and liq_temp > 100000:
                                                        print("AUUUww")
                                                        print(token_address)
                                                        print("55566665555")
                                                        #await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_11")
                                                        #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                
                                            elif (token_address in token_store and block_time > token_store[token_address]['block_time']) or token_address in high_count_tokens :
                                                token_store[token_address]['last_seen'] = current_date
                                                token_store[token_address]['count']= 0
                                                token_store[token_address]['block_time'] = block_time
                                                if 'array_time' not in token_store[token_address]:
                                                    token_store[token_address]['array_time'] = []
                                                token_store[token_address]['array_time'].append(block_time)
                                                fdv_temp = 100000
                                                liq_temp = 99
                                                price = 0
                                                if 'fdv' in pair:
                                                    fdv_temp = pair["fdv"]
                                                if 'liquidity' in pair:
                                                    liq_temp = pair["liquidity"]["usd"]
                                                if 'priceUsd' in pair:
                                                    price = pair["priceUsd"]
                                                pair_created_at = pair["pairCreatedAt"] / 1000
                                                temp_tx_sol = (abs(change_amount)/(10 ** decimals))*float(price)
                                                if temp_tx_sol > 1000 and pair["priceChange"]["h1"] > 10 and liq_temp > 15000 and fdv_temp < 30000000 :
                                                    convic = 0
                                                    if token_address in high_count_tokens_6m:
                                                        convic += 1
                                                    if token_address in high_count_tokens_5m:
                                                        convic += 1
                                                    if token_address in high_count_tokens_00:
                                                        convic += 1

                                                    if token_address not in high_count_tokens:
                                                        print(token_address)
                                                        print("0002222000")
                                                        high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1 , 'createdDelta': pair_created_at}
                                                        counts =high_count_tokens[token_address]['count']
                                                        #await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                        #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                    elif token_address in high_count_tokens:
                                                        if block_time > high_count_tokens[token_address]['block_time']:
                                                            if temp_tx_sol > 10000 and (current_time - pair_created_at) <= 1000:
                                                                await forward_alert("https://dexscreener.com/solana/"+token_address+" https://bullx.io/terminal?chainId=1399811149&address="+token_address+" #ALR #C:"+str(convic)+" Count:"+str(counts)+" FDV:"+str(pair["fdv"])+" Token Name:"+str(pair["baseToken"]["symbol"])+"10K Volume JEPEWOY VIRALWOY")

                                                            print(token_address)
                                                            print(block_time)
                                                            print("8822888")
                                                            print( token_store[token_address]['block_time'])
                                                            if token_address not in high_count_tokens:
                                                                high_count_tokens[token_address] = {'block_time': block_time, 'post': False, 'count': 1, 'createdDelta': pair_created_at }
                                                            else:
                                                                high_count_tokens[token_address]['count'] += 1
                                                            counts =high_count_tokens[token_address]['count']
                                                            high_count_tokens[token_address]['block_time'] = block_time
                                                            print("AUUUww5")
                                                            #await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                            #await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")

                                         

                    cur_time = time.time()
                    current_date = datetime.now()  
                    print(current_date)
                    for token in list(token_store.keys()):
                        if  'createdTime' in token_store[token] and 'fdv' in token_store[token] and token not in high_count_tokens_5m and token_store[token]['fdv'] < 7000000 and token_store[token]['count'] >= 5 and cur_time - token_store[token]['createdTime'] <= 500 and token_store[token]['liquidity'] > 20000:
                            convic = 0
                            counts = 0
                            if token in high_count_tokens:
                                convic += 1
                                counts = high_count_tokens[token]['count']
                            if token in high_count_tokens_6m:
                                convic += 1
                            if token in high_count_tokens_00:
                                convic += 1
                            if token not in high_count_tokens_5m:
                                print("AUUUww4")
                                #await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
                            else:
                                print("AUUUww3")
                                #await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
                            high_count_tokens_5m[token] = current_date
                      
                        # Periksa dan hapus data yang lebih dari 6 menit
                        six_minutes_ago = current_date - timedelta(minutes=5)
                        # Filter array_data untuk menghapus elemen yang lebih dari 6 menit
                        if 'array_time' in token_store[token]:
                            if len(token_store[token]['array_time']) > 0:
                                token_store[token]['array_time'] = [
                                    data for data in token_store[token]['array_time']
                                    if datetime.fromtimestamp(data) >= six_minutes_ago
                                ]
                        
                        if 'array_time' not in token_store[token]:
                                    token_store[token]['array_time'] = []

                        if token not in  high_count_tokens_6m and 'array_time' in token_store[token] and 'fdv' in token_store[token] and len(token_store[token]['array_time']) >= 4 and token_store[token]['fdv'] < 10000000:
                            url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{token}'
                            headers_dexscreener = {
                                'Cookie': '_ga_CFY1SSGE2N=GS1.1.1720353864.2.0.1720353864.0.0.0; _gid=GA1.2.1007166714.1722067188; _ga=GA1.1.1571615799.1702193879; cf_clearance=DAX6hNUR1EXDn1Y4BqSYUSqMtlWAzElF09z8My0I770-1722087608-1.0.1.1-HJnclhkye5z1u0TFwLJOOgPezl7KUDrAzwAMQwdk_FuE2r5Zk3YYlOJr2O491iYghjfQKj3eQxZGqBDgFK.j9g; _ga_532KFVB4WT=GS1.1.1722083517.783.1.1722096796.60.0.0; __cf_bm=IoQrPu9umlNj.l8JPtdrqQjcip9xaJztsaH2KdLYVTk-1722098687-1.0.1.1-q6N_SegQhyqMYGtBuQnUzReU4LQGQyrepoUEOHwREqyAesZeIhF2z_pMSRRXsuwOPcZcxgKOoObif1vVNmrRrEex0dU6uSQ04fT0PQd5ulQ; _ga_RD6VMQDXZ6=GS1.1.1722100207.25.0.1722100207.0.0.0'
                            }

                            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                            if 'error' in dexscreener_data:
                                print("ASSSSSOOOOOy")
                                print(dexscreener_data['error'])

                            pairs = dexscreener_data.get('pairs', None)
                            #print(pairs)
                            print("AAA")
                            if pairs:
                                liq = 0
                                fdv= 11000000
                                pair = pairs[0]  # Ambil pasangan pertama
                                price_change_h24 = pair.get('priceChange', {}).get('h1', None)
                                liq = pair.get('liquidity', {}).get('usd', None)
                                fdv = pair.get('fdv', None)
                                pair_created_at = pair.get('pairCreatedAt', None)
                                pair_created_at = pair_created_at / 1000
                                if price_change_h24 > 10 and liq and fdv < 10000000:
                                    if liq > 20000:
                                        convic = 0
                                        counts = 0
                                        if token in high_count_tokens:
                                            convic += 1
                                            counts = high_count_tokens[token]['count']
                                        if token in high_count_tokens_5m:
                                            convic += 1
                                        if token in high_count_tokens_00:
                                            convic += 1
                                        if token not in high_count_tokens_6m and (cur_time - pair_created_at) <= 1000:
                                            print("AUUUww1")
                                            #await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trensPer6Menit #C:"+str(convic)+" Count:"+str(counts))
                                            #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana "+str(token_store[token]['fdv']))
                                        else:
                                            print("AUUUww2")
                                            #await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trensPer6Menit #C:"+str(convic)+" Count:"+str(counts))
                                            #await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana "+str(token_store[token]['fdv']))
                                        high_count_tokens_6m[token] = current_date
                                        print("UHUHU")
                        
                        if token not in new_tokens:
                            if (current_date - token_store[token]['last_seen']) > timedelta(minutes=120):
                                del token_store[token]

                    # Print dan simpan token_address yang count kemunculan lebih dari 10
                    for token in high_count_tokens:
                        if token in token_store_pump:
                            store_str = json.dumps(token_store_pump[token], default=datetime_converter) 
                        else:
                            store_str=""
                        if token in token_store:
                            dex_str = json.dumps(token_store[token], default=datetime_converter) 
                        else:
                            dex_str=""
                        params_cto=""
                        if "cto" in dex_str:
                            params_cto= "#3CTOOO"      
                            if token_store[token]['telegram_url']:
                                group_link = token_store[token]['telegram_url']
                        if high_count_tokens[token]['post'] == False and  high_count_tokens[token]['count'] > 1 and (time.time() - high_count_tokens[token]['createdDelta']) <= 600 :
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            if token in token_volume :
                                await forward_alert("https://dexscreener.com/solana/"+token+" https://bullx.io/terminal?chainId=1399811149&address="+token+" "+store_str+" "+dex_str+" #C:"+str(convic)+" #ALR #VOLUME #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)              
                            await forward_msg("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trendsCount1000USD2 "+store_str+" #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)
                            #await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto+" member_TG:"+str(member_count))
                            high_count_tokens[token]['post'] = True
                        if high_count_tokens[token]['post'] == False and  high_count_tokens[token]['count'] > 2 and (time.time() - high_count_tokens[token]['createdDelta']) <= 1000 :
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            
                            if token in token_volume :
                                await forward_alert("https://dexscreener.com/solana/"+token+" https://bullx.io/terminal?chainId=1399811149&address="+token+" "+store_str+" "+dex_str+" #C:"+str(convic)+" #ALR #VOLUME #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)       
                            await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trendsCount1000USD3 "+store_str+" "+dex_str+" #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count'])+" "+params_cto)
                            #await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto+" member_TG:"+str(member_count))
                            high_count_tokens[token]['post'] = True
                        elif high_count_tokens[token]['post'] == False and high_count_tokens[token]['count'] > 2:
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1
                            await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trendsCount1000USD "+store_str+" "+dex_str+"  #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count']))
                            await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends "+params_cto)
                            high_count_tokens[token]['post'] = True
                        
                    
                    # Hapus token dari penyimpanan setelah lebih dari satu jam
                    tokens_to_remove1 = [token for token, value in high_count_tokens.items() if current_date - datetime.fromtimestamp(value['block_time']) > timedelta(minutes=60)]
                    for token in tokens_to_remove1:
                        del high_count_tokens[token]
                    
                    tokens_to_remove2 = [token for token, time_added in high_count_tokens_5m.items() if current_date - time_added > timedelta(minutes=60)]
                    for token in tokens_to_remove2:
                        del high_count_tokens_5m[token]

                    tokens_to_remove3 = [token for token, time_added in high_count_tokens_6m.items() if current_date - time_added > timedelta(minutes=60)]
                    for token in tokens_to_remove3:
                        del high_count_tokens_6m[token]

                    tokens_to_remove4 = [token for token, time_added in token_volume.items() if current_date - time_added > timedelta(minutes=40)]
                    for token in tokens_to_remove4:
                        del token_volume[token]
                    print("token_volume", token_volume)

                    tokens_to_remove5 = [token for token, time_added in viral_store.items() if current_date - time_added > timedelta(minutes=40)]
                    for token in tokens_to_remove5:
                        del viral_store[token]
                    
                    #print(high_count_tokens)

            except Exception as e:
                    tb = traceback.format_exc()
                    print("An error occurred:\n", tb)
                    print(f"Error11: {e}")

#=================================================================================================================================



# waktu di pumpfun ===================================================================================================================

def is_sideways(prices, threshold=0.1, mean_threshold=6.141472506989746e-8):
    mean_price = statistics.mean(prices)
    if mean_price >= mean_threshold:
        return False
    for price in prices:
        if abs(price - mean_price) / mean_price > threshold:
            return False
    return True

def detect_spike(data, avg_volume, spike_threshold=2):
    for item in data:
        volume = item['volume']
        close = item['close']
        open_price = item['open']
        if volume > avg_volume * spike_threshold and close > open_price:
            return True
    return False

def check_token(token_address):
    url = "https://108.181.33.119/api/checkToken"
    params = {
        "tokenAddress": token_address,
        "__cpo": "aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6"
    }
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "__cpc=RXFOUlV0ZjFxdHg5L1VGd1ZrazRKZm5iR3ZOZ1ZobVlPVHpTcWRGdnJBa0VHU2RqVXhScWNjUXB1OFg5R3k1REdGQk56M2ZtbUc3bDg1UFhYcW9BMWFjZnpWLzh2VVlXd1JvTFNPZXNVK3ZDWWNYc1lCVHE5SW1oSE1SMkJJMEh2eHkzTDRjR2o2YTBXSUlyOE9uTDZoU2p5ckt3dmZiWkJ4WjRwUTlxVzdDc0dNb05DQ2l2eHNTenBJY2JDNXIrWEFQZkhLOHBwSFg2QTBrMzBGVXljTlM3b1F1T2MxMndDdXg5U2VJbEJnb1pERUNBNFkrVGpRWWh1ekI5S0kydDBVQjVaZTg4bkZEd0JUajhqZ0lKMmVpcXNrMzdpNkY4UGFHWDZiOXpOMVBsWkxXcC80SjhBMG5TdW1hWko1d0lDS0dka1V5NzZuL1h5UUd3TXBxa2J4Y1lrdUtVZ1g5WmFtbFhIR3dSbE9hNFhIUmpMcjRKSSs3WEpYTVdiQ0p6eUtTcWdRWk9JTHpYTndpR1ovZkt0R0NwZjdoUTUrMERTKzU4UkF1N0lpUWFqeGw2aGQ4VFpHLytCMm1ZUndvOTNyUkRnVUxqeVRYZHprakFKWWJ1U2c9PQ==",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
   
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status token paid code {response.status_code}")
        return None
    
def check_token2(token_address):
    url = 'https://185.16.38.230/api/checkToken'

    params = {
        'tokenAddress': token_address,
        '__cpo': 'aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6'
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__cpc=YjdMaGNkQXh5bjh2allsMWRlZXBnRklacHZTMkxxa09zK0d1K1BCazZPRnJ6eXVZQ280b25OcWkwQ01FKzZNS0w4aU94TzJqbWJPTnFvZ3p4MzdJMEZjYjBzajYvK1VwNjFCNGllczdWdUF1YzhuRGRXd2VUZnZtcElFbTZER1I=',
        'Referer': 'https://185.16.38.230/__cpi.php?s=YjdMaGNkQXh5bjh2allsMWRlZXBnRklacHZTMkxxa09zK0d1K1BCazZPRnJ6eXVZQ280b25OcWkwQ01FKzZNS0w4aU94TzJqbWJPTnFvZ3p4MzdJMEZjYjBzajYvK1VwNjFCNGllczdWdUF1YzhuRGRXd2VUZnZtcElFbTZER1I%3D&r=aHR0cHM6Ly93d3cuY2hlY2tkZXgueHl6L2FwaS9jaGVja1Rva2VuP3Rva2VuQWRkcmVzcz1BNWhDM2s0Z0dMM2p0ejdYN2RnWFhFQUx1NnA3SnNER0dkbnljc2hQcHVtcA%3D%3D&__cpo=1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
   
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status token paid code {response.status_code}")
        return None
    
def check_price(token_address):
    url = f"https://frontend-api.pump.fun/candlesticks/{token_address}?offset=0&limit=1000&timeframe=1" 
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "if-none-match": 'W/"93e-bo8+J78RPS0I6CapRtkE1lQcxKk"',
        "origin": "https://pump.fun",
        "priority": "u=1, i",
        "referer": "https://pump.fun/",
        "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    } 
    params = {
        "tokenAddress": token_address
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response  # Assuming the response is JSON
    else:
        print(f"Request failed with status price code {response.status_code}")
        return None
    
def check_tx(token_address):
    url = "https://frontend-api.pump.fun/trades/"+token_address    
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,id;q=0.8,ms;q=0.7",
        "origin": "https://pump.fun",
        "priority": "u=1, i",
        "referer": "https://pump.fun/",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    } 

    offset = 0
    all_data_tx = []

    while True:
        params = {
            "limit": 200,
            "offset": offset
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data_tx = response.json()
            
            if len(data_tx) == 0:
                break
            
            all_data_tx.extend(data_tx)
            offset += 200
        else:
            print(f"Error: {response.status_code}")
            break

    if all_data_tx:
        return all_data_tx  # Assuming the response is JSON
    else:
        print(f"Request failed with status tx code {response.status_code}")
        return None

'''@client.on(events.NewMessage(chats=["@pumpfunnotifs"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:           
        # Regex untuk mencari token address setelah "🆕**Mint:**"
        mint_address = re.search(r'\*\*💎 Mint :\*\* `([^`]+)`', event.message.text)
        # Mencari token address menggunakan regex
        #match = re.search(pattern, event.message.text)
        if ("NEW TOKEN 25K MCAP" in event.message.text) and mint_address:
            token_address = mint_address.group(1)
            waktu_sekarang = datetime.now()


            response_tx =check_tx(token_address)
            response = check_price(token_address)
            response_paid = check_token(token_address)
               
            if response_tx and response and response_paid and response.status_code == 200 and response_tx.status_code == 200:


                print("token adres PF "+token_address)
                data_tx = response_tx.json()
                data_paid = response_paid.json()
                paid = data_paid.get('paid', 'Unknown')

                # Panjang array utama
                array_length = len(data_tx)
                
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                high_value_buy_5b = sum(1 for trade in data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                # Menghitung jumlah data dengan timestamp yang sama
                max_sol_amount_buy = max((trade['sol_amount'] for trade in data_tx if trade['is_buy']), default=None)

                timestamps = [trade['timestamp'] for trade in data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = sum(1 for count in timestamp_counts.values() if count > 1)
                text_temp= event.message.text.split("**Tool**")[0]
                result = (
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"buy dengan sol_amount > 1: {high_value_buy}\n"
                    f"sell dengan sol_amount > 1: {high_value_sell}\n"
                    f"buy dengan sol_amount > 5: {high_value_buy_5b}\n"
                    f"timestamp yang sama: {duplicate_timestamps}\n"
                    f"sol_amount tertinggi: {max_sol_amount_buy/1000000000}\n"
                    f"detail: {text_temp}"
                    f"Paid: {paid}"
                )
                sent = False
                ray=""
                if "NEW LISTING RAYDIUM" in event.message.text:
                    ray= "RAYYY LIST"
                else :
                    token_temps[token_address] = waktu_sekarang

                data = response.json()
                if paid and sent == False:
                    print("Datsinyall paid 1")
                    print(paid)
                    sent = True
                    await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                    await forward_check_x(str(token_address))
                if sent == False and len(data) == 2 and data[0]['volume'] > 50203042087 and data[1]['volume'] > 50203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                    print("Datsinyall 1")
                    sent = True
                    await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                    await forward_check_x(str(token_address))
                if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                    print("Datsinyall 2")
                    sent = True
                    await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                    await forward_check_x(str(token_address))
                if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                    print("Datsinyall 3")
                    sent = True
                    await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                    await forward_check_x(str(token_address))
                if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                    print("SinyalvolumePump4 ")
                    sent = True
                    await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                    await forward_check_x(str(token_address))
                if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                    # Mengambil harga penutupan (close) dan volume
                    closes = [item['close'] for item in data]
                    volumes = [item['volume'] for item in data]

                    # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                    sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                    if sideways_detected:
                        print("Kondisi sideways terdeteksi.")
                        avg_volume = statistics.mean(volumes[-10:-4])
                        # Deteksi spike volume pada 4 data paling akhir
                        if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                            print("Spike volume terdeteksi pada 4 data paling akhir.")
                            sent = True
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                            await forward_check_x(str(token_address))
                        else:
                            print("Tidak ada spike volume pada 4 data paling akhir.")
                    else:
                        print("Kondisi sideways tidak terdeteksi.")
                if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                    # Mengambil harga penutupan (close) dan volume
                    closes = [item['close'] for item in data]
                    volumes = [item['volume'] for item in data]

                    # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                    sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                    if sideways_detected:
                        print("Kondisi sideways terdeteksi.")
                        avg_volume = statistics.mean(volumes[:-2])
                        # Deteksi spike volume pada 4 data paling akhir
                        if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                            print("Spike volume terdeteksi pada 4 data paling akhir.")
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                            sent = True
                            await forward_check_x(str(token_address))
                        else:
                            print("Tidak ada spike volume pada 4 data paling akhir.")
                    else:
                        print("Kondisi sideways tidak terdeteksi.")
                else:
                    # Mengecek jika volume terbanyak bukan pada array paling awal
                    max_volume = max(data, key=lambda x: x['volume'])
                    if max_volume != data[0]:
                        print("Volume terbanyak bukan pada array paling awal.")
                        # Mengecek jika array paling akhir memiliki close lebih besar dari nilai close array sebelumnya
                        if data[-1]['close'] > data[-2]['close']:
                            print("Array paling akhir memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                            await forward_trend("https://pump.fun/"+str(token_address)+"  SinyalvolumePump")
                        else:
                            print("Array paling akhir tidak memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                    else:
                        print("Volume gagal")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            

    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error88: {e}")
        print(f"Error88: {e}")'''

def extract_segment(url):
    # Menghapus "https://" atau "http://"
    url = url.replace("https://", "").replace("http://", "")
    # Memisahkan domain dan sisa URL
    parts = url.split("/", 1)
    # Memeriksa apakah ada bagian setelah domain
    if len(parts) > 1:
        subparts = parts[1].split("/", 1)
        return subparts[0]
    return None

@client.on(events.NewMessage(chats=["@PumpFunNewPools"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"

        pattern_buy = r"The creator bought for ([\d.]+)"
        match_buy = re.search(pattern_buy, event.message.text)

        pattern_of = r"of\s+(\w+)"
        match_of = re.search(pattern_of, event.message.text)
        # Regex patterns
        pattern_website = r"Website\*\* :\s+(.*)"
        pattern_twitter = r"Twitter\*\* :\s+(.*)"
        pattern_telegram = r"Telegram\*\* :\s+(.*)"
        # Regex untuk menemukan alamat akun Solana dari URL
        pattern_dev = r'https://solscan.io/account/([a-zA-Z0-9]+)'

        # Cari kemunculan pertama pola dalam teks pesan
        match_dev = re.search(pattern_dev, event.message.text)

        # Search for patterns
        match_website = re.search(pattern_website, event.message.text)
        match_twitter = re.search(pattern_twitter, event.message.text)
        match_telegram = re.search(pattern_telegram, event.message.text)
        match = re.search(pattern, event.message.text)
        

        if "NEW PUMP FUN POOL" in event.message.text and match and match_buy and match_of and  match_website and match_twitter and match_telegram:
            result = {}
            token_address = match.group(1)
            amount = float(match_buy.group(1))
            word_after_of = match_of.group(1)
            first_address = match_dev.group(1)
            website_status = match_website.group(1).strip()
            twitter_status = match_twitter.group(1).strip()
            telegram_status = match_telegram.group(1).strip()
            result[token_address] = {
                                            "token_address": token_address,
                                            "word_after_of": word_after_of,
                                            "amount": amount,
                                            "website_status" : website_status,
                                            "twitter_status" :twitter_status,
                                            "telegram_status" :telegram_status,
                                            }
                    
            result_str = json.dumps(result)
            url_profile = f"https://frontend-api.pump.fun/users/{first_address}"
            headers_profile = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                'origin': 'https://pump.fun',
                'priority': 'u=1, i',
                'referer': 'https://pump.fun/',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
            }

            #print(first_address)
           
            #print(response)
            try:
                current_time = datetime.now()
                # Menghapus token yang sudah lebih dari 1 menit
                #print(viral_token)
                #response_paid = check_token(token_address)
                token_temps[token_address] = current_time
                param_viral = False
                tokens_to_remove3 = [token for token, data in viral_token.items() if all(current_time - time_added > timedelta(minutes=1) for time_added in data['timestamps'])]
                for token in tokens_to_remove3:
                    del viral_token[token]

                if "x.com" in twitter_status.lower():
                    if  "x.com" in website_status.lower() and "x.com" in telegram_status.lower():
                        param_viral = True
                    elif "available" in website_status.lower() and "available" in telegram_status.lower():
                        param_viral = True
                    elif "available" in website_status.lower() and "x.com" in telegram_status.lower():
                        param_viral = True

                    key_twitter = extract_segment(twitter_status.lower())
                    if key_twitter:
                        # Mengecek apakah token sudah ada 2 kali dalam 10 menit terakhir
                        token_data = viral_token.get(key_twitter, {'timestamps': [], 'some_string': twitter_status.lower(), 'some_boolean': param_viral})
                        token_data['timestamps'] = [time for time in token_data['timestamps'] if current_time - time <= timedelta(minutes=1)]

                        if len(token_data['timestamps']) >= 1 and param_viral:
                            if  key_twitter not in viral_store:
                                await forward_alert(key_twitter +" "+ twitter_status.lower() + " VRLLWOY")
                            viral_store[key_twitter] = current_time

                        # Menambahkan waktu saat ini ke dalam daftar waktu token
                        token_data['timestamps'].append(current_time)

                        # Menyimpan string dan boolean baru atau memperbarui yang ada
                        token_data['some_string'] = twitter_status.lower()
                        token_data['some_boolean'] = True

                        # Menyimpan kembali data token ke dalam viral_token
                        if param_viral:
                            viral_token[key_twitter] = token_data

                if word_after_of.lower() in website_status.lower() and  "onlyfans" not in website_status and "x.com" not in website_status and "twitch" not in website_status and "Not" not in website_status and "Not" not in twitter_status and ("x" in twitter_status or  "twitter"  in twitter_status) and word_after_of.lower() in twitter_status.lower() and "Not" not in telegram_status:
                    response = requests.get(url_profile, headers=headers_profile)
                    if response.status_code == 200 and response.headers.get('Content-Type'):
                        data = response.json()
                        username = data.get('username')
                        username = str(username)
                        last_update = data.get('last_username_update_timestamp')
                        #print(f"Username: {username}")
                        #print(f"Last Username Update Timestamp: {last_update}")
                        if  word_after_of.lower() in username.lower():
                            await forward_trend(str(result_str)+ "  Sinyalpumpawal")
                            await forward_trend("https://pump.fun/"+str(token_address) +"  "+str(last_update))
                    else:
                        print("ss")
                        #await forward_trend(str(result_str)+ "  Sinyalpumpawal")
                        #await forward_trend("https://pump.fun/"+str(token_address))
                    #if  "dognald" in str(word_after_of).lower():
                    #    await forward_msg(str(result_str)+ " DOGNALD Sinyalpumpawal")
                    #    await forward_msg("https://pump.fun/"+str(token_address))
            except requests.exceptions.JSONDecodeError:
                print(f"Permintaan gagal dengan status code: {response.status_code}")
                print("Konten respons:", response.text)

    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"ErrorQQ: {e}")


async def fetch_data_coin(url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return {'error': 'Request failed', 'status': response.status}

def calculate_delta_minutes(created_timestamp, king_of_the_hill_timestamp):
    created_time = datetime.fromtimestamp(created_timestamp / 1000, tz=timezone.utc)
    king_of_the_hill_time = datetime.fromtimestamp(king_of_the_hill_timestamp / 1000, tz=timezone.utc)
    delta = king_of_the_hill_time - created_time
    return delta.total_seconds() / 60  # Kembali dalam menit

async def check_string_async(s):
    # Cek apakah 4 karakter awal adalah huruf dan tidak diakhiri dengan 'pump'
    if re.match(r'^[A-Za-z]{4}', s) and not s.endswith('pump'):
        return True
    return False

def check_symbol(mint_string, symbol):
    return mint_string[:3].upper() == symbol[:3].upper()

async def get_token_info(mint_string, retries=3, delay=2):
    async with aiohttp.ClientSession() as session:
        url = f"https://pumpportal.fun/api/data/token-info?ca={mint_string}"
        for attempt in range(retries):
            async with session.get(url) as response:
                if response.status == 200:
                    token_info = await response.json()
                    if 'data' in token_info:
                        return token_info['data']
                await asyncio.sleep(delay)
        return None


# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=[PeerChannel(plonk_bot)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        token_address = ""
        ray_params = False
        if  "MOVING TO RAYDIUM" in event.message.text:
            ray_params = True
        if (ray_params or "NEW KOTH" in event.message.text) and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            match = re.search(r'\*\*Mint:\*\* `([\w]+)`', event.message.text)
            if match:
                token_address = match.group(1)
            #print(event.message.text)
            if ray_params == False:
                print(f"CA KOTH: {token_address}")
            else:
                print(f"CA Ray: {token_address}")
        if token_address != "":
            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)


                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                    
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah buy > 1 SOL: {high_value_buy}\n"
                    f"Jumlah sell > 1 SOL: {high_value_sell}\n"
                    f"Jumlah buy > 5 SOL: {high_value_buy_5b}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                
                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                
                                                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    result += f"https://pump.fun/profile/{user}  {persentase:.2f}%\n"
                    result += f"https://dexscreener.com/solana/{token_address}?maker={user}\n"
                    result += f"--------------------------------------------------------------\n"
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False

                
                sent = False
                ray= ""
                if ray_params:
                    ray= "RAYYY LIST Deploy"
                else:
                    ray= "KOTH"

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                found_tokens = [token for token in viral_store if token in text_messages.lower()]
                if found_tokens:
                    viral_param = True
                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  #ALR Viral Param PF "+ray)

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    if token_address in token_temps:
                        waktu_simpan=token_temps[token_address]
                        selisih_waktu = waktu_sekarang - waktu_simpan
                        if selisih_waktu < timedelta(minutes=5):
                            token_volume[token_address] = current_time
                            if viral_param:
                                await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalFASTLISTING "+ ray)
                            await forward_check_x(str(token_address))

                    data = response.json()

                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        await forward_check_x(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) >= 14 and ray_params:
                        if data[-1]['close'] > data[-2]['close'] and data[-2]['close'] > data[-3]['close'] and data[-1]['volume'] > 12203042087 and data[-2]['volume'] > 12203042087:
                            print("Spike volume terdeteksi pada 4 data paling akhir.")
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                            sent = True
                            token_volume[token_address] = current_time
                            if viral_param:
                                await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                            await forward_check_x(str(token_address))
                        else:
                            print("Tidak ada spike volume pada 4 data paling akhir.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    else:
                        # Mengecek jika volume terbanyak bukan pada array paling awal
                        max_volume = max(data, key=lambda x: x['volume'])
                        if max_volume != data[0]:
                            print("Volume terbanyak bukan pada array paling awal.")
                            # Mengecek jika array paling akhir memiliki close lebih besar dari nilai close array sebelumnya
                            if data[-1]['close'] > data[-2]['close']:
                                print("Array paling akhir memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                                await forward_trend("https://pump.fun/"+str(token_address)+"  SinyalvolumePump")
                                sent = True
                            else:
                                print("Array paling akhir tidak memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                        else:
                            print("Volume gagal")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
            if ray_params:
                token_to_delete = []
                for token_address, waktu_simpan in token_temps.items():
                    selisih_waktu = datetime.now() - waktu_simpan
                    if selisih_waktu > timedelta(minutes=30):
                        token_to_delete.append(token_address)
                for token_address in token_to_delete:
                    del token_temps[token_address]
    
                url_coin = f'https://frontend-api.pump.fun/coins/{token_address}'
                headers_coin = {
                    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                    'origin': 'https://pump.fun',
                    'referer': 'https://pump.fun/'
                }
                coin_data = await fetch_data_coin(url_coin, headers_coin)
                
                if 'error' in coin_data:
                    print(coin_data['error'])
                    return

                creator = coin_data.get('creator', None)
                symbol = coin_data.get('symbol', None)
                king_of_the_hill_timestamp = coin_data.get('king_of_the_hill_timestamp', None)
                twitter = coin_data.get('twitter', None)
                telegram = coin_data.get('telegram', None)
                website = coin_data.get('website', None)
                created_timestamp = coin_data.get('created_timestamp', None)
                
                if created_timestamp and king_of_the_hill_timestamp:
                    delta_minutes = calculate_delta_minutes(created_timestamp, king_of_the_hill_timestamp)
                else:
                    delta_minutes = None
                
                if (twitter and "cto" in twitter.lower()) or (telegram and "cto" in telegram.lower()) and delta_minutes and delta_minutes < 4:
                    await forward_msg("https://pump.fun/"+str(token_address) +"  HIGH CONVICTION!!!!")
                
                result = {
                    'creator': creator,
                    'symbol': symbol,
                    'king_of_the_hill_timestamp': king_of_the_hill_timestamp,
                    'twitter': twitter,
                    'telegram': telegram,
                    'website': website,
                    'delta_minutes': delta_minutes,
                    'signal': False,
                    'time' : datetime.now()
                }
                print(result['delta_minutes'])
                if   result['delta_minutes'] and result['delta_minutes'] > 0:
                    url_balances = f'https://frontend-api.pump.fun/balances/{creator}?limit=50&offset=0'
                    headers_balances = {
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                        'origin': 'https://pump.fun',
                        'referer': 'https://pump.fun/'
                    }
                    
                    balances_data = await fetch_data_coin(url_balances, headers_balances)
                    
                    if 'error' in balances_data:
                        print(balances_data['error'])
                        return
                    
                    # Cari nilai value dari symbol yang didapat dari endpoint pertama
                    value = None
                    for item in balances_data:
                        if item['symbol'] == symbol:
                            value = item['value']
                            break
                    result['value'] = value
                    print(result) 
                    if value and int(value) < 500:
                        token_store_pump[token_address] = result
                print("String tidak sssssssssssssssssssssssssssssss kata 'asas'")
                current_time = datetime.now()  
                for token in list(token_store_pump.keys()):
                    if token_store_pump[token]['time']:
                        if current_time - token_store_pump[token]['time'] > timedelta(minutes=120):
                            del token_store_pump[token]
                    else:
                        del token_store_pump[token]

    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================

'''
@client.on(events.NewMessage(chats=["@PumpFunHotCalls"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        token_address = ""
        if ("RAYDIUM POOL DEPLOYED" in event.message.text) and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"
            match = re.search(pattern, event.message.text)
            if match:
                token_address = match.group(1)
        elif ("NEW CURVE COMPLETED" in event.message.text):
            pattern = r'NEW CURVE COMPLETED\s*\n\s*`([A-Za-z0-9]+)`'
            match = re.search(pattern, event.message.text)
            if match:
                token_address = match.group(1)
        if token_address != "":
            token_address = match.group(1)
            print(f"CA Ray: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)


                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                    
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah buy > 1 SOL: {high_value_buy}\n"
                    f"Jumlah sell > 1 SOL: {high_value_sell}\n"
                    f"Jumlah buy > 5 SOL: {high_value_buy_5b}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                
                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                
                                                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    result += f"https://pump.fun/profile/{user}  {persentase:.2f}%\n"
                    result += f"https://dexscreener.com/solana/{token_address}?maker={user}\n"
                    result += f"--------------------------------------------------------------\n"
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False

                
                sent = False
                ray= "RAYYY LIST Deploy"

                current_time = datetime.now()
                viral_param = False
                found_tokens = [token for token in viral_store if token in event.message.text]
                if found_tokens:
                    viral_param = True

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    if token_address in token_temps:
                        waktu_simpan=token_temps[token_address]
                        selisih_waktu = waktu_sekarang - waktu_simpan
                        if selisih_waktu < timedelta(minutes=5):
                            token_volume[token_address] = current_time
                            if viral_param:
                                await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalFASTLISTING "+ ray)
                            await forward_check_x(str(token_address))

                    data = response.json()

                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        await forward_check_x(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    else:
                        # Mengecek jika volume terbanyak bukan pada array paling awal
                        max_volume = max(data, key=lambda x: x['volume'])
                        if max_volume != data[0]:
                            print("Volume terbanyak bukan pada array paling awal.")
                            # Mengecek jika array paling akhir memiliki close lebih besar dari nilai close array sebelumnya
                            if data[-1]['close'] > data[-2]['close']:
                                print("Array paling akhir memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                                await forward_trend("https://pump.fun/"+str(token_address)+"  SinyalvolumePump")
                                sent = True
                            else:
                                print("Array paling akhir tidak memiliki nilai close lebih besar dari nilai close array sebelumnya.")
                        else:
                            print("Volume gagal")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
            token_to_delete = []
            for token_address, waktu_simpan in token_temps.items():
                selisih_waktu = datetime.now() - waktu_simpan
                if selisih_waktu > timedelta(minutes=30):
                    token_to_delete.append(token_address)
            for token_address in token_to_delete:
                del token_temps[token_address]
   
            url_coin = f'https://frontend-api.pump.fun/coins/{token_address}'
            headers_coin = {
                'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                'origin': 'https://pump.fun',
                'referer': 'https://pump.fun/'
            }
            coin_data = await fetch_data_coin(url_coin, headers_coin)
            
            if 'error' in coin_data:
                print(coin_data['error'])
                return

            creator = coin_data.get('creator', None)
            symbol = coin_data.get('symbol', None)
            king_of_the_hill_timestamp = coin_data.get('king_of_the_hill_timestamp', None)
            twitter = coin_data.get('twitter', None)
            telegram = coin_data.get('telegram', None)
            website = coin_data.get('website', None)
            created_timestamp = coin_data.get('created_timestamp', None)
            
            if created_timestamp and king_of_the_hill_timestamp:
                delta_minutes = calculate_delta_minutes(created_timestamp, king_of_the_hill_timestamp)
            else:
                delta_minutes = None
            
            if (twitter and "cto" in twitter.lower()) or (telegram and "cto" in telegram.lower()) and delta_minutes and delta_minutes < 4:
                await forward_msg("https://pump.fun/"+str(token_address) +"  HIGH CONVICTION!!!!")
            
            result = {
                'creator': creator,
                'symbol': symbol,
                'king_of_the_hill_timestamp': king_of_the_hill_timestamp,
                'twitter': twitter,
                'telegram': telegram,
                'website': website,
                'delta_minutes': delta_minutes,
                'signal': False,
                'time' : datetime.now()
            }
            print(result['delta_minutes'])
            if   result['delta_minutes'] and result['delta_minutes'] > 0:
                url_balances = f'https://frontend-api.pump.fun/balances/{creator}?limit=50&offset=0'
                headers_balances = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
                    'origin': 'https://pump.fun',
                    'referer': 'https://pump.fun/'
                }
                
                balances_data = await fetch_data_coin(url_balances, headers_balances)
                
                if 'error' in balances_data:
                    print(balances_data['error'])
                    return
                
                # Cari nilai value dari symbol yang didapat dari endpoint pertama
                value = None
                for item in balances_data:
                    if item['symbol'] == symbol:
                        value = item['value']
                        break
                result['value'] = value
                print(result) 
                if value and int(value) < 500:
                    token_store_pump[token_address] = result
            print("String tidak sssssssssssssssssssssssssssssss kata 'asas'")
            current_time = datetime.now()  
            for token in list(token_store_pump.keys()):
                if token_store_pump[token]['time']:
                    if current_time - token_store_pump[token]['time'] > timedelta(minutes=120):
                        del token_store_pump[token]
                else:
                    del token_store_pump[token]
        else:
            print("String tidak mengandung kata 'BABI'")
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================
'''

@client.on(events.NewMessage(chats=["@PumpFun15K"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        pattern = r'Market cap\s*\n\s*`([A-Za-z0-9]+)`'
        match = re.search(pattern, event.message.text)
        if ("Market cap" in event.message.text) and match and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            token_address = match.group(1)
            print(f"CA 15K: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            token_temps[token_address] = waktu_sekarang
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)

                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah buy > 1 SOL: {high_value_buy}\n"
                    f"Jumlah sell > 1 SOL: {high_value_sell}\n"
                    f"Jumlah buy  > 5 SOL: {high_value_buy_5b}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                     

                        
                
                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False


                                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    result += f"https://pump.fun/profile/{user}  {persentase:.2f}%\n"
                    result += f"https://dexscreener.com/solana/{token_address}?maker={user}\n"
                    result += f"--------------------------------------------------------------\n"
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False

                sent = False
                ray= "15K"

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                found_tokens = [token for token in viral_store if token in text_messages.lower()]
                if found_tokens:
                    viral_param = True

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    data = response.json()
                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 50203042087 and data[1]['volume'] > 50203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR  Viral Param PF "+ray)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        await forward_check_x(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                                await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_trend("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================


@client.on(events.NewMessage(chats=["@PumpFun30K"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        pattern = r'Market cap\s*\n\s*`([A-Za-z0-9]+)`'
        match = re.search(pattern, event.message.text)
        if ("Market cap" in event.message.text) and match and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            token_address = match.group(1)
            print(f"CA 35K: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token(token_address)
            token_temps[token_address] = waktu_sekarang

            if all_data_tx and response  and response.status_code == 200:

                #data_paid = response_paid.json()
                #print(data_paid)
                #paid = data_paid.get('paid', 'Unknown')
                print("token adres PF "+token_address)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)

                    # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)

                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah buy > 1 SOL: {high_value_buy}\n"
                    f"Jumlah sell > 1 SOL: {high_value_sell}\n"
                    f"Jumlah buy > 5 SOL: {high_value_buy_5b}\n"
                    f"Jumlah data dengan timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi ketika is_buy: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol_amount untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                     
                    count_i+=1

                result += "Jumlah user dengan signature yang sama dan total sol_amount:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                

                                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    result += f"https://pump.fun/profile/{user}  {persentase:.2f}%\n"
                    result += f"https://dexscreener.com/solana/{token_address}?maker={user}\n"
                    result += f"--------------------------------------------------------------\n"
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False               

                sent = False
                ray= "30K "

                current_time = datetime.now()
                viral_param = False
                text_messages =event.message.text
                found_tokens = [token for token in viral_store if token in text_messages.lower()]
                if found_tokens:
                    viral_param = True

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    data = response.json()
                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        await forward_check_x(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+" #ALR Viral Param PF "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================

'''
@client.on(events.NewMessage(chats=["@PumpFunKingOfTheHill"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print(event.message.text)
        pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"
        match = re.search(pattern, event.message.text)
        if match and not any(substring in  event.message.text for substring in banned) and not any(substring in  event.message.text for substring in banned_wallet):
            token_address = match.group(1)
            print(f"CA KOTH: {token_address}")

            waktu_sekarang = datetime.now()
            all_data_tx =check_tx(token_address)
            response = check_price(token_address)
            #response_paid = check_token2(token_address)
               
            if all_data_tx and response and response.status_code == 200:

                print("token adres PF "+token_address)
                #data_paid = response_paid.json()
                #print(data_paid)
                paid = False
                # Panjang array utama
                array_length = len(all_data_tx)
    
                # Menghitung jumlah buy dan sell
                total_buy = sum(1 for trade in all_data_tx if trade['is_buy'])
                total_sell = sum(1 for trade in all_data_tx if not trade['is_buy'])
                
                # Menghitung jumlah buy dan sell dengan sol_amount lebih dari 1.000.000.000
                high_value_buy = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                high_value_sell = sum(1 for trade in all_data_tx if not trade['is_buy'] and trade['sol_amount'] > 1_000_000_000)
                
                # Menghitung jumlah buy dengan sol_amount lebih dari 5.000.000.000
                high_value_buy_5b = sum(1 for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] > 5_000_000_000)
                
                # Menghitung jumlah data dengan timestamp yang sama
                timestamps = [trade['timestamp'] for trade in all_data_tx]
                timestamp_counts = Counter(timestamps)
                duplicate_timestamps = {timestamp for timestamp, count in timestamp_counts.items() if count > 1}
                filtered_users = [trade for trade in all_data_tx if trade['is_buy'] and trade['sol_amount'] >= 500000000 and trade['timestamp'] in duplicate_timestamps]
                
                # Mendapatkan sol_amount tertinggi ketika is_buy
                max_sol_amount_buy = max((trade['sol_amount'] for trade in all_data_tx if trade['is_buy']), default=None)
                
                # Menghitung total sol_amount untuk setiap user yang is_buy = true
                user_sol_amounts = defaultdict(int)
                user_timestamps = defaultdict(list)
                user_transactions = defaultdict(list)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_sol_amounts[trade['user']] += trade['sol_amount']
                        user_timestamps[trade['user']].append(trade['timestamp'])
                        user_transactions[trade['user']].append(trade['sol_amount'])
                
                # Mengambil 5 user dengan sol_amount tertinggi
                top_users = sorted(user_sol_amounts.items(), key=lambda x: x[1], reverse=True)[:5]

                # Memeriksa kesamaan timestamp antara top 5 users
                timestamp_matches = defaultdict(set)
                for user, _ in top_users:
                    timestamps = user_timestamps[user]
                    for timestamp in timestamps:
                        for other_user, _ in top_users:
                            if other_user != user and timestamp in user_timestamps[other_user]:
                                timestamp_matches[user].add(timestamp)
                                timestamp_matches[other_user].add(timestamp)
                
                # Menentukan apakah ada user yang memiliki kesamaan timestamp lebih dari sekali
                has_multiple_matches = {user: len(matches) > 1 for user, matches in timestamp_matches.items()}
                
                # Mencari user dengan signature yang sama di filtered_users
                signature_counts = defaultdict(int)
                sol_amounts_per_signature = defaultdict(int)
                
                for trade in filtered_users:
                    signature = trade['signature']
                    signature_counts[signature] += 1
                    sol_amounts_per_signature[signature] += trade['sol_amount']
                
                # Mengambil jumlah user dengan signature yang sama dan total sol_amount
                same_signature_users = [(signature, count, sol_amount) for signature, count, sol_amount in zip(signature_counts.keys(), signature_counts.values(), sol_amounts_per_signature.values()) if count > 1]

                # Menghitung total sol_amount dari grup user yang memiliki kesamaan signature dengan minimal 2 atau lebih
                total_sol_amount_grouped = sum(sol_amount for _, _, sol_amount in same_signature_users)


                user_token_amounts = defaultdict(int)
                for trade in all_data_tx:
                    if trade['is_buy']:
                        user_token_amounts[trade['user']] += trade['token_amount']
                    else:
                        user_token_amounts[trade['user']] -= trade['token_amount']
                
                # Mengambil 5 user dengan token_amount tertinggi
                top_token_holders = sorted(user_token_amounts.items(), key=lambda x: x[1], reverse=True)[:5]


                if "**Tool**" in event.message.text:
                    text_temp= event.message.text.split("**Tool**")[0]
                else:
                    text_temp= event.message.text.split("**AD**")[0]
                # Hasil yang akan ditampilkan
                result = (
                    f"https://bullx.io/terminal?chainId=1399811149&address={token_address}\n"
                    f": {text_temp}\n"
                    f"Panjang array utama: {array_length}\n"
                    f"Jumlah total buy: {total_buy}\n"
                    f"Jumlah total sell: {total_sell}\n"
                    f"Jumlah buy > 1 SOL: {high_value_buy}\n"
                    f"Jumlah sell > 1 SOL: {high_value_sell}\n"
                    f"Jumlah buy > 5 SOL: {high_value_buy_5b}\n"
                    f"Jumlah timestamp yang sama: {len(duplicate_timestamps)}\n"
                    f"sol_amount tertinggi: {max_sol_amount_buy / 1_000_000_000:.2f} SOL\n"
                    f"Total sol untuk 5 users tertinggi dengan is_buy=True:\n"
                )
                
                top_user_flag = True
                count_i = 1
                for user, total_sol in top_users:
                    count_x=1
                    total_sol_billion = total_sol / 1_000_000_000
                    if total_sol_billion > 15:
                        top_user_flag = False
                    result += f"{count_i}: {user}\n"
                    result += f"   Total: {total_sol_billion:.2f} SOL\n"
                    for sol_amount in user_transactions[user]:
                        result += f"  {count_x}: {sol_amount / 1_000_000_000:.2f}  SOL\n"
                        count_x +=1
                    count_i+=1
                     

                
                result += "Jumlah user Bot:\n"
                for signature, count, total_sol in same_signature_users:
                    total_sol_billion = total_sol / 1_000_000_000
                    result += f"Jumlah user: {count}, Total sol_amount: {total_sol_billion:.2f} SOL\n"
                    if count > 1:
                        top_user_flag = False
                
                    # Menambahkan hasil pemeriksaan kesamaan timestamp
                result += "\nKesamaan timestamp antara top 5 users:\n"
                for user, has_match in has_multiple_matches.items():
                    if has_match:
                        result += f"{user}: {has_match}\n"
                        top_user_flag = False

                result += "\nTop 5 token holders:\n"
                for user, total_token in top_token_holders:
                    nilai_2 = 1000000000000000
                    # Menghitung persentase
                    persentase = (total_token / nilai_2) * 100
                    result += f"https://pump.fun/profile/{user}  {persentase:.2f}%\n"
                    result += f"https://dexscreener.com/solana/{token_address}?maker={user}\n"
                    result += f"--------------------------------------------------------------\n"
                    if user in banned_wallet or persentase > 12:
                        top_user_flag = False


            
                sent = False
                ray= " KOTH"

                current_time = datetime.now()
                viral_param = False
                found_tokens = [token for token in viral_store if token in event.message.text]
                if found_tokens:
                    viral_param = True
                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)

                if total_sol_amount_grouped / 1_000_000_000 < 1 and max_sol_amount_buy / 1_000_000_000 < 15 and top_user_flag:
                    if token_address in token_temps:
                        waktu_simpan=token_temps[token_address]
                        selisih_waktu = waktu_sekarang - waktu_simpan
                        if selisih_waktu < timedelta(minutes=2):
                            token_volume[token_address] = current_time
                            if viral_param:
                                await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                            await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalFASTLISTING "+ray)
                            await forward_check_x(str(token_address))

                    data = response.json()
                    if sent == False and paid:
                        print("Datsinyall paid 1")
                        print(paid)
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) == 2 and data[0]['volume'] > 40203042087 and data[1]['volume'] > 40203042087 and  data[0]['close'] > data[0]['open'] and  data[1]['close'] > data[1]['open']:
                        print("Datsinyall 1")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump1 "+ray)
                        await forward_check_x(str(token_address))
                    if  sent == False and len(data) > 3 and data[-1]['volume'] > 20203042087 and data[-1]['close'] > data[-1]['open'] and data[-2]['close'] > data[-2]['open'] and data[-3]['close'] > data[-3]['open']:
                        print("Datsinyall 2")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump2 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) <= 4 and len(data) > 2 and  data[0]['volume'] > 10203042087 and data[1]['volume'] > 12203042087 and data[2]['volume'] > 14203042087 :
                        print("Datsinyall 3")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump3 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 5 and data[-1]['volume'] > 15203042087 and data[-2]['volume'] > 7203042087 and data[-1]['close'] > data[-1]['open'] and  data[-2]['close'] > data[-2]['open']  and  data[-3]['close'] > data[-3]['open'] and  data[-4]['close'] > data[-4]['open'] and  data[-5]['close'] > data[-5]['open'] :
                        print("SinyalvolumePump4 ")
                        sent = True
                        token_volume[token_address] = current_time
                        if viral_param:
                            await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                        await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  SinyalvolumePump4 "+ray)
                        await forward_check_x(str(token_address))
                    if sent == False and len(data) >= 14:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[-10:-4])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[-10:-4])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-4:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike1 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
                    if sent == False and len(data) < 14 and len(data) > 2:  # Perlu setidaknya 14 data (10 untuk sideways + 4 untuk spike)
                        # Mengambil harga penutupan (close) dan volume
                        closes = [item['close'] for item in data]
                        volumes = [item['volume'] for item in data]

                        # Analisis kondisi sideways pada 10 data terakhir tanpa 4 data paling akhir
                        sideways_detected = is_sideways(closes[:-2])  # Cek kondisi sideways pada data ke-5 sampai ke-14 dari belakang

                        if sideways_detected:
                            print("Kondisi sideways terdeteksi.")
                            avg_volume = statistics.mean(volumes[:-2])
                            # Deteksi spike volume pada 4 data paling akhir
                            if detect_spike(data[-2:], avg_volume, spike_threshold=3):  # Cek spike pada 4 data paling akhir
                                print("Spike volume terdeteksi pada 4 data paling akhir.")
                                sent = True
                                token_volume[token_address] = current_time
                                if viral_param:
                                    await forward_alert("https://pump.fun/"+str(token_address)+" "+result+"  Viral Param PF "+ray)
                                await forward_msg("https://pump.fun/"+str(token_address)+" "+result+"  Sinyalspike2 "+ray)
                                await forward_check_x(str(token_address))
                            else:
                                print("Tidak ada spike volume pada 4 data paling akhir.")
                        else:
                            print("Kondisi sideways tidak terdeteksi.")
            else:
                print(f"Permintaan gagal dengan status kode {response.status_code}")
            
            token_to_delete = []
            for token_address, waktu_simpan in token_temps.items():
                selisih_waktu = datetime.now() - waktu_simpan
                if selisih_waktu > timedelta(minutes=30):
                    token_to_delete.append(token_address)
    except Exception as e:
        tb = traceback.format_exc()
        print("An error occurred:\n", tb)
        print(f"Error00: {e}")
'''


async def main():
    await client.start()
    print("Client started")
    await asyncio.gather(
        chek_ten_minutes(),
        get_volume(),
        #fetch_and_post_news(),
        client.run_until_disconnected()
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())