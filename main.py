import configparser
import discord
from discord.ext import commands
import datetime

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

# discordに必要な情報
TOKEN = config.get('discord', 'TOKEN')
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("ログインしました。")

@bot.event
async def on_voice_state_update(member, before, after):
    alert_channel = discord.utils.get(member.guild.text_channels, name='botテキスト')

    if before.channel is None:
        msg = f'{member.name}が参加しました'
        await alert_channel.send(msg)
    elif after.channel is None:
        msg = f'{member.name}が退出しました'
        await alert_channel.send(msg)

@bot.command()
async def speak(ctx, text):
    dt_now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    with open(f'./text/{dt_now}_voice.txt', mode='w', encoding='utf_8') as f:
        f.write(text)

    print(dt_now)

    await ctx.send(text), text
        


bot.run(TOKEN)