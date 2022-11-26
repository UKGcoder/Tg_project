from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from settings.settings import TOKEN_CLIENT

TOKEN = TOKEN_CLIENT
bot = Bot(TOKEN)
storage = RedisStorage2(host='redis', port=6379, db=10)
dp = Dispatcher(bot, storage=storage)
