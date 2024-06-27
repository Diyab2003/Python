def primeno(n):
    flag=0
    for value in range(2,n):
        if(n%value==0):
            return(1)
    return (0)


x=int(input("Enter a number"))
flag=primeno(x)
if(flag==0):
    print("Prime number")
else:
    print("Not a prime number")
