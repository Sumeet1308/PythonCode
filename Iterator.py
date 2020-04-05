def gen():
    i=1
    while i<=10:
        j=i*i
        yield j
        i=i+1

i=gen()
for j in i:
    print (j)