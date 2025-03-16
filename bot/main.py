import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, WebAppInfo, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def any_message(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text='Открыть',
            web_app=WebAppInfo(url="https://thesortage.space")
        )
    )

    await message.answer(
        text='Привет! Узнай сколько осталось до твоего дня рождения, открыв приложение',
        reply_markup=builder.as_markup()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
