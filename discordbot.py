import configparser
from discord.ext import commands

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

# discordに必要な情報
TOKEN = config.get('discord', 'TOKEN')
text_id = config.get('channel', 'text_test')
voice_id = config.get('channel', 'voice_test')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("ログインしました。")

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

# move!!!!
'''
@bot.event
async def on_voice_state_update(before, after):
    if before.voice_channel is None:
        alert_channel = bot.get_channel(text_id)
        name = after.name
        msg = f'{name}が参加しました。'
        await alert_channel.send(msg)
'''

bot.run(TOKEN)