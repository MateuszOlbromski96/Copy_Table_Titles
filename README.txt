-----------------------------------------------------------------------------------
[DATABASE SETUP]

MYSQL SERVER 5.0+ is required 

MySQL service must be running

Skipping the part from creating DATABASE employees with  employees.sql script,
there is GLOBAL VARIABLE to take care of, if using 'select * from titles'
statement and exporting all records to .csv as I did in my script.

max_allowed_packet variable determines the maximum size of packet (in bytes) that
MySQL can receive in one query. I've increased that value significantly, since my
packet included entire table in one querry.

-----------------------------------------------------------------------------------
[SCRIPT]


The script asks for 'host', 'username', 'password' to access server's database 
from which data from table 'titles' will be exported to csv file.

After succesful connection, list of databases on the server will be displayed.
Entering the DB name will be required as well as path to csv file which will be
created and loaded with titles table's data.
e.g. C:\...\titles.csv
Once the csv file is loaded, program will ask for 'host','username','password'
and 'database' to which data should be copied, after this the program closes.






RUN main.py from Copy_Table_Records folder











