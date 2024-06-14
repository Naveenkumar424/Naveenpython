#sum of n even numbers recursive
def evSum(n):
    if(n == 0):
        return 0
    return n+evSum(n-2)
#end of fun
n = int(input("Enter a numbers:"))
print("The sum of ",n," even numbers is ",evSum(n*2))
#end of code