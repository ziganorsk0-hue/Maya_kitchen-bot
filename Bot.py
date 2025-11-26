import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer("Бот работает! 🎉\n\nОтправь любое сообщение — я повторю.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ты отправил: {message.text}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
