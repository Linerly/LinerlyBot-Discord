print("Preparing the bot...")
import discord
import os
import distro
import time
import json
import random

from datetime import datetime, timedelta

from decouple import config

from discord_slash import SlashCommand

from discord.ext import commands

guild_ids = [809722018953166858]

client = commands.Bot(command_prefix = "l!", help_command = None)
slash = SlashCommand(client, sync_commands = True)

client.remove_command('help')


@client.event
async def on_ready():
    global start_time
    start_time = time.time()

    activity = discord.Activity(name = "requests and responding to them", type = discord.ActivityType.listening)
    await client.change_presence(status = discord.Status.online, activity = activity)
    print("I should be ready now!")


@client.command(help = "Shows a list of the bot's commands.")
async def help(ctx, args = None):
    help_embed = discord.Embed(title = "Let me help you!", color = 0x1e90ff)
    help_embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    command_names_list = [x.name for x in client.commands]

    if not args:
      help_embed.add_field(name = "Bot Commands", value = "\n".join([x.name for i, x in enumerate(client.commands)]), inline = False)
      help_embed.add_field(name = "Details", value = "Type `l!help <command name>` for more details about each command. \n \n*This is a rewritten version of LinerlyBot using Discord.py.*", inline = False)

    elif args in command_names_list:
      help_embed.add_field(name = args, value = client.get_command(args).help)

    else:
      help_embed.add_field(name = "Invalid command!", value = "That command isn't available.")

    await ctx.send(embed = help_embed)

@slash.slash(name = "help", description = "Shows a list of the bot's commands.")
async def _help(ctx, args = None):
    help_embed = discord.Embed(title = "Let me help you!", color = 0x1e90ff)
    help_embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    command_names_list = [x.name for x in client.commands]

    if not args:
      help_embed.add_field(name = "Bot Commands", value = "\n".join([x.name for i, x in enumerate(client.commands)]), inline = False)
      help_embed.add_field(name = "Details", value = "Type `l!help <command name>` for more details about each command. \n \n*This is a rewritten version of LinerlyBot using Discord.py.*", inline = False)

    elif args in command_names_list:
      help_embed.add_field(name = args, value = client.get_command(args).help)

    else:
      help_embed.add_field(name = "Invalid command!", value = "That command isn't available.")

    await ctx.send(embed = help_embed)

@client.command(help = "Tells you about the bot.")
async def about(ctx):
    embed = discord.Embed(color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "A new version of LinerlyBot which uses Discord.py instead of Discord.js.", value = "Previous LinerlyBot commands will be added back in the rewritten version! \n \n [Website](https://linerly.github.io/linerlybot) \n [Add LinerlyBot to your Discord Server](https://discord.com/oauth2/authorize?client_id=529566778293223434&permissions=2147485696&scope=bot+applications.commands) \n [Source Code](https://github.com/Linerly/linerlybot-rewritten)")
    await ctx.send(embed = embed)

@slash.slash(name = "about", description = "Tells you about the bot.")
async def _about(ctx):
    embed = discord.Embed(color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "A new version of LinerlyBot which uses Discord.py instead of Discord.js.", value = "Previous LinerlyBot commands will be added back in the rewritten version! \n \n [Website](https://linerly.github.io/linerlybot) \n [Add LinerlyBot to your Discord Server](https://discord.com/oauth2/authorize?client_id=529566778293223434&permissions=2147485696&scope=bot+applications.commands) \n [Source Code](https://github.com/Linerly/linerlybot-rewritten)")
    await ctx.send(embed = embed)

@client.command(help = "Checks the bot's current latency.")
async def ping(ctx):
    ping = str(round(client.latency * 1000))
    embed = discord.Embed(title = "Pong!", description = ping + " ms.", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    await ctx.send(embed = embed)

@slash.slash(name = "ping", description = "Checks the bot's current latency.")
async def _ping(ctx):
    ping = str(round(client.latency * 1000))
    embed = discord.Embed(title = "Pong!", description = ping + " ms.", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    await ctx.send(embed = embed)

@client.command(help = "I can show you what I'm feeling now.")
async def feeling(ctx):
    feelings = [':slight_smile:', ':upside_down:', ':woozy_face:', ':confused:', ':sleeping:', ':rolling_eyes:', ':smiling_face_with_tear:', ':no_mouth:']
    await ctx.send(random.choice(feelings))

@slash.slash(name = "feeling", description = "I can show you what I'm feeling now.")
async def _feeling(ctx):
    feelings = [':slight_smile:', ':upside_down:', ':woozy_face:', ':confused:', ':sleeping:', ':rolling_eyes:', ':smiling_face_with_tear:', ':no_mouth:']
    await ctx.send(random.choice(feelings))

def get_gold_balance(member: discord.Member):
    with open("bank.json", "r") as fp:
        print("Accessing JSON database...")
        data = json.load(fp)
  
    try:
        return data[f"{member.id}"]["gold"]
  
    except KeyError:
        data[f"{member.id}"] = {"gold": 0}
  
def add_gold_balance(member: discord.Member, amount):
    if os.path.isfile("bank.json"):
        with open("bank.json", "r") as fp:
            print("Loading JSON database...")
            data = json.load(fp)

    try:
        data[f"{member.id}"]["gold"] += amount

    except KeyError:
        data[f"{member.id}"] = {"gold": amount}

    else:
        data = {f"{member.id}": {"gold": amount}}

        with open("bank.json", "w+") as fp:
            print("Writing to JSON database...")
            json.dump(data, fp)

@client.command(help = "Check your balance by using the command.")
async def balance(ctx):
    gold_balance = str(get_gold_balance(ctx.author))

    embed = discord.Embed(title = "You currently have...", description = "<:gold:752147412445036645> " + gold_balance, color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "_ _", value = "Please be aware that new users that isn't in the database will result in an internal error!")
    await ctx.send(embed = embed)

@slash.slash(name = "balance", description = "Check your balance by using the command.")
async def _balance(ctx):
    gold_balance = str(get_gold_balance(ctx.author))

    embed = discord.Embed(title = "You currently have...", description = "<:gold:752147412445036645> " + gold_balance, color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "_ _", value = "Please be aware that new users that isn't in the database will result in an internal error!")
    await ctx.send(embed = embed)

@client.command(help = "Get some gold by working!")
async def work(ctx):
    job = "(insert job here)"
    gold = random.randint(0, 150)

    embed = discord.Embed(title = "Working", description = ctx.author.mention +", you work as a " + job + " and you got " + "<:gold:752147412445036645> " + str(gold) + " for working!", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "_ _", value = "Please be aware that new users that isn't in the database will result in an internal error!")

    add_gold_balance(ctx.author, get_gold_balance(ctx.author) + gold)

    await ctx.send(embed = embed)

@slash.slash(name = "work", description = "Get some gold by working!")
async def _work(ctx):
    job = "(insert job here)"
    gold = random.randint(0, 150)

    embed = discord.Embed(title = "Working", description = ctx.author.mention +", you work as a " + job + " and you got " + "<:gold:752147412445036645> " + str(gold) + " for working!", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")
    embed.add_field(name = "_ _", value = "Please be aware that new users that isn't in the database will result in an internal error!")

    add_gold_balance(ctx.author, get_gold_balance(ctx.author) + gold)

    await ctx.send(embed = embed)

@client.command(help = "Shows some info about the bot.")
async def info(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds = difference))
  
    ping = str(round(client.latency * 1000))

    embed = discord.Embed(title = "Bot Info", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")

    embed.add_field(name = "Bot Uptime", value = ":green_circle: " + text)

    embed.add_field(name = "Servers", value = ":desktop: in " + str(len(client.guilds)) + " servers")

    embed.add_field(name = "Latency", value = ":globe_with_meridians: " + ping + " ms")

    embed.add_field(name = "Operating System", value = ":penguin: running on " + str(distro.name(pretty = True)))
    await ctx.send(embed = embed)

@slash.slash(name = "info", description = "Shows some info about the bot.")
async def _info(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds = difference))
  
    ping = str(round(client.latency * 1000))

    embed = discord.Embed(title = "Bot Info", color = 0x1e90ff)
    embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://linerly.github.io/assets/linerlybot/linerlybot.jpg")

    embed.add_field(name = "Bot Uptime", value = ":green_circle: " + text)

    embed.add_field(name = "Servers", value = ":desktop: in " + str(len(client.guilds)) + " servers")

    embed.add_field(name = "Latency", value = ":globe_with_meridians: " + ping + " ms")

    embed.add_field(name = "Operating System", value = ":penguin: running on " + str(distro.name(pretty = True)))
    await ctx.send(embed = embed)

@slash.slash(help = "A test command to check if the bot works, nothing else.")
async def _test(ctx):
    await ctx.send("test")

@slash.slash(name = "test", description = "A test command to check if slash commands works, nothing else.")
async def _test(ctx):
    await ctx.send("test")

client.run(config('TOKEN'))