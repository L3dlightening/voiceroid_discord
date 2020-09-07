import configparser
import discord
from discord.ext import commands

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

# discordに必要な情報
TOKEN = config.get('discord', 'TOKEN')
# text_id = config.get('channel', 'text_test')
# voice_id = config.get('channel', 'voice_test')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("ログインしました。")

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.event
async def on_voice_state_update(member, before, after):
    alert_channel = discord.utils.get(member.guild.text_channels, name='botテキスト')

    if before.channel is None:
        msg = f'{member.name}が参加しました'
        await alert_channel.send(msg)
    elif after.channel is None:
        msg = f'{member.name}が退出しました'
        await alert_channel.send(msg)
        

bot.run(TOKEN)