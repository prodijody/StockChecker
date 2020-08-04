import os
import requests
import time
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read("config.ini")

user_id = parser.get("telegram", "user_id")
bot_token = parser.get("telegram", "bot_token")


def send_announcments(bot_message, user):
    send_text = (
        "https://api.telegram.org/bot"
        + bot_token
        + "/sendMessage?chat_id="
        + user
        + "&text="
        + bot_message
    )
    response = requests.get(send_text)
    print(response.json())
    time.sleep(1)


bot_message = "IN STOCK"

send_announcments(bot_message, user_id)
