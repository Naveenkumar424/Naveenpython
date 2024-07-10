#Cheack if a given number is prime of not
n = int(input("Enter a nmber:"))
isp = True
for i in range(2,n):
    if(n%i == 0):
        isp = False
if(isp):
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime.")
#end of code