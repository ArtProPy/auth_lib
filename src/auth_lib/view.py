import os

import requests
from fastapi.routing import APIRouter
from starlette.responses import Response

from src.auth_lib.serializers import BaseAuthValidator

router = APIRouter()


@router.post('/login/')
async def auth(response: Response, data: BaseAuthValidator):
    """Авторизация пользователя."""

    url = os.environ.get('PATH_AUTH_API')
    if not url:
        response.status_code = 400
        return {'error': f'Не установлен `PATH_AUTH_API={url}`'}

    response_data = requests.post(url, data=dict(data)).json()
    response.status_code = response_data.status_code

    return response_data.json()
