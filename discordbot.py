import asyncio
import discord
import random
import time
import os
from discord.ext import commands
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

# TOKEN = "ODc3NjU0ODEzMDkxOTU0NzE4.G8WM1M.wsAU-C7E5tMPmGV2TIUSPJg7AGOLdvyelGNZNQ"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)

# client = discord.Client()
# bot = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    channel = client.get_channel(837090657880637461)
    print("We have logged in as {0.user}".format(client))
    print("I am currently in", len(client.guilds), "servers.")

     # datetime.today().strftime("%H:%M:%S") == "17:09:00":
     #    print("A")
     #    await client.start(TOKEN)

    with open("raptors2023.txt", "r") as raptorsSchedule:
        hourBefore = datetime.today() + timedelta(hours=1)
        for line in raptorsSchedule:
            day, team, location, hour = line.split()

            if day == str(date.today()):
                while hour != str(hourBefore.strftime("%H:%M")):
                    hourBefore = datetime.today() + timedelta(hours=1)
                    await asyncio.sleep(1)

                embedVar = discord.Embed(title="Toronto Raptors Game Day", description="Facing the " + str(team) + " (" + str(location) + ") in one hour.", color=0xFF9900)
                embedVar.add_field(name="Do you think they can win?", value="React with your prediction.", inline=False)

                message = await channel.send(embed=embedVar)

                # msg = "The Raptors are facing the " + str(team) + " (" + str(location) + ") in one hour. Do you think they will win or lose?"
                # message = await channel.send(msg)
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                with open("raptors2023.txt", "r") as oldSched:
                    data = oldSched.read().splitlines(True)
                with open("raptors2023.txt", "w") as newSched:
                    newSched.writelines(data[1:])

    # if datetime.today().strftime("%H:%M") == "00:00":
    #     print("A")
    #     await client.start(TOKEN)

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    lMessage = user_message.lower()
    lenMessage = len(user_message)
    if message.guild:
        channel = str(message.channel.name)
    else:
        return
    print("[" + time.strftime("%H:%M:%S", time.localtime()) + f"] {username}: {user_message} ({channel})")
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

    if message.channel.name == "aaa":
        if "thank you" in user_message.lower() or "thanks" in user_message.lower():
            await message.channel.send(f"that wasn't for you but ok")
    await client.process_commands(message)


# make a hangman game where one player dms a word and others guess it
@client.command()
async def hangman(message):
    channel = await message.author.create_dm()
    await channel.send(embed = discord.Embed(title="Welcome to Hangman!", description="Please enter your word.", color=0xFF9900))

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
    await ctx.message.delete()
    voice_channel = ctx.author.voice.channel
    channel = None
    if voice_channel is not None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio("https://od.lk/s/MzVfMzI1MDczMzFf/clash_royale_emoji_king_laugh_green_screen_7229389992044983017-%5BAudioTrimmer.com%5D.mp3"))
        time.sleep(3)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + " is not in a channel.")



@client.command()
async def sched(message, num="5"):
    d = []
    t = []
    l = []
    h = []
    msg = ""

    with open("raptors2023.txt", "r") as raptorsSchedule:
        for line in raptorsSchedule:
            day, team, location, hour = line.split()
            d.append(day)
            t.append(team)
            l.append(location)
            h.append(hour)

        try:
            print(t[int(num) - 1])
        except IndexError:
            await message.channel.send(f"The Raptors don't have that amount of games left this season.")
            return
        except ValueError:
            await message.channel.send(f"Please enter a valid number.")
            return

        if int(num) >= 26:
            await message.channel.send(f"25 is the max number.")
            num = str(25)

        embedVar = discord.Embed(title="Raptors' next " + num + " game(s):", description="", color=0xFF9900)
        for i in range(int(num)):
            embedVar.add_field(name=str(t[i]) + " (" + str(l[i]) + ")", value="On " + str(d[i]) + " at " + str(h[i]), inline=False)

        await message.channel.send(embed=embedVar)






client.run(os.getenv("TOKEN"))
