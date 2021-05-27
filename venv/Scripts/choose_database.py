import mysql.connector as mc

def choose_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('show databases')
        for db in cursor:
            print(db)
        database = input("choose database to use: ")
        cursor.execute(F'use {database}')
        print("Database changed")
    except mc.Error as e:
        print(e)
    return