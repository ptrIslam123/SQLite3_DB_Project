#! /usr/bin/env python
import env
import main as m
import sqlexec as sql

def init(db_name):
    init_script = m.readf(env.SCRIPT_DIR_PATH + "init")

    sql.exec_sql(db_name, init_script)


def insert_data(db_name):
    query = m.readf(env.SCRIPT_DIR_PATH + "insert_data")
    sql.exec_sql(db_name, query)

    select_data(db_name)


def select_data(db_name):
    script = m.readf(env.SCRIPT_DIR_PATH + "select_data")
    res = sql.select_data(db_name, script)
    print (res)


def remove_data(db_name):
    delete_script = m.readf(env.SCRIPT_DIR_PATH + "remove")
    sql.delete_data(db_name, delete_script)

    select_data(db_name)


db_name = env.TABLE_DIR_PATH + "test.db"


init(db_name)

insert_data(db_name)

remove_data(db_name)
