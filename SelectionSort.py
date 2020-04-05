def mysort(lst):
    for i in range(len(lst)-1):
        min=i
        for j in range(i,len(lst)):
            if lst[j]<lst[min]:
                min=j

        temp=lst[i]
        lst[i]=lst[min]
        lst[min]=temp
    return lst
list=[235,34,12,53,23,63,43,24]
slist=mysort(list)
print (slist)