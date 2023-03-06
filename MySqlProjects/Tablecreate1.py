import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="Venkat12345@",
                                database="batch6pm")
    cur=con.cursor()
    tq="create table employee (empno int, ename varchar(10), esal  float , cname varchar(10)  ) "
    cur.execute(tq)
    print("Table created in MySQL--Verify")
except mysql.connector.DatabaseError as db:
	print("Problem in Database:",db)