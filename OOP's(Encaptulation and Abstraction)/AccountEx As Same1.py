class Account:
    def __init__(self):
        self.__acno=1234567890
        self.cname="Venkat"
        self.__pin=1234
        self.__bal=30000
        self.bname="BOB"
    def getacces(self):
        print("\t Enter the account number:{}".format(self.__acno)) # Possible to Access
        print("\t Enter the Ac Holder name:{}".format(self.cname))
        print("\t Enter the Ac pin:{}".format(self.__pin))# Possible to Access
        print("\t Enter the Ac Balence:{}".format(self.__bal))# Possible to Access
        print("\t Enter the Branch name:{}".format(self.bname))

#Main Program
ac=Account()
ac.getacces()