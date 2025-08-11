class student:
    name=""
    rollno=0
    std=0
    
   

    def getData(self,n,r,s):
        self.name=n
        self.rollno=r
        self.std=s
        
        
    def showData(self):
        print("-----------------------")
        print("Name        :: ",self.name)
        print("Roll No     :: ",self.rollno)
        print("Standard    :: ",self.std)
        print("-----------------------")
        

def main():
    
    c1=student()
    print("Student 1 data")
    print("___________________")
    c1.name=  str(input("Enter the Name     ::- "))
    c1.rollno=int(input("Enter the Roll No  ::- "))
    c1.std=   int(input("Enter the Standard ::- "))
    print("___________________")
    c1.showData()

    c2=student()
    print("Student 2 data")
    print("___________________")
    c2.name=  str(input("Enter the Name     ::- "))
    c2.rollno=int(input("Enter the Roll No  ::- "))
    c2.std=   int(input("Enter the Standard ::- "))
    print("___________________")
    c2.showData()

    
    

if __name__=='__main__':
    main()
        
