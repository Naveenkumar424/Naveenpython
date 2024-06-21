#Multiplication table between range in reverse
s = int(input("Enter start range"))
e = int(input("Enter end range"))
for i in range(s,e+1):
    for j in range(10,0,-1):
        print(i,"x",j,"=",i*j)
    print()
#end of code