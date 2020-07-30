from sqlalchemy import Column, String, Integer
from database import Base

class Article(Base):
    __tablename__ = 'articles'

    title = Column(String, primary_key=True)
    length = Column(Integer)