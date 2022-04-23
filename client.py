import discord
client = discord.Client()
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    pass

@client.event
async def on_message(message):
    print(message.content)


@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

@client.event
async def on_member_join(member):
    print(f"L'utilisateur {member.display_name} a rejoint le serveur !")
    
@client.event
async def on_member_join(member):
    general_channel = client.get_channel(967508479092879370)
    general_channel.send(f"Bienvenue sur le serveur de YO {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()   

client.run("OTU5MzUxODcwNDMyODgyNzM4.YkaoDQ.1BrGkkpNAM7IHPJBCEi15Ax8dos")