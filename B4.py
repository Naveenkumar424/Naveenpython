#use of dictionaries
n = int(input("How many pairs of values do you wish to read?"))
print(f"Enter {n} key value pairs:")
d = {}
for i in range(n):
    key = input("Enter Key:")
    value = input("Enter value:")
    d.update({key:value})
for key,value in d.items():
    print(key," = ",value)
#end of code
