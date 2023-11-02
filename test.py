import discord
import asyncio

intents = discord.Intents.all()

TOKEN = 'ODI5MjQ4ODMxMzg0MzIyMDQ4.GW02IZ.CHapRkkSE_sn8y5lTdmZw_AFvZrV5n-CkaS6PM'    # 実験

client = discord.Client(intents=intents)


async def main():
    @client.event
    async def discord():
        out_channel: discord.TextChannel = client.get_channel(800417185835122721)
        print('ログインしました')
        await out_channel.send('restarted')

    # start the client
    async with client:
        await client.start(TOKEN)

asyncio.run(main())
