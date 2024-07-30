"""Настройки swagger."""


def get_swagger() -> dict:
    """
    Возвращает данные, необходимые для заполнения swagger.

    :return: dict
    """

    tag = 'Удалённая работа с пользователем'

    error_500 = {
        500: {
            'description': 'Возникла непредвиденная ошибка.',
            'content': {
                'application/json': {
                    'example': {
                        'error': (
                            'Непредвиденный ход программы. Возникла '
                            'ошибка: `Каппибара проголодалась`'
                        ),
                    },
                },
            },
        },
    }

    return {
        'login': {
            'tags': [tag],
            'summary': f'Авторизация пользователя.',
            'status_code': 200,
            'responses': {
                200: {
                    'description': (
                        f'Успешная авторизация.'
                    ),
                    'content': {
                        'application/json': {
                            'example': {
                                'result': {
                                    'access_token': '<токен пользователя>',
                                    'token_type': 'bearer'
                                },
                            },
                        },
                    },
                },
                400: {
                    'description': 'Долгое время ожидания',
                    'content': {
                        'application/json': {
                            'example': {
                                'error': 'Время ожидания вышло',
                            },
                        },
                    },
                },
                **error_500,
            },
        },
    }
