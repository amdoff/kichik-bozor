from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
import db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "👋 Salom!\n"
        "🛒 Telegram Marketplace Bot\n\n"
        "/add - mahsulot qo‘shish\n"
        "/list - mahsulotlar"
    )

@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    await message.answer("Mahsulot nomi va narxini yuboring:\nMasalan: Telefon - 2 000 000")

@dp.message_handler(lambda m: "-" in m.text)
async def save_product(message: types.Message):
    try:
        name, price = message.text.split("-")
        db.add_product(name.strip(), price.strip())
        await message.answer("✅ Mahsulot qo‘shildi")
    except:
        await message.answer("❌ Format noto‘g‘ri")

@dp.message_handler(commands=['list'])
async def list_products(message: types.Message):
    products = db.get_products()
    if not products:
        await message.answer("❌ Mahsulot yo‘q")
    else:
        text = "🛒 Mahsulotlar:\n\n"
        for p in products:
            text += f"📦 {p[0]} — 💰 {p[1]}\n"
        await message.answer(text)

if __name__ == "__main__":
    executor.start_polling(dp)