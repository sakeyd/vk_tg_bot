
import os

from dotenv import load_dotenv
from telethon import TelegramClient, connection


load_dotenv()


# =========================
# Данные Telegram
# =========================

TG_TOKEN = os.getenv("TG_TOKEN")
TG_CHAT_ID = int(os.getenv("TG_CHAT_ID"))

TG_API_ID = int(os.getenv("TG_API_ID"))
TG_API_HASH = os.getenv("TG_API_HASH")


# =========================
# MTProto-прокси
# =========================

TG_PROXY_HOST = os.getenv("TG_PROXY_HOST")
TG_PROXY_PORT = int(os.getenv("TG_PROXY_PORT", "443"))
TG_PROXY_SECRET = os.getenv("TG_PROXY_SECRET")


# =========================
# Telegram-клиент
# =========================

client = TelegramClient(
    "telegram_bot",
    TG_API_ID,
    TG_API_HASH,

    # MTProto-прокси
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(
        TG_PROXY_HOST,
        TG_PROXY_PORT,
        TG_PROXY_SECRET,
    ),
)


# =========================
# Подключение
# =========================

async def init_telegram():

    if not client.is_connected():
        await client.connect()

    # Авторизация именно как бот
    if not await client.is_user_authorized():
        await client.sign_in(
            bot_token=TG_TOKEN
        )


# =========================
# Отправка текста
# =========================

async def send_to_telegram(text: str):

    try:

        await init_telegram()

        await client.send_message(
            TG_CHAT_ID,
            text,
            link_preview=False,
        )

    except Exception as error:

        print(
            "Ошибка Telegram:",
            error,
        )


# =========================
# Отправка одной фотографии
# =========================

async def send_photo_to_telegram(
    photo_url: str,
    caption: str | None = None,
):

    try:

        await init_telegram()

        await client.send_file(
            TG_CHAT_ID,
            photo_url,
            caption=caption,
        )

    except Exception as error:

        print(
            "Ошибка Telegram:",
            error,
        )


# =========================
# Отправка альбома
# =========================

async def send_photo_album_to_telegram(
    photo_urls: list[str],
    caption: str,
):

    try:

        await init_telegram()

        # Telegram позволяет отправлять
        # альбомами до 10 фотографий.
        for start in range(
            0,
            len(photo_urls),
            10,
        ):

            batch = photo_urls[
                start:start + 10
            ]

            # Подпись только у первой
            # фотографии первого альбома.
            current_caption = None

            if start == 0:
                current_caption = caption

            await client.send_file(
                TG_CHAT_ID,
                batch,
                caption=current_caption,
            )

    except Exception as error:

        print(
            "Ошибка Telegram:",
            error,
        )
