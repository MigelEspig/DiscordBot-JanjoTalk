import discord
from discord.ext import commands
from tokenBot import runBot

intents = discord.Intents.all()
bot = commands.Bot("~", intents=intents)

@bot.event
async def on_ready():
    #Comando confirmando o início do bot (possessão demoníaca)
    print("-- JanjoTALK no ar!!! --")

@bot.command()
async def odiar(ctx:commands.Context):
    # Comando para quando alguém escrever '~odiar', o bot retorna uma mensagem gratificante.
    name = ctx.author.display_name
    await ctx.reply(f"Obrigado, {name}, por odiar a deturpadora da paz")
    # Anotação científica: caso eu trocasse o "ctx.reply" por "ctx.send", o bot mandaria a mensagem sem dar reply.

@bot.command()
async def falar(ctx:commands.Context,*, text):
    # Comando teste temporário para repetir mensagem do remetente
    await ctx.send(text)


# COMANDOS RELACIONADOS À CALLS:
@bot.command()
async def entrar(ctx):
    # Comando para entrar na chamada que o remetente está
    if ctx.author.voice is None:
    # verifica se o remetente está em uma chamada
        await ctx.send("Você precisa estar em um canal de voz.")
        return

    canal = ctx.author.voice.channel

    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(canal)
    else:
        await canal.connect()

    await ctx.send(f"Entrei em **{canal.name}**!")


@bot.command()
async def sair(ctx):
    # Comando para sair da chamada que o remetente está/estava
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send("Saí da call.")
    else:
        await ctx.send("Não estou em nenhuma call.")

@bot.command()
async def tocar(ctx):
    # Comando para tocar um arquivo .mp3 da pasta nativa do programa
    if not ctx.author.voice:
    # verifica se o remetente está em uma chamada
        await ctx.send("Você precisa estar em uma call!")
        return

    canal = ctx.author.voice.channel

    if ctx.voice_client is None:
        await canal.connect()

    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    source = discord.FFmpegPCMAudio(r"C:\Users\Henri\Documents\GitHub\DiscordBot-JanjoTalk\Sounds\Musica2.mp3")
    await ctx.send("Tocando áudio!")
    ctx.voice_client.play(source)

runBot()

# bot.run("")
# INSERIR TOKEN DE ACESSO DO BOT PARA LIGÁ-LO
