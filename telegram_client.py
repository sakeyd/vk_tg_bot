import os
import json

import httpx

from dotenv import load_dotenv


load_dotenv()


TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = os.getenv("TG_CHAT_ID")


async def send_to_telegram(text: str):

    url = (
        f"https://api.telegram.org/"
        f"bot{TG_TOKEN}/sendMessage"
    )

    data = {
        "chat_id": TG_CHAT_ID,
        "text": text,
        "disable_web_page_preview": True,
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            data=data,
        )

    if response.status_code != 200:

        print(
            "Ошибка Telegram:",
            response.text,
        )


async def send_photo_to_telegram(
    photo_url: str,
    caption: str | None = None,
):

    url = (
        f"https://api.telegram.org/"
        f"bot{TG_TOKEN}/sendPhoto"
    )

    data = {
        "chat_id": TG_CHAT_ID,
        "photo": photo_url,
    }

    if caption:
        data["caption"] = caption

    async with httpx.AsyncClient() as client:

        response = await client.post(
            url,
            data=data,
        )

    if response.status_code != 200:

        print(
            "Ошибка Telegram:",
            response.text,
        )


async def send_photo_album_to_telegram(
    photo_urls: list[str],
    caption: str,
):

    url = (
        f"https://api.telegram.org/"
        f"bot{TG_TOKEN}/sendMediaGroup"
    )

    # Telegram разрешает максимум 10 фотографий
    # в одном альбоме
    for start in range(0, len(photo_urls), 10):

        batch = photo_urls[start:start + 10]

        media = []

        for index, photo_url in enumerate(batch):

            photo = {
                "type": "photo",
                "media": photo_url,
            }

            # Подпись только у первой фотографии
            # самого первого альбома
            if start == 0 and index == 0:
                photo["caption"] = caption

            media.append(photo)

        data = {
            "chat_id": TG_CHAT_ID,
            "media": json.dumps(media),
        }

        async with httpx.AsyncClient() as client:

            response = await client.post(
                url,
                data=data,
            )

        if response.status_code != 200:

            print(
                "Ошибка Telegram:",
                response.text,
            )