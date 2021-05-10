print("Preparing the bot...")
import discord
import os
import random

print("Initializing Repl.it database...")
from replit import db
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix = "l!", help_command = None)

client.remove_command('help')


@client.event
async def on_ready():
    activity = discord.Game(name = "in some servers", type = 1)
    await client.change_presence(status = discord.Status.online, activity = activity)
    print("I should be ready now!")


@client.command(help = "Shows a list of the bot's commands.")
async def help(ctx, args = None):
    help_embed = discord.Embed(title = "Let me help you!", color = 0x1e90ff)
    help_embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://cdn.discordapp.com/attachments/801291355707932672/841213994132176916/invert.png")
    command_names_list = [x.name for x in client.commands]

    if not args:
      help_embed.add_field(name = "Bot Commands", value = "\n".join([x.name for i, x in enumerate(client.commands)]), inline = False)
      help_embed.add_field(name = "Details", value = "Type `l!help <command name>` for more details about each command. \n \n*This is a rewritten version of LinerlyBot using Discord.py.*", inline = False)

    elif args in command_names_list:
      help_embed.add_field(name = args, value =client.get_command(args).help)

    else:
      help_embed.add_field(name = "Invalid command!", value = "That command isn't available.")

    await ctx.send(embed = help_embed)


@client.command(help = "Tells you about the bot.")
async def about(ctx):
  embed = discord.Embed(color = 0x1e90ff)
  embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://cdn.discordapp.com/attachments/801291355707932672/841213994132176916/invert.png")
  embed.add_field(name = "A new version of LinerlyBot which uses Discord.py instead of Discord.js.", value = "Previous LinerlyBot commands will be added back in the rewritten version! \n \n [Website](https://linerly.github.io/linerlybot) \n [Add Bot to your Server](https://discord.com/oauth2/authorize?client_id=833343953238884372&scope=bot&permissions=18432) \n [Source Code](https://github.com/Linerly/linerlybot-rewritten)")
  await ctx.send(embed = embed)


@client.command(help = "Checks the bot's current latency.")
async def ping(ctx):
  ping = str(round(client.latency * 1000))
  embed = discord.Embed(title = "Pong!", description = ping + " ms.", color = 0x1e90ff)
  embed.set_author(name = "LinerlyBot", url = "https://linerly.github.io/linerlybot", icon_url = "https://cdn.discordapp.com/attachments/801291355707932672/841213994132176916/invert.png")
  await ctx.send(embed = embed)


@client.command(help = "I can show you what I'm feeling now.")
async def feeling(ctx):
  feelings = [':slight_smile:', ':upside_down:', ':woozy_face:', ':confused:', ':sleeping:', ':rolling_eyes:', ':smiling_face_with_tear:', ':no_mouth:']
  await ctx.send(random.choice(feelings))


@client.command(help="(for testing purposes only)")
async def bank(ctx):
  value = db["currency"]
  await ctx.send("Bank: <:gold:752147412445036645> " + value)

client.run(os.environ['Token'])