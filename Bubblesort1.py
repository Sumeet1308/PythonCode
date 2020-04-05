def mysort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

list =[12,34,5,23,24,21]
slist=mysort(list)
print (slist)
