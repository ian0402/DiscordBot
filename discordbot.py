import discord
from discord.ext import commands
import asyncio
import yaml

intents = discord.Intents.all()

TOKEN = #TOKEN

bot = commands.Bot(command_prefix='/', intents=intents)

# 出力設定の読み込み
with open('config.yaml') as f:
    yml = yaml.safe_load(f)
debug_channel_id = yml['debugchannel']

# 起動処理
@bot.event
async def on_ready():
    print('ログインしました')
    await bot.tree.sync()
    debug_channel = bot.get_channel(debug_channel_id)
    await debug_channel.send('restarted')

# 各サーバーの出力チャンネルの設定コマンド
@bot.tree.command()
async def setoutput(interaction: discord.Interaction):
    """Set channel to send message"""
    with open('config.yaml', 'w') as f:
        newconf = {interaction.guild_id: interaction.channel_id}
        yml['outputchannel'].update(newconf)
        yaml.dump(yml, f)
    await interaction.response.send_message('Done')

# 通話開始の通知
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != None:
        if after.channel == None or len(before.channel.members) == len(after.channel.members):
            return
    bot_count = 0
    for x in after.channel.members:
        if x.bot:
            bot_count += 1

    if (len(after.channel.members) - bot_count == 1):
        try:
            output_channel = bot.get_channel(yml['outputchannel'][after.channel.guild.id])
        except:
            output_channel = after.channel.guild.text_channels[0]
        # await out_channel.send(f'{len(after.channel.members)},{after.channel.members},{HowManyBots(after.channel)}')
        await output_channel.send(f'{member.display_name}が{after.channel.name}で通話を開始しました！')

bot.run(TOKEN)
