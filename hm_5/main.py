import psycopg2
from pprint import pprint

def create_db(cur):
    '''Создание таблиц клиентов и телефонов'''

    cur.execute("""
    CREATE TABLE IF NOT EXISTS client(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100) NOT NULL, 
    surname VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phone(
    id SERIAL PRIMARY KEY,
    client_id INTEGER NOT NULL REFERENCES client(id),
    phone VARCHAR(20) DEFAULT NULL UNIQUE
    PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)


def add_client(cur, name, surname, email):
    '''Добавление клиента в таблицу client'''
    cur.execute("""
    INSERT INTO client(name, surname, email) VALUES(?, ?, ?);
    """, (name, surname, email))


def add_phone(cur, client_id, phone):
    '''Добавление номера телефона в таблицу phone'''
    cur.execute("""
    INSERT INTO phone(client_id, phone) VALUES(?, ?);
    """, (client_id, phone))



def clent_update():
    '''Изменение информации о клиенте'''
    command = int(input("Для изменения информации о клиенте, пожалуйста, введите нужную Вам команду.\n "
        "1 - изменить имя; 2 - изменить фамилию; 3 - изменить e-mail; 4 - изменить номер телефона"))

    while True:
        if command == 1:
            name = input("Введите id клиента имя которого хотите изменить: ")
            new_name = input("Введите имя для изменения: ")
            cur.execute("""
            UPDATE client SET name=? WHERE id=?;
            """, (new_name, name))
            break
        elif command == 2:
            surname = input("Введите id клиента фамилию которого хотите изменить: ")
            new_surname = input("Введите фамилию для изменения: ")
            cur.execute("""
            UPDATE client SET surname=? WHERE id=?;
            """, (new_surname, surname))
            break
        elif command == 3:
            email = input("Введите id клиента e-mail которого хотите изменить: ")
            new_email = input("Введите e-mail для изменения: ")
            cur.execute("""
            UPDATE client SET email=? WHERE id=?;
            """, (new_email, email))
            break
        elif command == 4:
            phone = input("Введите номер телефона который Вы хотите изменить: ")
            new_phone = input("Введите новый номер телефона, который заменит собой старый: ")
            cur.execute("""
            UPDATE phone SET phone=? WHERE phone=?;
            """, (new_phone, phone))
            break
        else:
            print("К сожалению, Вы ввели неправильную команду, пожалуйста, повторите ввод")



def delete_phone():
    '''Удаление номера телефона клиента из таблицы phone'''
    id_client = input("Введите id клиента номер телефона которого хотите удалить: ")
    phone = input("Введите номер телефона который хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phone WHERE client_id=? AND phone=?
        """, (id_client, phone))



def delete_client():
    '''Удаление имеющейся информации о клиенте'''
    id_client = input("Введите id клиента которого хотите удалить: ")
    surname = input("Введите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        #удаление связи с таблицей phone
        cur.execute("""
        DELETE FROM phone WHERE client_id=?
        """, (id_client,))
        #удаление информации о клиенте из таблицы client
        cur.execute("""
        DELETE FROM client WHERE id=? AND surname=?
        """, (id_client, surname))


def find_client():
    '''Поиск клиента по имени'''
    command = int(input("Для поиска информации о клиенте, пожалуйста, введите команду, где:\n "
          "1 - найти по имени; 2 - найти по фамилии; 3 - найти по e-mail; 4 - найти по номеру телефона"))
    while True:
        if command == 1:
            name = input("Введите имя для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, phone
            FROM client AS ch5
            LEFT JOIN phone AS cp ON cp.id = ch5.id
            WHERE name=?
            """, (name,))
            print(cur.fetchall())
        elif command == 2:
            surname = input("Введите фамилию для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, phone
            FROM client AS ch5
            LEFT JOIN phone AS cp ON cp.id = ch5.id
            WHERE surname=?
            """, (surname,))
            print(cur.fetchall())
        elif command == 3:
            email = input("Введите email для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, phone
            FROM client AS ch5
            LEFT JOIN phone AS cp ON cp.id = ch5.id
            WHERE email=?
            """, (email,))
            print(cur.fetchall())
        elif command == 4:
            phone = input("Введите номер телефона для поиска информации о клиенте: ")
            cur.execute("""
            SELECT id, name, surname, email, phone
            FROM client AS ch5
            LEFT JOIN phone AS cp ON cp.id = ch5.id
            WHERE phone=?
            """, (phone,))
            print(cur.fetchall())
        else:
            print("К сожалению, Вы ввели неправильную команду, пожалуйста, повторите ввод")



def check_function(cur):
    '''Проверочная функция, отображает содержимое таблиц'''
    cur.execute("""
    SELECT * FROM client;
    """)
    pprint(cur.fetchall())
    cur.execute("""
    SELECT * FROM phone;
    """)
    pprint(cur.fetchall())

#check_function()


if __name__ == '__main__':
    with psycopg2.connect(host="127.0.0.1", user="postgres", password="123456", database="h_w_5", port="5432") as conn:
        with conn.cursor() as cur:
            create_db(cur)
            check_function(cur)
            add_client(cur, "Гендальф", "Серый", "g_gray@com.com")
            add_client(cur, "Винни", "Пух", "br@com.com")
            add_client(cur, "Сталкер", "Меченный", "stalker@com.com")
            add_client(cur, "Снежная", "Королева", "snow_queen@com.com")
            add_client(cur, "Гудвин", "Ужасный", "gudvin@com.com")
            add_phone(cur, 1, "123456789")
            add_phone(cur, 2, "987654321")
            add_phone(cur, 3, "1111111111")
            add_phone(cur, 4, "77777777777")
            add_phone(cur, 5, "112233445566")
            clent_update()
            delete_phone()
            delete_client()
            find_client()
