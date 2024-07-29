import os

import requests
from fastapi.routing import APIRouter

from src.auth_lib.serializers import BaseAuthValidator

router = APIRouter()


@router.post('/login/')
async def auth(data: BaseAuthValidator):
    """Авторизация пользователя."""

    url = os.getenv('PATH_AUTH_API')

    return requests.post(url, data=dict(data)).json()
