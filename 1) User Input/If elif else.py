#To check the greatest Number
a=int(input("Enter No1"))
b=int(input("Enter No2"))
c=int(input("Enter No3"))

if a>b and a>c:
    print(str(a),"is greatest")
elif b>a and b>c:
    print(str(b),"is greatest")
elif c>b and c>a:
    print(str(c),"is greatest")