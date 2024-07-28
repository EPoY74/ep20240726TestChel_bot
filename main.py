"""
Пишу телеграмм бота

"""

from telebot import TeleBot

MY_TELEGRAM_API='7341698907:AAGlo8L4epgwUtOyXo31x-6wF4eVMRBmlj8'
bot = TeleBot(MY_TELEGRAM_API)


@bot.message_handler(commands=["start", "main"])
def start_bot(message):
    """
    Обработка команд start and stop
    :param message:
    :return:
    """
    bot.send_message(message.chat.id, "Привет")


# Обрабатываю команду help
@bot.message_handler(commands=["help"])
def help_info(message):
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
@bot.message_handler(commands = ["message_sys_info"])
def message_sys_info(message):
    """
    Processing command message_sys_info.
    This command dumps the entire message to the chat.
         """
    bot.send_message(message.chat.id, message)


# Обрабатываю текст введенный пользователем
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


if __name__ == "__main__":
    bot.infinity_polling()