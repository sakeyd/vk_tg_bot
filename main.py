import os

from dotenv import load_dotenv
from vkbottle.bot import Bot, Message

from media_handler import get_photo_urls

from telegram_client import (
    send_to_telegram,
    send_photo_to_telegram,
    send_photo_album_to_telegram,
)


load_dotenv()

VK_TOKEN = os.getenv("VK_TOKEN")


if not VK_TOKEN:
    raise ValueError("VK_TOKEN не найден в .env")


bot = Bot(token=VK_TOKEN)


@bot.on.message()
async def message_handler(message: Message):

    text = message.text or ""

    # Нет #важно — игнорируем
    if "#важно" not in text.lower():
        return

    # Убираем #важно и проверяем, осталось ли сообщение
    clean_text = text.lower().replace("#важно", "").strip()

    # Только #важно без текста — игнорируем
    if not clean_text:
        return

    print("1")

    # Получаем автора сообщения
    author_id = message.from_id

    users = await bot.api.users.get(
        user_ids=[author_id]
    )

    if users:
        author = users[0]

        author_name = (
            f"{author.first_name} "
            f"{author.last_name}"
        )

    else:
        author_name = "Неизвестный пользователь"

    # ID сообщения VK
    message_id = message.conversation_message_id

    # Ссылка на сообщение VK
    link = (
        f"https://vk.com/im?sel=c{message.peer_id}"
        f"&msgid={message_id}"
    )

    # Формируем сообщение для Telegram
    telegram_text = (
        f"📌 ВАЖНО\n\n"
        f"👤 {author_name}\n\n"
        f"{text}\n\n"
        f"🔗 Оригинал ВК:\n{link}"
    )

    # Получаем фотографии
    photo_urls = get_photo_urls(message)

    if photo_urls:

        if len(photo_urls) == 1:

            await send_photo_to_telegram(
                photo_urls[0],
                telegram_text,
            )

        else:

            await send_photo_album_to_telegram(
                photo_urls,
                telegram_text,
            )

    else:

        await send_to_telegram(
            telegram_text
        )

print("VK бот запущен...")

bot.run()