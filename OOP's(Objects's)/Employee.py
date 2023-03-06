class Employee:
	def  getempvalues(self):
		self.eno=int(input("Enter Employee Number:"))
		self.ename=input("Enter Employee Name:")
		self.sal=float(input("Enter Employee Salary:"))
		self.dsg=input("Enter Employee Designation:")
	def dispempvalues(self):
		print("\t{}\t{}\t{}\t{}".format(self.eno,self.ename,self.sal,self.dsg))
