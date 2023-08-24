from flask_app.extensions import db
from sqlalchemy import Integer, Column, String, DateTime
from sqlalchemy.sql import func


class User(db.Model):
    id = Column(Integer, primary_key=True, autoincrement="auto")
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
