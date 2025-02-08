from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import main_menu, lexicon_menu, etiquette_menu, email_menu
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

# Команда /start
@router.message(F.text == "/start")
async def send_welcome(message: Message):
    await message.answer("👋 Добро пожаловать! Выберите раздел:", reply_markup=main_menu)

# Обработчик кнопки "Обучение деловой лексике"
@router.callback_query(F.data == "lexicon")
async def show_lexicon_menu(callback: CallbackQuery):
    await callback.message.edit_text("📚 Выберите тему:", reply_markup=lexicon_menu)

# Обработчик кнопки "Советы по деловому этикету"
@router.callback_query(F.data == "etiquette")
async def show_etiquette_menu(callback: CallbackQuery):
    await callback.message.edit_text("📚 Выберите тему:", reply_markup=etiquette_menu)

# Универсальный обработчик для кнопок "Назад"
@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("👋 Добро пожаловать! Выберите раздел:", reply_markup=main_menu)
    await callback.answer()

# Обработчик кнопки "Назад" в разделе этикета
@router.callback_query(F.data == "back_to_etiquette_menu")
async def back_to_etiquette(callback: CallbackQuery):
    await callback.message.edit_text("📚 Выберите тему:", reply_markup=etiquette_menu)
    await callback.answer()

# Обработчик кнопки "Шаблоны письма"
@router.callback_query(F.data == "templates")
async def show_email_menu(callback: CallbackQuery):
    await callback.message.edit_text("📩 Выберите категорию письма:", reply_markup=email_menu)

# Обработчик кнопки "Назад" в разделе шаблонов
@router.callback_query(F.data == "back_to_templates_menu")
async def back_to_templates(callback: CallbackQuery):
    await callback.message.edit_text("📩 Выберите категорию письма:", reply_markup=email_menu)
    await callback.answer()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в наш бот! Выберите опцию из меню ниже.",
        reply_markup=main_menu  # Главное меню с кнопками
    )


