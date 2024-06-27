def  fact(x):
    if(x==0):
        return 1
    elif(x>0):
        if(x==1):
            return x
        else:
            f=x*fact(x-1)
        return f
n=int(input("Enter a number"))
f=1
print("Factorial of",n,"is:",fact(n))
