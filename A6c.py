#sequential search on array of floats
n = int(input("How many floating point values?"))
lf = []
print(f"Enter {n} floating point values:")
for i in range(n):
    lf.append(input())
key = input("Enter element to search:")
f = False
for i in lf:
    if(i == key):
        f = True
if(f):
    print("Element found")
else:
    print("Element not found")
#end of code
