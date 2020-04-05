def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d
def pattern(x,y):
    i=1
    for i in range(y+1):
        j=1
        for j in range (i):
            print (x," ",end="")
        print ("\n")

pattern('PQR',7)


add,sub=add_sub(10,5)
print ("The addition is ",add)
print ("The subtraction is ",sub)