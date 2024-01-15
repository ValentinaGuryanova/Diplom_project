import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.sql import func
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "products_shop",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("price", Integer(10)),
    Column("created_at", DateTime, default=func.now(), nullable=False),
    Column("updated_at", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)