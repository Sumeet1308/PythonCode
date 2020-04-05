def mysort(lst):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if (lst[j]>lst[j+1]):
                temp=lst[j+1]
                lst[j+1]=lst[j]
                lst[j]=temp
    return lst
list=[235,34,12,53,23,63,43,24]
slist=mysort(list)
print (slist)