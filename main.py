#! /usr/bin/env python

import sqlexec as sql
import env

def readf(fname):
    with open(fname) as file:
        return file.read()


def main():
    db_name = env.TABLE_DIR_PATH + "test.db"
    fname = env.SCRIPT_DIR_PATH + "init"
    
    print (db_name)
    print (fname)
    
    script = readf(fname)
    select_script = readf(env.SCRIPT_DIR_PATH + "select_data")
    #print (script)
    sql.exec_sql(db_name, script)
    print (sql.select_data(db_name, select_script))
    
    



if __name__ == "__main__":
    main()