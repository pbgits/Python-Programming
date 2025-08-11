
# Constructor __init__()
class Rectangle:


    def __init__(self,l=0,b=0):
        self.length=l
        self.breadth=b


        
    def showData(self):
        print("Length  : ",self.length)
        print("Breadth : ",self.breadth)
        
r1=Rectangle()
r1.length= int(input("Enter Length :"))
r1.breadth=int(input("Enter Breadth:"))
r1.showData()
        
        
    
