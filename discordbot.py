import discord
import random
from discord.ext import commands

TOKEN = "ODc3NjU0ODEzMDkxOTU0NzE4.YR1xvQ.CMGaozkt7gJirLw0E31KpuGhOPA"

client = commands.Bot(command_prefix="-")
# client = discord.Client()
# bot = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return
    if user_message.lower() == "hi":
        await message.channel.send(f"ok")
        return
    elif user_message.lower() == "bye":
        await message.channel.send(f"xD")
        return
    elif user_message.lower() == "ok":
        await message.channel.send(f"hi")
        return
    elif "i just" in user_message.lower():
        await message.channel.send(f"first time?")
        return
    elif "<:OMEGALUL:775515868410544149>" in user_message:
        await message.reply(f"SHEESH!", mention_author = False)
    elif "donowall" in user_message.lower():
        await message.reply(f"I should've voted you for meanest person", mention_author = False)
    elif "four" in user_message.lower():
        await message.channel.send(f"fo?")
    elif "fo?" in user_message.lower():
        await message.channel.send(f"https://imgur.com/a/IQpgMU9")
    elif "devour" in user_message.lower():
        await message.reply(f"https://tenor.com/view/lottery-loser-rat-mouse-gif-12761681", mention_author = False)
    elif "val" in user_message.lower():
        await message.reply(f"https://cdn.discordapp.com/attachments/770043097019056148/916065524172071002/D7_NFf60C-0Nd11gyqf4ulUcRZ3vATfsdkZCI5Pe6Gwiz6MB7-sObSF7H3mKGXUbwwr4Ehj7t8Urj2Ms765-nd-v1.png", mention_author = False)
    elif "ganyu" in user_message.lower():
        await message.reply(f"https://tenor.com/view/gigachad-genshin-keqing-gif-23205874", mention_author = False)
    elif "@poopsock#9879" in user_message:
        await message.channel.send(f"https://tenor.com/view/markiplier-funny-meme-what-gif-22548813")

        if "Recent osu! Standard Play for" in user_message:
            rand = random.randint(1, 3)
            if rand == 1:
                await message.channel.send(f"WTF, you're insane????")
        elif "choke" in user_message.lower():
            await message.channel.send(f"https://tenor.com/view/gene-issue-gif-22947786")

    if message.channel.name == "the-mgg-channel-and-no-mic":
        if "thank you" in user_message.lower() or "thanks" in user_message.lower():
            await message.channel.send(f"that wasn't for you but ok")
    await client.process_commands(message)

@client.command()
async def join(message):
    channel = message.author.voice.channel
    await channel.connect()


@client.command()
async def leave(message):
    await message.voice_client.disconnect()


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")


@client.command()
async def wysi(message):
    username = str(message.author).split('#')[0]
    if message.channel.name == "minichuffy":
        response = f"{username} rolled {random.randint(1, 1000)}"
        if response == f"{username} rolled 727":
            response = f"{username} rolled 727!!! https://tenor.com/view/aireu-727-wysi-when-you-see-it-osu-gif-21274243"
        await message.channel.send(response)
        return

client.run(TOKEN)