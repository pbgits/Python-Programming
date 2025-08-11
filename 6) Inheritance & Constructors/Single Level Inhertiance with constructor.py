# Single Level Inheritance

class A: #parent class
    
    def __init__(self,x=0):
        self.number1=x
    def showData1(self):
        print("Number1 =",self.number1)

class B(A):
    def __init__(self,x=0,y=0):
        A.__init__(self,x) #call parent constructor in child class
        self.number2=y
    def showData2(self):
        print("Number2 =",self.number2)

def main():

    obj=B()
    obj.number1=int(input("Enter Number 1 "))
    obj.number2=int(input("Enter number 2 "))
    obj.showData1()
    obj.showData2()
if __name__=="__main__":
    main()

        
        
