#check if prime or not 
#if not ,display all those numbers which divides this number
n = int(input("Enter a number:"))
isp = True
for i in range(2,n):
    if(n%i == 0):
        print(i,end='\t')
        isp = False
print()
if(isp):
    print(f"{n} is prime.")
else:
    print(f"{n} is not prime and above numbers divide the given number.")
#end of code
