#Sum of n fibonacci numbers
f0 = 0
f1 = 1
n = int(input("Enter a number:"))
fs = 0
fc = 0
while(fc<n):
    fs += f1
    f2 = f0+f1
    f0 = f1
    f1 = f2
    fc += 1
print(f"The sum of {n} fibonacci numbers is {fs}")
#end of code