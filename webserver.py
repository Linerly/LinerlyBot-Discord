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

        <body style="width: 75%; margin: auto;">
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

        <p class="has-line-data" data-line-start="6" data-line-end="7">The new version of LinerlyBot with <a href="http://discord.py">discord.py</a>.</p>
        <p class="has-line-data" data-line-start="8" data-line-end="9"><a href="https://discord.com/oauth2/authorize?client_id=529566778293223434&amp;permissions=2147485696&amp;scope=bot+applications.commands"><img src="https://img.shields.io/badge/-Add%20LinerlyBot%20to%20your%20Discord%20server!-1e90ff?style=for-the-badge" alt="Invite LinerlyBot"></a></p>

        <hr>
        
        <h1 class="code-line" data-line-start=12 data-line-end=13 ><a id="Features_12"></a>Features</h1>
        <ul>
        <li class="has-line-data" data-line-start="13" data-line-end="14">Informational commands such as the <code>help</code>, <code>info</code>, <code>ping</code>, and the <code>about</code> command.</li>
        <li class="has-line-data" data-line-start="14" data-line-end="15">Fun commands such as the <code>joke</code> and the <code>feeling</code> command.</li>
        <li class="has-line-data" data-line-start="15" data-line-end="16">Other miscellaneous such as the <code>quote</code> command.</li>
        <li class="has-line-data" data-line-start="16" data-line-end="18"><s>Gold as the currency for LinerlyBot.</s> Still not working, for now.</li>
        </ul>
        <hr>
        <h1 class="code-line" data-line-start=20 data-line-end=21 ><a id="Todo_20"></a>To-do</h1>
        <ul>
        <li class="has-line-data" data-line-start="21" data-line-end="23">Adding moderation commands, plus some other miscellaneous commands as well.</li>
        </ul>
        <hr>
        <h1 class="code-line" data-line-start=25 data-line-end=26 ><a id="Some_issues_when_using_LinerlyBot_25"></a>Some issue(s) when using LinerlyBot</h1>
        <ul>
        <li class="has-line-data" data-line-start="26" data-line-end="27">Occasionally, you might get the “Invalid interaction application command” error when using some slash commands, if you try again, it will work again like normal.</li>
        <li class="has-line-data" data-line-start="27" data-line-end="29">Currency commands don’t really work just yet, I haven’t figure out how to handle the <code>KeyError</code> error.</li>
        </ul>
        <hr>
        <h1 class="code-line" data-line-start=31 data-line-end=32 ><a id="Extra_notes_31"></a>Extra notes</h1>
        <ul>
        <li class="has-line-data" data-line-start="32" data-line-end="33">Now LinerlyBot is hosted on Replit.</li>
        <li class="has-line-data" data-line-start="33" data-line-end="35">LinerlyBot also uses the <a href="https://docs.replit.com/misc/database">Replit Database</a> as well.</li>
        </ul>
        <hr>
        <h1 class="code-line" data-line-start=37 data-line-end=38 ><a id="Additional_Python_libraries_used_for_LinerlyBot_37"></a>Additional Python libraries used for LinerlyBot</h1>
        <p class="has-line-data" data-line-start="39" data-line-end="40">Here is a list of the additional Python libraries used for LinerlyBot.</p>
        <ul>
        <li class="has-line-data" data-line-start="41" data-line-end="42"><a href="https://pypi.org/project/discord.py/">discord.py</a> - duh, you need it</li>
        <li class="has-line-data" data-line-start="42" data-line-end="43"><a href="https://pypi.org/project/discord-py-slash-command/">discord-py-slash-command</a> - for handling slash commands</li>
        <li class="has-line-data" data-line-start="43" data-line-end="44"><a href="https://pypi.org/project/distro/">distro</a> - for detecting what OS the bot is running on</li>
        <li class="has-line-data" data-line-start="44" data-line-end="45"><a href="https://pypi.org/project/pyjokes/">pyjokes</a> - for providing the jokes for the <code>joke</code> command</li>
        <li class="has-line-data" data-line-start="45" data-line-end="46"><a href="https://pypi.org/project/quoters/">quoters</a> - for providing random quotes for the <code>quote</code> command</li>
        <li class="has-line-data" data-line-start="46" data-line-end="47"><a href="https://pypi.org/project/webserver/">webserver</a> - for keeping the bot online (<code>keep_alive()</code>)</li>
        <li class="has-line-data" data-line-start="47" data-line-end="49"><a href="https://pypi.org/project/replit/">replit</a> -  just for providing the <a href="https://docs.replit.com/misc/database">Replit Database</a> client</li>
        </ul>
        <p class="has-line-data" data-line-start="49" data-line-end="50">(there might be more, just look at the <a href="https://github.com/Linerly/linerlybot-rewritten/blob/master/poetry.lock">poetry.lock</a> file if you want)</p>
        </body>

        </html>
    """


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
