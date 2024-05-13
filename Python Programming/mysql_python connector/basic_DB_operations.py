# -*- coding: utf-8 -*-
"""
Created on Mon May  8 15:27:03 2023

@author: cdacstaff
"""

import mysql.connector

# Create new table

cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
# cur.execute("""CREATE TABLE student( 
#             roll_no INT, 
#             subid varchar(10), 
#             marks INT);""")
cnx.commit()
cnx.close()


# Insert records
records=[[1,'sub1',34],
         [2,'sub1',30],
         [3,'sub1',23],
         [1,'sub2',23],
        [2,'sub2',26],
        [3,'sub2',30],
        [1,'sub3',30],
        [2,'sub3',30],
        [3,'sub3',27],
    ]



cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
for rno, sub, marks in records:
    query = "insert into student values(" +\
                str(rno)+","+\
                repr(sub) + ","+\
                str(marks)+");"
    print(query)
    cur.execute(query)

cnx.commit()
cnx.close()


# Select records and display them

cnx = mysql.connector.connect(user='root', 
                              password='root123',
                              host='127.0.0.1',
                              database='mytrial')
cur = cnx.cursor()
cur.execute("select * from student")

for row in cur:
    print(row)


cnx.close()


"""Another syntax"""
from mysql.connector import connect
""" Connect to mySQL server and create new data base"""
"""
with connect(host="localhost",user="root",password="root123") as connection:
    #        print(connection)
    #query="CREATE DATABASE mytrial;"
    #with connection.cursor() as cur:
    #    cur.execute(query)
    print("Successfully created a new database")
    query="SHOW DATABASES"
    with connection.cursor() as cur:
        cur.execute(query)
        for db in cur:
            print(db)
"""

""" Connecting to existing database and creating a table """
"""
with connect(host="localhost",user="root",
	password="root123", 
	database="mytrial") as connection:
    #print(connection)
    # Create Table
    query = "CREATE TABLE student( roll_no INT PRIMARY KEY, name varchar(10));"
    with connection.cursor() as cur:
        cur.execute(query)
    print("Successfully Created a table name student")
"""
""" Connect to Existing Database and insert records in existing table """
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Insert multiple records in a table
    query = "INSERT INTO student (roll_no,name) VALUES ( %s, %s );"
    student_records=[(1,"xyz"),(2,"pqr"),(3,"abhi")]
    with connection.cursor() as cur:
        cur.executemany(query,student_records)
        connection.commit()
    print("Successfully Inserted multiple student records")
"""
""" Connect to Existing Database and select records from existing table """
"""
with connect(host="localhost",user="root",password="root123", database="mytrial") as connection:
    #print(connection)
    # Select records and print them
    query = "select * from student;"
    with connection.cursor() as cur:
        cur.execute(query)
        for row in cur:
            print(row)
""" 



