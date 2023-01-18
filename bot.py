
import random
import discord
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix='<', description="uwu")


@bot.command(pass_context=True)
async def conectar(ctx):
    canal = ctx.message.author.voice.channel
    if not canal:
        await ctx.send("Conenctate antes de mandar comandos pibe.")
        return

    voz=get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()

@bot.command (pass_context = True)
async def desconectar(ctx):
    canal = ctx.message.author.voice.channel
    voz = get(bot.voice_clients,guild=ctx.guild)
    await voz.disconnect()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Nier:Automata™"))
    print('Ready!')
    return

@bot.command(name='s')
async def suma(ctx, num1, num2):
    resultado = int(num1)+int(num2)
    response = f"El resultado de la sumita que te hice es: " + str(resultado) + "." + " Cabeza de tacho"
    await ctx.send(response)
@bot.command(name='r')
async def resta(ctx, num1, num2):
    resultado = int(num1)-int(num2)
    response = f"El resultado de la restita que te hice es: " + str(resultado) + "." + " Cabeza de tacho"
    await ctx.send(response)

@bot.command(name='m')
async def multiplicacion(ctx, num1, num2):
    resultado = int(num1)*int(num2)
    response = f"El resultado de la multip... ah tremendo nombre. Es: " + str(resultado) + "." + " Cabeza de tacho"
    await ctx.send(response)

@bot.command(name='d')
async def division(ctx, num1, num2):
    resultado = int(num1)/int(num2)
    response = f"El resultado de la divicion que te hice es: " + str(resultado) + "." + " Cabeza de tacho"
    await ctx.send(response)

@bot.command(name="saludo")
async def saludo(ctx):
    canal = ctx.message.author.name
    if canal != "pepimaxy":
        response = f"Bom dia meu amor {canal}"
    elif canal == "Ghetto1982":
        response = f"Hola esposa de mi creador."
    else:
        response = f"Finisimo dia mi creador Pedrito... Alabada sea la tecnología por darme vida. 🙏"
    await ctx.send(response)

@bot.command(name="insulto")
async def insulto(ctx):
    listInsultos = [
        "Gordo puto",
        "Concha abierta",
        "Agüeonao",
        "Baboso",
        "Feo",
        "idiota",
        "adoquín",
        "lerdo", 
        "mameluco", 
        "mentecato", 
        "pazguato", 
        "imbécil", 
        "retrasado", 
        "estúpido", 
        "mastuerzo", 
        "atontao", 
        "orate", 
        "loco", 
        "subnormal", 
        "deficiente", 
        "majadero", 
        "cenutrio", 
        "zoquete", 
        "analfabeto", 
        "ignorante", 
        "palurdo", 
        "berzotas", 
        "gaznápiro",
        "sinvergüenza", 
        "ladrón", 
        "bellaco", 
        "degenerado", 
        "bribón", 
        "granuja", 
        "hupasangre", 
        "sanguijuela", 
        "cantamañanas", 
        "chupóptero", 
        "zascandil", 
        "canalla",
        "cagueta", 
        "cobarde", 
        "pusilánime", 
        "gallina", 
        "alfeñique", 
        "lechuguino",
    ]
    insult = random.choice(listInsultos)
    response = (insult.lower().capitalize())
    await ctx.send(response)
    
@bot.command(name="shiono")
async def shiono(ctx):
    respuestas = [
        'Ni idea man, vofi.',
        'Te lo juro por Dieguito Maradona.',
        'MUCHAAAAAAAAAACHOOOOOOOOOOOOO'
        'Facha dice que no.',
        'A Julian le gusta eso.',
        'Pedro dice que si y dejate de joder.',
        'Nada que ver.',
        'Tu vieja.',
        'EN EL PUNTO GEEEEEEEEEEEEEEE.',
        'Si pero te recomiendo que no 🤓',
        'Yo diria que si, pero mi celular esta cargando.'
    ]
    shiono = random.choice(respuestas)
    await ctx.send(shiono)

 
 
bot.run("OTY3MTUzMjY2MDM3MjM1NzMy.GidkEC.FGTFgbkZ2fF5SKc_MziM8LkpBZ0NrrL1HUOzjA")