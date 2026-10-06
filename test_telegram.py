
import asyncio

from telegram_client import init_telegram, client


async def main():

    print("Подключение к Telegram...")

    try:

        await init_telegram()

        print("Telegram подключен!")

        me = await client.get_me()

        print(
            "Подключено как:",
            me.username or me.first_name,
        )

    except Exception as error:

        print(
            "ОШИБКА:",
            repr(error),
        )

    finally:

        await client.disconnect()


asyncio.run(main())

