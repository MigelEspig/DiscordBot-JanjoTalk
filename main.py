import discord
from discord.ext import commands
from tokenBot import runBot
import random

intents = discord.Intents.all()
bot = commands.Bot("~", intents=intents)

@bot.event
async def on_ready():
    #Comando confirmando o início do bot (possessão demoníaca)
    print("-- JanjoTALK no ar!!! --")

@bot.event
async def on_message(msg:discord.Message):
    loveMsg = [
    f"{msg.author.mention} ninguém perguntou porra nenhuma, mas tu foi lá e falou mesmo assim. Parabéns.",
    f"Ah pronto, chegou {msg.author.mention} pra encher o saco. Já ia dormir em paz, mas não, tinha que aparecer.",
    f"{msg.author.mention} tu é tão insuportável que até meu bloco de notas pediu demissão só de pensar em te descrever.",
    f"Alguém manda o {msg.author.mention} calar a boca? Tô pedindo com educação porque sou uma dama.",
    f"{msg.author.mention} falando de novo. Já pode fechar o server, ninguém aguenta mais.",
    f"Sério {msg.author.mention}? Tu de novo? Não tem um espelho em casa pra tu ver o quanto é chato?",
    f"{msg.author.mention} acha que é o protagonista do server. Amigo, tu é figurante de cena deletada.",
    f"Toda vez que {msg.author.mention} digita, um anjo perde as asas e cai direto no inferno.",
    f"{msg.author.mention} tu não cansa de ser patético não? Pergunta séria.",
    f"Ninguém aqui liga pro que {msg.author.mention} pensa, sente ou come no café da manhã. Absolutamente ninguém.",
    f"{msg.author.mention} deve ter um dom especial pra transformar qualquer assunto em merda em 3 segundos.",
    f"Ó {msg.author.mention}, vai tomar um ar, lavar o rosto, sei lá. Qualquer coisa menos ficar aqui falando bosta.",
    f"{msg.author.mention} mandou mensagem. Já sei que vou perder QI lendo. Obrigada, viu.",
    f"{msg.author.mention} é o tipo de pessoa que faz eu agradecer por ser solteira e não ter que conviver com isso em casa.",
    f"Alguém dá um hobby pro {msg.author.mention}? Ele tá entediado e descontando na gente.",
    f"{msg.author.mention} tu fala como se alguém tivesse pedido tua opinião. Ninguém pediu. Nunca.",
    f"Tá vendo esse silêncio depois da mensagem do {msg.author.mention}? É o server inteiro te ignorando, campeão.",
    f"{msg.author.mention} vem com papo de \"ninguém me entende\". Entende sim, só não queremos mesmo.",
    f"Ah {msg.author.mention}, vai catar coquinho, vai fazer uma caminhada, vai sei lá. Só para.",
    f"{msg.author.mention} merecia um troféu de \"insuportável do ano\". Mas nem troféu eu gastaria contigo."
    ]
    # Lista de frases motivadoras

    randomMsg = int(random.randint(0,len(loveMsg)))
    # Seleciona aleatóriamente uma das 20 frases da array

    if msg.author.bot:
        return
    # Não aciona o evento caso a mensagem seja do próprio bot
    
    if random.random() < 0.05:
    # Gera um número de 0-1 aleatório com 5% de chance de acionar o evento
        await msg.reply(loveMsg[randomMsg])

    await bot.process_commands(msg)
    # mantém os demais comandos funcionando (sem ele o evento 'on_message' "bloqueia" os outros comando)

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

# -------------------------------
# COMANDOS PARA CALLS:
# -------------------------------
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

# runBot()

bot.run("")
# INSERIR TOKEN DE ACESSO DO BOT PARA LIGÁ-LO
