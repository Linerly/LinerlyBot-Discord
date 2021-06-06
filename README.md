# linerlybot-rewritten
![discord-server](https://img.shields.io/discord/551683447026876418?logoColor=1e90ff&style=plastic)

![license](https://img.shields.io/github/license/Linerly/linerlybot-rewritten?style=plastic)

![maintained?](https://img.shields.io/maintenance/yes/2021?style=plastic)

The new version of LinerlyBot with discord.py.

[Add LinerlyBot to your Discord server!](https://discord.com/oauth2/authorize?client_id=529566778293223434&permissions=2147485696&scope=bot+applications.commands)

---

# Some issues when using LinerlyBot
- When using slash commands, it may fail the first time using it, however it will work when you try again.
- The `quote` command will fail when using it as a slash command, it has to get the quotes somewhere on the internet, and then sending it back to you which causes delay.

---

# Additional Python libraries used for LinerlyBot

Here is a list of the additional Python libraries used for LinerlyBot.

- [discord.py](https://pypi.org/project/discord.py/) - duh, you need it
- [discord-py-slash-command](https://pypi.org/project/discord-py-slash-command/) - for handling slash commands
- [python-decouple](https://pypi.org/project/python-decouple/) - for reading parameters in an .env file, just for the bot's token
- [distro](https://pypi.org/project/distro/) - for detecting what OS the bot is running on
- [pyjokes](https://pypi.org/project/pyjokes/) - for providing the jokes for the `joke` command
- [quoters](https://pypi.org/project/quoters/) - for providing random quotes for the `quote` command