a=float(input("Enter the price"))
b=int(input("Enter the QTY"))



if b > 100:
    t = a * b
    d = t * 10 / 100
    f = t - d
    print (f)
else :
    t = a * b
    print (t)

    
