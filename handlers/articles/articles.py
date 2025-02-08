from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import articles_menu, main_menu

router = Router()

# 🔥 Подборка полезных книг и статей для делового общения
useful_resources = [
    "📖 **Искусство деловой переписки**:\n"
    "✍️ Хочешь писать письма, на которые отвечают? Тогда эти книги для тебя!\n"
    "1️⃣ *«Деловая переписка на все случаи жизни»* – Ольга Вершинина\n"
    "2️⃣ *«Как писать деловые письма»* – Александр Антонов\n"
    "🔗 [Гид по деловой переписке](https://www.unicraft.org/blog/8292/delovaya-perepiska/)",

    "💬 **Переговоры: как всегда добиваться своего**:\n"
    "🎯 Если хочешь договариваться так, чтобы тебя уважали и ценили, эти книги помогут!\n"
    "1️⃣ *«Переговоры без поражения»* – Роджер Фишер, Уильям Юри\n"
    "2️⃣ *«Даже не пытайтесь!»* – Крис Восс (экс-переговорщик ФБР)\n"
    "🔗 [Как вести переговоры: 10 работающих советов](https://venyoo.ru/blog/kak-pravilno-vesti-peregovory-10-rabotayushchih-sovetov/)",

    "📊 **Лидерство и влияние**:\n"
    "🚀 Если хочешь не просто говорить, а вдохновлять и вести за собой – начни отсюда!\n"
    "1️⃣ *«Лидер и племя»* – Дэвид Логан\n"
    "2️⃣ *«Как завоевывать друзей и оказывать влияние на людей»* – Дейл Карнеги\n"
    "🔗 [7 навыков для эффективного общения](https://finexecutive.com/ru/news/7_navykov_dlya_effektivnogo_obsheniya)",

    "🎩 **Деловой этикет и нетворкинг**:\n"
    "🤝 Хочешь, чтобы встречи с тобой запоминались, а контакты работали на тебя?\n"
    "1️⃣ *«Деловой этикет XXI века»* – Татьяна Николаева\n"
    "2️⃣ *«Никогда не ешьте в одиночку»* – Кейт Феррацци\n"
    "🔗 [Основы делового этикета](https://www.unisender.com/ru/glossary/delovoy_etiket/)"
]

# ✅ Обработчик кнопки "📚 Полезные статьи"
@router.callback_query(F.data == "articles")
async def useful_articles(callback: CallbackQuery):
    print("✅ Обработчик статей вызван!")  # Для отладки

    # Отправляем сообщение перед списком
    await callback.message.answer("🔹 Загружаю список полезных статей...")

    # Формируем список статей
    response = "\n\n".join(useful_resources)

    # Отправляем статьи пользователю
    await callback.message.answer(response, reply_markup=articles_menu)

    # Закрываем уведомление о нажатии кнопки
    await callback.answer()

# ✅ Обработчик кнопки "⬅️ Назад"
@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery):
    await callback.message.answer("📌 Вы вернулись в главное меню. Чем могу помочь?", reply_markup=main_menu)
    await callback.answer()


