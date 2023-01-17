from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

user = 'user'
password = 'password'
db = 'db'
port = 3306

url = f'mysql+pymysql://{user}:{password}@localhost:{port}/{db}?charset=utf8'

Engine = create_engine(url, encoding="utf-8", echo=False)
Base = declarative_base()

session = Session(
    autocommit=False,
    autoflush=False,
    bind=Engine
)