import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.start import router as start_router
from handlers.lexicon.negotiations import router as negotiations_router
from handlers.lexicon.emails import router as emails_router
from handlers.lexicon.calls import router as calls_router
from handlers.lexicon.presentations import router as presentations_router
from handlers.articles.articles import router as articles_router
from handlers.contacts.contacts import router as contacts_router
from handlers.etiquette.main import router as etiquette_main_router
from handlers.etiquette.style import router as etiquette_style_router
from handlers.etiquette.calls import router as etiquette_calls_router
from handlers.templates.info import router as info_router
from handlers.templates.partnership import router as partnership_router
from handlers.templates.complaint import router as complaint_router
from handlers.templates.invite import router as invite_router
from handlers.templates.reminder import router as reminder_router
from handlers.imitation.negotiationss import router as negotiationss_router
# Логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(start_router)
dp.include_router(negotiations_router)
dp.include_router(emails_router)
dp.include_router(calls_router)
dp.include_router(presentations_router)
dp.include_router(articles_router)
dp.include_router(contacts_router)
dp.include_router(etiquette_main_router)
dp.include_router(etiquette_style_router)
dp.include_router(etiquette_calls_router)
dp.include_router(info_router)
dp.include_router(partnership_router)
dp.include_router(complaint_router)
dp.include_router(invite_router)
dp.include_router(reminder_router)
dp.include_router(negotiationss_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

