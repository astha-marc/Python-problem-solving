num=int(input("Enter number:"))
max=0
digit=0
while(num>0):
    digit=num%10
    if(max<digit):
        max=digit
    num=num//10
print("Maximum number is:",max)