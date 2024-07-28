"""
Пишу телеграмм бота

"""

from webbrowser import open as web_open

from telebot import TeleBot

# noinspection SpellCheckingInspection
MY_TELEGRAM_API = '7341698907:AAGlo8L4epgwUtOyXo31x-6wF4eVMRBmlj8'
bot = TeleBot(MY_TELEGRAM_API)


@bot.message_handler(commands=["start", "main"])
def start_bot(message) -> None:
    """
    Обработка команд start and stop
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, "Привет")


# Обрабатываю команду help
@bot.message_handler(commands=["help"])
def help_info(message) -> None:
    """
    PRocessing help command
    :param message:
    :return:
    """
    # С форматированием
    bot.send_message(message.chat.id, "This is <b>help</b>", parse_mode='html')
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


@bot.message_handler(commands=["site", "website"])
def send_site() -> None:
    """
    Send to user our website
    :return:
    """
    web_open("mail.ru")


# Обрабатываю текст введенный пользователе
# ставить только после обработки всех команд!
# Если поставить до обработки команд, то все сообщения
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
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}")
    elif message.text.lower() == "id":
        # Так отвечаем нп конкретное сообщение
        bot.reply_to(message, f"id: {message.from_user.id}")


if __name__ == "__main__":
    bot.infinity_polling()
