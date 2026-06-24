num=int(input("Enter number:"))
flag=0
while(num>0):
    digit=num%10
    if(digit>=2):
        flag=1
        break
    num=num//10
if(flag==0):
    print("It is binary number.")
else:
    print("It is not binary number.")
