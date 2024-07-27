"""
Пишу телеграмм бота

"""

from telebot import TeleBot

MY_TELEGRAM_API='7341698907:AAGlo8L4epgwUtOyXo31x-6wF4eVMRBmlj8'
bot = TeleBot(MY_TELEGRAM_API)

# Обрабатываю командs start и main
def send_message(bot_in_sm, message_in_sm, text_in_sm):
    """
    Выводит сообщение пользователю
    :param message_in:
    :param text:
    :return:
    """


@bot.message_handler(commands=["start", "main"])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет")


# Обрабатываю команду help
@bot.message_handler(commands=["help"])
def help_info(message):
    # С форматированием
    bot.send_message(message.chat.id, "This is <b>help</b>", parse_mode='html')
    # Без форматирования
    bot.send_message(message.chat.id, "This is help")


# Обрабатываю команду message_sys_info
@bot.message_handler(commands = ["message_sys_info"])
def message_sys_info(message):
    bot.send_message(message.chat.id, message)


# Обрабатываю текст введенный пользователем
@bot.message_handler()
def processing_user_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}")


if __name__ == "__main__":

    bot.infinity_polling()