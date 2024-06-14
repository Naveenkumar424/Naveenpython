#sum of n even numbers iterative
n = int(input("Enter a number:"))
es = 0
for i in range(2,n*2+1,2):
    es += i
print("The sum of ",n," even numbers is ",es)
#end of code