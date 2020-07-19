# Database Connection
# Before connecting to a MySQL database, make sure of the followings −

# You have created a database TESTDB.

# You have created a table EMPLOYEE in TESTDB.

# This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.

# User ID "testuser" and password "test123" are set to access TESTDB.

# Python module MySQLdb is installed properly on your machine.

# You have gone through MySQL tutorial to understand MySQL Basics.

# Example
# Following is the example of connecting with MySQL database "TESTDB"

#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

cursor.execute(sql)
cursor.execute(sql1)

try:
    db.commit()
except:
    db.rollback()
    #go back to the previous state in case of any error
   
finally:
     # disconnect from server
    db.close()

# reading data from database

    sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"


   # Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')

    # Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)