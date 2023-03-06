#TestMySqlcon.py
import mysql.connector
con=mysql.connector.connect(host="localhost",
							user="root",
							passwd="Venkat12345@")
print("type of con=",type(con))
print("Python got connection from MySQL")