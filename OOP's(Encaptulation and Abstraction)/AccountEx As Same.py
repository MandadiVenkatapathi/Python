class Account:
    def __init__(self):
        self.__acno=1234567890
        self.cname="VenkataPathi"
        self.__pin=1234
        self.__bal=30000
        self.bname="BOB"
    def getacces(self):
        #print("\t Enter the account number:{}".format(self.acno)) Not Possible to Access
        print("\t Enter the Ac Holder name:{}".format(self.cname))
        #print("\t Enter the Ac pin:{}".format(self.pin)) Not Possible to Access
        #print("\t Enter the Ac Balence:{}".format(self.bal)) Not Possible to Access
        print("\t Enter the Branch name:{}".format(self.bname))

#Main Program
ac=Account()
ac.getacces()