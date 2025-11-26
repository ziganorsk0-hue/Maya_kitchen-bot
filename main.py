import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Приветствие
@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Здравствуйте! 👋\n"
        "Я — бот кухни Майя.\n"
        "Готов помочь вам с заказом, замером или консультацией.\n\n"
        "Как вас зовут?"
    )

# Получаем имя
@dp.message()
async def get_name(message: Message):
    user_name = message.text
    await message.answer(
        f"Очень приятно, {user_name}! 😊\n\n"
        "Оставьте, пожалуйста, номер телефона, чтобы наш специалист связался с вами."
    )

    # Следующее сообщение пользователя будет обработано другой функцией
    dp.message.register(get_phone, F.text)

async def get_phone(message: Message):
    phone = message.text
    await message.answer(
        f"Спасибо! 📞 Мы получили ваш номер: {phone}\n\n"
        "Хотите записаться на бесплатный замер?"
    )

    dp.message.register(final_step, F.text)

async def final_step(message: Message):
    await message.answer(
        "Отлично! 🎉\n"
        "Наш менеджер свяжется с вами в ближайшее время.\n\n"
        "Спасибо, что выбрали нас!"
    )

async def main():
    print("Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
