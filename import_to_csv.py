import csv
import mysql.connector as mc
import os.path

def import_to_csv(connection, csv_file_path):
    #filepath in secure_file_priv directory to allow import to file
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM titles')
            data = cursor.fetchall()
            with open(csv_file_path, 'w', newline='') as file:
                for row in data:
                    csv.writer(file, delimiter = ';').writerow(row)
        if(os.path.exists(csv_file_path)): return print("TABLE EXPORTED")
        else: print("Something went wrong! :(")

    except mc.Error as e:
        print(e)

