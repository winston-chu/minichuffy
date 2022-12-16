import asyncio
import discord
import random
import time
import os
import string
from discord.ext import commands
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import interactions

load_dotenv()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)
bot = interactions.Client(token=os.getenv("TOKEN"))


# client = discord.Client()
# bot = commands.Bot(command_prefix=".")


@client.event
async def on_ready():

    await client.change_presence(activity=discord.Game('Overwatch 4'))

    print("We have logged in as {0.user}".format(client))
    print("I am currently in", len(client.guilds), "servers.")

     # datetime.today().strftime("%H:%M:%S") == "17:09:00":
     #    print("A")
     #    await client.start(TOKEN)





@client.event
async def raptors_games():
    channel = client.get_channel(837090657880637461)
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
    if message.guild:
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        lMessage = user_message.lower()
        lenMessage = len(user_message)

        channel = str(message.channel.name)

        await client.change_presence(activity=discord.Game('Overwatch ' + str(random.randint(0, 1000000))))

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
            if random.randint(0, 9) == 5:
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

        if message.content.startswith('-hangman'):

            channel = await message.author.create_dm()
            intCount = 0
            toGuess = ""
            currentScore = ""
            lives = 12
            await channel.send(embed = discord.Embed(title="Welcome to Hangman!", description="Please enter your word.", color=0xFF9900))
            def check(m):
                return m.channel == channel
            response = await client.wait_for('message', check=check, timeout=60)
            word = response.content
            for i in range(len(word)):

                if word[i].isalpha():
                    toGuess += word[i].upper()
                    currentScore += "_"
                elif word[i].isnumeric():
                    toGuess += word[i]
                    intCount += 1
                    currentScore += "_"
                elif word[i].isspace():
                    toGuess += " "
                    currentScore += " "
                elif word[i] in string.punctuation:
                    toGuess += word[i]
                    currentScore += word[i]

            channel = message.channel
            toSend = discord.Embed(title=str(message.author) + " wants to play hangman!", color=0xFF9900)
            toSend.add_field(name="Hint: the amount of numbers in this word/sentence is: ", value=intCount, inline=False)
            toSend.add_field(name="Starting lives: ", value=lives, inline=False)
            toSend.add_field(name="Help: ", value="Each letter guess takes one life if wrong, each attempted answer guess takes two.", inline=False)
            await message.channel.send(embed = toSend)
            announcement = f"The current word/sentence to guess is:  " + "".join(" \\" + char if char == "_" and currentScore[i - 1] == "_" else "\\" + char if char == "_" else char for i, char in enumerate(currentScore))

            keepgoing = True
            numCorrect = 0
            def checkUser(m):
                return m.channel == channel and m.author != message.author

            while keepgoing:

                guessed = ""
                await message.channel.send(announcement)
                g = await client.wait_for('message', check=checkUser, timeout=600)
                guess = g.content
                # print(g)
                for char in range(len(guess)):
                    if guess[char].isalpha():
                        guessed += guess[char].upper()
                    elif guess[char].isnumeric():
                        guessed += guess[char]
                    elif guess[char].isspace():
                        guessed += " "
                    elif guess[char] in string.punctuation:
                        guessed += guess[char]

                if len(guess) == 1:
                    if guessed in currentScore:
                        await message.channel.send(f"Oops! this letter has already been guessed. Please try again.")

                    else:
                        guessInWord = False
                        for j in range(len(toGuess)):
                            if toGuess[j] == guessed:

                                currentScore = currentScore[:j] + guessed + currentScore[j + 1:]
                                numCorrect += 1
                                guessInWord = True
                            print(currentScore)

                        if not guessInWord:
                            lives -= 1
                            await message.channel.send(f"Sorry! You guessed wrong. " + str(lives) + " live(s) left.")

                        if lives <= 0:
                            outcome = f"You are out of lives! the correct word/sentence was: " + word
                            keepgoing = False

                        if guessInWord:
                            await message.channel.send(f"Correct! " + str(numCorrect) + " change(s).")

                            announcement = f"The current word/sentence to guess is:  " + "".join(" \\" + char if char == "_" and currentScore[i - 1] == "_" else "\\" + char if char == "_" else char for i, char in enumerate(currentScore))
                            numCorrect = 0
                        if currentScore == toGuess:
                            await message.channel.send(announcement)
                            outcome = f"You have guessed the word/sentence! Congrats!"
                            keepgoing = False

                else:
                    if guessed == toGuess:
                        outcome = f"You have guessed the word/sentence! Congrats!"
                        keepgoing = False

                    else:
                        lives -= 2
                        await message.channel.send(f"Sorry! You guessed wrong. " + str(lives) + " live(s) left.")

                        if lives <= 0:
                            outcome = f"You are out of lives! the correct word/sentence was: " + word
                            keepgoing = False

            endGame = discord.Embed(title=outcome, color=0xFF9900)
            endGame.add_field(name="Remaining Lives: ", value=lives, inline=False)
            await message.channel.send(embed = endGame)




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



@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
    scope=548550180807376921,
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")



# bot.start()
client.run(os.getenv("TOKEN"))
