def fact(n):
    fct = 1
    for i in range(n,1,-1):
        fct = fct*i
    return fct
if (__name__=="__main__"):
    x=fact(6)
    print(x)