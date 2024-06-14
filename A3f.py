#sum of n odd numbers recursive
def odSum(n):
    if(n == 1):
        return 1
    return n+odSum(n-2)
#end of fun
n = int(input("Enter a numbers:"))
print("The sum of ",n," odd numbers is ",odSum(n*2-1))
#end of code