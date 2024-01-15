from datetime import datetime
from typing import Optional, ClassVar

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    """ Модель товара """

    name = str
    price: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_active: bool

    def __str__(self):
        return f'{self.name}'


class User(BaseModel):
    """ Модель пользователя """

    username: str
    email: str
    phone_number: str
    password: str
    password2: str

    def __str__(self):
        return f'{self.name}'


