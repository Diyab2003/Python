limit=int(input("Enter the limit"))
n=[]
for i in range(1,limit+1):
    num=int(input("Enter a number"))
    n.append(num)
max=n[0]
for i in n:
    if (i>max):
        max=i
print(max)
            
