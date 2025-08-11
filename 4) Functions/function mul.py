def mul(x,y):
    s=x*y
    return s
def main():
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    result=mul(x,y)
    print("Multiplication={0:d}".format(result))
    
if __name__=='__main__':
    main()
