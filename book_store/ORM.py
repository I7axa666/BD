import sqlalchemy as sq
import datetime as dt

from sqlalchemy import Column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker



Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publishers"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), unique=True, nullable=False)


    def __str__(self):
        return f'Publisher {self.id} {self.pub_name}'


class Book(Base):
    __tablename__ = "books"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publishers.id"), nullable=False)

    def __str__(self):
        return f'Book {self.title}'

    publishers = relationship(Publisher, backref="book")


class Stock(Base):
    __tablename__ = 'stocks'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('books.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shops.id'))
    count = sq.Column(sq.Integer)

    def __str__(self):
        return f'Stock {self.count}'

    book = relationship(Book, backref='stocks')
    shop = relationship('Shop', backref='stocks')

class Shop(Base):
    __tablename__ = 'shops'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(50), unique=True, nullable=False)

    def __str__(self):
        return f'Shop {self.name}'

class Sale(Base):
    __tablename__ = 'sales'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stocks.id'))
    count = sq.Column(sq.Integer)

    def __str__(self):
        return f'Sale {self.price} {self.date_sale}'

    stock = relationship(Stock, backref='sale')

publisher_sales = sq.Table

def recreate_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


