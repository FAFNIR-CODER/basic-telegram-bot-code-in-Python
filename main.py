import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv
import random
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup


load_dotenv()
token = os.getenv("token")

bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="привет"),KeyboardButton(text="пока"),],[KeyboardButton(text="как делишки?")]],resize_keyboard=True)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("ты запустил меня!", reply_markup=main_keyboard)

@dp.message(F.text == "привет")
async def reply_hello(message: Message):
    await message.answer("хелоу!")

@dp.message(F.text == "пока")
async def reply_bye(message: Message):
    await message.answer("Завтра точно будет лучше, чем вчера....")

@dp.message(F.text == "как делишки?")
async def reply_how_are_you(message: Message):
    await message.answer("я же робот")


# 2

colors_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Красный")],
        [KeyboardButton(text="Зелёный")],
        [KeyboardButton(text="Синий")],
    ],
    resize_keyboard=True
)

@dp.message(Command("colors"))
async def colors(message: Message):
    await message.answer("Выберите цвет:", reply_markup=colors_keyboard)

@dp.message(F.text == "Красный")
async def red_answer(message: Message):
    await message.answer("🟥")

@dp.message(F.text == "Зелёный")
async def green_answer(message: Message):
    await message.answer("🟩")

@dp.message(F.text == "Синий")
async def blue_answer(message: Message):
    await message.answer("🟦")
#4

lang_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Python", callback_data="Python")],
        [InlineKeyboardButton(text="Java", callback_data="Java")],
        [InlineKeyboardButton(text="JavaScript", callback_data="JavaScript")],
    ]
)
@dp.message(Command("lang"))
async def choose(message: Message):
    await message.answer("выберите язык программирования", reply_markup=lang_keyboard)

@dp.callback_query(F.data.in_(["Python", "Java", "JavaScript"]))
async def select(callback: CallbackQuery):
    await callback.message.answer(f"вы выбрали язык {callback.data}")
    await callback.answer()

#5

inline_nums_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
        ],
        [
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
            InlineKeyboardButton(text="6", callback_data="6"),
        ],
    ])
@dp.message(Command("nums"))
async def send_inline_nums(message: Message):
    await message.answer("Выберите кнопку:", reply_markup=inline_nums_keyboard)

@dp.callback_query(F.data.in_(["1", "2", "3", "4", "5", "6"]))
async def num_selected(callback: CallbackQuery):
    await callback.message.answer(f"Вы нажали на кнопку {callback.data}")
    await callback.answer()
#3 я перенес его потому что 4 и 5 не работали(ии подсказал)
@dp.message(Command("numbers"))
async def numbers(message: Message):
    await message.answer("Введите число:")

@dp.message(F.text)
async def numbers_buttons(message: Message):
    if message.text.isdigit():
        count = int(message.text)
        buttons = []

        for _ in range(count):
            random_num = str(random.randint(1, 100))
            buttons.append([KeyboardButton(text=random_num)])

        numbers_keyboard = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True
        )
        await message.answer("Ваши кнопки:", reply_markup=numbers_keyboard)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
async def main():
    await dp.start_polling(bot)

asyncio.run(main())




