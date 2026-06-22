num=int(input("Enter number:"))
sum=0
i=1
while(num>i):
    if(num%i==0):
        sum=sum+i
    i=i+1
if(sum==num):
    print("It is perfect number")
else:
    print("It is not a perfect number.")
