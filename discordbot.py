from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# インストールした discord.py を読み込む
import discord
import random
import csv
import asyncio

# 接続に必要なオブジェクトを生成
client = discord.Client()
#ブキ読み込み
with open('./Splatoon2weapons.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    weapons = []
    for row in reader:
        weapons += row
f.close()
#名前読み込み
with open('./parts.txt', 'r', encoding='UTF-8') as f:
    parts = [s.strip() for s in f.readlines()]
f.close()
with open('./parts2.txt', 'r', encoding='UTF-8') as f:
    parts2 = [s.strip() for s in f.readlines()]
f.close()

voice = None
player = None

#豚彦用
ramen_size = ['ミニ','小','大']
buta = ['ラーメン','ぶた']
siru = ['','汁なし']
ninniku = ['','ニンニク少し','ニンニク','ニンニクマシマシ']
yasai= ['ヤサイ少なめ','','ヤサイマシ','ヤサイマシマシ']
seabura = ['','アブラマシ','アブラマシマシ']
karame = ['','カラメ','カラカラ']

#Apex用
with open('./apex_legends.txt', 'r', encoding='UTF-8') as f:
    apexlegends = [s.strip() for s in f.readlines()]
f.close()
with open('./apex_weapons.txt', 'r', encoding='UTF-8') as f:
    apexweapons = [s.strip() for s in f.readlines()]
f.close()
#音声ファイル
ikuokamoto = discord.FFmpegPCMAudio('./ikuokamoto.mp3')
ikisugiokamoto = discord.FFmpegPCMAudio('./ikisugiokamoto.mp3')
dokaben = discord.FFmpegPCMAudio('./dokaben.mp3')
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global voice, player
    msg = message.content
    if message.author.bot:
        return
    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/spla':
        size = len(weapons)
        i = random.randint(0,size-1)
        await message.channel.send('おめぇのブキは、' + weapons[i] + 'だな！')
        
    if message.content == '/apex':
        deletes = []
        for num in range(1,4):
            i = random.randint(0,len(apexlegends)-1)
            j = random.randint(0,len(apexweapons)-1)
            k = random.randint(0,len(apexweapons)-1)
            #リストからレジェンドを削除（被らないように）
            legend = apexlegends.pop(i)
            await message.channel.send(str(num) + "人目は、" + legend + "で" + apexweapons[j] + "と" + apexweapons[k] + "だな！")
            #削除されたレジェンドのリスト
            deletes.append(legend)
        #終わった後にまた元のリストに戻す
        apexlegends.extend(deletes)
        
    if message.content == '/myname':
        i = random.randint(0,len(parts))
        j = random.randint(0,len(parts)-1)
        k = random.randint(0,len(parts2)-1)
        if i == len(parts):
            await message.channel.send('おめぇの名前は、性器絶頂チンポギアだな！')
        else:
            await message.channel.send('おめぇの名前は、' + parts[i] + parts[j] + parts2[k] + 'だな！')

    if message.content == '/changename':
        i = random.randint(0,len(parts))
        j = random.randint(0,len(parts)-1)
        k = random.randint(0,len(parts2)-1)
        name = ""
        if i == len(parts):
            name = '性器絶頂チンポギア'
        else:
            name = parts[i] + parts[j] + parts2[k]
            
        await message.channel.send("おめぇの名前は、" + name + "だな！")
        await message.author.edit(nick=name)

    if message.content == '/showparts':
        for i in range(len(parts)):
            await message.channel.send(parts[i])
        
    if message.content == 'イク岡本':
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        vc = await message.author.voice.channel.connect()
        #再生する
        vc.play(ikuokamoto)
        #切断する
        await asyncio.sleep(2)
        await message.guild.voice_client.disconnect()
        
    if message.content == 'イキスギ岡本':
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        vc = await message.author.voice.channel.connect()
        #再生する
        vc.play(ikisugiokamoto)
        #切断する
        await asyncio.sleep(2)
        await message.guild.voice_client.disconnect()

    if message.content == '/bakadon':
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        # ボイスチャンネルに接続する
        vc = await message.author.voice.channel.connect()
        #GIFを送信する
        file = discord.File("./bakadon.gif", filename="bakadon.gif")
        await message.channel.send(file=file)
        await asyncio.sleep(1)
        #再生する
        vc.play(dokaben)
        #切断する
        await asyncio.sleep(6)
        await message.guild.voice_client.disconnect()
        
    if message.content == '/butahiko':
        i = random.randint(0,len(ramen_size)-1)
        j = random.randint(0,len(buta)-1)
        k = random.randint(0,len(siru)-1)
        l = random.randint(0,len(ninniku)-1)
        m = random.randint(0,len(yasai)-1)
        n = random.randint(0,len(seabura)-1)
        o = random.randint(0,len(karame)-1)
        await message.channel.send('おめぇのラーメンは、' + ramen_size[i] + buta[j] + siru[k] + ninniku[l] + yasai[m] + seabura[n] + karame[o] + 'だな！')
        
    if message.content == 'ニンニク入れますか?' or message.content == 'ニンニク入れますか？':
        l = random.randint(0,len(ninniku)-1)
        m = random.randint(0,len(yasai)-1)
        n = random.randint(0,len(seabura)-1)
        o = random.randint(0,len(karame)-1)
        await message.channel.send('俺のラーメンは、' + ninniku[l] + yasai[m] + seabura[n] + karame[o] + 'だな！')

# Botの起動とDiscordサーバーへの接続
client.run(token)
#808670943962464276
