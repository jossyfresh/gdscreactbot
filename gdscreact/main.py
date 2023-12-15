import asyncio
import logging
import sys
import json
import uuid
from os import getenv

from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import (
  KeyboardButton,
  Message,
  ReplyKeyboardMarkup,
  ReplyKeyboardRemove,
)

TOKEN = "6725669553:AAGx_TTCtDW8HqktD3HjsblewLQjVPMiFXE"
logging.basicConfig(level=logging.INFO)

jj_telegram_id = "923913833"
bot = Bot(token=TOKEN)

form_router = Router()

@form_router.message(CommandStart())
async def start_message(message: Message, state: FSMContext):
   jj_id = message.from_user.id
   print(jj_id)
   await message.answer(
    "Please Provide Your Excuse",reply_markup=ReplyKeyboardRemove(),)
   
@form_router.message()
async def send_to_jj(message:Message,state:FSMContext):
  returned_value = message.text
  username = message.from_user.username
  returned_value  = "@" + username + " " + returned_value
  await bot.send_message(chat_id=jj_telegram_id,text=returned_value)




async def main():
  
  dp = Dispatcher()  
  dp.include_router(form_router)
  await dp.start_polling(bot)
if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO, stream=sys.stdout)
  asyncio.run(main())