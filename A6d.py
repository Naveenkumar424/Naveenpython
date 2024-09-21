#read per and count number of distinction ,first class ,second class ,pass ,fail
n = int(input("How many students"))
ps = []
print(f"Enter percentage of {n} students:")
d,fc,sc,p,f = 0,0,0,0,0
for i in range(n):
    ps.append(input())
for i in ps:
    if(i > '85'):
        d += 1
    elif(i > '75'):
        fc += 1
    elif(i > '60'):
        sc += 1
    elif(i > '35'):
        p += 1
    else:
        f += 1
print(f"Number of students who obtained:\nDistinction\t:{d}\nFirst Class\t:{fc}\nSecond Class\t:{sc}\nPass\t\t:{p}\nFail\t\t:{f}")
#end of code