from datetime import datetime

import uvicorn
from fastapi import FastAPI

from src.app.api import ping
from src.app.api.models import Product
from src.app.db import database

app = FastAPI()


@app.post("/products/")
async def create_product(product: Product):
    return product


@app.get("/products/")
async def read_products():
    return Product(name="Product 1", price=10.0, created_at=datetime.now(), active=True)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
