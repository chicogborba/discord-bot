import discord
import os


intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.guild_messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")


client.run(os.getenv("TOKEN"))


# 		GatewayIntentBits.Guilds,
# 		GatewayIntentBits.GuildMessages,
# 		GatewayIntentBits.MessageContent,
# 		GatewayIntentBits.GuildMembers,
