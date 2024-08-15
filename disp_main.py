"""
Программа работы с базой данных.
В ней будет работать диспетчер
Автор: Евгений Петров
Цель: Учебный проект
Почта: p174@mail.ru
"""
import time
import typing

import psycopg2 as psy


def getting_time() -> typing.List:
    """
    Возвращает текущее время в неформатированном виде
    :return:
    """
    time_now_get = time.localtime(time.time())
    time_now_out_get: typing.List = [time_now_get.tm_mday,
                              time_now_get.tm_mon,
                              time_now_get.tm_year,
                              time_now_get.tm_hour,
                              time_now_get.tm_min,
                              time_now_get.tm_sec,
                              ]
    return time_now_out_get

def write_to_db(sql_con: str):
    """
    Запись запроса в БД PostgresQL
    :return:
    """
    try:
        print(f"Подключение к БД {getting_time()}")
        con = psy.connect(
                dbname="ep20240806test",
                user="postgres",
                password="Postgres",
                host="localhost",
                port="5432",
        )
        print(f"БД подключена {getting_time()}")
        with con.cursor() as curr:
            curr.execute(sql_con)
            con.commit()
            print(f"Запрос {sql_con} выполнен в {getting_time()}")
        con.close()
        print(f"Connection is closed {getting_time()}")
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


def read_all_from_db(sql_con: str):
    """
    Чтение запроса из  БД PostgresQL
    Возвращает все найденные строки из запроса

    sql_con: str - передаваемый sql запрос

    :return:
    """
    try:
        print(f"Подключение к БД {getting_time()}")
        con = psy.connect(
                dbname="ep20240806test",
                user="postgres",
                password="Postgres",
                host="localhost",
                port="5432",
        )
        print(f"БД подключена {getting_time()}")
        with con.cursor() as curr:
            curr.execute(sql_con)
            curr.fetchall()
            print(f"Запрос {sql_con} выполнен в {getting_time()}")
        con.close()
        print(f"Connection is closed {getting_time()}")
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err

if __name__ == "__main__":
    print(f"Диспетчер запустил программу в {getting_time()}")
