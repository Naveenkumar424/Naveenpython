#sort a given list of names using one of the standard sorting techniques
nn = int(input("How many names?"))
n = []
print(f"Enter {nn} names:")
for i in range(nn):
    n.append(input())
#selection sort 
for turn in range(len(n)):
    for inner in range(len(n)-turn-1):
        if(n[inner] > n[inner+1]):
            n[inner+1],n[inner] = n[inner],n[inner+1]
print(n)
#end of code