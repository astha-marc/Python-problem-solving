num=int(input("Enter number:"))
flag=0
digit=0
while(num>0):
    digit=num%10
    if(digit>=8):
        flag=1
    num=num//10
if(flag==0):
    print("It is octal number")
else:
    print("It is not octal number")