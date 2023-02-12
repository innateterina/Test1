import os
import sqlite3

from typing import List, Dict


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result

def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


def get_repeat_names() -> Dict:
    query_sql = '''
        SELECT FirstName
        From customers;
    '''
    names = execute_query(query_sql)
    counter = {}
    for item in names:
        counter[item] = counter.get(item, 0) + 1
    doubles = {item: count for item, count in counter.items() if count > 1}
    return doubles


result = get_repeat_names()
print(result)


def get_profit():
    query_sql = '''
        SELECT Sum(UnitPrice * Quantity)
        FROM invoice_items;
    '''
    total = execute_query(query_sql)
    unwrapper(total)










