# donate_telebot

# Donate Telebot

Этот проект представляет собой Telegram-бота на платформе Telebot, который позволяет принимать пожертвования от пользователей.

## Установка

1. Клонируйте репозиторий с помощью следующей команды:

    git clone https://github.com/MrTwinkle777/donate_telebot.git

2. Перейдите в директорию проекта:

    cd donate_telebot

3. Установите зависимости с помощью команды:

    pip install -r requirements.txt

4. Создайте файл `config.py` и добавьте в него следующие переменные:

    API_TOKEN = 'YOUR_API_TOKEN'
    PAYMENTS_TOKEN = 'YOUR_PAYMENTS_TOKEN'

Замените 'YOUR_API_TOKEN' на токен вашего Telegram-бота, а 'YOUR_PAYMENTS_TOKEN' на токен платежного провайдера.

### Использование:
Запустите бота с помощью команды:

python main.py

Напишите /start или /help, чтобы получить информацию о боте.
Напишите /donate, чтобы вызвать меню пожертвований.
Выберите сумму пожертвования и валюту.
После успешной оплаты вы получите сообщение с благодарностью.

#### Зависимости:
telebot

requests
