#sum of n natural numbers recursive
def natSum(n):
    if(n == 0):
        return 0
    return n+natSum(n-1)
#end of fun
n = int(input("Enter a number:"))
print(f"The sum of {n} natural numbers is {natSum(n)}")
#end of code