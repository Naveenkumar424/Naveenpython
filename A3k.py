#sum of natural numbers between a given range using function
def natSum(sr,er):
    ns = 0
    for i in range(sr,er+1):
        print(i)
        ns += i
    return ns
#end of function
sr = int(input("Enter the start range:"))
er = int(input("Enter the end range:"))
print(f"The sum of natural numbers between {sr} and {er} is {natSum(sr,er)}")
#end of code