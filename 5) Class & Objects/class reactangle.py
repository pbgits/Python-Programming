class Reactangle:
    length=0
    breadth=0

    def getData(self,l,b):
        self.length=l
        self.breadth=b
        
    def showData(self):
        print("length",self.length)
        print("breadth",self.breadth)

    def showArea(self):
        area=self.length+self.breadth
        print("Area of Rectangle={0:d}".format(area))

def main():
    
    r1=Reactangle()
    r1.length=int(input("Enter the length"))
    r1.breadth=int(input("Enter the breadth"))
    r1.showData()
    r1.showArea()

    r2=Reactangle()
    r2.getData(200,100)
    r2.showData()
    r2.showArea()
    

if __name__=='__main__':
    main()
        
