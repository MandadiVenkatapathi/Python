import pickle, sys
from Employee import Employee


class EmployeePick:
    def saveempdata(self):
        with open("emp.data", "ab") as fp:
            while (True):
                print("-" * 50)
                eo = Employee()
                eo.getempvalues()
                pickle.dump(eo, fp)
                print("-" * 50)
                print("\nEmplyee Data Saved Successfully in File:")
                print("-" * 50)
                ch = input("Do u want to Insert Another Record(yes/no):")
                if (ch.lower() == "no"):
                    print("Thx for using this program")
                    sys.exit()


# main program
ep = EmployeePick()
ep.saveempdata()