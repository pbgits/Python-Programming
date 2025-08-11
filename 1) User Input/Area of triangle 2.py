a=float(input("1st side"))
b=float(input("2nd side"))
c=float(input("3rd side"))
s=(a+b+c)*0.5
A=(s*(s-a)*(s-b)*(s-c))
Area=A**0.5
print("Area of Triangle"+str(Area))


