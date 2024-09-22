#read uucms numbers and count the number of students in each stream
n = int(input("How many students?"))
u = []
print(f"Enter {n} uucms numbers:")
for i in range(n):
    u.append(input())
s,c,a = 0,0,0
for i in u:
    if(i[7] == 'S'):
        s += 1
    elif(i[7] == 'C'):
        c += 1
    elif(i[7] == 'A'):
        a += 1
print(f"Number of students in:\nScience\t:{s}\nCommerce:{c}\nArts\t:{a}")
#end of code