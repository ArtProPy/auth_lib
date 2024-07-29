"""Конфигурация приложения."""

import os

from dotenv import load_dotenv

# Загрузка переменных окружения
LOAD_ENV = load_dotenv()

URL_AUTH_LOGIN_API = os.getenv('PATH_AUTH_API')
