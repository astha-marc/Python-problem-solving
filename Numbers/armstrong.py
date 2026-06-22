num=int(input("Enter number:"))
sum=0
digit=0
temp=num
while(num>0):
    digit=num%10
    sum=sum+digit*digit*digit
    num=num//10
if(temp==sum):
    print("It is armstrong number.")
else:
    print("It is not armstrong number")