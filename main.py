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

from telebot import TeleBot
import telebot.types as tt

# Импортируем файл настроек
import settings
# from  settings


# MY_TELEGRAM_API = '7341698907:AAGlo8L4epgwUtOyXo31x-6wF4eVMRBmlj8'
bot = TeleBot(settings.MY_TELEGRAM_API)


# noinspection SpellCheckingInspection



@bot.message_handler(commands=["start"])
def start_bot(message: tt.Message) -> None:
    """
    Обработка команды start и вывод кнопок под полем
    текста ввода в telergamm
    :param message:
    :return:
    """
    markup = tt.ReplyKeyboardMarkup()

    # Создаю кнопки расположенные в ряд
    btn1 = tt.KeyboardButton("О проекте")
    btn2 = tt.KeyboardButton("Сайт проекта")
    btn3 = tt.KeyboardButton("Контакты")

    # В первом ряду будет одна кнопка
    markup.row(btn1)

    # Во втором ряду будет 2 кнопки
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, "Привет", reply_markup=markup)
    # регистрируем следующий шаг
    bot.register_next_step_handler(message, on_click)


def on_click(message: tt.Message):
    """
    Обрабатываем действия кнопок
    :return:
    """
    # обработка будет происходить только один раз,
    # так как нет зарегистрированного следующего шага.
    # Что бы заработало еще раз - нужно заново перезапустить /start
    if message.text == "О проекте":
        bot.send_message(message.chat.id, "Обработка 'О проекте' ")
    elif message.text == "Сайт проекта":
        bot.send_message(message.chat.id, "Обработка 'Сайт проекта'")
    elif message.text == "Контакты":
        bot.send_message(message.chat.id, "Обработка 'Контакты'")



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
    web_open("mail.ru")


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


if __name__ == "__main__":
    bot.infinity_polling()
