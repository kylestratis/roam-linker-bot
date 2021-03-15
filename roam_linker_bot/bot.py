"""
This is a Discord bot that replies to any messages that have a Roam blockref with a URL to that blockref.
"""

# Standard library imports
import os
import re

# Third-party imports
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
ROAM_WORKSPACE = os.getenv("ROAM_WORKSPACE")

intents = discord.Intents(messages=True)
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    blockrefs = re.findall(r"\(\(([\w-]+?)\)\)", message.content)
    for blockref in blockrefs:
        url = f"https://roamresearch.com#/app/{ROAM_WORKSPACE}/page/{blockref}"
        await message.channel.send(url)


client.run(TOKEN)
