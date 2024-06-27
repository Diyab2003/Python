num=int(input("Enter a number"))
total=0
for value in range(1,num+1):
    total=total+value
print("Factors are:")
for i in range(1,num+1):
    if(num%i==0):
        print(i)
    
    
