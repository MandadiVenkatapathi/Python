import mysql.connector, sys


class Employee:
    def getempvalues(self):
        try:
            self.eno = int(input("Enter Employee Number:"))
            self.ename = input("Enter Employee Name:")
            self.sal = float(input("Enter Employee Salary:"))
            self.cname = input("Enter Employee Company Name:")
        except ValueError:
            print("Don't enter strs,ANV,symbols fo empno and salary:")
            sys.exit()

    def saveempdata(self):
        while (True):
            try:
                print("-" * 50)
                self.getempvalues()
                con = mysql.connector.connect(host="127.0.0.1",
                                              user="root",
                                              passwd="Venkat12345@",
                                              database="venkatdb")

                cur = con.cursor()
                # design the query and execute
                iq = "insert into employee values(%d,'%s',%f,'%s')"
                cur.execute(iq % (self.eno, self.ename, self.sal, self.cname))
                con.commit()
                print("-" * 50)
                print("\nEmployee Record Saved")
                print("-" * 50)
                ch = input("Do u want to insert another record(yes/no):")
                if (ch.lower() == "no"):
                    print("Thzx for using this program")
                    break
            except mysql.connector.DatabaseError as db:
                print("Prob in Database:", db)


# main program
e = Employee()
e.saveempdata()