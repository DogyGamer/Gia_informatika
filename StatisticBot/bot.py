import asyncio
import logging
import sys
import os

from scanfiles import getLastSolutionDate, scanFiles


from typing import *

from aiogram import Bot, Dispatcher, Router, types, BaseMiddleware
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import mysql.connector as conn
import datetime
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6969792699:AAFpKOD5vlrTv3ijeUCu7Ld5COWumJ4nmjY"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

class AuthMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.admins = [572745992]

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        if user_id in self.admins:
            return await handler(event, data)
        else:
            await event.answer(f"❌<b>You are not allowed❌</b>\nYour id: {user_id}")
dp.message.middleware(AuthMiddleware())

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("scan"))
async def echo_handler(message: types.Message) -> None:
    last_date = getLastSolutionDate()
    await message.answer(f"<b>Начинаем сканирование</b>\nДата последнего решения: <i>{last_date.isoformat()}</i>")
    
    by_folder_id, values = scanFiles(last_date)
    msg = "🧑‍🦽Найденные файлы, с момента последнего решения🧑‍🦽"
    for folder in by_folder_id.keys():
        msg += f"\n*Задание {folder}:*"
        for filename, is_correct in by_folder_id[folder]:
            name = filename.replace(".", "\.")
            if is_correct == None:
                emoji = "❔"
            elif is_correct:
                emoji = "✅"
            else:
                emoji = "❌"
            msg += f"\n • {name} {emoji}"
        msg += "\n"
    await message.answer(msg, parse_mode="MarkdownV2")
    
    
@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())