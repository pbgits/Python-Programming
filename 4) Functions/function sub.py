def sub(x,y):
    s=x-y
    return s
def main():
    x=int(input("Enter number 1:"))
    y=int(input("Enter number 2:"))
    result=sub(x,y)
    print("Subtraction={0:d}".format(result))
    
if __name__=='__main__':
    main()
