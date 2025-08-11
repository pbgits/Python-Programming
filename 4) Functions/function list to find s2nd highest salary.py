def user():
    l=[]
    z=[]
    i=0
    while i<=10:
        a=int(input("Enter the Salary of 10 Employes"))
        l.append(a)
        i+=1
    print(l)
    l.sort()
    print(l)
    print(str(l[9])+" is the 2nd Highest Salary")
    

    

   

         
def main():
    user()

if __name__ == '__main__':
    main()
    
        
        
