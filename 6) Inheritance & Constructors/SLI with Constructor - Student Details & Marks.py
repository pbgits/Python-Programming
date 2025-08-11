#single level inheritance
#student details & student marks example
#student details as A
#student marks   as B
#any comment

#define a class (parent)
class A:
    


    def __init__(self,r=0,n=""):
        self.roll_no=r
        self.name=n
    def showData1(self):
        print("-----------------")
        print("Name    ::",self.name)
        print("Roll No ::",self.roll_no)


class B(A):

    def __init__(self,e=0,m=0):
        
        self.eng=e
        self.math=m

    def showData2(self):
        print("English ::",self.eng)
        print("Maths   ::",self.math)
        print("-----------------")

def main():

    obj=B()
    obj.name    =str(input("Enter the Name          :"))
    obj.roll_no =int(input("Enter the Roll No       :"))
    obj.eng     =int(input("Enter the English Marks :"))
    obj.math    =int(input("Enter the Maths Marks   :"))
    obj.showData1()
    obj.showData2()
if __name__=='__main__':
    main()
    
