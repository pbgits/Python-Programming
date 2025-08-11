#HOW TO DECLARE A FUNCTION
#def -- define
def sub(x,y):
    c=x-y
    return c

def add(x,y):
    s=x+y
    return s

while True:
    
    if __name__=='__main__':
        
        x=int(input("Enter number 1:")) # take number 1
        y=int(input("Enter number 2:")) # take number 2
        result1=add(x,y)
        result2=sub(x,y)
        print(f"Sum = {result1}")
        print(f"Sub = {result2}")
    
