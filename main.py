import telebot
from telebot import types

from key_board import ikb_donate_RUB, ikb_donate_USD

API_TOKEN = 'YOUR API TOKEN'
PAYMENTS_TOKEN = 'YOUR PAYMENTS TOKEN'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am donatestBot.
I am here to take all of your money!
Write /donate and give me ALL YOUR MONEY!\
""")


# Handle '/donate'
@bot.message_handler(commands=['donate'])
def donate_moar_plz(message):
    # Вызов меню донатов
    bot.send_photo(chat_id=message.from_user.id,
                   photo=open('media\support_us.jpg', 'rb'),
                   caption='НУ ЧТО, СКОЛЬКО ДЕНЯК У ТЕБЯ?\n'
                           '(возможен и более клиентоориентировованный текст)',
                   reply_markup=ikb_donate_RUB)


# Callback menu donate
@bot.callback_query_handler(func=lambda call: call.data.startswith('donate'))
def answer_donate_pay(callback):
    data = callback.data.split(':')
    if data[1] == 'close':
        # Удадение меню донатов
        bot.edit_message_reply_markup(chat_id=callback.from_user.id,
                                      message_id=callback.message.id)
    elif data[1] == 'change_currency':
        if data[2] == 'RUB':
            bot.edit_message_reply_markup(chat_id=callback.from_user.id,
                                          message_id=callback.message.id,
                                          reply_markup=ikb_donate_USD)
        elif data[2] == 'USD':
            bot.edit_message_reply_markup(chat_id=callback.from_user.id,
                                          message_id=callback.message.id,
                                          reply_markup=ikb_donate_RUB)
    elif data[2] == 'RUB':
        # Отправка платежа
        bot.send_invoice(
            chat_id=callback.message.chat.id,
            title='На День Рождение',
            description=f"Оплата в размере {data[1]} рублей",
            invoice_payload='custom_payload',
            provider_token=PAYMENTS_TOKEN,
            start_parameter='donate',
            currency=data[2],
            is_flexible=False,
            prices=[types.LabeledPrice(f"Оплата {data[1]}", int(data[1]) * 100)]
        )
    elif data[2] == 'USD':
        bot.send_message(callback.message.chat.id, 'Извините, в данный момент доступна только оплата в рублях!')


# Подтверждаем платеж перед выполнением
@bot.pre_checkout_query_handler(func=lambda query: True)
def process_pre_checkout_query(query):
    bot.answer_pre_checkout_query(query.id, ok=True)


# Обработка успешной оплаты
@bot.message_handler(content_types=['successful_payment'])
def handle_successful_payment(message):
    amount = message.successful_payment.total_amount / 100
    currency = message.successful_payment.currency
    message_text = ''
    if currency == 'USD':
        amount_text = '$' + str(amount)
        if amount < 10:
            message_text = f"Спасибо за донат в размере {amount_text}!"
        else:
            message_text = f"СУПЕРСпасибо за донат в размере {amount_text}!"
    elif currency == 'RUB':
        amount_text = str(amount) + ' ' + 'рублей'
        if amount < 500:
            message_text = f"Спасибо за донат в размере {amount_text}!"
        else:
            message_text = f"СУПЕРСпасибо за донат в размере {amount_text}!"

    if message_text:
        bot.send_message(chat_id=message.from_user.id, text=message_text)


bot.infinity_polling()
