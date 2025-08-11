class car:
    Company=""
    FuelType=""
    Colour=""
    Seater=0
    
    def getData(self,c,f,cr,s):
        self.Company=c
        self.FuelType=f
        self.Colour=cr
        self.Seater=s   
        
    def showData(self):
        print("Comapny        :: ",self.Company)
        print("FuelType       :: ",self.FuelType)
        print("Colour         :: ",self.Colour)
        print("Seater         :: ",self.Seater)    

def main():
    
    c1=car()
    print("Enter the details of the Car")
    print("_____________________________")
    print("")
    print("SUZUKI, HONDA, HYUNDAI, MAHINDRA")
    c1.Company=  str(input("Enter the Company Name     ::- "))
    print("----------------")
    print("CNG, PETROL, DIESEL, HYBRID")
    c1.FuelType= str(input("Enter the FuelType         ::- "))
    print("----------------")
    print("BLACK, WHITE, GREY, RED")
    c1.Colour=   str(input("Enter the Colour           ::- "))
    print("----------------")
    print("1] 2+2, 2] 2+3, 3] 2+4")
    c1.Seater=   int(input("Enter the Seater           ::- "))
    print("----------------")
    print("")
    print("_____________________________")
    c1.showData()
    
    

if __name__=='__main__':
    main()
        
