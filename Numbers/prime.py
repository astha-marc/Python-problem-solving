num=int(input("Enter number:"))
flag=0
i=2
while(i<=num/2):
    if(num%i==0):
        flag=1
        break
    i=i+1
if(flag==0):
    print("It is prime number.")
else:
    print("It is not prime number.")

