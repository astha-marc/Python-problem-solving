num=int(input("Enter number:"))
sum=0
digit=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of digits:",sum)