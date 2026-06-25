num=int(input("Enter number:"))
F1=1
F2=0
F3=0
i=1
while(i<=num):
    F3=F1+F2
    print(F3)
    F1=F2
    F2=F3
    i=i+1
