import mysql.connector as mc
import csv
import time
from getpass import getpass
from connect_to_source import connect_to_source
from import_to_csv import import_to_csv
from import_from_csv_to_table import import_from_csv_to_table
from connect_to_destination import connect_to_destination
if __name__ == '__main__':
    try:
        print("Hello! To login to MySQL server you need to enter your credentials!")
        time.sleep(2)
        host = input('Enter host: ')
        user = input("Enter username: ")
        password = getpass('Enter your password: ')
        connection_1 = connect_to_source(host, user, password)
        print('REMEMBER ABOUT secure-file-priv DIRECTORY PATH!')
        time.sleep(3)
        csv_path = input("Enter path to export table to: ")
        t0=time.time()
        import_to_csv(connection_1, csv_path)
        t1=time.time()
        connection_2 = connect_to_destination()
        t2=time.time()
        import_from_csv_to_table(connection_2, csv_path)
        print("Importing and exporting table executed in: {%f.2} seconds. " % (time.time()-t2+t1-t0))
    except mc.Error as e:
        print(e)
    finally:
        connection_1.close()
        connection_2.close()
        print("Disconnecting from server, goodbye!")
















