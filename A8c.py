#writeing to a text file
name = input("Enter Name:")
dept = input("Enter Department:")
desg = input("Enter Designation:")
sal = input("Enter Salary:")
ls = [name,dept,desg,sal]
fp = open("Emp.txt","w")
fp.write(str(ls))
#end of code