import datetime

from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import foreign
from sqlalchemy.orm import relationship
from sqlalchemy.orm import remote
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import cast

from . import db


class Category(db.Model):
    """Illustrates the "materialized paths" pattern.

    Materialized paths is a way to represent a tree structure in SQL with fast
    descendant and ancestor queries at the expense of moving nodes (which require
    O(n) UPDATEs in the worst case, where n is the number of nodes in the tree). It
    is a good balance in terms of performance and simplicity between the nested
    sets model and the adjacency list model.

    It works by storing all nodes in a table with a path column, containing a
    string of delimited IDs. Think file system paths:

        1
        1.2
        1.3
        1.3.4
        1.3.5
        1.3.6
        1.7
        1.7.8
        1.7.9
        1.7.9.10
        1.7.11

    Descendant queries are simple left-anchored LIKE queries, and ancestors are
    already stored in the path itself. Updates require going through all
    descendants and changing the prefix.

    In our scenario the paths are generated like:

        women
        women/skirts
        women/dresses
        women/dresses/maxi
        men
        men/blouses
    """
    __tablename__ = "category"

    id = db.Column(Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(120))
    slug = db.Column(db.String(50))

    path = db.Column(db.String(500), nullable=False, index=True)

    # To find the descendants of this node, we look for nodes whose path
    # starts with this node's path.
    descentands = db.relationship(
        "Category",
        viewonly=True,
        order_by=path,
        primaryjoin=remote(foreign(path)).like(path.concat("/%")),
    )

    # Finding the ancestors is a little bit trickier. We need to create a fake
    # secondary table since this behaves like a many-to-many join.
    secondary = db.select(
        [
            id.label("id"),
            db.func.unnest(
                db.cast(
                    db.func.string_to_array(
                        db.func.regexp_replace(path, r"\/?\w+$", ""), "/"
                    ),
                    db.ARRAY(db.String),
                )
            ).label("ancestor_id"),
        ]
    ).alias()

    ancestors = db.relationship(
        "Category",
        viewonly=True,
        secondary=secondary,
        primaryjoin=id == secondary.c.id,
        secondaryjoin=secondary.c.ancestor_id == id,
        order_by=path,
    )

    products = db.relationship('Product', backref='category', lazy=True)

    @property
    def depth(self):
        return len(self.path.split("/")) - 1

    def __repr__(self):
        return f"Category {self.path}"

    def __str__(self):
        root_depth = self.depth
        s = [self.slug]
        s.extend(
            ((n.depth - root_depth) * "  " + n.slug)
            for n in self.descendants
        )
        return "\n".join(s)

    def move_to(self, new_parent):
        new_path = new_parent.path + "/" + self.slug
        for n in self.descendants:
            n.path = new_path + n.path[len(self.path) :]
        self.path = new_path


class Product(db.Model):
    __tablename__ = 'products'

    link = db.Column(db.String(200), unique=True, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(10))
    image = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    active = db.Column(db.Boolean(), default=True)
    category_id = db.Column(Integer, db.ForeignKey('category.id'))

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