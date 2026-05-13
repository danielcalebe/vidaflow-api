import os
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///vidaflow.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "SUPER_SECRET_KEY"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)