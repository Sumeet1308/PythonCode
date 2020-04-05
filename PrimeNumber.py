for i in range(2,50):
    x = int(i/2)
    for j in range (2,x):
        if (i%j==0):
            break
    else:
        print (i)
