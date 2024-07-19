import requests
import random
from dotenv import load_dotenv
import os
import telegram

def download_image(img_url, img_path, params=None):
    response = requests.get(img_url, params)
    response.raise_for_status()

    with open(img_path, 'wb') as file:
        file.write(response.content)


def get_last_comic_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    last_comic_number = response['num']
    return last_comic_number


def main():
    last_comic_number = get_last_comic_number()
    num = random.randint(1, last_comic_number)
    url = f'https://xkcd.com/{num}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    image_url = response['img']
    filename = f'comic{num}.png'
    download_image(image_url, filename)
    comment = response['alt']
    load_dotenv()
    token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=token)
    with open(filename, 'rb') as photo:
        bot.send_photo(chat_id=tg_chat_id, photo=photo)
    bot.send_message(text=comment, chat_id=tg_chat_id)
    os.remove(filename)
            

if __name__ == '__main__':
    main()