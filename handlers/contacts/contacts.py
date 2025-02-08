from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import contacts_menu, main_menu  # Клавиатура для контактов (с кнопкой назад)
router = Router()

# ✅ Обработчик кнопки "Контакты"
@router.callback_query(F.data == "contacts")
async def contacts(callback: CallbackQuery):
    # Отправляем информацию о контактах и клавиатуру с кнопкой "⬅️ Назад"
    await callback.message.answer(
        "📩 Контакты проекта:\n"
        "👤 @waiiikim\n"
        "👤 @araymaratova\n"
        "👤 @shaltyyn", 
        reply_markup=contacts_menu  # Отправляем клавиатуру с кнопкой назад
    )

    # Закрываем уведомление о нажатии кнопки
    await callback.answer()

# ✅ Обработчик кнопки "⬅️ Назад"
@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery):
    await callback.message.answer("Вы вернулись в главное меню.", reply_markup=main_menu)
    await callback.answer()
