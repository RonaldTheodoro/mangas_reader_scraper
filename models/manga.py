import sqlalchemy as sa

from .base import Base


class Manga(Base):
    __tablename__ = 'manga'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    url = sa.Column(sa.String, nullable=False)
    is_complete = sa.Column(sa.Boolean, nullable=False)

    def __repr__(self):
        items = self.__dict__.items()
        attr = [f'{key}={value}' for key, value in items if '_sa_' not in key]
        attr = ', '.join(attr)
        return f'{self.__class__.__name__}({attr})'
