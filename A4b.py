#multiplication table between a given range
s = int(input("Enter start range:"))
e = int(input("Enter end range:"))
for i in range(s,e+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()
#end of code