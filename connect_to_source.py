import mysql.connector as mc

def connect_to_source(host,user,password):
    try:
        with mc.connect(host=host, password=password, user=user) as connection:
            print("You have connected to server succesfuly!")
            with connection.cursor() as cursor:
                cursor.execute("SHOW DATABASES")
                for db in cursor:
                    print(db)
                database = input("Select Database to copy from: ")
            connection = mc.connect(host=host, password=password, user=user, database=database)
    except mc.Error as e:
        print(e)

    return connection




