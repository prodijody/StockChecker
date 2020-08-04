import os
import requests
import time
from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")

user_id = parser.get("telegram", "user_id")
bot_token = parser.get("telegram", "bot_token")
print(user_id,bot_token)

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

def get_stock():
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Origin': 'https://aodour.pk',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://aodour.pk/brand/the-ordinary/1',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'If-None-Match': 'W/^\\^c91-Xe06tNX/fqUoa9xHU2uK8t/Ez1I^\\^',
    }

    params = (
        ('variationSlug', '1'),
    )

    response = requests.get('https://nodeapi.aodour.pk/api/productdetail/product-data', headers=headers, params=params)

    return int(response.json()["result"]["product_variations"][0]["available_stock"])

if __name__ == "__main__":
    if get_stock() > 0:
        send_announcments(f"IN STOCK https://aodour.pk/brand/the-ordinary/1", user_id)
