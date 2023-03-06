import pickle
class EmployeUnPick:
	def  reademprecord(self):
		try:
			with open("emp.data","rb") as fp:
				print("-"*50)
				print("\tEmpno\tName\tSal\tDesg")
				print("-"*50)
				while(True):
					try:
						obj=pickle.load(fp)  # here obj is of type <class 'Emp.Employee'>
						obj.dispempvalues()
					except EOFError:
						print("-"*50)
						break
		except FileNotFoundError:
			print("File does not exist:")

#main program
epk=EmployeUnPick()
epk.reademprecord()