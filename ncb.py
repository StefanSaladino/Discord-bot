import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()

# Retrieve token from token.env file
with open('token.env', 'r') as file:
    TOKEN = file.read().strip()

# Retrieve guild name from guild.env file
with open('guild.env', 'r') as file:
    GUILD_NAME = file.read().strip()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD_NAME)
    if guild:
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    else:
        print(f'Bot is not connected to the guild: {GUILD_NAME}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'nice' in message.content.lower():
        await message.channel.send('NICE COCK!')

    await bot.process_commands(message)

bot.run(TOKEN)

