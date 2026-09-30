import discord
from discord.ext import commands

intents = discord.Intents.all();
bot = commands.Bot("~", intents=intents)

@bot.event
async def on_ready():
    print("-- JanjoTALK no ar!!! --")

@bot.command()
async def odiar(ctx:commands.Context):
    name = ctx.author.display_name
    await ctx.reply(f"Obrigado, {name}, por odiar a deturpadora da paz")
    # Anotação científica: caso eu trocasse o "ctx.reply" por "ctx.send", o bot mandaria a mensagem sem dar reply.

bot.run("MTU1NDkxNDc5NjIzNzg4NTU5MQ.GuFRIY.PZhK0tLv4PPbOkwtLtDYzd3zCfFXZMRWrYjrpk")
