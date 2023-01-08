import psycopg2
from psycopg2 import Error
from settings import PASSWORD

class Db:

    def command(self, query, tup):
        conn = psycopg2.connect(database="netology_db",
                                user="postgres",
                                password=PASSWORD)
        with conn.cursor() as cur:
            try:
                cur.execute(query.format(table_name=self.table_name), tup)
                conn.commit()

            except (Exception, Error) as error:
                conn.rollback()
                return print("Ошибка отправки в БД", error)

            # cur.execute("""SELECT * FROM customers;""")
            # print(cur.fetchall())
            # cur.execute("""SELECT * from phone_numbers;""")
            # print(cur.fetchall())
            try:
                for table in cur.fetchall():
                    print(table)
            except:
                    print('Готово')
            conn.close()


class Table(Db):
    def __init__(self, table_name):
        self.table_name = table_name

    def create_table(self):
        self.tup = tuple()

        self.query = """
        CREATE TABLE IF NOT EXISTS {table_name} (
            id SERIAL PRIMARY KEY,
            cust_name VARCHAR(10) NOT NULL,
            cust_surname VARCHAR(20) NOT NULL,
            email VARCHAR(40) NOT NULL
        );
        """
        self.command(self.query, self.tup)

        tup = tuple()
        self.add_query = """
        CREATE TABLE IF NOT EXISTS Phone_numbers (
	        id SERIAL PRIMARY KEY,
	        cust_id INTEGER NOT NULL REFERENCES Customers(id),
	        phone_number VARCHAR(12) UNIQUE NOT NULL CHECK (CHAR_LENGTH(phone_number)>=10)
        );
        """
        self.command(self.add_query, self.tup)
        return

    def add_customer(self):
        # self.tup = tuple()
        self.cust_name = input('Введите имя: ')
        self.cust_surname = input('Введите фамилию: ')
        self.email = input('Введите email: ')
        self.tup = (self.cust_name, self.cust_surname, self.email)
        self.query = """
        INSERT INTO {table_name}(cust_name, cust_surname, email)
        VALUES (%s, %s, %s);
        """
        self.command(self.query, self.tup)

    def add_number(self):
        self.phone_number = input('Введите номер телефона: ')
        self.cust_id = int(input('Введите номер клиента: '))
        self.tup = (self.cust_id, self.phone_number)
        self.query = """
        INSERT INTO phone_numbers(cust_id, phone_number)
        VALUES (%s, %s);
        """
        self.command(self.query, self.tup)

    def edit_data(self):
        self.id = int(input('Введите номер клиента: '))
        self.what1 = input('Введите имя: ')
        self.what2 = input('Введите фамилию: ')
        self.what3 = input('Введите email: ')
        self.tup = (self.what1, self.what2, self.what3, self.id)
        self.query = """
        UPDATE {table_name} 
        SET cust_name=%s, cust_surname=%s, email=%s
        WHERE id = %s;
        """
        self.command(self.query, self.tup)

    def delete_phone(self):
        self.id = int(input('Введите номер клиента: '))
        self.tup = (self.id,)
        self.query = """
        DELETE FROM phone_numbers 
        WHERE cust_id=%s;
        """
        self.command(self.query, self.tup)

    def delete_cust(self):
        self.id = int(input('Введите номер клиента: '))
        self.tup = (self.id,)
        self.query = """
        DELETE FROM {table_name} 
        WHERE id=%s;
        """
        self.command(self.query, self.tup)

    def find_cust(self):
        self.ithem = input('Введите составляющую поиска: ')
        self.tup = (self.ithem, self.ithem, self.ithem, self.ithem)
        self.query = """
        SELECT c.id, cust_name, cust_surname, email, phone_number FROM {table_name} c
        LEFT JOIN phone_numbers pn ON pn.cust_id = c.id
        WHERE cust_name=%s 
        OR cust_surname=%s 
        OR email=%s 
        OR phone_number=%s;
        """
        self.command(self.query, self.tup)

if __name__ == '__main__':
    table =Table('Customers')
    # table.create_table()
    # table.add_customer()
    # table.add_number()
    # table.edit_data()
    # table.delete_phone()
    # table.delete_cust()
    # table.find_cust()

