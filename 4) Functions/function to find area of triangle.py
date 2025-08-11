def area(a,b,c):
    s=(a+b+c)*0.5
    A=(s*(s-a)*(s-b)*(s-c))
    z=A**0.5
    return z
def main():
    print("--To find Area of Triangle--")
    print(">> Enter all sides of triangle in Cm")
    a=float(input(("Enter the 1st side:  ")))
    b=float(input(("Enter the 2nd side:  ")))
    c=float(input(("Enter the 3rd side:  ")))
    result=area(a,b,c)
    print("Area= {0:f}".format(result)+" Sq cm")
    
if __name__=='__main__':
    main()
