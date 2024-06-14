#sum of n natural numbers iterative
n = int(input("Enter a number:"))
s = 0
for i in range(n+1):
    s += i
#end of for
print(f"The sum of {n} natural numbers is {s}")
#end of code