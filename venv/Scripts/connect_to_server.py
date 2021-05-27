import mysql.connector as mc
from getpass import getpass

def connect_to_server(host,user,password):
    try:
        connection=mc.connect(host=host, password=password, user=user)
        print(connection)
        print("You have connected to your server succesfuly!")
    except mc.Error as e:
        print(e)

    return connection




