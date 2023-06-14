from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_donate_RUB = InlineKeyboardMarkup()

ikb_donate_RUB.row(InlineKeyboardButton(text='50 рублей', callback_data='donate:50:RUB'),
                   InlineKeyboardButton(text='200 рублей', callback_data='donate:200:RUB'))

ikb_donate_RUB.row(InlineKeyboardButton(text='500 рублей', callback_data='donate:500:RUB'),
                   InlineKeyboardButton(text='1000 рублей', callback_data='donate:1000:RUB'))

ikb_donate_RUB.row(InlineKeyboardButton(text='Изменить валюту RUB/USD', callback_data='donate:change_currency:RUB'))
ikb_donate_RUB.row(InlineKeyboardButton(text="Закрыть", callback_data='donate:close'))


ikb_donate_USD = InlineKeyboardMarkup()

ikb_donate_USD.row(InlineKeyboardButton(text='1$', callback_data='donate:1:USD'),
                   InlineKeyboardButton(text='5$', callback_data='donate:5:USD'))

ikb_donate_USD.row(InlineKeyboardButton(text='10$', callback_data='donate:10:USD'),
                   InlineKeyboardButton(text='20$', callback_data='donate:20:USD'))

ikb_donate_USD.row(InlineKeyboardButton(text='Изменить валюту RUB/USD', callback_data='donate:change_currency:USD'))
ikb_donate_USD.row(InlineKeyboardButton(text="Закрыть", callback_data='donate:close'))



