num=int(input("Enter number:"))
sum=0
mul=1
while(num>0):
    digit=num%10
    sum=sum+digit
    mul=mul*digit
    num=num//10
if(sum==mul):
    print("It is a spy number.")
else:
    print("It is not a spy number.")