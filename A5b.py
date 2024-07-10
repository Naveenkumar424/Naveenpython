#check if a number is prime or not
#if prime ,generate the remaining numbers upto that number
#check prime using a function
def isp(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True
#end of function
#main
n = int(input("Enter a number:"))
if(isp(n)):
    print(f"{n} is prime and prime numbers upto {n} are:")
    for i in range(1,n):
        if(isp(i)):
            print(i,end = '\t')
else:
    print(f"{n} is not prime.")
#end of code