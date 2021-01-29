#! /usr/bin/env python
import sqlite3


def get_sql_cursor(db_name):
    connection = sqlite3.connect("test.db")
    return connection.cursor(), connection



def exec_sql(db_name, script):
    cursor, connection = get_sql_cursor(db_name)

    cursor.executescript(script)
    connection.commit()



def select_data(db_name, select_script):
    cursor, conneciton = get_sql_cursor(db_name)

    cursor.execute(select_script)
    conneciton.commit()

    return cursor.fetchall()



def insert_data(db_name, query, data):
    if not isinstance(data, list):
        raise TypeError("type(data) is not type(list)")

    cursor, connection = get_sql_cursor(db_name)

    for row in data:
        cursor.execute(query, row)

    connection.commit()



def delete_data(db_name, script):
    cursor, connection = get_sql_cursor(db_name)

    cursor.execute(script)
    connection.commit()