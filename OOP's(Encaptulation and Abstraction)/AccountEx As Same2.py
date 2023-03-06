class Account:
	def  __init__(self):
		self.__acno=1234
		self.cname="Rossum"
		self.__bal=45.78
		self.__pin=4321
		self.bname="SBI"
	def  __getaccess(self):
		print("\nAccount Number:{}".format(self.__acno)) #Possible to Access
		print("Account Holder Name:{}".format(self.cname))
		print("Account Balanace:{}".format(self.__bal))   #Possible to Access
		print("Account PIN:{}".format(self.__pin)) #Possible to Access
		print("Account Banch Name:{}".format(self.bname))
	def  getAccount(self):
		self.getaccess() # Calling Enacpsulated Instance Method from Other Instance Method of same class--Not Possible

#main program
ac=Account()
ac.getaccount()
