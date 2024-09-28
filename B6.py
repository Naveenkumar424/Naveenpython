#dictionary use
a = dict()
n = int(input("how many elements?"))
for i in range(n):
    key = input("Enter Key:")
    value = input("Enter value:")
    a.update({key:value})
for key,value in a.items():
    print(f"{key} = {value}")
#end of code