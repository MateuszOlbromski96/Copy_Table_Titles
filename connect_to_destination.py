import mysql.connector as mc
from getpass import getpass
#Function connects to database and returns the connection object

def connect_to_destination():
    try:
        host = input("Enter host name of server's destination database ")
        user = input("Enter username: ")
        database = input('Choose database: ')
        password = getpass("Enter password: ")
        connection = mc.connect(host=host, user=user, database=database, password=password)
    except mc.Error as e:
        print(e)
    return connection
