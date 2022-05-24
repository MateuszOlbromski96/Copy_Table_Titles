import csv #reading and writing tabular data
import mysql.connector as mc #enables communication with server
import os.path # To verify writing data succeeds

#filepath in secure_file_priv directory to allow import to directory other than MySQL server's!

def import_to_csv(connection, csv_file_path):
    #Function fetches data from table using sql statement and writes to csv file
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM titles')
            data = cursor.fetchall()                           			#Assigning list of tuples to variable
            with open(csv_file_path, 'w', newline='') as file:                  #newline to ensure no blank rows in between happen
                for row in data:
                    csv.writer(file, delimiter = ';').writerow(row)             #writing data to csv file
        if(os.path.exists(csv_file_path)): return print("TABLE EXPORTED")       #checking if file exists
        else: print("Something went wrong!")

    except mc.Error as e:
        print(e)

