str=input("Enter the string")
for i in range(0,int((len(str)-1)/2)):
    j=len(str)-1-i
    if (str[i]!=str[j]):
        print("Not a pallindrom")
        break
else:
    print("Pallindrom")
