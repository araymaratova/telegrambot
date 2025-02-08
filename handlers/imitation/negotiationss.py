import random
from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram import types
from keyboards import imitation_menu, main_menu
from aiogram import Dispatcher

router = Router()

# Список сценариев для переговоров
negotiation_scenarios = [
    "💼 Вам предложили скидку 5%, но вы хотите 10%. Как ответите?",
    "📅 Клиент требует выполнить заказ за 3 дня, но вам нужно 7. Как аргументируете?",
    "💰 Вы ведете переговоры о зарплате. Как убедите работодателя повысить её?",
    "📉 Партнер хочет уменьшить бюджет проекта. Как защитите свое предложение?",
    "📦 Поставщик задерживает доставку. Как убедите его ускорить процесс?",
    "📊 Ваш руководитель сомневается в новой стратегии. Как убедите его?",
    "🔄 Коллега не выполняет свою часть работы. Как проведете переговоры?",
    "📍 Клиент хочет эксклюзивные условия, но компания не готова. Как ответите?",
    "📈 Вы продаете услугу, но клиент сомневается в её эффективности. Как убеждаете?",
    "📜 Вы хотите подписать контракт, но клиент выдвигает сложные условия. Как поступите?"
]

@router.callback_query(lambda c: c.data == "imitation")
async def imitation_negotiations(callback_query: CallbackQuery):
    # Случайный выбор одного сценария
    random_scenario = random.choice(negotiation_scenarios)
    await callback_query.message.answer(
        f"Ситуация для переговоров:\n\n{random_scenario}",
        reply_markup=imitation_menu  # Здесь будет клавиатура с кнопкой "Назад"
    )
    await callback_query.answer()

# Словарь с ключевыми словами
keywords = {
    "скидка": ["скидка", "компромисс", "альтернатива", "обоснование"],
    "срок": ["срок", "перенос", "гибкость", "оптимизация"],
    "зарплата": ["зарплата", "достижения", "опыт", "аргументы"],
    "бюджет": ["бюджет", "расходы", "приоритеты", "обоснование"],
    "доставка": ["доставка", "задержка", "ускорить", "решение"],
    "стратегия": ["стратегия", "анализ", "план", "данные"],
    "работа": ["команда", "ответственность", "обязанности", "распределение"],
    "эксклюзив": ["уникальные условия", "взаимовыгода", "переговоры"],
    "услуга": ["польза", "качество", "отзывы", "доказательства"],
    "контракт": ["подписание", "уступки", "условия", "переговоры"]
}

# Оценка ответа пользователя
def evaluate_response(user_response):
    score = 0
    user_text = user_response.lower()

    for topic, words in keywords.items():
        if any(word in user_text for word in words):
            score += 1

    if score >= 3:
        return random.choice(["🔥 Отличный ответ! Вы уверенно ведете переговоры!", "✅ Супер! Ваши аргументы сильные и логичные!"])
    elif score == 2:
        return random.choice(["👍 Неплохо! Ваш ответ логичен, но можно добавить больше фактов.", "🧐 Хороший ход, но попробуйте усилить аргументацию."])
    elif score == 1:
        return random.choice(["🤔 Интересная идея, но стоит добавить больше аргументов.", "📌 Ваша позиция понятна, но попробуйте сильнее убедить собеседника."])
    else:
        return random.choice(["❌ Этот аргумент слабый. Попробуйте более логичный подход.", "🚨 Нужно больше деталей! Перечитайте задание и подумайте ещё."])

# Обработчик для ответа
@router.message(lambda message: message.reply_to_message and "Ситуация для переговоров" in message.reply_to_message.text)
async def evaluate_message(message: types.Message):
    # Оценка ответа пользователя
    evaluation = evaluate_response(message.text)
    await message.answer(evaluation)

# Обработчик для кнопки "Назад"
@router.callback_query(lambda c: c.data == "main_menu")
async def back_to_main_menu(callback_query: CallbackQuery):
    await callback_query.message.answer("Возвращаемся в главное меню...", reply_markup=main_menu)
    await callback_query.answer()

# Обработчик для кнопки "📝 Ответить на ситуацию"
@router.callback_query(lambda c: c.data == "answer_scenario")
async def handle_answer_scenario(callback_query: CallbackQuery):
    # Вставьте сюда код для обработки нажатия на кнопку
    await callback_query.message.answer("Напишите свой ответ на ситуацию:")
    await callback_query.answer()
    
@router.callback_query(lambda c: c.data == "imitation")
async def imitation_negotiations(callback_query: CallbackQuery):
    # Случайный выбор одного сценария
    random_scenario = random.choice(negotiation_scenarios)
    await callback_query.message.answer(
        f"Ситуация для переговоров:\n\n{random_scenario}",
        reply_markup=imitation_menu  # Здесь будет клавиатура с кнопкой "Назад"
    )
    await callback_query.answer()
