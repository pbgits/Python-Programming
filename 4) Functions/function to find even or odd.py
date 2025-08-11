def answer(a):
    if a%2==0:
        print ("Number is Even")
    else:
        print ("Number is Odd" ) 
    
    
def main():
    a=int(input("Enter the number"))
    answer(a)
    
    
if __name__=='__main__':
    main()
