import discord
import random
import time
from discord.ext import commands

TOKEN = "ODc3NjU0ODEzMDkxOTU0NzE4.Grr4Mk.1vreJHRndUmar0qoIUkekKbEwmc67Af8-DFPeo"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)


# client = discord.Client()
# bot = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    print("I am currently in", len(client.guilds), "servers.")


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    lMessage = user_message.lower()
    lenMessage = len(user_message)
    channel = str(message.channel.name)
    print("|" + time.strftime("%H:%M:%S", time.localtime()) + f"| {username}: {user_message} ({channel})")
    mention = f'<@!{username}>'

    if message.author == client.user:
        return

    if user_message.lower() == "hi":
        await message.channel.send(f"ok")

    if user_message.lower() == "bye":
        await message.channel.send(f"xD")

    if user_message.lower() == "ok":
        await message.channel.send(f"hi")

    if "i just" in user_message.lower():
        await message.channel.send(f"first time?")

    if "<:OMEGALUL:775515868410544149>" in user_message:
        await message.reply(f"SHEESH!", mention_author=False)

    if "donowall" in user_message.lower():
        await message.reply(f"I should've voted you for meanest person", mention_author=False)

    if "four" in user_message.lower():
        await message.channel.send(f"fo?")

    if "fo?" in user_message.lower():
        await message.channel.send(f"https://i.imgur.com/VeTNSCg.jpeg")

    if "devour" in user_message.lower():
        await message.reply(f"https://tenor.com/view/lottery-loser-rat-mouse-gif-12761681", mention_author=False)

    if "val" in user_message.lower():
        await message.reply(
            f"https://cdn.discordapp.com/attachments/770043097019056148/916065524172071002/D7_NFf60C-0Nd11gyqf4ulUcRZ3vATfsdkZCI5Pe6Gwiz6MB7-sObSF7H3mKGXUbwwr4Ehj7t8Urj2Ms765-nd-v1.png",
            mention_author=False)

    if "ganyu" in user_message.lower() and user_message != (
    f"https://tenor.com/view/ganyu-flowers-eat-eating-ganyu-poggers-gif-23827527"):
        await message.reply(f"https://tenor.com/view/gigachad-genshin-keqing-gif-23205874", mention_author=False)

    if "i am" in user_message.lower():
        name = lMessage.split("i am", 1)[1]
        await message.channel.send(f"hi" + name)

    if "<@!746078147463741590>" in user_message:
        if user_message == "<@!746078147463741590>":
            await message.channel.send(username + ": Michael")
            await message.channel.send(f"https://tenor.com/view/markiplier-funny-meme-what-gif-22548813")
        else:
            michaelMessage = user_message.replace("<@!746078147463741590>", "")
            await message.channel.send(username + ":" + michaelMessage)
        # await message.delete

    if message.author.id == 366269406214619136:
        await message.add_reaction("🤓")

    if message.author.id == 321027153489559553 and "I " == user_message[0:2].upper():
        await message.add_reaction("👑")
        await message.add_reaction("🇬")
        await message.add_reaction("🇴")
        await message.add_reaction("🇦")
        await message.add_reaction("🇹")
        await message.add_reaction("‼")
        await message.add_reaction("🙌")

    if "on god" in user_message.lower():
        await message.reply(f"On fracture!", mention_author=False)

    if "arcane" in user_message.lower():
        await message.channel.send(f"https://tenor.com/view/space-launch-funny-meme-space-force-space-gif-17548362")

    if "Recent osu! Standard Play for" in user_message:
        rand = random.randint(1, 3)
        if rand == 1:
            await message.channel.send(f"WTF, you're insane????")
    if "choke" in user_message.lower():
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


@client.command()
async def gettime(message):
    rand = random.randint(0, 2)
    if rand == 0:
        await message.channel.send(time.strftime("%H:%M:%S", time.localtime()))
    else:
        await message.channel.send(f"It's time for you to get a watch.")


@client.command(name="laugh")
async def laugh(ctx):
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("https://od.lk/s/MzVfMzI1MDczMzFf/clash_royale_emoji_king_laugh_green_screen_7229389992044983017-%5BAudioTrimmer.com%5D.mp3"))
        # vc.play(discord.FFmpegPCMAudio(executable="/Users/winstonchu/audio-orchestrator-ffmpeg/bin/ffmpeg", source="clash_royale_emoji_king_laugh_green_screen_7229389992044983017-[AudioTrimmer.com].mp3"))
        # while not vc.is_done():
        time.sleep(3)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")
    await ctx.message.delete()


client.run(TOKEN)
