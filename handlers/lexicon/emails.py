from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery
from keyboards import lexicon_submenu
from aiogram.types import CallbackQuery

router = Router()

# Обработчик для выбора подраздела "Деловая переписка"
@router.callback_query(F.data == "emails")
async def show_emails_submenu(callback: CallbackQuery):
    await callback.message.edit_text("📌 Выберите подраздел:", reply_markup=lexicon_submenu("emails"))

# Термины по деловой переписке
email_terms = {
    "Адресат": "Лицо или организация, которой направлено письмо. Важно правильно указать имя и должность получателя, чтобы письмо не потерялось.",
    "Аутрич (Outreach)": "Метод холодной переписки для установления контакта. Используется для привлечения клиентов, партнеров или сотрудничества.",
    "Вложения": "Файлы, прикрепленные к электронному письму. Убедитесь, что файлы имеют понятное название и не превышают допустимый размер.",
    "Грейс-период": "Дополнительное время для ответа на письмо. Обычно используется в случаях, когда требуется больше времени для подготовки ответа.",
    "Деловой тон": "Официальный и вежливый стиль общения в письмах. Исключает сленг, излишнюю эмоциональность и неформальные выражения.",
    "Желательная дата ответа": "Срок, до которого желательно получить ответ. Указывается в письме, чтобы ускорить обратную связь.",
    "Заголовок (Subject)": "Тема письма, кратко отражающая его содержание. Должна быть информативной и привлекать внимание.",
    "Копия (CC)": "Дополнительные получатели письма, которые видят переписку. Используется для информирования заинтересованных лиц.",
    "Логичная структура": "Четкое разделение письма на вступление, основную часть и заключение. Помогает адресату быстро понять суть письма.",
    "Межкультурная коммуникация": "Особенности общения с представителями других стран. Учитывайте культурные различия в формулировках и тоне.",
    "Нетикет": "Правила деловой электронной переписки. Включает вежливость, четкость и соблюдение форматов."
}

# Лекция по деловой переписке
email_lecture = """
Деловая переписка – это официальное общение через электронную почту, которое требует соблюдения определенных правил и стандартов. Основная цель – передача информации, обсуждение деловых вопросов и установление контактов. Умение грамотно вести деловую переписку является важным навыком для любого профессионала.

🔹 Структура делового письма:
1️⃣ Заголовок (Subject) – четко отражает суть письма. Например: «Предложение о сотрудничестве» или «Уточнение по проекту X». Заголовок должен быть кратким, но информативным.
2️⃣ Приветствие – указывает на уважение к адресату. Используйте вежливые фразы, такие как «Уважаемый Иван Иванович» или «Здравствуйте, команда проекта».
3️⃣ Основная часть – содержит ключевую информацию, изложенную четко и структурировано. Разделите текст на абзацы, используйте списки для перечисления. Например: «Мы хотели бы обсудить следующие вопросы: 1) Сроки выполнения проекта, 2) Бюджет, 3) Дополнительные требования».
4️⃣ Заключение – подведение итогов, выражение ожиданий по ответу. Например: «Буду признателен за ваш ответ до конца недели» или «С нетерпением жду ваших комментариев».
5️⃣ Подпись – указывает имя, должность и контакты отправителя. Например: «С уважением, Алексей Петров, менеджер по продажам, +7 (999) 123-45-67».

📌 Правила эффективной деловой переписки:
Будьте краткими и по существу. Никто не любит длинные письма. Избегайте лишней информации и сосредоточьтесь на главном.
Соблюдайте вежливый и профессиональный тон. Даже в сложных ситуациях сохраняйте уважение к адресату.
Проверяйте орфографию и пунктуацию. Ошибки создают плохое впечатление и могут привести к недопониманию.
Указывайте конкретный вопрос или просьбу в письме. Это помогает адресату быстрее понять, что от него требуется.
Используйте форматирование (абзацы, списки). Это делает письмо более удобочитаемым и структурированным.

❌ Распространенные ошибки:
Отсутствие темы письма. Письмо без темы может быть проигнорировано или попасть в спам.
Размытые или неконкретные формулировки. Если вы не можете четко выразить свою мысль, адресат может вас неправильно понять.
Отправка письма без проверки на ошибки. Опечатки и грамматические ошибки снижают доверие к отправителю.
Излишняя неформальность в официальной переписке. Использование сленга или слишком дружелюбного тона может быть неуместным.

📝 Дополнительные советы:
- Перед отправкой письма перечитайте его несколько раз, чтобы убедиться в отсутствии ошибок.
- Если письмо важное, попросите коллегу проверить его перед отправкой.
- Используйте шаблоны для часто отправляемых писем, чтобы сэкономить время.
- Не забывайте про вложения. Убедитесь, что все файлы прикреплены и имеют понятные названия.

Следуя этим рекомендациям, вы сможете вести профессиональную и эффективную деловую переписку, которая поможет вам выстраивать успешные деловые отношения и решать рабочие задачи быстрее и качественнее.
"""

# Обработчик терминов
@router.callback_query(F.data == "emails_terms")
async def send_email_terms(callback: CallbackQuery):
    terms_text = "\n\n".join([f"📌 {term} — {definition}" for term, definition in email_terms.items()])
    await callback.message.edit_text(f"Термины по деловой переписке:\n\n{terms_text}", 
                                     reply_markup=lexicon_submenu("emails"))

# Обработчик лекции
@router.callback_query(F.data == "emails_lectures")
async def send_email_lecture(callback: CallbackQuery):
    await callback.message.edit_text(f"Лекция по деловой переписке:\n\n{email_lecture}", 
                                     reply_markup=lexicon_submenu("emails"))
