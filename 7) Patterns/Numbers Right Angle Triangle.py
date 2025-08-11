i=1
j=1
a=1
for i in range(1,5):
    #a=1
    for j in range(1,i+1):
        print(a,end="")
        a+=1
    # ending line after each row
    print("\r")
