def mysort(list):
    for i in range(len(list)-1):
        min=i
        for j in range(i,len(list)-1):
            if list[j]<list[min]:
                min=j
        temp=list[i]
        list[i]=list[min]
        list[min]=temp
    return list

list =[12,34,5,23,24,21]
slist=mysort(list)
print (slist)
