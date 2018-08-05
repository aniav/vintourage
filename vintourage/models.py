import datetime

from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Product(Base):
    __tablename__ = 'products'

    link = Column(String(200), unique=True, primary_key=True)
    name = Column(String(50))
    price = Column(String(10))
    image = Column(String(200))
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Product %r (%r)>' % (self.name, self.link)