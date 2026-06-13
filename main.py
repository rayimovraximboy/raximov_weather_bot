import os  # Qo'shildi (os.getenv ishlashi uchun)
import requests  # Bor edi
from dotenv import load_dotenv  # Qo'shildi (load_dotenv ishlashi uchun)
from aiogram import Bot, Dispatcher  # Bor edi
from aiogram.filters import Command  # Bor edi
from aiogram.types import Message  # Bor edi

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

bot = Bot(token=TOKEN)  # ← Bot ni bu yerda yarating
dp = Dispatcher()

# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    text = "Salom bu bot orqali ob-havo ma'lumotlarini olishingiz mumkin. Xohlagan shahar nomini kiriting."
    await message.answer(text)

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer("Sizga qanday yordam kerak")

@dp.message()
async def echo_handler(message: Message) -> None:
    city_name = message.text
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={API_KEY}")
    if response.status_code == 200:
        # Bu yerda qavs o'rni to'g'rilandi: .json() dan keyin qavs ochib-yopildi
        data = response.json()['main']['temp']
        await message.answer(f"Bugun {city_name.capitalize()}da {data} gradus ob-havo")
    else:
        await message.answer("Shahar nomi xato kiritildi yoki shahar topilmadi")

# Run the bot
async def main() -> None:
    await dp.start_polling(bot)  # ← bot ni shu yerga bering

if __name__ == "__main__":
    import asyncio  # Qo'shildi (asyncio.run ishlashi uchun)
    asyncio.run(main())