#sequential search on array of student names
n = int(input("How many students?"))
ls = []
print(f"Enter {n} names:")
for i in range(n):
    ls.append(input())
key = input("Enter name to search:")
f = False
for i in ls:
    if(i == key):
        f = True
if(f):
    print("Name found")
else:
    print("Name not found")
#end of code