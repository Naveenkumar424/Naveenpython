#read dob and calculate age
from datetime import *
dob = input("Enter dob seperated by '-':")
d,m,y = dob.split('-')
cy = datetime.now().year
print("The age of the person is ",cy-int(y))
#end of code