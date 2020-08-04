import os
import requests
import time

bot_token = "1383192732:AAHATHy1V8dVef4wW8U4_lT7JsM4T_iK_wE"


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

send_announcments(bot_message, "1332193862")
