"""
Файл настроек для телеграмм бота
Адрес урока (одного из):
https://www.youtube.com/watch?v=RpiWnPNTeww
Библиотека: pyTelegramBotAPI
"""
import os

# Токен от телеграмм бота
MY_TELEGRAM_API = os.getenv("MY_TELEGRAM_API_202407_TEST_BOT")
DB_NAME: str = "ep20240806test"
USER: str = "postgres"
PASSWORD: str = "Postgres"
HOST: str = "localhost"
PORT: str = "5432"
