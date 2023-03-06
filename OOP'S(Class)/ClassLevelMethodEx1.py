#Program accepting student number,name and marks whose studing "OUCET"
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcollname(cls):
        cls.cname="ANUFET" #calss level member
    def readstudvalues(self):
        self.sno=int(input("Enter The Student Number:"))
        self.sname=input("Enter The Student name:")
        self.marks=float(input("Enter The Student Marks:"))
    def dispstudvalues(self):
        print("-"*50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.sname))
        print("Student Marks:{}".format(self.marks))
        print("Student College Name:{}".format(self.cname))
        print("-" * 50)

Student.getcollname() # calling Class Level Method w.r.t Class Name
s=Student() # creating an object of student class
s.readstudvalues()
s.dispstudvalues()


