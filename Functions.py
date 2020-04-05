def lstfun():
    lst = [12, 34, 5, 34, 34]
    x = calc(lst)
    print (x)

def calc(lst):
    j=0;
    for i in lst:
        j=j+i
    return j

lstfun()