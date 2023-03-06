import mysql.connector 
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                               password="Venkat12345@")
cursor = mydb.cursor()
print("connection has been done", cursor)
