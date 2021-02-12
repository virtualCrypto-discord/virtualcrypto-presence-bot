import discord
from discord.ext import tasks
from os import environ
from dotenv import load_dotenv
load_dotenv(verbose=True)

intents = discord.Intents.none()
intents.guilds = True

client = discord.Client(intents=intents)


@tasks.loop(hours=1)
async def set_presence_task():
    await client.wait_until_ready()
    await client.change_presence(
        activity=discord.Game(name=f"/help | {len(client.guilds)}guilds")
    )

set_presence_task.start()


client.run(environ["BOT_TOKEN"])
