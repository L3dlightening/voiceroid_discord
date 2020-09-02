import discord
import configparser

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

# discordに必要な情報
TOKEN = config.get('discord', 'TOKEN')
text_id = config.get('channel', 'text_test')
voice_id = config.get('channel', 'voice_test')

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

# ToDo 動かないヨ
@client.event
async def on_voice_state_update(member, before, after):
    if after.server.id == voice_id:
        channel = client.get_channel(text_id)
        text = member.name + 'さんが参加しました。'
        await channel.send(text)


client.run(TOKEN)