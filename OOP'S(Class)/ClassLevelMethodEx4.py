#Program accepting student number,name and marks whose studing "OUCET"
#ClassLevelMethodEx4.py
class Student:
	@classmethod
	def getcollname(cls):
		cls.cname="OUCET"  # Class Level Data Member
		cls.getcolladdr() # Calling Class Level Method w.r.t cls
	@classmethod
	def getcolladdr(cls):
		Student.caddr="HYD"  # Class Level Data Member

	def  readstudvalues(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.marks=float(input("Enter Student Marks:"))
	def  dispstudvalues(self):
		self.getcollname()  # calling Class Level Method  w.r.t self
		print("-"*50)
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Marks:{}".format(self.marks))
		print("Student College Name:{}".format(Student.cname))
		print("Student College Address:{}".format(Student.caddr))
		print("-"*50)

#main program
s=Student()  # creating an object of student class
s.readstudvalues()
s.dispstudvalues()