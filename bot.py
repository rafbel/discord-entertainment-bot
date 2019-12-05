from crawler import crawl
import discord

TOKEN = 'YOUR TOKEN'
client = discord.Client()

@client.event
async def on_ready():
    print('I am ready to Rock and Roll')

@client.event
async def on_message(message):
    if message.content == '$crawl':
        links = crawl()

        for link in links:
            await message.channel.send(link)

client.run(TOKEN)

crawl()