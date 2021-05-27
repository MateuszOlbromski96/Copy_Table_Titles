import csv
import mysql.connector as mc


def import_from_csv_to_table(connection, csv_file_path):
    #deletes data from table titles if database employees_copy is being used
    #imports list of tuplets from csv and inserts into database's table
    try:
        with connection.cursor() as cursor:
            if cursor.execute('SELECT COUNT(emp_no) FROM titles'):
                cursor.execute("DELETE FROM titles")
                connection.commit()
            else:
                with open(csv_file_path, 'r') as file:
                    data = []
                    csv_file = csv.reader(file, delimiter = ';')
                    for row in csv_file:
                        record = (row[0], row[1], row[2], row[3])
                        data.append(record)
            sql_insert_query = "INSERT INTO titles VALUES (%s,%s,%s,%s)"
            cursor.executemany(sql_insert_query,data)
            connection.commit()
    except mc.Error as e:
        print(e)
    return print("Table copied successfully!")

