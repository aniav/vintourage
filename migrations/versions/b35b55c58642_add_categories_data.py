"""empty message

Revision ID: b35b55c58642
Revises: d51e55c16a35
Create Date: 2020-11-09 15:47:00.590980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b35b55c58642'
down_revision = 'd51e55c16a35'
branch_labels = None
depends_on = None


def upgrade():
    from crawler.constants import Categories
    from vintourage.models import Category
    from vintourage import db

    for category in Categories:
        path = category.value
        slug = path.split('/')[-1]
        category = Category.query.filter_by(path=path).first()
        if not category:
            category = Category(
                path=path,
                slug=slug,
                name=slug.capitalize()
            )
            db.session.add(category)
            db.session.commit()


def downgrade():
    pass
