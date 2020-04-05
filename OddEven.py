def cnt(lst):
    even=0
    odd=0
    for i in lst:
        if (i%2==0):
            even=even+1
        else:
            odd=odd+1
    return (even,odd)

lst = []
n=int(input("Enter the number of elements"))
for i in range (0,n):
    ele=int(input())
    lst.append(ele)

even,odd=cnt(lst)
print ("Even ",even)
print ("Odd ",odd)


