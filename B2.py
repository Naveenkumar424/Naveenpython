#implement selection Sort
a = [1,5,2,3,4]
for turn in range(len(a)):
    minPos = turn
    for inner in range(turn+1,len(a)):
        if(a[minPos] > a[inner]):
            minPos = inner
    a[minPos],a[turn] = a[turn],a[minPos]
print(a)
#end of code