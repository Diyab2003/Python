lim=int(input("Enter limit"))
num=[]
even=[]
odd=[]
for i in range(1,lim+1):
    x=int(input("Enter a number"))
    num.append(x)
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Odd numbers:",odd)
print("Even numbers:",even)
