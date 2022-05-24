import mysql.connector as mc

#Function connects with server, prints list of existing databases and asks for choosing one. Returns connection object

def connect_to_source(host,user,password):
    try:
        with mc.connect(host=host, password=password, user=user) as connection:
            print("You have connected to server successfully!")
            with connection.cursor() as cursor: #Cursor object to communicate with database
                cursor.execute("SHOW DATABASES")

                for db in cursor:       #printing dbs list
                    print(db)
                database = input("Select Database to copy from: ")
            connection = mc.connect(host=host, password=password, user=user, database=database)
    except mc.Error as e:
        print(e)

    return connection #returning connection object with chosen database




