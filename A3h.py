#sum of n prime numbers
n = int(input("Enter a number:"))
ps = 0
pc = 0
pn = 0
while(pc<=n):
    isp=True
    for i in range(2,pn):
        if(pn%i == 0):
            isp = False
    if(isp):
        print(pn)
        pc += 1
        ps += pn
    pn += 1
#end of while
print(f"The sum of {n} prime numbers is {ps}")
#end of code