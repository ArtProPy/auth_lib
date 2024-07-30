"""Набор сериалайзеров."""

from pydantic import BaseModel, Field


class BaseAuthValidator(BaseModel):
    """Валидатор базовых полей пользователя."""

    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
