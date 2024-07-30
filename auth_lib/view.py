"""Представления библиотеки."""
import os

import requests
from fastapi.routing import APIRouter
from requests import ReadTimeout
from starlette.responses import Response

from auth_lib.serializers import BaseAuthValidator
from auth_lib.swagger_setting import get_swagger

router = APIRouter()


@router.post('/login/', **get_swagger().get('login', {}))
async def auth(response: Response, data: BaseAuthValidator):
    """Авторизация пользователя."""

    # Url по которому будет получаться авторизация
    url = os.environ.get('PATH_AUTH_API')
    if not url:
        response.status_code = 400
        return {'error': f'Не установлен `PATH_AUTH_API={url}`'}

    # Запрос на авторизацию
    try:
        response_data = requests.post(url, data=dict(data), timeout=10)

    except ReadTimeout:
        response.status_code = 400
        return {'error': 'Время ожидания вышло'}

    except Exception as exp:
        response.status_code = 500
        return {
            'error': f'Непредвиденный ход программы. Возникла ошибка: {exp}',
        }
    response.status_code = response_data.status_code

    return response_data.json()
