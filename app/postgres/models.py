from sqlalchemy import Column, Integer, String
from app.postgres.utils.db import Base

class Article(Base):
    __tablename__ = "articles"
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=False)
