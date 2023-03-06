class Sum:
	def readvalues(self):
		self.a=float(input("Enter First Value:"))
		self.b=float(input("Enter Second Value:"))
	def addvalues(self):
		self.c=self.a+self.b
	def  dispvalues(self):
		print("sum({},{})={}".format(self.a,self.b,self.c))

#main program
s1=Sum()
s1.readvalues()
s1.addvalues()
s1.dispvalues()