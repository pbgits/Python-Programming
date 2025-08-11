class Circle:
    radius=0
   

    def getData(self,r):
        self.length=r
        
        
    def showData(self):
        print("Radius",self.radius)
        

    def showArea(self):
        area=3.17*self.radius**2
        print("Area of Circle={0:f}".format(area))

def main():
    
    c1=Circle()
    c1.radius=int(input("Enter the radius"))
    c1.showData()
    c1.showArea()

    
    

if __name__=='__main__':
    main()
        
