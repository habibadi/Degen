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

# Inisialisasi klien Telegram
client = TelegramClient(session_name, api_id, api_hash)

#Tools and Forward messages ================================================================================================================================================

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
        await forward_news_p0(event.message.text+"  #P0")
    except Exception as e:
        print(f"ErrorA: {e}")

# News P0
@client.on(events.NewMessage(chats=["@WatcherGuru"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        await forward_news_p0(event.message.text+"  #P0")
    except Exception as e:
        print(f"ErrorB: {e}")

# News P0
@client.on(events.NewMessage(chats=["@walter_bloomberg"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
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
        await forward_news_p0(event.message.text+"  #P0")
    except Exception as e:
        print(f"ErrorD: {e}")

# News P0
@client.on(events.NewMessage(chats=["@Tree_Alpha_News"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text+"  #P0")
    except Exception as e:
        print(f"ErrorE: {e}")

@client.on(events.NewMessage(chats=["@TwttrToTG_TweetBot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received:")
        print(event.message.text)
        await forward_news_p0(event.message.text+"  #P0")
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
@client.on(events.NewMessage(chats=["@djenbullz"]))  # DJ bulls
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        await forward_msg_tw_bot(event.message.text+"  #sinyallDJJJJ", event.message.media)
        if "Bought" in event.message.text or  "aped" in event.message.text or "degen" in event.message.text or "Degen" in event.message.text or "Play" in event.message.text or "play" in event.message.text or "plays" in event.message.text or "Plays" in event.message.text:
            await forward_msg(event.message.text+"  #sinyallDJJJJ", event.message.media)
    except Exception as e:
        print(f"ErrorI: {e}")


@client.on(events.NewMessage(chats=["@ray_blue_bot"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        #print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd:")
        #print(event.message.text)
        pattern = r"\[DS\]\((https://[^\)]+)\)"

        # Mencari kecocokan dengan pola regex
        match_ca = re.search(pattern, event.message.text)
        if match_ca:
            dex_url = match_ca.group(1)
            #print("New message werfwereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee: "+str(dex_url))
                        
        if ("DjDegen" in event.message.text) and "BUY" in event.message.text and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #DJDegen", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("dj02" in event.message.text) and "BUY" in event.message.text and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #dj02", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif ("DjMain" in event.message.text) and "BUY" in event.message.text and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
            print("New message received:")
            #print(event.message.text)
            await forward_msg(event.message.text+"  #djMain", event.message.media)
            if match_ca:
                dex_url = match_ca.group(1)
                await forward_msg(dex_url)
        elif "BUY" in event.message.text and "WaleCad" in event.message.text and "TRANSFER" not in event.message.text and "transferred" not in event.message.text :
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
                if mc_buy < 80000:
                    await forward_msg_trojan(dex_url)
                if mc_buy < 400000:
                    print("New message receivedsdddddddddddddddddddddddddddddddddddddddddddddddddd: "+str(mc_buy))
                    await forward_msg(event.message.text+"  #Cadbuy", event.message.media)
                    await forward_msg(dex_url)
                else:
                    print("New messagefdghttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt: "+str(mc_buy))
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
            await forward_msg(event.message.text+"  #sinyallDJJJJ", event.message.media)
            #await forward_msg_trojan(event.message.text+"  #sinyallDJJJJ", event.message.media)
    except Exception as e:
        print(f"ErrorK: {e}")

# sinyal dj ===================================================================================================================

# sinyal prefer ==============================================================================================================
@client.on(events.NewMessage(chats=["@preferrichroom"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        sender = await event.get_sender()
        sender_id = sender.id
        sender_username = sender.username
        if sender_username == "elroybandicoot" or sender_username == "elroysadrakh" or sender_username == "limehizel" or sender_username == "captainJedi" or sender_username == "vannightmare" or sender_username == "donRichX" or sender_username == "jojobmnn" or sender_username == "chenzeth" :   
            await forward_rick_bot(event.message.text+" sinyalprefer", event.message.media)
            #print(event.message.text)
            if "grup" in event.message.text or "cto" in event.message.text or "aped" in event.message.text or "play" in event.message.text or "$" in event.message.text or "chads" in event.message.text or "one" in event.message.text or "dj" in event.message.text or "Dj" in event.message.text:
                await forward_trend(event.message.text+"  #sinyalPreferGrup" + str(sender_username) , event.message.media)
    except Exception as e:
        print(f"ErrorL: {e}")

# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=[PeerChannel(user_tesrick)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received: wokwokwokwokwokwokwokwokowk")
        #print(event.message.text)
        await forward_trend(event.message.text+"  #sinyalprefer", event.message.media)
    except Exception as e:
        print(f"ErrorM: {e}")
# sinyal prefer ============================================================================================================== 


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
        for token in list(token_ca.keys()):
            try:
                if datetime.now()  - token_store_pump[token]['time'] > timedelta(minutes=12):
                    #print(token_store_pump[token]['sendingMessage'])
                    url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{token}'
                    headers_dexscreener = {
                        'Cookie': '__cf_bm=ilYYFsMnDWiKGlUT2u9_u7bzz2c.wwtvnSOFneuGvYg-1718214670-1.0.1.1-po6XK.mduhfRi61dChrki9lm7oz3Wna6L2D_QB_qDejnxVBsjaBeKDWXCXv2UlXz4vHR6euE4MDKgYZuF7GMI.kcMHO_tU2RJPPe2Dlhx5k'
                    }

                    dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                    if 'error' in dexscreener_data:
                        print("ASSSSSOOOOOy")
                        print(dexscreener_data['error'])
                        return

                    pairs = dexscreener_data.get('pairs', None)
                    print(token_ca)
                    print(pairs)
                    if pairs:
                        del token_ca[token]
                        pair = pairs[0]  # Ambil pasangan pertama
                        price_change_h24 = pair.get('priceChange', {}).get('h24', None)
                        fdv = pair.get('fdv', None)
                        volume_h24 = pair.get('volume', {}).get('h24', None)
                        txns_h24 = pair.get('txns', {}).get('h24', None)
                        buy = pair.get('txns', {}).get('h24', {}).get('buys', None)
                        sell = pair.get('txns', {}).get('h24', {}).get('sells', None)
                        print("String tidak 222222222222222222222222222222222222222 kata 'ddddas'")
                        print(token_ca)
                        print(pairs)
                        print(price_change_h24)
                        percent_sell = (int(sell)/(int(buy)+int(sell)))*100
                        if float(price_change_h24) > 0 and percent_sell <50 and int(buy) >= 680:
                            result = {
                                'price_change_h24': price_change_h24,
                                'volume_h24': volume_h24,
                                'txns_h24': txns_h24,
                                'fdv': fdv
                            }
                            # Simpan hasil ke token_store_pump
                            result_str = json.dumps(result)
                            store_str = json.dumps(token_store_pump[token], default=datetime_converter)  
                            token_store_pump[token]['signal'] = True
                            if float(fdv) > 100000:
                                convic = 0
                                counts = 0
                                if token in high_count_tokens_5m:
                                    convic += 1
                                if token in high_count_tokens_6m:
                                    convic += 1
                                if token in high_count_tokens:
                                    convic += 1               
                                    counts = high_count_tokens[token]['count']   
                                await forward_msg("https://dexscreener.com/solana/"+token+"   #PUMPFUN_00 #C:"+str(convic)+" Count:"+str(counts))
                                await forward_msg(store_str+" "+result_str+" %: "+str(percent_sell))
                                high_count_tokens_00[token] = datetime.now()
                        else:
                            result = {
                                'price_change_h24': price_change_h24,
                                'volume_h24': volume_h24,
                                'txns_h24': txns_h24
                            }
                            # Simpan hasil ke token_store_pump
                            result_str = json.dumps(result)
                            store_str = json.dumps(token_store_pump[token], default=datetime_converter)  
                            print("https://dexscreener.com/solana/"+token+"   #PUMPFUN_9999")                  
                            #await forward_trend("https://dexscreener.com/solana/"+token+"   #PUMPFUN_00")
                            #await forward_trend(store_str+" "+result_str+" %: "+str(percent_sell))
                            token_store_pump[token]['signal'] = True
                        
            except Exception as e:
                print(f"Error55: {e}")
        await asyncio.sleep(3)


# Fungsi untuk menangani pesan baru
@client.on(events.NewMessage(chats=[PeerChannel(user_check_x)]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        print("New message received: wuwuwuwu")
        #print(event.message.text)
        pattern = r"`(\d+(\.\d+)?[KM]?)%` \| `\$(\d+(\.\d+)?[KM]?)` 🅑 `(\d+)` 🅢 `(\d+)`"
        pattern2 = r'Age: `(\d+)m`'
        pattern3 = r"👀 (\d+)"

        # Mencari menggunakan pola regex
        match_skema = re.search(pattern, event.message.text)
        match_age = re.search(pattern2, event.message.text)
        # Search for the pattern in the text
        match_mata = re.search(pattern3, event.message.text)

        if  "🚨" in event.message.text or "LOW LIQ WARNING" in event.message.text or "Can freeze!" in event.message.text or "Token dipped!" in event.message.text :
            #expired_fifo_queue.popleft()
            print("sssf")
            if len(expired_fifo_queue)>0:
                await asyncio.sleep(6)
                await forward_check_x(str(expired_fifo_queue[0]))
        
        elif match_age and match_skema and match_mata:
            ca_temp=expired_fifo_queue[0]
            #expired_fifo_queue.popleft()
            qty_percent = match_skema.group(1)
            qty_vol = match_skema.group(3)
            qty_buy = match_skema.group(5)
            qty_sell = match_skema.group(6)
            age = match_age.group(1)
            mata = match_mata.group(1)

            if int(age) < 5 and int(mata) > 14 and  int(qty_sell) > 40:
                value_before_percent = ''.join([char for char in qty_percent if char.isdigit() or char in {',', '.','K','M'}])
                if value_before_percent[-1].upper() == 'K':
                    qty_percent1= float(value_before_percent[:-1]) * 1_000
                elif value_before_percent[-1].upper() == 'M':
                    qty_percent1= float(value_before_percent[:-1]) * 1_000_000
                else:
                    qty_percent1= float(value_before_percent) 
            
                value_vol1 = ''.join([char for char in qty_vol if char.isdigit() or char in {',', '.','K','M'}])
                if value_vol1[-1].upper() == 'K':
                    qty_vol1= float(value_vol1[:-1]) * 1_000
                elif value_vol1[-1].upper() == 'M':
                    qty_vol1= float(value_vol1[:-1]) * 1_000_000
                else:
                    qty_vol1= float(value_vol1)

                rug_chance=0
                print(f"rug_chance: {rug_chance}")
                if  ((qty_percent1>80 and qty_vol1>10000) or qty_vol1>35000) or qty_vol1>500000:
                    if "💊" in event.message.text:
                        await forward_trend("https://dexscreener.com/solana/"+ca_temp+"?maker=CoS7AcV6cHsD8ReZysJ86tNvF462TNhGdZV4VkNqM3Ne  #vol="+str(qty_vol1)+" %="+str(qty_percent1)+" B="+str(qty_buy)+" S="+str(qty_sell)+" M="+str(mata)+" rug="+str(rug_chance)+" #PUMPFUN" )
                    else:
                        await forward_trend("https://dexscreener.com/solana/"+ca_temp+"?maker=CoS7AcV6cHsD8ReZysJ86tNvF462TNhGdZV4VkNqM3Ne  #vol="+str(qty_vol1)+" %="+str(qty_percent1)+" B="+str(qty_buy)+" S="+str(qty_sell)+" M="+str(mata)+" rug="+str(rug_chance)+" #NON")

            print("f")
            if len(expired_fifo_queue)>0:
                await asyncio.sleep(6)
                await forward_check_x(str(expired_fifo_queue[0]))
        
        else:
            #expired_fifo_queue.popleft()
            print("sssf")
            if len(expired_fifo_queue)>0:
                await asyncio.sleep(6)
                await forward_check_x(str(expired_fifo_queue[0]))
                    
    except Exception as e:
        print(f"Error33: {e}")

# ricky 5 menit awal ============================================================================================================== 



# get volume ============================================================================================================== 
url = 'https://api.solscan.io/v2/account/token/txs'
params = {
    'address': 'AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS',
    'limit': '40',
    'offset': '0',
    'account_type': 'non-existence',
    'change_type': 'dec'
}
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,ms;q=0.7',
    'cookie': '_ga=GA1.1.1552685285.1703187686; amp_1adb3b=ewmgcpLztfynKaJxQoFPW3...1hpvuj7s3.1hpvuj7s3.c.0.c; cf_clearance=rgPc01TXz7nXZPfbEIVM.K95obk39YycLu41gmri4b8-1719330805-1.0.1.1-Qn2kuR5Oz0JT2M4lD7Lf6OzBhlNwoMzEkqbbkhfDj7H.LRYF2_2tNsUElr1eMhRuuVYpyPDvU23bseLMnSOyEg; _ga_PS3V7B7KV0=GS1.1.1719342728.120.1.1719342774.0.0.0',
    'origin': 'https://solscan.io',
    'priority': 'u=1, i',
    'referer': 'https://solscan.io/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'sol-aut': 'kgh7fF6nUhEcDGlB9dls0fKaN4mOYUS-0AjKz-2r',
    'token': '',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

}





# Penyimpanan token_address dan waktu terakhir diperbarui
token_store = {}
# Penyimpanan token_address dengan count > 10 dan waktu ditambahkannya
high_count_tokens = {}

token_store_pump = {}

high_count_tokens_5m = {} 

high_count_tokens_6m = {}

high_count_tokens_00 = {}


token_ca = {}

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
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await asyncio.sleep(30)
                current_time = datetime.now()    
                # Fetch data from API
                data = await fetch_data(session)
                #print(data)
                if data.get('success') and 'data' in data and 'tx' in data['data']:
                    transactions = data['data']['tx']['transactions']
                    new_tokens = set()
                    current_date = datetime.now() 
                    for transaction in transactions:
                        change = transaction.get('change', {})
                        token_address = change.get('tokenAddress')
                        change_amount = change.get('changeAmount', 0)
                        decimals = change.get('decimals', 0)
                        block_time = change.get('blockTime')
                        if token_address and token_address != 'So11111111111111111111111111111111111111112' and str(change_amount).startswith('-'):
                            new_tokens.add(token_address)
                            url_dexscreener = f'https://api.dexscreener.com/latest/dex/tokens/{token_address}'
                            headers_dexscreener = {
                                'Cookie': '__cf_bm=ilYYFsMnDWiKGlUT2u9_u7bzz2c.wwtvnSOFneuGvYg-1718214670-1.0.1.1-po6XK.mduhfRi61dChrki9lm7oz3Wna6L2D_QB_qDejnxVBsjaBeKDWXCXv2UlXz4vHR6euE4MDKgYZuF7GMI.kcMHO_tU2RJPPe2Dlhx5k'
                            }
                            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)
                            if 'error' in dexscreener_data:
                                print("ASSSSSOOOOOy")
                                print(dexscreener_data['error'])
                            pairs = dexscreener_data.get('pairs', None)                

                            if token_address not in token_store:
                                token_store[token_address] = {'last_seen': current_date, 'count': 1, 'block_time': block_time}
                                #print(token_ca)
                                #print(pairs)
                                current_time = time.time()
                                result = {}
                                if pairs:
                                    for pair in dexscreener_data["pairs"]:
                                        pair_created_at = pair["pairCreatedAt"] / 1000  # convert to seconds
                                        created_at_datetime = datetime.fromtimestamp(pair_created_at, tz=timezone.utc)
                                        fdv_temp = 100000
                                        liq_temp = 99
                                        if 'fdv' in pair:
                                            fdv_temp = pair["fdv"]
                                        if 'liquidity' in pair:
                                            liq_temp = pair["liquidity"]["usd"]
                                        token_store[token_address] = {'last_seen': current_date, 'count': 1, 'block_time': block_time, 'createdTime': pair_created_at, 'array_time' : [block_time] , 'fdv' : fdv_temp  }
                                        #print(current_time - pair_created_at)
                                        if pair_created_at > 0 and (current_time - pair_created_at) <= 300:  # 5 minutes in seconds
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
                                            if (pair["priceChange"]["h24"] > 0  and 'fdv' in pair and liq_temp > 200000 and pair["fdv"] < 50000000) :
                                                await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_200k")
                                                await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                await forward_check_x(token_address)
                                            elif pair["priceChange"]["h1"] > 15 and (abs(change_amount)/(10 ** decimals))*float(pair["priceUsd"]) > 1000 and token_address not in  high_count_tokens and liq_temp > 20000 :
                                                convic = 0
                                                if token_address in high_count_tokens_6m:
                                                    convic += 1
                                                if token_address in high_count_tokens_5m:
                                                    convic += 1
                                                if token_address in high_count_tokens_00:
                                                    convic += 1
                                                high_count_tokens[token_address] = {'block_time': current_date, 'post': False, 'count': 0 }
                                                counts = high_count_tokens[token_address]['count']
                                                await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                            elif pair["priceChange"]["h24"] > 10 and liq_temp > 100000:
                                                await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA="+str(result_str)+" #PUMPFUN_11")
                                                await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                                               
                            elif token_address in token_store and block_time > token_store[token_address]['block_time']:
                                if pairs:
                                    for pair in dexscreener_data["pairs"]:
                                        fdv_temp = 100000
                                        liq_temp = 99
                                        price = 0
                                        if 'fdv' in pair:
                                            fdv_temp = pair["fdv"]
                                        if 'liquidity' in pair:
                                            liq_temp = pair["liquidity"]["usd"]
                                        if 'priceUsd' in pair:
                                            price = pair["priceUsd"]
                                        
                                        if pair["priceChange"]["h1"] > 15 and (abs(change_amount)/(10 ** decimals))*float(price) > 1000 and liq_temp > 20000 :
                                            convic = 0
                                            if token_address in high_count_tokens_6m:
                                                convic += 1
                                            if token_address in high_count_tokens_5m:
                                                convic += 1
                                            if token_address in high_count_tokens_00:
                                                convic += 1

                                            if token_address not in high_count_tokens:
                                                high_count_tokens[token_address] = {'block_time': current_date, 'post': False, 'count': 0 }
                                            else:
                                                high_count_tokens[token_address]['block_time'] = current_date
                                                high_count_tokens[token_address]['post'] = False
                                                if 'count' not in token_store[token_address]:
                                                    high_count_tokens[token_address]['count'] = 0
                                                else:
                                                    high_count_tokens[token_address]['count'] += 1
                                            counts =high_count_tokens[token_address]['count']
                                            if token_address not in  high_count_tokens:
                                                await forward_msg("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                await forward_msg("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
                                            else:
                                                await forward_trend("https://dexscreener.com/solana/"+token_address+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS  #DATA= #PUMPFUN_1000USD #C:"+str(convic)+" Count:"+str(counts))
                                                await forward_trend("https://birdeye.so/find-trades/"+token_address+"?chain=solana")
        
                                
                                token_store[token_address]['last_seen'] = current_date
                                token_store[token_address]['count']= 0
                                token_store[token_address]['block_time'] = block_time
                                if 'array_time' not in token_store[token_address]:
                                    token_store[token_address]['array_time'] = []
                                token_store[token_address]['array_time'].append(block_time)
                               
                    # Simpan token_address yang count kemunculan lebih dari 10 ke dalam satu variabel dan catat waktu ditambahkannya
                    tokens_with_high_count = [token for token, data in token_store.items() if data['count'] > 10]
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
                                await forward_msg("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
                            else:
                                await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trends5Menit #C:"+str(convic)+" Count:"+str(counts))
                                await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana #trends5Menit")
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
                                'Cookie': '__cf_bm=ilYYFsMnDWiKGlUT2u9_u7bzz2c.wwtvnSOFneuGvYg-1718214670-1.0.1.1-po6XK.mduhfRi61dChrki9lm7oz3Wna6L2D_QB_qDejnxVBsjaBeKDWXCXv2UlXz4vHR6euE4MDKgYZuF7GMI.kcMHO_tU2RJPPe2Dlhx5k'
                            }

                            dexscreener_data = await fetch_data_coin(url_dexscreener, headers_dexscreener)

                            if 'error' in dexscreener_data:
                                print("ASSSSSOOOOOy")
                                print(dexscreener_data['error'])

                            pairs = dexscreener_data.get('pairs', None)
                            #print(token_ca)
                            #print(pairs)
                            print("AAA")
                            if pairs:
                                liq = 0
                                pair = pairs[0]  # Ambil pasangan pertama
                                price_change_h24 = pair.get('priceChange', {}).get('h1', None)
                                liq = pair.get('liquidity', {}).get('usd', None)
                                if price_change_h24 > 10 and liq:
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
                                        if token not in high_count_tokens_6m:
                                            await forward_msg("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trensPer6Menit #C:"+str(convic)+" Count:"+str(counts))
                                            await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana "+str(token_store[token]['fdv']))
                                        else:
                                            await forward_trend("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trensPer6Menit #C:"+str(convic)+" Count:"+str(counts))
                                            await forward_trend("https://birdeye.so/find-trades/"+token+"?chain=solana "+str(token_store[token]['fdv']))
                                        high_count_tokens_6m[token] = current_date
                                        print("UHUHU")
                        
                        if token not in new_tokens:
                            if (current_date - token_store[token]['last_seen']) > timedelta(minutes=120):
                                del token_store[token]

                    # Print dan simpan token_address yang count kemunculan lebih dari 10
                    for token in high_count_tokens:
                        if high_count_tokens[token]['post'] == False and high_count_tokens[token]['count'] > 2:
                            convic = 0
                            if token_address in high_count_tokens_6m:
                                convic += 1
                            if token_address in high_count_tokens_5m:
                                convic += 1
                            if token_address in high_count_tokens_00:
                                convic += 1       
                            await forward_msg("https://dexscreener.com/solana/"+token+"?maker=AD65fgYti96iSSzSPaNazV9Bs29m7JbNomGjG4Cp5WFS #trendsCount1000USD #C:"+str(convic)+" #Count:"+str(high_count_tokens[token]['count']))
                            await forward_msg("https://birdeye.so/find-trades/"+token+"?chain=solana #trends")
                            high_count_tokens[token]['post'] = True
                    
                    # Hapus token dari penyimpanan setelah lebih dari satu jam
                    tokens_to_remove1 = [token for token, value in high_count_tokens.items() if current_date - value['block_time'] > timedelta(minutes=30)]
                    for token in tokens_to_remove1:
                        del high_count_tokens[token]
                    
                    tokens_to_remove2 = [token for token, time_added in high_count_tokens_5m.items() if current_date - time_added > timedelta(minutes=30)]
                    for token in tokens_to_remove2:
                        del high_count_tokens_5m[token]

                    tokens_to_remove3 = [token for token, time_added in high_count_tokens_6m.items() if current_date - time_added > timedelta(minutes=30)]
                    for token in tokens_to_remove3:
                        del high_count_tokens_6m[token]

            except Exception as e:
                    tb = traceback.format_exc()
                    print("An error occurred:\n", tb)
                    print(f"Error11: {e}")

#=================================================================================================================================



# waktu di pumpfun ===================================================================================================================

'''
@client.on(events.NewMessage(chats=["@pumpfunnewlistingalerts"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        current_time = datetime.now()   
        # Regex untuk mencari token address setelah "🆕**Mint:**"
        pattern = r"🆕\*\*Mint:\*\* `([^`]+)`"
        # Mencari token address menggunakan regex
        match = re.search(pattern, event.message.text)
        if "NEW KING OF THE HILL IN TOWN" in event.message.text and match:
            print(event.message.text)
            token_address = match.group(1)
            if token_address in token_store_pump:
                token_store_pump[token_address]['block_time'] = current_time - token_store_pump[token_address]['last_seen']
                token_store_pump[token_address]['last_seen'] = current_time
                print(f"Error: {str(token_store_pump)}")
                            #await forward_msg(event.message.text , event.message.media)

    except Exception as e:
        print(f"Error: {e}")

@client.on(events.NewMessage(chats=["@PumpFunNewPools"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        current_time = datetime.now()   
        pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"
        match = re.search(pattern, event.message.text)
        if "NEW PUMP FUN POOL" in event.message.text and match:
            #print(event.message.text)
            for token in list(token_store_pump.keys()):
                if current_time - token_store_pump[token]['last_seen'] > timedelta(minutes=30):
                    del token_store_pump[token]
            token_address = match.group(1)
            current_time = datetime.now()
            # Waktu terakhir terlihat (misalnya 150 menit yang lalu)
            last_seen_time = current_time - timedelta(minutes=150)
            # Menghitung selisih waktu
            time_difference = current_time - last_seen_time
            token_store_pump[token_address] = {'last_seen': current_time, 'block_time': time_difference, 'sendingMessage': False}
    except Exception as e:
        print(f"Error: {e}")
'''
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


    
@client.on(events.NewMessage(chats=["@PumpFunRaydium"]))  # Ganti dengan nama grup Anda
async def handle_new_message(event):
    try:
        pattern = r"🔗 \*\*MINT CA\*\*\n`([^`]+)`"
        match = re.search(pattern, event.message.text)
        if "RAYDIUM POOL DEPLOYED" in event.message.text and match:
            token_address = match.group(1)
            print(f"CA: {token_address}")

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
            if  result['delta_minutes'] > 0:
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
                if int(value) < 500:
                    token_store_pump[token_address] = result
                    token_ca[token_address] = {'dex': False}
            print("String tidak sssssssssssssssssssssssssssssss kata 'asas'")
            print(token_ca)
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
        print(f"Error00: {e}")
# waktu di pumpfun ===================================================================================================================

@client.on(events.NewMessage(chats=["@SOLWalletTrackerBot"]))  # DJ bulls
async def handle_new_message(event):
    try:
        print("New message received:")
        #print(event.message.text)
        #await forward_msg_tw_bot(event.message.text+"  #sinyallDJJJJ", event.message.media)
        #if "Bought" in event.message.text or "degen" in event.message.text or "Degen" in event.message.text or "Play" in event.message.text or "play" in event.message.text or "plays" in event.message.text or "Plays" in event.message.text:
        #    await forward_msg(event.message.text+"  #sinyallDJJJJ", event.message.media)
    except Exception as e:
        print(f"ErrorO: {e}")


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