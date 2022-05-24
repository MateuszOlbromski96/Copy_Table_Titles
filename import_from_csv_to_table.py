import csv
import mysql.connector as mc

# Filepath in secure_file_priv directory to allow import to directory other than MySQL server's!

def import_from_csv_to_table(connection, csv_file_path):

    # Deletes data from table titles if database employees_copy is being used
    # Imports list of tuplets from csv and inserts into database's table

    try:
        with connection.cursor() as cursor:
            # Checking if the table in targeted DB isn't empty, if so deleting all records
            if cursor.execute('SELECT COUNT(emp_no) FROM titles'):
                cursor.execute("DELETE FROM titles")
                connection.commit()
            # If table is empty, opening csv file and reading data
            else:
                with open(csv_file_path, 'r') as file:
                    data = []                                            # Creating empty list
                    csv_file = csv.reader(file, delimiter = ';')         # Reading data
                    for row in csv_file:
                        record = (row[0], row[1], row[2], row[3])        # Assembling columns values into tuple
                        data.append(record)                              # Inserting tuples to the list

            sql_insert_query = "INSERT INTO titles VALUES (%s,%s,%s,%s)" # SQL query
            cursor.executemany(sql_insert_query,data)                    # Executing sql query with given data
            connection.commit()                                          # Sending commit statement to server
    except mc.Error as e:
        print(e)

    # Returning row's count to compare it with the source DB's table
    return len(data)

