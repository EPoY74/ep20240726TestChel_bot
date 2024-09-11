"""
Файл настроек для телеграмм бота
Адрес урока (одного из):
https://www.youtube.com/watch?v=RpiWnPNTeww
Библиотека: pyTelegramBotAPI
"""
import os

# Считываю переменную окружения из ОС с
# токеном подключения к telegramm MY_TELEGRAM_API_202407_TEST_BOT
MY_TELEGRAM_API = os.getenv("MY_TELEGRAM_API_202407_TEST_BOT")

# Считываю параметры подключеия к БД из
#  переменных окружения операционой системы.
# Они расположены вне кода с целью обеспечения безопасности
#  и снижения риска утечки конфиденциальной информации

# Считываю переменную окружения из ОС с
# наименованием БД MY_TELEGRAM_BOT_DBNAME_202407_TEST
MY_TELEGRAM_BOT_DBNAME = os.getenv("MY_TELEGRAM_BOT_DBNAME_202407_TEST")

# Считываю переменную окружения из ОС с
# именем пользователя БД MY_TELEGRAM_BOT_USER_202407_TEST
MY_TELEGRAM_BOT_USER = os.getenv("MY_TELEGRAM_BOT_USER_202407_TEST")

# Считываю переменную окружения из ОС с 
# перолем от БД  MY_TELEGRAM_BOT_PASSWORD_202407_TEST
MY_TELEGRAM_BOT_PASSWORD = os.getenv("MY_TELEGRAM_BOT_PASSWORD_202407_TEST")

# Считываю переменную окружения из ОС с
# хостом расположеня БД MY_TELEGRAM_BOT_HOST_202407_TEST
MY_TELEGRAM_BOT_HOST = os.getenv("MY_TELEGRAM_BOT_HOST_202407_TEST")

# Считываю переменную окружения из ОС с
# портом подключения к БД MY_TELEGRAM_BOT_PORT_202407_TEST
MY_TELEGRAM_BOT_PORT = os.getenv("MY_TELEGRAM_BOT_PORT_202407_TEST")
