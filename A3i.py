#find the sum of natural numbers using function
def natSum(n):
    ns = 0
    for i in range(n+1):
        ns += i
    return ns
#end of function
n = int(input("Enter a number:"))
print(f"The sum of {n} natural numbers is {natSum(n)}")
#end of code