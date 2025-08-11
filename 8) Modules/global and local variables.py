# Global Variable & Local Variable

x=10 #global variable


def show():
    global x
    #to access global variable use global keyword
    #x=5 #local variable
    
    
    print("x = ",x)
show()
