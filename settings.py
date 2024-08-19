"""
Файл настроек для телеграмм бота
Адрес урока (одного из):
https://www.youtube.com/watch?v=RpiWnPNTeww
Библиотека: pyTelegramBotAPI
"""
import os

# Токен от телеграмм бота
MY_TELEGRAM_API = os.getenv("MY_TELEGRAM_API_202407_TEST_BOT")

# Параметры подключения к БД postgresQL
MY_TELEGRAM_BOT_DBNAME = os.getenv("MY_TELEGRAM_BOT_DBNAME_202407_TEST")
MY_TELEGRAM_BOT_USER = os.getenv("MY_TELEGRAM_BOT_USER_202407_TEST")
MY_TELEGRAM_BOT_PASSWORD = os.getenv("MY_TELEGRAM_BOT_PASSWORD_202407_TEST")
MY_TELEGRAM_BOT_HOST = os.getenv("MY_TELEGRAM_BOT_HOST_202407_TEST")
MY_TELEGRAM_BOT_PORT = os.getenv("MY_TELEGRAM_BOT_PORT_202407_TEST")
