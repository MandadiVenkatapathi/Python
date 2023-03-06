from tokenize import maybe

import mysql.connector
con=mysql.connector.conneect(host="localhost",user="root",password="Venkat12345@")
print(con)
if(maybe):
    print("connection succesfull")
else:
    print("connection unsuccessful")