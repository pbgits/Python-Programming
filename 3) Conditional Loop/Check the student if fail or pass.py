a=float(input("Enter the marks"))

if   a >= 0 and a < 35:
    print ("fail ")
    
elif a>=75:
    print("Student has Secured Distinction")

elif a>=60:
    print("Student has Secured first class")
    
elif a>=50:
    print("Student has Secured second class")
    
elif a >= 35:
    print("Student has passed the exam")  
else:
    print("Enter correct marks")
