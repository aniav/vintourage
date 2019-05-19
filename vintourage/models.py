import datetime

from . import db


class Product(db.Model):
    __tablename__ = 'products'

    link = db.Column(db.String(200), unique=True, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(10))
    image = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Product %r (%r)>' % (self.name, self.link)