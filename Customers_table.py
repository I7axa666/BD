import psycopg2
from settings import PASSWORD
from pprint import pprint

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    id SERIAL PRIMARY KEY,
                    name    VARCHAR(10) NOT NULL,
                    surname VARCHAR(20) NOT NULL,
                    email   VARCHAR(40) NOT NULL
                );
                """)

        cur.execute("""
                CREATE TABLE IF NOT EXISTS Phone_numbers (
                    id SERIAL PRIMARY KEY,
                    cust_id      INTEGER            NOT NULL REFERENCES Customers(id),
                    phone_number VARCHAR(12) UNIQUE NOT NULL CHECK (CHAR_LENGTH(phone_number)>=10)
                );
                """)
        conn.commit()
    return print("Таблица создана")

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
                INSERT INTO Customers(name, surname, email)
                VALUES (%s, %s, %s)
                RETURNING id;
                """, (first_name, last_name, email))
        client_id = cur.fetchone()
        if phones != None:
            cur.execute("""
                    INSERT INTO phone_numbers(cust_id, phone_number)
                    VALUES (%s, %s);
                    """, (client_id, phones))
        conn.commit()
    return print("Клиент добавлен!")

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
                INSERT INTO phone_numbers(cust_id, phone_number)
                VALUES (%s, %s);
                """, (client_id, phone))
        conn.commit()
    return print("Телефон добавлен!")

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        if first_name != None:
            cur.execute("""
                    UPDATE Customers 
                    SET name=%s
                    WHERE id=%s;
                    """, (first_name, client_id))
        if last_name != None:
            cur.execute("""
                    UPDATE Customers 
                    SET surname=%s
                    WHERE id=%s;
                    """, (last_name, client_id))
        if email != None:
            cur.execute("""
                    UPDATE Customers 
                    SET email=%s
                    WHERE id=%s;
                    """, (email, client_id))
        if phones != None:
            cur.execute("""
                    UPDATE Phone_numbers 
                    SET phone_number=%s
                    WHERE phone_number = %s;
                    """, (phones[1], phones[0]))
        conn.commit()
    return print("Данные изменены!")

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
                DELETE FROM phone_numbers 
                WHERE cust_id=%s 
                AND phone_number=%s;
                """, (client_id, phone))
        conn.commit()
    return print("Телефон удален!")

def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
                DELETE FROM phone_numbers 
                WHERE cust_id=%s;
                """, (client_id,))
        cur.execute("""
                DELETE FROM customers 
                WHERE id=%s;
                """, (client_id,))
        conn.commit()
    return print("Данные о клиенте удалены!")

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    query = """
            SELECT c.id, name, surname, email, pn.phone_number FROM customers c
            LEFT JOIN phone_numbers pn ON pn.cust_id = c.id
            WHERE"""
    params = []
    tup = []
    fields = {'name': first_name, 'surname': last_name, 'email': email, 'phone_number': phone}
    for key, value in fields.items():
        if value != None:
            params.append(key + "=%s")
            tup.append(value)
    res = ' AND '.join(params) + ';'
    q_res = query + ' ' + res
    q_tup = tuple(tup)

    with conn.cursor() as cur:
        cur.execute(q_res.format('customers'), q_tup)
        pprint(cur.fetchall())

def my_command():
    while True:
        command = input("Введите команду: ").lower()
        if command == '':
            print("\nПрограмма остановлена. Хорошего дня!")
            break

        with psycopg2.connect(database="netology_db",
                              user="postgres",
                              password=PASSWORD) as conn:
            if command == "c":
                create_db(conn)
            elif command == "a_c":
                first_name = input('Введите имя: ')
                last_name = input('Введите фамилию: ')
                email = input('Введите email: ')
                phone = input('Введите телефон: ')
                if phone == '':
                    add_client(conn, first_name, last_name, email)
                else:
                    add_client(conn, first_name, last_name, email, phone)
            elif command == "a_p":
                client_id = int(input('Введите id клиента: '))
                phone = input('Введите номер телефона: ')
                add_phone(conn, client_id, phone)
            elif command == "c_c":
                client_id = int(input('Введите id клиента: '))
                edit_fields = input('что меняем?(name, surname, email, phone указать через пробел): ').split()
                for fields in edit_fields:
                    if fields == 'name':
                        first_name = input("Ведите имя: ")
                        change_client(conn, client_id, first_name=first_name)
                    elif fields == 'surname':
                        last_name = input("Ведите фамилию: ")
                        change_client(conn, client_id, last_name=last_name)
                    elif fields == 'email':
                        email = input("Ведите email: ")
                        change_client(conn, client_id, email=email)
                    elif fields == 'phone':
                        phones = []
                        phone = input('Введите номер телефона, который нужно изменить: ')
                        phones.append(phone)
                        phone = input('Введите новый номер телефона: ')
                        phones.append(phone)
                        change_client(conn, client_id, phones=phones)
                    else:
                        print("Введено неверное поле")
                        return
            elif command == "d_p":
                client_id = int(input('Введите id клиента: '))
                phone = input('Введите номер телефона: ')
                delete_phone(conn, client_id, phone)
            elif command == "d_c":
                client_id = int(input('Введите id клиента: '))
                delete_client(conn, client_id)
            elif command == "f_c":
                search_info = input('что известно о клиенте?(name, surname, email, phone указать через пробел): ').split()
                s_list = []

                if 'name' in search_info:
                    first_name = input("Ведите имя: ")
                    s_list.append(first_name)
                else:
                    s_list.append(None)
                if 'surname' in search_info:
                    last_name = input("Ведите фамилию: ")
                    s_list.append(last_name)
                else:
                    s_list.append(None)
                if 'email' in search_info:
                    email = input("Ведите email: ")
                    s_list.append(email)
                else:
                    s_list.append(None)
                if 'phone' in search_info:
                    phone = input("Ведите телефон: ")
                    s_list.append(phone)
                else:
                    s_list.append(None)
                find_client(conn, *s_list)
            else:
                print("Такой команды не существует")

        conn.close()

if __name__ == '__main__':
    my_command()