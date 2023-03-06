pa,r,t=float(input("Enter the princple amont:")),float(input("Enter the rate of interest:")),int(input("Enter the Time of months:"))
Si=(pa*r*t)/100
Ta=pa+Si
print("&"*50)
print("\tSimple interest of given ledger={}".format(Si))
print("\tTotal Amount of {} and {}={}".format(pa,Si,Ta))
print("&"*50)
