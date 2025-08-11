#number divisible by 1 and itself

def prime(a):
    i=1
    ctr=0
    for i in range(1,a+1):
        if a%i==0:
            ctr+=1
    if ctr>2:
        print("Number is Not prime")
    else:
        print("Number is prime")
        
   
def main():
    a=int(input("Enter the Number"))
    prime(a)
if __name__=='__main__':
    main()

