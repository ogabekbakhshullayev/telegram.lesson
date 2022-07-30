from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.startKeyboard import startmenu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Telefon raqamingiz va manziligizni kiriting", reply_markup=startmenu)
