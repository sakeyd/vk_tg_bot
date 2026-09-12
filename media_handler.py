from typing import List

from vkbottle.bot import Message


def get_photo_urls(message: Message) -> List[str]:

    photo_urls = []

    if not message.attachments:
        return photo_urls

    for attachment in message.attachments:

        if not attachment.photo:
            continue

        photo = attachment.photo

        if not photo.sizes:
            continue

        # Берём самое большое изображение
        largest = max(
            photo.sizes,
            key=lambda size: size.width * size.height
        )

        photo_urls.append(largest.url)

    return photo_urls