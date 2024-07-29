import requests
from fastapi.routing import APIRouter

from src.conf.settings import URL_AUTH_LOGIN_API
from src.auth_lib.serializers import BaseAuthValidator

router = APIRouter()


@router.post('/login/')
async def auth(data: BaseAuthValidator):
    """Авторизация пользователя."""

    return requests.post(URL_AUTH_LOGIN_API, data=dict(data)).json()
