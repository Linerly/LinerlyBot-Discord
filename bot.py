print("Preparing the bot...")
import json
import os
import platform
import random
import time
from datetime import timedelta

import discord
import distro
import pyjokes
import requests
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
from quoters import Quote

from webserver import keep_alive


def splitTime(seconds: int) -> list:
    "Split time into decades, years, months, weeks, days, hours, minutes, and seconds."
    seconds = int(seconds)

    def modTime(sec, num):
        smod = sec % num
        return int((sec - smod) // num), smod

    divs = (
        15768000000000000,
        3153600000000000,
        315360000000000,
        31536000000000,
        31536000000,
        3153600000,
        315360000,
        31536000,
        2628000,
        604800,
        86400,
        3600,
        60,
        1,
    )
    ret = []
    for num in divs:
        t, seconds = modTime(seconds, num)
        ret.append(t)
    return ret


def combineAnd(data: list) -> str:
    "Join values of text, and have 'and' with the last one properly."
    data = list(data)
    if len(data) >= 2:
        data[-1] = "and " + data[-1]
    if len(data) > 2:
        return ", ".join(data)
    return " ".join(data)


def printTime(seconds: int, singleTitleAllowed: bool = True) -> str:
    "Returns time using the output of splitTime."
    times = (
        "eons",
        "eras",
        "epochs",
        "ages",
        "millenniums",
        "centuries",
        "decades",
        "years",
        "months",
        "weeks",
        "days",
        "hours",
        "minutes",
        "seconds",
    )
    single = [i[:-1] for i in times]
    single[5] = "century"
    split = splitTime(seconds)
    zipidxvalues = [(idx, split[idx]) for idx in range(len(split)) if split[idx]]
    if singleTitleAllowed:
        if len(zipidxvalues) == 1:
            index, value = zipidxvalues[0]
            if value == 1:
                return single[index]
    data = []
    for index, value in zipidxvalues:
        title = single[index] if abs(value) < 2 else times[index]
        data.append(str(value) + " " + title)
    return combineAnd(data)


client = commands.Bot(
    intents=discord.Intents.all(), command_prefix="l!", help_command=None
)
slash = SlashCommand(client, sync_commands=True)

client.remove_command("help")


@client.event
async def on_ready():
    global start_time
    start_time = time.time()

    print("I should be ready now!")


@client.command(help="Shows a list of the bot's commands.")
async def help(ctx, command=None):
    help_embed = discord.Embed(title="Let me help you!", color=0x1E90FF)
    help_embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    command_names_list = [x.name for x in client.commands]

    if not command:
        help_embed.add_field(
            name="Bot Commands",
            value="\n".join([x.name for i, x in enumerate(client.commands)]),
            inline=False,
        )
        help_embed.add_field(
            name="Details",
            value="Type `l!help <command name>` for more details about each command. \n \n*This is a rewritten version of LinerlyBot using Discord.py.*",
            inline=False,
        )

    elif command in command_names_list:
        help_embed.add_field(name=command, value=client.get_command(command).help)

    else:
        help_embed.add_field(
            name="Invalid command!", value="That command isn't available."
        )

    await ctx.send(embed=help_embed)


@slash.slash(
    name="help",
    description="Shows a list of the bot's commands.",
    options=[
        create_option(
            name="command",
            description="Specify a command that you want to get more info about it.",
            option_type=3,
            required=False,
        )
    ],
)
async def _help(ctx, command: str):
    help_embed = discord.Embed(title="Let me help you!", color=0x1E90FF)
    help_embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    command_names_list = [x.name for x in client.commands]

    if not command:
        help_embed.add_field(
            name="Bot Commands",
            value="\n".join([x.name for i, x in enumerate(client.commands)]),
            inline=False,
        )
        help_embed.add_field(
            name="Details",
            value="Type `/help <command name>` for more details about each command. \n \n*This is a rewritten version of LinerlyBot using Discord.py.*",
            inline=False,
        )

    elif command in command_names_list:
        help_embed.add_field(name=command, value=client.get_command(command).help)

    else:
        help_embed.add_field(
            name="Invalid command!", value="That command isn't available."
        )

    await ctx.send(embed=help_embed)


@client.command(help="Tells you about the bot.")
async def about(ctx):
    embed = discord.Embed(color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    embed.add_field(
        name="A new version of LinerlyBot which uses Discord.py instead of Discord.js.",
        value="Previous LinerlyBot commands will be added back in the rewritten version! \n \n [Website](https://linerly.github.io/linerlybot) \n [Add LinerlyBot to your Discord Server](https://discord.com/api/oauth2/authorize?client_id=529566778293223434&permissions=1576266871&scope=applications.commands%20bot) \n [Source Code](https://github.com/Linerly/linerlybot-rewritten)",
    )
    await ctx.send(embed=embed)


@slash.slash(name="about", description="Tells you about the bot.")
async def _about(ctx):
    embed = discord.Embed(color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    embed.add_field(
        name="A new version of LinerlyBot which uses Discord.py instead of Discord.js.",
        value="Previous LinerlyBot commands will be added back in the rewritten version! \n \n [Website](https://linerly.github.io/linerlybot) \n [Add LinerlyBot to your Discord Server](https://discord.com/oauth2/authorize?client_id=529566778293223434&permissions=2147485696&scope=bot+applications.commands) \n [Source Code](https://github.com/Linerly/linerlybot-rewritten)",
    )
    await ctx.send(embed=embed)


@client.command(help="Checks the bot's current latency.")
async def ping(ctx):
    ping = str(round(client.latency * 1000))
    embed = discord.Embed(title="Pong!", description=ping + " ms.", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    await ctx.send(embed=embed)


@slash.slash(name="ping", description="Checks the bot's current latency.")
async def _ping(ctx):
    ping = str(round(client.latency * 1000))
    embed = discord.Embed(title="Pong!", description=ping + " ms.", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )
    await ctx.send(embed=embed)


@client.command(help="I can show you what I'm feeling now.")
async def feeling(ctx):
    feelings = [
        ":slight_smile:",
        ":upside_down:",
        ":woozy_face:",
        ":confused:",
        ":sleeping:",
        ":rolling_eyes:",
        ":smiling_face_with_tear:",
        ":no_mouth:",
    ]
    await ctx.send(random.choice(feelings))


@slash.slash(name="feeling", description="I can show you what I'm feeling now.")
async def _feeling(ctx):
    feelings = [
        ":slight_smile:",
        ":upside_down:",
        ":woozy_face:",
        ":confused:",
        ":sleeping:",
        ":rolling_eyes:",
        ":smiling_face_with_tear:",
        ":no_mouth:",
    ]
    await ctx.send(random.choice(feelings))


@client.command(help="Shows some info about the bot.")
async def info(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))

    ping = str(round(client.latency * 1000))

    embed = discord.Embed(title="Bot Info", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )

    embed.add_field(name="Bot Uptime", value=":green_circle: " + text)

    embed.add_field(
        name="Servers", value=":desktop: in " + str(len(client.guilds)) + " servers"
    )

    embed.add_field(name="Latency", value=":globe_with_meridians: " + ping + " ms")

    embed.add_field(
        name="Operating System",
        value=":penguin: running on " + str(distro.name(pretty=True)),
    )

    embed.add_field(
        name="Python Version",
        value=":snake: Python " + str(platform.python_version()),
    )

    await ctx.send(embed=embed)


@slash.slash(name="info", description="Shows some info about the bot.")
async def _info(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))

    ping = str(round(client.latency * 1000))

    embed = discord.Embed(title="Bot Info", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )

    embed.add_field(name="Bot Uptime", value=":green_circle: " + text)

    embed.add_field(
        name="Servers", value=":desktop: in " + str(len(client.guilds)) + " servers"
    )

    embed.add_field(name="Latency", value=":globe_with_meridians: " + ping + " ms")

    embed.add_field(
        name="Operating System",
        value=":penguin: running on " + str(distro.name(pretty=True)),
    )

    embed.add_field(
        name="Python Version",
        value=":snake: Python " + str(platform.python_version()),
    )

    await ctx.send(embed=embed)


@client.command(help="Tells you random jokes.")
async def joke(ctx):
    await ctx.send(pyjokes.get_joke())


@slash.slash(name="joke", description="Tells you random jokes.")
async def _joke(ctx):
    await ctx.send(pyjokes.get_joke())


@client.command(help="Tells you random quotes.")
async def quote(ctx):
    async with ctx.typing():
        await ctx.send(Quote.print())


@slash.slash(name="quote", description="Tells you random quotes.")
async def _quote(ctx):
    await ctx.send(Quote.print())


@client.command(
    help="Generate, predict, or just complete texts. The generated text may contain profanity."
)
async def text(ctx, text=None):
    async with ctx.typing():
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                "text": text,
            },
            headers={"api-key": os.environ["DEEPAI_API_KEY"]},
        )

        await ctx.send(
            f"**Raw JSON Output** \n*provided by DeepAI* \n```{str(r.json())}```"
        )


@slash.slash(
    name="text",
    description="Generate, predict, or just complete texts.",
    options=[
        create_option(
            name="text",
            description="Your text - anything!",
            option_type=3,
            required=True,
        )
    ],
)
async def _text(ctx, text: str):
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            "text": text,
        },
        headers={"api-key": os.environ["DEEPAI_API_KEY"]},
    )

    await ctx.send(
        f"**Raw JSON Output** \n*provided by DeepAI* \n```{str(r.json())}```"
    )


@client.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def balance(ctx):
    with open("bank.json") as file:
        gold = json.load(file)

    if str(ctx.author.id) not in gold:
        gold[str(ctx.author.id)] = 0

    embed = discord.Embed(title="You currently have...", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )

    embed.add_field(
        name="Gold", value=f"<:gold:752147412445036645> {gold[str(ctx.author.id)]}"
    )
    await ctx.send(embed=embed)

    with open("bank.json", "w") as write:
        json.dump(gold, write, indent=2)


@client.command()
@commands.cooldown(rate=1, per=900, type=commands.BucketType.user)
async def work(ctx):
    with open("bank.json") as file:
        gold = json.load(file)

    amount = random.randint(100, 750)
    job = random.choice(
        [
            "game developer",
            "designer",
            "programmer",
            "singer",
            "bartender",
            "cashier",
            "janitor",
            "doctor",
            "YouTuber",
            "streamer",
            "construction worker",
            "mechanic",
            "carpenter",
            "nurse",
            "police officer",
            "lawyer",
            "developer",
            "graphics designer",
            "writer",
        ]
    )

    gold[str(ctx.author.id)] += amount

    embed = discord.Embed(title="Working", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )

    embed.add_field(
        name="Gold",
        value=f"{ctx.message.author.mention}, you've worked as a {job} and you got <:gold:752147412445036645> {amount} for working!",
    )
    await ctx.send(embed=embed)

    with open("bank.json", "w") as write:
        json.dump(gold, write, indent=2)


@slash.slash(name="balance", description="Shows your current gold balance.")
async def _balance(ctx):
    with open("bank.json") as file:
        gold = json.load(file)

    if str(ctx.author.id) not in gold:
        gold[str(ctx.author.id)] = 0

    embed = discord.Embed(title="You currently have...", color=0x1E90FF)
    embed.set_author(
        name="LinerlyBot",
        url="https://linerly.github.io/linerlybot",
        icon_url="https://linerly.github.io/assets/linerlybot/linerlybot.png",
    )

    embed.add_field(
        name="Gold", value=f"<:gold:752147412445036645> {gold[str(ctx.author.id)]}"
    )
    await ctx.send(embed=embed)

    with open("bank.json", "w") as write:
        json.dump(gold, write, indent=2)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        if str(error).startswith("You are on cooldown. Try again in"):
            secs = str(error)[34:]
        if secs.endswith("s"):
            secs = secs[:-1]
        secs = int(float(secs))
        newerror = f"You are on cooldown. Try again in {printTime(secs)}."
        await ctx.send(newerror)


keep_alive()
client.run(os.environ["TOKEN"])
