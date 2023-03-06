class Sum:
	def readvalues(self):
		self.a=float(input("Enter First Value:"))
		self.b=float(input("Enter Second Value:"))
	def addvalues(self):
		self.c=self.a+self.b
	def  dispvalues(self):
		self.readvalues()
		self.addvalues()
		print("sum({},{})={}".format(self.a,self.b,self.c))

#main program
s1=Sum()
s1.dispvalues()