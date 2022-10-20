import discord
import requests
import json
import os
import random
from pokemon import Pokemon


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.guild_messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# Send a embed message with a random Pokemon name
async def pokemon_command(message):
    pokemon = Pokemon()
    embed = discord.Embed(
        title="Name: " + pokemon.name,
        description="Type: " + pokemon.type,
        color=pokemon.color,
    )
    embed.set_image(url=pokemon.image)
    # set image size
    await message.channel.send(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!h"):
        await message.channel.send("Hello!")

    if message.content.startswith("!p"):
        await pokemon_command(message)


client.run(os.getenv("TOKEN"))
