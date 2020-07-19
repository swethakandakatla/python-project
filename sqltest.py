import pyodbc
import pandas as pd

conn=pyodbc.connect("Driver = {SQL Server Native Client 11.0};"               
               "Server = Server_Name;"
               "Database = Database_Name;"
               "username = User_Name;"
               "password = User_Password;"
               "Trusted_Connection = yes;")
cursor=conn.cursor()
sql_query = pd.read_sql_query('SELECT * FROM TestDB.dbo.Person',conn)
cursor.execute("select * from employer")