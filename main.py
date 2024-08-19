"""
Пишу телеграмм бота
Это учебный проект.
Адрес урока (одного из):
https://www.youtube.com/watch?v=RpiWnPNTeww
Библиотека: pyTelegramBotAPI
Bot: @epTestChel_bot
Ссылка: https://t.me/epTestChel_bot


"""

# Для улучшения быстродействия импортируем только то, используем.
# Если импортировать всю полностью библиотеку, то каждый раз будет
# вызываться поиск по библиотеке (насколько я понял)
from webbrowser import open as web_open
import time
import datetime
from typing import List

from telebot import TeleBot
import telebot.types as tt
import psycopg2 as psy

# Импортируем файл настроек
import settings

# Создаем экземляр класса TeleBot, настройки берем из переменных окружения
bot = TeleBot(settings.MY_TELEGRAM_API)


def fixing_launch_bot():
    """
    Фиксирует время старта бота.
    Побочно проверяем доступность БД для записи
    :return:
    """
    start_bot_time = datetime.datetime.now()
    sql_query = """
    INSERT INTO telegramm_bot_start 
    (started_datetime)
    VALUES
    (%s)
    """
    try:
        print(f"Подключение к БД {getting_time()}")
        con = psy.connect(
                dbname="ep20240806test",
                user="postgres",
                password="Postgres",
                host="localhost",
                port="5432",
        )
        print(f"БД подключена {getting_time()}")
        with con.cursor() as curr:
            curr.execute(sql_query, (start_bot_time,))
            con.commit()
            print(f"Запрос {sql_query} выполнен в {getting_time()}")
        con.close()
        print(f"Connection is closed {getting_time()}")
        divide_line(50)
        print(f"Start bot at {start_bot_time}")
        divide_line()
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


def divide_line(length: int = 30):
    """Выводит разделительную линию длинной length в консоль


    Args:
        length (int): длинна разделительной линии
        Значение по умолчанию 30
    """
    print (length * "-")

def getting_time() -> List:
    """
    Возвращает текущее время в неформатированном виде
    :return:
    """
    time_now_get = time.localtime(time.time())
    time_now_out_get: List = [time_now_get.tm_mday,
                              time_now_get.tm_mon,
                              time_now_get.tm_year,
                              time_now_get.tm_hour,
                              time_now_get.tm_min,
                              time_now_get.tm_sec,
                              ]
    return time_now_out_get


def write_to_db(sql_query_con: str):
    """
    Запись запроса в БД PostgresQL
    sql_con: - запрос в БД
    :return:
    """
    try:
        print(f"Подключение к БД {getting_time()}")
        con = psy.connect(
                dbname="ep20240806test",
                user="postgres",
                password="Postgres",
                host="localhost",
                port="5432",
        )
        print(f"БД подключена {getting_time()}")
        with con.cursor() as curr:
            curr.execute(sql_query_con)
            con.commit()
            print(f"Запрос {sql_query_con} выполнен в {getting_time()}")
            con.close()
        print(f"Connection is closed {getting_time()}")
        divide_line(50)
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


def make_first_start_table():
    """
    Делает первую таблицу при запуске бота.
    На самом деле, я думаю, она не нужна - лишнее обращение
    и лишняя нагрузка на сервер.
    То есть, БД можно сделать заранее или вручную или
    написав отдельные скрипты.
    :return:
    """
    # sql_query ="""
    # DROP TABLE telegramm_user
    # """
    # write_to_db(sql_query)
    sql_query = """
    CREATE TABLE IF NOT EXISTS telegramm_user (
    id SERIAL PRIMARY KEY,
    telegramm_username varchar(32),
    telegramm_id INTEGER NOT NULL,
    telegramm_firstname varchar(100),
    telegramm_lastname varchar(100),
    started_date timestamp NOT NULL
    );
    """
    write_to_db(sql_query)


def write_users_data_to_db(message_wri: tt.Message):
    """
    Записывает данные пользователя, запустившего
    бот комендой /start 

    Args:
        message (_type_): _description_
    """

    user_name = message_wri.from_user.username
    first_name = message_wri.from_user.first_name
    last_name = message_wri.from_user.last_name
    user_id = message_wri.from_user.id
    started_date_wri = datetime.datetime.now()

    sql_query = """
    INSERT INTO telegramm_user 
    (telegramm_username, telegramm_firstname, telegramm_lastname, telegramm_id, started_date)
    VALUES
    (%s, %s, %s, %s, %s);
    """
    # write_to_db(sql_query)

    try:
        print(f"Подключение к БД {getting_time()}")
        con = psy.connect(
                dbname="ep20240806test",
                user="postgres",
                password="Postgres",
                host="localhost",
                port="5432",
        )
        print(f"БД подключена {getting_time()}")
        with con.cursor() as curr:
            curr.execute(sql_query, (user_name, first_name, last_name, user_id, started_date_wri))
            con.commit()
            print(f"Запрос {sql_query} выполнен в {getting_time()}")
        con.close()
        print(f"Connection is closed {getting_time()}")
        divide_line(50)
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


@bot.message_handler(commands=["start"])
def start_bot(message: tt.Message) -> None:
    """
    Обработка команды start и вывод кнопок под полем
    текста ввода в telergam
    :param message:
    :return:
    """
    # ЗАкоментировал, так как таблица уже готова
    # Что бы избежать лишних и ненужных запросов
    # make_first_start_table()

    write_users_data_to_db(message)

    print(bot.user.id)
    print(bot.user)
    print(20 * "-")
    print(message.from_user)

    markup = tt.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаю кнопки
    # будут расположены под текстовым полем ввода
    btn1 = tt.KeyboardButton("🤯О проекте🤯")
    btn2 = tt.KeyboardButton("Сайт проекта")
    btn3 = tt.KeyboardButton("Контакты")

    # В первом ряду будет одна кнопка
    markup.row(btn1)

    # Во втором ряду будет 2 кнопки
    markup.row(btn2, btn3)

    # Отправляю привет и названеи нажаттй кнопки в чат для дальнейшей обработки
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)
    # регистрируем следующий шаг, это какая функция будет вызвана

    # Открываю файл на чтение в двоичносм(не текстовом) режиме,
    # буду отправлять фото.
    # Видео, аудио, отправляется аналогияно, только с помощью других методов
    with open("./photos/8_03_24.jpg", "rb") as photo_file:
        bot.send_photo(message.chat.id, photo_file, reply_markup=markup)
    # photo_file = open ("./photos/8-03-24.jpg", "rb")
    bot.register_next_step_handler(message, on_click)


def on_click(message: tt.Message) -> None:
    """
    Обрабатываем действия кнопок
    :return:
    """
    # обработка будет происходить только один раз,
    # так как нет зарегистрированного следующего шага.
    # Что бы заработало еще раз - нужно заново перезапустить /start
    if message.text.find("О проекте") != -1:
        bot.send_message(message.chat.id, "Обработка 'О проекте' ")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Сайт проекта":
        bot.send_message(message.chat.id, "Обработка 'Сайт проекта'")
        bot.register_next_step_handler(message, on_click)
    elif message.text == "Контакты":
        bot.send_message(message.chat.id, "Обработка 'Контакты'")
        bot.register_next_step_handler(message, on_click)


@bot.message_handler(commands=["main"])
def main_bot(message) -> None:
    """
    Обработка команды main и вывод приветствия
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, "Привет! Это основной блок!")


# Обрабатываю команду help
@bot.message_handler(commands=["help"])
def help_info(message) -> None:
    """
    Processing help command
    :param message:
    :return:
    """
    # С форматированием
    bot.send_message(message.chat.id,
                     "This is <b>help</b>",
                     parse_mode='html'
                     )

    # Без форматирования
    bot.send_message(message.chat.id, "This is help")


# Обрабатываю команду message_sys_info
@bot.message_handler(commands=["message_sys_info"])
def message_sys_info(message) -> None:
    """
    Processing command message_sys_info.
    This command dumps the entire message to the chat.
         """
    bot.send_message(message.chat.id, message)


# Отправляем пользователю ссылку на сайт
@bot.message_handler(commands=["site", "website"])
# Пришлось добавить self, так как почему-то начала появляться ошибка,
# что при отсутствии входящих параметров, функция получает один параметр.
# Инет сказал, что лечится именно так
def send_site(self) -> None:
    """
    Send to user our website
    :return:
    """
    # Что бы не ругался линтер
    if self:
        pass

    web_open("https://www.укпривилегия.рф/")


# принимаю фото от пользователя
@bot.message_handler(content_types=["photo"])
def get_photo_file(message):
    """
    Gets photo file from user
    :param message:
    :return:
    """
    #  Вывожу в ответ пользователю описание фото

    # Создаю объект кнопки markup через значение types
    # InlineKeyboardMarkup() - класс инлайн кнопок
    markup = tt.InlineKeyboardMarkup()

    # Создаю кнопки расположенные в ряд
    btn1 = tt.InlineKeyboardButton("Перейти на сайт", url="mail.ru")
    btn2 = tt.InlineKeyboardButton("Удалить фото", callback_data="delete")
    btn3 = tt.InlineKeyboardButton("Изменить текст", callback_data="edit")

    # В первом ряду будет одна кнопка
    markup.row(btn1)

    # Во втором ряду будет 2 кнопки
    markup.row(btn2, btn3)

    # Через метод add добавляю кнопку
    markup.add(tt.InlineKeyboardButton(
        "Перейти на сайт",
        url="mail.ru"
    )
    )
    # Добавляю вторую кнопку
    markup.add(tt.InlineKeyboardButton(
        "Удалить фото",
        callback_data="delete"
    )
    )
    # Добавляю третью кнопку
    markup.add(tt.InlineKeyboardButton(
        "Изменить текст",
        callback_data="edit"
    )
    )

    bot.reply_to(message, f"Вы написали: {message.caption}")

    # не зависимо от того, какой метод используется, send_message или reply_to,
    # кнопку передаем через параметр reply_markup= ,который в качестве
    # значения получает весь объект markup
    bot.reply_to(message, "Какое красивое фото!", reply_markup=markup)
    # print(message)


# Обрабатываю этим декоратором callback_data

@bot.callback_query_handler(func=lambda callback: True)
def callback_massage(callback):
    """

    :param callback:
    :return:
    """
    # Через параметр data обрабатываем именно ранее нажатые
    # кнопки с callback_data
    if callback.data == "delete":
        bot.delete_message(
            callback.message.chat.id,
            # Изменяю предыдущее сообщение
            callback.message.message_id - 1
        )
    elif callback.data == "edit":
        bot.edit_message_text(
            "Edit text",
            callback.message.chat.id,
            callback.message.message_id
        )


# Обрабатываю текст введенный пользователя
# ставить только после обработки всех команд!
# Если поставить до обработки команд, то все сообщения,
# Даже команды будут обрабатываться не как команды,
# а как просто текст
@bot.message_handler()
def processing_user_text(message):
    """
    Process user text.
    This is test of handler of user messages.
    Currently, puts Привет and adds sender's name
    :param message:
    :return:
    """
    if message.text.lower() == "привет":
        bot.send_message(
            message.chat.id,
            f"Привет {message.from_user.first_name}"
        )
    elif message.text.lower() == "id":
        # Так отвечаем нп конкретное сообщение
        bot.reply_to(message, f"id: {message.from_user.id}")


def main():
    """
    Основной блок программы.
    :return:
    """
    fixing_launch_bot()
    bot.infinity_polling()


if __name__ == "__main__":
    main()
