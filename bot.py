import os
import discord
import config
import quote
from dotenv import load_dotenv

# A Discord bot that returns a random inspirational quote or an Games Done Quick style donation message.

# Load the file that contains Discord-related credentials
load_dotenv()   
TOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")

# Represents connection to Discord
client = discord.Client()

@client.event
async def on_ready():
    # For the user to see that the bot has connected successfully to the server.
    for guild in client.guilds:

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    # Listen to the messages and react accordingly if a bot command is called.
    # Ignore messages sent by the bot
    if message.author == client.user:
        return
    
    if message.content.startswith(f"{config.PREFIX}{config.QUOTE_COMMAND}"):
        motivational_quote = quote.get_motivated()
        msg = f'{motivational_quote["text"]}\n-{motivational_quote["author"]}'
        await message.channel.send(f"```{msg}```")
    
    if message.content.startswith(f"{config.PREFIX}{config.GDQ_COMMAND}"):
        msg = quote.get_quote()
        await message.channel.send(f"```{msg}```")

client.run(TOKEN)
