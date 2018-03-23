import discord
import asyncio
import botMessages
import botSecret
import requests
from os import environ

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
#!test -A test command for the bot
    if message.content.startswith('!test'):
        await client.send_message(message.channel, botMessages.Test)

#!cat -send a random image of a cat
    if message.content.startswith('!cat'):
        response = requests.get('http://thecatapi.com/api/images/get', stream=True)
        with open ('cat.png', 'wb') as f:
            f.write(response.raw.read())
        with open('cat.png', 'rb') as f:
            await client.send_file(message.channel, f, filename='cat.png', content='Please, enjoy this cat.')

#Run locally
#client.run(botSecret.Token)

#Run on Heroku. Defined under Settings->Config Vars
client.run(environ.get('BOT_TOKEN'))