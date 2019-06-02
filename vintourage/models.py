import datetime

from . import db


class Product(db.Model):
    __tablename__ = 'products'

    link = db.Column(db.String(200), unique=True, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(10))
    image = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return '<Product %r (%r)>' % (self.name, self.link)

    def update(self, **kwargs):
        """Update values on an instance with kwargs.

        Details from crawlers come in as a dict so it's easier to update it
        with this helper function than to do assignment by hand.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.updated = datetime.datetime.utcnow()