import logging

from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin, to_cyrillic

API_TOKEN = '5642990611:AAGf_EO6m2jmXZmz48xm7bJGifbpHIt1uiU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum Lotin-Kiril botiga xush kelibsiz!!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alykum")


@dp.message_handler()
async def tarjima(message: types.Message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    await message.answer(javob)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
