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
    ep_current_time = time.localtime(time.time())
    time_now_out_get: typing.List = [ep_current_time.tm_mday,
                                     ep_current_time.tm_mon,
                                     ep_current_time.tm_year,
                                     ep_current_time.tm_hour,
                                     ep_current_time.tm_min,
                                     ep_current_time.tm_sec,
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
    Чтение запроса из БД PostgresQL.
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
            read_all_results = curr.fetchall()
            print(f"Запрос {sql_con} выполнен в {getting_time()}")
        con.close()
        print(f"Connection is closed {getting_time()}")
        return read_all_results
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


def get_table_datas(table_name: str):
    """
    Читаю название таблицы 
    """
    sql_query = f"""
    SELECT
    *
    FROM
        {table_name};
    """
    return read_all_from_db(sql_query)


if __name__ == "__main__":
    print(f"Диспетчер запустил программу в {getting_time()}")
    results = get_table_datas('telegramm_user')
    for result in results:
        print(result)
