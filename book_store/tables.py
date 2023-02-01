import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
import ORM as orm
from settings import DSN
from data import read_json


engine = sq.create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()

class Servise:
    def __init__(self, session):
        self.session = session

    def create_publisher(self, pub_name):
        publisher = orm.Publisher(pub_name=pub_name)
        session.add(publisher)
        session.commit()
        return publisher

    def create_book (self, title, publisher):
        book = orm.Book(title=title, publishers=publisher)
        session.add(book)
        session.commit()
        return book

    def create_stock(self, id_book, id_shop, count):
        stock = orm.Stock(book=id_book, shop=id_shop, count=count)
        session.add(stock)
        session.commit()
        return stock

    def create_shop(self, name):
        shop = orm.Shop(name=name)
        session.add(shop)
        session.commit()
        return shop

    def create_sale(self, price, date_sale, id_stock, sale_count):
        sale = orm.Sale(price=price, date_sale=date_sale, stock=id_stock, count=sale_count)
        session.add(sale)
        session.commit()
        return sale

    def purchase_fact(self, pub):
        try:
            id_publisher = int(pub)
            info = self.session.query(orm.Publisher, orm.Book, orm.Shop, orm.Sale).join(orm.Book).join(orm.Stock).join(
                orm.Shop).join(orm.Sale).filter(orm.Publisher.id == id_publisher)

        except ValueError:
            info = self.session.query(orm.Publisher, orm.Book, orm.Shop, orm.Sale).join(orm.Book).join(orm.Stock).join(
                orm.Shop).join(orm.Sale).filter(orm.Publisher.name == pub)

        return info

    def fill_out_tables(self, data):
        for item in data:
            model = {
                'publisher': orm.Publisher,
                'shop': orm.Shop,
                'book': orm.Book,
                'stock': orm.Stock,
                'sale': orm.Sale
            }[item.get('model')]
            session.add(model(id=item.get('pk'), **item.get('fields')))
        session.commit()
        return

session.close()

if __name__ == '__main__':
    orm.recreate_tables(engine)
    data = read_json('tests_data.json')
    service = Servise(session)
    service.fill_out_tables(data)

    pub = input("Введите id или название издательства: ")
    for item in service.purchase_fact(pub):
        print(item.Book.title, item.Shop.name, item.Sale.price, item.Sale.date_sale, sep=' | ')