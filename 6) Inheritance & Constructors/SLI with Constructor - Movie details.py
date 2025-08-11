# movieCD as A
# songCD  as B

class CD:

    def __init__(self,t,m):
        self.title=t
        self.size=m
    def showCD(self):
        print("Title  :",self.title)
        print("Size   :",self.size)
    
class movieCD(CD):
    
    def __init__(self,t,m,a,g):
        CD.__init__(self,t,m)
        self.actor=a
        self.genre=g
    def showA(self):
        print("Actor  :",self.actor)
        print("Genre  :",self.genre)
    
        
class songCD(CD):

    def __init__(self,t,m,s,y):
        CD.__init__(self,t,m)
        self.singer=s
        self.year=y
    def showB(self):
        print("Singer :",self.singer)
        print("Year   :",self.year)

def main():
    
    m1=movieCD("ABC",20,"Actor","GEn")
    
    m2=songCD("XYZ",25,"singer",2002)

    """
    m1.title    =str    (input("Enter the Movie Name  "))
    m1.size     =float  (input("Enter the Movie Size  "))
    
    m1.actor    =str    (input("Enter the Actor  "))
    m1.genre    =str    (input("Enter the Genre  "))

    m2.title    =str    (input("Enter the Song  Name  "))
    m2.size     =float  (input("Enter the Song  Size  "))
    
    m2.singer   =str    (input("Enter the Singer "))
    m2.year     =int    (input("Enter the Year   "))
    """

    m1.showCD()
    m1.showA()
    m2.showCD()
    m2.showB()
    
if __name__=='__main__':
    main()

    
    
