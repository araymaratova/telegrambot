from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 📌 Главное меню
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📖 Обучение деловой лексике", callback_data="lexicon")],
    [InlineKeyboardButton(text="✉️ Шаблоны деловой переписки", callback_data="templates")],
    [InlineKeyboardButton(text="💬 Имитация переговоров", callback_data="imitation")],
    [InlineKeyboardButton(text="🎩 Советы по деловому этикету", callback_data="etiquette")],
    [InlineKeyboardButton(text="📚 Полезные статьи", callback_data="articles")],
    [InlineKeyboardButton(text="📞 Контактная информация", callback_data="contacts")]
])

# 📌 Подменю "Обучение деловой лексике"
lexicon_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🤝 Переговоры", callback_data="negotiations")],
    [InlineKeyboardButton(text="📧 Переписка", callback_data="emails")],
    [InlineKeyboardButton(text="📞 Телефонные разговоры", callback_data="calls")],
    [InlineKeyboardButton(text="📊 Презентации", callback_data="presentations")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]
])

# 📌 Подразделы в обучении (термины, лекции, тест)
def lexicon_submenu(topic: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📌 Термины", callback_data=f"{topic}_terms")],
        [InlineKeyboardButton(text="📖 Лекции", callback_data=f"{topic}_lectures")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="lexicon")]
    ])

# 📚 Клавиатура для полезных статей (без ненужной кнопки)
articles_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]
])

contacts_menu = InlineKeyboardMarkup(inline_keyboard=[  # Кнопка "назад" для контактов
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]
])

# 📌 Клавиатура для раздела "Советы по деловому этикету"
etiquette_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📚 Основные правила общения", callback_data="etiquette_main")],
    [InlineKeyboardButton(text="📋 Разница между официальным и неофициальным стилем", callback_data="official_vs_informal")],
    [InlineKeyboardButton(text="📞 Советы по голосовым и видеозвонкам", callback_data="calls_and_video")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]  # Кнопка назад
])

back_to_etiquette_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="etiquette")]  # Вернем в меню этикета
])

email_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📩 Запрос информации", callback_data="email_info")],
    [InlineKeyboardButton(text="🤝 Сотрудничество", callback_data="email_partnership")],
    [InlineKeyboardButton(text="⚠️ Жалобы и претензии", callback_data="email_complaint")],
    [InlineKeyboardButton(text="📅 Приглашения и встречи", callback_data="email_invite")],
    [InlineKeyboardButton(text="⏳ Напоминания и дедлайны", callback_data="email_reminder")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]  # Кнопка назад
])

back_to_templates_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="templates")]
])


imitation_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Ответить на ситуацию", callback_data="answer_scenario")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="main_menu")]
])




