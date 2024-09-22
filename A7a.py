#read dob and display month
dob = input("Enter date of birth seperated by '-':")
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
d,m,y = dob.split('-')
print(f'He is born in the month {months[int(m)-1]}')
#end of code