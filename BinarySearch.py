pos=-1
def search(lst,n):
    l = 0                               #   Lower bound set to zero (index value)
    u = len(lst)-1                      #   Upper bound set to highest index value of list
    while l <= u:                       #   Loop will continue till the lower and upper bound meets
        mid = (l+u)//2                  #   Mid integer value bet upper and lower bound is found
        if (lst[mid]==n):               #   Compare Mid value with value to be searched
            globals()['pos']=mid        #   If found, job is done
            return True
        else:                           #   Else find out whether value to be searched is higher or lower than mid value
            if n>lst[mid]:              #   If higher than mid value shift lower bound to mid value + 1
                l=mid+1
            else:
                u=mid-1                 #   If lower than mid value shift upper bound to mid value - 1
    return False
lst = [12,434,433,524,3223,552,662]
slst = sorted(lst)
print(slst)
n=int(input("Enter the number you want to search in the list"))
if (search(slst,n)):
    print ("Value found at the position ",pos+1)
else:
    print ("Value not found")