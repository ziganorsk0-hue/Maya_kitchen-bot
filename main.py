import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.executor import start_webhook
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# === Handlers ===
@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer("Бот работает на Render! 🎉")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ты отправил: {message.text}")

# === Webhook settings ===
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL") + WEBHOOK_PATH

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", 10000))

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == "__main__":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=HOST,
        port=PORT
    )
