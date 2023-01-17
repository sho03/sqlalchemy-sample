from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from settings import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(100))