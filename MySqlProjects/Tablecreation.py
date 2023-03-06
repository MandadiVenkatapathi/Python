import mysql.connector
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                password="Venkat12345@",
                                database="batch6pm")
    cur=con.cursor()
    tq="create table student (sno int, sname varchar(10), marks  float , cname varchar(10)  ) "
    cur.execute(tq)
    print("Table created in MySQL--Verify")
except mysql.connector.DatabaseError as db:
	print("Problem in Database:",db)
