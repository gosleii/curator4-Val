import telebot

bot = telebot.TeleBot('6871706140:AAG2sND507abdAh11Nso9PfBtigaDCNtbug')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'йо, как по французски "меня зовут"?', parse_mode='Markdown')


@bot.message_handler(commands=['Je'])
def main(message):
    bot.send_message(message.chat.id, 'Je', parse_mode='Markdown')


@bot.message_handler(commands=['map'])
def main(message):
    bot.send_message(message.chat.id, 'mah', parse_mode='Markdown')


@bot.message_handler(commands=['pelle'])
def main(message):
    bot.send_message(message.chat.id, 'pel', parse_mode='Markdown')


@bot.message_handler(commands=['Jemappelle'])
def main(message):
    bot.send_message(message.chat.id, 'Me pooh pooh', parse_mode='Markdown')


bot.infinity_polling()