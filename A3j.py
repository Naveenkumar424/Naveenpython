#sum of natural numbers between a given range
sr = int(input("Enter the start range:"))
er = int(input("Enter the end range:"))
ns = 0
for i in range(sr,er+1):
    print(i)
    ns += i
print(f"The sum of natural numbers between {sr} and {er} is {ns}")
#end of code