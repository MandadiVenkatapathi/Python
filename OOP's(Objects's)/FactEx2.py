class Fact:
    def readvalues(self):
        try:
            self.n = int(input("Enter Value of n:"))
            self.calfactorial()
        except ValueError:
            print("Don't Enter strs, symbols and ANV")

    def calfactorial(self):
        if (self.n < 0):
            print("{} is invalid".format(self.n))
        else:
            f = 1
            for i in range(1, self.n + 1):
                f = f * i
            else:
                print("Factorial({})={}".format(self.n, f))