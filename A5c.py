#check if a number is prime or not usinf=g function
#if prime generate remaining prime numbers using another function
def isp(n):
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True
#end of function
def gp(n):
    for i in range(1,n):
        if(isp(i)):
            print(i,end='\t')
#end of gp
#main
n = int(input("Enter a number:"))
if(isp(n)):
    print(f"{n} is prime.")
    print(f"Prime numbers till {n} are:")
    gp(n)
else:
    print(f"{n} is not prime.")
#end of code