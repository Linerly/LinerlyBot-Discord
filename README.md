![linerlybot logo](https://raw.githubusercontent.com/Linerly/linerlybot-rewritten/master/profile-picture.png)

<h2 align="center">linerlybot-rewritten</h2>

<p align="center">
    <a href="https://discord.gg/a9Sy7gE"><img alt="Discord Server" src="https://img.shields.io/discord/551683447026876418?logoColor=1e90ff&style=flat"></a>
    <a href="https://github.com/Linerly/linerlybot-rewritten/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Linerly/linerlybot-rewritten?style=flat"></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat"></a>
    <a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
</p>

---

The new version of LinerlyBot with discord.py.

[![Invite LinerlyBot](https://img.shields.io/badge/-Add%20LinerlyBot%20to%20your%20Discord%20server!-1e90ff?style=for-the-badge)](https://discord.com/oauth2/authorize?client_id=529566778293223434&permissions=2147485696&scope=bot+applications.commands)

---

# Features
- Informational commands such as the `help`, `info`, `ping`, and the `about` command.
- Fun commands such as the `joke` and the `feeling` command.
- Other miscellaneous such as the `quote` command.
- ~~Gold as the currency for LinerlyBot.~~ Still not working, for now.

---

# To-do
- Adding moderation commands, plus some other miscellaneous commands as well.

---

# Some issue(s) when using LinerlyBot
- Occasionally, you might get the "Invalid interaction application command" error when using some slash commands, if you try again, it will work again like normal.
- Currency commands don't really work just yet, I haven't figure out how to handle the `KeyError` error.

---

# Extra notes
- Now LinerlyBot is hosted on Replit.
- LinerlyBot also uses the [Replit Database](https://docs.replit.com/misc/database) as well.

---

# Additional Python libraries used for LinerlyBot

Here is a list of the additional Python libraries used for LinerlyBot.

- [discord.py](https://pypi.org/project/discord.py/) - duh, you need it
- [discord-py-slash-command](https://pypi.org/project/discord-py-slash-command/) - for handling slash commands
- [distro](https://pypi.org/project/distro/) - for detecting what OS the bot is running on
- [pyjokes](https://pypi.org/project/pyjokes/) - for providing the jokes for the `joke` command
- [quoters](https://pypi.org/project/quoters/) - for providing random quotes for the `quote` command
- [webserver](https://pypi.org/project/webserver/) - for keeping the bot online (`keep_alive()`)
- [replit](https://pypi.org/project/replit/) -  just for providing the [Replit Database](https://docs.replit.com/misc/database) client

(there might be more, just look at the [poetry.lock](https://github.com/Linerly/linerlybot-rewritten/blob/master/poetry.lock) file if you want)