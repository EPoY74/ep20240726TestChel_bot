"""
Данный код используется для формирования запроса в БД
Что бы что-то поменять в базе.
Автор: Евгений Петров
Почта: p174@mail.ru
Дата: 20240817
"""
from datetime import time
from typing import List
import time

import psycopg2 as psy

def divide_line(length: int):
    """Выводит разделительную линию длинной length в консоль

    Args:
        length (int): длинна разделительной линии
    """
    print(length * "-")


def getting_time() -> List:
    """
    Возвращает текущее время в неформатированном виде
    :return:
    """
    time_now_get = time.localtime(time.time())
    time_now_out_get: List = [time_now_get.tm_mday,
                              time_now_get.tm_mon,
                              time_now_get.tm_year,
                              time_now_get.tm_hour,
                              time_now_get.tm_min,
                              time_now_get.tm_sec,
                              ]
    return time_now_out_get


def write_to_db(sql_query_con: str):
    """
    Запись запроса в БД PostgresQL
    sql_con: - запрос в БД
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
            curr.execute(sql_query_con)
            con.commit()
            print(f"Запрос {sql_query_con} выполнен в {getting_time()}")

        con.close()
        print(f"Connection is closed {getting_time()}")
        divide_line(50)
    except psy.Error as err:
        print(f"Ошибка: \n:{err}\n{getting_time()}")
        raise err


if __name__ == "__main__":
    ep_sql_query = """
     ALTER TABLE
      telegramm_user 
     ALTER COLUMN
      telegramm_id
     SET
      NOT NULL
     """

    write_to_db(ep_sql_query)

    #  Добавляю проверку NOT NULL
    # ep_sql_query = """
    #  ALTER TABLE
    #   telegramm_user
    #  ALTER COLUMN
    #   telegramm_id
    #  SET
    #   NOT NULL
    #  """

    # Добавляю поле в БД
    # ep_sql_query = """
    #   ALTER TABLE telegramm_user
    #   ADD COLUMN
    #   telegramm_id INTEGER;
    #   """


    #  Убираю NOT NULL в поле
    # ep_sql_query = """
    #  ALTER TABLE
    #   telegramm_user
    #  ALTER COLUMN
    #   telegramm_username
    #  DROP
    #   NOT NULL
    #  """