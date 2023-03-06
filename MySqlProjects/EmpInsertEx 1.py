import  mysql.connector
def  emprecordinsert():
	while(True):
		try:
			con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="Venkat12345@",
														database="batch6pm" )
			cur=con.cursor()
			#accept employee values from KBD
			print("-"*50)
			empno=int(input("Enter Employee Number:"))
			ename=input("Enter Employee Name:")
			sal=float(input("Enter Employee Salary:"))
			cname=input("Enter Employee Company Name:")
			#prepare query and execute
			iq="insert into employee values (%d,'%s',%f,'%s') "
			cur.execute(iq  %(empno,ename,sal,cname))
			#OR
			#cur.execute("insert into employee values (%d,'%s',%f,'%s')" %(empno,ename,sal,cname))
			con.commit()
			print("-"*50)
			print("{} Emplyee Record Inserted:".format(cur.rowcount))
			print("-"*50)
			ch=input("Do u want to insert another employee record(yes/no):")
			if(ch=="no"):
				break
		except mysql.connector.DatabaseError as db:
			print("Problem in Database:",db)
		except ValueError:
			print("Don't enter strs, symbols and alpha-numerics for Empno, Salary:")


#main program
emprecordinsert()