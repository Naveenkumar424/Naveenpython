#sum of n odd numbers iterative
n = int(input("Enter a number:"))
os = 0
for i in range(1,n*2+1,2):
    os += i
print("The sum of ",n," odd numbers is ",os)
#end of code