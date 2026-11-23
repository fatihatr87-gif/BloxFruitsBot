import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Blox Fruits Bot is online! 🍎")

bot.run("YOUR_BOT_TOKEN")
