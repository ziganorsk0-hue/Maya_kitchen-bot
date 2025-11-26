import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
import os

# ВАЖНО: токен берём из переменных среды Render
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден! Добавь переменную среды BOT_TOKEN в Render.")

# Инициализация
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Бот успешно запущен 🔥")

# Ловим остальные сообщения
@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты сказал: {message.text}")

# Основная функция
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
