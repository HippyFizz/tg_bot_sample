import telebot
from config.options import mainOptions

bot = telebot.TeleBot(mainOptions.token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, ("Привет!\n"
                                       "Я тут, чтобы сделать процесс разработки,\n"
                                       "Gett Taxi b2b Portal максимально удобным!\n"
                                       "Список моих команд будет обновляться, а возможности расти!\n"
                                       "По любым вопросам обращаться к создателю @hippyfizz\n"))


@bot.message_handler(commands=['show_my_id'])
def send_user_id(message):
    bot.reply_to(message, "Ваш telegram ID: {0}".format(message.from_user.id))


@bot.message_handler(commands=['show_info'])
def send_user_id(message):
    bot.reply_to(message,
                 ("Django: \n"
                  "http://51.15.54.58:27020\n"
                  "Tornado: \n"
                  "http://51.15.54.58:27022\n"
                  "Users frontend:\n"
                  "http://51.15.54.58:27025\n"
                  "System frontend:\n"
                  "https://51.15.54.58:27030\n"
                  "pgAdmin:\n"
                  "http://51.15.54.58:5051\n"
                  "Jenkins:\n"
                  "http://51.15.54.58:8090\n"))


bot.remove_webhook()
bot.set_webhook(url=mainOptions.getWebhookUrlBase(),
                certificate=open(mainOptions.cert, 'r'))
