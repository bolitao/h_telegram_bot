import configparser

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging

config = configparser.ConfigParser()
config.read('conf.ini')
bot_token = config['telegram'].get('token')
remote_mysql_conf = config['remote_mysql']
ssh_host = remote_mysql_conf.get('ssh_host')
ssh_port = remote_mysql_conf.get('ssh_port')
ssh_user = remote_mysql_conf.get('ssh_user')
ssh_pw = remote_mysql_conf.get('ssh_pw')
mysql_host = remote_mysql_conf.get('mysql_host')
mysql_port = remote_mysql_conf.get('mysql_port')
db_user = remote_mysql_conf.get('db_user')
db_password = remote_mysql_conf.get('db_password')
dbname = remote_mysql_conf.get('dbname')

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")


def response_text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='?')


def ehentai_daily(update, context):
    pass  # TODO: get daily ehentai toplist


def ehentai_monthly(update, context):
    pass  # TODO: get monthly ehentai toplist


def ehentai_yearly(update, context):
    pass  # TODO: get yearly ehentai toplist


def random_pic(update, context):
    pass  # TODO: get random picture


if __name__ == '__main__':
    start_handle = CommandHandler("start", start)
    dispatcher.add_handler(start_handle)
    any_text_response_handle = MessageHandler(Filters.text, response_text)
    dispatcher.add_handler(any_text_response_handle)
    updater.start_polling()
