import mysql.connector
con=mysql.connector.connect(host="localhost",
													user="root",
													passwd="Venkat12345@")
cur=con.cursor()
print("type of cur=",type(cur))
print("Python Program created an object of cursor")