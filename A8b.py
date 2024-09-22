#read file calculate marks and display in good looking format
fp = open("marks.txt","r")
l = fp.read().splitlines()
ls = []
for i in l:
    ls.append(i.split(','))
for i in ls:
    i.append(int(i[2])+int(i[3])+int(i[4]))
    i.append(round(i[5]/180*100,2))
    if(i[6] > 85):
        i.append("Distinction")
    elif(i[6] > 75):
        i.append("First Class")
    elif(i[6] > 60):
        i.append("Second Class")
    elif(i[6] > 35):
        i.append("Pass")
    else:
        i.append("Fail")
print("Name\tRegno\t\tSub1\tSub2\tSub3\tTotal\tPer\tGrade")
for i in ls:
    for j in i:
        print(j,end = '\t')
    print()
#end of code