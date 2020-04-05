a=10
b="b"
try:
    x=a/b
    print (x)
except ZeroDivisionError as e:
    x=a
    print (x)
    print ("You can not divide by zero so divided by 1")
except Exception as e:
    print ("Unexpected fatal error :",e)
finally :
    print ("Bye")