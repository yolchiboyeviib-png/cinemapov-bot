import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Telegram Bot Token va Yopiq Baza Kanal ID si
API_TOKEN = '8824829774:AAFCp8RHRdCriOyArwfXbYvtFFb3oTuOoc8'
STORAGE_CHANNEL_ID = -1002145892011  # O'zingizning yopiq kanalingiz ID si

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "🍿 **CinemaPOV Bot'ga xush kelibsiz!**\n\n"
        "Kino tomosha qilish uchun kino kodini yuboring (Masalan: `1`):"
    )

@dp.message(F.text.isdigit())
async def send_movie(message: types.Message):
    code = int(message.text)
    try:
        await bot.copy_message(
            chat_id=message.chat.id,
            from_chat_id=STORAGE_CHANNEL_ID,
            message_id=code
        )
    except Exception:
        await message.answer("❌ Bu kod bo'yicha kino topilmadi.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
