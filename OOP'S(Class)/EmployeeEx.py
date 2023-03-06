#Program for storing Employee Details such as empno,ename and sal and cname by using classes and objects
# (Instance Method)
class Employee:
	cname="IBM" # Class Level Data Member
	def  readempvalues(self):
		print("\nAddress of current =",id(self))
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))
	def dispempdata(self):
		print("\nAddress of current =",id(self))
		print("Employee Number:{}".format(self.eno))
		print("Employee Name:{}".format(self.ename))
		print("Employee Salary:{}".format(self.sal))
		print("Employee Company Name:{}".format(self.cname))


#main program
e1=Employee()
print("Id of e1 in main program=",id(e1))
#read the data for e1 object
e1.readempvalues()  # Function Call
e2=Employee()
print("Id of e2 in main program=",id(e2))
#read the data for e2 object
e2.readempvalues()  # Function Call
print("-"*50)
print("First Emplyee  Object Data:")
print("-"*50)
e1.dispempdata()
print("-"*50)
print("Second Emplyee  Object Data:")
print("-"*50)
e2.dispempdata()
print("-"*50)