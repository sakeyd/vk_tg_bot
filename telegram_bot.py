from telethon import events, Button

from telegram_client import client, init_telegram


# =========================
# Главное меню
# =========================

def main_menu():

    return [
        [
            Button.inline("📚 ДЗ", b"homework"),
            Button.inline("📅 Расписание", b"schedule"),
        ],
        [
            Button.inline("⏰ Дедлайны", b"deadlines"),
            Button.inline("📢 Важное", b"important"),
        ],
        [
            Button.inline("ℹ️ Помощь", b"help"),
        ],
    ]


# =========================
# Меню ДЗ
# =========================

def homework_menu():

    return [
        [
            Button.inline("📅 Сегодня", b"homework_today"),
            Button.inline("➡️ Завтра", b"homework_tomorrow"),
        ],
        [
            Button.inline("📆 На неделю", b"homework_week"),
        ],
        [
            Button.inline("◀️ Назад", b"main"),
        ],
    ]


# =========================
# Меню расписания
# =========================

def schedule_menu():

    return [
        [
            Button.inline("📅 Сегодня", b"schedule_today"),
            Button.inline("➡️ Завтра", b"schedule_tomorrow"),
        ],
        [
            Button.inline("📆 На неделю", b"schedule_week"),
        ],
        [
            Button.inline("◀️ Назад", b"main"),
        ],
    ]


# =========================
# Главное меню
# =========================

async def show_main_menu(event):

    text = (
        "🤖 <b>Учебный бот</b>\n\n"
        "Выбери нужный раздел:"
    )

    await event.edit(
        text,
        buttons=main_menu(),
        parse_mode="html",
    )


# =========================
# Меню ДЗ
# =========================

async def show_homework_menu(event):

    text = (
        "📚 <b>Домашние задания</b>\n\n"
        "Что посмотреть?"
    )

    await event.edit(
        text,
        buttons=homework_menu(),
        parse_mode="html",
    )


# =========================
# Меню расписания
# =========================

async def show_schedule_menu(event):

    text = (
        "📅 <b>Расписание</b>\n\n"
        "Что посмотреть?"
    )

    await event.edit(
        text,
        buttons=schedule_menu(),
        parse_mode="html",
    )


# =========================
# Дедлайны
# =========================

async def show_deadlines(event):

    text = (
        "⏰ <b>Дедлайны</b>\n\n"
        "Пока дедлайнов нет.\n\n"
        "Позже здесь будут отображаться "
        "ближайшие задания и сроки сдачи."
    )

    await event.edit(
        text,
        buttons=[
            [
                Button.inline("◀️ Назад", b"main"),
            ]
        ],
        parse_mode="html",
    )


# =========================
# Важное
# =========================

async def show_important(event):

    text = (
        "📢 <b>Важное</b>\n\n"
        "Позже здесь будут отображаться "
        "важные сообщения группы."
    )

    await event.edit(
        text,
        buttons=[
            [
                Button.inline("◀️ Назад", b"main"),
            ]
        ],
        parse_mode="html",
    )


# =========================
# Помощь
# =========================

async def show_help(event):

    text = (
        "ℹ️ <b>Помощь</b>\n\n"
        "📚 ДЗ — домашние задания\n"
        "📅 Расписание — расписание занятий\n"
        "⏰ Дедлайны — сроки сдачи\n"
        "📢 Важное — важные сообщения\n\n"
        "Позже добавим команды и "
        "понимание обычных сообщений."
    )

    await event.edit(
        text,
        buttons=[
            [
                Button.inline("◀️ Назад", b"main"),
            ]
        ],
        parse_mode="html",
    )


# =========================
# Команда /start
# =========================

@client.on(events.NewMessage(pattern=r"^/start$"))
async def start_handler(event):

    # Пока работаем только в личных сообщениях
    if not event.is_private:
        return

    await event.respond(
        "🤖 <b>БОТ КСУ-2</b>\n\n"
        "Выбери нужный раздел:",
        buttons=main_menu(),
        parse_mode="html",
    )


# =========================
# Команда /меню
# =========================

@client.on(events.NewMessage(pattern=r"^/меню$"))
async def menu_handler(event):

    if not event.is_private:
        return

    await event.respond(
        "🤖 <b>Учебный бот</b>\n\n"
        "Выбери нужный раздел:",
        buttons=main_menu(),
        parse_mode="html",
    )


# =========================
# Обработка кнопок
# =========================

@client.on(events.CallbackQuery)
async def callback_handler(event):

    data = event.data.decode("utf-8")

    if data == "main":

        await show_main_menu(event)

    elif data == "homework":

        await show_homework_menu(event)

    elif data == "schedule":

        await show_schedule_menu(event)

    elif data == "deadlines":

        await show_deadlines(event)

    elif data == "important":

        await show_important(event)

    elif data == "help":

        await show_help(event)

    elif data == "homework_today":

        await event.edit(
            "📚 <b>ДЗ на сегодня</b>\n\n"
            "Пока база домашних заданий пустая.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"homework"),
                ]
            ],
            parse_mode="html",
        )

    elif data == "homework_tomorrow":

        await event.edit(
            "📚 <b>ДЗ на завтра</b>\n\n"
            "Пока база домашних заданий пустая.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"homework"),
                ]
            ],
            parse_mode="html",
        )

    elif data == "homework_week":

        await event.edit(
            "📚 <b>ДЗ на неделю</b>\n\n"
            "Пока база домашних заданий пустая.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"homework"),
                ]
            ],
            parse_mode="html",
        )

    elif data == "schedule_today":

        await event.edit(
            "📅 <b>Расписание на сегодня</b>\n\n"
            "Расписание пока не добавлено.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"schedule"),
                ]
            ],
            parse_mode="html",
        )

    elif data == "schedule_tomorrow":

        await event.edit(
            "📅 <b>Расписание на завтра</b>\n\n"
            "Расписание пока не добавлено.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"schedule"),
                ]
            ],
            parse_mode="html",
        )

    elif data == "schedule_week":

        await event.edit(
            "📅 <b>Расписание на неделю</b>\n\n"
            "Расписание пока не добавлено.",
            buttons=[
                [
                    Button.inline("◀️ Назад", b"schedule"),
                ]
            ],
            parse_mode="html",
        )


# =========================
# Запуск Telegram-бота
# =========================

async def main():

    print("Подключение Telegram...")

    await init_telegram()

    print("Telegram-бот запущен!")

    await client.run_until_disconnected()


client.loop.run_until_complete(main())