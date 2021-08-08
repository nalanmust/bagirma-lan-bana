from flask import Flask, render_template
from telegram_bot import TelethonBot
import asyncio


app = Flask(__name__)
bot = TelethonBot(3226017, "8702e11ddbf002c90b373da426332147")
loop = asyncio.get_event_loop()


@app.route("/")
def mainpage() -> str:
    return "sa"


@app.route("/api/<telegram_username>")
def api_page(telegram_username: str):
    info = loop.run_until_complete(
        bot.get_user_info(
            telegram_username
        )
    )

    return render_template(
        "svg.svg", info=info
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
