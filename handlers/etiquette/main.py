from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import etiquette_menu, back_to_etiquette_menu  # Клавиатура с кнопкой назад

router = Router()

# ✅ Основные правила общения в бизнес-среде
@router.callback_query(F.data == "etiquette_main")
async def etiquette_main(callback: CallbackQuery):
    await callback.message.answer(
        "💼 Основные правила общения в бизнес-среде:\n\n"
        "1️⃣ Используйте вежливые фразы и формулировки. "
        "Например, начинайте письма с приветствия и заканчивайте их благодарностью. "
        "На звонках используйте фразы вроде «Добрый день», «Спасибо за ваше время» и «Буду признателен за помощь».\n\n"
        "2️⃣ Соблюдайте уважение к собеседнику, избегайте агрессии и раздражения. "
        "Даже в сложных ситуациях сохраняйте спокойствие и старайтесь найти компромисс. "
        "Помните, что грубость может испортить деловые отношения.\n\n"
        "3️⃣ Не забывайте о правильном тоне и манере общения в письмах и на звонках. "
        "В письмах избегайте излишне эмоциональных выражений, а на звонках говорите четко и уверенно. "
        "Старайтесь не перебивать собеседника.\n\n"
        "4️⃣ Придерживайтесь нейтральных и позитивных тем в разговоре. "
        "Избегайте обсуждения политики, религии и личных тем, если это не уместно. "
        "Лучше сосредоточьтесь на рабочих вопросах и общих интересах.\n\n"
        "5️⃣ Следите за временем, чтобы не отвлекать собеседника лишний раз. "
        "Если вы договорились о звонке или встрече, начинайте вовремя и не затягивайте разговор. "
        "Уважайте время других людей.\n\n"
        "🔹 В бизнесе важно соблюдать такт и быть готовым к конструктивному диалогу. "
        "Следуя этим правилам, вы сможете выстроить прочные и уважительные отношения с коллегами и партнерами.",
        reply_markup=etiquette_menu  # Клавиатура с кнопкой назад
    )
    await callback.answer()

