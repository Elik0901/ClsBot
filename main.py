from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config

TOKEN = '6233891913:AAEnhx_96SR0wsiB4k-3da8XbC5h29ORhac'
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
