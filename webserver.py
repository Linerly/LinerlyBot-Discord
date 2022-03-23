from threading import Thread

from flask import Flask

app = Flask("")


@app.route("/")
def home():
    return """
        <!DOCTYPE="html">
        <html>

        <head>
        <link rel="icon" href="https://linerly.tk/assets/linerlybot/linerlybot.png" type="image/png">
        <title>LinerlyBot</title>
        </head>

        <body style="width: 80%; margin: auto;">
        <br>

        <img alt="LinerlyBot logo" src="https://raw.githubusercontent.com/Linerly/linerlybot-rewritten/master/profile-picture.png" style="display: block; margin-left: auto; margin-right: auto; border-radius: 50%;" width="128" height="128">

        <h2 align="center">linerlybot-rewritten</h2>

        <p align="center">
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
        </body>

        </html>
    """


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
