#sequential search on array of integers
from array import *
n = int(input("How many numbers?"))
print(f"Enter {n} numbers")
a = array("i",[])
for i in range(n):
    a.append(int(input()))
key = int(input("Enter element to search:"))
f = False
for i in a:
    if(i == key):
        f = True
if(f):
    print("Element found")
else:
    print("Element not found")
#end of code