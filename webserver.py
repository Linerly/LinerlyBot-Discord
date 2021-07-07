from threading import Thread

from flask import Flask

app = Flask("")


@app.route("/")
def home():
    return """
        <!DOCTYPE="html">
        <html>

        <head>
        <link rel="icon" href="https://linerly.github.io/assets/linerlybot/linerlybot.png" type="image/png">
        <title>LinerlyBot Repl Page</title>
        </head>

        <body style="width: 80%; margin: auto;">
        <style>
            figure message {
                top: 0;
                left: 0;
                position: absolute;
            }
        </style>
  
        <style>
            #message {
                margin: 0;
                padding: 12px 15px;
                background-color: #1e90ff;
                color: #fff;
                text-align: center;
                font-family: sans-serif;
                font-size: 13px;
            }
        </style>

        <p id="message">You're in LinerlyBot's Replit site. <a href="https://linerly.github.io/linerlybot">Click here to go to LinerlyBot's main page!</a></p>

        <br>

        <img alt="LinerlyBot logo" src="https://raw.githubusercontent.com/Linerly/linerlybot-rewritten/master/profile-picture.png" style="display: block; margin-left: auto; margin-right: auto; border-radius: 50%;" width="128" height="128">

        <h2 align="center">linerlybot-rewritten</h2>

        <p align="center">
            <a href="https://discord.gg/a9Sy7gE"><img alt="Discord Server" src="https://img.shields.io/discord/551683447026876418?logoColor=1e90ff&style=flat"></a>
            <a href="https://github.com/Linerly/linerlybot-rewritten/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Linerly/linerlybot-rewritten?style=flat"></a>
            <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat"></a>
            <a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
        </p>

        <hr>

        <p>The new version of LinerlyBot with <a href="https://discordpy.readthedocs.io/en/stable">discord.py</a>.</p>
        <p><a href="https://discord.com/oauth2/authorize?client_id=529566778293223434&amp;permissions=2147485696&amp;scope=bot+applications.commands"><img src="https://img.shields.io/badge/-Add%20LinerlyBot%20to%20your%20Discord%20server!-1e90ff?style=for-the-badge" alt="Invite LinerlyBot"></a></p>

        <hr>
        
        <h1>Features</h1>
        <ul>
        <li>Informational commands such as the <code>help</code>, <code>info</code>, <code>ping</code>, and the <code>about</code> command.</li>
        <li>Fun commands such as the <code>joke</code> and the <code>feeling</code> command.</li>
        <li>Other miscellaneous such as the <code>quote</code> command.</li>
        <li>Gold as the currency for LinerlyBot.</li>
        </ul>
        <hr>
        <h1>To-do</h1>
        <ul>
        <li>Adding moderation commands, plus some other miscellaneous commands as well.</li>
        </ul>
        <hr>
        <h1>Some issue(s) when using LinerlyBot</h1>
        <ul>
        <li>Occasionally, you might get the “Invalid interaction application command” error when using some slash commands, if you try again, it will work again like normal.</li>
        <li>Currency commands don’t really work just yet, I haven’t figure out how to handle the <code>KeyError</code> error.</li>
        </ul>
        <hr>
        <h1>Extra notes</h1>
        <ul>
        <li>Now LinerlyBot is hosted on Replit.</li>
        <li>LinerlyBot also uses the <a href="https://docs.replit.com/misc/database">Replit Database</a> as well.</li>
        </ul>
        <hr>
        <h1>Additional Python libraries used for LinerlyBot</h1>
        <p>Here is a list of the additional Python libraries used for LinerlyBot.</p>
        <ul>
        <li><a href="https://pypi.org/project/discord.py/">discord.py</a> - duh, you need it</li>
        <li><a href="https://pypi.org/project/discord-py-slash-command/">discord-py-slash-command</a> - for handling slash commands</li>
        <li><a href="https://pypi.org/project/distro/">distro</a> - for detecting what OS the bot is running on</li>
        <li><a href="https://pypi.org/project/pyjokes/">pyjokes</a> - for providing the jokes for the <code>joke</code> command</li>
        <li><a href="https://pypi.org/project/quoters/">quoters</a> - for providing random quotes for the <code>quote</code> command</li>
        <li><a href="https://pypi.org/project/webserver/">webserver</a> - for keeping the bot online (<code>keep_alive()</code>)</li>
        <li><a href="https://pypi.org/project/replit/">replit</a> -  just for providing the <a href="https://docs.replit.com/misc/database">Replit Database</a> client</li>
        </ul>
        <p>(there might be more, just look at the <a href="https://github.com/Linerly/linerlybot-rewritten/blob/master/poetry.lock">poetry.lock</a> file if you want)</p>
        </body>

        </html>
    """


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
